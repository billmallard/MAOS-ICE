"""Crank routes for the one-off 200 hp engine, costed on the first-engine basis (AER-3411).

Bill's direction (2026-10-17, exploration, not a ruling): optimize for the
one-off build, so every route is priced with all of its NRE on one crank.

What this script does, each part labeled:
  1. A cost model for a machined crank, split into material, machine hours,
     one-off NRE, heat treatment, grinding and balance, and calibrated on the
     three sourced anchors in envelope v1 section 9.4. It answers Bill's third
     question: is the crank price metal, or one-off engineering and setup?
  2. The five routes in the issue, plus the decoupled-propeller-shaft that
     route 2 needs, each with a first-engine cost band.
  3. The physics checks that decide whether a route lives:
       - press-fit joint slip (route 1), Lame thick-cylinder fit pressure;
       - roller big-end L10 life (route 1 with one-piece rods), ISO 281 form;
       - cast-iron crankpin fatigue (route 3), nominal fillet stress with a
         notch factor and a Goodman line, against 4340 on the same geometry;
       - 180-degree V6 on 3 shared pins (route 4): firing intervals and the
         free primary couple, and the torsional modes of the 3-throw crank.
  4. A survey of mass-production cranks that could be reused once the
     propeller loads are taken off the crank (route 2).

Every figure is tagged:
  [S]  sourced (URL and read date in docs/engine/sources/CRANK_SOURCES_2026-10-18.md
       or in MANUFACTURING_ENVELOPE.md, as named)
  [E]  PROPULSION estimate, method in the comment
  [A]  ASSUMED, no source; the band is the uncertainty
None of these is a quote. Nothing here has been made or tested.

Run: python3 crank_routes.py
"""
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


TV = load(os.path.join(HERE, "..", "engine_phase1", "torsional_h.py"), "torsional_h")

RHO_STEEL = 7850.0
P_KW = 200 * 0.745699872

# ------------------------------------------------------------------ geometry
# Ratios taken from concept H (LS7 module: 104.8 bore, 101.6 stroke, LS pitch
# 111.76 mm, 2.100 in rod journal, 60 mm mains, envelope 9.4) and used to scale
# the crank to other bores and strokes. [E]
PITCH_PER_BORE = 111.76 / 104.8
PIN_PER_BORE = 53.34 / 104.8
MAIN_PER_BORE = 60.0 / 104.8
BANK_OFFSET_PER_BORE = 38.6 / 104.8     # flat engine: opposed rods side by side
NOSE_TAIL_MM = 180.0                    # propeller flange, thrust faces, tail [E]


def geom(n_cyl, bore, stroke, layout="flat"):
    """Crank geometry in mm and kg. layout: 'flat' (one throw per cylinder,
    opposed banks), 'shared' (two rods per pin: 180-degree or 90-degree V),
    'inline'."""
    pitch = PITCH_PER_BORE * bore
    d_pin, d_main = PIN_PER_BORE * bore, MAIN_PER_BORE * bore
    if layout == "flat":
        throws = n_cyl
        length = (n_cyl / 2) * pitch + BANK_OFFSET_PER_BORE * bore + NOSE_TAIL_MM
    elif layout == "shared":
        throws = n_cyl // 2
        length = throws * pitch + 0.25 * bore + NOSE_TAIL_MM
    else:
        throws = n_cyl
        length = n_cyl * pitch + NOSE_TAIL_MM
    # Billet diameter: counterweight swing. 2 x stroke + 0.3 x pin reproduces
    # the bar sizes billet makers start from (about 8.5 in for a 4.000 in
    # stroke V8, about 7-7.5 in for an 86 mm stroke I6). [E]
    d_billet = 2.0 * stroke + 0.3 * d_pin
    billet_kg = RHO_STEEL * math.pi / 4 * (d_billet / 1000) ** 2 * (length + 25) / 1000
    # Finished crank about 14 % of the billet: an LS 4.000 in forged crank is
    # about 23 kg against a 179 kg bar on this model. [E]
    finished_kg = 0.14 * billet_kg
    return dict(throws=throws, pitch=pitch, d_pin=d_pin, d_main=d_main, length=length,
                d_billet=d_billet, billet_kg=billet_kg, finished_kg=finished_kg)


