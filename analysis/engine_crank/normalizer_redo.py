"""Turbo against supercharger, reopened (AER-3411; corrects RECOST_PHASE1B.md section 6).

Bill's reading (2026-10-17): section 6 says the ground-adjustable propeller
"does not hold rpm in a climb", so a fixed-ratio supercharger gives back its
boost as rpm falls. In a steady climb at Vy the airspeed is held, and with a
normalized engine the rpm does not decay through the climb. He is right, and
normalizer_h.py's own table shows it: turbo rpm 2,570 -> 2,899 -> 3,087 from
sea level to 12,000 ft. What was wrong was the supercharger's design point:
its ratio was set to make full pressure ratio at 3,300 rpm, which a
cruise-pitched propeller reaches only near cruise speed. In the Vy climb the
engine never gets there.

This script keeps every model and number in normalizer_h.py (imported, not
copied) and changes one thing: the Rotrex ratio is set where the duty is,
at the climb rpm at the critical altitude on the hot day. Then it asks:
  1. climb power at Vy, ISA and ISA+20, turbo against both supercharger ratios;
  2. what the new ratio does at cruise rpm (impeller overspeed, bypass loss);
  3. what holding the full 200 hp net would cost in boost and knock margin;
  4. whether a geared engine changes any of it.

Bypass loss (not modelled in phase 1b): a centrifugal compressor held to
1.00 bar manifold by a recirculating bypass still turns at full speed. Its
drive power lies between two bounds: the isentropic work of the pressure
ratio actually needed (ideal modulation, lower bound) and the full head
times the engine flow (phase 1b's upper bound). Without a Rotrex map the
truth is not pinned; both are printed.

Run: python3 normalizer_redo.py
"""
import importlib.util
import math
import os

from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


NZ = load(os.path.join(HERE, "..", "engine_phase1", "normalizer_h.py"), "normalizer_h")
KN = load(os.path.join(HERE, "..", "engine_phase1", "knock.py"), "knock")

CP, K, P_RATED, N_RATED, M_AIR, MAP_SL = NZ.CP, NZ.K, NZ.P_RATED, NZ.N_RATED, NZ.M_AIR, NZ.MAP_SL
ETA = NZ.ETA_C[1]          # 0.72, as the phase 1b climb table
ETA_LO = NZ.ETA_C[0]


def head_at(n, n_design, ft_d=12000, dT_d=20):
    """Isentropic head (J/kg) of the fixed-ratio supercharger at crank rpm n,
    when its ratio gives the required PR at n_design, ft_d, ISA+dT_d."""
    p, T, _ = NZ.isa(ft_d, dT_d)
    pr = NZ.pr_required(ft_d, dT_d)
    h_d = CP * T * (pr ** K - 1)
    return h_d * (n / n_design) ** 2


def sc_power(n, ft, dT, n_design, bypass="upper", eta=ETA):
    """Net shaft power (kW) of the supercharged engine at rpm n."""
    p, T, _ = NZ.isa(ft, dT)
    head = head_at(n, n_design)
    pr_cap = (1 + head / (CP * T)) ** (1 / K)
    mp = min(pr_cap * (p - NZ.DP_FILT) - NZ.DP_IC, MAP_SL)
    m = M_AIR * (mp / MAP_SL) * (n / N_RATED)          # as normalizer_h.py (intercooler holds the charge)
    if bypass == "upper":
        w = head
    else:
        pr_need = min(pr_cap, (MAP_SL + NZ.DP_IC) / (p - NZ.DP_FILT))
        w = CP * T * (pr_need ** K - 1)
    drive = m * w / eta / NZ.ETA_BELT / 1000
    return P_RATED * mp / MAP_SL * n / N_RATED - drive, mp, drive


def turbo_power(n, ft, dT):
    return P_RATED * n / N_RATED


def na_power(n, ft, dT):
    _, _, sig = NZ.isa(ft, dT)
    return P_RATED * n / N_RATED * NZ.gagg_ferrar(sig)


def climb_rpm(f, ft, dT):
    """rpm where the 3b propeller at 80 kt absorbs what the engine makes (the
    normalizer_h.py propeller law, density ratio from ISA+dT)."""
    _, _, sig = NZ.isa(ft, dT)
    return min(NZ.prop_rpm(lambda n: f(n, ft, dT), sig), N_RATED)


def design_rpm_at_climb():
    """Self-consistent design rpm: the climb rpm at 12,000 ft ISA+20 when the
    supercharger's ratio makes exactly 1.00 bar at that rpm."""
    def resid(nd):
        n = climb_rpm(lambda n, ft, dT: sc_power(n, ft, dT, nd, "lower")[0], 12000, 20)
        return n - nd
    return brentq(resid, 2400, 3300)


