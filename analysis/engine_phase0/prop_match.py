"""Propeller-match physics floor for the phase-0 drive options (AER-3320).

Blade-element / momentum (BEM) model of a generic two-blade propeller with
Prandtl tip loss, swirl, a thin cambered section (Clark-Y-like) and a
compressibility drag rise. It is a *comparative* tool: every option uses the
same blade, so differences come from how each drive and pitch strategy lets
the engine and the propeller meet, not from blade design.

Reference case: the 200 hp family member (149 kW takeoff), normalized, so the
same shaft power is available at sea level and at the 8,000 ft cruise
altitude. Speeds: static to 180 KTAS (the issue's assumed 150-180 KTAS cruise;
there is no airframe). Results are expressed as
    thrust power / rated shaft power  = (usable shaft fraction) * (drive eff) * eta_prop
which is the quantity an airframe would see, independent of its drag.

Methods: Glauert/McCormick annulus momentum + blade element; tip loss
F = 2/pi acos(exp(-B(R-r)/(2 r sin phi))); swirl a' from angular momentum;
section cl = cl0 + a0*alpha (Prandtl-Glauert to M 0.7), soft stall at
cl_max; cd = cd0 + k (cl-cl_d)^2 + 20 (M - Mcrit)^4 (Korn-type rise).
Engine full-throttle power vs rpm: P/P_r = (n/n_r)(1 + 0.25 (1 - n/n_r)),
a broad naturally aspirated torque curve (ASSUMED shape).

Run: python3 prop_match.py [--json out.json]
"""
import json
import math
import sys

import numpy as np
from scipy.optimize import brentq

KT = 0.514444
P_RATED = 200 * 0.745699872 * 1000  # W
B = 2


def isa(h_ft):
    h = h_ft * 0.3048
    T = 288.15 - 0.0065 * h
    p = 101325.0 * (T / 288.15) ** 5.2559
    return p / (287.05 * T), math.sqrt(1.4 * 287.05 * T)


class Prop:
    def __init__(self, D, nst=40, p_nom_over_D=0.8):
        self.R = D / 2
        self.D = D
        r = np.linspace(0.18, 0.99, nst) * self.R
        self.r = r
        self.dr = np.gradient(r)
        x = r / self.R
        self.c = self.R * (0.17 - 0.08 * (x - 0.18) / 0.81)   # tapered chord, c/R 0.17 -> 0.09 (AF ~100 class)
        # helical twist for a nominal pitch; collective beta75 is added
        pn = p_nom_over_D * D
        self.twist = np.arctan(pn / (2 * math.pi * r)) - math.atan(pn / (2 * math.pi * 0.75 * self.R))

    @staticmethod
    def section(alpha, M):
        cl0, a0, clmax = 0.35, 2 * math.pi * 0.9, 1.25
        pg = 1 / math.sqrt(1 - min(M, 0.7) ** 2)
        cl = (cl0 + a0 * alpha) * pg
        if cl > clmax:
            # post-stall plateau with flat-plate-like drag growth (ASSUMED; static
            # and low-speed climb results are the least certain outputs)
            a_s = (clmax / pg - cl0) / a0
            cl = max(clmax - 0.2 * (cl - clmax), 1.0)
            cd_stall = 1.8 * (math.sin(alpha) ** 2 - math.sin(a_s) ** 2)
        else:
            cd_stall = 0.0
        cl = max(cl, -0.8)
        mcrit = 0.72
        cd = 0.0085 + 0.010 * (cl - 0.4) ** 2 + (20 * (M - mcrit) ** 4 if M > mcrit else 0.0) + max(cd_stall, 0.0)
        return cl, cd

    def perf(self, V, n_rps, beta75, rho, a_snd):
        """Thrust (N), shaft power (W), efficiency at airspeed V (m/s), n (rev/s)."""
        Om = 2 * math.pi * n_rps
        T = Q = 0.0
        for r, dr, c, tw in zip(self.r, self.dr, self.c, self.twist):
            beta = beta75 + tw
            ap = 0.0
            def resid(w, ap):
                ut = Om * r * (1 - ap)
                ua = V + w
                phi = math.atan2(ua, ut)
                W = math.hypot(ua, ut)
                cl, cd = self.section(beta - phi, W / a_snd)
                f = B * (self.R - r) / (2 * r * max(math.sin(phi), 1e-4))
                F = 2 / math.pi * math.acos(min(math.exp(-f), 1.0))
                F = max(F, 1e-3)
                cn = cl * math.cos(phi) - cd * math.sin(phi)
                ct = cl * math.sin(phi) + cd * math.cos(phi)
                dT_be = B * 0.5 * rho * W * W * c * cn
                dT_mo = 4 * math.pi * r * rho * ua * w * F
                return dT_be - dT_mo, (phi, W, cn, ct, F, ua)
            for _ in range(3):
                g = lambda w: resid(w, ap)[0]
                wmax = 3 * (Om * self.R) + 1
                if g(0.0) <= 0:
                    w = 0.0
                else:
                    w = brentq(g, 0.0, wmax, xtol=1e-6)
                _, (phi, W, cn, ct, F, ua) = resid(w, ap)
                dQ_be = B * 0.5 * rho * W * W * c * ct * r
                # angular momentum: dQ = 4 pi r^3 rho ua Om a' F
                ap = min(dQ_be / (4 * math.pi * r ** 3 * rho * max(ua, 0.5) * Om * F), 0.3)
            T += B * 0.5 * rho * W * W * c * cn * dr
            Q += B * 0.5 * rho * W * W * c * ct * r * dr
        P = Q * Om
        eta = T * V / P if P > 0 else 0.0
        return T, P, eta


