"""Physics floor for the phase-0 engine concepts (AER-3320).

First-principles sizing only -- no vendor part, no CAD. For each concept and
each family member (100/200/300 hp takeoff) this computes:

  displacement, cylinders, bore/stroke, BMEP, mean piston speed, rpm,
  fuel and air flow, the heat balance (shaft / coolant / oil / exhaust),
  the normalizing compressor duty at the critical altitude, and a mass
  estimate scaled from the best-matched analog engine class.

Methods
  BMEP:   P = BMEP * Vd * N / (60 * k)   k = 2 for 4-stroke, 1 for 2-stroke
          and 1 per rotor per eccentric-shaft rev for a Wankel (Heywood 2.2,
          Yamamoto for the rotary displacement convention).
  Sp:     Sp = 2 * S * N / 60
  Heat:   fuel power = P / eta_b, eta_b = 3600 / (BSFC * LHV); split by class
          fractions from Heywood ch. 12 (energy balance), closed by
          construction and checked for a plausible exhaust share.
  Comp:   W = m_air * cp * T1 * (PR^((g-1)/g) - 1) / eta_c   (isentropic
          compressor with an efficiency), ISA atmosphere.
  Mass:   m = m_ref * (hp / hp_ref) ^ x per analog class, times a sand-cast
          penalty. This is EXTRAPOLATION, +/-25 %, labeled as such.

Run:  python3 engine_floor.py            (prints markdown tables)
      python3 engine_floor.py --json out.json
"""
import json
import math
import sys

HP = 0.745699872  # kW per hp
FAMILY_HP = (100, 200, 300)

# ISA
def isa(h_ft):
    h = h_ft * 0.3048
    T = 288.15 - 0.0065 * h
    p = 101325.0 * (T / 288.15) ** 5.2559
    return T, p


# Bores are anchored to catalog piston families per the MANUFACTURING
# envelope v0 (AER-3321, finding 4): A = Lycoming 540 cylinder (130.2 x 111.1),
# B = 86 mm (Toyota/Subaru FA20 family), C = GM LS7 (104.8 x 101.6),
# D = 4.5 in big-block Chevy (114.3), E = Mercedes OM640 (83 x 92).
# F (opposed-piston, port-controlling skirt) and G (Mazda 13B rotor) have no
# general catalog piston; see ARCHITECTURES.md.
CONCEPTS = [
    # key, name, cycle, fuel, cylinders per member, bore mm, stroke mm (per piston),
    # takeoff rpm per member, normalizing, analog class
    dict(key="A", name="Flat, low-speed, big-bore, direct drive",
         cycle="4S-SI", fuel="auto gas", cyl=(2, 4, 6), bore=130.2, stroke=111.1,
         rpm=(2750, 2750, 2750), drive="direct",
         norm="turbo", analog="lycoming"),
    dict(key="B", name="Flat, high-speed, small-bore, geared (Rotax-scaled module)",
         cycle="4S-SI", fuel="auto gas", cyl=(4, 8, 12), bore=86.0, stroke=64.0,
         rpm=(5800, 5800, 5800), drive="reduction ~2.4:1",
         norm="turbo", analog="rotax"),
    dict(key="C", name="V-2/4/6, paired crankpins, mid-speed, geared",
         cycle="4S-SI", fuel="auto gas", cyl=(2, 4, 6), bore=104.8, stroke=101.6,
         rpm=(4700, 4700, 4700), drive="reduction ~2.0:1",
         norm="turbo", analog="vgeared"),
    dict(key="D", name="Radial, single-throw crank, liquid-cooled",
         cycle="4S-SI", fuel="auto gas", cyl=(3, 7, 9), bore=114.3, stroke=106.0,
         rpm=(2600, 2400, 2600), drive="direct",
         norm="geared centrifugal supercharger", analog="radial"),
    dict(key="E", name="4-stroke diesel, common rail, turbo, geared (I3/I6/V8)",
         cycle="4S-CI", fuel="Jet-A / diesel", cyl=(3, 6, 8), bore=83.0, stroke=92.0,
         rpm=(3900, 3900, 3900), drive="reduction ~1.6:1",
         norm="turbo (integral to the cycle)", analog="diesel4s"),
    dict(key="F", name="Opposed-piston 2-stroke diesel, no cylinder head",
         cycle="2S-CI-OP", fuel="Jet-A / diesel", cyl=(2, 4, 6), bore=82.0, stroke=78.0,
         rpm=(3000, 3000, 3000), drive="crank-gear train, ~1.25:1",
         norm="scavenge blower + turbo (integral)", analog="op2s"),
    dict(key="G", name="Wankel rotary, rotor-module family",
         cycle="Wankel", fuel="auto gas", cyl=(2, 4, 6), bore=None, stroke=None,
         chamber_L=0.654, rpm=(4600, 4600, 4600), drive="reduction ~2.0:1",
         norm="turbo", analog="wankel"),
]

