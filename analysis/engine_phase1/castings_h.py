"""Concept H castings: the numbers behind the rulings on MANUFACTURING envelope
v1 section 9.5 and 9.4, and the 200 hp cost floor rerun on two bases (AER-3331).

Inputs:
  * `h_quote_estimate.py` (MANUFACTURING, AER-3328): first-op and casting
    estimate per part number. Used unchanged; its six-casting result is
    reproduced here as a regression check before anything is changed.
  * `member_200.py` / `../engine_phase0/cost_floor.py`: the phase-1 line items.
  * Envelope v1 section 9.7: the line-item replacements (crank, liners,
    normalizing, castings, first-op).

What this script adds, each labeled:
  1. The post-ruling casting set: each cylinder bank merged into its crankcase
     half (9.5 #1), both case halves machined in one HMC setup on the doweled
     pair (#2), one head part number used on both banks (#3), head as a
     4-axis part (#4). Hours and fixture deltas are PROPULSION [E] on top of
     MANUFACTURING's [E] baseline, named beside each number.
  2. The scrap cost the merge adds (a scrapped pour loses the whole half).
  3. Wet-liner (Darton MID) against dry-sleeve mass, per cylinder.
  4. Main oil gallery: drill depth rule and pressure drop at full flow.
  5. HMC envelope for the one-setup pair.
  6. The 200 hp cost floor, four steps from the published phase-1 number, on
     basis 1 (first engine carries all NRE) and basis 2 (each engine of a
     batch of 5, NRE paid once by the program, reported separately).

Regression: step 1 below reproduces `cost_v1.py` (AER-3329) for H as sent on
both bases; steps 2 and 3 are what this issue adds.

Run: python3 castings_h.py
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


Q = load(os.path.join(HERE, "h_quote_estimate.py"), "h_quote_estimate")
M = load(os.path.join(HERE, "member_200.py"), "member_200")
CF = M.CF


def add(a, b, k=1.0):
    return (a[0] + k * b[0], a[1] + k * b[1])


def per_engine(parts):
    """The aggregation in h_quote_estimate.py's __main__, as a function."""
    n_cast = sum(p["n_per_engine"] for p in parts.values())
    e = {k: (0.0, 0.0) for k in ("fo_q1", "fo_q5", "fo_marg", "c_q1", "c_q5", "nre")}
    for p in parts.values():
        n, pn = p["n_per_engine"], p["part_numbers"]
        _, nre, _ = None, None, None
        _, _, nre = Q.first_op(p, 1)
        nre_eng = (nre[0] * pn, nre[1] * pn)
        b1 = n / pn
        _, m1, _ = Q.first_op(p, b1)
        _, m5, _ = Q.first_op(p, 5 * b1)
        e["fo_q1"] = add(e["fo_q1"], add(nre_eng, m1, n))
        e["fo_q5"] = add(e["fo_q5"], add((nre_eng[0] / 5, nre_eng[1] / 5), m5, n))
        e["fo_marg"] = add(e["fo_marg"], m5, n)
        e["nre"] = add(e["nre"], nre_eng)
        c1, _ = Q.casting(p, 1, 1 / n_cast)
        c5, _ = Q.casting(p, 5, 1 / 15)
        e["c_q1"] = add(e["c_q1"], c1, n)
        e["c_q5"] = add(e["c_q5"], c5, n)
    return e


# ------------------------------------------------ post-ruling casting set
CASE = Q.PARTS["case half (pair = 2 part numbers)"]
BLOCK = Q.PARTS["cylinder-bank block (L = R, 1 part number)"]
HEAD = Q.PARTS["bank head (mirrored L/R, 2 part numbers)"]

# Bounding boxes of the coarse STEP models (cad/concept_h/PART_LIST.md). The
# bureau prices printed sand on the CAD bounding box, so these replace the
# phase-1 envelope boxes.
STEP_BOX = {"H-101": (563, 331, 235), "H-201": (384, 190, 113)}

