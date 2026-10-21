"""Concept H against an open conversion on a production core, against buying an Aeromomentum (AER-3632).

Exploration, not a ruling. Prints markdown tables; open_conversion_tables.md is the output.

Options, per family member:
  A     concept H, the program's made-from-files engine (scaling_sweep.py's model at 100 / 200 / 300 hp)
  B     an open conversion: a production core, the program's gearbox, the program's two-lane FADEC,
        open install documentation
  B0    an Aeromomentum engine with the program's FADEC in place of its ECU (the AER-3631 mule route),
        or a used Suzuki core behind Aeromomentum's own gearbox, bought standalone
  base  buy an Aeromomentum, closed, as sold

Definitions are REQUIREMENTS R-35 (cost: parts and services, 2026 USD, no labor, no propeller,
no engine mount; the mount is listed separately because every option needs one) and R-37 (mass:
installed dry, with exhaust, no fluids, radiator or propeller). Mid = geometric mean of low and high.

Cost bases:
  basis 1  the program's first engine, carrying all of its NRE
  basis 3  a builder making one engine from the program's published files (drawings free; the builder
           still pays quantity-one shop setup). MANUFACTURING, AER-3633: for instant-quote CNC parts the two
           bases are almost the same; basis 3 falls sharply only for castings with proven gating.

Tags: [S] sourced (sources/OPEN_CONVERSION_SOURCES_2026-10-21.md), [F] forum or snippet only,
[E] PROPULSION estimate, [MFG] MANUFACTURING's estimate on AER-3633 (2026-10-21, not a quote),
[A] assumed. None of these figures is a quote.

Run: python3 open_conversion.py > open_conversion_tables.md
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


SS = load(os.path.join(HERE, "..", "engine_crank", "scaling_sweep.py"), "scaling_sweep")
CF = SS.CH.CF                       # engine_phase0/cost_floor.py, the program's shared line items
HP = 0.745699872
ETA_GEAR = 0.97                     # [E] single-stage gearbox, as HAYABUSA_PLATFORM (0.97-0.98)
FMEP = 1.6e5                        # Pa, [A] as torsional_busa.py


def mid(lo, hi):
    return math.sqrt(lo * hi)


def tot(d, i=None):
    if i is None:
        return sum(v[0] for v in d.values()), sum(v[1] for v in d.values())
    return sum(v[i][0] for v in d.values()), sum(v[i][1] for v in d.values())


def k(x):
    return f"${x / 1e3:.1f}k"


# ---------------------------------------------------------------------------------------------
# 1. Ratings: what the core must do at the flange, as BMEP and piston speed, against its own car curve
# ---------------------------------------------------------------------------------------------
# OEM figures [S/F, sources file]: displacement L, stroke mm, peak power kW @ rpm, peak torque N m @ rpm
CORES = {
    "Suzuki K15B (in production, port injection)": dict(vd=1.462, stroke=85.0, z=4, p=(77.0, 6000), t=(138.0, 4400)),
    "Suzuki G15A (Aeromomentum AM15 core; out of production)": dict(vd=1.497, stroke=84.5, z=4, p=None, t=None),
    "Subaru EZ36 (2007-2019, out of production)": dict(vd=3.629, stroke=91.0, z=6, p=(191.0, 6000), t=(335.0, 4400)),
    "GM LS3 (crate engine still sold)": dict(vd=6.2, stroke=92.0, z=8, p=(321.0, 5900), t=(576.0, 4600)),
}
# The aircraft rating asked of each (R-2: takeoff at the flange; R-3: MCP >= 90 % of takeoff)
RATINGS = {
    "Suzuki K15B (in production, port injection)": [("100 hp takeoff", 100, 5800), ("90 hp MCP", 90, 5500)],
    "Subaru EZ36 (2007-2019, out of production)": [("200 hp takeoff", 200, 5000), ("180 hp MCP", 180, 4700)],
    "GM LS3 (crate engine still sold)": [("300 hp takeoff", 300, 4400), ("270 hp MCP", 270, 4100)],
}
# Aeromomentum's own ratings [S, A2 A3 A6], rpm at the crank; whether at the crank or the flange is not stated
AM_RATED = {"AM13 (1.298 L)": (1.298, 100, 5800, 75.5), "AM15 (1.497 L)": (1.497, 120, 5800, 84.5),
            "AM20T (1.998 L, turbo)": (1.998, 260, 5800, 86.0)}


def bmep(kw, vd_l, rpm):
    return kw * 1e3 * 120 / (vd_l * 1e-3 * rpm) / 1e5


def ratings():
    print("## 1. Ratings: what each core is asked for, as BMEP and piston speed\n")
    print("The core's own ceiling is its car peak-torque BMEP (the highest it reaches anywhere on the car curve). "
          "Takeoff power at the flange is crank power x 0.97.\n")
    print("| Core | Point | rpm | crank kW | BMEP (bar) | piston speed (m/s) | car peak-torque BMEP (bar) | car peak-power BMEP (bar) | margin to car peak torque |")
    print("|---|---|---|---|---|---|---|---|---|")
    out = {}
    for name, pts in RATINGS.items():
        c = CORES[name]
        b_t = c["t"][0] * 4 * math.pi / (c["vd"] * 1e-3) / 1e5
        b_p = bmep(c["p"][0], c["vd"], c["p"][1])
        for lab, hp, rpm in pts:
            kw = hp * HP / ETA_GEAR
            b = bmep(kw, c["vd"], rpm)
            sp = 2 * c["stroke"] / 1000 * rpm / 60
            out[(name, lab)] = (b, sp)
            print(f"| {name} | {lab} | {rpm:,} | {kw:.1f} | {b:.1f} | {sp:.1f} | {b_t:.1f} | {b_p:.1f} | {1 - b / b_t:.0%} |")
    print("\nYardsticks (HAYABUSA_PLATFORM section 2): Rotax 912 ULS 11.2 bar / 11.8 m/s at takeoff; concept H 10.3 bar / 11.2 m/s; "
          "Viking and Aeromomentum about 16 m/s.\n")
    print("**Aeromomentum's own ratings, as BMEP** (a check the vendor's figures cannot fake; crank power assumed):\n")
    print("| Model | rated | rpm | BMEP if at the crank (bar) | piston speed (m/s) |")
    print("|---|---|---|---|---|")
    for m, (vd, hp, rpm, st) in AM_RATED.items():
        print(f"| {m} | {hp} hp | {rpm:,} | {bmep(hp * HP, vd, rpm):.1f} | {2 * st / 1000 * rpm / 60:.1f} |")
    print()
    return out


# ---------------------------------------------------------------------------------------------
# 2. R-25 with one plug per cylinder: brake power left when one cylinder's coil or plug fails
# ---------------------------------------------------------------------------------------------
def one_dead(z, bmep_mcp_bar):
    imep = bmep_mcp_bar * 1e5 + FMEP
    return ((z - 1) / z * imep - FMEP) / (imep - FMEP)


def lane_loss(r):
    print("## 2. R-25 on a one-plug-per-cylinder core: MCP left after one coil or plug fails\n")
    print("Method as torsional_busa.py section 4: ((z-1)/z x IMEP - FMEP) / BMEP at the MCP point, FMEP 1.6 bar [A]. "
          "Two ECUs, two crank sensors and two power feeds can be made dual on any core; the plug and its coil cannot, "
          "unless the head has two plugs per cylinder.\n")
    print("| Core | cylinders | MCP BMEP (bar) | MCP left, one cylinder dead | R-25 asks |")
    print("|---|---|---|---|---|")
    for name, pts in RATINGS.items():
        z = CORES[name]["z"]
        b = r[(name, pts[1][0])][0]
        print(f"| {name} | {z} | {b:.1f} | {one_dead(z, b):.0%} | 90 % |")
    for lab, z, b in (("Aeromomentum AM13 / AM15 (one plug, one ECU, as sold)", 4, 10.5), ("Concept H (two plugs per cylinder by design)", 6, 9.3)):
        left = one_dead(z, b) if "H" not in lab[:9] else 1.0
        note = f"{left:.0%}" if "H" not in lab[:9] else "about 97-99 % (one plug of two lost per cylinder; not computed here)"
        print(f"| {lab} | {z} | {b:.1f} | {note} | 90 % |")
    print()


# ---------------------------------------------------------------------------------------------
# 3. Installed dry mass (R-37)
# ---------------------------------------------------------------------------------------------
NORMALIZER_KG = (14.0, 21.5)        # turbo + intercooler, RECOST_PHASE1B section 7 [E]
NORMALIZER_COST = (2000, 4500)      # cost_v1.py NORM_TURBO [MFG envelope 10]

MASS = {
    "B-100, Suzuki 1.5 L I4 core, program gearbox": {
        "core with OE starter and alternator, no OE manifolds [E: AM15 complete 83.9 kg less its gearbox; K15B 85 kg, secondary]": (72.0, 85.0),
        "program gearbox with coupling and slip clutch [MFG AER-3633]": (6.0, 10.0),
        "adapter plate and flywheel hub [E]": (2.0, 4.0),
        "second FADEC lane: ECU, crank sensor, harness [E, as HAYABUSA]": (2.0, 3.0),
        "second generator for lane B (R-25) [E]": (2.0, 4.0),
        "exhaust, 4-into-1 stainless [E]": (4.0, 7.0),
        "intake plenum and filter [E]": (1.5, 3.0),
        "oil system for aircraft attitudes: baffled sump or accumulator [E]": (0.5, 2.0),
        "fuel pumps and filters at the engine [E]": (1.0, 2.0),
    },
    "B-200, Subaru EZ36 core, program gearbox": {
        "core with OE starter and alternator [E: no OEM figure found; Eggenfellner E6 3.0 L package about 159 kg with gearbox, secondary]": (125.0, 145.0),
        "program gearbox with coupling and slip clutch [MFG AER-3633]": (10.0, 16.0),
        "adapter plate and flywheel hub [E]": (3.0, 5.0),
        "second FADEC lane [E]": (2.5, 4.0),
        "second generator for lane B [E]": (2.0, 4.0),
        "exhaust, two 3-into-1 [E]": (6.0, 10.0),
        "intake [E]": (2.0, 4.0),
        "oil system for aircraft attitudes [E]": (1.0, 4.0),
        "fuel pumps and filters [E]": (1.0, 2.0),
    },
    "B-300, GM LS3 crate core, program gearbox": {
        "long block with starter and alternator [F: 375 lb undressed to 435 lb dressed, sources conflict]": (175.0, 197.0),
        "program gearbox, about 840 N m at 2,550 propeller rpm, 0.020-0.036 kg per N m [E, CRANK_AND_SCALING 5]": (17.0, 30.0),
        "adapter plate and flywheel hub [E]": (3.0, 6.0),
        "second FADEC lane [E]": (3.0, 4.5),
        "second generator for lane B [E]": (2.0, 4.0),
        "exhaust, two 4-into-1 [E]": (8.0, 14.0),
        "intake [E]": (3.0, 5.0),
        "oil system for aircraft attitudes [E]": (1.0, 5.0),
        "fuel pumps and filters [E]": (1.0, 2.0),
    },
    "Aeromomentum AM15, as sold (baseline)": {
        "AM15 with gearbox, starter, alternator, ECU, harness [S, A3: 185 lb]": (83.9, 83.9),
        "exhaust header and muffler (sold separately) [E]": (4.0, 7.0),
    },
    "Aeromomentum AM13, as sold (baseline)": {
        "AM13 with gearbox, starter, alternator, ECU, harness [S, A2: 170 lb]": (77.1, 77.1),
        "exhaust header and muffler [E]": (4.0, 7.0),
    },
    "B0, AM15 with the program FADEC in place of its ECU": {
        "AM15 as sold [S]": (83.9, 83.9),
        "exhaust [E]": (4.0, 7.0),
        "second FADEC lane, second crank sensor; the AM ECU removed [E]": (1.5, 2.5),
        "second generator for lane B [E]": (2.0, 4.0),
    },
}
R37 = {100: 90, 200: 150, 300: 210}


def h_point(hp):
    """Concept H through scaling_sweep.py's model. 100 hp: flat-4 on H's module at 2,700 rpm (RANKING_PHASE1
    section 5). 200 hp: H as drawn. 300 hp: a second, larger flat-6 module at 3,300 rpm (phase-2 work, not
    designed; an extrapolation of the model)."""
    v1 = math.pi / 4 * 104.8 ** 2 * 101.6 / 1e6
    if hp == 100:
        n, N, vd, B, S = 4, 2700, 4 * v1, 104.8, 101.6
    elif hp == 200:
        n, N, vd, B, S = 6, 3300, 6 * v1, 104.8, 101.6
    else:
        vd = hp * HP * 1e3 * 120 / (SS.BMEP * 1e5 * 3300) * 1e3
        v = vd / 6 / 1000
        S = (4 * v * 0.97 ** 2 / math.pi) ** (1 / 3) * 1000
        B = S / 0.97
        n, N = 6, 3300
    pt = dict(n=n, N=N, vd=vd, bore=B, stroke=S, sp=2 * S / 1000 * N / 60, ratio=1.0, geared=False,
              drive_kg=(0.0, 0.0), drive_cost=(CF.DRIVE["direct"], CF.DRIVE["direct"]), route="billet specialist")
    return SS.evaluate(pt)


def mass():
    print("## 3. Installed dry mass (R-37 definition)\n")
    rows = {}
    for opt, d in MASS.items():
        print(f"**{opt}**\n")
        print("| Line | low (kg) | high (kg) |")
        print("|---|---|---|")
        for kk, (lo, hi) in d.items():
            print(f"| {kk} | {lo:.1f} | {hi:.1f} |")
        lo, hi = tot(d)
        rows[opt] = (lo, hi)
        print(f"| **Installed dry, naturally aspirated** | **{lo:.0f}** | **{hi:.0f}** |")
        print(f"| with the program's normalizer (R-5, R-7) | {lo + NORMALIZER_KG[0]:.0f} | {hi + NORMALIZER_KG[1]:.0f} |\n")
    print("**Summary against R-37** (proposed: 90 / 150 / 210 kg):\n")
    print("| Member | Option | NA (kg) | normalized (kg) | R-37 |")
    print("|---|---|---|---|---|")
    for hp in (100, 200, 300):
        p = h_point(hp)
        lab = "A, concept H (scaling_sweep model; its 9 kg turbo is in the figure)" + (" [extrapolated: module not designed]" if hp == 300 else "")
        print(f"| {hp} hp | {lab} | - | {p['mass'][0]:.0f}-{p['mass'][1]:.0f} | {R37[hp]} |")
        for opt, (lo, hi) in rows.items():
            if opt.startswith(f"B-{hp}") or (hp == 100 and ("AM1" in opt or opt.startswith("B0"))):
                print(f"| {hp} hp | {opt} | {lo:.0f}-{hi:.0f} | {lo + NORMALIZER_KG[0]:.0f}-{hi + NORMALIZER_KG[1]:.0f} | {R37[hp]} |")
        if hp == 200:
            print("| 200 hp | Aeromomentum AM20T, turbocharged to its rating (breaks R-5) [S, A6: 285 lb] | - | 129 (boosted, not normalized) | 150 |")
    print("\nConcept H at 200 hp is 148-158 kg on phase 1b's own build-up (RECOST_PHASE1B section 7); the sweep model gives 143-145 kg. "
          "The sweep is used here so the three members are on one model.\n")
    return rows


# ---------------------------------------------------------------------------------------------
# 4. Cost, R-35 definition, basis 1 and basis 3
# ---------------------------------------------------------------------------------------------
def heat_line(kw):
    return (CF.COOLING_PER_100KW[0] * kw / 100, CF.COOLING_PER_100KW[1] * kw / 100)


COMMON_100 = {
    "FADEC, two lanes (cost_floor.py, same line as H) [E]": (CF.FADEC, CF.FADEC),
    "second crank sensor and trigger [E]": ((100, 300), (100, 300)),
    "second generator and regulator for lane B (cost_floor START_ALT) [E]": (CF.START_ALT, CF.START_ALT),
    "cooling at 78 kW to coolant and oil (cost_floor rate) [E]": (heat_line(78), heat_line(78)),
    "fuel system, two pumps, E15-rated (cost_floor) [E]": (CF.FUEL["SI"], CF.FUEL["SI"]),
    "exhaust (cost_floor) [E]": (CF.EXHAUST, CF.EXHAUST),
    "intake plenum and filter [E]": ((200, 500), (200, 500)),
    "oil system for aircraft attitudes: baffles, pickup, accumulator or dry sump [E]": ((300, 1200), (300, 1200)),
    "misc: fasteners, seals, filters (cost_floor) [E]": (CF.MISC, CF.MISC),
}

COST = {   # each line: (basis 1 band, basis 3 band)
    "B-100, Suzuki 1.5 L I4 core, program gearbox": dict({
        "used core, Suzuki M15A / K15B class [MFG AER-3633]": ((600, 1500), (600, 1500)),
        "teardown, crack check, rebuild to the program's measurement sheet; builder assembles [MFG]": ((1500, 3800), (1500, 3800)),
        "program gearbox, catalog gear pair, billet case [MFG]": ((3300, 9600), (2700, 8100)),
        "adapter plate and drilled OE flywheel as hub [MFG]": ((1100, 2800), (800, 2100)),
    }, **COMMON_100),
    "B-100 alt, new Aeromomentum long block behind the program gearbox": dict({
        "Aeromomentum AM15 long block, new [S, A12: $4,295]": ((4295, 4295), (4295, 4295)),
        "program gearbox, catalog gear pair [MFG]": ((3300, 9600), (2700, 8100)),
        "adapter plate and hub [MFG]": ((1100, 2800), (800, 2100)),
    }, **COMMON_100),
    "B-100 alt, used Suzuki core behind Aeromomentum's gearbox (bought standalone)": dict({
        "used core [MFG]": ((600, 1500), (600, 1500)),
        "rebuild to the measurement sheet [MFG]": ((1500, 3800), (1500, 3800)),
        "Aeromomentum gearbox complete GB1-A01 [S, A12: $2,495] and mounting plate set [S: $477]": ((2972, 2972), (2972, 2972)),
        "fit check of the AM gearbox to the chosen core's face, hub [E]": ((200, 1000), (200, 800)),
    }, **COMMON_100),
}

COMMON_200 = {
    "FADEC, two lanes [E]": (CF.FADEC, CF.FADEC),
    "second crank sensor [E]": ((100, 300), (100, 300)),
    "second generator for lane B [E]": (CF.START_ALT, CF.START_ALT),
    "cooling at 156 kW [E]": (heat_line(156), heat_line(156)),
    "fuel system [E]": (CF.FUEL["SI"], CF.FUEL["SI"]),
    "exhaust, two banks (cost_floor x 1.5) [E]": ((450, 1200), (450, 1200)),
    "intake [E]": ((300, 800), (300, 800)),
    "oil system for aircraft attitudes [E]": ((400, 1500), (400, 1500)),
    "misc [E]": (CF.MISC, CF.MISC),
}
COST["B-200, Subaru EZ36 core, program gearbox"] = dict({
    "used EZ36 core, delivered [MFG]": ((1500, 4600), (1500, 4600)),
    "teardown, inspection, rebuild; builder assembles [MFG]": ((3200, 7200), (3200, 7200)),
    "program gearbox, catalog module-4 pair, own case with the bellhousing face [MFG]": ((5100, 13900), (4200, 11800)),
    "adapter plate and hub (a separate plate only if one gearbox serves both cores) [MFG]": ((1600, 4300), (1200, 3400)),
}, **COMMON_200)
COMMON_300 = {kk.replace("156", "234"): (heat_line(234), heat_line(234)) if "cooling" in kk else v for kk, v in COMMON_200.items()}
COST["B-300, GM LS3 crate core, program gearbox"] = dict({
    "LS3 long block, new crate (19435106: $7,677 sale to $9,656 MSRP) [S]": ((7677, 9656), (7677, 9656)),
    "program gearbox, about 500 N m input; MFG's EZ36 line x 1.2 [E]": ((6100, 16700), (5000, 14200)),
    "adapter plate and hub [E, MFG EZ36 line]": ((1600, 4300), (1200, 3400)),
}, **COMMON_300)

BASE = {   # bought, as sold; R-35 adds what the price leaves out
    "Aeromomentum AM13, as sold": {
        "AM13 with gearbox, starter, alternator, ECU [S, A2]": (11500, 12600),
        "radiator [S, A13]": (205, 345),
        "exhaust header and muffler [S, A13: $735 + $139]": (874, 874),
        "hoses, oil cooler, fuel system parts [E]": (600, 1300),
    },
    "Aeromomentum AM15, as sold": {
        "AM15 with gearbox, starter, alternator, ECU [S, A3]": (13000, 14100),
        "radiator [S, A13]": (205, 345),
        "exhaust header and muffler [S, A13]": (874, 874),
        "hoses, oil cooler, fuel system parts [E]": (600, 1300),
    },
    "B0, AM15 with the program FADEC in place of its ECU": {
        "AM15 as sold [S]": (13000, 14100),
        "radiator, exhaust, hoses [S + E, as above]": (1679, 2519),
        "program FADEC, two lanes, less the AM ECU's $450 resale [E]": (CF.FADEC[0] - 450, CF.FADEC[1] - 450),
        "second crank sensor, second generator [E]": (500, 1200),
    },
    "Aeromomentum AM20T, as sold (turbocharged to 260 hp; breaks R-5)": {
        "AM20T [S, A6]": (27995, 27995),
        "radiator, exhaust, hoses [E, AM15 lines x 1.5]": (2500, 3800),
    },
}
MOUNT = {100: ((1400, 3700), (1300, 3200)), 200: ((1800, 4500), (1600, 4000)), 300: ((2000, 5000), (1800, 4500))}   # builder TIG [MFG]


def cost():
    print("## 4. Cost, R-35 definition (no labor, no propeller, no engine mount)\n")
    summary = []
    for opt, d in COST.items():
        print(f"**{opt}**\n")
        print("| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |")
        print("|---|---|---|---|---|")
        for kk, (b1, b3) in d.items():
            print(f"| {kk} | ${b1[0]:,.0f} | ${b1[1]:,.0f} | ${b3[0]:,.0f} | ${b3[1]:,.0f} |")
        l1, h1 = tot(d, 0)
        l3, h3 = tot(d, 1)
        print(f"| **Total, naturally aspirated** | **${l1:,.0f}** | **${h1:,.0f}** | **${l3:,.0f}** | **${h3:,.0f}** |\n")
        summary.append((opt, (l1, mid(l1, h1), h1), (l3, mid(l3, h3), h3)))
    for opt, d in BASE.items():
        print(f"**{opt}**\n")
        print("| Line | low | high |")
        print("|---|---|---|")
        for kk, (lo, hi) in d.items():
            print(f"| {kk} | ${lo:,.0f} | ${hi:,.0f} |")
        lo, hi = tot(d)
        print(f"| **Total** | **${lo:,.0f}** | **${hi:,.0f}** |\n")
        summary.append((opt, (lo, mid(lo, hi), hi), (lo, mid(lo, hi), hi)))

    print("**Summary** (low / mid / high; a bought engine is the same on both bases):\n")
    print("| Member | Option | basis 1, program's first engine | basis 3, builder from published files | with the normalizer, basis 1 |")
    print("|---|---|---|---|---|")
    for hp in (100, 200, 300):
        p = h_point(hp)
        b1 = p["b1"]
        b3 = (0.85 * b1[0], 0.85 * b1[1], b1[2])
        lab = "A, concept H (sweep model; turbo included)" + (" [extrapolated]" if hp == 300 else "")
        print(f"| {hp} hp | {lab} | {k(b1[0])} / {k(b1[1])} / {k(b1[2])} | about {k(b3[0])} / {k(b3[1])} / {k(b3[2])} [E: 0.85-1.0 x basis 1] | (included) |")
        for opt, s1, s3 in summary:
            tag = opt.split(",")[0]
            if tag.startswith(f"B-{hp}") or (hp == 100 and ("AM13" in opt or "AM15" in opt or tag == "B0")) or (hp == 200 and "AM20T" in opt):
                norm = "breaks R-5" if "AM20T" in opt else f"{k(s1[0] + NORMALIZER_COST[0])} / {k(mid(s1[0] + NORMALIZER_COST[0], s1[2] + NORMALIZER_COST[1]))} / {k(s1[2] + NORMALIZER_COST[1])}"
                print(f"| {hp} hp | {opt} | {k(s1[0])} / {k(s1[1])} / {k(s1[2])} | {k(s3[0])} / {k(s3[1])} / {k(s3[2])} | {norm} |")
    print("\nEngine mount, every option, builder TIG [MFG]: "
          + "; ".join(f"{hp} hp ${m[0][0]/1e3:.1f}k-{m[0][1]/1e3:.1f}k (basis 3 ${m[1][0]/1e3:.1f}k-{m[1][1]/1e3:.1f}k)" for hp, m in MOUNT.items()) + ".\n")
    print("Concept H's basis 3 is not computed line by line. MANUFACTURING (AER-3633) reads a builder's quantity-one price as close to "
          "the first engine's, because a job shop writes its own CAM from a STEP; only published gating takes a real cut. "
          "0.85-1.0 x basis 1 is that reading, not a build-up. Basis 2 (five engines, NRE paid once) is lower: "
          f"{k(h_point(200)['b2'][0])} / {k(h_point(200)['b2'][1])} at 200 hp.\n")
    return summary


# ---------------------------------------------------------------------------------------------
# 5. Time and effort to a first ground run and a first flight (program calendar, weeks)
# ---------------------------------------------------------------------------------------------
# Each task: (low, high) weeks, and the tasks it waits on. Critical path = longest chain. [E] unless tagged.
SCHED = {
    "A, concept H 200 hp": {
        "finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard": ((26, 52), []),
        "RFQ path exists (AER-3330, open since 2026-10-16)": ((4, 26), []),
        "crank: quote, make, nitride, grind, balance [S: 18-20 weeks lead]": ((20, 26), ["finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard", "RFQ path exists (AER-3330, open since 2026-10-16)"]),
        "castings: print, pour, T6, RT, impregnate; one remake allowed [S envelope: 2-4 weeks per pour]": ((6, 12), ["finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard", "RFQ path exists (AER-3330, open since 2026-10-16)"]),
        "first-op machining and inspection [S envelope: 2-6 weeks]": ((4, 10), ["castings: print, pour, T6, RT, impregnate; one remake allowed [S envelope: 2-4 weeks per pour]"]),
        "FADEC: two lanes to ground-run standard (shared with B; AER-3631 starts it)": ((26, 52), []),
        "assembly, stand build, first run": ((6, 12), ["crank: quote, make, nitride, grind, balance [S: 18-20 weeks lead]", "first-op machining and inspection [S envelope: 2-6 weeks]", "FADEC: two lanes to ground-run standard (shared with B; AER-3631 starts it)"]),
        "stand program to flight: calibration, torsional survey, 50-100 h endurance, teardown": ((16, 30), ["assembly, stand build, first run"]),
        "installation in an airframe and taxi tests (airframe not chosen; MAOS paused)": ((8, 16), ["stand program to flight: calibration, torsional survey, 50-100 h endurance, teardown"]),
    },
    "B, open conversion, 100 hp Suzuki I4": {
        "buy and rebuild a core [MFG: 1-3 + 3-8 weeks]": ((4, 11), []),
        "gearbox: rate, design, draw [E]": ((8, 16), []),
        "gearbox, adapter and hub: make [MFG: 4-8 weeks catalog pair]": ((4, 8), ["gearbox: rate, design, draw [E]"]),
        "FADEC: two lanes to ground-run standard (shared; AER-3631 starts it)": ((26, 52), []),
        "assembly, stand build, first run": ((4, 8), ["buy and rebuild a core [MFG: 1-3 + 3-8 weeks]", "gearbox, adapter and hub: make [MFG: 4-8 weeks catalog pair]", "FADEC: two lanes to ground-run standard (shared; AER-3631 starts it)"]),
        "stand program to flight: calibration, torsional survey with the real propeller, 50-100 h, teardown": ((12, 24), ["assembly, stand build, first run"]),
        "installation in an airframe and taxi tests": ((8, 16), ["stand program to flight: calibration, torsional survey with the real propeller, 50-100 h, teardown"]),
    },
    "B, open conversion, 200 hp EZ36": {
        "buy and rebuild a core [MFG: 1-3 + 3-8 weeks]": ((4, 11), []),
        "gearbox: rate, design, draw [E]": ((10, 20), []),
        "gearbox, adapter and hub: make [MFG: 4-8, custom pair 8-14 weeks]": ((6, 14), ["gearbox: rate, design, draw [E]"]),
        "FADEC: two lanes, 6 cylinders (shared)": ((26, 52), []),
        "assembly, stand build, first run": ((4, 8), ["buy and rebuild a core [MFG: 1-3 + 3-8 weeks]", "gearbox, adapter and hub: make [MFG: 4-8, custom pair 8-14 weeks]", "FADEC: two lanes, 6 cylinders (shared)"]),
        "stand program to flight": ((12, 24), ["assembly, stand build, first run"]),
        "installation in an airframe and taxi tests": ((8, 16), ["stand program to flight"]),
    },
    "Baseline: buy an AM15": {
        "order and delivery [A: no lead time published]": ((4, 12), []),
        "first run on the vendor's ECU (no program FADEC)": ((1, 2), ["order and delivery [A: no lead time published]"]),
        "installation in an airframe and taxi tests": ((8, 16), ["first run on the vendor's ECU (no program FADEC)"]),
    },
    "B0, AM15 with the program FADEC (AER-3631)": {
        "order and delivery [A]": ((4, 12), []),
        "FADEC: two lanes to ground-run standard (shared)": ((26, 52), []),
        "first run on the program FADEC, on the stand": ((2, 4), ["order and delivery [A]", "FADEC: two lanes to ground-run standard (shared)"]),
        "stand program to flight: FADEC fault injection, 25-50 h": ((6, 12), ["first run on the program FADEC, on the stand"]),
        "installation in an airframe and taxi tests": ((8, 16), ["stand program to flight: FADEC fault injection, 25-50 h"]),
    },
}
LABOR_H = {   # builder hours to a ready-to-install engine, one engine from published files [E; MFG lines named]
    "A, concept H 200 hp": {"assemble a bare-casting engine: fit liners, seats, guides, bearings, crank, cam, valvetrain": (120, 250),
                            "two-lane FADEC harness and calibration": (60, 140), "cooling, exhaust, intake, normalizer": (60, 120),
                            "engine mount, builder TIG [MFG]": (40, 80), "first runs on a stand": (20, 40)},
    "B, open conversion, 100 hp Suzuki I4": {"core teardown and rebuild to the measurement sheet [MFG]": (25, 45),
                                              "gearbox assembly: preload, backlash, coupling [E]": (15, 35),
                                              "two-lane FADEC harness and calibration": (60, 140), "cooling, exhaust, intake, oil system": (40, 80),
                                              "engine mount, builder TIG [MFG]": (40, 80), "first runs on a stand": (15, 30)},
    "B, open conversion, 200 hp EZ36": {"core teardown and rebuild [MFG]": (35, 65), "gearbox assembly [E]": (20, 40),
                                        "two-lane FADEC harness and calibration": (70, 150), "cooling, exhaust, intake, oil system": (50, 100),
                                        "engine mount, builder TIG [MFG]": (50, 90), "first runs on a stand": (15, 30)},
    "Baseline: buy an AM15": {"cooling, exhaust, fuel and wiring to the vendor's manual [E]": (40, 80),
                              "engine mount (builder TIG, or bought if the airframe kit has one) [MFG]": (0, 80)},
}


def critical(tasks):
    memo = {}

    def finish(t, i):
        if (t, i) not in memo:
            d, deps = tasks[t]
            memo[(t, i)] = d[i] + max((finish(p, i) for p in deps), default=0)
        return memo[(t, i)]
    return {t: (finish(t, 0), finish(t, 1)) for t in tasks}


def schedule():
    print("## 5. Program calendar to a first ground run and a first flight\n")
    print("Weeks from a go decision, low / high, as the longest chain through the task list below each option. Tasks without a "
          "dependency run in parallel. Every duration is [E] unless tagged. The airframe is assumed available when the engine is ready; "
          "it is not (MAOS is paused), and that is the same for every option.\n")
    print("| Option | first ground run (weeks) | first flight (weeks) | the chain that sets the first run |")
    print("|---|---|---|---|")
    for opt, tasks in SCHED.items():
        f = critical(tasks)
        run = [t for t in tasks if "first run" in t][0]
        fl = [t for t in tasks if t.startswith("installation")][0]
        deps = tasks[run][1]
        driver = max(deps, key=lambda p: f[p][1]) if deps else "-"
        print(f"| {opt} | {f[run][0]}-{f[run][1]} | {f[fl][0]}-{f[fl][1]} | {driver} |")
    print()
    for opt, tasks in SCHED.items():
        print(f"<details><summary>{opt}: tasks</summary>\n")
        print("| Task | weeks | waits on |")
        print("|---|---|---|")
        for t, (d, deps) in tasks.items():
            print(f"| {t} | {d[0]}-{d[1]} | {'; '.join(deps) if deps else '-'} |")
        print("\n</details>\n")
    print("**Builder hours to a ready-to-install engine** (not in R-35's cost):\n")
    print("| Option | hours |")
    print("|---|---|")
    for opt, d in LABOR_H.items():
        lo, hi = tot(d)
        print(f"| {opt} | {lo:.0f}-{hi:.0f} |")
    print()


if __name__ == "__main__":
    r = ratings()
    lane_loss(r)
    mass()
    cost()
    schedule()
