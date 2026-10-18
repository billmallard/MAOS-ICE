"""Concept H crankshaft: adapted catalog crank against a one-off, and the
torsional case for the chosen crank (AER-3439).

MANUFACTURING (AER-3384) asked for a decision between an adapted catalog
6-throw billet (2JZ / RB26 class) and a one-off billet, before the crank
drawing. AER-3412 added a third candidate: a Continental O-470 / IO-520
crank, a flat-6 with H's 4.000 in stroke. This script holds the physics that
decides between them, and the numbers the drawing H-301 carries.

  1. Firing: can each candidate's throw phasing fire H's opposed six evenly?
     Every cylinder's TDC is enumerated over 720 deg (the AER-3411 lesson).
  2. Fit: stroke, mains, pins, throw spacing and flange against H.
  3. Web bending at H's 111.8 mm bank pitch, against a running reference
     (the cast-iron GM LS crank) on the same statically determinate method,
     and the pitch that restores the margin.
  4. Torsion: a multi-mass chain with stiffness from the drawn geometry
     (Carter's equivalent length), forced response to the gas and inertia
     torque harmonics, and three damper options.
  5. Cost of each candidate, first engine.

Tags: [S] sourced (docs/engine/sources/CRANK_SOURCES_2026-10-18.md, the
2026-10-18 addendum), [E] PROPULSION estimate with the method here,
[A] assumed. None of these figures is a quote. Nothing has been made or run.

Run: python3 crank_decision.py > crank_decision_tables.md
"""
import itertools
import math

import numpy as np
from scipy.linalg import eigh

G = 80e9
E = 207e9

# ------------------------------------------------------------- H geometry
BORE = 104.8e-3          # LS7 liner [S envelope 9.4]
STROKE = 101.6e-3        # 4.000 in
R = STROKE / 2
ROD = 154.1e-3           # LS7 rod, 6.067 in [E, LS class]
LAM = R / ROD
D_MAIN = 60.0e-3         # envelope 9.4
D_PIN = 53.34e-3         # 2.100 in, catalog LS rods
W_PIN = 24.1e-3          # one LS rod per pin: 0.940 in big end + side clearance [E]
M_REC = 0.90             # piston, rings, pin, rod small end [A, as torsional_h.py]
M_ROT = 0.45             # rod big end [A]
RPM_RATED = 3300
RPM_IDLE = 700
P_PEAK_BAR = 70.0        # [A], as CRANK_AND_SCALING section 3.1; the cycle model below checks it
BMEP = 10.3e5            # concept H [E, phase 1]
ETA_M = 0.85             # [A]
CR = 8.4                 # knock.py

# ================================================================ 1. firing


def tdc_set(throw_angles, banks):
    """TDC crank angles (mod 360) of each cylinder. A cylinder on the
    opposite bank reaches TDC when its pin points the other way."""
    return [(a + (180 if b == "R" else 0)) % 360 for a, b in zip(throw_angles, banks)]


