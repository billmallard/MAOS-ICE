"""FADEC flight mule on a bought conversion (AER-3631): rating check, lane residuals, injectors, costs.

Four questions, one section each.

1. Rating check. Each vendor's takeoff claim as BMEP, against the donor car
   engine's own published peak torque, with the implied volumetric efficiency
   (Heywood eq. 2.41: bmep = eta_f * eta_v * rho_a * (F/A) * Q_LHV). This is
   the check the inputs cannot fake: a naturally aspirated port-injected engine
   with no tuned-length credit sits near eta_v 0.85-0.95 at its rated speed.
2. What a single failure leaves on a 4-cylinder with one plug per cylinder.
   Live cylinders cannot add IMEP at full throttle, so the residual at the
   takeoff rpm is ((z - k)/z * IMEP - FMEP) / (IMEP - FMEP), the same form as
   torsional_busa.py section 4, with FMEP as a band [A] (Heywood ch. 13 class).
3. Injector size if each cylinder gets a second injector on lane B, so that
   either injector alone carries takeoff fuel on E15.
4. Cost of the FADEC substitution and of each airframe route, low / high, on
   sourced vendor list prices where they exist and PROPULSION estimates [E]
   where they do not. None of these is a quote (AER-3330).

Tags: [S] vendor or official source, [F] forum, listing or secondary, [E]
PROPULSION estimate, [A] assumed. Source keys are in
docs/engine/sources/FADEC_MULE_SOURCES_2026-10-21.md.

Run: python3 mule.py
"""
import math

HP = 0.745699872
RHO_A = 1.184            # kg/m^3, ISA sea level + 10 C intake [A]
Q_LHV_E10 = 42.0e6       # J/kg, E10 [A]
AFR_STOICH = {"E0": 14.7, "E10": 14.1, "E15": 13.8}   # [A] linear blend of 14.7 and 9.0
LAMBDA_TO = 0.88         # takeoff enrichment [A]
ETA_F_BAND = (0.30, 0.33)  # brake fuel-conversion efficiency at full throttle, rich [A]; 0.33 credits DI and CR 11.5
RHO_FUEL = 0.745         # kg/L [A]

# name, z, displacement (L), vendor claim (hp, rpm), donor published (kW, rpm, peak N m, rpm), injection
ENGINES = [
    ("Aeromomentum AM15", 4, 1.497, (120, 5800), (71, 6000, 128, 3200), "port"),   # vendor [S AM3]; G15A [F OT14]
    ("Aeromomentum AM13", 4, 1.298, (105, 5800), None, "port"),                     # [S AM2]; G13BB rating not sourced
    ("Viking 130", 4, 1.498, (130, 5400), (97, 6500, 154.6, 4600), "direct"),       # [S VK1]; Honda L15B 130 hp, 114 lb ft [S OT15]
]


def bmep(kw, rpm, vd_l):
    return kw * 1e3 * 2 / (vd_l * 1e-3 * rpm / 60) / 1e5   # bar


def eta_v(bmep_bar, eta_f, fuel="E10"):
    fa = 1 / (AFR_STOICH[fuel] * LAMBDA_TO)
    return bmep_bar * 1e5 / (eta_f * RHO_A * fa * Q_LHV_E10)


def section1():
    print("## 1. Rating check: the vendor claim against the donor engine's own torque\n")
    print("| Engine | Claim | BMEP at the claim | Implied eta_v (eta_f 0.33 / 0.30) | Donor's peak torque as BMEP | Claim / donor peak torque | Power at the claimed rpm if torque is held at the donor's peak |")
    print("|---|---|---|---|---|---|---|")
    for name, z, vd, (hp, rpm), donor, inj in ENGINES:
        kw = hp * HP
        b = bmep(kw, rpm, vd)
        ev = f"{eta_v(b, ETA_F_BAND[1]):.2f} / {eta_v(b, ETA_F_BAND[0]):.2f}"
        if donor:
            _, _, tq, _ = donor
            b_d = 4 * math.pi * tq / (vd * 1e-3) / 1e5
            tq_claim = kw * 1e3 / (rpm * 2 * math.pi / 60)
            p_cap = tq * rpm * 2 * math.pi / 60 / 1e3
            print(f"| {name} | {hp} hp at {rpm:,} | {b:.1f} bar | {ev} | {b_d:.1f} bar ({tq} N m) | {tq_claim / tq:.2f} | {p_cap:.0f} kW, {p_cap / HP:.0f} hp (an upper bound: torque falls past its peak) |")
        else:
            print(f"| {name} | {hp} hp at {rpm:,} | {b:.1f} bar | {ev} | not sourced | - | - |")
    print("\nReading: a naturally aspirated port-injected engine at its rated speed sits near eta_v 0.85-0.95 without tuned lengths")
    print("the vendors do not describe. The AM15 claim needs the top of that range, at a torque 15 % above the donor's own peak.")
    print("The Viking 130 claim needs eta_v above 1, 11 % above the Honda's peak torque, 1,100 rpm below the Honda's peak-power")
    print("speed. Neither is shown to be wrong; both are unmeasured. The stand measures them (G1).\n")


