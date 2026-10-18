"""H-301 crankshaft: the quoting print (AER-3439). A shaded view of the STL
that h_crank.py writes, a side view and an end view projected from the same
mesh, and the governing dimensions taken from h301_params.json. The STEP and
CRANK_H301.md are the deliverable; this picture is how a reviewer reads them.

Run: python3 render_h301.py <dir holding H-301.stl>
"""
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else HERE
G = json.load(open(os.path.join(HERE, "h301_params.json")))
INFO = json.load(open(os.path.join(HERE, "h301.json")))


def read_stl(path):
    """Binary STL, as MeshPart writes it."""
    with open(path, "rb") as f:
        f.read(80)
        n = int(np.frombuffer(f.read(4), "<u4")[0])
        rec = np.frombuffer(f.read(50 * n), dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]))
    return rec["v"].astype(float)


def shade(tris, light=(0.4, 0.5, 0.75)):
    n = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    k = 0.35 + 0.65 * np.abs(n @ (np.array(light) / np.linalg.norm(light)))
    return np.clip(np.outer(k, [0.62, 0.66, 0.72]), 0, 1)


def silhouette(ax, tris, i, j, color="0.80"):
    ax.add_collection(PolyCollection(tris[:, :, [i, j]], facecolors=color, edgecolors=color, linewidths=0.2))


def dim(ax, x0, x1, y, text, above=True):
    ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", lw=0.7, color="k"))
    ax.text((x0 + x1) / 2, y + (3 if above else -3), text, ha="center", va="bottom" if above else "top", fontsize=6.5)


tris = read_stl(os.path.join(SRC, "H-301.stl"))
fig = plt.figure(figsize=(16, 10))

# --- side view (x horizontal, z vertical), cylinder 1 at TDC
ax = fig.add_axes([0.05, 0.46, 0.63, 0.49])
silhouette(ax, tris, 0, 2)
mains = [G["x_main0"] + k * G["pitch"] for k in range(4)]
R = G["stroke"] / 2
for k, xm in enumerate(mains):
    ax.plot([xm, xm], [-120, 120], "k-.", lw=0.4)
    ax.text(xm, -128, f"M{k+1}\n{xm:.1f}", ha="center", va="top", fontsize=6.5)
for bay in range(3):
    m0 = mains[bay]
    x1 = m0 + G["main_w"] / 2 + G["web_t"] + G["pin_w"] / 2
    for i, x in ((2 * bay, x1), (2 * bay + 1, x1 + G["pin_w"] + G["web_t"])):
        a = -G["throws_against_rotation"][i]
        zc = R * math.cos(math.radians(a))
        ax.plot([x, x], [zc - 30, zc + 30], "b-.", lw=0.4)
        ax.text(x, 100 if i % 2 == 0 else -100, f"P{i+1}\n{x:.2f}", ha="center", va="center", fontsize=6.5, color="b")
dim(ax, mains[0], mains[1], 112, f"bank pitch = main spacing {G['pitch']:.1f}")
x1 = mains[0] + G["main_w"] / 2 + G["web_t"] + G["pin_w"] / 2
dim(ax, x1, x1 + G["pin_w"] + G["web_t"], 75, f"bank offset {G['pin_w'] + G['web_t']:.1f}")
dim(ax, INFO["x_span"][0], INFO["x_span"][1], -150, f"overall {INFO['x_span'][1] - INFO['x_span'][0]:.1f}", above=False)
ax.text(-25, 82, f"propeller flange\nOD {G['flange_od']:.0f} x {G['flange_t']}\n6 bushing bores {G['flange_bushing_bore']}\non {G['flange_bc']} (4.750 in)\npilot {G['pilot_d']:.0f} [Q]",
        fontsize=6.5, ha="center")
xr = mains[3] + G["main_w"] / 2
ax.text(xr + 40, 82, f"cam-gear seat {G['cam_gear_seat_d']:.0f} x {G['cam_gear_seat_l']:.0f}\nreluctor seat {G['reluctor_seat_d']:.0f} x {G['reluctor_seat_l']:.0f}\n"
        f"damper flange {G['damper_flange_od']:.0f}, 6 x M10 on {G['damper_bc']:.0f}\ndamper pilot {G['damper_pilot_d']:.0f}", fontsize=6.5, ha="center")