# 9.5 #1 + #2: bank merged into the case half. MANUFACTURING's box was
# 560 x 300 x 325; the STEP's deck sits 235 mm from the split plane. Open-deck wet-liner jacket: the coolant core is
# supported and cleaned out through the deck, core 10-25 % of the part box [E].
# Programming: case 12-22 h plus the deck/register/head-stud program, about
# half of the block's 8-14 h [E]. Fixture: the pair fixture carries a deck-side
# load, +100-300 per part number [E]. Setup B cycle: + 1.0-1.5 h for deck,
# registers and head studs on the same HMC setup (MANUFACTURING 9.5 #1).
MERGED = dict(
    n_per_engine=2, part_numbers=2,
    cam_h=(CASE["cam_h"][0] + 4, CASE["cam_h"][1] + 6),
    fixture=(CASE["fixture"][0] + 100, CASE["fixture"][1] + 300),
    setups=[
        CASE["setups"][0],
        (Q.RATE_HMC, (1.25, 1.75), (2.5 + 1.0, 3.5 + 1.5)),
    ],
    inspect_h=(2.0, 3.5),
    box_mm=STEP_BOX["H-101"], core_frac=(0.10, 0.25))

# 9.5 #3 + #4: one head part number on both banks (rotated 180 deg about the
# vertical axis), every feature axis normal to the head's long axis, so the
# second setup is a 4-axis job. Cycle +0.5 h for indexing on 4-axis rather
# than 5-axis interpolation [E]. NRE paid once for both heads.
HEAD_4AX = dict(HEAD, part_numbers=1, box_mm=STEP_BOX["H-201"],
                setups=[HEAD["setups"][0], (Q.RATE_4AX, (1.0, 2.0), (3.0, 4.5))])

PARTS_9_7 = Q.PARTS                                   # six castings, as quoted
PARTS_RULED = {"case half, bank merged": MERGED, "head, one part number, 4-axis": HEAD_4AX}


# ------------------------------------------------ scrap the merge adds
# A casting found bad at radiography before first-op is lost; its replacement
# is poured again. P_SCRAP per bureau first-article pour is ASSUMED (no
# published rate for one-offs). A merged half carries the defect-prone
# volume of a case half plus a block, so its scrap chance is 1-(1-p)^2.
P_SCRAP = (0.05, 0.20)


def scrap_ev():
    sep_case, _ = Q.casting(CASE, 1, 1 / 6)
    sep_blk, _ = Q.casting(BLOCK, 1, 1 / 6)
    mrg, _ = Q.casting(MERGED, 1, 1 / 4)
    out = []
    for p in P_SCRAP:
        pm = 1 - (1 - p) ** 2
        sep = 2 * (p * sep_case[1] + p * sep_blk[1])
        merged = 2 * pm * mrg[1]
        out.append((p, sep, merged))
    return out


# ------------------------------------------------ liner mass per cylinder
RHO_FE, RHO_AL = 7.10, 2.68          # g/cm^3, ductile iron, A356
BORE = 104.8


def ring_kg(d_in, wall, length, rho):
    d_out = d_in + 2 * wall
    return math.pi / 4 * (d_out ** 2 - d_in ** 2) * length / 1e6 * rho


def liners():
    # Darton MID: supplied at 4.100 in, 0.220 in wall (envelope 9.4 [S]);
    # length 180 mm ASSUMED (not published); top flange +0.3-0.5 kg [E].
    mid = ring_kg(4.100 * 25.4, 0.220 * 25.4, 180, RHO_FE)
    mid = (mid + 0.3, mid + 0.5)
    # Dry sleeve in a closed deck: 3 mm iron sleeve, 160 mm long [E], in a
    # 6 mm A356 cylinder wall, plus a 10 mm closed deck over the jacket
    # annulus (about 15 mm wide) [E]. The outer jacket wall is common to both.
    dry_fe = ring_kg(BORE, 3.0, 160, RHO_FE)
    dry_al = ring_kg(BORE + 6, 6.0, 160, RHO_AL) + ring_kg(BORE + 18, 15, 10, RHO_AL)
    return mid, dry_fe + dry_al, dry_fe, dry_al


P_PEAK = 7.0   # MPa, peak cylinder pressure, normalized (sea-level-like) SI at 10 bar BMEP, ASSUMED 70 bar


