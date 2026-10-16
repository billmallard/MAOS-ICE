"""Turbocharger versus supercharger for concept H, on envelope v1 sourcing (AER-3329).

Hardware: Garrett GT2860RS / GTX2860R class turbocharger with wastegate, and
Rotrex C30-94 centrifugal supercharger on a fixed belt step-up (envelope v1
section 10, the only catalog supercharger that fits the duty). Both feed the
same air-to-air intercooler.

Method (Heywood ch. 6; ideal-gas, steady flow, 1-D):
  - ISA atmosphere; ISA+20 C for the hot case.
  - Required pressure ratio: sea-level manifold pressure (1.00 bar) plus the
    intercooler drop, over ambient less the filter drop.
  - Compressor power: m cp T1 (PR^((g-1)/g) - 1) / eta_c.
  - Turbine expansion ratio to supply that power from the exhaust, and the
    pumping work of the resulting exhaust back-pressure:
    (p3 - p2) x Vd x N / 2.
  - Supercharger on a fixed ratio: the isentropic head scales with impeller
    tip speed squared, so with crank rpm squared (Euler; Dixon ch. 7).
  - Ground-adjustable propeller (drive pick 3b): absorbed power ~ rho n^3,
    calibrated so that full throttle at sea level reaches 2,570 rpm in an
    80 kt climb (drive_match.py, RANKING_PHASE1.md section 7). This is a
    fixed-advance-ratio approximation; it gives the rpm trend, not the value.
  - Engine power at constant BMEP is proportional to manifold pressure and rpm
    (charge-temperature effects folded into the intercooler holding ~45 C).
  - Unboosted power at altitude: Gagg-Ferrar, P/P0 = sigma - (1 - sigma)/7.55.

Every efficiency and loss below is ASSUMED unless tagged; the compressor-map
match is not checked (no digitized map; envelope 10.1 leaves it to PROPULSION).

Run: python3 normalizer_h.py
"""
import math

from scipy.optimize import brentq

CP, G = 1005.0, 1.4
K = (G - 1) / G
CP_E, KE = 1150.0, 0.33 / 1.33          # exhaust gas
P0, T0 = 1.01325, 288.15                # bar, K
VD = 5.26e-3                            # m^3, concept H (member_200.py)
N_RATED = 3300.0
P_RATED = 149.1                         # kW, 200 hp
M_AIR = 0.160                           # kg/s at 200 hp (envelope 10, from 46.2 kg/h fuel, AFR ~12.5)
AFR = 12.5
MAP_SL = 1.00                           # bar, sea-level manifold pressure held by normalizing
DP_IC, DP_FILT = 0.05, 0.02             # bar, intercooler and filter drops, ASSUMED
ETA_C = (0.60, 0.72)                    # compressor isentropic efficiency band, ASSUMED (map not checked)
ETA_T, ETA_MECH = 0.70, 0.97            # turbine, turbo bearing, ASSUMED
ETA_BELT = 0.95                         # belt + Rotrex traction drive, ASSUMED
T3 = 1100.0                             # K, turbine inlet at rich takeoff mixture, ASSUMED
DP_EXH = 0.03                           # bar, downpipe and outlet loss, ASSUMED
P3_SL_GATE_OPEN = (0.10, 0.20)          # bar over ambient at SL with the gate open, ASSUMED
N_CLIMB_SL = 2570.0                     # rpm, 3b at full throttle, 80 kt, SL (section 7)


def isa(ft, dT=0.0):
    h = ft * 0.3048
    T = T0 - 0.0065 * h
    p = P0 * (T / T0) ** 5.2559
    return p, T + dT, (p / P0) / ((T + dT) / T0)    # p bar, T K, sigma


def pr_required(ft, dT=0.0):
    p, T, _ = isa(ft, dT)
    return (MAP_SL + DP_IC) / (p - DP_FILT)


def comp_power(m, T1, pr, eta):
    return m * CP * T1 * (pr ** K - 1) / eta / 1000.0    # kW


def comp_out_T(T1, pr, eta):
    return T1 * (1 + (pr ** K - 1) / eta)


def turbine_er(Wc_kW, m_air):
    m_e = m_air * (1 + 1 / AFR)
    need = Wc_kW * 1000 / ETA_MECH
    x = 1 - need / (m_e * CP_E * T3 * ETA_T)
    return x ** (-1 / KE)


def pumping_kW(dp_bar, n):
    return dp_bar * 1e5 * VD * n / 60 / 2 / 1000


def gagg_ferrar(sigma):
    return sigma - (1 - sigma) / 7.55


def prop_rpm(available, rho_ratio):
    """rpm at which the propeller absorbs what the engine delivers at that rpm."""
    k = P_RATED * (N_CLIMB_SL / N_RATED) / (N_CLIMB_SL ** 3)     # calibrated at SL, NA, full throttle
    return brentq(lambda n: available(n) - k * rho_ratio * n ** 3, 1000, 4000)


