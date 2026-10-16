"""200 hp member re-costed on MANUFACTURING envelope v1 (AER-3329).

Replaces the phase-1 cost lines that envelope v1 section 9.7 re-estimates
(first-op, castings, crank, liners, normalizing, machine shop) for concept H,
for H with MANUFACTURING's two largest DFM levers taken (envelope 9.5 items 1
and 4: bank block merged into the case half, head made a 4-axis part), and
for concept A, so the H-over-A pick can be checked on the same basis. Every
other line is the phase-0 line item, unchanged (`../engine_phase0/cost_floor.py`).

Two cost bases, because R-35's "first article" has two readings (AER-3330):

  builder  each engine of a batch of 5, first-op NRE (CAM programs and
           fixtures) paid once by the program and carried as its own line
  first    the very first engine, carrying every CAM program and fixture

All v1 lines are [E] (MANUFACTURING's bottom-up estimate on [S] rates), not
[Q]: there is no STEP geometry and no RFQ yet (envelope 9.6). Concept A's
casting envelopes are PROPULSION's [E], scaled from H's (see A_PARTS).

Run: python3 cost_v1.py
"""
import copy
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


HQ = load("h_quote_estimate")
M2 = load("member_200")
CF = M2.CF
add = HQ.add

# ---------------------------------------------------------------- castings
H_PARTS = HQ.PARTS

# H with envelope 9.5 item 1 (block merged into each case half) and item 4
# (head setup B on a 4-axis machine). Merged half: 560 x 300 x 325 mm with a
# jacket core; +1.0-1.5 h of setup-B cycle and the deck/register program
# (MANUFACTURING 9.5); CAM and fixture grow by the block's share [E].
_case = copy.deepcopy(H_PARTS["case half (pair = 2 part numbers)"])
_case.update(cam_h=(18, 32), fixture=(1000, 2500), inspect_h=(2.0, 3.5),
             box_mm=(560, 300, 325), core_frac=(0.15, 0.35))
_case["setups"] = [_case["setups"][0], (HQ.RATE_HMC, (1.0, 1.5), (3.5, 5.0))]
_head = copy.deepcopy(H_PARTS["bank head (mirrored L/R, 2 part numbers)"])
_head["setups"][1] = (HQ.RATE_4AX, (1.0, 2.0), (2.5, 4.0))
H_DFM_PARTS = {"case half with integral bank (2 part numbers)": _case,
               "bank head, 4-axis (mirrored L/R, 2 part numbers)": _head}


def scaled(p, box, hours, n=None, pn=None):
    q = copy.deepcopy(p)
    q["box_mm"] = box
    q["cam_h"] = tuple(h * hours for h in q["cam_h"])
    q["setups"] = [(r, s, tuple(c * hours for c in cy)) for r, s, cy in q["setups"]]
    if n is not None:
        q["n_per_engine"] = n
    if pn is not None:
        q["part_numbers"] = pn
    return q


# Concept A, flat-4, 130.2 mm bore (Lycoming 540 cylinder): PROPOSED [E]
# envelopes. Case half shorter and deeper than H's (two throws fewer, larger
# bore); block carries 2 liners not 3; one head per cylinder, one part number
# for all four (Lycoming practice), still a 5-axis part as drawn.
A_PARTS = {
    "case half": scaled(H_PARTS["case half (pair = 2 part numbers)"], (480, 330, 180), 0.9),
    "2-cylinder bank block (L = R)": scaled(H_PARTS["cylinder-bank block (L = R, 1 part number)"], (330, 200, 190), 0.8),
    "cylinder head (1 part number)": scaled(H_PARTS["bank head (mirrored L/R, 2 part numbers)"], (220, 190, 130), 0.6, n=4, pn=1),
}


def castings_line(parts, basis):
    """(first-op, castings, program NRE) per engine, each a (low, high) pair."""
    n_cast = sum(p["n_per_engine"] for p in parts.values())
    fo, ca, nre_t = (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)
    for p in parts.values():
        n, pn = p["n_per_engine"], p["part_numbers"]
        _, _, nre = HQ.first_op(p, 1)
        nre_t = add(nre_t, nre, pn)
        if basis == "first":
            _, marg, _ = HQ.first_op(p, n / pn)
            fo = add(fo, add((nre[0] * pn, nre[1] * pn), marg, n))
            c, _ = HQ.casting(p, 1, 1 / n_cast)
        else:
            _, marg, _ = HQ.first_op(p, 5 * n / pn)
            fo = add(fo, marg, n)
            c, _ = HQ.casting(p, 5, 1 / 15)
        ca = add(ca, c, n)
    return fo, ca, nre_t