ax.set_xlim(-60, 540)
ax.set_ylim(-175, 135)
ax.set_aspect("equal")
ax.set_title("H-301 crankshaft, side view, cylinder 1 at TDC (pin P1 toward the LH bank, +z). x from the case front face, mm", fontsize=9)
ax.set_xlabel("x (mm)")
ax.set_ylabel("z (mm), +z LH bank")

# --- end view from the rear
ax = fig.add_axes([0.70, 0.45, 0.28, 0.48])
t = tris.copy()
silhouette(ax, t, 2, 1, "0.85")
for i in range(6):
    a = math.radians(-G["throws_against_rotation"][i])
    zc, yc = R * math.cos(a), R * math.sin(a)
    # seen from the rear +z is on the left: plot -z to the right
    ax.add_patch(plt.Circle((-zc, yc), G["pin_d"] / 2, fill=False, color="b", lw=0.8))
    ax.text(-zc * 1.9, yc * 1.9, f"P{i+1}\n{G['throws_against_rotation'][i]} deg", ha="center", va="center", fontsize=7, color="b")
ax.add_patch(plt.Circle((0, 0), G["main_d"] / 2, fill=False, color="k", lw=0.8))
ax.annotate("", (40, 95), (-40, 95), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3", lw=1))
ax.text(0, 112, "rotation: clockwise seen from the rear", ha="center", fontsize=7)
ax.text(-105, -118, "LH bank", fontsize=7)
ax.text(70, -118, "RH bank", fontsize=7)
ax.set_xlim(-130, 130)
ax.set_ylim(-130, 125)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("End view from the rear. Pin angles are measured against\nthe rotation from P1, cylinder 1 at TDC. Firing 1-6-3-2-5-4", fontsize=8)

# --- shaded iso
ax = fig.add_axes([0.0, 0.0, 0.40, 0.38], projection="3d")
ax.add_collection3d(Poly3DCollection(tris, facecolors=shade(tris), edgecolors="none"))
lo, hi = tris.reshape(-1, 3).min(0), tris.reshape(-1, 3).max(0)
c, r = (lo + hi) / 2, (hi - lo).max() / 2
ax.set_xlim(c[0] - r, c[0] + r)
ax.set_ylim(c[1] - r, c[1] + r)
ax.set_zlim(c[2] - r, c[2] + r)
ax.view_init(elev=22, azim=-58)
ax.set_axis_off()
ax.set_title("shaded, from the front left", fontsize=8)

# --- notes block
notes = (
    f"H-301 crankshaft, concept H 200 hp member. Rev A, for quotation only. AER-3439. Model mass {INFO['mass_kg']} kg.\n"
    "Material: 4340 VAR, AMS 6414 (quote AMS 6415 air-melt as an alternate). Quench and temper 28-32 HRC core.\n"
    f"Journals: mains {G['main_d']:.2f} (-0.013/-0.025 [E], to the main shell maker's table [Q]); pins {G['pin_d']} = 2.100 in\n"
    f"(LS rod shell table). Pin width {G['pin_w']}; main width {G['main_w']:.0f}, M1 {G['front_main_w']:.0f} with ground thrust faces.\n"
    f"Fillets R{G['fillet_r']:.0f} on every journal, ground in form, no undercut; journals Ra 0.2 um, fillets Ra 0.4 um.\n"
    "Gas nitride after finish grind: effective case 0.30-0.50 mm, compound layer <= 5 um on journals; micropolish after.\n"
    "Runout, supported on M1 and M4: M2/M3 0.025 FIR; flange face 0.05 FIR [E] (Continental IO-520 service limit 0.005 in [S]).\n"
    "Oil: one straight 6 mm drilling per pin from its nearer main; break and polish both ends; no plugs.\n"
    "Balance the crank alone, no bob weight, ISO 21940-11 G2.5 at 3,300 rpm [E]; match rods end for end and pistons per pair.\n"
    "MPI (ASTM E1444) after rough machining and after nitriding. Unlisted dims ISO 2768-m. Nothing here has been made or tested."
)
fig.text(0.44, 0.03, notes, fontsize=7.4, family="monospace", va="bottom")
fig.savefig(os.path.join(HERE, "H-301_drawing.png"), dpi=130)
print("wrote H-301_drawing.png")