# ------------------------------------------------------------------ cost model
# One machined steel crank = material + machine hours + one-off NRE + heat
# treatment + grind + balance + inspection. Low/high bands.
STEEL_PER_KG = (7.7, 9.3)        # [S] 4140 HT/annealed round, 8.5-8.75 in, retail (sources file); 4340 not checked, likely higher
NITRIDE = (300, 600)             # [E] gas-nitride lot, one part
BALANCE = (300, 400)             # [S] envelope 2.1
MPI = (100, 300)                 # [E] magnetic-particle inspection and a CMM report


def machined(g, shop):
    """shop: 'specialist' (Crower/Bryant/Winberg class, crank lathes and
    in-house grinding) or 'general' (turn-mill job shop, automotive crank
    grinder for the journals). Returns cost components, (low, high) each."""
    size = (g["d_billet"] / 219.2) ** 0.3          # hours grow weakly with size [E]
    if shop == "specialist":
        rate = (120, 150)                           # $/h [E]
        hours = (9 + 3.7 * g["throws"]) * size      # [E] fitted so calibrate() reproduces the three anchors
        nre = (1000, 2000)                          # drawing check, CAM, crank fixtures [E]
        grind = (0, 0)                              # in-house, inside the hours
    else:
        rate = (100, 160)                           # $/h, turn-mill job shop [E]
        hours = (12 + 4.6 * g["throws"]) * size     # no crank lathe: pins milled by interpolation, about 1.25x the specialist [E]
        nre = (1300, 3800)                          # 10-20 h CAM at $100-150 + soft jaws, steady rest [E]
        grind = (150 + 15 * (g["throws"] + 4), 300 + 30 * (g["throws"] + 4))   # auto crank grinder, new stock [E from the [S] $85-200 regrind]
    c = dict(
        material=(g["billet_kg"] * STEEL_PER_KG[0], g["billet_kg"] * STEEL_PER_KG[1]),
        machining=(hours * rate[0], hours * rate[1]),
        nre=nre, nitride=NITRIDE, grind=grind, balance=BALANCE,
        inspection=MPI if shop == "general" else (0, 0))
    return c, hours


def tot(c):
    return (sum(v[0] for v in c.values()), sum(v[1] for v in c.values()))


def calibrate():
    """Reproduce the three envelope 9.4 anchors [S] with the specialist model.
    Catalog billets carry no NRE (the program exists) and run at a batch rate."""
    rows = []
    # concept H one-off: MANUFACTURING's $6.3k-9k + balance $0.3-0.4k
    gH = geom(6, 104.8, 101.6)
    cH, hH = machined(gH, "specialist")
    rows.append(("H flat-6 one-off (envelope 9.4: $6.6k-9.4k incl. balance)", tot(cH), hH))
    # catalog 2JZ 6-throw 4340 billet, nitrided: $4.0k-4.9k (no NRE, $90-100/h batch rate, no balance)
    g2 = geom(6, 86.0, 86.0, "inline")
    c2, h2 = machined(g2, "specialist")
    c2.update(nre=(0, 0), balance=(0, 0), machining=(h2 * 90, h2 * 100))
    rows.append(("2JZ catalog 6-throw billet (envelope 9.4: $4.0k-4.9k)", tot(c2), h2))
    # Crower custom V8 billet, 4.000 in stroke: $6,288 (no balance)
    g8 = geom(8, 104.8, 101.6, "shared")
    c8, h8 = machined(g8, "specialist")
    c8.update(balance=(0, 0))
    rows.append(("Crower custom V8 4-throw (envelope 9.4: $6,288)", tot(c8), h8))
    return rows, cH


# ------------------------------------------------------------------ route 1
# Built-up crank. 1a: press-fit cheeks on ground pins (one-piece rods, roller
# big ends, as the Porsche 547). 1b: one-throw modules, each a small one-piece
# crank with integral pin, joined at the mains by a bolted face joint (Hirth
# or fitted bolts), plain bearings and split catalog rods.
E_STEEL = 207e3        # MPa
MU_FIT = 0.15          # dry steel shrink fit [A], 0.12-0.20 in the literature


