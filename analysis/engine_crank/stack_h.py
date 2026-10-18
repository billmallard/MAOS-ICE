"""Concept H rod, piston, liner and deck stack against crank H-301 (AER-3442).

crank_decision.py section 6 (AER-3439) found that the LS7 stack (6.067 in
rod, 235 mm deck, Darton 147.3 mm sleeve) interferes with H-301 at BDC. This
script picks the rod and the deck, and states the piston and liner-bottom
relief that gives 3 mm everywhere.

No catalog vendor publishes a big-end outline or a piston skirt profile
(searched 2026-10-18: Callies 2022 catalog, K1 2015 catalog, Manley, MAHLE,
JE, Wiseco, Diamond; see docs/engine/sources/STACK_SOURCES_2026-10-18.md).
They publish rod length, journal, pin, big-end width and bolt size, and the
piston's compression height, pin size and pin length. So the check is
turned round. Instead of testing one assumed outline, the script sweeps the
crank through 720 deg and maps, in each piston's own frame, how high the
crank reaches below the gudgeon pin. That map is a keep-out spec: any piston
whose material stays out of it, by drawing or by measurement, clears by
3 mm. The same is done for the liner bottom.

  1. Catalog rods with a 2.100 in journal and a 0.927 in pin [S].
  2. Keep-out map under the piston, per rod length and big-end radius.
  3. Liner bottom: the height the crank needs, and what that leaves the
     piston's ring pack at BDC.
  4. The pick: rod, piston, deck, liner length and relief.

Tags: [S] sourced, [E] PROPULSION estimate with its method here, [A]
assumed, [Q] needs a vendor drawing or a measured part. Nothing has been
made, measured or run.

Run: python3 stack_h.py > stack_h_tables.md
"""
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("crank_decision", os.path.join(HERE, "crank_decision.py"))
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)          # the module's own tables sit behind __main__ guards
G = cd.GEOM                           # cad/concept_h/h301_params.json, the H-301 geometry

IN = 25.4
CLEAR = 3.0                           # the target clearance, mm (AER-3442)
R = G["stroke"] / 2

# --------------------------------------------------------------- 1. catalog
# Callies 2022 catalog p.18 (LS Ultra H-Beam, Ultra I-Beam, Compstar) [S];
# all 2.100 in journal, 0.940 in big-end width, 7/16 in cap screws, 0.927 in
# pin unless noted. The LS7 OE rod is 6.067 in [S, MAHLE LS7 sheet].
RODS = [
    (6.067, "GM LS7 OE (MAHLE LS7 piston sheet rod length) [S]", "-"),
    (6.125, "Callies Ultra H-Beam U16300, 649 g [S]", "most common LS stroker length"),
    (6.200, "Callies Ultra H-Beam U16303, 625 g [S]", ""),
    (6.350, "Callies Ultra H-Beam U16302, 658 g; Ultra I-Beam U17178, 674 g [S]", ""),
    (6.460, "Callies Ultra H-Beam U16301, 661 g [S]", "longest Ultra H-Beam on 2.100 in"),
    (6.560, "Callies Compstar CSC6560DS2A2AH, 655 g [S]; pin 0.927 in read from the part-number code [E]", "longest 2.100 in rod found"),
]

# Catalog pistons, 4.125 in (104.8 mm) bore, 0.927 in pin [S, MAHLE LS7 sheet].
PISTONS = [
    ("MAHLE 930221525 (LS7, for the 6.067 in rod)", 1.181, 447, "4032"),
    ("MAHLE 930221625 (LS7, for the 6.125 in rod)", 1.105, 438, "4032"),
]
PIN_LEN = 2.250 * IN                  # JE / CP LS7 wrist pin length [S]
DECK_CLEAR = 0.5                      # piston crown below the deck at TDC [E]; the gasket sets squish
SLEEVE = 147.3                        # Darton MID LS sleeve length [S, rfq-package-v1]

# Big-end swing radius about the pin centre. Published: housing bore
# 2.225 in for the 2.100 in journal [S, K1], 7/16 in cap screws [S, Callies,
# Molnar, K1]. Estimate: housing radius 28.3 + cap wall 5 + head of a 7/16
# 12-point cap screw reaching about 8.5 mm past that at its outer corner, so
# 42 mm [E]; 46 mm is run as the bounding case for a wide-bolt rod [A].
BIGEND = (42.0, 46.0)
# Bounding cap model [E]: a box about the pin, half-width 40.9 mm across
# (cap-screw axis 33.3 mm off centre: housing radius 28.3 + half the 11.1 mm
# screw; plus a 7.6 mm head radius, 0.6 in across a 7/16 12-point head) and
# 34 mm deep on both sides of the pin (housing radius 28.3 + 5.7 mm cap wall,
# the screw heads seated in the cap's spot-faces). Corners at 53 mm from the
# pin, past both circles. Run as "box".
CAP_BOX = (40.9, 34.0)


