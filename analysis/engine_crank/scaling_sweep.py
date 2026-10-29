"""Small-fast against large-slow for the 200 hp member, as a sweep (AER-3411).

Phase 0/1 compared four discrete points (B, C, H, A). This sweeps the axis:
cylinder count 4 / 6 / 8 (flat, opposed, one throw per cylinder: the family
architecture of concept H), rated crank rpm 2,600-6,000, at the BMEP concept H
runs (10.3 bar, implied eta_v 0.91 on engine_floor.py's fuel and AFR).

For each point:
  geometry   Vd = P x 120 / (BMEP x N). Stroke/bore 0.97 (H's ratio) unless
             mean piston speed would pass SP_MAX; then the stroke is cut to
             SP_MAX and the bore opened up. Points over B/S 1.45 are dropped
             (too flat a chamber for a knock-limited engine) [E].
  drive      direct up to 3,400 rpm (H's 1.73 m propeller); above that a
             single-stage reduction to 2,550 propeller rpm (a 1.9-2.0 m
             propeller at tip Mach about 0.8, drive_match.py option 2 class).
  knock      knock-limited CR on MON 85 at K*_air (knock.py, unchanged), and
             the ideal-Otto fuel-burn change against H's CR.
  mass       modern light-engine fit on the UL Power family and checked on
             Rotax 912 and Jabiru (method in mass_bare), x1.10 sand-cast, plus
             the turbo, second lane, net Darton liner allowance as phase 1b,
             plus the gearbox or decoupler.
  crank      crank_routes.py geometry and cost, by route.
  cost       concept H's step-3 line items (castings_h.py), each scaled by the
             driver named in scale_lines(); basis 1 (first engine carries all
             NRE) is the primary result, basis 2 is shown beside it.
  torsion    torsional_h.py's lumped chain, scaled with the geometry, to flag a
             mode-1 crossing of a major order inside 60-105 % of rated rpm.

The gearbox is priced and massed as acceptable (Bill's direction 2, an input
to weigh, not a ruling), with a proven-class reliability assumption stated in
the doc. All figures are [E] or [A] unless a source is named. Nothing here
has been made or tested.

Run: python3 scaling_sweep.py            (tables)
     python3 scaling_sweep.py --plot     (also writes sweep_200hp.png)
"""
import importlib.util
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


CR = load(os.path.join(HERE, "crank_routes.py"), "crank_routes")
CH = load(os.path.join(HERE, "..", "engine_phase1", "castings_h.py"), "castings_h")
KN = load(os.path.join(HERE, "..", "engine_phase1", "knock.py"), "knock")
TV = CR.TV

P_KW = CR.P_KW
BMEP = 10.3
SP_MAX = 16.0           # m/s, about Viking/Aeromomentum's flying auto conversions [S, COMPARABLE_ENGINES]; H runs 11.2
BS_MAX = 1.45
N_DIRECT_MAX = 3400
N_PROP_GEARED = 2550
H_REF = dict(n=6, bore=104.8, stroke=101.6, N=3300)

# Reduction gearbox, single stage, with a Rotax-style friction overload clutch
# and a catalog torsional coupling. First engine (basis 1) and each of five
# (basis 2). [E] build-up in CRANK_AND_SCALING.md section 5; AER-3412 to check.
GEARBOX_B1 = (2900, 9800)
GEARBOX_B2 = (2000, 6000)
GEARBOX_KG_PER_NM = (0.020, 0.036)    # [E] on Marcotte M-300 (unverified 21 kg, 300 hp) and Auto PSRUs 250Z (32 kg)
DECOUPLER_B2 = (800, 2400)


def mass_bare(vd_l, n, bore):
    """Bare dry mass, kg. Linear fit through UL260iS (4 cyl, 2.59 L, 60.1 kg),
    UL350iS (4 cyl, 3.50 L, 66.1 kg) and UL520iS (6 cyl, 5.25 L, 93.3 kg)
    [S, COMPARABLE_ENGINES]: 11.8 + 6.6 kg/L + 7.8 kg per cylinder at the UL
    105.6 mm bore. Checks: Jabiru 3300 (6 cyl, 3.3 L) 80 kg against 83.5 kg
    listed with exhaust; Rotax 912 (4 cyl, 1.35 L) 45 kg + about 11 kg of
    gearbox and liquid-cooling parts against 56.6 kg. The per-cylinder term
    is scaled with bore to the first power [A] (0 to 2 moves a 86 mm 8-cylinder
    by -7 to +6 kg)."""
    return 11.8 + 6.6 * vd_l + 7.8 * n * (bore / 105.6)