def press_fit(d, L, D_hub, delta_over_d):
    """Lame: fit pressure of a solid pin in a hub of outside diameter D_hub,
    same steel, diametral interference delta. Returns pressure (MPa), torque
    capacity (N m), hub hoop stress at the bore (MPa)."""
    k = (D_hub ** 2 - d ** 2) / (D_hub ** 2)
    p = E_STEEL * delta_over_d / 2 * k
    T = MU_FIT * p * math.pi * d * L * d / 2 / 1000          # N m (mm^3 x MPa / 1000)
    hoop = p * (D_hub ** 2 + d ** 2) / (D_hub ** 2 - d ** 2)
    return p, T, hoop


def throw_torque_peak(bore, p_peak_bar=70.0, stroke=101.6):
    """Peak instantaneous torque one firing cylinder puts through its throw:
    gas force x crank radius x the lever factor near 15-20 deg ATDC (about
    0.45, rod/crank 3.0) [E]."""
    F = p_peak_bar * 0.1 * math.pi / 4 * bore ** 2      # N
    return F * stroke / 2 / 1000 * 0.45, F


def l10_hours(C_kN, P_kN, rpm):
    """ISO 281 roller form, L10 = (C/P)^(10/3) million revs."""
    return (C_kN / P_kN) ** (10 / 3) * 1e6 / (rpm * 60)


def big_end_equiv_load(bore, stroke, rpm, p_peak_bar, m_rec=0.9, lam=0.28):
    """Mean-cubic rod big-end load over 720 deg [E]: about 60 deg of combustion
    at 0.6 of the peak gas force, and inertia (1 + lambda) m r w^2 for the
    rest. Coarse; it sets the order of magnitude."""
    F_gas = p_peak_bar * 0.1 * math.pi / 4 * bore ** 2 / 1000          # kN
    w = rpm * 2 * math.pi / 60
    F_in = m_rec * stroke / 2000 * w ** 2 * (1 + lam) / 1000           # kN
    return ((60 / 720) * (0.6 * F_gas) ** 3 + (660 / 720) * F_in ** 3) ** (1 / 3)


# Route 1a cost [E]: cheeks from 32 mm 4140 pre-hard plate, waterjet, then
# jig-bored and faced; pins and stubs from induction-hardened ground shafting.
def route1a_cost(throws):
    cheeks = 2 * throws + 2
    pins = throws + 2 * throws // 2 + 2          # crankpins + main stubs
    return dict(
        cheek_plate_and_waterjet=(cheeks * 55, cheeks * 110),
        cheek_jig_bore_and_face=(cheeks * 1.0 * 90, cheeks * 1.5 * 130),
        pins_from_ground_shafting=(pins * 40, pins * 90),
        one_piece_rods_custom=(1200, 2500),           # no catalog one-piece rod at LS size [E]
        less_catalog_rods_and_shells=(-800, -400),    # the LS rods and shells it replaces [E]
        roller_cages_and_main_rollers=(throws * 60 + 7 * 60, throws * 150 + 7 * 200),
        assembly_fixture_and_indexing=(800, 2000),
        press_assembly_check_balance=(500, 1000),
    )


def route1b_cost(g):
    """One-throw modules: each is a short one-piece crank turned on a lathe
    with an offset fixture, plus a bolted face joint at each main. [E]"""
    z = g["throws"]
    return dict(
        material=(g["billet_kg"] * 0.45 * STEEL_PER_KG[0], g["billet_kg"] * 0.45 * STEEL_PER_KG[1]),  # short bars waste less
        module_turning=((5 + 4.5 * z) * 100, (8 + 6.0 * z) * 160),
        face_joints=((z + 1) * 150, (z + 1) * 400),   # Hirth needs gear grinding; fitted bolts need a jig ream [E]
        nre=(1500, 4000),
        nitride=NITRIDE, grind=(300, 600), balance=BALANCE, inspection=MPI,
        assembly_and_runout_check=(300, 800),
    )