# ---------------------------------------------------------------- other v1 lines
CRANK_H = (6300 + 300, 9000 + 400)   # [E MFG 9.4] one-off flat-6 billet + balance
LINER_PER_CYL = (300, 450)           # [E MFG 9.4] Darton MID share incl. bore/hone
NORM_TURBO = (2000, 4500)            # [MFG 10] turbo, gate control, lines, intercooler
DECK = (125 * 1.3, 285 * 1.3)        # [S-MFG 2.1] one deck, x1.3 for 2026; the block decks move into first-op
DAMPER = (400, 1500)                 # crank pendulum damper, as member_200.cost_200
# Darton MID sleeve 2.5-3 kg each [E MFG 9.4]; net of the aluminium it
# displaces in the block (density ratio 2.7/7.2): +0.625 x gross [E].
LINER_KG_NET = (6 * 2.5 * (1 - 2.7 / 7.2), 6 * 3.0 * (1 - 2.7 / 7.2))
# Concept A's Lycoming 540-bore pistons, priced: Aircraft Spruce lists
# 5.125 in Lycoming pistons at $460-639 each (read 2026-10-16) [S], against the
# LS-class Wiseco forged piston the catalog set already carries, $155-280
# (envelope 4) [S]. Premium per cylinder = $460-280 to $639-155. Rings not
# included (the Lycoming ring is priced per ring, $60-184 [S]), so this is low.
A_PISTON_PREMIUM = (460 - 280, 639 - 155)


def cost(concept, basis, parts=None, a_pistons_priced=False):
    """Line items for the 200 hp member; returns (dict of lines, program NRE)."""
    c = M2.COST_P1[concept]
    n = c["n"][1]
    L = {}
    L["catalog set per cylinder"] = (CF.PER_CYL["SI"][0] * n, CF.PER_CYL["SI"][1] * n)
    L["second ignition lane"] = (CF.DUAL_LANE_PER_CYL[0] * n, CF.DUAL_LANE_PER_CYL[1] * n)
    L["seats and guides"] = (CF.SEATS_GUIDES_PER_CYL[0] * n, CF.SEATS_GUIDES_PER_CYL[1] * n)
    L["liners incl. bore/hone [v1]"] = (LINER_PER_CYL[0] * n, LINER_PER_CYL[1] * n)
    k = c["crank"][1] / M2.COST_P1["H"]["crank"][1]
    L["crank incl. balance [v1]"] = (CRANK_H[0] * k, CRANK_H[1] * k)
    fo, ca, nre = castings_line(parts, basis)
    L["first-op machining [v1]"] = fo
    L["castings: mold, pour, T6, impregnation, RT [v1]"] = ca
    L["cam"] = CF.CAM
    ms = (CF.MACHINE_SHOP[0] * 1.3, CF.MACHINE_SHOP[1] * 1.3)
    L["machine shop, less block decks [v1]"] = (ms[0] - 2 * DECK[0], ms[1] - 2 * DECK[1])
    L["FADEC, two lanes"] = CF.FADEC
    L["normalizing: turbo + intercooler [v1]"] = NORM_TURBO
    L["cooling"] = (CF.COOLING_PER_100KW[0] * CF.HEAT["SI"][1] / 100, CF.COOLING_PER_100KW[1] * CF.HEAT["SI"][1] / 100)
    for name, v in (("starter, alternator", CF.START_ALT), ("drive (direct)", CF.DRIVE["direct"]),
                    ("fuel system", CF.FUEL["SI"]), ("exhaust", CF.EXHAUST), ("misc", CF.MISC)):
        L[name] = v
    if concept == "H":
        L["crank pendulum damper"] = DAMPER
    if concept == "A" and a_pistons_priced:
        L["aviation piston premium [S]"] = (A_PISTON_PREMIUM[0] * n, A_PISTON_PREMIUM[1] * n)
    return L, nre