def dry_mass(pt):
    """Installed-dry basis of member_200.py / RECOST_PHASE1B section 7:
    (bare + 14.7 kg ready-to-fly extras) x 1.10 sand-cast + 9 kg turbo +
    6 kg jackets and second lane + the net Darton MID allowance (H: 9.4-11.2
    kg for 6 cylinders, scaled by liner volume)."""
    liner = (1.57 * pt["n"] * (pt["bore"] / 104.8) ** 2 * (pt["stroke"] / 101.6),
             1.87 * pt["n"] * (pt["bore"] / 104.8) ** 2 * (pt["stroke"] / 101.6))
    base = (mass_bare(pt["vd"], pt["n"], pt["bore"]) + 14.7) * 1.10 + 9.0 + 6.0
    d = pt["drive_kg"]
    return (base + liner[0] + d[0], base + liner[1] + d[1])


def env(n, bore, stroke):
    """Casting envelope, mm^3: case length x width across decks x height
    (fitted to concept H's STEP: 434 x 473 x 330 mm against 563 x 470 x 331
    with the flange; only the ratio is used)."""
    pitch = CR.PITCH_PER_BORE * bore
    L = (n / 2) * pitch + CR.BANK_OFFSET_PER_BORE * bore + 60
    W = 2 * (0.5 * stroke + 1.52 * stroke + 0.3 * bore)
    Hh = 1.6 * bore + 1.6 * stroke
    return L * W * Hh


ENV_H = env(6, 104.8, 101.6)


def crank_cost(pt, route, basis):
    g = CR.geom(pt["n"], pt["bore"], pt["stroke"], pt.get("layout", "flat"))
    if route == "billet specialist":
        c, _ = CR.machined(g, "specialist")
    elif route == "general CNC":
        c, _ = CR.machined(g, "general")
    elif route == "cast ADI":
        c = CR.route3_cost(g, True)
    else:
        raise KeyError(route)
    if basis == 2:
        for k in ("nre", "gating_design_and_solidification_sim"):
            if k in c:
                c[k] = (c[k][0] / 5, c[k][1] / 5)
    return CR.tot(c)


def scale_lines(pt, basis, crank):
    L = dict(CH.lines(3, basis))
    n, r_env = pt["n"], env(pt["n"], pt["bore"], pt["stroke"]) / ENV_H
    for k in ("catalog per-cylinder set", "second coil per cylinder", "seats and guides", "liners"):
        L[k] = (L[k][0] * n / 6, L[k][1] * n / 6)                      # per cylinder
    f = 0.35 + 0.65 * r_env                                            # 35 % per-casting fixed (T6, RT, impregnation, setup) [E]
    L["castings"] = (L["castings"][0] * f, L["castings"][1] * f)
    f = (0.55 + 0.45 * n / 6) if basis == 1 else (0.30 + 0.70 * n / 6)  # NRE per part number fixed; features per cylinder [E]
    L["first-op"] = (L["first-op"][0] * f, L["first-op"][1] * f)
    for k, a in (("exhaust", 0.6), ("misc", 0.7)):
        L[k] = (L[k][0] * (a + (1 - a) * n / 6), L[k][1] * (a + (1 - a) * n / 6))
    L["crank"] = crank
    del L["drive (direct)"]
    L["drive"] = pt["drive_cost"][basis - 1]
    return L


def torsion_flag(pt):
    """Mode-1 crossing of a major order inside 60-105 % of rated rpm. Every
    inertia and stiffness is H's torsional_h.py value scaled with bore [E]."""
    s = pt["bore"] / 104.8
    h = TV.CASES["H flat-6, LS7 module, 3,300 rpm"]
    c = dict(h, z=pt["n"], idle=0.6 * pt["N"], red=pt["N"], stroke=pt["stroke"] / 1000,
             dj=CR.MAIN_PER_BORE * pt["bore"] / 1000, Leq=h["Leq"] * s, Ln=h["Ln"] * s,
             jc=h["jc"] * s ** 5, m_rec=h["m_rec"] * s ** 3, m_rot=h["m_rot"] * s ** 3, jr=h["jr"] * s ** 5)
    Jp = 1.0 if pt["ratio"] == 1 else max(0.05, 1.0 / pt["ratio"] ** 2)
    f, X, *_ = TV.model(c, Jp)
    cr = TV.campbell(c, f, X)
    hits = [(o, rpm) for m, ff, o, rpm, mj, rel in cr if mj and m == 1]
    return f[0], hits