# ------------------------------------------------------------------ route 3
# Cast crank: fatigue sanity check at the crankpin fillet and cost.
# Endurance limits are 10^7-cycle rotating-bending values for polished
# specimens; [A] until the sources file has them (MANUFACTURING AER-3412).
MATERIALS = {
    #  name: (UTS MPa, endurance Se MPa, notch sensitivity q, modulus GPa, note)
    "4340 Q&T, nitrided (the billet baseline)": (1000, 550, 0.90, 207, "[A] Se with nitrided case, no fillet roll"),
    "pearlitic ductile iron (EN-GJS-700-2 class)": (700, 315, 0.50, 170, "[S] Se 315 MPa, 50 % survival, 50-75 mm section (Zanardi)"),
    "ADI 1050-6 (ISO 17804; ASTM A897 1050/750/7 class)": (1050, 360, 0.55, 165, "[S] Se 360 MPa, 50 % survival, 30-60 mm wall (Zanardi)"),
}
KT_FILLET = 2.0          # pin-to-web fillet, r/d about 0.06 [A]


def pin_fillet_stress(bore, d_pin, p_peak_bar=70.0, arm_per_bore=0.25, m_rec=0.9, stroke=101.6, rpm=3300):
    """Nominal bending stress at the crankpin fillet [E]. The gas force acts on
    the pin with a lever arm to the nearest main of about 0.25 x bore (web plus
    half a main). Inertia reverses the load near TDC exhaust, so the stress
    cycle runs from -inertia to +gas. Returns (mean, alternating) MPa."""
    F_gas = p_peak_bar * 0.1 * math.pi / 4 * bore ** 2
    w = rpm * 2 * math.pi / 60
    F_in = m_rec * stroke / 2000 * w ** 2 * 1.28
    arm = arm_per_bore * bore
    Z = math.pi * d_pin ** 3 / 32
    s_max, s_min = F_gas * arm / Z, -F_in * arm / Z
    return (s_max + s_min) / 2, (s_max - s_min) / 2


def goodman_sf(s_m, s_a, uts, se, q):
    kf = 1 + q * (KT_FILLET - 1)
    return 1 / (kf * s_a / se + s_m / uts), kf


def gyro_nose_stress(J_prop, rpm, q_rad_s, d_nose):
    """Fully reversed rotating bending at the crank nose from propeller
    gyroscopic moment M = J Omega q (direct drive only). [E]"""
    M = J_prop * rpm * 2 * math.pi / 60 * q_rad_s
    return M, M * 1000 / (math.pi * d_nose ** 3 / 32)


def route3_cost(g, adi):
    """Near-net cast crank, first engine. [E] until AER-3412."""
    c = dict(
        gating_design_and_solidification_sim=(800, 2500),
        printed_mold_and_pour=(600, 1800),
        trial_pours_and_scrap=(600, 2400),            # 1-2 extra pours at one-off scrap rates [A]
        rt_and_mpi=(250, 600),
        rough_and_finish_turning=((6 + 2.0 * g["throws"]) * 100, (10 + 3.0 * g["throws"]) * 160),
        grind=(300, 600), balance=BALANCE,
    )
    if adi:
        c["austempering"] = (250, 700)
    return c


# ------------------------------------------------------------------ route 2
# Decouple the propeller: a propeller shaft on its own bearing pair in the nose
# case, joined to the crank by a torsionally stiff, angularly soft coupling
# (disc pack or crowned-tooth gear coupling), so the crank sees torque only.
DECOUPLER_COST = dict(
    prop_shaft_turned_ground_flange=(400, 1000),
    bearing_pair_and_seal=(150, 500),
    nose_case_growth_casting_and_first_op=(300, 1000),
    disc_or_gear_coupling=(300, 1000),
)
DECOUPLER_KG = (5.0, 9.0)   # [E]

