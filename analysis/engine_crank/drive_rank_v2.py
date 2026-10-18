"""The phase-1 drive ranking, rerun with the gearbox scored as a proven-class part (AER-3411).

drive_rank.py (AER-3326) scored every geared option 1 of 10 on risk ("total
loss of thrust", FL-1), at weight 0.25. Bill's direction 2 (2026-10-17,
exploration, not a ruling): a highly reliable gearbox is an acceptable risk,
as Rotax shows, and it protects the engine in a propeller strike. This
reruns the same matrix, same performance cells, same weights and the same
Monte Carlo, changing only the geared options' risk score and, as a second
step, their cost and mass to the first-engine gearbox band of this issue.

Risk scores tried for options 2 and 7 (the reduction drive):
  1   phase 1: total loss of thrust, as a near-disqualifier
  7   proven class: the total-loss path exists but at a rate assumed of the
      order of the crankshaft's, which every option already carries; credit
      for the overload clutch that protects the crank in a propeller strike
  10  the gearbox counted as part of the engine, like the crank
The cost and mass change: gearbox $2.9k-9.8k first engine (mid $5.3k) and
11-20 kg (mid 15 kg) [E] (CRANK_AND_SCALING.md section 5), plus the phase-1
propeller figure.

Run: python3 drive_rank_v2.py   (reruns drive_match.py, about 20 s)
"""
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("drive_rank", os.path.join(HERE, "..", "engine_phase1", "drive_rank.py"))
DR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DR)

GEARED = ("2 ", "7 ")
PROP_FP, PROP_CS = 4000, 14800
GB_MID = math.sqrt(2900 * 9800)
GB_KG = 15.0


def matrix(out, names, risk_geared, first_engine_gearbox):
    raw = []
    for n in names:
        rows = {r["V"]: r for r in out[n]["rows"]}
        cost, mass, risk, _ = DR.lookup(n)
        if n.startswith(GEARED):
            risk = risk_geared
            if first_engine_gearbox:
                cost = (PROP_FP if n.startswith("2 ") else PROP_CS) + GB_MID
                mass = (7.0 if n.startswith("2 ") else 20.0) + GB_KG
        raw.append([max(rows[80]["thp_frac"], 0), max(rows[165]["thp_frac"], 0), rows[0]["T"] / 1000, cost, mass, risk])
    X = np.array([[np.nan if v is None else v for v in r] for r in raw], float)
    for j in (3, 4):
        col = X[:, j]
        col[np.isnan(col)] = np.nanmax(col)
    S = np.zeros_like(X)
    for j in range(X.shape[1]):
        x = X[:, j]
        if j == 3:
            S[:, j] = np.clip(10 * (1 - x / 22000), 0, 10)
        elif j == 4:
            S[:, j] = np.clip(10 * (1 - x / 150), 0, 10)
        else:
            S[:, j] = 10 * x / x.max()
    return S


if __name__ == "__main__":
    out = DR.DM.main()
    names = list(out)
    unverified = [i for i, n in enumerate(names) if n.startswith(("8b", "4a", "5 "))]
    keep = [i for i in range(len(names)) if i not in unverified]
    short = lambda n: n.split(" ")[0] + ("(3,300)" if "held" in n else "") + ("(sched)" if "schedule" in n else "")
    print("| Gearbox risk score | gearbox cost and mass | rank of 2 (reduction, fixed pitch) / of 7 (CS + reduction) among the 7 verified options | order, verified options | first-place share, centred Dirichlet |")
    print("|---|---|---|---|---|")
    for risk in (1, 7, 10):
        for fe in (False, True):
            S = matrix(out, names, risk, fe)[keep]
            tot = S @ DR.W
            o = np.argsort(-tot)
            nk = [names[keep[i]] for i in o]
            r2 = 1 + next(i for i, n in enumerate(nk) if n.startswith("2 "))
            r7 = 1 + next(i for i, n in enumerate(nk) if n.startswith("7 "))
            rng = np.random.default_rng(1)
            Wd = rng.dirichlet(20 * DR.W, 20000)
            first = np.bincount((Wd @ S.T).argmax(1), minlength=len(keep)) / 20000
            share = "; ".join(f"{short(names[keep[i]])} {first[i]:.0%}" for i in np.argsort(-first) if first[i] >= 0.01)
            print(f"| {risk} | {'first engine, $5.3k + prop, 15 kg + prop' if fe else 'phase 1 ($1.5k-5k [Q], 21-32 kg)'} | {r2} / {r7} | "
                  + " > ".join(short(n) for n in nk) + f" | {share} |")