def _outline(kind, g):
    if kind == "bigend" and g.get("bigend_box"):
        bw, bh = g["bigend_box"]
        t = np.linspace(-1, 1, 21)
        pts = np.r_[np.c_[bw * t, np.full_like(t, bh)], np.c_[bw * t, np.full_like(t, -bh)],
                    np.c_[np.full_like(t, bw), bh * t], np.c_[np.full_like(t, -bw), bh * t]]
        return pts + np.array([0.0, R])
    return _cd_outline(kind, g)


_cd_outline = cd.outline


def deck_for(rod_in, ch_in):
    return R + rod_in * IN + ch_in * IN + DECK_CLEAR


# ------------------------------------------------------------ 2. keep-out map
GRID = 2.0
XS = np.arange(-60, 60.01, GRID)      # along the crank axis (the gudgeon pin's direction), from the bore centre
YS = np.arange(-60, 60.01, GRID)      # across, toward the thrust faces


def reach_map(g, step=2):
    """For each cylinder, over 720 deg: the highest point any crank feature
    (webs, counterweights, the other rods' big ends and pins; not its own
    pin and rod) reaches toward the gudgeon pin, as height above the pin
    (negative = below it), on a 2 mm grid in the piston's own (x, y).
    Also the highest point the crank reaches in the liner-wall annulus,
    measured from the crank axis."""
    L = g["rod_length"]
    feats = cd.crank_features(g)
    cyl_x = []
    for bay in range(3):
        m0 = g["x_main0"] + bay * g["pitch"]
        x1 = m0 + g["main_w"] / 2 + g["web_t"] + g["pin_w"] / 2
        cyl_x += [x1, x1 + g["pin_w"] + g["web_t"]]
    nx, ny = len(XS), len(YS)
    names = sorted({f[0] for f in feats})
    per = {n: np.full((6, nx, ny), -np.inf) for n in names}
    liner = np.full(6, -np.inf)
    liner_who = [None] * 6
    outl = {k: _outline(k, g) for k in ("main-pin", "pin-pin", "cw", "bigend", "pin")}
    for th in np.arange(0, 720, step):
        pin_h = []
        for a, b in zip(g["throws_against_rotation"], g["banks"]):
            phi = math.radians(th - a) - (0 if b == "L" else math.pi)
            pin_h.append(R * math.cos(phi) + math.sqrt(L ** 2 - (R * math.sin(phi)) ** 2))
        for name, xs, ithrow, kind in feats:
            ang = math.radians(th - g["throws_against_rotation"][ithrow])
            pts = outl[kind]
            y = pts[:, 0] * math.cos(ang) + pts[:, 1] * math.sin(ang)
            z = -pts[:, 0] * math.sin(ang) + pts[:, 1] * math.cos(ang)
            iy = np.rint((y - YS[0]) / GRID).astype(int)
            ok = (iy >= 0) & (iy < ny)
            for x in np.arange(xs[0], xs[1] + 0.01, GRID):
                for j, b in enumerate(g["banks"]):
                    if kind in ("pin", "bigend") and j == ithrow:
                        continue
                    along = z if b == "L" else -z
                    dx = x - cyl_x[j]
                    if abs(dx) > 60:
                        continue
                    ix = int(round((dx - XS[0]) / GRID))
                    np.maximum.at(per[name][j, ix], iy[ok], (along - pin_h[j])[ok])
                    rad = np.hypot(dx, y)
                    wall = (rad > g["piston_r"]) & (rad <= g["liner_wall_od_bottom"] / 2)
                    if wall.any() and along[wall].max() > liner[j]:
                        liner[j] = along[wall].max()
                        liner_who[j] = name
    stack = np.stack([per[n] for n in names])
    reach = stack.max(axis=0)
    who = np.where(np.isfinite(reach), np.array(names, dtype=object)[stack.argmax(axis=0)], None)
    return reach, who, liner, liner_who, L - R


