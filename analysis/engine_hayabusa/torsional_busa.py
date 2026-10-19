"""Torque excitation and a damped geared drive: a Hayabusa behind a gearbox (AER-3525).

Question 3 of AER-3525: does the torsional risk of a high-rpm inline-4 behind a
gearbox get better or worse than concept B (phase 0), and how does it compare
with the Rotax 912, the 4-cylinder gearbox engine that flies in numbers?

Method, in three steps.

1. Crank torque of one cylinder over 720 degrees: a single-zone cylinder
   pressure (polytropic compression and expansion, n = 1.32; a Wiebe burn,
   a = 5, m = 2, 20 degrees BTDC start, 55 degrees long; blowdown from 140
   degrees ATDC; Heywood ch. 9 form) with the heat release scaled to a target
   IMEP, times the exact slider-crank lever arm; plus the reciprocating inertia
   torque. Cylinders are summed at their firing offsets (even firing).
2. Fourier orders of the summed torque, per crank revolution. For an evenly
   fired 4-cylinder 4-stroke the major orders are 2, 4, 6; for 8 cylinders,
   4 and 8.
3. A two-inertia drive reflected to the crank: J_e (crank, rods, primary,
   generator rotor), a coupling of stiffness k with viscous damping (damping
   ratio ZETA on the coupled mode), the propeller J_p / i^2 with aerodynamic
   damping c = 2 Q / w (Q goes as w^2 on a fixed-pitch propeller). Each order
   is applied at J_e; the alternating torque in the coupling (the gear mesh)
   is added order by order (in-phase, an upper bound) and divided by the mean
   torque. Above 1, the mesh torque reverses every firing pulse: gear hammer,
   and the classic PSRU fatigue path (FL-2).

Loads follow a fixed-pitch propeller curve: full throttle at the takeoff rpm,
IMEP falling as rpm^2 below it (torque on a propeller curve), plus a friction
allowance. Every inertia, stiffness and mass is ASSUMED, with bands, until
parts are weighed. The point is the ratio between engines on one method, not
an absolute stress. A dynamometer torsional survey with the real drive is the
final check.

Run: python3 torsional_busa.py
"""
import math

import numpy as np

N_POLY = 1.32
P_IM, P_EX = 1.0e5, 1.08e5
ZETA = 0.08          # coupled-mode damping ratio of a rubber or friction coupling, ASSUMED
FMEP = 1.6e5         # Pa, friction at high rpm (Heywood ch. 13 class), ASSUMED; IMEP = BMEP + FMEP

# name, z, bore, stroke, rod, CR, takeoff rpm, takeoff BMEP (Pa), idle, ratio, m_rec per cyl, J_e band, J_p band
ENGINES = {
    "Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1": dict(
        z=4, B=0.081, S=0.065, L=0.1155, CR=11.0, n_to=7000, bmep=13.0e5, idle=1700, i=2.92,
        m_rec=(0.42, 0.52), Je=(0.020, 0.050), Jp=(0.6, 1.2)),
    "Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1": dict(
        z=4, B=0.084, S=0.061, L=0.1025, CR=10.8, n_to=5800, bmep=11.25e5, idle=1400, i=2.43,
        m_rec=(0.42, 0.52), Je=(0.030, 0.060), Jp=(0.6, 1.2)),
    "Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1": dict(
        z=8, B=0.086, S=0.064, L=0.110, CR=9.8, n_to=5800, bmep=10.3e5, idle=1800, i=2.40,
        m_rec=(0.42, 0.52), Je=(0.050, 0.080), Jp=(1.0, 1.8)),
}
# Rotax 912 ULS: bore/stroke 84/61, CR 10.8, 73.5 kW at 5,800, gearbox 2.43 (sources COMPARABLE_ENGINES [R1][R3]);
# rod length ASSUMED. Hayabusa: 81 x 65 mm, rod length ASSUMED from the class (Gen2/3 measured values not found).


_CACHE = {}