KSTAR = KN.run()[1]
CR_H = KN.cr_limit(104.8, 101.6, 3300, 85, KSTAR)


def point(n, N, stroke_over_bore=0.97, route="billet specialist"):
    vd = P_KW * 1000 * 120 / (BMEP * 1e5 * N) * 1000          # L
    v1 = vd / n / 1000                                          # m^3 per cylinder
    S = (4 * v1 * stroke_over_bore ** 2 / math.pi) ** (1 / 3)  # m, from v = pi/4 B^2 S with S = k B
    B = S / stroke_over_bore
    if 2 * S * N / 60 > SP_MAX:
        S = SP_MAX * 60 / (2 * N)
        B = math.sqrt(4 * v1 / (math.pi * S))
    bore, stroke = B * 1000, S * 1000
    if bore / stroke > BS_MAX:
        return None
    geared = N > N_DIRECT_MAX
    ratio = N / N_PROP_GEARED if geared else 1.0
    if geared:
        T_prop = P_KW * 1000 / (N_PROP_GEARED * 2 * math.pi / 60)
        drive_kg = (GEARBOX_KG_PER_NM[0] * T_prop, GEARBOX_KG_PER_NM[1] * T_prop)
        drive_cost = (GEARBOX_B1, GEARBOX_B2)
    else:
        drive_kg = (0.0, 0.0)
        drive_cost = (CH.CF.DRIVE["direct"], CH.CF.DRIVE["direct"])
    pt = dict(n=n, N=N, vd=vd, bore=bore, stroke=stroke, sp=2 * S * N / 60, ratio=ratio,
              geared=geared, drive_kg=drive_kg, drive_cost=drive_cost, route=route)
    # a cast crank needs the propeller loads off the crank: add a decoupler when direct
    if route == "cast ADI" and not geared:
        pt["drive_kg"] = CR.DECOUPLER_KG
        pt["drive_cost"] = (CR.tot(CR.DECOUPLER_COST), DECOUPLER_B2)
    return evaluate(pt)


def evaluate(pt):
    pt["cr"] = KN.cr_limit(pt["bore"], pt["stroke"], pt["N"], 85, KSTAR)
    pt["fuel"] = KN.otto(CR_H) / KN.otto(pt["cr"]) - 1
    pt["mass"] = dry_mass(pt)
    g = CR.geom(pt["n"], pt["bore"], pt["stroke"], pt.get("layout", "flat"))
    pt["crank_kg"] = g["finished_kg"]
    for b in (1, 2):
        crank = pt["crank_override"][b - 1] if "crank_override" in pt else crank_cost(pt, pt["route"], b)
        L = scale_lines(pt, b, crank)
        if "extra" in pt:
            for k, v in pt["extra"].items():
                L[k] = v[b - 1]
        lo, hi = sum(v[0] for v in L.values()), sum(v[1] for v in L.values())
        pt[f"b{b}"] = (lo, math.sqrt(lo * hi), hi)
        pt[f"lines{b}"] = L
        pt[f"crank{b}"] = crank
    pt["f1"], pt["tv"] = torsion_flag(pt)
    return pt


def oe_overlay():
    """Mass-production cranks (crank_routes.OE_CRANKS) placed on the same cost
    and mass model. The crank line is the bought crank plus balance and
    inspection; a direct-drive point carries the propeller-shaft decoupler.
    Castings use the flat-engine envelope formula at the same bore, stroke
    and cylinder count, which is coarse for a V8 block or an inline-6 [E]."""
    pts = []
    for c in CR.OE_CRANKS:
        line = CR.oe_crank_cost(c)
        if line is None:
            continue
        lay = {"90 V8": "shared", "I6": "inline"}.get(c["layout"], "flat")
        for b in c["bores"]:
            vd, N, sp = CR.oe_point(c, b)
            geared = N > N_DIRECT_MAX
            ratio = N / N_PROP_GEARED if geared else 1.0
            if geared:
                T_prop = P_KW * 1000 / (N_PROP_GEARED * 2 * math.pi / 60)
                dk, dc = (GEARBOX_KG_PER_NM[0] * T_prop, GEARBOX_KG_PER_NM[1] * T_prop), (GEARBOX_B1, GEARBOX_B2)
            else:
                dk, dc = CR.DECOUPLER_KG, (CR.tot(CR.DECOUPLER_COST), DECOUPLER_B2)
            pt = dict(n=c["n"], N=round(N), vd=vd, bore=b, stroke=c["stroke"], sp=sp, ratio=ratio, geared=geared,
                      drive_kg=dk, drive_cost=dc, route="OE", layout=lay, crank_override=(line, line), label=c["name"])
            pts.append(evaluate(pt))
    return pts