def even_firing_orders(tdcs):
    """All firing orders with 120 deg intervals over 720 deg. Each cylinder
    may fire at its TDC angle t or at t + 360."""
    n = len(tdcs)
    found = []
    for choice in itertools.product((0, 360), repeat=n):
        fire = sorted(((t + c) % 720, i) for i, (t, c) in enumerate(zip(tdcs, choice)))
        gaps = [(fire[(k + 1) % n][0] - fire[k][0]) % 720 for k in range(n)]
        if all(g == 720 // n for g in gaps):
            found.append(tuple(i for _, i in fire))
    return found


# H: three bays, each with an LH and an RH rod side by side (LH forward),
# so along the crank the banks run L R L R L R (H-101/H-102 STEP).
BANKS = ["L", "R", "L", "R", "L", "R"]
LAYOUTS = {
    "H boxer throws (pairs at 180, bays at 0 / 240 / 120)": [0, 180, 240, 60, 120, 300],
    "inline-6 catalog crank (2JZ, RB26: 0 / 120 / 240 / 240 / 120 / 0)": [0, 120, 240, 240, 120, 0],
    "inline-6 crank, any bank assignment": None,
}


def firing_section():
    print("## 1. Can the crank fire H evenly?\n")
    print("| Crank | TDC angles mod 360 (cyl 1-6) | Even 120-degree firing orders found |")
    print("|---|---|---|")
    for name, throws in LAYOUTS.items():
        if throws is None:
            n_ok = 0
            for banks in itertools.product("LR", repeat=6):
                if banks.count("L") != 3:
                    continue
                n_ok += bool(even_firing_orders(tdc_set([0, 120, 240, 240, 120, 0], banks)))
            print(f"| {name} | (all 20 three-and-three assignments) | {n_ok} of 20 assignments fire evenly, and none of them is L R L R L R |" if n_ok else
                  f"| {name} | (all 20 three-and-three assignments) | none |")
            continue
        t = tdc_set(throws, BANKS)
        orders = even_firing_orders(t)
        txt = (f"{len(orders)}: " + ", ".join("-".join(str(i + 1) for i in o) for o in orders)) if orders else "**none**"
        print(f"| {name} | {t} | {txt} |")
    print()


def balance(throws, banks, pitch_x):
    """Free primary and secondary forces and couples of a flat engine,
    unit reciprocating mass and radius; x along the crank. Each piston moves
    along +-z; its force is +-cos(theta_i) (primary) and +-lam cos 2theta_i."""
    th = np.radians(np.arange(0, 360, 1.0))
    out = {}
    for order in (1, 2):
        Fz = np.zeros_like(th)
        Mz = np.zeros_like(th)
        for a, b, x in zip(throws, banks, pitch_x):
            s = 1 if b == "L" else -1
            ang = th + np.radians(a) + (0 if b == "L" else np.pi)   # angle from this cylinder's TDC
            f = s * np.cos(order * ang)
            Fz += f
            Mz += f * x
        out[order] = (np.abs(Fz).max(), np.abs(Mz).max())
    return out


# ================================================================ 2. fit
CANDIDATES = [
    # name, layout, stroke mm, mains (n, dia mm), pin dia mm, throw spacing, flange, price, tag
    ("H (needed; H-301 at the 122 mm pitch)", "opposed 6, pairs 180 apart", 101.6, "4 x 60.0", 53.34, "41.4 / 80.6 mm alternating (was 38.6 / 73.2 at 111.8)", "propeller flange, SAE No. 2 class", "-", ""),
    ("Brian Crower 2JZ billet", "inline 6", "86 / 94 / 96", "7 x 62", "48 (Honda) or 52", "one per bore pitch (not found)", "flywheel", "$4,520-4,734", "[S]"),
    ("Tomei / Nitto RB26 billet", "inline 6", "73.7-77.7 class", "7 x 55 [E]", "48 [E]", "one per bore pitch", "flywheel", "$4.0k-4.9k", "[S env 9.4]"),
    ("Continental O-470 / IO-520", "opposed 6, 4 mains", 101.6, "4 x 60.3 (2.375 in)", 57.15, "Continental case (not found)", "integral propeller flange", "$8,500 used tagged; $11,924 new", "[S]"),
    ("Subaru EZ36 OE (H-EZ36, geared)", "opposed 6, 7 mains", 91.0, "7 (dia not found)", "not found", "one per bay, 98.4 mm pitch", "flywheel", "$524", "[S]"),
]

# ================================================================ 3. web bending
# Statically determinate ("split at the mains") method, the conservative
# form used for crank design checks: each bay is a simply supported beam
# between its two mains, loaded by the firing rod's gas force at its pin.
# It over-predicts absolute stress; the RATIO to a crank that runs is what
# is used here.


def web_stress(F, span, x_pin, half_main, web_t, web_w):
    """Nominal bending stress at the mid-thickness of the web next to the
    main nearest the loaded pin. Load F at x_pin from that main."""
    b = span - x_pin
    x_web = half_main + web_t / 2
    M = F * b / span * x_web
    Z = web_w * web_t ** 2 / 6
    return M / Z


def bay_layout(pitch, w_main=22e-3, w_pin=W_PIN, middle_web_extra=0.0):
    """Two separate pins and three webs between two mains."""
    webs = pitch - w_main - 2 * w_pin
    t_out = (webs - middle_web_extra) / 3
    t_mid = t_out + middle_web_extra
    x_pin1 = w_main / 2 + t_out + w_pin / 2
    return t_out, t_mid, x_pin1


def web_section():
    print("## 3. Web bending: H's bank pitch against a crank that runs\n")
    A = math.pi / 4 * BORE ** 2
    F_H = P_PEAK_BAR * 1e5 * A
    # Reference: cast-iron GM LS crank, 99 mm bore at 80 bar [A], 111.76 mm
    # pitch, two rods side by side on one 48 mm pin, 65 mm mains about 25 mm
    # wide [E]; webs (111.76 - 25 - 48) / 2.
    F_LS = 80e5 * math.pi / 4 * 0.099 ** 2
    t_ls = (111.76e-3 - 25e-3 - 48e-3) / 2
    w_web = 1.6 * D_PIN          # web width across the throw [E, both cranks]
    s_ls = web_stress(F_LS, 111.76e-3, 12.5e-3 + t_ls + 12e-3, 12.5e-3, t_ls, 1.6 * 0.0533)
    print(f"Method: each bay simply supported at its mains, one rod firing at {P_PEAK_BAR:.0f} bar [A] "
          f"({F_H/1e3:.1f} kN on 104.8 mm), nominal bending at the web next to the nearer main. "
          f"Web width {w_web*1e3:.0f} mm (1.6 x pin) [E]. Reference: a cast-iron LS crank at 80 bar [A] on the same method, "
          f"webs {t_ls*1e3:.1f} mm: **{s_ls/1e6:.0f} MPa**.\n")
    # nitrided 4340 against pearlitic ductile iron, rotating-bending fatigue at 50 % survival
    strength_ratio = 550 / 315   # CRANK_AND_SCALING section 3.3 [A]/[S]
    print(f"Fatigue strength, nitrided 4340 over pearlitic ductile iron: {strength_ratio:.2f} (CRANK_AND_SCALING 3.3). "
          "Margin ratio = (H strength / H stress) / (LS strength / LS stress); 1.0 means the same margin as a cast LS crank at full throttle in a car.\n")
    print("| Bank pitch (mm) | Outer webs (mm) | Middle web (mm) | Crank and case longer by (mm) | H web stress (MPa) | Ratio to LS | Margin ratio |")
    print("|---|---|---|---|---|---|---|")
    rows = []
    for pitch in (111.76e-3, 115e-3, 118e-3, 120e-3, 122e-3, 125e-3, 128e-3):
        t_out, t_mid, x1 = bay_layout(pitch)
        s = web_stress(F_H, pitch, x1, 11e-3, t_out, w_web)
        mr = strength_ratio * s_ls / s
        rows.append((pitch, t_out, s, mr))
        print(f"| {pitch*1e3:.1f} | {t_out*1e3:.1f} | {t_mid*1e3:.1f} | {3*(pitch-111.76e-3)*1e3:.0f} | {s/1e6:.0f} | {s/s_ls:.2f} | {mr:.2f} |")
    print()
    return rows


# ================================================================ 4. torsion
# Cycle: a single-zone pressure trace, polytropic compression and expansion
# and a Wiebe burn, scaled to the IMEP that H's BMEP needs. It is used only
# for the torque harmonics' shape; the peak pressure is checked against
# the 70 bar assumption.


def pressure_trace(rpm, imep_target, map_bar=1.0, n_poly=1.32):
    th = np.radians(np.arange(-360, 360, 0.5))       # 0 = firing TDC
    Vd = math.pi / 4 * BORE ** 2 * STROKE
    Vc = Vd / (CR - 1)
    s = R * (1 - np.cos(th)) + ROD - np.sqrt(ROD ** 2 - (R * np.sin(th)) ** 2)
    V = Vc + math.pi / 4 * BORE ** 2 * s
    th0, dth = np.radians(-18), np.radians(50)        # burn start and duration [A]; 50 % burned at about 8 deg ATDC
    xb = np.where(th > th0, 1 - np.exp(-5 * ((th - th0) / dth).clip(0, None) ** 3), 0.0)

    def run(Q):
        p = np.empty_like(th)
        p[0] = map_bar * 1e5
        g = 1.3
        for i in range(1, len(th)):
            if th[i] < -np.pi or th[i] > np.radians(180) - 1e-9:
                p[i] = map_bar * 1e5 if th[i] < -np.pi else 1.05e5     # gas exchange [A]
                continue
            dQ = Q * (xb[i] - xb[i - 1])
            dV = V[i] - V[i - 1]
            p[i] = p[i - 1] + (-g * p[i - 1] * dV + (g - 1) * dQ) / V[i]
        return p
    lo, hi = 0.0, 5000.0
    for _ in range(40):
        Q = (lo + hi) / 2
        p = run(Q)
        imep = np.trapezoid(p, V) / Vd
        lo, hi = (Q, hi) if imep < imep_target else (lo, Q)
    return th, p, V


def cylinder_torque(rpm, th, p):
    """Gas plus reciprocating inertia torque of one cylinder, N m."""
    w = rpm * 2 * math.pi / 60
    A = math.pi / 4 * BORE ** 2
    beta = np.arcsin(LAM * np.sin(th))
    lever = R * np.sin(th + beta) / np.cos(beta)
    acc = R * w ** 2 * (np.cos(th) + LAM * np.cos(2 * th))
    F = (p - 1.0e5) * A - M_REC * acc
    return F * lever


def harmonics(rpm, imep):
    th, p, V = pressure_trace(rpm, imep)
    T = cylinder_torque(rpm, th, p)
    N = len(T)
    C = np.fft.rfft(T) / N * 2
    # rfft over 720 deg: bin k is order k/2
    return {k / 2: C[k] for k in range(1, 25)}, p.max() / 1e5, T.mean()


def carter_terms(d_j, d_p, r, w):
    """Carter's equivalent length of one throw (Ker Wilson, Practical
    Solution of Torsional Vibration Problems), referred to the journal
    diameter D:  Le = D^4 [ (2b + 0.8 h)/D^4 + 0.75 a / d^4 + 1.5 r / (h w^3) ]
    with 2b the journal length, a the pin length, h the web thickness, w the
    web width and r the crank radius. Split here into per-feature
    compliances so a segment can be built from the features it contains:
    each web carries half of the 0.8 h and of the 1.5 r / (h w^3) terms."""
    return dict(
        journal=lambda l: l / d_j ** 4,
        pin=lambda l: 0.75 * l / d_p ** 4,
        web=lambda h: 0.4 * h / d_j ** 4 + 0.75 * r / (h * w ** 3),
    )


def k_from(Le_over_D4, d_j=D_MAIN):
    return G * math.pi * d_j ** 4 / 32 / (d_j ** 4 * Le_over_D4)


def chain(pitch=111.76e-3, J_prop=1.0, damper=None, stiff=1.0):
    """Masses: propeller, flange/nose, six throws, rear (cam gear and
    accessory drive), optional damper ring. Returns J, K, the throw indices
    and the segment list for stress."""
    t_out, t_mid, x1 = bay_layout(pitch)
    w_web = 1.6 * D_PIN
    jt = 0.008 + M_ROT * R ** 2 + 0.5 * M_REC * R ** 2          # as torsional_h.py [A]
    c = carter_terms(D_MAIN, D_PIN, R, w_web)
    # within a bay: half pin, the middle web (pin to pin, so two web legs), half pin
    k_in = k_from(c["pin"](W_PIN) + 2 * c["web"](t_mid)) * stiff
    # across a main: half pin, web, main journal, web, half pin
    k_across = k_from(c["pin"](W_PIN) + 2 * c["web"](t_out) + c["journal"](22e-3)) * stiff
    k_nose = G * math.pi * (0.065 ** 4 - 0.030 ** 4) / 32 / 0.15   # as torsional_h.py [A]
    J = [J_prop, 0.01, jt, jt, jt, jt, jt, jt, 0.02]
    k = [1e7, k_nose, k_in, k_across, k_in, k_across, k_in, k_across * 0.6]
    # the rear segment: half a bay plus the rear snout to the cam gear [E]
    seg = ["hub", "nose", "bay1 in", "main 2", "bay2 in", "main 3", "bay3 in", "rear main to snout"]
    if damper is not None:
        J.append(damper["J"])
        k.append(damper.get("k", 0.0))
        seg.append("damper")
    return np.array(J), np.array(k), list(range(2, 8)), seg


def assemble(J, k, c_seg, extra_c=None):
    n = len(J)
    K = np.zeros((n, n))
    C = np.zeros((n, n))
    for i, (ki, ci) in enumerate(zip(k, c_seg)):
        for M, v in ((K, ki), (C, ci)):
            M[i, i] += v
            M[i + 1, i + 1] += v
            M[i, i + 1] -= v
            M[i + 1, i] -= v
    if extra_c:
        for (a, b), ci in extra_c.items():
            C[a, a] += ci
            C[b, b] += ci
            C[a, b] -= ci
            C[b, a] -= ci
    return K, C


H_THROWS = [0, 180, 240, 60, 120, 300]
PITCH = 122.0e-3            # H-301 bank pitch, chosen in section 3
# firing order: of the 8 even orders section 1 finds for H's throws, the one
# that alternates banks (each bank fires every 240 deg): 1-6-3-2-5-4
FIRING = [o for o in even_firing_orders(tdc_set(H_THROWS, BANKS))
          if [BANKS[i] for i in o] == ["L", "R"] * 3][0]
ETA_HYST = 0.04               # crank structural loss factor [A]; magnifier 1/eta = 25
ORDERS = (1.5, 3, 4.5, 6, 7.5, 9)


def forced(rpm, H, pitch=111.76e-3, J_prop=1.0, damper=None, pendulum=None, orders=ORDERS,
           stiff=1.0, eta=ETA_HYST):
    """Steady-state response at this rpm, order by order. Returns, per
    order, the largest nominal vibratory shear in the crank segments (MPa,
    on the 60 mm journal) and the complex displacement vector."""
    w0 = rpm * 2 * math.pi / 60
    J, k, throws, seg = chain(pitch, J_prop, damper, stiff)
    c_seg = [0.0] * len(k)
    if damper is not None:
        c_seg[-1] = damper["c"]
    fire_angle = {cyl: 120 * slot for slot, cyl in enumerate(FIRING)}
    res = {}
    for q in orders:
        w = q * w0
        Jq = J.copy()
        if pendulum is not None:
            n2 = pendulum["n"] ** 2
            jeff = pendulum["m"] * pendulum["Rp"] ** 2 * n2 / (n2 - q ** 2)
            for node in pendulum["nodes"]:
                Jq[node] += jeff
        K, C = assemble(Jq, k, c_seg)
        Kc = K * (1 + 1j * eta)
        # propeller aerodynamic damping, d(torque)/d(omega) = 2 Q / omega [E]
        Kc[0, 0] += 1j * w * 2 * 432 / w0
        F = np.zeros(len(J), complex)
        for cyl, node in enumerate(throws):
            F[node] = H[q] * np.exp(-1j * math.radians(q * fire_angle[cyl]))
        x = np.linalg.solve(Kc - w ** 2 * np.diag(Jq) + 1j * w * C, F)
        T = np.array([abs(ki * (x[i] - x[i + 1])) for i, ki in enumerate(k)])
        res[q] = (T[2:8].max() * 16 / (math.pi * D_MAIN ** 3) / 1e6, x)
    return res


def modes(pitch=111.76e-3, J_prop=1.0, stiff=1.0):
    J, k, *_ = chain(pitch, J_prop, None, stiff)
    K, _ = assemble(J, k, [0] * len(k))
    w2, X = eigh(K, np.diag(J))
    return np.sqrt(np.clip(w2, 0, None))[1:4] / 2 / math.pi, X[:, 1:4]


def worst(pitch, **kw):
    """Worst RSS-of-orders journal shear from 1,000 rpm to 105 % of rated."""
    best = (0.0, 0)
    for r in range(1000, int(1.05 * RPM_RATED) + 1, 25):
        res = forced(r, harm_at(r), pitch, **kw)
        s = math.sqrt(sum(v[0] ** 2 for v in res.values()))
        if s > best[0]:
            best = (s, r)
    return best


# Yardstick for the vibratory stress: the IACS UR M68 permissible torsional
# stress for continuous running, tau_C = (UTS + 160)/18 * C_K * C_D * (3 - 2 lam^2),
# lam = rpm / rated, with lam >= 0.9 taken as 1.38 (the formula's value at
# 0.9). C_K = 0.50 for a radial (oil) hole, C_D = 0.35 + 0.93 d^-0.2 (d mm).
# It is a shaft rule used as a yardstick, not a crankshaft rule [E].
def tau_allow(uts=1000.0, d_mm=60.0, ck=0.50, lam=1.0):
    cd = 0.35 + 0.93 * d_mm ** -0.2
    f = 3 - 2 * min(lam, 0.9) ** 2
    return (uts + 160) / 18 * ck * cd * f


VISCOUS = dict(J=0.015, k=0.0, c=None)       # ring inertia [E]: catalog Fluidampr class, 0.01-0.02 kg m^2 (MANUFACTURING, AER-3443); c is not published [Q]
PEND = dict(m=0.55, Rp=0.075, n=6.1)         # one 6th-order pendulum [A]; Rp = pivot radius + pendulum length


def torsion_section(pitch):
    print(f"## 4. Torsion, H-301 at a {pitch*1e3:.1f} mm bank pitch\n")
    imep = BMEP / ETA_M
    H, pmax, Tm = harmonics(RPM_RATED, imep)
    print(f"Cycle check at {RPM_RATED:,} rpm, IMEP {imep/1e5:.1f} bar: peak pressure **{pmax:.0f} bar** "
          f"(section 3 uses {P_PEAK_BAR:.0f} bar as the design load); mean indicated torque {6*Tm:.0f} N m "
          f"(200 hp at 3,300 rpm is 432 N m brake, {432/ETA_M:.0f} indicated at eta_m {ETA_M}).\n")
    print("Torque harmonics of one cylinder at rated (N m, amplitude): " +
          ", ".join(f"order {q:g}: {abs(H[q]):.0f}" for q in ORDERS) + "\n")
    f, X = modes(pitch)
    print(f"Modes 1 / 2 / 3: **{f[0]:.0f} / {f[1]:.0f} / {f[2]:.0f} Hz**, stiffness from Carter's equivalent length on the "
          f"H-301 webs (phase 1's assumed-stiffness chain gave 261 / 768 / 1274 Hz). "
          "Mode-1 shape, propeller, nose, throws 1-6, rear: " + " ".join(f"{v/abs(X[:,0]).max():+.2f}" for v in X[:, 0]) +
          ". The propeller is a near-node; the rear end swings most.\n")
    cross = [(q, f[0] * 60 / q) for q in ORDERS if 1000 <= f[0] * 60 / q <= 1.2 * RPM_RATED]
    print("Mode-1 crossings from 1,000 rpm to 120 % of rated (3 and 6 and 9 are the major orders): " +
          "; ".join(f"order {q:g} at {r:,.0f} rpm" for q, r in cross) + "\n")

    # tune the viscous damper
    best = None
    for c in (10, 20, 30, 45, 60, 90):
        wv = worst(pitch, damper=dict(VISCOUS, c=c))
        if best is None or wv[0] < best[0][0]:
            best = (wv, c)
    vd = dict(VISCOUS, c=best[1])
    opts = [
        ("no damper", {}),
        (f"viscous damper on the rear snout (ring {VISCOUS['J']} kg m^2 [A], c {best[1]} N m s/rad, swept)", dict(damper=vd)),
        ("two 6th-order pendulums on bay 3 (rear) [A]", dict(pendulum=dict(PEND, nodes=[6, 7]))),
        ("two 6th-order pendulums on bay 1 (propeller end)", dict(pendulum=dict(PEND, nodes=[2, 3]))),
    ]
    rpms = [1200, 1600, 2000, 2300, 2600, 2900, 3100, 3300, 3465]
    ta = tau_allow()
    print(f"Forced response: RSS over orders {', '.join(f'{q:g}' for q in ORDERS)} of the nominal vibratory shear in the "
          f"60 mm journal, worst crank segment, MPa single amplitude. Structural loss factor {ETA_HYST} [A]; "
          f"propeller fixed pitch, 1.0 kg m^2 [A]; full throttle on the propeller curve. "
          f"Yardstick: IACS M68 continuous limit with an oil-hole factor, **{ta:.0f} MPa** at and near rated [E, a shaft rule].\n")
    print("| Option | " + " | ".join(f"{r:,}" for r in rpms) + " | worst, 1,000-3,465 rpm |")
    print("|---|" + "---|" * (len(rpms) + 1))
    out = {}
    for name, kw in opts:
        row = []
        for r in rpms:
            res = forced(r, harm_at(r), pitch, **kw)
            row.append(f"{math.sqrt(sum(v[0] ** 2 for v in res.values())):.1f}")
        w = worst(pitch, **kw)
        out[name] = w
        print(f"| {name} | " + " | ".join(row) + f" | **{w[0]:.1f} at {w[1]:,}** |")
    print()

    print("Sensitivity of the worst case (MPa at rpm), no damper against the viscous damper:\n")
    print("| Case | Mode 1 (Hz) | No damper | Viscous damper |")
    print("|---|---|---|---|")
    cases = [("baseline", {}), ("crank stiffness x0.8", dict(stiff=0.8)), ("crank stiffness x1.2", dict(stiff=1.2)),
             ("loss factor 0.02", dict(eta=0.02)), ("propeller 0.6 kg m^2", dict(J_prop=0.6)),
             ("propeller 2.5 kg m^2", dict(J_prop=2.5))]
    for name, kw in cases:
        fm = modes(pitch, kw.get("J_prop", 1.0), kw.get("stiff", 1.0))[0][0]
        a = worst(pitch, **kw)
        b = worst(pitch, damper=vd, **kw)
        print(f"| {name} | {fm:.0f} | {a[0]:.1f} at {a[1]:,} | {b[0]:.1f} at {b[1]:,} |")
    print()

    # pendulum swing at the 6th-order crossing, and the pendulum's geometry
    n2 = PEND["n"] ** 2
    rr = PEND["Rp"] / (1 + n2)
    q = 6
    r6 = int(f[0] * 60 / 6)
    res = forced(r6, harm_at(r6), pitch, pendulum=dict(PEND, nodes=[6, 7]), orders=(6,))
    x = res[6][1]
    phi = PEND["Rp"] / rr * q ** 2 / (n2 - q ** 2) * abs(x[6])
    print(f"Pendulum check: tuned to order {PEND['n']}, pivot radius {(PEND['Rp']-rr)*1e3:.1f} mm, effective length "
          f"**{rr*1e3:.1f} mm** (Continental IO-520: 6th-order pin 0.5549-0.5574 in in a 0.622-0.626 in bushing bore, "
          f"which gives a length of about 1.7-1.8 mm [S]). Swing at the 6th-order crossing ({r6:,} rpm): {math.degrees(phi):.1f} deg.\n")
    return out, f, vd


_HCACHE = {}


def harm_at(rpm):
    """Harmonics at full throttle on the fixed-pitch propeller curve: power
    goes as rpm^3, so IMEP as rpm^2, with the inertia torque at this rpm."""
    key = int(rpm)
    if key not in _HCACHE:
        imep = BMEP / ETA_M * min(1.0, (rpm / RPM_RATED) ** 2)
        imep = max(imep, 3e5)
        _HCACHE[key] = harmonics(rpm, imep)[0]
    return _HCACHE[key]


# ================================================================ 5. cost


def cost_section():
    print("## 5. First-engine cost of each candidate (basis 1, none quoted)\n")
    print("| Candidate | Crank | What else it costs H | Lead | Verdict |")
    print("|---|---|---|---|---|")
    rows = [
        ("Catalog inline-6 billet (2JZ / RB26)", "$4.0k-4.9k [S]", "cannot fire a flat six evenly (section 1), wrong stroke and throw spacing: a different engine (an inline-6 block and one long head), not an adaptation", "stock to weeks", "**does not fit H**"),
        ("One-off billet to H-301, crank specialist", "$6.6k-9.4k incl. balance [E, envelope 9.4]", "H-101/H-102/H-201 at the 122 mm pitch (section 3), and a deck rise for a longer rod or relieved liner bottoms (section 6)", "18-20 weeks [S, reseller]", "**recommended**"),
        ("One-off to H-301, general turn-mill shop (route 5)", "$7k-19k, central $10-12k [E, AER-3412]", "as above; the builder owns the crank process (nitride, grind, straightening)", "6-12 weeks [E]", "lead-time alternate, same drawing"),
        ("Continental O-470 / IO-520, VAR, used", "$8.2k-10.5k ready to install [S]; $1.5k-3k as a core plus overhaul [E, AER-3443], if the core passes; $11.9k new [S]", "case redrawn to Continental's main spacing (not found); 2.250 in pins, so no LS rods; damper pins at 3,300 rpm carry 1.34x the centrifugal load of 2,850", "stock, used market", "cheaper only as core + overhaul; open until a core is measured"),
        ("Subaru EZ36 OE, geared (H-EZ36)", "$0.9k-1.2k on the line [S + E]", "a gearbox $2.9k-9.8k [E], a 92 mm cylinder module, 7 mains", "days", "Bill's open card on AER-3411; not H as drawn"),
    ]
    for r in rows:
        print("| " + " | ".join(r) + " |")
    print()


if __name__ == "__main__":
    print("# crank_decision.py tables (AER-3439)\n")
    print("Generated by `python3 crank_decision.py`. Tags as in the script header. None of these figures is a quote.\n")
    firing_section()
    t = [0, 180, 240, 60, 120, 300]
    for pitch in (111.76, 122.0):
        xs = []
        for bay in range(3):
            t_out, _, x1 = bay_layout(pitch * 1e-3)
            xs += [bay * pitch + x1 * 1e3, bay * pitch + x1 * 1e3 + (W_PIN + t_out) * 1e3]
        b = balance(t, BANKS, np.array(xs) * 1e-3)
        print(f"Balance of H's boxer throws at a {pitch:.1f} mm pitch (unit mass and crank radius): primary force {b[1][0]:.1e}, "
              f"primary couple {b[1][1]:.1e} m; secondary force {b[2][0]:.1e}, secondary couple {b[2][1]:.1e} m.\n")
    print("## 2. Fit against H\n")
    print("| Candidate | Layout | Stroke (mm) | Mains | Pin (mm) | Throw spacing | Front end | Price | Tag |")
    print("|---|---|---|---|---|---|---|---|---|")
    for c in CANDIDATES:
        print("| " + " | ".join(str(v) for v in c) + " |")
    print()
    rows = web_section()
    f0 = modes(111.76e-3)[0]
    print(f"At the drawn 111.8 mm pitch, for comparison: modes {f0[0]:.0f} / {f0[1]:.0f} / {f0[2]:.0f} Hz.\n")
    summary, f, vd = torsion_section(PITCH)
    cost_section()


# ================================================================ 6. clearance
# Item 4 of rfq-package-v1: the counterweight envelope against the liner and
# the piston skirt. H-301's geometry comes from cad/concept_h/h301_params.json,
# the same file the STEP is built from. The pistons are modelled as full
# discs of the bore, with the skirt ending skirt_below_pin under the gudgeon
# pin [A]: a conservative stand-in until a catalog piston drawing is in hand.
import json as _json
import os as _os

GEOM = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                                     "..", "..", "cad", "concept_h", "h301_params.json")))