def _geometry(e):
    """Kinematics and the two pressure traces (no burn, unit heat) for one engine; p is affine in Q."""
    key = id(e)
    if key in _CACHE:
        return _CACHE[key]
    B, S, L, CR = e["B"], e["S"], e["L"], e["CR"]
    r = S / 2
    A = math.pi * B * B / 4
    Vd = A * S
    Vc = Vd / (CR - 1)
    th = np.radians(np.arange(-360.0, 360.0, 0.25))     # 0 = firing TDC
    sn = np.sin(th)
    x = r * (1 - np.cos(th)) + L - np.sqrt(L * L - (r * sn) ** 2)
    V = Vc + A * x
    dxdt = r * sn + (r * r * sn * np.cos(th)) / np.sqrt(L * L - (r * sn) ** 2)
    d2x = np.gradient(np.gradient(x, th), th)
    th_s, dur = math.radians(-20), math.radians(55)
    i_bdc = int(np.searchsorted(th, -math.pi))
    i_evo = int(np.searchsorted(th, math.radians(140)))
    i_tdc = int(np.searchsorted(th, math.pi))
    xb = np.clip((th - th_s) / dur, 0, None)
    burn = 1 - np.exp(-5 * xb ** 3)

    def trace(p_in, Q):
        p = np.full_like(th, P_EX)
        p[:i_bdc] = p_in
        j_s = int(np.searchsorted(th, th_s))
        p[i_bdc:j_s] = p_in * (V[i_bdc] / V[i_bdc:j_s]) ** N_POLY
        for j in range(j_s, i_evo):
            dQ = Q * (burn[j] - burn[j - 1])
            p[j] = p[j - 1] + ((N_POLY - 1) * dQ - N_POLY * p[j - 1] * (V[j] - V[j - 1])) / V[j - 1]
        pe = p[i_evo - 1]
        p[i_evo:i_tdc] = pe + (P_EX - pe) * (th[i_evo:i_tdc] - th[i_evo - 1]) / (math.pi - th[i_evo - 1])
        return p

    p0 = trace(P_IM, 0.0)
    p1 = trace(P_IM, 1.0) - p0
    out = dict(th=th, A=A, Vd=Vd, V=V, dxdt=dxdt, d2x=d2x, p0=p0, p1=p1,
               imep0=np.trapezoid(p0, V) / Vd, imep1=np.trapezoid(p1, V) / Vd)
    _CACHE[key] = out
    return out


def cylinder_torque(e, rpm, imep, m_rec):
    g = _geometry(e)
    Q = max(0.0, (imep - g["imep0"]) / g["imep1"])
    p = g["p0"] + Q * g["p1"]
    w = rpm * 2 * math.pi / 60
    Tg = (p - P_IM) * g["A"] * g["dxdt"]
    Ti = -m_rec * g["d2x"] * w * w * g["dxdt"]
    return g["th"], Tg + Ti, p.max()


def engine_torque(e, rpm, imep, m_rec, dead=0):
    """Sum of z cylinders at even firing; `dead` cylinders are motored (no burn)."""
    th, T1, pmax = cylinder_torque(e, rpm, imep, m_rec)
    _, T0, _ = cylinder_torque(e, rpm, 0.0, m_rec)
    n = len(th)
    tot = np.zeros(n)
    step = n // e["z"]                    # even firing: 720 / z degrees apart
    for k in range(e["z"]):
        tot += np.roll(T0 if k < dead else T1, k * step)
    return th, tot, pmax


def orders(th, T):
    n = len(T)
    F = np.fft.rfft(T) / n
    mean = F[0].real
    # 720 degrees of data: index h is order h/2 per revolution
    amp = {h / 2: 2 * abs(F[h]) for h in range(1, 25)}
    return mean, amp


