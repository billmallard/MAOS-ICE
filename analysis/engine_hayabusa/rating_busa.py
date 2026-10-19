"""Aircraft-duty rating of a Suzuki Hayabusa core, and where it lands (AER-3525, question 1, 5, 6).

A motorcycle is rated at its peak; an aircraft engine is rated at what it can
hold. This script sets a takeoff (5 min) and a maximum continuous (MCP) point
for the Hayabusa from three limits, each named:

  piston speed   mean piston speed Sp = 2 S n. Bands from engines that hold
                 their rating for a TBO: Rotax 912 ULS at MCP 11.2 m/s
                 (5,500 rpm, 61 mm), the Viking/Aeromomentum Suzuki-Honda
                 conversions at about 16 m/s (CRANK_AND_SCALING sweep cap).
  BMEP           no higher than the motorcycle's own full-throttle BMEP at that
                 rpm (from Suzuki's torque claim and published dyno curves),
                 and at MCP held to the Rotax 912 class (about 10.5-12 bar).
                 The Rotax 915 (turbo, 1,200 h TBO) is the boosted yardstick.
  knock          knock.py's calibrated Livengood-Wu index on MON 85 (91 AKI,
                 R-12), with the liquid-cooled-head credit; the compression
                 ratio the engine may keep at sustained full throttle.

Then: flange power through a gearbox (eta 0.97-0.98, ASSUMED, Rotax-class
single-stage gears), BSFC-based fuel flow, the implied volumetric efficiency
(a check the inputs cannot fake, engine-sizing lesson), heat to coolant and
oil (radiator.py's Heywood fractions), and the radiator system mass from
radiator.py rerun at the Hayabusa's MCP heat.

Tags: [S] sourced in sources/HAYABUSA_SOURCES_2026-10-19.md, [E] estimate with
the method here, [A] assumed.

Run: python3 rating_busa.py
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P1 = os.path.join(HERE, "..", "engine_phase1")


def _load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(P1, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


KN = _load("knock")
RAD = _load("radiator")
HP = 0.745699872
LHV = 42.0e3          # kJ/kg, gasoline, as radiator.py
RHO_FUEL = 0.74       # kg/L, E0-E10 gasoline [A]

# ------------------------------------------------------------- engine data
GENS = {
    # Suzuki Japan claims [H1]; bore, stroke, CR [H1][H5][H11]; sources/HAYABUSA_SOURCES_2026-10-19.md
    "Gen 3 (2021-)": dict(B=81.0, S=65.0, Vd=1.340, CR=12.5, P_peak=(188 * 0.7355, 9700), T_peak=(149.0, 7000)),
    "Gen 2 (2008-2020)": dict(B=81.0, S=65.0, Vd=1.340, CR=12.5, P_peak=(197 * 0.7355, 9500), T_peak=(155.0, 7200)),
    "Gen 1 (1999-2007)": dict(B=81.0, S=63.0, Vd=1.298, CR=11.0, P_peak=(175 * 0.7355, 9800), T_peak=(138.2, 7000)),
}
# Full-throttle crank torque (N m) against rpm, Gen 3 stock: the BT Moto Dynojet rear-wheel curve [H18]
# (91 / 96.5 / 103 / 100.5 lb-ft at 5,000 / 6,000 / 7,000 / 8,000 rpm) divided by 0.94, the ratio of
# Suzuki's 149 N m crank claim to the 140 N m read at the wheel at 7,000 rpm [E]. 5,500, 6,500, 7,500 interpolated.
WOT_TORQUE_GEN3 = {5000: 131.0, 5500: 135.0, 6000: 139.0, 6500: 144.0, 7000: 149.0, 7500: 148.0, 8000: 145.0}

# The aircraft rating, as bands [low, high]
TO_RPM = (6500, 7000)        # takeoff, 5 min
MCP_RPM = (5800, 6500)       # hold for hours
MCP_BMEP = (10.5e5, 11.5e5)  # Pa, Rotax 912 class at MCP (912 ULS: 11.1 bar)
TO_BMEP_CAP = 12.0e5         # Pa, the low takeoff band: eta_v <= 1.0 at BSFC 280, AFR 12.8 (no tuned-intake credit)
CR_AIR = 11.0                # lower-compression pistons for sustained full throttle on MON 85 (knock section)
ETA_GEAR = (0.97, 0.98)
BSFC_TO = (270.0, 300.0)     # g/kWh, rich takeoff [A]; the motorcycle's 14.1 bar torque peak implies ~265-275
BSFC_MCP = (265.0, 285.0)    # g/kWh [E]; Rotax 912 ULS 25 L/h at 69 kW MCP = ~268 g/kWh (COMPARABLE_ENGINES [R3])
AFR_TO, AFR_MCP = 12.8, 13.2

COMPARE = [
    # name, takeoff kW @ rpm, MCP kW @ rpm, Vd L, stroke mm, source
    ("Rotax 912 ULS", (73.5, 5800), (69.0, 5500), 1.352, 61.0, "COMPARABLE_ENGINES [R1][R3]"),
    ("Rotax 915 iS (turbo)", (104.0, 5800), (99.0, 5500), 1.352, 61.0, "COMPARABLE_ENGINES [R5]"),
    ("Rotax 916 iS (turbo)", (117.0, 5800), (101.0, 5500), 1.352, 61.0, "COMPARABLE_ENGINES [R6]"),
    ("Concept H (200 hp member)", (200 * HP, 3300), (180 * HP, 3300), 5.26, 101.6, "RANKING_PHASE1 / CRANK_AND_SCALING"),
]


def bmep(P_kW, rpm, Vd_L):
    return P_kW * 1e3 / (Vd_L * 1e-3 * rpm / 120)


def power(bmep_pa, rpm, Vd_L):
    return bmep_pa * Vd_L * 1e-3 * rpm / 120 / 1e3


def sp(S_mm, rpm):
    return 2 * S_mm / 1000 * rpm / 60


def eta_v(P_kW, bsfc, afr, rpm, Vd_L, rho=1.184):
    mf = P_kW * bsfc / 3600 / 1000          # kg/s fuel
    return mf * afr / (rho * Vd_L * 1e-3 * rpm / 120)


def otto(cr, g=1.30):
    return 1 - cr ** (1 - g)


def wot_torque(rpm):
    pts = sorted(WOT_TORQUE_GEN3.items())
    for (r0, t0), (r1, t1) in zip(pts, pts[1:]):
        if r0 <= rpm <= r1:
            return t0 + (t1 - t0) * (rpm - r0) / (r1 - r0)
    raise ValueError(rpm)


def rating():
    g = GENS["Gen 3 (2021-)"]
    cr_pen = otto(CR_AIR) / otto(g["CR"])             # power ratio for the lower-CR piston
    out = {}
    # takeoff: the motorcycle's own WOT torque at the rpm, less the CR penalty
    to = []
    for rpm in TO_RPM:          # low band: BMEP capped where eta_v reaches 1.0
        to.append((rpm, power(TO_BMEP_CAP, rpm, g["Vd"]), TO_BMEP_CAP))
    for rpm in TO_RPM:          # high band: the motorcycle's WOT curve less the CR penalty
        T = wot_torque(rpm) * cr_pen
        P = T * rpm * 2 * math.pi / 60 / 1e3
        to.append((rpm, P, bmep(P, rpm, g["Vd"])))
    out["TO"] = to
    mcp = []
    for rpm, b in zip(MCP_RPM, MCP_BMEP):
        mcp.append((rpm, power(b, rpm, g["Vd"]), b))
    out["MCP"] = mcp
    out["cr_pen"] = cr_pen
    return g, out


def radiator_at(P_mcp_kW):
    """radiator.py at a different MCP: its globals scaled, its model unchanged."""
    saved = (RAD.P_MCP, RAD.Q_FUEL, RAD.Q_COOL, RAD.Q_OIL)
    RAD.P_MCP = P_mcp_kW
    RAD.Q_FUEL = P_mcp_kW / (3600 / (RAD.BSFC_MCP * RAD.LHV))
    RAD.Q_COOL = 0.24 * RAD.Q_FUEL
    RAD.Q_OIL = 0.05 * RAD.Q_FUEL
    res = [RAD.run(80, Td, Vf, 0) for Td in (0.032, 0.050, 0.064) for Vf in (6.0, 8.0, 10.0, 12.0)]
    res = [r for r in res if r]
    best = min(res, key=lambda r: r["sys_kg"] + 2.0 * r["rad"]["Pdrag"])
    q = (RAD.Q_COOL, RAD.Q_OIL)
    RAD.P_MCP, RAD.Q_FUEL, RAD.Q_COOL, RAD.Q_OIL = saved
    return q, min(r["sys_kg"] for r in res), max(r["sys_kg"] for r in res), best


if __name__ == "__main__":
    g, R = rating()
    print("## 1. The motorcycle ratings, as published\n")
    print("| Generation | bore x stroke (mm) | Vd (L) | CR | peak power | BMEP at peak power | Sp at peak power | peak torque | BMEP at peak torque |")
    print("|---|---|---|---|---|---|---|---|---|")
    for n, e in GENS.items():
        P, nP = e["P_peak"]
        T, nT = e["T_peak"]
        print(f"| {n} | {e['B']} x {e['S']} | {e['Vd']:.3f} | {e['CR']} | {P:.0f} kW ({P/HP:.0f} hp) at {nP:,} | "
              f"{bmep(P, nP, e['Vd'])/1e5:.1f} bar | {sp(e['S'], nP):.1f} m/s | {T:.0f} N m at {nT:,} | {4*math.pi*T/(e['Vd']*1e-3)/1e5:.1f} bar |")

    print("\n## 2. Knock-limited compression ratio at sustained full throttle, MON 85 (knock.py)\n")
    ks, kstar, _ = KN.run()
    kliq = ks[0]
    print("| rpm | Sp (m/s) | CR limit, air-cooled threshold | CR limit, liquid-cooled-head credit (Rotax 912 anchor) | stock CR | margin at stock CR (liquid credit) |")
    print("|---|---|---|---|---|---|")
    for rpm in (5500, 6000, 6500, 7000, 7500, 9700):
        a = KN.cr_limit(g["B"], g["S"], rpm, 85, kstar)
        l = KN.cr_limit(g["B"], g["S"], rpm, 85, kliq)
        print(f"| {rpm:,} | {sp(g['S'], rpm):.1f} | {a:.1f} | {l:.1f} | {g['CR']} | {l - g['CR']:+.1f} |")
    print(f"\nLower-compression pistons at CR {CR_AIR}: ideal Otto power ratio {R['cr_pen']:.3f} against CR {g['CR']}.")

    print("\n## 3. The aircraft rating (Gen 2 or Gen 3: same 81 x 65 mm and CR; Gen 3 curve; CR 11 pistons), crank and propeller flange\n")
    print("| Point | rpm | Sp (m/s) | BMEP (bar) | crank (kW / hp) | flange, gearbox 0.97-0.98 (hp) | fuel (L/h) | implied eta_v | coolant / oil heat (kW) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for lab, pts, bs, afr in (("Takeoff, 5 min, eta_v-capped", R["TO"][:2], (280.0, 280.0), AFR_TO),
                              ("Takeoff, 5 min, motorcycle WOT curve", R["TO"][2:], (BSFC_TO[0], BSFC_TO[0]), AFR_TO),
                              ("MCP", R["MCP"], BSFC_MCP, AFR_MCP)):
        for (rpm, P, b), bsfc in zip(pts, bs):
            ev = eta_v(P, bsfc, afr, rpm, g["Vd"])
            fuel = P * bsfc / 1000 / RHO_FUEL
            qf = P / (3600 / (bsfc * LHV / 1000))
            print(f"| {lab} | {rpm:,} | {sp(g['S'], rpm):.1f} | {b/1e5:.1f} | {P:.0f} / {P/HP:.0f} | "
                  f"{P*ETA_GEAR[0]/HP:.0f}-{P*ETA_GEAR[1]/HP:.0f} | {fuel:.0f} | {ev:.2f} | {0.24*qf:.0f} / {0.05*qf:.0f} |")

    print("\n## 4. Against the yardsticks\n")
    print("| Engine | takeoff | BMEP at takeoff | Sp at takeoff | MCP | BMEP at MCP | Sp at MCP | MCP / takeoff | source |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, (Pt, nt), (Pm, nm), Vd, S, src in COMPARE:
        print(f"| {name} | {Pt/HP:.0f} hp at {nt:,} | {bmep(Pt, nt, Vd)/1e5:.1f} bar | {sp(S, nt):.1f} m/s | {Pm/HP:.0f} hp at {nm:,} | "
              f"{bmep(Pm, nm, Vd)/1e5:.1f} bar | {sp(S, nm):.1f} m/s | {Pm/Pt:.0%} | {src} |")
    to_lo, to_hi = R["TO"][0], R["TO"][3]
    m_lo, m_hi = R["MCP"][0], R["MCP"][1]
    print(f"| **Hayabusa, aircraft rating (this script)** | {to_lo[1]/HP:.0f}-{to_hi[1]/HP:.0f} hp crank at {to_lo[0]:,}-{to_hi[0]:,} | "
          f"{to_lo[2]/1e5:.1f}-{to_hi[2]/1e5:.1f} bar | {sp(g['S'], to_lo[0]):.1f}-{sp(g['S'], to_hi[0]):.1f} m/s | "
          f"{m_lo[1]/HP:.0f}-{m_hi[1]/HP:.0f} hp crank at {m_lo[0]:,}-{m_hi[0]:,} | {m_lo[2]/1e5:.1f}-{m_hi[2]/1e5:.1f} bar | "
          f"{sp(g['S'], m_lo[0]):.1f}-{sp(g['S'], m_hi[0]):.1f} m/s | | |")

    print("\n## 5. Boost: what 150-200 hp at the flange asks of a 1.34 L core\n")
    print("| Target at the flange | rpm | crank kW needed (gearbox 0.975) | BMEP | against Rotax 915 takeoff BMEP | against Rotax 916 takeoff BMEP | Sp | manifold pressure for that BMEP (bar abs, scaled from the NA point) |")
    print("|---|---|---|---|---|---|---|---|")
    b915 = bmep(104.0, 5800, 1.352)
    b916 = bmep(117.0, 5800, 1.352)
    b_na = R["TO"][1][2]       # the eta_v-capped NA point, 12 bar
    for hp in (130, 150, 175, 200):
        for rpm in (6500, 7000, 7500):
            Pc = hp * HP / 0.975
            b = bmep(Pc, rpm, g["Vd"])
            print(f"| {hp} hp | {rpm:,} | {Pc:.0f} | {b/1e5:.1f} bar | {b/b915:.2f}x | {b/b916:.2f}x | {sp(g['S'], rpm):.1f} m/s | {b/b_na:.2f} |")

    print("\n## 6. Radiator and oil cooler at the Hayabusa's MCP (radiator.py, R-22 case: MCP, 80 KIAS, sea level ISA+20)\n")
    print("| MCP crank (kW) | coolant / oil heat (kW) | installed system (kg), grid range | design point: radiator face (cm^2), system (kg), drag (% MCP) |")
    print("|---|---|---|---|")
    for P in (m_lo[1], m_hi[1], 200 * 0.9 * HP):
        (qc, qo), lo, hi, best = radiator_at(P)
        tag = " (concept H, for reference)" if P > 120 else ""
        print(f"| {P:.0f}{tag} | {qc:.0f} / {qo:.0f} | {lo:.1f}-{hi:.1f} | {best['rad']['Af']*1e4:,.0f}, {best['sys_kg']:.1f}, "
              f"{100*best['drag_frac']:.1f} % |")