CATALOG_BORES = [(84.0, "Rotax 912"), (86.0, "FA20 / 2JZ"), (89.0, "various"), (92.0, "EZ36"), (96.0, "LS 4.8/5.3"),
                 (99.5, "EJ25"), (101.6, "SBC / 4.3 V6"), (103.25, "LS3"), (104.8, "LS7"), (111.1, "-"), (130.2, "Lycoming 540")]


def nearest_piston(b):
    d, name = min(((abs(b - cb), f"{cb} {nm}") for cb, nm in CATALOG_BORES), key=lambda x: x[0])
    return name, d


def k(v):
    return f"{v/1000:.1f}"


def row(pt):
    pis, d = nearest_piston(pt["bore"])
    tv = "; ".join(f"o{o:g}@{rpm:,.0f}" for o, rpm in pt["tv"]) or "clear"
    drive = f"{pt['ratio']:.2f}:1" if pt["geared"] else "direct"
    return (f"| {pt['N']:,} | {drive} | {pt['vd']:.2f} | {pt['bore']:.1f} x {pt['stroke']:.1f} | {pt['sp']:.1f} | {pis} ({d:+.1f}) | "
            f"{pt['cr']:.1f} | {100*pt['fuel']:+.1f} % | {pt['crank_kg']:.0f} | {pt['mass'][0]:.0f}-{pt['mass'][1]:.0f} | "
            f"{k(pt['crank1'][0])}-{k(pt['crank1'][1])} | {k(pt['b1'][0])} / {k(pt['b1'][1])} / {k(pt['b1'][2])} | "
            f"{k(pt['b2'][0])} / {k(pt['b2'][1])} | {pt['f1']:.0f} Hz: {tv} |")


HEAD = ("| rpm | drive | Vd (L) | bore x stroke | Sp | nearest catalog piston (mm off) | CR, MON 85 | fuel vs H | crank kg | dry kg | "
        "crank $k, first engine | **basis 1 $k** low / mid / high | basis 2 $k low / mid | crank mode 1: major-order crossings in 60-105 % rpm |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")

RPMS = (2600, 2800, 3000, 3300, 3400, 3600, 4000, 4400, 4800, 5200, 5600, 6000)


def sweep(route="billet specialist"):
    out = {}
    for n in (4, 6, 8):
        out[n] = [p for p in (point(n, N, route=route) for N in RPMS) if p is not None]
    return out


