"""Rank the auto-gas concepts for the 200 hp member (AER-3326).

Method: a weighted-sum decision matrix (multi-attribute value scoring).
Each criterion has a raw metric with units, computed by a named script. Raw
metrics are normalized two ways, and both rankings are printed:

  ratio-to-best:  score = 10 * best / x     (lower-is-better metrics)
                  score = 10 * x / best     (higher-is-better)
  min-max:        score = 10 * (worst - x) / (worst - best)

Weights trace to Bill's rulings and brief (stated per criterion below). Rank
robustness is tested by Monte Carlo over weights: 20,000 draws from a
Dirichlet centred on the stated weights (concentration 20), and 20,000 from a
flat Dirichlet (every weighting equally likely). The share of draws in which
each concept ranks first is printed.

Run: python3 rank.py
"""
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


KN = load("knock")
M2 = load("member_200")
EF = M2.EF
TV0 = M2.load("torsional")

KEYS = ["A", "B", "C", "D", "G", "H"]

# ---- raw metrics -------------------------------------------------------
_, _, krows = KN.run()
knock_pen = {r["name"][0]: r["fuel_pen"] for r in krows}
knock_pen["G"] = 0.03   # Wankel: not in the knock model; ~+3 % from a 13B-class CR of about 9 (ASSUMED)
bsfc = {k: 310 for k in KEYS}
bsfc["G"] = 340         # phase-0 class values, engine_floor.py

mass, cost_mid, cost_lo, parts = {}, {}, {}, {}
for k in KEYS:
    if k == "H":
        m = M2.h_member(1, 200)
    else:
        m = EF.member(next(x for x in EF.CONCEPTS if x["key"] == k), 1, 200)
    mass[k] = m["dry_kg"] + m["cool_kg"][1]
    lo, hi = M2.cost_200(k)
    cost_lo[k] = lo
    cost_mid[k] = math.sqrt(lo * hi)
    parts[k] = M2.count(k)[0]

fuel = {k: bsfc[k] / 310 * (1 + knock_pen[k]) for k in KEYS}

# drive risk: direct drive has no gearbox (deletes FL-1, the documented total-
# loss-of-thrust mode) and sits on the stiff side of the torsional window.
# Geared: 3 + 3 * (soft-coupling stiffness needed / the easiest geared case),
# so the hardest-to-tune gearbox scores lowest (torsional.py, phase 0).
win = {}
for name, z, idle, red, ratio, Je, Jp in TV0.CASES:
    win[name[0]] = TV0.window(z, idle, red, ratio, Je, Jp)[3]
kmax = max(win[k] for k in ("B", "C", "G"))
drive = {k: 3 + 3 * win[k] / kmax for k in ("B", "C", "G")}
drive.update(A=10.0, D=10.0, H=9.0)   # H: -1 for the crank pendulum damper torsional_h.py may require

# made-from-files: custom precision parts with no catalog source, beyond the
# crank every concept needs. A: aviation-catalog pistons, priced [Q] (0.5).
# B, C: gear set. D: master and link rods, supercharger gear train. G: multi-
# piece eccentric shaft, trochoid housing supply, gear set. H: pendulum damper (0.5).
custom = dict(A=0.5, B=1, C=1, D=2, G=3, H=0.5)
files = {k: 10 / (1 + custom[k]) for k in KEYS}

# family fit (two modules allowed, ruling 4): family members the 200 hp
# member's module serves smoothly (no 2- or 3-cylinder member, eta_v <= 0.97).
family = dict(A=2, B=2, C=2, D=2, G=2.5, H=2)

CRIT = [
    # key, label, values, lower-is-better, weight, trace
    ("cost", "cost floor mid, $k", {k: cost_mid[k] / 1000 for k in KEYS}, True, 0.25, "Bill ruling 2: <= $22k"),
    ("parts", "parts, non-fastener", parts, True, 0.15, "brief: fewer parts"),
    ("mass", "installed dry + cooling, kg", mass, True, 0.15, "R-37 (proposed)"),
    ("drive", "drive / torsional risk, 0-10", drive, False, 0.15, "brief: propeller constraint; FL-1/FL-2"),
    ("fuel", "fuel-burn index (BSFC x knock CR cost)", fuel, True, 0.10, "rulings 1 (auto gas); R-12"),
    ("files", "made-from-files, 0-10", files, False, 0.10, "brief: made from files; envelope"),
    ("family", "family members served, of 3", family, False, 0.10, "ruling 4: two modules"),
]
W0 = np.array([c[4] for c in CRIT])


def scores(norm):
    S = np.zeros((len(KEYS), len(CRIT)))
    for j, (_, _, vals, low, _, _) in enumerate(CRIT):
        x = np.array([vals[k] for k in KEYS], float)
        if norm == "ratio":
            S[:, j] = 10 * (x.min() / x if low else x / x.max())
        else:
            best, worst = (x.min(), x.max()) if low else (x.max(), x.min())
            S[:, j] = 10 * (worst - x) / (worst - best) if worst != best else 10
    return S


def mc(S, alpha, n=20000, seed=1):
    rng = np.random.default_rng(seed)
    W = rng.dirichlet(alpha, n)
    tot = W @ S.T
    first = np.bincount(tot.argmax(1), minlength=len(KEYS)) / n
    return first


if __name__ == "__main__":
    print("## Raw metrics, 200 hp member\n")
    print("| Criterion | weight | trace | " + " | ".join(KEYS) + " |")
    print("|---|---|---|" + "---|" * len(KEYS))
    for key, label, vals, low, w, tr in CRIT:
        print(f"| {label} | {w:.2f} | {tr} | " + " | ".join(
            f"{vals[k]:.2f}" if vals[k] < 10 and not float(vals[k]).is_integer() else f"{vals[k]:.0f}" for k in KEYS) + " |")
    print("| (cost floor low end, $k, for the $22k test) | - | - | " + " | ".join(f"{cost_lo[k]/1000:.1f}" for k in KEYS) + " |")
    for norm in ("ratio", "minmax"):
        S = scores(norm)
        tot = S @ W0
        order = np.argsort(-tot)
        print(f"\n## Weighted scores, {norm} normalization\n")
        print("| Concept | " + " | ".join(c[0] for c in CRIT) + " | total | rank |")
        print("|---|" + "---|" * (len(CRIT) + 2))
        rank = {KEYS[i]: r + 1 for r, i in enumerate(order)}
        for i in order:
            print(f"| {KEYS[i]} | " + " | ".join(f"{s:.1f}" for s in S[i]) + f" | {tot[i]:.2f} | {rank[KEYS[i]]} |")
        f1 = mc(S, 20 * W0)
        f2 = mc(S, np.ones(len(CRIT)))
        print("\nShare of weight draws ranking each concept first: centred / flat Dirichlet")
        print("| " + " | ".join(KEYS) + " |")
        print("|" + "---|" * len(KEYS))
        print("| " + " | ".join(f"{a:.0%} / {b:.0%}" for a, b in zip(f1, f2)) + " |")
    # one-at-a-time: drop each criterion
    S = scores("ratio")
    print("\n## Leave-one-criterion-out (ratio normalization): winner when a criterion is removed\n")
    print("| removed | winner | runner-up |")
    print("|---|---|---|")
    for j, c in enumerate(CRIT):
        w = W0.copy()
        w[j] = 0
        w /= w.sum()
        tot = S @ w
        o = np.argsort(-tot)
        print(f"| {c[0]} | {KEYS[o[0]]} ({tot[o[0]]:.2f}) | {KEYS[o[1]]} ({tot[o[1]]:.2f}) |")
