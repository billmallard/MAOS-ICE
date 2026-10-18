"""Plot for scaling_sweep.py: first-engine cost and dry mass against rated rpm
(AER-3411). Called by `python3 scaling_sweep.py --plot`. Palette: the
dataviz reference categorical slots 1-3, validated (light surface); aqua is
under 3:1 against the surface, so every series is also direct-labeled and
carries its own marker, and the numbers are in scaling_sweep_tables.md."""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SERIES = {4: ("#2a78d6", "o"), 6: ("#eb6834", "s"), 8: ("#1baf7a", "^")}


def plot(sweep, h, path, oe=()):
    h_off = {"b1": (30, 34), "mass": (-12, -16)}
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), facecolor=SURFACE)
    for ax, key, lab in ((axes[0], "b1", "First-engine cost, basis 1 mid ($k)"),
                         (axes[1], "mass", "Installed dry mass, band mid (kg)")):
        ax.set_facecolor(SURFACE)
        for n, pts in sweep.items():
            col, mk = SERIES[n]
            x = [p["N"] for p in pts]
            y = [p[key][1] / 1000 if key == "b1" else sum(p["mass"]) / 2 for p in pts]
            for seg in ([i for i, p in enumerate(pts) if not p["geared"]], [i for i, p in enumerate(pts) if p["geared"]]):
                ax.plot([x[i] for i in seg], [y[i] for i in seg], color=col, lw=2, marker=mk, ms=8, mec=SURFACE, mew=2, zorder=3)
            ax.annotate(f"{n} cyl, custom crank", (x[-1], y[-1]), xytext=(6, 0), textcoords="offset points",
                        color=INK2, fontsize=9, va="center")
        for p in oe:
            y = p[key][1] / 1000 if key == "b1" else sum(p["mass"]) / 2
            ax.plot(p["N"], y, marker="D", ms=9, color=INK, mec=SURFACE, mew=2, zorder=4)
            off = p.get("off", {}).get(key, (7, -10))
            ax.annotate(p["short"], (p["N"], y), xytext=off, textcoords="offset points", color=INK, fontsize=8.5,
                        arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6) if abs(off[1]) > 14 else None)
        yh = h["b1"][1] / 1000 if key == "b1" else sum(h["mass"]) / 2
        ax.plot(3300, yh, marker="*", ms=16, color=INK, mec=SURFACE, mew=1.5, zorder=5)
        ax.annotate("concept H", (3300, yh), xytext=(h_off[key]), textcoords="offset points", color=INK, fontsize=9, ha="center",
                    arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
        ax.axvline(3400, color=INK2, lw=1, ls=":", zorder=1)
        ax.annotate("gearbox above 3,400 rpm", (3420, ax.get_ylim()[0]), xytext=(4, 6), textcoords="offset points",
                    color=INK2, fontsize=8.5)
        ax.set_title(lab, color=INK, fontsize=11, loc="left")
        ax.set_xlabel("Rated crank rpm, 200 hp member", color=INK2)
        ax.grid(True, color=GRID, lw=0.8)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        for s in ("left", "bottom"):
            ax.spines[s].set_color(GRID)
        ax.tick_params(colors=INK2)
        ax.set_xlim(2450, 6900)
    fig.text(0.01, 0.005, "Estimates [E], not quotes. Custom crank = one-off billet from a crank specialist. "
             "Diamonds = mass-production cranks. Bands and tables: scaling_sweep_tables.md.", color=INK2, fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