def total(L):
    lo = sum(v[0] for v in L.values())
    hi = sum(v[1] for v in L.values())
    return lo, math.sqrt(lo * hi), hi


VARIANTS = (("H", "H as sent (6 castings)", H_PARTS),
            ("H", "H with DFM items 1 + 4 (4 castings)", H_DFM_PARTS),
            ("A", "A (8 castings, PROPOSED envelopes)", A_PARTS),
            ("A+", "A with Lycoming pistons priced", A_PARTS))


def phase1(k):
    lo, hi = M2.cost_200(k)
    return lo, math.sqrt(lo * hi), hi


if __name__ == "__main__":
    f = lambda t: f"${t[0]/1000:.1f}k / ${t[1]/1000:.1f}k / ${t[2]/1000:.1f}k"
    print("## 200 hp cost floor, low / mid / high (mid is the geometric mean)\n")
    print("| Variant | phase 1 (AER-3326) | v1, builder basis | v1, first engine | program NRE, once |")
    print("|---|---|---|---|---|")
    res = {}
    for k, name, parts in VARIANTS:
        priced = k == "A+"
        k = k[0]
        Lb, nre = cost(k, "builder", parts, priced)
        Lf, _ = cost(k, "first", parts, priced)
        res[name] = (Lb, Lf, nre)
        print(f"| {name} | {f(phase1(k))} | {f(total(Lb))} | {f(total(Lf))} | ${nre[0]/1000:.1f}k-{nre[1]/1000:.1f}k |")

    print("\n## Line items, builder basis\n")
    names = [v[1] for v in VARIANTS]
    print("| Line | " + " | ".join(names) + " |")
    print("|---|" + "---|" * len(names))
    keys = list(dict.fromkeys(key for n in names for key in res[n][0]))
    for key in keys:
        cells = []
        for n in names:
            v = res[n][0].get(key)
            cells.append("-" if v is None else f"${v[0]/1000:.2f}k-{v[1]/1000:.2f}k")
        print(f"| {key} | " + " | ".join(cells) + " |")

    print("\n## The $22k test (R-35)\n")
    for n in names:
        for basis, L in (("builder", res[n][0]), ("first engine", res[n][1])):
            lo, mid, hi = total(L)
            print(f"- {n}, {basis}: low ${lo/1000:.1f}k is {'under' if lo <= 22000 else 'over'} $22k by "
                  f"${abs(lo - 22000)/1000:.1f}k; mid ${mid/1000:.1f}k")

    print("\n## What holding $22k would take (H with DFM items 1 + 4, builder basis)\n")
    L = dict(res[names[1]][0])
    lo, mid, hi = total(L)
    print(f"- start: low ${lo/1000:.1f}k, mid ${mid/1000:.1f}k")
    n_lo, n_hi = L.pop("normalizing: turbo + intercooler [v1]")
    lo2, mid2, _ = total(L)
    print(f"- delete normalizing (ruling 3 then fails; see the turbo trade): low ${lo2/1000:.1f}k, mid ${mid2/1000:.1f}k")
    lo3 = lo2 - L["second ignition lane"][0]
    print(f"- and delete the second ignition lane (R-25 then fails): low ${lo3/1000:.1f}k")

    print("\n## Mass and parts, concept H\n")
    print(f"- Darton MID liners, net of displaced aluminium: +{LINER_KG_NET[0]:.1f} to +{LINER_KG_NET[1]:.1f} kg [E]")
    m = M2.h_member(1, 200)
    print(f"- installed dry: phase 1 {m['dry_kg']:.0f} kg; with Darton MID {m['dry_kg'] + LINER_KG_NET[0]:.0f}-{m['dry_kg'] + LINER_KG_NET[1]:.0f} kg (R-37 proposed: 150 kg)")
    p, u, fa, P = M2.count("H")
    print(f"- parts as sent: {p} non-fastener, {u} unique, about {fa} fasteners")
    print(f"- with the block merge: {p - 2 - 2} non-fastener (2 blocks, 2 block-to-case gaskets), "
          f"about {fa - 24}-{fa - 16} fasteners (16-24 studs and nuts, envelope 9.5 item 1)")
