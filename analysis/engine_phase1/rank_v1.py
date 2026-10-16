"""Rerun the phase-1 concept ranking on envelope v1 costs (AER-3329).

Same matrix, weights, normalizations and Monte Carlo as `rank.py`; only the
inputs that envelope v1 moves are replaced:

  cost   A and H from `cost_v1.py` (mid of the band), on the basis named.
         B, C, D and G were not re-estimated by MANUFACTURING; they are
         scaled by the mean v1 / phase-1 ratio of A and H (ASSUMED). Under
         ratio normalization a common scale factor changes nothing.
  mass   H + the Darton MID liner mass (cost_v1.LINER_KG_NET, mid).
  parts  H with the block merge: 2 castings and 2 gaskets fewer.

A's Lycoming pistons are priced in every case here (cost_v1.A_PISTON_PREMIUM),
except the last two blocks, which repeat the builder basis without them so the
effect of that one line is visible. The scale factor for B, C, D and G uses
A without the premium, since they carry no aviation pistons.

Run: python3 rank_v1.py
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


R = load("rank")
CV = load("cost_v1")
KEYS = R.KEYS


def run(basis, h_variant, a_pistons_priced=True):
    parts_h = CV.H_PARTS if h_variant == "sent" else CV.H_DFM_PARTS
    mid_h = CV.total(CV.cost("H", basis, parts_h)[0])[1]
    mid_a0 = CV.total(CV.cost("A", basis, CV.A_PARTS)[0])[1]
    mid_a = CV.total(CV.cost("A", basis, CV.A_PARTS, a_pistons_priced)[0])[1]
    ratio = 0.5 * (mid_h / CV.phase1("H")[1] + mid_a0 / CV.phase1("A")[1])
    crit = [list(c) for c in R.CRIT]
    vals = {c[0]: dict(c[2]) for c in crit}
    for k in KEYS:
        vals["cost"][k] = R.cost_mid[k] / 1000 * ratio
    vals["cost"]["H"] = mid_h / 1000
    vals["cost"]["A"] = mid_a / 1000
    vals["mass"]["H"] = R.mass["H"] + 0.5 * sum(CV.LINER_KG_NET)
    if h_variant == "dfm":
        vals["parts"]["H"] = R.parts["H"] - 4
    for c in crit:
        c[2] = vals[c[0]]
    saved = R.CRIT
    R.CRIT = crit
    try:
        out = {}
        for norm in ("ratio", "minmax"):
            S = R.scores(norm)
            tot = S @ R.W0
            out[norm] = (tot, R.mc(S, 20 * R.W0), R.mc(S, np.ones(len(crit))))
    finally:
        R.CRIT = saved
    return vals, ratio, out


if __name__ == "__main__":
    cases = [(b, hv, True) for b in ("builder", "first") for hv in ("sent", "dfm")]
    cases += [("builder", "sent", False), ("builder", "dfm", False)]
    for basis, hv, ap in cases:
        vals, ratio, out = run(basis, hv, ap)
        print(f"## Basis: {basis}; H {'as sent' if hv == 'sent' else 'with DFM items 1 + 4'}; "
              f"A pistons {'priced' if ap else 'at the LS price'} (B, C, D, G costs scaled x{ratio:.3f})\n")
        print("| | " + " | ".join(KEYS) + " |")
        print("|---|" + "---|" * len(KEYS))
        print("| cost mid, $k | " + " | ".join(f"{vals['cost'][k]:.1f}" for k in KEYS) + " |")
        print("| mass, kg | " + " | ".join(f"{vals['mass'][k]:.0f}" for k in KEYS) + " |")
        print("| parts | " + " | ".join(f"{vals['parts'][k]:.0f}" for k in KEYS) + " |")
        for norm, (tot, f1, f2) in out.items():
            order = np.argsort(-tot)
            print(f"| {norm} total | " + " | ".join(f"{tot[i]:.2f}" for i in range(len(KEYS))) + " |")
            print(f"| {norm} first, centred / flat | " + " | ".join(f"{a:.0%} / {b:.0%}" for a, b in zip(f1, f2)) + " |")
            print(f"\n{norm}: order " + ", ".join(f"{KEYS[i]} {tot[i]:.2f}" for i in order) + "\n")