def eng_power(frac_n):
    frac_n = min(frac_n, 1.0)
    return P_RATED * frac_n * (1 + 0.25 * (1 - frac_n))


def solve_beta(prop, V, n, P, rho, a, lo_deg=2, hi_deg=50):
    """Lowest (unstalled-branch) blade angle that absorbs P: scan up from fine."""
    f = lambda b: prop.perf(V, n, b, rho, a)[1] - P
    grid = np.radians(np.arange(lo_deg, hi_deg + 0.1, 1.0))
    prev = grid[0]
    fp = f(prev)
    if fp >= 0:
        return prev
    for b in grid[1:]:
        fb = f(b)
        if fb >= 0:
            return brentq(f, prev, b, xtol=1e-5)
        prev, fp = b, fb
    raise ValueError("cannot absorb power")


def fixed_pitch(prop, beta, n_r, V, rho, a, eff_drive=1.0, ratio_tag=""):
    """Full throttle with a fixed blade angle: rpm floats; capped at redline."""
    g = lambda n: prop.perf(V, n, beta, rho, a)[1] - eng_power(n / n_r) * eff_drive
    lo, hi = 0.3 * n_r, n_r
    if g(hi) < 0:            # prop too light: would overspeed -> throttle to redline
        T, P, eta = prop.perf(V, n_r, beta, rho, a)
        return dict(n=n_r, Pshaft=P / eff_drive, T=T, eta=eta, limit="redline")
    n = brentq(g, lo, hi, xtol=1e-4)
    T, P, eta = prop.perf(V, n, beta, rho, a)
    return dict(n=n, Pshaft=P / eff_drive, T=T, eta=eta, limit="full throttle")


def const_speed(prop, n, V, rho, a, eff_drive=1.0, beta_fine=math.radians(10), beta_coarse=math.radians(45)):
    P = P_RATED * eff_drive
    try:
        beta = solve_beta(prop, V, n, P, rho, a, lo_deg=math.degrees(beta_fine))
    except ValueError:
        beta = beta_coarse
    beta = min(max(beta, beta_fine), beta_coarse)
    if beta == beta_fine:
        r = fixed_pitch(prop, beta, n, V, rho, a, eff_drive)
        r["limit"] = "fine stop"
        return r
    T, P2, eta = prop.perf(V, n, beta, rho, a)
    return dict(n=n, Pshaft=P2 / eff_drive, T=T, eta=eta, limit="governing")