# Diesel E is also shown "literally normalized": sea-level manifold ~1 bar.
DIESEL_NA = dict(key="E-NA", name="4-stroke diesel held to ~1 bar manifold (literal normalizing)",
                 cycle="4S-CI", fuel="Jet-A / diesel", cyl=(6, 12, 18), bore=83.0, stroke=92.0,
                 rpm=(4000, 4000, 4000), drive="reduction", norm="turbo, normalizing only",
                 analog="diesel4s", mass_vd_ref="E")

# Cycle data: BSFC at takeoff (g/kWh), LHV (MJ/kg), delivered AFR, heat
# fractions of fuel energy to coolant and to oil (Heywood ch. 12 ranges;
# class values chosen inside them and stated in the doc).
CYCLE = {
    "4S-SI":    dict(bsfc=310, lhv=42.0, afr=12.4, f_cool=0.24, f_oil=0.05,
                     note="E10 LHV; takeoff rich, lambda ~0.88"),
    "4S-CI":    dict(bsfc=225, lhv=42.8, afr=20.3, f_cool=0.20, f_oil=0.06,
                     note="lambda ~1.4 at full load"),
    "2S-CI-OP": dict(bsfc=215, lhv=42.8, afr=30.0, f_cool=0.16, f_oil=0.07,
                     note="trapped lambda ~1.6, scavenge ratio ~1.3"),
    "Wankel":   dict(bsfc=340, lhv=42.0, afr=12.4, f_cool=0.27, f_oil=0.08,
                     note="rotary BSFC penalty, high surface/volume"),
}

# Mass analogs: (reference dry kg, reference hp, scaling exponent, source tag)
# Reference masses are vendor dry figures (bare engine as the vendor defines
# it, no coolant/oil/radiator). Exponents are fitted across the class where
# two members exist, otherwise assumed and labeled.
ANALOG = {
    "lycoming": (89.3, 100, 0.79, "Continental O-200-D 89.3 kg / Lycoming IO-540-K 212.7 kg (vendor, read 2026-10-16); fitted exponent"),
    "rotax":    (56.6, 100, 0.85, "Rotax 912 ULS 56.6 kg incl. gearbox; exponent ASSUMED"),
    "vgeared":  (75.0, 100, 0.80, "between Rotax and Lycoming classes; ASSUMED"),
    "radial":   (85.0, 100, 0.75, "Verner/Rotec radial class ~0.75-0.8 kg/hp; ASSUMED exponent"),
    "diesel4s": (121.0, 133, 0.80, "Continental CD-135 134 kg incl. gearbox/turbo/FADEC, less the turbo+FADEC allowances added below; ASSUMED exponent"),
    "op2s":     (90.0, 100, 0.80, "no modern aviation OP analog; ASSUMED ~0.9 kg/hp at 100 hp"),
    "wankel":   (70.0, 100, 0.75, "Mazda 13B bare + PSRU class; ASSUMED"),
}
SAND_CAST_PENALTY = 1.10   # thicker sand-cast walls on ~40 % of mass; ASSUMED
TURBO_KG = {100: 6.0, 200: 9.0, 300: 12.0}      # turbo+wastegate+intercooler+ducting, ASSUMED
FADEC_KG = 4.0                                   # two lanes, harness, sensors; ASSUMED
COOLING_KW_PER_KG = (3.7, 8.0, 27.3)             # installed-system bounds (low, mid, high)