def zones(g):
    """The piston regions below the pin, in its own frame [E/A]:
    bosses, |x| from the small-end slot to the pin end (PIN_LEN/2) plus a
    2.5 mm lip, |y| <= boss_half_w; skirt panels, the thrust sides beyond
    |y| >= panel_y within +/- panel_half_chord of x; the rest of the bore."""
    X, Y = np.meshgrid(XS, YS, indexing="ij")
    rad = np.hypot(X, Y)
    inbore = rad <= g["piston_r"]
    boss = inbore & (np.abs(X) <= PIN_LEN / 2 + 2.5) & (np.abs(Y) <= g["boss_half_w"])
    panel = inbore & (np.abs(X) <= g["panel_half_chord"]) & (np.abs(Y) >= g["panel_y"])
    rest = inbore & ~boss & ~panel
    return dict(boss=boss, panel=panel, rest=rest, bore=inbore)


def floor_depth(reach, mask):
    """Deepest allowed piston material below the pin centre in the region,
    for 3 mm: depth = -(highest crank reach) - 3. Larger is better."""
    r = reach[:, mask]
    top = r[np.isfinite(r)].max() if np.isfinite(r).any() else -np.inf
    return -top - CLEAR


def run_case(rod_in, bigend_r, ch_in=1.105, step=2):
    dl = rod_in * IN - G["rod_length"]
    deck = deck_for(rod_in, ch_in)
    box = bigend_r == "box"
    g = dict(G, rod_length=rod_in * IN, bigend_r=42.0 if box else bigend_r, bigend_box=CAP_BOX if box else None,
             liner_bottom_from_axis=deck - SLEEVE)
    reach, who, liner, liner_who, pin_bdc = reach_map(g, step)
    z = zones(g)
    out = dict(rod=rod_in, bigend=bigend_r, deck=deck, pin_bdc=pin_bdc,
               boss=floor_depth(reach, z["boss"]), panel=floor_depth(reach, z["panel"]),
               rest=floor_depth(reach, z["rest"]), liner_need=liner.max() + CLEAR,
               liner_uncut=deck - SLEEVE, reach=reach, who=who, g=g, z=z)
    return out


# ---------------------------------------------------- 3. ring pack and liner
# MAHLE 930221625: 1.0 / 1.0 / 2.0 mm rings [S]. Ring-pack bottom (lower oil
# rail) above the pin centre: CH - top land 5.0 - (1.0 + 3.8 + 1.0 + 3.8 +
# 2.0) [E, LS forged-piston land proportions] = 11.5 mm at CH 1.105 in. The
# oil ring must stay inside the liner at BDC with 3 mm: liner bottom <=
# pin at BDC + ring-pack bottom - 3.
def ringpack_above_pin(ch_in):
    return ch_in * IN - 5.0 - (1.0 + 3.8 + 1.0 + 3.8 + 2.0)


def main():
    print("# stack_h.py tables (AER-3442)\n")
    print("Generated by `python3 stack_h.py`. Crank geometry: `cad/concept_h/h301_params.json` (H-301 Rev A, "
          f"{G['pitch']} mm bank pitch, bank offset {G['pin_w'] + G['web_t']:.1f} mm). Tags as in the script header. "
          "Nothing here has been made or measured.\n")
    print("## 1. Catalog rods, 2.100 in journal, 0.927 in pin\n")
    print("| Length (in) | Length (mm) | Part | Note |\n|---|---|---|---|")
    for r, p, n in RODS:
        print(f"| {r:.3f} | {r*IN:.1f} | {p} | {n} |")
    print()

    print("## 2. Keep-out under the piston and at the liner bottom\n")
    print(f"Swept every 2 deg over 720 deg on a {GRID:.0f} mm grid in each piston's frame. Each cell holds the highest point "
          "the crank (webs, counterweights R62, the other rods' big ends) reaches toward that piston's gudgeon pin. "
          f"The table gives the **deepest piston material allowed below the pin centre for {CLEAR:.0f} mm**, per region "
          "(larger is better). Regions: **bosses**, |x| <= "
          f"{PIN_LEN/2+2.5:.1f} mm (pin length 2.250 in [S] plus a 2.5 mm lip [E]) and |y| <= {G['boss_half_w']} mm; "
          f"**skirt panels**, thrust sides beyond |y| {G['panel_y']} mm within +/-{G['panel_half_chord']} mm of x; **rest**, "
          "everything else inside the bore. Deck and liner use the CH 1.105 in piston. "
          "**Liner need** is the lowest the liner bottom may sit (from the crank axis) for 3 mm.\n")
    print("| Rod (in) | Big end R (mm) | Deck (mm) | Pin at BDC from axis (mm) | Bosses: max depth (mm) | Panels | Rest | Liner need (mm) | Uncut liner bottom (mm) |")
    print("|---|---|---|---|---|---|---|---|---|")
    cases = {}
    for rod in (6.067, 6.200, 6.350, 6.460, 6.560):
        for be in BIGEND:
            c = run_case(rod, be, step=4)
            cases[(rod, be)] = c
            print(f"| {rod:.3f} | {be:.0f} | {c['deck']:.1f} | {c['pin_bdc']:.1f} | {c['boss']:.1f} | {c['panel']:.1f} | "
                  f"{c['rest']:.1f} | {c['liner_need']:.1f} | {c['liner_uncut']:.1f} |")
    print()
    print("A real piston's pin boss reaches at least the pin radius (11.8 mm) plus a boss wall below the pin centre: "
          "**about 17-18 mm** [E; crank_decision.py assumed 18]. Skirt panels on catalog LS forgings run "
          "about 25-30 mm below the pin [A, not published]. So the boss column decides the rod, and the panel column "
          "says how much skirt relief that rod needs.\n")
    return cases


