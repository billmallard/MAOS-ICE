"""Drive and propeller match at the leading concepts' rpm (AER-3326).

Reuses the phase-0 BEM model (`../engine_phase0/prop_match.py`) unchanged: same
blade, same section, same engine full-throttle curve, same atmosphere rule
(to 100 kt at sea level ISA, 120 kt and up at 8,000 ft ISA, normalized).

Two engine cases:
  H  flat-6 direct, rated 3,300 rpm. UL520iS practice: takeoff 200 hp at
     3,300, MCP 185 hp at 2,800 (0.925). A variable-pitch propeller can run
     that schedule; a fixed-pitch one cannot choose its rpm.
  A  flat-4 direct, rated 2,750 rpm (phase-0 option rows already cover 2,700).

Diameters are set by tip Mach. Helical tip Mach is printed for every row at
static (sea level) and 180 kt (8,000 ft).

Run: python3 drive_match.py   (about 1 min)
"""
import importlib.util
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("pm", os.path.join(HERE, "..", "engine_phase0", "prop_match.py"))
PM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PM)
KT = PM.KT
P = PM.P_RATED
rho0, a0 = PM.isa(0)
rho8, a8 = PM.isa(8000)


def tipM(D, rpm, V, a):
    return math.hypot(math.pi * D * rpm / 60, V) / a


def sched_cs(prop, n_to, n_mcp, mcp_frac, V, rho, a, eff=1.0):
    """Constant speed: takeoff rpm and power to 100 kt, MCP rpm and power above."""
    if V <= 100 * KT:
        return PM.const_speed(prop, n_to, V, rho, a, eff)
    r = PM.const_speed(prop, n_mcp, V, rho, a, eff * mcp_frac)
    return r


def build():
    nH = 3300 / 60
    nH_mcp = 2800 / 60
    ratio = 1.375                    # 3,300 -> 2,400 prop rpm
    nG = nH / ratio
    DH = 1.73                        # 68 in: static tip M 0.86 at 3,300
    DG = 1.98                        # 78 in: static tip M 0.73 at 2,400
    pH, pG = PM.Prop(DH), PM.Prop(DG)
    eff_gear, eff_cvt, eff_2 = 0.98, 0.88, 0.97
    b_comp = PM.solve_beta(pH, 130 * KT, nH, P, rho8, a8)
    b_climb = PM.solve_beta(pH, 80 * KT, nH, P, rho0, a0)
    b_cruise = PM.solve_beta(pH, 165 * KT, nH, P, rho8, a8)
    b_compG = PM.solve_beta(pG, 130 * KT, nG, P * eff_gear, rho8, a8)
    b_cvt = PM.solve_beta(pH, 180 * KT, nH_mcp, P * eff_cvt, rho8, a8)
    opts = {
        "1 Direct, fixed pitch (130 kt), 1.73 m": (DH, 3300,
            lambda V, r, a: PM.fixed_pitch(pH, b_comp, nH, V, r, a)),
        "2 Reduction 1.375:1, fixed pitch (130 kt), 1.98 m": (DG, 2400,
            lambda V, r, a: PM.fixed_pitch(pG, b_compG, nG, V, r, a, eff_gear)),
        "3a Ground-adjustable, climb (80 kt)": (DH, 3300,
            lambda V, r, a: PM.fixed_pitch(pH, b_climb, nH, V, r, a)),
        "3b Ground-adjustable, cruise (165 kt)": (DH, 3300,
            lambda V, r, a: PM.fixed_pitch(pH, b_cruise, nH, V, r, a)),
        "4a CVT 0.88 + fixed pitch, prop capped 2,800": (DH, 2800,
            lambda V, r, a: PM.cvt(pH, b_cvt, nH_mcp, V, r, a, eff_cvt)),
        "5 Two-speed (1.25:1 low) + cruise blade": (DH, 3300,
            lambda V, r, a: max((PM.fixed_pitch(pH, b_cruise, nH, V, r, a, eff_2),
                                 PM.fixed_pitch(pH, b_cruise, nH / 1.25, V, r, a, eff_2)), key=lambda d: d["T"])),
        "6/7/9 Variable pitch direct, held at 3,300": (DH, 3300,
            lambda V, r, a: PM.const_speed(pH, nH, V, r, a)),
        "6/7/9 Variable pitch direct, 3,300 TO / 2,800 MCP (UL schedule)": (DH, 3300,
            lambda V, r, a: sched_cs(pH, nH, nH_mcp, 0.925, V, r, a)),
        "7 Constant speed behind 1.375:1, 1.98 m": (DG, 2400,
            lambda V, r, a: PM.const_speed(pG, nG, V, r, a, eff_gear)),
        "8b Flex blade, +/-1 deg (P-tip class)": (DH, 3300,
            lambda V, r, a: PM.fixed_pitch(pH, b_comp + math.radians(-1 + 2 * min(V / (180 * KT), 1)), nH, V, r, a)),
    }
    return opts


def main():
    out = {}
    for name, (D, rpm, fn) in build().items():
        rows = PM.sweep(fn)
        out[name] = dict(D=D, rpm=rpm, rows=rows,
                         M0=tipM(D, rpm, 0, a0), M180=tipM(D, rpm, 180 * KT, a8))
    return out


if __name__ == "__main__":
    out = main()
    print("| Option (engine H, 200 hp, 3,300 rpm) | tip M static / 180 kt | " + " | ".join(f"{v} kt" for v in PM.SPEEDS) + " |")
    print("|---|---|" + "---|" * len(PM.SPEEDS))
    for k, d in out.items():
        cells = []
        for r in d["rows"]:
            if r["V"] == 0:
                cells.append(f"{r['T']/1000:.2f} kN")
            elif r["thp_frac"] <= 0.02:
                cells.append("overspeeds")
            else:
                cells.append(f"{r['thp_frac']:.2f} ({r['eta']:.2f})")
        print(f"| {k} | {d['M0']:.2f} / {d['M180']:.2f} | " + " | ".join(cells) + " |")
    print("\nCell = thrust power / rated shaft power (propeller efficiency). Static column = static thrust (rank order only; phase-0 fidelity note).")
    print("\nLimits reached:")
    for k, d in out.items():
        print(f"- {k}: " + ", ".join(f"{r['V']}:{r['limit']}@{r['n']*60:.0f}" for r in d["rows"]))
    if "--json" in sys.argv:
        import json
        with open(sys.argv[sys.argv.index("--json") + 1], "w") as f:
            json.dump(out, f, indent=1, default=str)