def cvt(prop, beta, n_cap, V, rho, a, eff_drive):
    """Engine held at rated rpm and power; prop rpm free up to the tip cap."""
    P = P_RATED * eff_drive
    g = lambda n: prop.perf(V, n, beta, rho, a)[1] - P
    if g(n_cap) < 0:
        T, P2, eta = prop.perf(V, n_cap, beta, rho, a)
        return dict(n=n_cap, Pshaft=P2 / eff_drive, T=T, eta=eta, limit="prop rpm cap")
    n = brentq(g, 0.2 * n_cap, n_cap, xtol=1e-4)
    T, P2, eta = prop.perf(V, n, beta, rho, a)
    return dict(n=n, Pshaft=P2 / eff_drive, T=T, eta=eta, limit="ratio")


SPEEDS = [0, 60, 80, 100, 120, 150, 165, 180]


def atmos_for(Vkt):
    return isa(0) if Vkt <= 100 else isa(8000)


def sweep(fn):
    rows = []
    for vk in SPEEDS:
        rho, a = atmos_for(vk)
        V = max(vk * KT, 0.0)
        r = fn(V, rho, a)
        r["V"] = vk
        r["thp_frac"] = r["T"] * V / P_RATED
        r["shaft_frac"] = r["Pshaft"] / P_RATED
        rows.append(r)
    return rows


def main():
    # Direct drive: 2,700 rpm, D 1.88 m (74 in). Geared: prop 2,300 rpm, D 2.03 m (80 in).
    n_dir = 2700 / 60
    n_ger = 2300 / 60
    pd = Prop(1.88)
    pg = Prop(2.03)
    rho0, a0 = isa(0)
    rho8, a8 = isa(8000)
    b_climb_d = solve_beta(pd, 80 * KT, n_dir, P_RATED, rho0, a0)
    b_cruise_d = solve_beta(pd, 165 * KT, n_dir, P_RATED, rho8, a8)
    b_comp_d = solve_beta(pd, 130 * KT, n_dir, P_RATED, rho8, a8)
    eff_gear, eff_cvt, eff_2spd = 0.98, 0.88, 0.97
    b_comp_g = solve_beta(pg, 130 * KT, n_ger, P_RATED * eff_gear, rho8, a8)
    # CVT: fixed blade set for best cruise; the ratio supplies climb rpm.
    n_cap_d = 2900 / 60
    b_cvt = solve_beta(pd, 180 * KT, n_dir, P_RATED * eff_cvt, rho8, a8)

    options = {
        "1 Direct drive, fixed pitch (compromise, 130 kt design)":
            sweep(lambda V, r, a: fixed_pitch(pd, b_comp_d, n_dir, V, r, a)),
        "2 Fixed reduction, fixed pitch (bigger slower prop, 130 kt design)":
            sweep(lambda V, r, a: fixed_pitch(pg, b_comp_g, n_ger, V, r, a, eff_gear)),
        "3 Ground-adjustable, climb setting (80 kt design)":
            sweep(lambda V, r, a: fixed_pitch(pd, b_climb_d, n_dir, V, r, a)),
        "3 Ground-adjustable, cruise setting (165 kt design)":
            sweep(lambda V, r, a: fixed_pitch(pd, b_cruise_d, n_dir, V, r, a)),
        "4 CVT + fixed pitch (blade set at 180 kt, eff 0.88)":
            sweep(lambda V, r, a: cvt(pd, b_cvt, n_cap_d, V, r, a, eff_cvt)),
        "4b CVT + fixed pitch, eff 0.94 (sensitivity: metal-belt/toroidal class, UNSOURCED)":
            sweep(lambda V, r, a: cvt(pd, solve_beta(pd, 180 * KT, n_dir, P_RATED * 0.94, rho8, a8), n_cap_d, V, r, a, 0.94)),
        "5 Two-speed gearbox + fixed pitch (cruise blade; low gear 1.25:1; eff 0.97)":
            sweep(lambda V, r, a: max(
                (fixed_pitch(pd, b_cruise_d, n_dir, V, r, a, eff_2spd),
                 fixed_pitch(pd, b_cruise_d, n_dir / 1.25, V, r, a, eff_2spd)),
                key=lambda d: d["T"])),
        "6 In-flight adjustable or constant speed, direct (2,700 rpm)":
            sweep(lambda V, r, a: const_speed(pd, n_dir, V, r, a)),
        "7 Constant speed behind reduction (prop 2,300 rpm, D 2.03 m)":
            sweep(lambda V, r, a: const_speed(pg, n_ger, V, r, a, eff_gear)),
    }
    # self-adjusting: governs between stops with an rpm droop at low speed (ASSUMED 5 %)
    def selfadj(V, r, a):
        frac = 0.95 + 0.05 * min(V / (180 * KT), 1.0)
        res = const_speed(pd, n_dir * frac, V, r, a, eff_drive=eng_power(frac) / P_RATED)
        return res
    options["8a Self-adjusting, governing passive hub (Aeromatic class, historical), 5 % droop ASSUMED"] = sweep(selfadj)
    # flex-blade passive pitch (Prince P-tip class): ~4 in of pitch change on a
    # ~70 in prop, i.e. about +/-1 deg at 0.75R, flat at static, coarse at cruise
    def flex(V, r, a):
        b = b_comp_d + math.radians(-1.0 + 2.0 * min(V / (180 * KT), 1.0))
        return fixed_pitch(pd, b, n_dir, V, r, a)
    options["8b Self-adjusting, flex blade (P-tip class), +/-1 deg ASSUMED"] = sweep(flex)

    # static thrust momentum check: ideal T = (2 rho A P^2)^(1/3)
    A = math.pi * (1.88 / 2) ** 2
    T_ideal = (2 * rho0 * A * P_RATED ** 2) ** (1 / 3)
    return options, dict(T_ideal_static_N=T_ideal,
                         beta_deg=dict(climb=math.degrees(b_climb_d), cruise=math.degrees(b_cruise_d),
                                       compromise=math.degrees(b_comp_d), cvt=math.degrees(b_cvt)))