ALT_CRIT_FT = 12000
COMP_EFF = {"turbo": 0.70, "geared centrifugal supercharger": 0.65}
MAP_TARGET_BAR = 1.08   # 1.0 bar manifold + ~0.08 bar intercooler/throttle loss


def displacement(c, n):
    if c["cycle"] == "Wankel":
        return c["chamber_L"] * n
    if c["cycle"] == "2S-CI-OP":
        return math.pi / 4 * (c["bore"] / 1000) ** 2 * (2 * c["stroke"] / 1000) * n * 1000
    return math.pi / 4 * (c["bore"] / 1000) ** 2 * (c["stroke"] / 1000) * n * 1000


def bmep_bar(P_kW, Vd_L, N, cycle):
    k = 2 if cycle in ("4S-SI", "4S-CI") else 1
    return P_kW * 60 * k / (Vd_L * 1e-3 * N) / 1e5 * 1e3


def compressor(m_air, T1, PR, eta):
    g = 1.4
    cp = 1.005
    dT = T1 * (PR ** ((g - 1) / g) - 1) / eta
    return m_air * cp * dT, T1 + dT


def member(c, i, hp, alt_ft=ALT_CRIT_FT):
    n = c["cyl"][i]
    N = c["rpm"][i]
    P = hp * HP
    Vd = displacement(c, n)
    bmep = bmep_bar(P, Vd, N, c["cycle"])
    Sp = None if c["stroke"] is None else 2 * c["stroke"] / 1000 * N / 60
    cy = CYCLE[c["cycle"]]
    mf = cy["bsfc"] * P / 1000 / 3600            # kg/s fuel
    eta = 3600 / (cy["bsfc"] * cy["lhv"])
    Qf = P / eta
    Qc = cy["f_cool"] * Qf
    Qo = cy["f_oil"] * Qf
    Qx = Qf - P - Qc - Qo
    m_air = mf * cy["afr"]
    T1, p1 = isa(alt_ft)
    if c["cycle"] in ("4S-SI", "Wankel"):
        PR = MAP_TARGET_BAR * 1e5 / p1
    elif c["key"] == "E-NA":
        PR = MAP_TARGET_BAR * 1e5 / p1
    elif c["cycle"] == "4S-CI":
        PR = 2.2e5 / p1          # sea-level boost held to altitude
    else:
        PR = 2.0e5 / p1          # OP2S scavenge + boost manifold held to altitude
    eta_c = COMP_EFF.get(c["norm"], 0.70)
    Wc, T2 = compressor(m_air, T1, PR, eta_c)
    ref_kg, ref_hp, x, _ = ANALOG[c["analog"]]
    bare = ref_kg * (hp / ref_hp) ** x * SAND_CAST_PENALTY
    if c.get("mass_vd_ref"):
        # same cylinder module, more of it: scale the turbo-diesel's mass by
        # displacement ratio ^0.8 (fixed accessories do not double). ASSUMED.
        ref = next(r for r in CONCEPTS if r["key"] == c["mass_vd_ref"])
        bare *= (Vd / displacement(ref, ref["cyl"][i])) ** 0.8
    with_norm = bare + TURBO_KG[hp] + FADEC_KG
    cool_mid = (Qc + Qo) / COOLING_KW_PER_KG[1]
    cool_lo = (Qc + Qo) / COOLING_KW_PER_KG[2]
    cool_hi = (Qc + Qo) / COOLING_KW_PER_KG[0]
    # airflow-fits-displacement check: implied volumetric (or delivery) ratio
    # at sea level. Manifold density: 1 bar/288 K unboosted; turbo diesel
    # 2.2 bar and OP2S 2.0 bar, intercooled to 50 C.
    if c["cycle"] == "4S-CI" and c["key"] != "E-NA":
        rho = 2.2e5 / (287 * 323)
    elif c["cycle"] == "2S-CI-OP":
        rho = 2.0e5 / (287 * 323)
    else:
        rho = 1.0e5 / (287 * 288)
    intakes_per_s = N / 60 / (2 if c["cycle"] in ("4S-SI", "4S-CI") else 1)
    eta_v = m_air / (rho * Vd * 1e-3 * intakes_per_s)
    return dict(hp=hp, kW=P, eta_v=eta_v, n=n, N=N, Vd_L=Vd, bmep=bmep, Sp=Sp, eta_b=eta,
                fuel_kg_h=mf * 3600, fuel_gph=mf * 3600 / (0.745 if c["cycle"] in ("4S-SI", "Wankel") else 0.81) / 3.785,
                Qfuel=Qf, Qcool=Qc, Qoil=Qo, Qexh=Qx, exh_frac=Qx / Qf,
                m_air=m_air, PR=PR, Wc=Wc, Wc_frac=Wc / P, T2C=T2 - 273.15,
                bare_kg=bare, dry_kg=with_norm, cool_kg=(cool_lo, cool_mid, cool_hi),
                installed_kg=with_norm + cool_mid)