def section2():
    print("## 2. What one failure leaves on a 4-cylinder with one plug per cylinder\n")
    print("Full throttle at the takeoff rpm; IMEP = BMEP + FMEP; FMEP band 1.5-2.2 bar [A]. BMEP is taken at the donor-consistent")
    print("figure (section 1, about 10.7 bar) and at the vendor claim (12.4 bar), so the band covers both.\n")
    print("| Failure | Cylinders lost (k of 4) | Brake power left, share of takeoff |")
    print("|---|---|---|")
    z = 4
    cases = [
        ("one lane: ECU, its power feed, its crank sensor, its MAP or TPS, with automatic takeover by the other lane", 0),
        ("one coil-on-plug coil, one plug, one plug lead, or a single injector (no second injector)", 1),
        ("one wasted-spark coil pack (fires two cylinders): the vendor's ignition as described, if confirmed", 2),
        ("one injector, with a second injector per cylinder on the other lane", 0),
    ]
    for label, k in cases:
        vals = []
        for b in (10.7, 12.4):
            for f in (1.5, 2.2):
                imep = b + f
                vals.append(max(0.0, ((z - k) / z * imep - f) / (imep - f)))
        lo, hi = min(vals), max(vals)
        s = "100 %" if k == 0 else f"{lo:.0%}-{hi:.0%}"
        print(f"| {label} | {k} | {s} |")
    print("\nR-25 asks for at least 90 %. A dead cylinder on a geared 4-cylinder also adds half and first orders to the drive")
    print("(FL-52's method found a mesh torque reversal near 3,400 crank rpm on the Hayabusa); the Guibo coupling's stiffness is")
    print("not published, so that case is open on the AM15 until the stand survey (G3).\n")


def section3():
    print("## 3. A second injector per cylinder: size so that either one alone carries takeoff on E15\n")
    print("| Engine | Takeoff power used | BSFC at takeoff [A] | Fuel, E15 | Per injector, one per cylinder | Static flow needed at 85 % duty |")
    print("|---|---|---|---|---|---|")
    for name, z, vd, (hp, rpm), donor, inj in ENGINES:
        if inj != "port":
            continue
        kw = hp * HP                                  # vendor claim: the conservative case for sizing
        for bsfc in (0.32, 0.36):
            mf = kw * bsfc * AFR_STOICH["E0"] / AFR_STOICH["E15"]   # kg/h, E15 needs more mass of fuel
            per = mf / z / RHO_FUEL * 1000 / 60      # cc/min
            print(f"| {name} | {hp} hp | {bsfc} kg/kWh | {mf:.1f} kg/h | {per:.0f} cc/min | {per / 0.85:.0f} cc/min |")
    print("\nA catalog EV14 high-impedance injector of about 250-300 cc/min at 3 bar covers it. The vendor's injector flow is not")
    print("published; at 43 psi (2.96 bar) the catalog rating applies almost unchanged.\n")