def md(options, chk):
    L = ["| Option | " + " | ".join(f"{v} kt" for v in SPEEDS) + " |",
         "|---|" + "---|" * len(SPEEDS)]
    for k, rows in options.items():
        cells = []
        for r in rows:
            if r["V"] == 0:
                cells.append(f"T0 {r['T']/1000:.2f} kN")
            elif r["thp_frac"] <= 0.02:
                cells.append("overspeeds")
            else:
                cells.append(f"{r['thp_frac']:.2f} ({r['eta']:.2f}, {r['shaft_frac']:.2f})")
        L.append(f"| {k} | " + " | ".join(cells) + " |")
    L.append("")
    L.append("Cell = thrust power / rated shaft power (prop efficiency, usable shaft fraction). "
             "Static column = static thrust. Speeds to 100 kt at sea level ISA, 120 kt and up at 8,000 ft ISA (normalized: same shaft power). Momentum-ideal static thrust for the 1.88 m disk at 149 kW: "
             f"{chk['T_ideal_static_N']/1000:.2f} kN. Blade angles at 0.75R (deg): "
             + ", ".join(f"{k} {v:.1f}" for k, v in chk["beta_deg"].items()))
    L.append("")
    L.append("Limits reached (by speed): ")
    for k, rows in options.items():
        L.append(f"- {k}: " + ", ".join(f"{r['V']}:{r['limit']}@{r['n']*60:.0f}" for r in rows))
    return "\n".join(L)


if __name__ == "__main__":
    o, chk = main()
    print(md(o, chk))
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w") as f:
            json.dump(dict(options=o, check=chk), f, indent=1)