def coupling_ratio(e, rpm, imep, m_rec, Je, Jp, k, dead=0, all_orders=False):
    th, T, pmax = engine_torque(e, rpm, imep, m_rec, dead)
    mean, amp = orders(th, T)
    w = rpm * 2 * math.pi / 60
    Jpr = Jp / e["i"] ** 2
    cp = 2 * max(mean, 1.0) / w                           # propeller damping, reflected
    wn = math.sqrt(k * (1 / Je + 1 / Jpr))
    c = 2 * ZETA * wn * (Je * Jpr / (Je + Jpr))
    alt = 0.0
    for q, Tq in amp.items():
        if not all_orders and q not in [e["z"] / 2 * m for m in (1, 2, 3)]:
            continue
        if all_orders and q > 3 * e["z"] / 2:
            continue
        W = q * w
        M = np.array([[-Je * W * W + 1j * W * c + k, -(1j * W * c + k)],
                      [-(1j * W * c + k), -Jpr * W * W + 1j * W * (c + cp) + k]])
        x = np.linalg.solve(M, np.array([Tq, 0]))
        alt += abs((k + 1j * W * c) * (x[0] - x[1]))
    return mean, alt, wn / (2 * math.pi), amp, pmax


def k_for_f(f, Je, Jpr):
    return (2 * math.pi * f) ** 2 / (1 / Je + 1 / Jpr)


def sweep(name, e, f1_frac, mid=True):
    """Coupling tuned so f1 = f1_frac x the idle major-order frequency; returns worst ratio over idle..105 %."""
    Je = sum(e["Je"]) / 2 if mid else e["Je"][0]
    Jp = sum(e["Jp"]) / 2 if mid else e["Jp"][1]
    m_rec = sum(e["m_rec"]) / 2 if mid else e["m_rec"][1]
    Jpr = Jp / e["i"] ** 2
    f_idle = e["z"] / 2 * e["idle"] / 60
    k = k_for_f(f1_frac * f_idle, Je, Jpr)
    worst = (0, None)
    rows = []
    for rpm in np.linspace(e["idle"], 1.05 * e["n_to"], 40):
        load = min(1.0, (rpm / e["n_to"]) ** 2)
        imep = max(e["bmep"] * load + FMEP * (rpm / e["n_to"]), 2.0e5)
        mean, alt, f1, amp, pmax = coupling_ratio(e, rpm, imep, m_rec, Je, Jp, k)
        rows.append((rpm, mean, alt, alt / mean))
        if alt / mean > worst[0]:
            worst = (alt / mean, rpm)
    return k, f1, rows, worst