# Mass-production cranks that could carry the cylinder sizes on the table.
# Dimensions and prices: [S] where the sources file has them; None = not found.
OE_CRANKS = [
    # price: new retail [S] (sources file) or None (not found). The LS 92 mm
    # stroke is priced as the sourced 4.000 in forgings [E]: the same makers
    # list both. OE cast LS cranks exist and are cheaper; not priced here.
    dict(name="GM LS V8, 92 mm stroke, cross-plane", layout="90 V8", n=8,
         bores=(96.0, 104.8), stroke=92.0, pitch=111.76, price=(819, 1250), tag="[E] as the 4.000 in forgings",
         note="8 cylinders at 200 hp is 25 hp each"),
    dict(name="GM LS V8, 4.000 in stroke, forged 4340 (K1, Callies)", layout="90 V8", n=8,
         bores=(104.8,), stroke=101.6, pitch=111.76, price=(819, 1250), tag="[S]",
         note="concept H's cylinder module exactly; 7.0 L is the 300 hp member's displacement"),
    dict(name="GM 4.3 L 90-degree V6, split pins", layout="90 V6 split-pin", n=6,
         bores=(101.6, 104.8), stroke=88.4, pitch=111.76, price=None, tag="not found",
         note="SBC/LS pitch, so the LS7 liner and piston fit; needs a balance shaft (GM added one in 1992)"),
    dict(name="Toyota 2JZ inline-6, forged, OE new", layout="I6", n=6,
         bores=(86.0,), stroke=86.0, pitch=None, price=(1480, 1480), tag="[S]",
         note="the 86 mm module of concept B; bore pitch not found"),
    dict(name="Subaru EZ36 flat-6, OE new", layout="flat-6", n=6,
         bores=(92.0,), stroke=91.0, pitch=98.4, price=(524, 524), tag="[S]",
         note="the only mass-production boxer-6 crank in the size class; 6.4 mm between bores, tighter than H's 7.0 mm with the Darton MID; no catalog wet liner for it was looked for"),
]
OE_ADDONS = dict(balance=BALANCE, mpi_and_polish=(100, 300))   # [S] balance; [E] inspection


def oe_crank_cost(c):
    """First-engine crank line for a bought crank: price + balance with our
    rotating assembly + inspection. None if the price was not found."""
    if c["price"] is None:
        return None
    return tot(dict(OE_ADDONS, price=c["price"]))


def oe_point(c, bore, bmep=10.3):
    vd = math.pi / 4 * (bore / 1000) ** 2 * (c["stroke"] / 1000) * c["n"] * 1000   # L
    rpm = P_KW * 1000 * 120 / (bmep * 1e5 * vd * 1e-3)                            # 4-stroke, P = BMEP Vd N / 120
    sp = 2 * c["stroke"] / 1000 * rpm / 60
    return vd, rpm, sp


# ------------------------------------------------------------------ route 4
def firing_180v6():
    """TDC opportunities of a 180-degree V6 with 3 pins at 120 deg, two rods per
    pin. Left bank TDC at the pin angle, right bank 180 deg later. Returns the
    best (most even) firing set over 720 deg and its intervals."""
    import itertools
    pins = (0, 120, 240)
    opts = []
    for p in pins:
        opts.append((p, p + 360))                 # left cylinder on pin p
        opts.append(((p + 180) % 360, (p + 180) % 360 + 360))   # right cylinder on pin p
    best = None
    for choice in itertools.product((0, 1), repeat=6):
        ev = sorted(o[c] for o, c in zip(opts, choice))
        iv = [(ev[(i + 1) % 6] - ev[i]) % 720 for i in range(6)]
        score = max(iv) - min(iv)
        if best is None or score < best[0]:
            best = (score, ev, iv)
    return best


def couples_180v6(m_rec, stroke_m, rpm, pitch_m):
    """Free primary couple of a 180-degree V6 on 3 shared pins. The two pistons
    on one pin move the same way in space, so their primary forces add (2m)
    and their secondary forces cancel; across 3 pins at 120 deg the forces
    cancel and leave the inline-3 rocking couple sqrt(3) F a."""
    w = rpm * 2 * math.pi / 60
    F = 2 * m_rec * stroke_m / 2 * w ** 2
    return F, math.sqrt(3) * F * pitch_m