def thin_wet(wall=3.5):
    """A custom thinner wet liner: mass and thin-wall hoop stress at peak pressure."""
    kg = ring_kg(BORE, wall, 180, RHO_FE) + 0.3
    hoop = P_PEAK * (BORE / 2) / wall
    return kg, hoop


# ------------------------------------------------ main oil gallery
def gallery():
    L_side = 280.0                   # mm, 560 mm case drilled from both ends
    d_min = L_side / 25              # 9.5 #6: 25 x D per drilled run
    q_oil = M.h_member(1, 200)["Qoil"]           # kW to oil, engine_floor.py method
    flow = q_oil / (0.85 * 2.1 * 15)             # L/s, rho 0.85 kg/L, cp 2.1, dT 15 K
    nu, rho = 10e-6, 850                          # 10 cSt at 100 C
    rows = []
    for d in (12, 14):
        a = math.pi / 4 * (d / 1000) ** 2
        v = flow / 1000 / a
        re = v * d / 1000 / nu
        f = 0.316 / re ** 0.25
        dp = f * (0.560 / (d / 1000)) * rho * v ** 2 / 2 / 1e5   # bar, full flow over full length
        rows.append((d, L_side / d, v, re, dp))
    return q_oil, flow, d_min, rows


# ------------------------------------------------ HMC envelope for the pair
def hmc(deck_mm=235, box_half_mm=325):
    for z in (2 * deck_mm, 2 * box_half_mm):
        swing = math.hypot(STEP_BOX["H-101"][0], z) + 100   # + 50 mm tool clearance per side [E]
        yield z, swing


# ------------------------------------------------ cost floor, 200 hp, H
def lines(step, basis):
    """Per-engine cost lines for concept H at 200 hp. step:
    0 = phase 1 as published; 1 = 9.7 dropped in (six castings);
    2 = + rulings (four castings); 3 = + MACHINE_SHOP double counts removed.
    basis: 1 = first engine carries all NRE; 2 = each of 5, NRE paid once."""
    n = 6
    L = {
        "catalog per-cylinder set": (CF.PER_CYL["SI"][0] * n, CF.PER_CYL["SI"][1] * n),
        "second coil per cylinder": (CF.DUAL_LANE_PER_CYL[0] * n, CF.DUAL_LANE_PER_CYL[1] * n),
        "seats and guides": (CF.SEATS_GUIDES_PER_CYL[0] * n, CF.SEATS_GUIDES_PER_CYL[1] * n),
        "cam": CF.CAM, "FADEC": CF.FADEC,
        "cooling": (CF.COOLING_PER_100KW[0] * CF.HEAT["SI"][1] / 100, CF.COOLING_PER_100KW[1] * CF.HEAT["SI"][1] / 100),
        "starter, alternator": CF.START_ALT, "drive (direct)": CF.DRIVE["direct"], "fuel": CF.FUEL["SI"],
        "exhaust": CF.EXHAUST, "misc": CF.MISC, "crank damper": (400, 1500),
    }
    if step == 0:
        c = M.COST_P1["H"]
        L["liners"] = (CF.LINER_PER_CYL[0] * n, CF.LINER_PER_CYL[1] * n)
        L["crank"] = (CF.CRANK[0] * c["crank"][1], CF.CRANK[1] * c["crank"][1])
        L["normalizing"] = CF.NORM["turbo"]
        L["machine shop"] = (CF.MACHINE_SHOP[0] * 1.3, CF.MACHINE_SHOP[1] * 1.3)
        L["castings"] = add(add((0, 0), CF.CASE_HALF, 2 * c["case"][1]), CF.HEAD, 2)
        L["castings"] = add(L["castings"], (M.BLOCK[0] * M.BLOCK_SCALE["H"], M.BLOCK[1] * M.BLOCK_SCALE["H"]), 2)
        L["first-op"] = (CF.FIRST_OP[0] * 6, CF.FIRST_OP[1] * 6)
        return L
    L["liners"] = (1800, 2700)                     # 9.7, MID incl. bore and hone
    L["crank"] = (6600, 9400)                      # 9.7, incl. balance
    L["normalizing"] = (2000, 4500)                # 9.7 / section 10
    # 9.7: drop the two block decks (deck flatness $125-285 each [S], x1.3)
    L["machine shop"] = ((CF.MACHINE_SHOP[0] - 2 * 125) * 1.3, (CF.MACHINE_SHOP[1] - 2 * 285) * 1.3)
    if step >= 3:
        # MACHINE_SHOP (envelope 2.2) = align hone + deck x2 + bore/hone x6 +
        # valve work + balance. Bore/hone is now in the liner line, valve work
        # in the seats-and-guides line, balance in the crank line, decks in
        # first-op. What is left is the align hone: $350-440 [S, 9.5 #2],
        # x1.3 on the high end for 2026.
        L["machine shop"] = (350, 440 * 1.3)
    e = per_engine(PARTS_9_7 if step == 1 else PARTS_RULED)
    if basis == 1:
        L["castings"], L["first-op"] = e["c_q1"], e["fo_q1"]
    else:
        L["castings"], L["first-op"] = e["c_q5"], e["fo_marg"]
    return L


