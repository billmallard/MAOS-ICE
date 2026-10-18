"""Keep-out map under the piston for the picked stack (AER-3442).

For every point of the piston's footprint, the deepest piston material
allowed below the gudgeon-pin centre for 3 mm to the crank, worst of the
six cylinders, over 720 deg. The bounding cap box is used for the rod big
ends. Outlined: the pin-boss zone and the two skirt-panel zones.

Run: python3 plot_stack_h.py   (writes stack_h_keepout.png beside it)
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, Rectangle
import numpy as np

import stack_h as s

c = s.run_case(s.PICK["rod_in"], "box", s.PICK["ch_in"], step=2)
reach = c["reach"].max(axis=0)
depth = -reach - s.CLEAR
depth = np.where(c["z"]["bore"], np.clip(depth, None, 60), np.nan)

ramp = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
cmap = LinearSegmentedColormap.from_list("blue", ramp[::-1])   # dark = crank close = little room
fig, ax = plt.subplots(figsize=(7.2, 6.4), dpi=130)
m = ax.pcolormesh(s.XS, s.YS, depth.T, cmap=cmap, vmin=15, vmax=60, shading="nearest")
cb = fig.colorbar(m, ax=ax, shrink=0.85)
cb.set_label("deepest piston material allowed below the pin centre (mm)", color="#333")
g = s.G
ax.add_patch(Circle((0, 0), g["piston_r"], fill=False, ec="#555", lw=1))
bl = s.PIN_LEN / 2 + 2.5
ax.add_patch(Rectangle((-bl, -g["boss_half_w"]), 2 * bl, 2 * g["boss_half_w"], fill=False, ec="#222", lw=1.6, ls="--"))
for sy in (1, -1):
    y0 = g["panel_y"] if sy > 0 else -g["piston_r"]
    ax.add_patch(Rectangle((-g["panel_half_chord"], y0), 2 * g["panel_half_chord"], g["piston_r"] - g["panel_y"],
                           fill=False, ec="#222", lw=1.6))
ax.text(0, 0, f"pin bosses\n<= {c['boss']:.1f} mm", ha="center", va="center", color="white", fontsize=9)
ax.text(0, 46, f"skirt panel <= {c['panel']:.1f} mm", ha="center", va="center", color="#111", fontsize=9)
ax.text(0, 28, "own rod's slot:\nnot checked", ha="center", va="center", color="#333", fontsize=8)
ax.text(0, -46, "skirt panel", ha="center", va="center", color="#111", fontsize=9)
ax.set_xlabel("x along the gudgeon pin / crank axis, from the bore centre (mm)", color="#333")
ax.set_ylabel("y toward the thrust faces (mm)", color="#333")
ax.set_aspect("equal")
ax.set_xlim(-56, 56)
ax.set_ylim(-56, 56)
ax.set_title(f"Piston keep-out, {s.PICK['rod_in']:.3f} in rod, H-301, 3 mm clearance\n"
             "worst of six cylinders over 720 deg; big ends as the bounding cap box", fontsize=10)
for sp in ax.spines.values():
    sp.set_color("#999")
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stack_h_keepout.png"))
print("boss", c["boss"], "panel", c["panel"])
