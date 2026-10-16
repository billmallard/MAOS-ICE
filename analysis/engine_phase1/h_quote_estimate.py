"""Concept H castings: first-op machining and bureau casting, bottom-up estimate.

MANUFACTURING, AER-3328, 2026-10-16. Method: operation-by-operation time
estimate x sourced shop rates (job-shop costing; each hour figure is [E]),
plus sourced printed-sand rate x mold bounding box. Every input is a (low, high)
pair. Run: python3 h_quote_estimate.py
"""

# ---- sourced rates [S], read 2026-10-16 (sources in envelope v1 section 9)
RATE_4AX = (60, 90)       # $/h, 4-axis mill (fabcon.com, 2026-05)
RATE_5AX = (100, 200)     # $/h, 5-axis (fabcon.com; precisionam.com 2026-05)
RATE_HMC = (100, 175)     # $/h, HMC: no published rate found; taken as 5-axis band [E]
RATE_CAM = (50, 150)      # $/h, CAM programming (hotean.com, 2025-08)
SAND = 0.13               # $/in^3 of CAD bounding box, Hoosier, cleaned (page updated 2025-12-16)
IN3_PER_L = 61.024

# ---- per part number: one-time NRE (programming h, fixture $) and per-part work
# setups: list of (machine rate, setup hours per batch, cycle hours per part)
PARTS = {
    "case half (pair = 2 part numbers)": dict(
        n_per_engine=2, part_numbers=2,
        cam_h=(12, 22),           # per part number; pair shares the setup-B program
        fixture=(800, 2000),      # per part number: split-face plate + share of the pair tombstone
        setups=[
            (RATE_4AX, (1.0, 1.5), (1.2, 1.8)),   # A: split face, dowels, ~30 bolt holes
            (RATE_HMC, (1.0, 1.5), (2.5, 3.5)),   # B: on doweled pair, half share: mains, cam, thrust, 6 lifters, pad, studs, galleries
        ],
        inspect_h=(1.5, 3.0),     # first-article inspection per batch per part number
        box_mm=(560, 300, 160), core_frac=(0.0, 0.15)),
    "cylinder-bank block (L = R, 1 part number)": dict(
        n_per_engine=2, part_numbers=1,
        cam_h=(8, 14), fixture=(600, 1500),
        setups=[
            (RATE_4AX, (0.75, 1.25), (0.6, 1.0)),  # A: base pad, stud holes
            (RATE_4AX, (0.75, 1.25), (1.2, 2.0)),  # B: deck, 3 upper + 3 lower registers, head studs, coolant boss
        ],
        inspect_h=(1.0, 2.0),
        box_mm=(380, 190, 165), core_frac=(0.30, 0.50)),
    "bank head (mirrored L/R, 2 part numbers)": dict(
        n_per_engine=2, part_numbers=2,
        cam_h=(14, 25),           # per part number (second of a mirror pair is cheaper; not credited)
        fixture=(1000, 2500),
        setups=[
            (RATE_4AX, (0.75, 1.25), (0.8, 1.2)),  # A: deck, head-bolt holes, dowels
            (RATE_5AX, (1.0, 2.0), (2.5, 4.0)),    # B: seats, guides, plugs, injectors, rocker pads, port flanges
        ],
        inspect_h=(1.5, 3.0),
        box_mm=(380, 180, 110), core_frac=(0.50, 0.80)),
}

# ---- casting per part [E] except sand rate
SAND_MARGIN_MM = 50       # mold wall around the part, each side [E]
RIGGING = (1.15, 1.35)    # gating and risers enlarge the box [E]
POUR_Q1 = (400, 1200)     # pour, knock-out, cut-off, fettle, one-off [E]; Speed-Talk 2018: $200-2,000 per casting
POUR_Q5 = (250, 700)      # same melt serves the batch [E]
T6_LOT = (150, 400)       # one lot carries all castings in the order [E]; no published minimum found
IMPREG_LOT = (150, 350)   # one-off lot [E]; production is ~$13/part (Godfrey & Wing 2021)
RT_PER = (150, 600)       # 6-12 DR exposures at $15-50 plus tech time (NDT rate guide 2026) [E]


def add(a, b, k=1.0):
    return (a[0] + k * b[0], a[1] + k * b[1])