def crank_features(g):
    """Sample points of every web and counterweight in the crank frame at
    crank angle 0, with the pin direction of each point's throw. Each item:
    (name, x array, local polar points (r, ang) relative to that pin's angle)."""
    R_ = g["stroke"] / 2
    feats = []
    for bay in range(3):
        m0 = g["x_main0"] + bay * g["pitch"]
        hw = g["main_w"] / 2
        xa = m0 + hw                                   # web A front face
        xs = [xa, xa + g["web_t"]]
        xp1 = xa + g["web_t"] + g["pin_w"] / 2
        xm = xp1 + g["pin_w"] / 2
        xs_mid = [xm, xm + g["web_t"]]
        xp2 = xm + g["web_t"] + g["pin_w"] / 2
        xb = xp2 + g["pin_w"] / 2
        xs_b = [xb, xb + g["web_t"]]
        i1, i2 = 2 * bay, 2 * bay + 1
        feats.append(("web A", xs, i1, "main-pin"))
        feats.append(("middle web", xs_mid, i1, "pin-pin"))
        feats.append(("web B", xs_b, i2, "main-pin"))
        feats.append(("counterweight A", xs, i1, "cw"))
        feats.append(("counterweight B", xs_b, i2, "cw"))
        feats.append(("pin", [xp1 - g["pin_w"] / 2, xp1 + g["pin_w"] / 2], i1, "pin"))
        feats.append(("pin", [xp2 - g["pin_w"] / 2, xp2 + g["pin_w"] / 2], i2, "pin"))
        feats.append(("opposed rod big end", [xp1 - g["pin_w"] / 2, xp1 + g["pin_w"] / 2], i1, "bigend"))
        feats.append(("opposed rod big end", [xp2 - g["pin_w"] / 2, xp2 + g["pin_w"] / 2], i2, "bigend"))
    return feats


