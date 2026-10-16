"""Radiator and oil cooler sizing at MCP / Vy / ISA+20 C (AER-3326, narrows R-38).

Case (REQUIREMENTS R-22): maximum continuous power held at Vy climb, sea level
ISA+20 C (35 C). Cross-check at the 12,000 ft critical altitude, ISA+20 C,
same indicated airspeed, where MCP is still held (ruling 3).

Heat (engine_floor.py method, Heywood ch. 12 fractions): MCP = 90 % of 200 hp
(R-3), BSFC 290 g/kWh at MCP (best-power class value, ASSUMED, against 310 at
takeoff), coolant 24 % and oil 5 % of fuel energy.

Core model:
  air side   louvered-fin flat-tube core; Colburn j from Chang & Wang (1997),
             j = Re_Lp^-0.49 (th/90)^0.27 (Fp/Lp)^-0.14 (Fl/Lp)^-0.29
                 (Td/Lp)^-0.23 (Ll/Lp)^0.68 (Tp/Lp)^-0.28 (df/Lp)^-0.05
             straight-fin efficiency; friction f = 4.5 j (ASSUMED, the
             louvered-fin class ratio)
  liquid side h_c A_c = 3 x air-side eta_o h A for coolant, 1 x for oil
             (ASSUMED: the air side dominates, as in automotive cores)
  exchange   epsilon-NTU, crossflow, both fluids unmixed (Kays & London)
  drag       duct momentum: exit velocity from total-pressure loss
             (core dp + 0.15 q diffuser/duct loss, ASSUMED), no Meredith heat
             recovery credited (conservative at climb speed)
  mass       core metal from fin and tube geometry (aluminum), tanks and
             headers +40 % of core (ASSUMED), coolant in the core, then the
             installed system: engine coolant, hoses, two pumps (R-23),
             expansion tank, oil cooler, mounts (line items below)

Vy is an airframe number and there is no airframe (MAOS paused): 80 KIAS is
ASSUMED, and 70 and 90 KIAS are printed as sensitivity.

Run: python3 radiator.py
"""
import math

HP = 0.745699872
P_MCP = 0.90 * 200 * HP          # kW
BSFC_MCP, LHV = 290.0, 42.0
Q_FUEL = P_MCP / (3600 / (BSFC_MCP * LHV))
Q_COOL = 0.24 * Q_FUEL
Q_OIL = 0.05 * Q_FUEL

# core geometry (automotive louvered-fin class), metres
Lp, TH, Fp, Fl, Ll, Tp, DF = 1.2e-3, 28.0, 1.4e-3, 8.0e-3, 6.5e-3, 10.0e-3, 0.08e-3
TUBE_H, TUBE_WALL = 2.0e-3, 0.3e-3
K_AL, RHO_AL = 200.0, 2700.0

CP_AIR, MU, K_AIR, PR = 1007.0, 1.90e-5, 0.0275, 0.71
CP_COOL = 3600.0                 # 50/50 ethylene glycol, J/kg K
COOL_FLOW = 2.5                  # kg/s (about 150 L/min), ASSUMED
T_COOL_IN = 105.0                # C, radiator inlet; 50/50 at a 1.0 bar cap boils near 125 C
CP_OIL, OIL_FLOW, T_OIL_IN = 2100.0, 0.6, 110.0


def isa(h_ft, dT=0.0):
    h = h_ft * 0.3048
    T = 288.15 - 0.0065 * h
    p = 101325.0 * (T / 288.15) ** 5.2559
    T += dT
    return p / (287.05 * T), T - 273.15, p