if __name__ == "__main__":
    h = evaluate(dict(n=6, N=3300, vd=5.26, bore=104.8, stroke=101.6, sp=11.2, ratio=1.0, geared=False,
                      drive_kg=(0, 0), drive_cost=(CH.CF.DRIVE["direct"],) * 2, route="billet specialist"))
    ref = CH.total(CH.lines(3, 1)), CH.total(CH.lines(3, 2))
    print("## Regression: concept H through the sweep model\n")
    print(f"basis 1 {k(h['b1'][0])} / {k(h['b1'][1])} / {k(h['b1'][2])} (castings_h.py step 3: {k(ref[0][0])} / {k(ref[0][1])} / {k(ref[0][2])}); "
          f"basis 2 {k(h['b2'][0])} / {k(h['b2'][1])} (castings_h.py: {k(ref[1][0])} / {k(ref[1][1])}); "
          f"dry {h['mass'][0]:.0f}-{h['mass'][1]:.0f} kg (RECOST_PHASE1B section 7: 143-145 kg before the sourced turbo and intercooler); "
          f"CR {h['cr']:.1f} (knock.py 8.4).\n")
    print("Basis 1 matches. Basis 2 is lower by the crank's one-off NRE ($1.0k-2.0k), which this model pays once by the program,"
          " as basis 2 already does for the castings; castings_h.py kept the crank at its first-engine price on both bases.\n")
    for route in ("billet specialist", "cast ADI"):
        print(f"\n## Sweep, crank route: {route}" + (" (direct points carry a propeller-shaft decoupler)" if route == "cast ADI" else "") + "\n")
        for n, pts in sweep(route).items():
            print(f"\n### {n} cylinders, flat\n")
            print(HEAD)
            for pt in pts:
                print(row(pt))

    # best per cylinder count, basis 1 mid, billet crank
    print("\n## Cheapest point per cylinder count, basis 1 mid\n")
    for route in ("billet specialist", "general CNC", "cast ADI"):
        for n, pts in sweep(route).items():
            b = min(pts, key=lambda p: p["b1"][1])
            print(f"- {route}, {n} cyl: {b['N']:,} rpm ({'geared' if b['geared'] else 'direct'}), "
                  f"${k(b['b1'][0])}k / ${k(b['b1'][1])}k / ${k(b['b1'][2])}k, {b['mass'][0]:.0f}-{b['mass'][1]:.0f} kg")

    # what moves between H and a geared 6-cylinder at 4,800 rpm, line by line
    g6 = point(6, 4800)
    print("\n## Line by line: H (6 cyl, 3,300 direct) against a geared 6-cylinder at 4,800 rpm, basis 1\n")
    print("| Line | H | 6 cyl, 4,800 rpm, geared | change (low / high) |")
    print("|---|---|---|---|")
    keys = sorted(set(h["lines1"]) | set(g6["lines1"]), key=lambda x: -h["lines1"].get(x, (0, 0))[1])
    for key in keys:
        a, b = h["lines1"].get(key, (0, 0)), g6["lines1"].get(key, (0, 0))
        if a == b:
            continue
        print(f"| {key} | {k(a[0])}-{k(a[1])} | {k(b[0])}-{k(b[1])} | {(b[0]-a[0])/1000:+.1f} / {(b[1]-a[1])/1000:+.1f} |")
    print(f"| **total** | {k(h['b1'][0])}-{k(h['b1'][2])} | {k(g6['b1'][0])}-{k(g6['b1'][2])} | "
          f"{(g6['b1'][0]-h['b1'][0])/1000:+.1f} / {(g6['b1'][2]-h['b1'][2])/1000:+.1f} |")
    print(f"| dry mass (kg) | {h['mass'][0]:.0f}-{h['mass'][1]:.0f} | {g6['mass'][0]:.0f}-{g6['mass'][1]:.0f} | |")

    print("\n## Mass-production cranks on the same model (route 2), first engine\n")
    print("| Crank | cylinders | bore x stroke | rpm | drive | Vd (L) | CR, MON 85 | dry kg | crank line | **basis 1 $k** low / mid / high | basis 2 $k low / mid | against H, basis 1 low / mid |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for pt in oe_overlay():
        drive = f"gearbox {pt['ratio']:.2f}:1" if pt["geared"] else "direct + decoupler"
        print(f"| {pt['label']} | {pt['n']} | {pt['bore']} x {pt['stroke']} | {pt['N']:,} | {drive} | {pt['vd']:.2f} | {pt['cr']:.1f} | "
              f"{pt['mass'][0]:.0f}-{pt['mass'][1]:.0f} | {k(pt['crank1'][0])}-{k(pt['crank1'][1])} | "
              f"{k(pt['b1'][0])} / {k(pt['b1'][1])} / {k(pt['b1'][2])} | {k(pt['b2'][0])} / {k(pt['b2'][1])} | "
              f"{(pt['b1'][0]-h['b1'][0])/1000:+.1f} / {(pt['b1'][1]-h['b1'][1])/1000:+.1f} |")
    print("\nGM 4.3 V6: crank price not found, so not costed.")

    if "--plot" in sys.argv:
        sys.path.insert(0, HERE)
        import plot_sweep
        oe = oe_overlay()
        for p in oe:
            p["short"] = {"shared": "LS V8", "inline": "2JZ I6"}.get(p.get("layout"), "EZ36 flat-6") + f" {p['bore']:g}x{p['stroke']:g}"
        offs = [{"b1": (-10, -40), "mass": (8, -4)}, {"b1": (10, -38), "mass": (8, -4)}, {"b1": (8, 14), "mass": (8, -4)},
                {"b1": (-30, 16), "mass": (8, -10)}, {"b1": (8, -10), "mass": (8, -10)}]
        for p, o in zip(oe, offs):
            p["off"] = o
        plot_sweep.plot(sweep("billet specialist"), h, os.path.join(HERE, "sweep_200hp.png"), oe)