def cr_limit_at(map_bar):
    """H's knock-limited CR on MON 85 at a manifold pressure other than 1 bar,
    with K* calibrated at 1 bar (the anchors ran unboosted)."""
    kstar = KN.run()[1]
    old = KN.P_IM_ATM
    KN.P_IM_ATM = map_bar / 1.01325
    cr = KN.cr_limit(104.8, 101.6, 3300, 85, kstar)
    KN.P_IM_ATM = old
    return cr


if __name__ == "__main__":
    nd = design_rpm_at_climb()
    print("## 1. Where the supercharger's ratio should be set\n")
    print(f"- Phase 1b set it at 3,300 rpm (12,000 ft ISA+20). With the 3b propeller in an 80 kt climb the engine never reaches 3,300.")
    print(f"- Set at the climb rpm it actually turns at 12,000 ft ISA+20, solved self-consistently: **{nd:,.0f} rpm**.")
    print(f"- That is a pulley ratio {N_RATED/nd:.3f}x the phase 1b one (impeller {100*(N_RATED/nd-1):.0f} % faster at every crank rpm).\n")

    print("## 2. Full-throttle climb at 80 kt, ground-adjustable propeller (3b)\n")
    print("| Atmosphere | Altitude | turbo: rpm, net % | SC ratio at 3,300 (phase 1b): rpm, net % | SC ratio at climb rpm, bypass upper bound | SC ratio at climb rpm, bypass lower bound | no normalizer |")
    print("|---|---|---|---|---|---|---|")
    for dT in (0, 20):
        for ft in (0, 8000, 12000):
            cells = []
            n = climb_rpm(turbo_power, ft, dT)
            cells.append(f"{n:,.0f}, {turbo_power(n, ft, dT)/P_RATED:.0%}")
            for nd_, bp in ((N_RATED, "upper"), (nd, "upper"), (nd, "lower")):
                f = lambda n, ft, dT: sc_power(n, ft, dT, nd_, bp)[0]
                n = climb_rpm(f, ft, dT)
                pw, mp, drv = sc_power(n, ft, dT, nd_, bp)
                cells.append(f"{n:,.0f}, {pw/P_RATED:.0%} (MAP {mp:.2f}, drive {drv:.1f} kW)")
            n = climb_rpm(na_power, ft, dT)
            cells.append(f"{n:,.0f}, {na_power(n, ft, dT)/P_RATED:.0%}")
            print(f"| ISA+{dT} | {ft:,} ft | " + " | ".join(cells) + " |")
    print("\nThe rpm rises through the climb in every normalized column, as Bill said. The phase 1b supercharger loses because"
          " its ratio was set at an rpm the climb never reaches, not because the rpm decays.")

    print("\n## 3. The new ratio at cruise rpm (3,300) and at sea level\n")
    for ft, dT in ((12000, 0), (8000, 0), (0, 0), (0, 20)):
        pr_cap = (1 + head_at(3300, nd) / (CP * NZ.isa(ft, dT)[1])) ** (1 / K)
        for bp in ("upper", "lower"):
            pw, mp, drv = sc_power(3300, ft, dT, nd, bp)
            print(f"- {ft:,} ft ISA+{dT}, 3,300 rpm, bypass {bp} bound: compressor can make PR {pr_cap:.2f}; manifold held {mp:.2f} bar; "
                  f"drive {drv:.1f} kW ({drv/P_RATED:.0%}); net {pw/P_RATED:.0%}")
    print(f"- Turbo at the same points: net 100 % to 12,000 ft, with a 1-2 kW pumping gain at altitude and 1-3 kW back-pressure at sea level (normalizer_h.py).")

    print("\n## 4. Holding the full 200 hp net with the supercharger\n")
    for ft, dT in ((12000, 20), (8000, 20)):
        _, _, drv = sc_power(3300, ft, dT, 3300, "lower")
        map_needed = MAP_SL * (1 + drv / P_RATED)
        print(f"- {ft:,} ft ISA+{dT}: drive about {drv:.1f} kW, so manifold about {map_needed:.2f} bar to net 200 hp; "
              f"H's knock-limited CR on MON 85 falls from {cr_limit_at(1.0):.2f} to {cr_limit_at(map_needed):.2f}")

    print("\n## 5. A geared engine\n")
    for N in (3300, 4800, 5800):
        print(f"- rated {N:,} rpm: with a fixed-pitch propeller the climb rpm is the same fraction of rated ({nd/N_RATED:.0%} at 12,000 ft ISA+20), "
              f"so every percentage above carries over; the belt step-up to the Rotrex is {N_RATED/N:.2f}x the 3,300 rpm engine's.")
    print("- With a constant-speed propeller holding rated rpm in the climb, the supercharger's design point and cruise point coincide; the trade closes"
          " to drive power, mass and heat, as phase 1b said.")