def run():
    out = {}
    for c in CONCEPTS + [DIESEL_NA]:
        out[c["key"]] = dict(concept={k: v for k, v in c.items()},
                             members=[member(c, i, hp) for i, hp in enumerate(FAMILY_HP)])
    # critical-altitude sensitivity for the SI concepts (compressor duty)
    sens = {}
    for alt in (8000, 12000, 16000):
        m = member(CONCEPTS[0], 1, 200, alt)
        sens[alt] = dict(PR=m["PR"], Wc=m["Wc"], Wc_frac=m["Wc_frac"], T2C=m["T2C"])
    return out, sens


def md(out, sens):
    L = []
    L.append("| Concept | hp | cyl | Vd (L) | bore x stroke (mm) | rpm | BMEP (bar) | Sp (m/s) | fuel (kg/h) | coolant / oil / exhaust (kW) | exh. share | PR @12k ft | comp. work (% P) | T2 (C) | eta_v SL | bare / dry+norm+FADEC / installed (kg) |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for k, d in out.items():
        c = d["concept"]
        bs = "rotor 0.654 L" if c["bore"] is None else (
            f"{c['bore']:.0f} x 2x{c['stroke']:.0f}" if c["cycle"] == "2S-CI-OP" else f"{c['bore']:.0f} x {c['stroke']:.0f}")
        for m in d["members"]:
            sp = "-" if m["Sp"] is None else f"{m['Sp']:.1f}"
            L.append(f"| {k} | {m['hp']} | {m['n']} | {m['Vd_L']:.2f} | {bs} | {m['N']} | {m['bmep']:.1f} | {sp} | {m['fuel_kg_h']:.1f} | "
                     f"{m['Qcool']:.0f} / {m['Qoil']:.0f} / {m['Qexh']:.0f} | {m['exh_frac']:.2f} | {m['PR']:.2f} | {100*m['Wc_frac']:.1f} | {m['T2C']:.0f} | {m['eta_v']:.2f} | "
                     f"{m['bare_kg']:.0f} / {m['dry_kg']:.0f} / {m['installed_kg']:.0f} |")
    L.append("")
    L.append("Critical-altitude sensitivity, concept A 200 hp (ISA):")
    L.append("")
    L.append("| critical altitude (ft) | pressure ratio | compressor work (kW) | % of rated | outlet T (C) |")
    L.append("|---|---|---|---|---|")
    for alt, s in sens.items():
        L.append(f"| {alt} | {s['PR']:.2f} | {s['Wc']:.1f} | {100*s['Wc_frac']:.1f} | {s['T2C']:.0f} |")
    return "\n".join(L)


if __name__ == "__main__":
    out, sens = run()
    print(md(out, sens))
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w") as f:
            json.dump(dict(out=out, sens=sens), f, indent=1, default=str)
