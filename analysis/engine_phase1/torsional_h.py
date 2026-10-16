"""Multi-mass torsional model, direct-drive crank and propeller (AER-3326).

Phase 0 used a two-inertia window. Here the crank is a lumped chain:
  propeller - flange/nose - throw 1 ... throw z - rear (accessory/starter gear)
with stiffness per segment from G J / L_eq. Natural frequencies and mode
shapes come from the generalized eigenproblem K x = w^2 J x (Den Hartog;
Ker Wilson for the equivalent-length idea). A Campbell check then lists every
4-stroke order (0.5 to 9) that crosses a mode between idle and 105 % of
redline, and flags the major orders (multiples of z/2 for an evenly fired
engine), whose excitation adds in phase at every throw.

Every inertia and stiffness is ASSUMED from catalog-class dimensions until
parts exist. The point is where the modes sit and what they are sensitive to,
not a stress. A dynamometer torsional survey is the final check.

Run: python3 torsional_h.py
"""
import math

import numpy as np
from scipy.linalg import eigh

G = 80e9


def k_shaft(d_out, d_in, L):
    return G * math.pi * (d_out ** 4 - d_in ** 4) / 32 / L


def j_throw(stroke_m, m_rec, m_rot, j_crank):
    r = stroke_m / 2
    return j_crank + m_rot * r * r + 0.5 * m_rec * r * r


CASES = {
    # z, idle, redline, stroke, journal d, L_eq per throw, nose L, crank J per throw, J_rear
    "H flat-6, LS7 module, 3,300 rpm": dict(z=6, idle=700, red=3300, stroke=0.1016, dj=0.060, Leq=0.14,
                                            Ln=0.15, jc=0.008, jr=0.02, m_rec=0.9, m_rot=0.45),
    "A flat-4, Lycoming 540 module, 2,750 rpm": dict(z=4, idle=700, red=2750, stroke=0.1111, dj=0.060, Leq=0.16,
                                                     Ln=0.15, jc=0.012, jr=0.02, m_rec=1.3, m_rot=0.6),
}
J_PROPS = (0.6, 1.0, 1.5, 2.5)   # kg m^2: light composite fixed pitch to metal constant speed, ASSUMED


def model(c, Jp):
    z = c["z"]
    jt = j_throw(c["stroke"], c["m_rec"], c["m_rot"], c["jc"])
    J = [Jp, 0.01] + [jt] * z + [c["jr"]]
    kt = k_shaft(c["dj"], 0.0, c["Leq"])
    kn = k_shaft(0.065, 0.030, c["Ln"])
    k = [1e7, kn] + [kt] * (z - 1) + [kt]       # prop hub-to-flange very stiff
    n = len(J)
    K = np.zeros((n, n))
    for i, ki in enumerate(k):
        K[i, i] += ki
        K[i + 1, i + 1] += ki
        K[i, i + 1] -= ki
        K[i + 1, i] -= ki
    w2, X = eigh(K, np.diag(J))
    f = np.sqrt(np.clip(w2, 0, None)) / (2 * math.pi)
    return f[1:4], X[:, 1:4], jt, kt, kn


def campbell(c, f_modes, X):
    z = c["z"]
    out = []
    for m, (f, x) in enumerate(zip(f_modes, X.T)):
        throws = x[2:2 + z]
        rel = abs(throws.sum()) / (abs(x).max() * z)   # in-phase (major order) participation
        for o2 in range(1, 19):
            o = o2 / 2
            rpm = f * 60 / o
            if c["idle"] <= rpm <= 1.05 * c["red"]:
                major = abs(o / (z / 2) - round(o / (z / 2))) < 1e-9
                out.append((m + 1, f, o, rpm, major, rel))
    return out


if __name__ == "__main__":
    for name, c in CASES.items():
        print(f"\n## {name}\n")
        print("| J_prop (kg m^2) | mode 1 / 2 / 3 (Hz) | major-order crossings in idle-105 % redline | redline major-order frequency | mode-1 margin above the top major order at redline |")
        print("|---|---|---|---|---|")
        for Jp in J_PROPS:
            f, X, jt, kt, kn = model(c, Jp)
            cr = campbell(c, f, X)
            majors = [f"mode {m} x order {o:g} at {rpm:,.0f} rpm" for m, ff, o, rpm, mj, rel in cr if mj]
            top = c["z"] / 2 * c["red"] / 60
            ords = [c["z"] / 2 * i for i in (1, 2, 3)]
            # margin: mode 1 against the major orders' frequency at redline
            margins = [f[0] / (o * c["red"] / 60) for o in ords]
            print(f"| {Jp} | {f[0]:.0f} / {f[1]:.0f} / {f[2]:.0f} | {'; '.join(majors) if majors else 'none'} | "
                  + ", ".join(f"{o:g}: {o*c['red']/60:.0f} Hz" for o in ords)
                  + " | " + ", ".join(f"{o:g}: {mg:.2f}" for o, mg in zip(ords, margins)) + " |")
        print(f"\nThrow inertia {jt:.4f} kg m^2, throw stiffness {kt:,.0f} N m/rad, nose {kn:,.0f} N m/rad (ASSUMED).")
        # sensitivity: crank stiffness +/-30 %
        for s in (0.7, 1.3):
            c2 = dict(c, Leq=c["Leq"] / s)
            f, X, *_ = model(c2, 1.0)
            print(f"Throw stiffness x{s}: J_prop 1.0 modes {f[0]:.0f} / {f[1]:.0f} / {f[2]:.0f} Hz")