LINES = [
    # item, low, high, tag
    ("Two lane ECUs: uaEFI ($275 each) with case ($50), or Proteus ($800 each, no case)", 650, 1600, "S OT16, OT17"),
    ("Lane isolation and arbitration board: per-output high-side switch per lane on each injector, logic OR on each coil, hardware watchdog; two prototype spins", 300, 1000, "E"),
    ("Coil-on-plug conversion: 4 coils (D585 class, $48-51) with brackets and short leads", 250, 500, "S ARCHITECTURES; E"),
    ("Program trigger wheel on the front pulley (36-1, cut) and two Hall sensors with a cut bracket", 100, 300, "E"),
    ("Second MAP, second TPS track, second coolant and air temperature sensors", 150, 400, "E"),
    ("Two wideband sensors (LSU 4.9 class; the uaEFI carries the controller)", 200, 300, "E"),
    ("Second power feed: lane B on its own battery and fuse, sized for 30 min of lane B, coils, injectors and one pump", 300, 800, "E"),
    ("Two lane harnesses, no shared connector, keyed, per-output fusing", 400, 1200, "E"),
    ("Hardware-in-the-loop bench: crank and cam stimulator, injector and coil load boxes", 300, 1000, "E"),
]
OPTION_INJ = ("Second injector per cylinder: 4 EV14 ($72-89), a second rail, a new or bossed intake manifold (printed-mold cast or machined)", 900, 3200, "S ARCHITECTURES; E")
STAND = ("Propeller test stand: frame, mount, load cell for thrust and torque reaction, EGT x4, fuel flow, logging", 1500, 5000, "E")


def section4():
    print("## 4. Cost of the FADEC substitution on an AM15 (parts and services, 2026 USD, no labor) [E unless tagged]\n")
    print("| Line | Low | High | Tag |")
    print("|---|---|---|---|")
    lo = hi = 0
    for item, a, b, t in LINES:
        print(f"| {item} | ${a:,} | ${b:,} | {t} |")
        lo += a
        hi += b
    print(f"| **Substitution, single injector per cylinder** | **${lo:,}** | **${hi:,}** | |")
    a, b = OPTION_INJ[1], OPTION_INJ[2]
    print(f"| {OPTION_INJ[0]} | ${a:,} | ${b:,} | {OPTION_INJ[3]} |")
    print(f"| **Substitution, with the second injector** | **${lo + a:,}** | **${hi + b:,}** | |")
    print(f"| {STAND[0]} | ${STAND[1]:,} | ${STAND[2]:,} | {STAND[3]} |")
    eng = (13000, 14100)
    t_lo, t_hi = eng[0] + lo + a + STAND[1], eng[1] + hi + b + STAND[2]
    print(f"| AM15 engine with gearbox, starter, alternator and its ECU (kept as the baseline and the spare) | ${eng[0]:,} | ${eng[1]:,} | S AM3 |")
    print(f"| **Engine, FADEC and stand: everything before an airframe** | **${t_lo:,}** | **${t_hi:,}** | |")
    print()
    return t_lo, t_hi


def section5(pre):
    print("## 5. Airframe routes, added to section 4's total\n")
    fwf = 2530 + 2130 + 1237            # Aeromomentum Zenith 650/750 cowling, propeller, mount [S AF4]
    rest = (1500, 4000)                 # exhaust, radiator, fuel, instruments for the swap [E]
    routes = [
        ("B. Used Rotax 912 E-AB (Zenith CH 750 / Kitfox / Rans class), re-engined with the AM15",
         (40000 + fwf + rest[0], 99000 + fwf + rest[1]), "S AF4, F AF20; the Rotax resale (one 912iS at $23.5k, F AF21) is not subtracted"),
        ("C. Zenith CH 750 STOL kit, built, with the AM15",
         (38725 + fwf + rest[0] + 10000, 38725 + fwf + rest[1] + 25000), "S AF9, AF4; avionics, instruments and finish $10-25k [E]"),
        ("A. Flying Viking 130 CH 750, re-engined with the AM15",
         (69000 + fwf + rest[0], 135000 + fwf + rest[1]), "F AF14, AF15; the removed Viking's resale not found"),
        ("D. Host aircraft: an owner flying an AM15 aircraft lends it",
         (2000, 10000), "E: swap parts back to stock, insurance increment, the owner's costs; no AM15 aircraft for sale was found and no host is known"),
        ("E. No airframe yet: ground stand only", (0, 0), "flight deferred"),
    ]
    print("| Route | Airframe and installation, low | high | With section 4, low | high | Basis |")
    print("|---|---|---|---|---|---|")
    for name, (a, b), basis in routes:
        print(f"| {name} | ${a:,} | ${b:,} | ${a + pre[0]:,} | ${b + pre[1]:,} | {basis} |")
    print()


if __name__ == "__main__":
    print("# FADEC flight mule: tables (generated by mule.py)\n")
    section1()
    section2()
    section3()
    pre = section4()
    section5(pre)
