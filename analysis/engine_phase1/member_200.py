"""200 hp member: physics floor for variant H, part count and cost for every
auto-gas candidate (AER-3326).

Reuses the phase-0 models unchanged (`../engine_phase0/engine_floor.py`,
`cost_floor.py`) and adds:

  1. Variant H, written in phase 1: the concept C cylinder module (GM LS7 bore
     and stroke, 104.8 x 101.6 mm) in a flat-6, direct drive, 3,300 rpm
     takeoff. Flown analog: UL Power UL520iS, 105.6 x 100 mm, 5,254 cc, flat-6,
     direct drive, 200 hp at 3,300 rpm, 185 hp at 2,800 rpm, CR 8.7, MON 88,
     93.3 kg dry, 108 kg ready to fly (ulpower.com, read 2026-10-16). Its
     cylinder is within 0.4 % of the LS7's swept volume.
  2. A part count per concept, by bill-of-materials enumeration (method below).
  3. A cost floor with the casting list made explicit. Phase 0 priced
     crankcase halves and heads but carried no line for the cylinder-jacket
     castings. Phase 1 adds that line for every concept that has one, so the
     200 hp cost floors move up against phase 0. Everything else is the
     phase-0 line items, tags unchanged ([S-MFG], [E], [Q]).

Run: python3 member_200.py
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P0 = os.path.join(HERE, "..", "engine_phase0")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(P0, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


EF = load("engine_floor")
CF = load("cost_floor")
HP = EF.HP

# ---------------------------------------------------------------- variant H
H = dict(key="H", name="Flat-6, LS7 module, direct drive, 3,300 rpm (UL520 recipe, liquid-cooled)",
         cycle="4S-SI", fuel="auto gas", cyl=(4, 6, 8), bore=104.8, stroke=101.6,
         rpm=(2700, 3300, 3400), drive="direct", norm="turbo", analog="ul")
# Mass anchor: UL520iS ready-to-fly 108 kg (contents not defined by UL; taken
# as the closest match to R-37 "installed dry"), x1.10 sand-cast penalty as
# every phase-0 concept, + 4 kg net for water jackets, thermostat and two
# electric pumps in place of fins (ASSUMED), + turbo (phase-0 allowance)
# + 2 kg for the second ECU lane UL sells as an option (ASSUMED).
UL520_RTF = 108.0
UL_EXP = 0.80   # ASSUMED, as the phase-0 geared/V class
H_EXTRA = 4.0 + 2.0


def h_member(i, hp):
    m = EF.member(dict(H, analog="lycoming"), i, hp)   # physics only; mass replaced below
    bare = UL520_RTF * (hp / 200) ** UL_EXP * EF.SAND_CAST_PENALTY
    dry = bare + EF.TURBO_KG[hp] + H_EXTRA
    m.update(bare_kg=bare, dry_kg=dry, installed_kg=dry + m["cool_kg"][1])
    return m


# ---------------------------------------------------------------- part count
# Bill-of-materials enumeration, non-fastener parts. Fasteners (bolts, studs,
# nuts, washers) and O-rings are counted separately as an estimate. Each line
# is a named part class; counts follow the concept's layout as written in
# ARCHITECTURES.md. "Unique" counts a part number once however many times it
# repeats: that is the number a builder orders and MANUFACTURING quotes.
def per_cyl(valves, pushrod, tubes):
    parts = {
        "piston": 1, "piston pin": 1, "pin clips": 2, "rings": 3, "rod": 1,
        "rod shells": 2, "small-end bush": 1, "liner": 1,
        "valves": valves, "valve springs": valves, "retainers": valves, "keepers": 2 * valves,
        "stem seals": valves, "guides": valves, "seat inserts": valves,
        "spark plugs": 2, "coils": 2, "injector": 1, "exhaust header pipe": 1,
    }
    unique = {"piston": 1, "piston pin": 1, "pin clips": 1, "rings": 3, "rod": 1, "rod shells": 1,
              "small-end bush": 1, "liner": 1, "valves": 2, "valve springs": 1, "retainers": 1,
              "keepers": 1, "stem seals": 1, "guides": 1, "seat inserts": 2, "spark plugs": 1,
              "coils": 1, "injector": 1, "exhaust header pipe": 2}
    if pushrod:
        parts.update({"lifters": valves, "pushrods": valves, "rockers": valves})
        unique.update({"lifters": 1, "pushrods": 1, "rockers": 1})
        if tubes:
            parts["pushrod tubes"] = valves
            unique["pushrod tubes"] = 1
    else:
        parts.update({"followers": valves})
        unique.update({"followers": 1})
    return parts, unique


ENGINE_COMMON = {   # every concept: accessories, FADEC, normalizing, cooling hardware
    "starter": 1, "alternator": 1, "coolant pumps (2, R-23)": 2, "thermostat + housing": 2,
    "oil pump assembly": 6, "oil filter + adapter": 2, "sump / oil tank": 1,
    "ECUs (2 lanes)": 2, "harness (2 lanes)": 2, "crank sensors (2)": 2, "cam / phase sensors (2)": 2,
    "MAP/IAT/CLT x2 lanes": 6, "oil P/T, fuel P, knock x2": 5, "throttle body": 1,
    "fuel rail + regulator": 3, "intake plenum": 1, "turbo + wastegate actuator": 2,
    "intercooler": 1, "exhaust collector + wastegate pipe": 2, "covers (valve, timing, accessory)": 4,
    "gaskets (sheet)": 8, "crank seals": 2, "prop flange / hub adapter": 1,
}
GEARBOX = {"gearbox case halves": 2, "input gear": 1, "output gear": 1, "shafts": 2,
           "gearbox bearings": 4, "gearbox seals": 2, "soft torsional coupling": 3,
           "overload / slip clutch": 6}


def count(concept):
    """Returns (parts, unique, fasteners) for the 200 hp member."""
    k = concept
    P, U = {}, {}

    def add(d, u=None, n=1):
        for key, v in d.items():
            P[key] = P.get(key, 0) + v * n
            U[key] = max(U.get(key, 0), (u or {}).get(key, v if u is None else 1))

    common_u = {key: 1 for key in ENGINE_COMMON}
    common_u.update({"coolant pumps (2, R-23)": 1, "ECUs (2 lanes)": 1, "harness (2 lanes)": 2,
                     "crank sensors (2)": 1, "cam / phase sensors (2)": 1, "MAP/IAT/CLT x2 lanes": 3,
                     "oil P/T, fuel P, knock x2": 4, "gaskets (sheet)": 5, "crank seals": 2,
                     "covers (valve, timing, accessory)": 3, "oil pump assembly": 6})
    add(ENGINE_COMMON, common_u)
    fast = 120   # common accessories, covers, manifolds (estimate)
    if k in ("A", "B", "C", "D", "H"):
        lay = dict(A=(4, 2, True, True, 3, 2, 2, 1), B=(8, 4, False, False, 5, 2, 4, 4),
                   C=(4, 2, True, False, 3, 1, 2, 1), D=(7, 2, True, True, 2, 2, 7, 1),
                   H=(6, 2, True, True, 4, 2, 2, 1))[k]
        n, valves, pushrod, tubes, mains, case_pieces, heads, cams = lay
        pc, pu = per_cyl(valves, pushrod, tubes)
        add(pc, pu, n)
        blocks = dict(A=2, B=2, C=0, D=7, H=2)[k]   # cylinder-bank or barrel castings
        add({"crankshaft": 1, "main shells": 2 * mains, "thrust washers": 2,
             "case pieces": case_pieces, "cylinder blocks / barrels": blocks, "heads": heads,
             "camshafts": cams, "cam drive (gears / sprockets / belt)": 3 if cams == 1 else 2 + cams,
             "rocker shafts": 0 if not pushrod else (heads if k != "D" else heads),
             "intake runners": n, "head gaskets": heads if k != "D" else n})
        U.update({"crankshaft": 1, "main shells": 2, "thrust washers": 1, "case pieces": case_pieces,
                  "cylinder blocks / barrels": 0 if blocks == 0 else (1 if k == "D" else 2),
                  "heads": 1 if k == "D" else 2, "camshafts": 1, "cam drive (gears / sprockets / belt)": 3,
                  "rocker shafts": 1, "intake runners": 1, "head gaskets": 1})
        fast += n * 14 + mains * 4 + case_pieces * 10 + heads * 6
        if k == "D":
            add({"master rod": 1, "link rods": n - 1, "link pins": n - 1, "link-pin retainers": 2 * (n - 1),
                 "cam ring + followers carrier": 2, "supercharger impeller + drive gears": 4})
            U.update({"master rod": 1, "link rods": 1, "link pins": 1, "link-pin retainers": 1,
                      "cam ring + followers carrier": 2, "supercharger impeller + drive gears": 4})
            P["turbo + wastegate actuator"] -= 2
            P["rod"] -= n
            P["rod shells"] -= 2 * n - 2
            U["rod"] = 0
    if k == "G":
        n = 4
        per_rotor = {"rotor": 1, "rotor housing": 1, "apex seals": 3, "apex springs": 3,
                     "corner seals": 6, "corner springs": 6, "side seals": 6, "side seal springs": 6,
                     "oil seal rings": 4, "oil seal springs": 4, "rotor bearing": 1, "rotor gear": 1,
                     "spark plugs": 2, "coils": 2, "injector": 1, "exhaust header pipe": 1,
                     "intake runners": 1}
        u = {key: 1 for key in per_rotor}
        u.update({"apex seals": 1, "corner seals": 1, "side seals": 2, "oil seal rings": 2})
        add(per_rotor, u, n)
        add({"intermediate plates": n - 1, "end plates": 2, "stationary gears": 2,
             "eccentric shaft (multi-piece)": 3, "main bearings": 2, "tension bolts / dowels set": 0})
        U.update({"intermediate plates": 1, "end plates": 2, "stationary gears": 1,
                  "eccentric shaft (multi-piece)": 3, "main bearings": 1})
        fast += 4 * 4 + 18 + 40
    if k in ("B", "C", "G"):
        add(GEARBOX, {key: 1 for key in GEARBOX})
        fast += 30
    return sum(P.values()), sum(U.values()), fast, P


# ---------------------------------------------------------------- cost
BLOCK = (600, 1500)   # [E] cylinder-bank / barrel jacket casting, bureau rate, ~half a case half's sand
COST_P1 = dict(CF.CONCEPTS)
COST_P1["H"] = dict(cy="SI", n=(4, 6, 8), heads=(2, 2, 2), cams=(1, 1, 1), crank=(0.9, 1.15, 1.35),
                    case=(0.8, 1.0, 1.25), norm="turbo", drive="direct")
BLOCKS_200 = dict(A=2, B=2, C=0, D=7, G=0, H=2)   # the casting list in count()
BLOCK_SCALE = dict(A=1.0, B=0.9, C=0, D=0.45, G=0, H=1.15)   # by bank size, ASSUMED


def cost_200(k):
    c = COST_P1[k]
    lo, hi = CF.member(c, 1)
    nb = BLOCKS_200[k]
    s = BLOCK_SCALE[k]
    lo += nb * (BLOCK[0] * s + CF.FIRST_OP[0])
    hi += nb * (BLOCK[1] * s + CF.FIRST_OP[1])
    if k == "H":
        # direct drive on the stiff side needs a crank pendulum damper or a
        # proven torsional margin (torsional_h.py): ASSUMED one damper pair
        lo += 400
        hi += 1500
    return lo, hi


if __name__ == "__main__":
    print("## Variant H physics floor\n")
    print("| hp | cyl | Vd (L) | rpm | BMEP (bar) | Sp (m/s) | eta_v SL | fuel (kg/h) | coolant / oil / exhaust (kW) | installed dry (+ cooling mid) kg |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i, hp in enumerate(EF.FAMILY_HP):
        m = h_member(i, hp)
        print(f"| {hp} | {m['n']} | {m['Vd_L']:.2f} | {m['N']} | {m['bmep']:.1f} | {m['Sp']:.1f} | {m['eta_v']:.2f} | "
              f"{m['fuel_kg_h']:.1f} | {m['Qcool']:.0f} / {m['Qoil']:.0f} / {m['Qexh']:.0f} | {m['dry_kg']:.0f} (+{m['cool_kg'][1]:.0f}) |")
    # the 300 hp check at 3,300 rpm, where the prop limits rpm
    m = EF.member(dict(H, analog="lycoming", rpm=(2700, 3300, 3300)), 2, 300)
    print(f"\n300 hp flat-8 held to 3,300 rpm: BMEP {m['bmep']:.1f} bar, eta_v {m['eta_v']:.2f}.")
    m = EF.member(dict(H, analog="lycoming"), 0, 100)
    print(f"100 hp flat-4 at 2,700 rpm: BMEP {m['bmep']:.1f} bar, eta_v {m['eta_v']:.2f}, Sp {m['Sp']:.1f} m/s.")
    for rpm in (2800, 3000, 3300):
        m = EF.member(dict(H, analog="lycoming", rpm=(rpm, rpm, rpm)), 1, 200)
        print(f"200 hp flat-6 at {rpm} rpm: BMEP {m['bmep']:.1f} bar, eta_v {m['eta_v']:.2f}")

    print("\n## 200 hp member: mass, part count, cost\n")
    print("| Concept | installed dry (kg) | + cooling mid (kg) | parts (non-fastener) | unique part numbers | fasteners (est.) | cost floor low / mid / high |")
    print("|---|---|---|---|---|---|---|")
    for k in ("A", "B", "C", "D", "G", "H"):
        if k == "H":
            m = h_member(1, 200)
        else:
            c = next(x for x in EF.CONCEPTS if x["key"] == k)
            m = EF.member(c, 1, 200)
        p, u, f, _ = count(k)
        lo, hi = cost_200(k)
        mid = math.sqrt(lo * hi)
        print(f"| {k} | {m['dry_kg']:.0f} | {m['cool_kg'][1]:.0f} | {p} | {u} | {f} | ${lo/1000:.1f}k / ${mid/1000:.1f}k / ${hi/1000:.1f}k |")
    print("\nCost mid is the geometric mean of the band. The 200 hp target is $22k (Bill, 2026-10-16).")