PICK = dict(rod_in=6.560, ch_in=1.105, liner_bottom=100.0, boss_below_pin=18.0, skirt_below_pin=26.0)


def boss_owner(c):
    """The feature that reaches highest into the boss column."""
    r = np.where(c["z"]["boss"][None], c["reach"], -np.inf)
    j, ix, iy = np.unravel_index(np.argmax(r), r.shape)
    return c["who"][j, ix, iy], XS[ix], YS[iy]


def pick_section(cases):
    p = PICK
    print("## 3. Which rod: the boss column\n")
    print("| Rod (in) | Deck (mm) | Boss depth allowed, R42 / box (mm) | Margin over an 18 mm boss [E] | Set by |")
    print("|---|---|---|---|---|")
    for rod in (6.350, 6.460, 6.560):
        a = run_case(rod, 42.0, p["ch_in"], step=2)
        b = run_case(rod, "box", p["ch_in"], step=2)
        own, x, y = boss_owner(b)
        lim = min(a["boss"], b["boss"])
        print(f"| {rod:.3f} | {a['deck']:.1f} | {a['boss']:.1f} / {b['boss']:.1f} | {lim - 18:+.1f} | {own} at x {x:+.0f}, y {y:+.0f} |")
    print()
    c = run_case(p["rod_in"], 42.0, p["ch_in"], step=2)
    cb = run_case(p["rod_in"], "box", p["ch_in"], step=2)
    rp = ringpack_above_pin(p["ch_in"])
    liner_max = c["pin_bdc"] + rp - CLEAR
    print(f"## 4. The pick: {p['rod_in']:.3f} in rod, CH {p['ch_in']:.3f} in piston, liner bottom {p['liner_bottom']:.0f} mm\n")
    print(f"Deck **{c['deck']:.1f} mm** from the crank axis (LS7 stack 235.0; **+{c['deck']-235:.1f} per side**). "
          f"Gudgeon pin at BDC {c['pin_bdc']:.1f} mm from the axis. Liner {c['deck'] - p['liner_bottom']:.1f} mm long "
          f"(Darton MID {SLEEVE} [S]: **cut {SLEEVE - (c['deck'] - p['liner_bottom']):.1f} mm off the bottom**).\n")
    print("| Check | Big end R42 [E] | Big end box [E, bound] | Requirement it sets |")
    print("|---|---|---|---|")
    print(f"| Bosses: deepest material below the pin for 3 mm | {c['boss']:.1f} | {cb['boss']:.1f} | catalog boss bottom <= {min(c['boss'], cb['boss']):.1f} mm below the pin [Q] |")
    print(f"| Skirt panels: deepest below the pin for 3 mm | {c['panel']:.1f} | {cb['panel']:.1f} | skirt panel bottom <= {min(c['panel'], cb['panel']):.1f} mm below the pin where the crank passes [Q] |")
    print(f"| Rest of the bore below the pin | {c['rest']:.1f} | {cb['rest']:.1f} | no material below the ring belt outside bosses and panels |")
    print(f"| Liner bottom, lowest allowed from the axis | {c['liner_need']:.1f} | {cb['liner_need']:.1f} | set at {p['liner_bottom']:.0f} |")
    print(f"| Liner bottom, highest allowed (oil ring covered at BDC by 3 mm) | {liner_max:.1f} | {liner_max:.1f} | ring-pack bottom {rp:.1f} mm above the pin [E] |")
    sk = c["pin_bdc"] - 30.0
    print(f"| Skirt out of the liner at BDC (30 mm skirt) | {p['liner_bottom'] - sk:.1f} | | LS7 in its own block: {87.7 - (154.1 - R - 30):.1f} |")
    print()
    for label, cc in (("R42", c), ("box", cb)):
        reach = cc["reach"].max(axis=0)
        need = -reach - CLEAR
        X, Y = np.meshgrid(XS, YS, indexing="ij")
        m = cc["z"]["panel"] & (need < 30.0)
        if m.any():
            print(f"Big end {label}: a skirt panel 30 mm below the pin needs relief over x {X[m].min():+.0f} to {X[m].max():+.0f} mm "
                  f"(along the pin), |y| {np.abs(Y[m]).min():.0f} to {np.abs(Y[m]).max():.0f} mm, up to **{(30.0 - need[m]).max():.1f} mm** deep.\n")
        else:
            print(f"Big end {label}: a skirt panel 30 mm below the pin needs no relief.\n")
    return c, cb


