"""Shaded renders of the concept H casting set from the STL files that
h_castings.py writes beside the STEP files (AER-3331). Fit-check pictures
only; the STEP files are the deliverable.

Run: python3 render_h.py <dir holding the .stl files>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

SRC = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = os.path.dirname(os.path.abspath(__file__))


def read_stl(path):
    v = []
    with open(path) as f:
        for line in f:
            t = line.split()
            if t and t[0] == "vertex":
                v.append([float(t[1]), float(t[2]), float(t[3])])
    return np.array(v).reshape(-1, 3, 3)


def shade(tris, light=(0.4, 0.5, 0.75)):
    n = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    k = 0.35 + 0.65 * np.abs(n @ (np.array(light) / np.linalg.norm(light)))
    return np.clip(np.outer(k, [0.62, 0.66, 0.72]), 0, 1)


def draw(ax, tris, elev, azim, title):
    pc = Poly3DCollection(tris, facecolors=shade(tris), edgecolors="none")
    ax.add_collection3d(pc)
    lo, hi = tris.reshape(-1, 3).min(0), tris.reshape(-1, 3).max(0)
    c, r = (lo + hi) / 2, (hi - lo).max() / 2
    ax.set_xlim(c[0] - r, c[0] + r)
    ax.set_ylim(c[1] - r, c[1] + r)
    ax.set_zlim(c[2] - r, c[2] + r)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim, vertical_axis="y")
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)


def sheet(name, views, src):
    tris = read_stl(os.path.join(SRC, src))
    fig = plt.figure(figsize=(6 * len(views), 6), dpi=110)
    for i, (elev, azim, title) in enumerate(views):
        draw(fig.add_subplot(1, len(views), i + 1, projection="3d"), tris, elev, azim, title)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight")
    plt.close(fig)
    print(name, len(tris), "triangles")


sheet("H-101_views.png", [(25, 35, "H-101 case half LH: deck, liner registers, head studs"),
                          (20, -125, "H-101: split face, main housings, cam bore, dowels")], "H-101.stl")
sheet("H-201_views.png", [(25, -150, "H-201 head: deck, chambers, seat bores, ring dowels"),
                          (55, -30, "H-201: intake face (top), plug set A, injectors, rocker box")], "H-201.stl")
sheet("H-000_casting_set.png", [(30, 50, "Casting set: H-101 + H-102 + 2 x H-201 (fit check)")],
      "H-000_casting_set.stl")
