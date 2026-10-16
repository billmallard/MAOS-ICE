"""Rank the drive and propeller options at concept H's rpm (AER-3326).

Weighted-sum decision matrix with Monte Carlo over weights. Performance
criteria use ratio-to-best (as rank.py). Cost and mass are scored against the
engine's own budget instead, so a small absolute difference between two cheap
propellers does not swamp everything else:
  cost score = 10 (1 - cost / $22,000),  mass score = 10 (1 - kg / 150 kg)
(the ruled 200 hp cost and the proposed R-37 mass). Options with an unverified
price or behavior are ranked, flagged, and the ranking is repeated without them. Performance cells come from drive_match.py. Mass
and price are the phase-0 sourced figures in
`docs/engine/sources/PROP_AND_DRIVE_SOURCES_2026-10-16.md` (as summarized in
DRIVE_AND_PROP.md); where none was found the option takes the worst value in
the set and is flagged UNPRICED.

Criteria and weights:
  climb   thrust-power fraction at 80 kt            0.20  (brief: prop constraint)
  cruise  thrust-power fraction at 165 kt           0.20
  static  static thrust                             0.05  (rank order only)
  cost    prop + drive, USD (builder pays it; it is outside the engine's $22k
          by the R-35 definition)                   0.20  (ruling 2, brief)
  mass    prop + drive, kg                          0.10
  risk    worst single failure, 0-10: 10 none beyond the blade, 7 fails to
          a fixed pitch, 4 fails to a fixed pitch with overspeed exposure,
          1 total loss of thrust (gearbox, belt, neutral)  0.25 (FL ledger)

Run: python3 drive_rank.py   (reruns drive_match.py, about 20 s)
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("dm", os.path.join(HERE, "drive_match.py"))
DM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DM)

# option key prefix -> (cost USD, mass kg, risk score, note)
DATA = {
    "1 ": (4000, 7.0, 10, "MT / Sensenich fixed pitch $3,600-4,304, 5.4-8.2 kg"),
    "2 ": (6250, 33.0, 1, "gearbox $1.5-5k [Q] + prop; gearbox 21-32 kg; FL-1"),
    "3a": (3600, 8.5, 10, "Whirlwind GA-200L $2,915 to Sensenich $4,338, 8-9 kg"),
    "3b": (3600, 8.5, 10, "as 3a"),
    "4a": (None, None, 1, "UNPRICED: no flying piston CVT found; belt failure = total loss (FL-3)"),
    "5 ": (None, None, 1, "UNPRICED: no flying example; neutral must be designed out (FL-5)"),
    "6/7/9 Variable pitch direct, held": (14800, 20.0, 4, "Hartzell C2YR $12,463 + PCU5000X $2,350; 16-23 kg; oil loss -> fine (FL-7)"),
    "6/7/9 Variable pitch direct, 3,300 TO": (14800, 20.0, 4, "as above, UL rpm schedule"),
    "7 ": (18050, 46.0, 1, "CS + gearbox; FL-1"),
    "8b": (1900, 7.0, 10, "one owner report, about $1,900; mass not found (taken as fixed pitch); 200 hp availability not confirmed"),
}
W = np.array([0.20, 0.20, 0.05, 0.20, 0.10, 0.25])
LOWER = [False, False, False, True, True, False]


def lookup(name):
    for k, v in DATA.items():
        if name.startswith(k):
            return v
    raise KeyError(name)


if __name__ == "__main__":
    out = DM.main()
    names = list(out)
    raw = []
    for n in names:
        rows = {r["V"]: r for r in out[n]["rows"]}
        cost, mass, risk, note = lookup(n)
        raw.append([max(rows[80]["thp_frac"], 0), max(rows[165]["thp_frac"], 0), rows[0]["T"] / 1000, cost, mass, risk])
    X = np.array([[np.nan if v is None else v for v in r] for r in raw], float)
    for j in (3, 4):   # unpriced -> worst in set, flagged
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
    tot = S @ W
    order = np.argsort(-tot)
    print("| rank | Option | 80 kt | 165 kt | static (kN) | prop + drive $ | kg | risk 0-10 | total | note |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r, i in enumerate(order):
        c, m, rk, note = lookup(names[i])
        print(f"| {r+1} | {names[i]} | {X[i,0]:.2f} | {X[i,1]:.2f} | {X[i,2]:.2f} | "
              f"{'UNPRICED' if c is None else f'{c:,.0f}'} | {'n/f' if m is None else f'{m:.0f}'} | {rk} | {tot[i]:.2f} | {note} |")
    unverified = [i for i, n in enumerate(names) if n.startswith(("8b", "4a", "5 "))]
    for subset, idx in (("all options", list(range(len(names)))),
                        ("without unverified options (8b, 4a, 5)", [i for i in range(len(names)) if i not in unverified])):
        rng = np.random.default_rng(1)
        Ss = S[idx]
        o = np.argsort(-(Ss @ W))
        print(f"\n{subset}: order " + " > ".join(names[idx[i]].split(' ')[0] + ('' if 'held' not in names[idx[i]] else '(3,300)') + ('(sched)' if 'schedule' in names[idx[i]] else '') for i in o))
        for label, alpha in (("centred", 20 * W), ("flat", np.ones(len(W)))):
            Wd = rng.dirichlet(alpha, 20000)
            first = np.bincount((Wd @ Ss.T).argmax(1), minlength=len(idx)) / 20000
            print(f"  first-place share, {label} Dirichlet: " + "; ".join(
                f"{names[idx[i]][:34]} {first[i]:.0%}" for i in np.argsort(-first) if first[i] >= 0.01))