if __name__ == "__main__":
    print("## 1. Crank torque at takeoff, full throttle (mid inertias and masses)\n")
    print("| Engine | rpm | IMEP (bar) | peak cylinder pressure (bar) | mean torque (N m) | major order | its amplitude (N m) | amplitude / mean | 2nd-order inertia part alone (N m) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, e in ENGINES.items():
        m = sum(e["m_rec"]) / 2
        imep = e["bmep"] + FMEP
        th, T, pmax = engine_torque(e, e["n_to"], imep, m)
        mean, amp = orders(th, T)
        q = e["z"] / 2
        _, Tin, _ = engine_torque(e, e["n_to"], 1.0e3, m)   # nearly no gas load: the inertia part
        _, ain = orders(th, Tin)
        print(f"| {name} | {e['n_to']:,} | {imep/1e5:.1f} | {pmax/1e5:.0f} | {mean:.0f} | {q:.0f} | {amp[q]:.0f} | {amp[q]/mean:.2f} | {ain[q]:.0f} |")

    print("\n## 2. Two-inertia window (phase-0 method), firing band idle to 105 %\n")
    print("| Engine | J_e (kg m^2) | J_p reflected (kg m^2) | firing band (Hz) | soft: k below (N m/rad) | stiff: k above (N m/rad) |")
    print("|---|---|---|---|---|---|")
    for name, e in ENGINES.items():
        for Je in e["Je"]:
            Jpr = e["Jp"][0] / e["i"] ** 2
            fi = e["z"] / 2 * e["idle"] / 60
            fr = e["z"] / 2 * 1.05 * e["n_to"] / 60
            print(f"| {name} | {Je:.3f} | {Jpr:.3f} | {fi:.0f} - {fr:.0f} | {k_for_f(fi/1.25, Je, Jpr):,.0f} | {k_for_f(fr*1.25, Je, Jpr):,.0f} |")

    print("\n## 3. Alternating torque at the gear mesh, divided by mean torque, worst point idle to 105 % on a propeller curve\n")
    print("Coupling tuned so the first mode sits at a fraction of the idle major-order frequency. Above 1.0 the mesh torque reverses.\n")
    print("The last row per engine is stiff tuning: f1 at 1.25 x the major-order frequency at 105 % rpm.\n")
    print("| Engine | f1 / idle firing frequency | k (N m/rad, crank side) | f1 (Hz) | wind-up at takeoff mean torque, crank side (deg) | worst ratio, mid inertias | at rpm | worst ratio, light engine + heavy propeller + heavy pistons | ratio at takeoff rpm, mid |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, e in ENGINES.items():
        stiff = 1.25 * 1.05 * e["n_to"] / e["idle"]
        for frac in (0.5, 0.7, 1.5, 3.0, stiff):
            k, f1, rows, worst = sweep(name, e, frac)
            _, _, _, w2 = sweep(name, e, frac, mid=False)
            r_to = [r for r in rows if r[0] >= e["n_to"]][0]
            twist = math.degrees(r_to[1] / k)
            print(f"| {name} | {frac:.2f} | {k:,.0f} | {f1:.0f} | {twist:.1f} | {worst[0]:.2f} | {worst[1]:,.0f} | {w2[0]:.2f} | {r_to[3]:.2f} |")

    print("\n## 4. One cylinder dead (a single-plug engine losing one coil, plug or injector), soft coupling at 0.5 x idle firing frequency\n")
    print("All orders to 3 x z/2 are summed (half-orders appear when a cylinder stops firing). The live cylinders are held at the")
    print("IMEP that keeps the same mean torque the propeller curve asks for, until they reach the takeoff IMEP (then rpm falls).\n")
    print("| Engine | f1 (Hz) | crank rpm where order 0.5 / 1 / 1.5 cross f1 | worst ratio, all live | worst ratio, one dead | at rpm | worst ratio, one dead, in flight (above 45 % rpm) | at rpm | brake power left at the MCP rpm, one dead (share of MCP) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, e in ENGINES.items():
        Je, Jp, m_rec = sum(e["Je"]) / 2, sum(e["Jp"]) / 2, sum(e["m_rec"]) / 2
        Jpr = Jp / e["i"] ** 2
        k = k_for_f(0.5 * e["z"] / 2 * e["idle"] / 60, Je, Jpr)
        f1 = math.sqrt(k * (1 / Je + 1 / Jpr)) / (2 * math.pi)
        z = e["z"]
        worst_live, worst_dead, worst_fl = 0.0, (0.0, 0), (0.0, 0)
        for rpm in np.linspace(e["idle"], e["n_to"], 60):
            load = min(1.0, (rpm / e["n_to"]) ** 2)
            imep = max(e["bmep"] * load + FMEP * (rpm / e["n_to"]), 2.0e5)
            m0, a0, *_ = coupling_ratio(e, rpm, imep, m_rec, Je, Jp, k, 0, True)
            imep_d = min(imep * z / (z - 1), e["bmep"] + FMEP)
            m1, a1, *_ = coupling_ratio(e, rpm, imep_d, m_rec, Je, Jp, k, 1, True)
            worst_live = max(worst_live, a0 / m0)
            if a1 / m1 > worst_dead[0]:
                worst_dead = (a1 / m1, rpm)
            if rpm >= 0.45 * e["n_to"] and a1 / m1 > worst_fl[0]:
                worst_fl = (a1 / m1, rpm)
        imep_mcp = e["bmep"] * 0.9 + FMEP
        left = ((z - 1) / z * imep_mcp - FMEP) / (imep_mcp - FMEP)
        cross = " / ".join(f"{60 * f1 / q:,.0f}" for q in (0.5, 1.0, 1.5))
        print(f"| {name} | {f1:.0f} | {cross} | {worst_live:.2f} | {worst_dead[0]:.2f} | {worst_dead[1]:,.0f} | {worst_fl[0]:.2f} | {worst_fl[1]:,.0f} | {left:.0%} |")
