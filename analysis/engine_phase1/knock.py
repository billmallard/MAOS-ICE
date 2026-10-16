"""Knock-limited compression ratio per concept on pump gas (AER-3326).

A comparative knock proxy, not a combustion model. It asks: at the same fuel,
charge state and BMEP class, how much longer does the end gas of one cylinder
geometry sit hot before the flame reaches it, against how fast it auto-ignites?

  Knock index   K = t_burn / tau_endgas            (Livengood-Wu, one-step form)
  End-gas delay tau = 17.68 ms (ON/100)^3.402 p^-1.7 exp(3800/T)
                (Douaud & Eyzat 1978; p in atm, T in K; Heywood ch. 9)
  End-gas state p = p_im CR^n Phi,   T = T_im CR^(n-1) Phi^((n-1)/n)
                n = 1.30 polytropic; Phi = 2.5 is the pressure rise from the
                burned charge compressing the end gas, the same for every case
                (ASSUMED: all cases run 10-11 bar BMEP, so the peak-pressure
                ratio is of one class)
  Burn time     t_burn = L / S_T, L = 0.5 B (two plugs per cylinder, R-25),
                S_T = S_L + u', u' = Sp (turbulent flame speed tracks mean
                piston speed; Heywood ch. 9-10 give u' ~ 0.5 Sp and S_T ~ 2 u'
                in this regime). S_L = 0.5 m/s.

Calibration: five engines that run, each at its rated fuel. The four air-cooled
anchors set the conservative threshold K*_air (their median); their spread is
printed as the model's scatter. The Rotax 912 ULS, the only anchor with liquid-
cooled heads, sets K*_liq: the credit a liquid-cooled head and a modern chamber
might buy. Neither is a measurement on this engine.
Avgas grades are read as their lean (motor-method) rating; that is an
approximation. Air-cooled anchors run hotter walls and charge than a liquid-
cooled head would; the model does not credit liquid cooling, so it is
conservative for this engine.

Output: the compression ratio at which each concept reaches K* on MON 85
(91 AKI, REQUIREMENTS R-12) and MON 82 (about 87 AKI, R-13), and the ideal
Otto-cycle fuel-burn cost of that ratio against 10:1.

Run: python3 knock.py
"""
import math

N_POLY = 1.30
PHI = 2.5
S_L = 0.5
P_IM_ATM = 1.0
T_IM_K = 330.0   # charge at IVC after wall heating, ASSUMED; same for every case

# name, bore mm, stroke mm, rated rpm, CR, fuel octane (MON or avgas lean), source
ANCHORS = [
    ("Rotax 912 ULS (liquid heads)", 84.0, 61.0, 5800, 10.8, 85, "CR: Rotax 912 datasheet / Wikipedia; MON 85: [R1][R3]"),
    ("UL Power UL520iS (air)", 105.6, 100.0, 3300, 8.7, 88, "ulpower.com UL520iS page, read 2026-10-16"),
    ("Lycoming O-320-E2D (air)", 130.2, 98.4, 2700, 7.0, 80, "80/87 avgas, CR 7.00 (Wikipedia O-320; TCDS not read)"),
    ("Lycoming O-360-A1A (air)", 130.2, 111.1, 2700, 8.5, 91, "91/96 avgas, CR 8.50 (Wikipedia O-360 variants; TCDS not read)"),
    ("Lycoming IO-360-A (air)", 130.2, 111.1, 2700, 8.7, 99.6, "100/100LL avgas, CR 8.70 (same source)"),
]

CONCEPTS = [
    ("A flat-4 direct, Lycoming 540 module", 130.2, 111.1, 2750),
    ("B flat-8 geared, 86 mm module", 86.0, 64.0, 5800),
    ("C V4 geared, LS7 module", 104.8, 101.6, 4700),
    ("D radial-7 direct, 4.5 in module", 114.3, 106.0, 2400),
    ("H flat-6 direct, LS7 module (phase-1 variant)", 104.8, 101.6, 3300),
]


def tau_ms(on, cr):
    p = P_IM_ATM * cr ** N_POLY * PHI
    T = T_IM_K * cr ** (N_POLY - 1) * PHI ** ((N_POLY - 1) / N_POLY)
    return 17.68 * (on / 100) ** 3.402 * p ** -1.7 * math.exp(3800 / T)


def t_burn_ms(bore, stroke, rpm):
    sp = 2 * stroke / 1000 * rpm / 60
    return 0.5 * bore / 1000 / (S_L + sp) * 1000, sp


def K(bore, stroke, rpm, cr, on):
    return t_burn_ms(bore, stroke, rpm)[0] / tau_ms(on, cr)


def cr_limit(bore, stroke, rpm, on, kstar):
    lo, hi = 5.0, 14.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if K(bore, stroke, rpm, mid, on) > kstar:
            hi = mid
        else:
            lo = mid
    return lo


def otto(cr, g=1.30):
    return 1 - cr ** (1 - g)


def run():
    ks = [K(b, s, n, cr, on) for _, b, s, n, cr, on, _ in ANCHORS]
    air = sorted(ks[1:])
    kstar = 0.5 * (air[1] + air[2])
    kliq = ks[0]
    rows = []
    for name, b, s, n in CONCEPTS:
        tb, sp = t_burn_ms(b, s, n)
        cr85 = cr_limit(b, s, n, 85, kstar)
        cr82 = cr_limit(b, s, n, 82, kstar)
        # band from the anchor spread
        cr85_lo = cr_limit(b, s, n, 85, min(ks[1:]))
        cr85_hi = cr_limit(b, s, n, 85, kliq)
        burn = otto(10.0) / otto(cr85) - 1
        rows.append(dict(name=name, tb=tb, sp=sp, cr85=cr85, cr85_lo=cr85_lo, cr85_hi=cr85_hi,
                         cr82=cr82, fuel_pen=burn))
    return ks, kstar, rows


if __name__ == "__main__":
    ks, kstar, rows = run()
    print("Anchors (each at its rated fuel):\n")
    print("| Engine | bore x stroke (mm) | rpm | CR | octane | t_burn (ms) | K | source |")
    print("|---|---|---|---|---|---|---|---|")
    for (nm, b, s, n, cr, on, src), k in zip(ANCHORS, ks):
        print(f"| {nm} | {b:.1f} x {s:.1f} | {n} | {cr} | {on} | {t_burn_ms(b, s, n)[0]:.2f} | {k:.3f} | {src} |")
    print(f"\nK*_air (median of the four air-cooled anchors) = {kstar:.3f}; their spread {min(ks[1:]):.3f}-{max(ks[1:]):.3f} "
          f"({100*(max(ks[1:])/min(ks[1:])-1):.0f} %). K*_liq (Rotax 912 ULS) = {ks[0]:.3f}, {ks[0]/kstar:.2f}x K*_air.\n")
    print("| Concept (200 hp) | Sp (m/s) | t_burn (ms) | knock-limited CR on MON 85 at K*_air (air-cooled worst anchor to liquid-cooled credit) | CR on MON 82 at K*_air | ideal Otto fuel-burn cost vs CR 10, at K*_air |")
    print("|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['name']} | {r['sp']:.1f} | {r['tb']:.2f} | {r['cr85']:.1f} ({r['cr85_hi']:.1f}-{r['cr85_lo']:.1f}) | "
              f"{r['cr82']:.1f} | +{100*r['fuel_pen']:.1f} % |")