def outline(kind, g):
    """2-D outline points (y, z) of a feature with its own pin along +z."""
    R_ = g["stroke"] / 2
    a = np.radians(np.arange(0, 360, 3))
    if kind == "main-pin":
        pts = np.r_[np.c_[g["web_main_r"] * np.sin(a), g["web_main_r"] * np.cos(a)],
                    np.c_[g["web_pin_r"] * np.sin(a), R_ + g["web_pin_r"] * np.cos(a)]]
    elif kind == "pin-pin":
        pts = np.r_[np.c_[g["web_pin_r"] * np.sin(a), R_ + g["web_pin_r"] * np.cos(a)],
                    np.c_[g["web_pin_r"] * np.sin(a), -R_ + g["web_pin_r"] * np.cos(a)]]
    elif kind == "cw":
        b = np.radians(np.linspace(-g["cw_half_angle"], g["cw_half_angle"], 23)) + np.pi
        pts = np.c_[g["cw_r"] * np.sin(b), g["cw_r"] * np.cos(b)]
    elif kind == "bigend":   # rod big end and cap bolts, a circle about the pin [A]
        pts = np.c_[g["bigend_r"] * np.sin(a), R_ + g["bigend_r"] * np.cos(a)]
    else:   # pin
        pts = np.c_[g["pin_d"] / 2 * np.sin(a), R_ + g["pin_d"] / 2 * np.cos(a)]
    return pts


