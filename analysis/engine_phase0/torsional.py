"""Torsional-vibration floor for the drive options (AER-3320).

Two-inertia model, everything reflected to the crankshaft:
    f1 = (1/2pi) sqrt(k (1/J_e + 1/J_p'))   J_p' = J_prop / ratio^2
Excitation: a 4-stroke with z evenly fired cylinders has its main firing
order at z/2 per crank revolution; idle to redline sets the band it sweeps.
A drive is safe at this fidelity if f1 sits below the firing frequency at
idle by a margin (soft, "sub-idle" tuning, the Rotax/EPI approach) or above
it at redline by a margin (stiff). The window between is where k must not
land. Inertias are representative, ASSUMED until real parts exist.

Run: python3 torsional.py
"""
import math

CASES = [
    # name, cylinders, idle rpm, redline rpm (crank), ratio, J_engine kg m^2, J_prop kg m^2 (at prop)
    ("A direct, 4-cyl 200 hp, 2,750 rpm", 4, 700, 2750, 1.0, 0.25, 1.4),
    ("A direct, 2-cyl 100 hp, 2,750 rpm", 2, 800, 2750, 1.0, 0.15, 0.9),
    ("B geared 2.4:1, 8-cyl 200 hp, 5,800 rpm", 8, 1800, 5800, 2.4, 0.06, 1.4),
    ("C geared 2.0:1, 4-cyl 200 hp, 4,800 rpm", 4, 1500, 4800, 2.0, 0.12, 1.6),
    ("E geared 1.6:1, 6-cyl diesel 200 hp, 3,900 rpm", 6, 1000, 3900, 1.6, 0.20, 1.6),
    ("G geared 2.0:1, 4-rotor 200 hp, 4,600 rpm (1 pulse/rotor/rev)", 8, 1500, 4600, 2.0, 0.10, 1.6),
]
MARGIN = 1.25  # keep f1 at least 25 % away from the firing band (ASSUMED rule of thumb)


def window(z, idle, red, ratio, Je, Jp):
    Jpr = Jp / ratio ** 2
    f_idle = z / 2 * idle / 60
    f_red = z / 2 * red / 60
    inv = 1 / Je + 1 / Jpr
    k_soft_max = (2 * math.pi * f_idle / MARGIN) ** 2 / inv
    k_stiff_min = (2 * math.pi * f_red * MARGIN) ** 2 / inv
    return Jpr, f_idle, f_red, k_soft_max, k_stiff_min


if __name__ == "__main__":
    print("| Case | J_prop reflected (kg m^2) | firing band (Hz) | soft: k below (N m/rad) | stiff: k above (N m/rad) |")
    print("|---|---|---|---|---|")
    for name, z, idle, red, ratio, Je, Jp in CASES:
        Jpr, fi, fr, ks, kh = window(z, idle, red, ratio, Je, Jp)
        print(f"| {name} | {Jpr:.3f} | {fi:.0f} - {fr:.0f} | {ks:,.0f} | {kh:,.0f} |")