def first_op(p, qty):
    """Per-casting first-op cost at a batch of `qty` of that part number."""
    nre = (p["cam_h"][0] * RATE_CAM[0] + p["fixture"][0], p["cam_h"][1] * RATE_CAM[1] + p["fixture"][1])
    setup = (sum(r[0] * s[0] for r, s, c in p["setups"]), sum(r[1] * s[1] for r, s, c in p["setups"]))
    cycle = (sum(r[0] * c[0] for r, s, c in p["setups"]), sum(r[1] * c[1] for r, s, c in p["setups"]))
    insp = (p["inspect_h"][0] * RATE_4AX[0], p["inspect_h"][1] * RATE_4AX[1])
    per = lambda x, d: (x[0] / d, x[1] / d)
    t = add(per(nre, qty), per(setup, qty))
    t = add(t, cycle)
    t = add(t, per(insp, qty))
    marginal = add(cycle, per(add(setup, insp), qty))  # NRE paid once by the program
    return t, marginal, nre


def casting(p, qty, lot_share):
    x, y, z = (d + 2 * SAND_MARGIN_MM for d in p["box_mm"])
    box_in3 = x * y * z / 1e6 * IN3_PER_L
    core_in3 = p["box_mm"][0] * p["box_mm"][1] * p["box_mm"][2] / 1e6 * IN3_PER_L
    sand = (SAND * (box_in3 * RIGGING[0] + core_in3 * p["core_frac"][0]),
            SAND * (box_in3 * RIGGING[1] + core_in3 * p["core_frac"][1]))
    pour = POUR_Q1 if qty == 1 else POUR_Q5
    t = add(sand, pour)
    t = add(t, T6_LOT, lot_share)
    t = add(t, IMPREG_LOT, lot_share)
    t = add(t, RT_PER)
    return t, sand


if __name__ == "__main__":
    castings_per_engine = sum(p["n_per_engine"] for p in PARTS.values())
    eng = {k: (0.0, 0.0) for k in ("fo_q1", "fo_q5", "fo_marg", "c_q1", "c_q5", "nre")}
    print("| Part | First-op, qty 1 | First-op, qty 5 (each) | First-op marginal, NRE paid once | NRE per part number | Casting, qty 1 | Casting, qty 5 (each) | Printed sand |")
    print("|---|---|---|---|---|---|---|---|")
    for name, p in PARTS.items():
        q1, m, nre = first_op(p, 1)
        q5, _, _ = first_op(p, 5)
        # an engine order of 6 castings shares one T6 and one impregnation lot;
        # a qty-5 batch is 30 castings, and a lot is shared by about 15
        c1, sand = casting(p, 1, 1 / castings_per_engine)
        c5, _ = casting(p, 5, 1 / 15)
        n = p["n_per_engine"]
        # qty 1 per part number means one engine; mirror pairs and L=R blocks
        # are billed per part number, so NRE lands once per part number
        pn = p["part_numbers"]
        nre_eng = (nre[0] * pn, nre[1] * pn)
        # first engine: NRE once per part number + marginal per casting at batch = castings of that number
        batch1 = n / pn
        _, m1, _ = first_op(p, batch1)
        eng["fo_q1"] = add(eng["fo_q1"], add(nre_eng, m1, n))
        _, m5, _ = first_op(p, 5 * batch1)
        eng["fo_q5"] = add(eng["fo_q5"], add((nre_eng[0] / 5, nre_eng[1] / 5), m5, n))
        eng["fo_marg"] = add(eng["fo_marg"], m5, n)
        eng["nre"] = add(eng["nre"], nre_eng)
        eng["c_q1"] = add(eng["c_q1"], c1, n)
        eng["c_q5"] = add(eng["c_q5"], c5, n)
        f = lambda v: f"${v[0]:,.0f}-{v[1]:,.0f}"
        print(f"| {name} | {f(q1)} | {f(q5)} | {f(m)} | {f(nre)} | {f(c1)} | {f(c5)} | {f(sand)} |")
    f = lambda v: f"${v[0]/1000:.1f}k-{v[1]/1000:.1f}k"
    print("\nPer engine (6 castings):")
    print(f"- first-op, first engine (all NRE on it): {f(eng['fo_q1'])}")
    print(f"- first-op, batch of 5 engines (NRE spread over 5): {f(eng['fo_q5'])} per engine")
    print(f"- first-op, NRE paid once by the program, batch of 5: {f(eng['fo_marg'])} per engine")
    print(f"- first-op NRE, whole program (CAM + fixtures): {f(eng['nre'])}")
    print(f"- castings, first engine: {f(eng['c_q1'])}")
    print(f"- castings, batch of 5 engines: {f(eng['c_q5'])} per engine")
    print("\nPhase-1 model lines (member_200.py) for comparison: FIRST_OP $3.0k-12.0k; castings $4.4k-10.9k.")