def piston_hit(dx, y, along, skirt_bottom, g, model):
    """Gap (mm, along the bank axis) between crank points and one piston.
    'disc': the full bore down to the skirt bottom (conservative).
    'relieved' [A]: skirt panels only on the thrust sides (|dx| <= panel
    half-chord, |y| >= panel_y) down to the skirt bottom; the pin bosses
    (|dx| <= boss half-length, |y| <= boss half-width) down to the gudgeon
    pin less boss_below_pin; nothing else below the ring belt."""
    pin = skirt_bottom + g["skirt_below_pin"]
    rad = np.hypot(dx, y)
    gaps = []
    if model == "disc":
        m = rad <= g["piston_r"]
        if m.any():
            gaps.append((skirt_bottom - along[m]).min())
    else:
        m = (np.abs(dx) <= g["panel_half_chord"]) & (np.abs(y) >= g["panel_y"]) & (rad <= g["piston_r"])
        if m.any():
            gaps.append((skirt_bottom - along[m]).min())
        m = (np.abs(dx) <= g["boss_half_len"]) & (np.abs(y) <= g["boss_half_w"])
        if m.any():
            gaps.append((pin - g["boss_below_pin"] - along[m]).min())
        m = rad <= g["piston_r"]
        if m.any():
            gaps.append((pin - g["belt_below_pin"] - along[m]).min())
    return min(gaps) if gaps else None