def total(L):
    lo = sum(v[0] for v in L.values())
    hi = sum(v[1] for v in L.values())
    return lo, math.sqrt(lo * hi), hi


def k(v):
    return f"${v/1000:.1f}k"


def kr(v):
    return f"${v[0]/1000:.1f}k-{v[1]/1000:.1f}k"


if __name__ == "__main__":
    base = per_engine(PARTS_9_7)
    print("## Regression: MANUFACTURING's six-casting result, re-aggregated\n")
    print(f"first-op first engine {kr(base['fo_q1'])}; NRE-once marginal {kr(base['fo_marg'])}; "
          f"NRE {kr(base['nre'])}; castings q1 {kr(base['c_q1'])}, q5 {kr(base['c_q5'])} "
          f"(envelope 9.3: $9.8k-33.9k; $1.7k-4.6k; $7.2k-26.7k; $6.2k-14.7k, $5.1k-11.2k)\n")

    print("## Per casting after the rulings\n")
    print("| Part | Qty / engine | Part numbers | First-op qty 1 | First-op marginal, NRE once | NRE per part number | Casting qty 1 | Casting qty 5 |")
    print("|---|---|---|---|---|---|---|---|")
    for name, p in PARTS_RULED.items():
        q1, m, nre = Q.first_op(p, 1)
        c1, _ = Q.casting(p, 1, 1 / 4)
        c5, _ = Q.casting(p, 5, 1 / 15)
        print(f"| {name} | {p['n_per_engine']} | {p['part_numbers']} | {kr(q1)} | {kr(m)} | {kr(nre)} | {kr(c1)} | {kr(c5)} |")
    ruled = per_engine(PARTS_RULED)
    print("\n| Per engine | Six castings (9.3) | Four castings (rulings) | Change |")
    print("|---|---|---|---|")
    for key, lab in (("fo_q1", "first-op, first engine (all NRE)"), ("fo_marg", "first-op, each of 5, NRE once"),
                     ("nre", "program NRE, once"), ("c_q1", "castings, first engine"), ("c_q5", "castings, each of 5")):
        d = (ruled[key][0] - base[key][0], ruled[key][1] - base[key][1])
        print(f"| {lab} | {kr(base[key])} | {kr(ruled[key])} | {d[0]/1000:+.1f}k / {d[1]/1000:+.1f}k |")

    print("\n## What each ruling buys, applied one at a time (first-op + castings, per engine)\n")
    print("| Casting set | Basis 1: first engine | Basis 2: each of 5, NRE once | Program NRE |")
    print("|---|---|---|---|")
    head_mirror = HEAD
    head_one = dict(HEAD, part_numbers=1)
    sets = (("six castings (9.3)", PARTS_9_7),
            ("#1 bank merged into case half", {"m": MERGED, "h": head_mirror}),
            ("#1 + #3 one head part number", {"m": MERGED, "h": head_one}),
            ("#1 + #3 + #4 head on 4-axis", PARTS_RULED))
    for lab, ps in sets:
        e = per_engine(ps)
        print(f"| {lab} | {kr(add(e['fo_q1'], e['c_q1']))} | {kr(add(e['fo_marg'], e['c_q5']))} | {kr(e['nre'])} |")

    print("\n## Head: 4-axis against 5-axis, per head (one part number either way)\n")
    h5 = dict(HEAD, part_numbers=1)
    for lab, p in (("5-axis", h5), ("4-axis", HEAD_4AX)):
        _, m, _ = Q.first_op(p, 10)
        print(f"- {lab}: marginal first-op at a batch of 10 heads {kr(m)}")

    print("\n## Scrap the merge adds (RT before first-op; P_SCRAP assumed)\n")
    for p, sep, mrg in scrap_ev():
        print(f"- p = {p:.2f} per pour: expected scrap per engine, separate {k(sep)}, merged {k(mrg)}, "
              f"merge adds {k(mrg - sep)} (high-end casting cost)")

    mid, dry, dfe, dal = liners()
    print("\n## Liner mass per cylinder\n")
    print(f"- Darton MID wet liner: {mid[0]:.2f}-{mid[1]:.2f} kg iron; x6 = {6*mid[0]:.1f}-{6*mid[1]:.1f} kg")
    print(f"- dry sleeve, closed deck: {dfe:.2f} kg iron + {dal:.2f} kg A356 = {dry:.2f} kg; x6 = {6*dry:.1f} kg")
    print(f"- wet-liner penalty: {6*(mid[0]-dry):.1f}-{6*(mid[1]-dry):.1f} kg per engine "
          f"(not the 15-18 kg gross: the dry option needs its own aluminum wall and deck)")
    print(f"- iron alone, MID against a 3 mm dry sleeve: {6*(mid[0]-dfe):.1f}-{6*(mid[1]-dfe):.1f} kg per engine "
          f"(the saving if the sleeve's aluminum wall is left out)")
    for w in (5.6, 3.5):
        kg, hoop = thin_wet(w)
        print(f"- wet liner, {w} mm wall: about {kg:.2f} kg; hoop stress at {P_PEAK*10:.0f} bar peak {hoop:.0f} MPa")

    q, flow, dmin, rows = gallery()
    print("\n## Main oil gallery\n")
    print(f"- oil heat {q:.0f} kW at 200 hp -> {flow*60:.0f} L/min at a 15 K oil rise; 25 x D over 280 mm per side -> D >= {dmin:.1f} mm")
    for d, ld, v, re, dp in rows:
        print(f"- {d} mm: {ld:.0f} x D per side, {v:.1f} m/s, Re {re:.0f}, full-flow drop over 560 mm {dp:.2f} bar (upper bound)")

    print("\n## HMC envelope for the doweled pair\n")
    for z, s in hmc():
        print(f"- pair {STEP_BOX['H-101'][0]} x {STEP_BOX['H-101'][1]} x {z:.0f} mm (z across both decks): swing needed about {s:.0f} mm")

    print("\n## 200 hp cost floor, concept H (low / mid / high; mid = geometric mean)\n")
    print("| Step | Basis 1: first engine, carries all NRE | Basis 2: each engine of 5, NRE paid once |")
    print("|---|---|---|")
    labels = ("0. Phase 1 as published (RANKING_PHASE1 section 1)", "1. Envelope 9.7 line items, six castings",
              "2. + rulings 9.5 #1-#4 (four castings)", "3. + MACHINE_SHOP double counts removed")
    for s, lab in enumerate(labels):
        cells = []
        for b in (1, 2):
            lo, md, hi = total(lines(s, b))
            cells.append(f"{k(lo)} / {k(md)} / {k(hi)}")
        print(f"| {lab} | {cells[0]} | {cells[1]} |")
    print(f"\nProgram NRE outside basis 2 (CAM + fixtures, four castings, three part numbers): {kr(ruled['nre'])} once.")
    print(f"Basis 2 with that NRE spread over 5 engines instead: "
          f"{k(total(lines(3, 2))[0] + ruled['nre'][0]/5)} - {k(total(lines(3, 2))[2] + ruled['nre'][1]/5)}.")

    print("\n### Line items, step 3\n")
    print("| Line | Basis 1 | Basis 2 |")
    print("|---|---|---|")
    L1, L2 = lines(3, 1), lines(3, 2)
    for key in sorted(L1, key=lambda x: -L1[x][1]):
        print(f"| {key} | {kr(L1[key])} | {kr(L2[key])} |")