if __name__ == "__main__":
    print("## Duty, 200 hp at 3,300 rpm\n")
    print("| Altitude | ISA dT | ambient p (bar) | T1 (K) | PR required | compressor power (kW), eta 0.72 / 0.60 | compressor out (C), 0.72 / 0.60 | corrected flow (lb/min) |")
    print("|---|---|---|---|---|---|---|---|")
    for ft in (0, 8000, 12000):
        for dT in (0, 20):
            p, T, _ = isa(ft, dT)
            pr = pr_required(ft, dT)
            wc = [comp_power(M_AIR, T, pr, e) for e in ETA_C[::-1]]
            t2 = [comp_out_T(T, pr, e) - 273.15 for e in ETA_C[::-1]]
            corr = M_AIR * math.sqrt(T / T0) / (p / P0) * 132.28
            print(f"| {ft:,} ft | +{dT} | {p:.3f} | {T:.1f} | {pr:.2f} | {wc[0]:.1f} / {wc[1]:.1f} | {t2[0]:.0f} / {t2[1]:.0f} | {corr:.1f} |")

    print("\n## Turbocharger: turbine expansion ratio and back-pressure cost at 3,300 rpm\n")
    print("| Case | compressor power (kW) | turbine ER needed | p3 (bar) | p3 - p2 (bar) | pumping (kW) | share of 149 kW |")
    print("|---|---|---|---|---|---|---|")
    for ft, dT in ((12000, 20), (12000, 0), (8000, 20)):
        p, T, _ = isa(ft, dT)
        pr = pr_required(ft, dT)
        for eta in ETA_C[::-1]:
            wc = comp_power(M_AIR, T, pr, eta)
            er = turbine_er(wc, M_AIR)
            p3 = (p + DP_EXH) * er
            dp = p3 - MAP_SL
            print(f"| {ft:,} ft ISA+{dT}, eta_c {eta} | {wc:.1f} | {er:.2f} | {p3:.2f} | {dp:+.2f} | {pumping_kW(dp, N_RATED):+.1f} | {pumping_kW(dp, N_RATED)/P_RATED:+.1%} |")
    for dp in P3_SL_GATE_OPEN:
        print(f"| SL, gate open, p3 - p2 = {dp:.2f} bar | 0 | - | - | {dp:+.2f} | {pumping_kW(dp, N_RATED):+.1f} | {pumping_kW(dp, N_RATED)/P_RATED:+.1%} |")
    print("\nNegative p3 - p2 is a pumping gain: at altitude the turbine inlet sits below the normalized manifold.")

    print("\n## Supercharger on a fixed ratio: what the rpm does to the boost\n")
    p, T, sig = isa(12000, 20)
    pr_design = pr_required(12000, 20)
    head_design = CP * T * (pr_design ** K - 1)          # J/kg isentropic at 3,300 rpm
    print(f"Ratio set so the Rotrex makes PR {pr_design:.2f} at 3,300 rpm, 12,000 ft ISA+20.\n")
    print("| rpm | PR | manifold (bar) | power at that rpm, % of rated | drive power (kW), eta 0.72 / 0.60 |")
    print("|---|---|---|---|---|")
    for n in (3300, 3000, 2800, 2570):
        head = head_design * (n / N_RATED) ** 2
        pr = (1 + head / (CP * T)) ** (1 / K)
        mp = min(pr * (p - DP_FILT) - DP_IC, MAP_SL)
        m = M_AIR * (mp / MAP_SL) * (n / N_RATED)
        drv = [m * head / e / ETA_BELT / 1000 for e in ETA_C[::-1]]
        pw = mp / MAP_SL * n / N_RATED
        print(f"| {n:.0f} | {pr:.2f} | {mp:.2f} | {pw:.0%} | {drv[0]:.1f} / {drv[1]:.1f} |")

    print("\n## Climb at full throttle with the ground-adjustable propeller (3b), 80 kt, ISA\n")
    print("ISA, because the propeller law is calibrated at sea-level ISA. The supercharger ratio is still the ISA+20 design above.\n")
    print("| Altitude | rpm, turbo | net power, turbo (% of 200 hp) | rpm, supercharger | net power, supercharger | rpm, no normalizer | net power, no normalizer |")
    print("|---|---|---|---|---|---|---|")
    eta = ETA_C[1]
    for ft in (0, 8000, 12000):
        p, T, sig = isa(ft, 0)
        rho = sig

        def turbo(n):
            return P_RATED * n / N_RATED

        def sc(n):
            head = head_design * (n / N_RATED) ** 2
            pr = (1 + head / (CP * T)) ** (1 / K)
            mp = min(pr * (p - DP_FILT) - DP_IC, MAP_SL)
            m = M_AIR * (mp / MAP_SL) * (n / N_RATED)
            return P_RATED * mp / MAP_SL * n / N_RATED - m * head / eta / ETA_BELT / 1000

        def na(n):
            return P_RATED * n / N_RATED * gagg_ferrar(sig)

        cells = []
        for f in (turbo, sc, na):
            n = min(prop_rpm(f, rho), N_RATED)
            cells.append(f"{n:.0f} | {f(n)/P_RATED:.0%}")
        print(f"| {ft:,} ft | " + " | ".join(cells) + " |")
    print("\nThe supercharger is throttled to 1.00 bar wherever it could make more, but is still charged"
          " its full head times the engine flow. That is an upper bound on its drive power at low altitude;"
          " the real figure depends on how it is unloaded (bypass or inlet throttle), which is not modelled.")

    print("\n## Loss of the normalizer: power left at full rpm (Gagg-Ferrar)\n")
    for ft in (8000, 12000):
        _, _, sig = isa(ft, 0)
        print(f"- {ft:,} ft ISA: sigma {sig:.3f}, {gagg_ferrar(sig):.0%} of rated, about {200*gagg_ferrar(sig):.0f} hp")