def clearance(g, step=2, model="disc"):
    R_ = g["stroke"] / 2
    L = g["rod_length"]
    feats = crank_features(g)
    cyl_x = []
    for bay in range(3):
        m0 = g["x_main0"] + bay * g["pitch"]
        x1 = m0 + g["main_w"] / 2 + g["web_t"] + g["pin_w"] / 2
        cyl_x += [x1, x1 + g["pin_w"] + g["web_t"]]
    worst = {}
    for th in np.arange(0, 720, step):
        # piston skirt bottoms, along each bank axis
        skirt = []
        for j, (a, b) in enumerate(zip(g["throws_against_rotation"], g["banks"])):
            pin_dir = math.radians(th - a)
            phi = pin_dir - (0 if b == "L" else math.pi)
            s = R_ * math.cos(phi) + math.sqrt(L ** 2 - (R_ * math.sin(phi)) ** 2)
            skirt.append(s - g["skirt_below_pin"])
        for name, xs, ithrow, kind in feats:
            ang = math.radians(th - g["throws_against_rotation"][ithrow])
            pts = outline(kind, g)
            y = pts[:, 0] * math.cos(ang) + pts[:, 1] * math.sin(ang)
            z = -pts[:, 0] * math.sin(ang) + pts[:, 1] * math.cos(ang)
            for x in np.linspace(xs[0], xs[1], 4):
                for j, b in enumerate(g["banks"]):
                    if kind in ("pin", "bigend") and j == ithrow:
                        continue                       # a pin and its rod live under their own piston
                    along = z if b == "L" else -z
                    rad = np.hypot(x - cyl_x[j], y)
                    gap = piston_hit(x - cyl_x[j], y, along, skirt[j], g, model)
                    if gap is not None:
                        key = (name, "piston")
                        if key not in worst or gap < worst[key][0]:
                            worst[key] = (gap, th, j + 1)
                    wall = (rad > g["piston_r"]) & (rad <= g["liner_wall_od_bottom"] / 2)
                    if wall.any():
                        gap = (g["liner_bottom_from_axis"] - along[wall]).min()
                        key = (name, "liner bottom")
                        if key not in worst or gap < worst[key][0]:
                            worst[key] = (gap, th, j + 1)
    return worst