def geometry(Td):
    """Per square metre of face: air area, sigma, metal mass, liquid volume."""
    n_tubes = 1 / Tp
    fin_area = n_tubes * (1 / Fp) * 2 * Fl * Td          # both faces of each fin
    tube_area = n_tubes * 2 * Td
    A = fin_area + tube_area
    sigma = (Tp - TUBE_H) / Tp * (1 - DF / Fp)
    metal = RHO_AL * (fin_area / 2 * DF + n_tubes * 2 * (Td + TUBE_H) * TUBE_WALL)
    liq_vol = n_tubes * (Td - 2 * TUBE_WALL) * (TUBE_H - 2 * TUBE_WALL)
    return A, fin_area, sigma, metal, liq_vol


def ua_per_face(Td, rho, V_face, liquid_ratio):
    A, Af, sigma, metal, liq = geometry(Td)
    Vc = V_face / sigma
    Re = rho * Vc * Lp / MU
    j = Re ** -0.49 * (TH / 90) ** 0.27 * (Fp / Lp) ** -0.14 * (Fl / Lp) ** -0.29 * (Td / Lp) ** -0.23 \
        * (Ll / Lp) ** 0.68 * (Tp / Lp) ** -0.28 * (DF / Lp) ** -0.05
    h = j * rho * Vc * CP_AIR / PR ** (2 / 3)
    m = math.sqrt(2 * h / (K_AL * DF))
    l = Fl / 2
    eta_f = math.tanh(m * l) / (m * l)
    eta_o = 1 - Af / A * (1 - eta_f)
    hA_air = eta_o * h * A
    UA = 1 / (1 / hA_air + 1 / (liquid_ratio * hA_air))
    f = 4.5 * j
    dp = f * (A / (sigma * 1.0)) / Td * Td * rho * Vc ** 2 / 2   # f (A/Amin) G^2/(2 rho), per face m^2
    return UA, dp, metal, liq, j, Re


def eps_crossflow(ntu, cr):
    return 1 - math.exp((1 / cr) * ntu ** 0.22 * (math.exp(-cr * ntu ** 0.78) - 1))


def size(Q_kW, T_hot, C_hot, liquid_ratio, Td, V_face, rho, T_amb, V_inf):
    """Face area that rejects Q at the given face velocity."""
    def q_of(Af):
        UA, dp, *_ = ua_per_face(Td, rho, V_face, liquid_ratio)
        C_air = rho * V_face * Af * CP_AIR
        Cmin, Cmax = min(C_air, C_hot), max(C_air, C_hot)
        eps = eps_crossflow(UA * Af / Cmin, Cmin / Cmax)
        return eps * Cmin * (T_hot - T_amb) / 1000
    lo, hi = 0.005, 3.0
    if q_of(hi) < Q_kW:
        return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if q_of(mid) < Q_kW:
            lo = mid
        else:
            hi = mid
    Af = hi
    UA, dp, metal, liq, j, Re = ua_per_face(Td, rho, V_face, liquid_ratio)
    mdot = rho * V_face * Af
    q_inf = 0.5 * rho * V_inf ** 2
    dp_tot = dp + 0.15 * q_inf
    Ve2 = V_inf ** 2 - 2 * dp_tot / rho
    if Ve2 <= 0:
        return None
    D = mdot * (V_inf - math.sqrt(Ve2))
    return dict(Af=Af, dp=dp, mdot=mdot, D=D, Pdrag=D * V_inf / 1000, core_kg=metal * Af * 1.4,
                liq_kg=liq * Af * 1070, j=j, Re=Re)


SYSTEM_KG = {   # installed-system line items besides the cores, ASSUMED unless tagged
    "engine-side coolant, 6 L of 50/50": 6.4,
    "hoses, clamps, fittings": 2.5,
    "two electric pumps (R-23), EWP115 class": 2.0,
    "expansion tank + cap + thermostat housing": 1.2,
    "oil lines and thermostat": 1.0,
    "ducts, mounts, flaps (sheet / printed)": 3.0,
}