def torsion_3throw():
    """FL-24 check: 3-throw crank, two rods per throw, against H's 6-throw."""
    h = TV.CASES["H flat-6, LS7 module, 3,300 rpm"]
    three = dict(h, z=3, m_rec=2 * h["m_rec"], m_rot=2 * h["m_rot"], jc=1.4 * h["jc"], Leq=0.16)
    out = {}
    for label, c in (("H 6-throw (torsional_h.py)", h), ("180-degree V6, 3 throws", three)):
        f, X, jt, kt, kn = TV.model(c, 1.0)
        cr = TV.campbell(dict(c, z=6), f, X)          # orders of a 6-cylinder engine either way
        out[label] = (f, [(m, o, rpm) for m, ff, o, rpm, mj, rel in cr if abs(o / 3 - round(o / 3)) < 1e-9])
    return out


# ------------------------------------------------------------------ report
def kr(v):
    return f"${v[0]/1000:.1f}k-{v[1]/1000:.1f}k"


if __name__ == "__main__":
    print("## 1. What a one-off machined crank costs, and why\n")
    rows, cH = calibrate()
    print("| Anchor | model | hours |")
    print("|---|---|---|")
    for lab, t, h in rows:
        print(f"| {lab} | {kr(t)} | {h:.0f} |")
    gH = geom(6, 104.8, 101.6)
    t = tot(cH)
    print(f"\nConcept H crank: billet {gH['d_billet']:.0f} mm x {gH['length']+25:.0f} mm, {gH['billet_kg']:.0f} kg of bar; "
          f"finished about {gH['finished_kg']:.0f} kg ({gH['finished_kg']/gH['billet_kg']:.0%} of the bar).\n")
    print("| Component (H, specialist, first engine) | low | high | share of the mid |")
    print("|---|---|---|---|")
    mid = math.sqrt(t[0] * t[1])
    for k, v in cH.items():
        if v[1] == 0:
            continue
        print(f"| {k} | ${v[0]:,.0f} | ${v[1]:,.0f} | {math.sqrt(max(v[0],1)*v[1])/mid:.0%} |")
    print(f"| **total** | **${t[0]:,.0f}** | **${t[1]:,.0f}** | |")

    print("\n### Does the crank shrink with the cylinder? Same model, specialist shop, first engine\n")
    print("| Crank | throws | stroke (mm) | pin (mm) | bar (kg) | finished (kg) | material | machining | total |")
    print("|---|---|---|---|---|---|---|---|---|")
    for lab, n, b, s, lay in (("A flat-4, 130.2 x 111.1", 4, 130.2, 111.1, "flat"),
                              ("H flat-6, 104.8 x 101.6", 6, 104.8, 101.6, "flat"),
                              ("flat-6, 92 x 80", 6, 92.0, 80.0, "flat"),
                              ("B flat-8, 86 x 64", 8, 86.0, 64.0, "flat"),
                              ("flat-4, 104.8 x 101.6", 4, 104.8, 101.6, "flat"),
                              ("C V4, 2 shared pins, 104.8 x 101.6", 4, 104.8, 101.6, "shared")):
        g = geom(n, b, s, lay)
        c, h = machined(g, "specialist")
        print(f"| {lab} | {g['throws']} | {s:.0f} | {g['d_pin']:.0f} | {g['billet_kg']:.0f} | {g['finished_kg']:.0f} | "
              f"{kr(c['material'])} | {kr(c['machining'])} | {kr(tot(c))} |")

    print("\n## 2. Route 5: a crank drawn for a general turn-mill shop\n")
    c5, h5 = machined(gH, "general")
    for k, v in c5.items():
        if v[1]:
            print(f"- {k}: {kr(v)}")
    print(f"- **total, first engine: {kr(tot(c5))}** ({h5:.0f} machine hours) against the specialist's {kr(t)}")
    c5r = dict(c5, nre=(0, 0))
    print(f"- second and later cranks off the same program: {kr(tot(c5r))}")

    print("\n## 3. Route 1: built-up crank\n")
    bore = 104.8
    T_pk, F_pk = throw_torque_peak(bore)
    T_mean = P_KW * 1000 / (3300 * 2 * math.pi / 60)
    print(f"Peak gas force {F_pk/1000:.1f} kN at 70 bar [A]; peak torque one firing throw passes {T_pk:,.0f} N m; "
          f"mean engine torque at 200 hp, 3,300 rpm {T_mean:.0f} N m.\n")
    print("| Pin d (mm) | fit length = cheek (mm) | hub OD (mm) | interference | fit pressure (MPa) | slip torque (N m) | hub hoop (MPa) | slip torque / peak throw torque |")
    print("|---|---|---|---|---|---|---|---|")
    for d, L, D, dl in ((53.3, 14.6, 100, 0.0010), (53.3, 14.6, 100, 0.0018), (53.3, 25.0, 100, 0.0018), (60.0, 30.0, 110, 0.0018)):
        p, T, hoop = press_fit(d, L, D, dl)
        print(f"| {d} | {L} | {D} | {dl*1000:.1f} per mille | {p:.0f} | {T:,.0f} | {hoop:.0f} | {T/T_pk:.2f} |")
    print("\nRoller big end (one-piece rod, needle cage on the pin), L10 at cruise:\n")
    print("| Case | equivalent load P (kN) | cage C (kN) | L10 (h) | C needed for L10 = 2,000 h | C for L10 = 10,000 h |")
    print("|---|---|---|---|---|---|")
    for lab, b, s, rpm, pk, mrec in (("H, 104.8 bore, cruise 2,900 rpm, 50 bar", 104.8, 101.6, 2900, 50, 0.9),
                                     ("H, takeoff 3,300 rpm, 70 bar", 104.8, 101.6, 3300, 70, 0.9),
                                     ("86 mm bore, cruise 5,000 rpm, 50 bar", 86.0, 64.0, 5000, 50, 0.5)):
        P = big_end_equiv_load(b, s, rpm, pk, mrec)
        for C in (50.0,):
            need = lambda L: P * (L * rpm * 60 / 1e6) ** 0.3
            print(f"| {lab} | {P:.1f} | {C:.0f} [S] | {l10_hours(C, P, rpm):,.0f} | {need(2000):.0f} | {need(10000):.0f} |")
    c1a = route1a_cost(6)
    print(f"\nRoute 1a cost, first engine: {kr(tot(c1a))}")
    for k, v in c1a.items():
        print(f"- {k}: {kr(v) if v[0] >= 0 else f'-${-v[0]/1000:.1f}k to -${-v[1]/1000:.1f}k'}")
    c1b = route1b_cost(gH)
    print(f"\nRoute 1b (one-throw modules, bolted face joints, plain bearings), first engine: {kr(tot(c1b))}")
    for k, v in c1b.items():
        print(f"- {k}: {kr(v)}")
    print(f"- crank grows by about {7 * 12:.0f}-{7 * 20:.0f} mm (a 12-20 mm joint flange at each of 7 joints) [E]")

    print("\n## 4. Route 3: cast crank, fatigue sanity check at the crankpin fillet\n")
    s_m, s_a = pin_fillet_stress(104.8, gH["d_pin"])
    print(f"H crankpin {gH['d_pin']:.1f} mm, 70 bar peak [A], lever 0.25 x bore: nominal mean {s_m:.0f} MPa, alternating {s_a:.0f} MPa; Kt {KT_FILLET} [A].\n")
    print("| Material | UTS | Se | q | Kf | Goodman safety factor | modulus (GPa) | note |")
    print("|---|---|---|---|---|---|---|---|")
    for name, (uts, se, q, E, note) in MATERIALS.items():
        sf, kf = goodman_sf(s_m, s_a, uts, se, q)
        print(f"| {name} | {uts} | {se} | {q} | {kf:.2f} | {sf:.2f} | {E} | {note} |")
    print("\nDirect drive adds propeller gyroscopic bending at the nose (rotating, fully reversed):\n")
    for Jp, q in ((1.0, 1.0), (2.5, 1.0), (1.0, 2.5)):
        M, s = gyro_nose_stress(Jp, 3300, q, 65.0)
        print(f"- J {Jp} kg m^2, {q} rad/s pitch or yaw rate [A]: moment {M:.0f} N m, nominal {s:.0f} MPa at a 65 mm nose")
    # torsional effect of the lower modulus
    print(f"\nLower modulus moves crank mode 1 by sqrt(E/207): ADI x{math.sqrt(165/207):.2f}, so H's 261 Hz goes to about "
          f"{261*math.sqrt(165/207):.0f} Hz and the 6th-order crossing from 2,610 to about {2610*math.sqrt(165/207):,.0f} rpm.")
    for adi in (False, True):
        c3 = route3_cost(gH, adi)
        print(f"\nRoute 3 cost, {'ADI' if adi else 'as-cast ductile iron'}, first engine: {kr(tot(c3))}")
        for k, v in c3.items():
            print(f"- {k}: {kr(v)}")

    print("\n## 5. Route 4: 180-degree V6 on 3 shared pins\n")
    score, ev, iv = firing_180v6()
    print(f"Most even firing order available over 720 deg: TDCs at {ev}; intervals {iv} deg (even would be 120 throughout).")
    F, Mc = couples_180v6(0.9, 0.1016, 3300, 0.11176)
    print(f"Free primary couple at 3,300 rpm: primary force per pin {F/1000:.1f} kN (both rods), couple {Mc:,.0f} N m at 55 Hz; "
          f"crank counterweights can halve it to a {Mc/2:,.0f} N m rotating couple; a counter-rotating balance shaft removes the rest.")
    print("H's flat-6: all primary and secondary forces and couples cancel (the three bank-offset couples sum to zero at 120 deg).")
    for lab, (f, cr) in torsion_3throw().items():
        print(f"- {lab}: modes {f[0]:.0f} / {f[1]:.0f} / {f[2]:.0f} Hz; 6-cylinder major-order crossings (orders 3, 6, 9) idle to 105 %: "
              + ("; ".join(f"mode {m} x order {o:g} at {rpm:,.0f} rpm" for m, o, rpm in cr) or "none"))
    g3 = geom(6, 104.8, 101.6, "shared")
    c4, _ = machined(g3, "specialist")
    print(f"\n3-throw crank, specialist, first engine: {kr(tot(c4))} (bar {g3['billet_kg']:.0f} kg, length {g3['length']:.0f} mm) "
          f"against 6-throw {kr(t)}; a balance shaft, gears and bearings add about $0.3k-1.0k and 3-5 kg [E].")

    print("\n## 6. Route 2: mass-production cranks, once the propeller loads are off the crank\n")
    print(f"Decoupler (propeller shaft on its own bearings + stiff disc or gear coupling): {kr(tot(DECOUPLER_COST))}, "
          f"{DECOUPLER_KG[0]:.0f}-{DECOUPLER_KG[1]:.0f} kg [E].\n")
    print("| Crank | layout | bore (mm) | stroke | Vd (L) | rpm for 200 hp at 10.3 bar | Sp (m/s) | drive it needs | pitch - bore (mm) | crank price | crank line, first engine |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for c in OE_CRANKS:
        for b in c["bores"]:
            vd, rpm, sp = oe_point(c, b)
            drive = "direct + decoupler" if rpm <= 3400 else f"gearbox {rpm/2550:.2f}:1 to 2,550 prop rpm"
            gap = "n/f" if c["pitch"] is None else f"{c['pitch'] - b:.1f}"
            pr = "not found" if c["price"] is None else f"${c['price'][0]:,}-{c['price'][1]:,} {c['tag']}"
            line = oe_crank_cost(c)
            print(f"| {c['name']} | {c['layout']} | {b} | {c['stroke']} | {vd:.2f} | {rpm:,.0f} | {sp:.1f} | {drive} | {gap} | {pr} | "
                  f"{'-' if line is None else kr(line)} |")
    print(f"\nAgainst the one-off billet line of {kr(t)}.")