def rerun_section6():
    """crank_decision.py section 6 itself, on the picked stack: its relieved
    piston model with the boss and panel depths of the pick, the bounding
    cap box for the big end, the liner bottom at the pick."""
    p = PICK
    deck = deck_for(p["rod_in"], p["ch_in"])
    g = dict(G, rod_length=p["rod_in"] * IN, liner_bottom_from_axis=p["liner_bottom"],
             boss_below_pin=p["boss_below_pin"], skirt_below_pin=p["skirt_below_pin"],
             boss_half_len=PIN_LEN / 2 + 2.5)
    print("## 5. crank_decision.py section 6, rerun on the picked stack\n")
    print(f"`crank_decision.clearance()`, relieved model, every 2 deg: rod {p['rod_in']} in, liner bottom {p['liner_bottom']:.0f} mm, "
          f"bosses {p['boss_below_pin']:.0f} mm below the pin over |x| <= {PIN_LEN/2+2.5:.1f}, skirt panels {p['skirt_below_pin']:.0f} mm "
          "below the pin. Negative = interference.\n")
    rows = {}
    for label, gg in (("big end R42 [E]", dict(g, bigend_r=42.0)), ("big end R46 [A]", dict(g, bigend_r=46.0)),
                      ("big end box [E, bound]", dict(g, bigend_box=CAP_BOX))):
        cd.outline = _outline
        try:
            w = cd.clearance(gg, step=2, model="relieved")
        finally:
            cd.outline = _cd_outline
        rows[label] = w
    keys = sorted(rows["big end box [E, bound]"], key=lambda k: rows["big end box [E, bound]"][k][0])
    print("| Feature | Against | " + " | ".join(rows) + " |")
    print("|---|---|" + "---|" * len(rows))
    for k in keys:
        print(f"| {k[0]} | {k[1]} | " + " | ".join(f"{rows[l][k][0]:.1f}" if k in rows[l] else "-" for l in rows) + " |")
    print()
    worst = {l: min(v[0] for v in w.values()) for l, w in rows.items()}
    print("Smallest gap: " + "; ".join(f"{l} **{v:.1f} mm**" for l, v in worst.items()) + ".\n")
    return worst, deck


def write_stack(deck):
    """The stack the castings are drawn to (cad/concept_h/h_stack.json)."""
    p = PICK
    out = dict(
        _note="Concept H rod / piston / liner / deck stack against crank H-301. Generated by "
              "analysis/engine_crank/stack_h.py (AER-3442); read by cad/concept_h/h_castings.py with h301_params.json. mm.",
        rod_in=p["rod_in"], rod_mm=round(p["rod_in"] * IN, 2),
        rod_part="Callies Compstar CSC6560DS2A2AH, 2.100 in journal, 0.927 in pin [S; pin from the code, E]",
        piston_part="MAHLE 930221625, 4.125 in, CH 1.105 in, 0.927 in pin, with skirt relief per stack_h.py [S + Q]",
        ch_mm=round(p["ch_in"] * IN, 2), deck_clearance=DECK_CLEAR,
        deck=round(deck, 1), liner_bottom=p["liner_bottom"], liner_length=round(deck - p["liner_bottom"], 1),
        boss_max_below_pin=p["boss_below_pin"], skirt_max_below_pin=p["skirt_below_pin"])
    path = os.path.join(HERE, "..", "..", "cad", "concept_h", "h_stack.json")
    with open(path, "w") as f:
        import json
        json.dump(out, f, indent=1)
        f.write("\n")


if __name__ == "__main__":
    cases = main()
    pick_section(cases)
    worst, deck = rerun_section6()
    write_stack(deck)
