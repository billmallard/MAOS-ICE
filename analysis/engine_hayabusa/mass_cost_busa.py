"""Installed mass, first-engine cost and a durability bracket for a Hayabusa conversion (AER-3525, questions 2, 6, 7).

Mass is on REQUIREMENTS R-37's "installed dry" definition: engine, reduction
drive, normalizer (if fitted), FADEC, starter, generators and exhaust; no
fluids, radiator or propeller. The radiator system is its own line, from
rating_busa.py (radiator.py at the Hayabusa's MCP heat).

Cost is on R-35's definition and on basis 1 (the first engine carries its
NRE): parts and services, 2026 USD, excluding builder labor and the propeller.
Builder labor is estimated separately, in hours. Lines shared with concept H
reuse the program's estimates unchanged (analysis/engine_phase0/cost_floor.py,
CRANK_AND_SCALING.md section 5 for the gearbox), so the comparison with H is on
one basis. Mid = geometric mean of low and high, as in phases 1 and 1b.

Tags: [S] sourced (sources/HAYABUSA_SOURCES_2026-10-19.md), [F] forum or a
search snippet only, [E] PROPULSION estimate, [MFG] MANUFACTURING's envelope
estimate on AER-3526 (2026-10-19, first engine). None of these is a quote.

Run: python3 mass_cost_busa.py
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cost_floor", os.path.join(HERE, "..", "engine_phase0", "cost_floor.py"))
CF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CF)

HP = 0.745699872
# Aircraft rating from rating_busa.py (takeoff high band, MCP high band)
P_TO_CRANK = 105.0           # kW at 7,000 rpm
P_MCP_CRANK = 83.0           # kW at 6,500 rpm
RATIO = 2.92                 # 7,000 crank to ~2,400 propeller rpm
T_PROP = P_TO_CRANK * 0.975 * 1e3 / (7000 / RATIO * 2 * math.pi / 60)   # N m at the propeller, takeoff
HEAT_MCP = 67.0 + 14.0       # kW to coolant and oil at MCP (rating_busa.py)

# Gearbox: the program's proven-class build-up and mass rate (CRANK_AND_SCALING.md section 5;
# scaling_sweep.py GEARBOX_B1, GEARBOX_KG_PER_NM). No Hayabusa PSRU exists to buy (sources, section D).
GEARBOX_B1 = (2900, 9800)
GEARBOX_KG_PER_NM = (0.020, 0.036)
GBP_USD = 1.33               # [A] exchange rate for the SBD price

MASS = {   # kg, installed dry (R-37)
    "engine with its integral gearbox, clutch, starter and stator [F, H21 H22]": (86.0, 92.0),
    "dry-sump conversion, net of the wet pan: pump, tank, lines [E]": (2.0, 4.0),
    "reduction gearbox at 0.020-0.036 kg per N m of propeller torque [E]": (GEARBOX_KG_PER_NM[0] * T_PROP, GEARBOX_KG_PER_NM[1] * T_PROP),
    "adapter plate and soft coupling [E, MFG]": (2.0, 4.0),
    "two-lane FADEC: second ECU, second coils, second crank sensor, harness [E]": (2.5, 4.0),
    "second generator for lane B (R-25 two power feeds) [E]": (2.0, 4.0),
    "exhaust, 4-into-1 stainless [E]": (4.0, 7.0),
    "intake plenum and air filter [E]": (1.5, 3.0),
    "engine mount, 4130 tube bed with isolators [E, MFG]": (3.0, 5.0),
    "fuel pumps and filters at the engine [E]": (1.0, 2.0),
}
NORMALIZER_KG = (14.0, 21.5)  # turbo system + intercooler, envelope 10 / RECOST_PHASE1B section 7 [E]
RADIATOR_SYSTEM_KG = (20.1, 21.4)   # rating_busa.py section 6 design points, 68-83 kW MCP

COST = {   # USD, basis 1, R-35 definition
    "used Gen 2 core, 7k-32k miles (eBay snapshot) [S, H24]": (3000, 3820),
    "aircraft-duty rebuild parts: cam chain and tensioner, all shells, rings, gaskets [S partial H39-H42, E]": (1000, 1500),
    "11:1 pistons for sustained full throttle on MON 85 (knock section) [E]": (700, 1100),
    "machine shop: crack test of crank and rods, valve job, inspection [E]": (500, 1200),
    "dry sump: SBD kit GBP 1,160 ex VAT plus tank, lines and fittings [S D30 + E]": (1160 * GBP_USD + 400, 1160 * GBP_USD + 800),
    "reduction gearbox, proven-class, made (none to buy, P section 1) [E, CRANK_AND_SCALING 5]": GEARBOX_B1,
    "adapter plate and crank-side hub [MFG AER-3526]": (1100, 4500),
    "torsional elastic coupling [MFG AER-3526]": (300, 1000),
    "FADEC, two lanes (cost_floor.py, same line as H) [E]": CF.FADEC,
    "second coil per cylinder, 4 x D585 class (cost_floor.py) [S-MFG]": (CF.DUAL_LANE_PER_CYL[0] * 4, CF.DUAL_LANE_PER_CYL[1] * 4),
    "second plug per cylinder: sleeved plug tubes, two scrap heads, section, fixture, prove-out [MFG AER-3526; outside the envelope until a section proves it]": (2100, 7300),
    "second crank sensor and trigger wheel [E]": (100, 300),
    "second generator and regulator for lane B (cost_floor START_ALT as the allowance) [E]": CF.START_ALT,
    "cooling at 81 kW (cost_floor.py rate per 100 kW) [E]": (CF.COOLING_PER_100KW[0] * HEAT_MCP / 100, CF.COOLING_PER_100KW[1] * HEAT_MCP / 100),
    "fuel system, two pumps, E15-rated hoses (cost_floor.py) [E]": CF.FUEL["SI"],
    "exhaust (cost_floor.py) [E]": CF.EXHAUST,
    "intake plenum and filter [E]": (200, 500),
    "engine mount, 4130 tube bed, 4 isolators, jig; builder TIG (shop route $3.0k-8.4k) [MFG AER-3526]": (1400, 3700),
    "misc: fasteners, seals, filters (cost_floor.py) [E]": CF.MISC,
}
NORMALIZER_COST = (2000, 4500)   # cost_v1.py NORM_TURBO [MFG 10]

LABOR_H = {   # builder hours [E]
    "teardown, inspection, rebuild with new pistons": (30, 50),
    "dry sump fit": (10, 20),
    "gearbox, adapter and coupling fit and alignment": (40, 100),
    "FADEC wiring, two lanes, and calibration on the stand": (60, 140),
    "cooling, exhaust and intake fabrication": (40, 80),
    "engine mount welding, builder TIG, skill B3 (MFG AER-3526)": (40, 80),
    "first runs and a torsional survey on the stand": (20, 40),
}

# Durability bracket. The only high-load evidence: Radical's quoted rebuild interval for its
# 1340 engines, 90-100 h of race running, 205 bhp at 9,500 rpm [F, D1 D2 D3]; 1500 engines 40 h [F, D1 D2].
RADICAL_H = (90.0, 100.0)
RACE_MEAN_RPM = (7500.0, 9000.0)   # [A] mean rpm over a race lap, not peak
AIR_MCP_RPM = (5800.0, 6500.0)
WEAR_EXP = (1.0, 3.0)              # [A] hours scale as rpm^-k: k=1 sliding distance; k=3 Archard with inertia load ~ rpm^2


def mid(lo, hi):
    return math.sqrt(lo * hi)


def tot(d):
    return sum(v[0] for v in d.values()), sum(v[1] for v in d.values())


if __name__ == "__main__":
    print(f"Propeller torque at takeoff: {T_PROP:.0f} N m ({P_TO_CRANK:.0f} kW crank, 7,000 rpm, {RATIO}:1).\n")
    print("## 1. Installed dry mass (R-37 definition)\n")
    print("| Line | low (kg) | high (kg) |")
    print("|---|---|---|")
    for k, (lo, hi) in MASS.items():
        print(f"| {k} | {lo:.1f} | {hi:.1f} |")
    mlo, mhi = tot(MASS)
    print(f"| **Installed dry, naturally aspirated** | **{mlo:.0f}** | **{mhi:.0f}** |")
    print(f"| + normalizer (turbo + intercooler), if fitted | {mlo + NORMALIZER_KG[0]:.0f} | {mhi + NORMALIZER_KG[1]:.0f} |")
    print(f"| radiator, oil cooler and coolant system (separate line, R-38) | {RADIATOR_SYSTEM_KG[0]:.1f} | {RADIATOR_SYSTEM_KG[1]:.1f} |")
    print(f"| installed with the cooling system, NA | {mlo + RADIATOR_SYSTEM_KG[0]:.0f} | {mhi + RADIATOR_SYSTEM_KG[1]:.0f} |")
    print(f"\nPer takeoff horsepower at the flange (113-139 hp): {mlo/139:.2f}-{mhi/113:.2f} kg/hp, NA, installed dry.")

    print("\n## 2. First-engine cost, basis 1 (R-35 definition: parts and services, no labor, no propeller)\n")
    print("| Line | low | high |")
    print("|---|---|---|")
    for k, (lo, hi) in COST.items():
        print(f"| {k} | ${lo:,.0f} | ${hi:,.0f} |")
    clo, chi = tot(COST)
    print(f"| **Total, naturally aspirated** | **${clo:,.0f}** | **${chi:,.0f}** |")
    print(f"\nLow / mid / high: ${clo/1e3:.1f}k / ${mid(clo, chi)/1e3:.1f}k / ${chi/1e3:.1f}k.")
    nlo, nhi = clo + NORMALIZER_COST[0], chi + NORMALIZER_COST[1]
    print(f"With a normalizer: ${nlo/1e3:.1f}k / ${mid(nlo, nhi)/1e3:.1f}k / ${nhi/1e3:.1f}k.")
    # what is Hayabusa-specific and what is the program's own work
    shared = ("gearbox", "adapter", "elastic", "FADEC", "second coil", "second crank", "second generator", "cooling", "fuel system", "exhaust", "intake", "mount", "misc")
    slo = sum(v[0] for k, v in COST.items() if any(s in k for s in shared))
    shi = sum(v[1] for k, v in COST.items() if any(s in k for s in shared))
    print(f"Of which lines any engine in the program needs (gearbox, FADEC, cooling, fuel, exhaust, mount, misc): ${slo/1e3:.1f}k-{shi/1e3:.1f}k; "
          f"the Hayabusa-specific core, rebuild, pistons, dry sump and head work: ${(clo-slo)/1e3:.1f}k-{(chi-shi)/1e3:.1f}k.")
    no_dual = [k for k in COST if k.startswith(("second plug", "second coil", "second crank", "second generator"))]
    dlo = sum(COST[k][0] for k in no_dual)
    dhi = sum(COST[k][1] for k in no_dual)
    print(f"The dual-lane hardware beyond one FADEC line (second plug, coils, sensor, generator): ${dlo/1e3:.1f}k-{dhi/1e3:.1f}k.")

    print("\n## 3. Builder labor (not in R-35's cost)\n")
    print("| Task | hours |")
    print("|---|---|")
    for k, (lo, hi) in LABOR_H.items():
        print(f"| {k} | {lo}-{hi} |")
    llo, lhi = tot(LABOR_H)
    print(f"| **Total** | **{llo}-{lhi}** |")

    print("\n## 4. Durability bracket: Radical race hours scaled to aircraft MCP rpm\n")
    print("| Wear law, hours as rpm^-k | race mean rpm | aircraft MCP rpm | life multiplier | equivalent aircraft hours to a Radical-class rebuild |")
    print("|---|---|---|---|---|")
    vals = []
    for k in WEAR_EXP:
        for nr in RACE_MEAN_RPM:
            for na in AIR_MCP_RPM:
                m = (nr / na) ** k
                vals.append((RADICAL_H[0] * m, RADICAL_H[1] * m))
                print(f"| k = {k:.0f} | {nr:,.0f} | {na:,.0f} | {m:.2f} | {RADICAL_H[0]*m:.0f}-{RADICAL_H[1]*m:.0f} |")
    print(f"\nBand: {min(v[0] for v in vals):.0f}-{max(v[1] for v in vals):.0f} h. Against R-40's 2,000 h TBO target.")