def clearance_section():
    g = GEOM
    print("## 6. Web, counterweight and opposed-rod envelope against the liner and the pistons (rfq item 4)\n")
    print(f"Swept every 2 deg over 720 deg. Liner bottom {g['liner_bottom_from_axis']} mm from the crank axis "
          f"(Darton MID, 147.3 mm long [S, rfq-package-v1]); rod {g['rod_length']} mm [E]; big end and cap bolts "
          f"a {g['bigend_r']} mm radius about the pin [A]. Webs {2*g['web_pin_r']:.0f} mm wide, round-ended; counterweights "
          f"{g['cw_r']} mm radius over +/-{g['cw_half_angle']} deg on the outer webs. Two piston models: **disc**, the full "
          f"bore down to {g['skirt_below_pin']} mm below the gudgeon pin [A]; **relieved** [A], skirt panels only on the thrust "
          f"sides (+/-{g['panel_half_chord']} mm of chord, beyond |y| {g['panel_y']} mm), pin bosses +/-{g['boss_half_len']} x "
          f"+/-{g['boss_half_w']} mm down to {g['boss_below_pin']} mm below the pin, ring belt {g['belt_below_pin']} mm below "
          "the pin. Negative = interference.\n")
    res = {m: clearance(g, model=m) for m in ("disc", "relieved")}
    keys = sorted(res["disc"], key=lambda k: res["disc"][k][0])
    print("| Feature | Against | Disc: gap (mm), crank angle, cylinder | Relieved: gap (mm), crank angle, cylinder |")
    print("|---|---|---|---|")
    for k in keys:
        a = res["disc"][k]
        b = res["relieved"].get(k)
        bt = f"{b[0]:.1f}, {b[1]:.0f}, {b[2]}" if b else "-"
        print(f"| {k[0]} | {k[1]} | {a[0]:.1f}, {a[1]:.0f}, {a[2]} | {bt} |")
    print()
    for m in ("disc", "relieved"):
        lo, hi = 40.0, 95.0
        for _ in range(16):
            mid = (lo + hi) / 2
            ww = clearance(dict(g, cw_r=mid), step=4, model=m)
            mm = min(v[0] for k, v in ww.items() if k[0].startswith("counterweight"))
            lo, hi = (mid, hi) if mm >= 3.0 else (lo, mid)
        print(f"Largest counterweight radius with 3 mm to every piston and liner, {m} model: **{lo:.1f} mm**.\n")
    print("What clears the opposed rod and the middle web: a longer catalog rod raises the deck, the BDC piston and the "
          "liner bottom by the same amount (relieved model, every 4 deg, counterweights excluded):\n")
    print("| Rod (in) | Deck rise (mm) | Worst piston gap (mm) | Worst liner gap (mm) | Catalog 2.100 in journal, 0.927 in pin |")
    print("|---|---|---|---|---|")
    cat = {6.067: "LS7 [E]", 6.125: "BTR, Scat class [S]", 6.200: "Eagle ESP [S]", 6.360: "Speedmaster [S, snippet]",
           6.460: "not found", 6.618: "not found"}
    for rod_in, note in cat.items():
        dl = rod_in * 25.4 - g["rod_length"]
        gg = dict(g, rod_length=g["rod_length"] + dl, liner_bottom_from_axis=g["liner_bottom_from_axis"] + dl)
        w = clearance(gg, step=4, model="relieved")
        pis = min(v[0] for k, v in w.items() if k[1] == "piston" and not k[0].startswith("counter"))
        lin = min(v[0] for k, v in w.items() if k[1] == "liner bottom" and not k[0].startswith("counter"))
        print(f"| {rod_in:.3f} | {dl:.1f} | {pis:.1f} | {lin:.1f} | {note} |")
    print()
    return res


if __name__ == "__main__":
    clearance_section()
    print("## 7. Paired rotating and reciprocating mass for the balance note\n")
    print("The opposed pair in each bay runs on pins 180 deg apart, so each pair's rotating and reciprocating forces "
          "cancel as forces and leave a couple on the bank offset; the three bays' couples sum to zero (section 1). "
          "The crank is therefore balanced alone, with no bob weight, provided rods are matched end for end and "
          "pistons by weight across each opposed pair.\n")