def run(V_kias=80, Td=0.050, V_face=10.0, h_ft=0, dT=20.0):
    rho, T_amb, p = isa(h_ft, dT)
    rho0 = isa(0)[0]
    V_inf = V_kias * 0.514444 * math.sqrt(1.225 / rho)     # TAS from EAS
    Vf = V_face * math.sqrt(rho0 / rho) if h_ft else V_face   # same duct, same IAS -> same dynamic pressure
    r = size(Q_COOL, T_COOL_IN, COOL_FLOW * CP_COOL, 3.0, Td, Vf, rho, T_amb, V_inf)
    o = size(Q_OIL, T_OIL_IN, OIL_FLOW * CP_OIL, 1.0, 0.040, Vf, rho, T_amb, V_inf)
    if r is None or o is None:
        return None
    sys_kg = r["core_kg"] + r["liq_kg"] + o["core_kg"] + o["liq_kg"] * 0.85 + sum(SYSTEM_KG.values())
    return dict(rad=r, oil=o, sys_kg=sys_kg, V_inf=V_inf, T_amb=T_amb,
                drag_frac=(r["Pdrag"] + o["Pdrag"]) / P_MCP,
                kw_per_kg=(Q_COOL + Q_OIL) / sys_kg)


if __name__ == "__main__":
    print(f"MCP {P_MCP:.0f} kW; fuel {Q_FUEL:.0f} kW; coolant {Q_COOL:.0f} kW; oil {Q_OIL:.0f} kW.\n")
    print("| case | V (KIAS) | core depth (mm) | face velocity (m/s) | radiator face (cm^2) | oil cooler face (cm^2) | air (kg/s) | core dp (Pa) | cooling drag power (kW, % MCP) | installed system (kg) | kW per kg |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    rows = []
    for (case, h) in (("SL ISA+20", 0), ("12,000 ft ISA+20", 12000)):
        for V in (70, 80, 90):
            for Td in (0.032, 0.050, 0.064):
                for Vf in (6.0, 8.0, 10.0, 12.0):
                    res = run(V, Td, Vf, h)
                    if res is None:
                        continue
                    r, o = res["rad"], res["oil"]
                    if V == 80 or (Td == 0.050 and Vf == 8.0):
                        print(f"| {case} | {V} | {Td*1000:.0f} | {Vf:.0f} | {r['Af']*1e4:,.0f} | {o['Af']*1e4:,.0f} | {r['mdot']+o['mdot']:.2f} | "
                              f"{r['dp']:.0f} | {r['Pdrag']+o['Pdrag']:.1f} ({100*res['drag_frac']:.1f} %) | {res['sys_kg']:.1f} | {res['kw_per_kg']:.1f} |")
                    rows.append((case, V, Td, Vf, res))
    print("\nInstalled-system line items besides the cores (kg): " + "; ".join(f"{k} {v}" for k, v in SYSTEM_KG.items()))
    sl = [x[4] for x in rows if x[0] == "SL ISA+20" and x[1] == 80]
    best = min(sl, key=lambda r: r["sys_kg"] + 2.0 * r["rad"]["Pdrag"])  # 2 kg per kW of drag power, ASSUMED trade
    print(f"\nSL ISA+20, 80 KIAS: installed system {min(r['sys_kg'] for r in sl):.1f}-{max(r['sys_kg'] for r in sl):.1f} kg across the depth/face-velocity grid; "
          f"drag {min(100*r['drag_frac'] for r in sl):.1f}-{max(100*r['drag_frac'] for r in sl):.1f} % of MCP.")
    print(f"Design point (min of mass + 2 kg per kW of drag power): radiator {best['rad']['Af']*1e4:,.0f} cm^2, "
          f"oil cooler {best['oil']['Af']*1e4:,.0f} cm^2, system {best['sys_kg']:.1f} kg, drag {100*best['drag_frac']:.1f} % MCP, "
          f"{best['kw_per_kg']:.1f} kW/kg, {(Q_COOL)/(best['rad']['Af']*1e4):.3f} kW/cm^2 radiator.")
