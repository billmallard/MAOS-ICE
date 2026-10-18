"""Concept H, H-301 crankshaft: STEP of the one-off billet crank for the
specialist RFQ (AER-3439). Geometry from h301_params.json, which the
clearance sweep in analysis/engine_crank/crank_decision.py also reads.

Drawn: main journals, crankpins, webs (round-ended, 1.6 x pin wide),
counterweight lobes on the outer webs, the propeller flange with its six
bushing bores and pilot, the seal journal, the rear snout (cam-gear seat,
reluctor seat and damper-hub seat, each keyed at P1's angle and stepping
down toward the rear so its ring slides on from the rear, and the tapped
centre-bolt hole that clamps the stack (Rev B, MANUFACTURING DFM B1), the
front thrust collar ahead of M1 (Rev B, B2), and one oil drilling from a
main to each pin. Not drawn: fillets (called out on the
drawing), thrust faces' relief grooves, chamfers, the center holes.

Nothing here has been made, measured or run. An experimental engine design.

Frame (engine, mm): x along the crank axis from the case front face
(propeller end) to the rear; y up; z outboard, +z the LH bank. The crank
is shown with cylinder 1 at TDC (its pin on +z).

Run (from the MAOS-ICE checkout):
  mkdir -p /maos-work/shared/cad/aer3439_h301
  cp cad/concept_h/h_crank.py cad/concept_h/h301_params.json /maos-work/shared/cad/aer3439_h301/
  maos freecad -c "OUT='/workspace/cad/aer3439_h301'; exec(open(OUT + '/h_crank.py').read())"
"""
import json
import math
import os

import FreeCAD as App
import Import
import Part
from FreeCAD import Vector as V

OUT = globals().get("OUT", os.getcwd())
G = json.load(open(os.path.join(OUT, "h301_params.json")))
RHO = 7.85e-6                       # kg/mm^3, 4340
R = G["stroke"] / 2
X_AX = V(1, 0, 0)


def cyl(r, x0, x1):
    return Part.makeCylinder(r, x1 - x0, V(x0, 0, 0), X_AX)


def radial(ang_deg, r):
    """Point at radius r in the y-z plane; angle from +z toward +y, which is
    the position a pin reaches after turning ang_deg in the direction of
    rotation (clockwise seen from the rear, the usual tractor sense) [E]."""
    a = math.radians(ang_deg)
    return V(0, r * math.sin(a), r * math.cos(a))


def pin_dir(i):
    # cylinder 1 at TDC: pin i sits a_i AGAINST the direction of rotation from pin 1
    return -G["throws_against_rotation"][i]


def stadium(c0, c1, r, x0, x1):
    """Round-ended slab joining two circles of radius r centred at c0 and
    c1 (y-z points), from x0 to x1."""
    a = Part.makeCylinder(r, x1 - x0, V(x0, c0.y, c0.z), X_AX)
    b = Part.makeCylinder(r, x1 - x0, V(x0, c1.y, c1.z), X_AX)
    d = c1 - c0
    L = d.Length
    if L < 1e-6:
        return a
    u = V(0, d.y / L, d.z / L)
    n = V(0, -u.z, u.y)
    p = [c0 + n * r, c1 + n * r, c1 - n * r, c0 - n * r]
    w = Part.makePolygon([V(x0, q.y, q.z) for q in p] + [V(x0, p[0].y, p[0].z)])
    box = Part.Face(w).extrude(V(x1 - x0, 0, 0))
    return a.fuse(b).fuse(box)


def sector(r, half, centre_deg, x0, x1):
    s = Part.makeCylinder(r, x1 - x0, V(x0, 0, 0), X_AX, 2 * half)
    # makeCylinder's sector starts on local +x of its placement; for an x-axis
    # cylinder that is the global +z... confirm by its centre of mass below
    cm = s.CenterOfMass
    cur = math.degrees(math.atan2(cm.y, cm.z))
    s.rotate(V(0, 0, 0), X_AX, -(centre_deg - cur))
    cm = s.CenterOfMass
    got = math.degrees(math.atan2(cm.y, cm.z))
    if abs(((got - centre_deg + 180) % 360) - 180) > 1.0:
        s.rotate(V(0, 0, 0), X_AX, 2 * (centre_deg - cur))
    return s


def build():
    parts = []
    feats = []
    mains = [G["x_main0"] + k * G["pitch"] for k in range(4)]
    hw = G["main_w"] / 2
    # main journals; the front one is wider, forward, for the thrust faces
    jspan = []
    for k, xm in enumerate(mains):
        x0 = xm + hw - G["front_main_w"] if k == 0 else xm - hw
        x1 = xm + hw
        parts.append(cyl(G["main_d"] / 2, x0, x1))
        jspan.append((x0, x1))
        feats.append(("main journal" + (" (thrust)" if k == 0 else ""), f"M{k+1}", f"x {x0:.1f}-{x1:.1f}", f"dia {G['main_d']:.2f}, width {x1-x0:.1f}"))
    pins = []
    for bay in range(3):
        m0 = mains[bay]
        xa = m0 + hw
        xp = [xa + G["web_t"] + G["pin_w"] / 2]
        xp.append(xp[0] + G["pin_w"] + G["web_t"])
        i1, i2 = 2 * bay, 2 * bay + 1
        c1 = radial(pin_dir(i1), R)
        c2 = radial(pin_dir(i2), R)
        for i, x in zip((i1, i2), xp):
            c = radial(pin_dir(i), R)
            p = Part.makeCylinder(G["pin_d"] / 2, G["pin_w"], V(x - G["pin_w"] / 2, c.y, c.z), X_AX)
            parts.append(p)
            pins.append((i, x, c))
            feats.append(("crankpin", f"P{i+1} ({G['banks'][i]}H)", f"x {x:.2f}", f"dia {G['pin_d']:.2f}, width {G['pin_w']:.1f}; at {G['throws_against_rotation'][i]} deg against rotation from P1"))
        o = V(0, 0, 0)
        # web A: front main to pin 1, with its counterweight
        xs = (xa, xa + G["web_t"])
        parts.append(stadium(o, c1, G["web_pin_r"], *xs))
        parts.append(sector(G["cw_r"], G["cw_half_angle"], pin_dir(i1) + 180, *xs))
        # middle web: pin 1 to pin 2
        xs = (xp[0] + G["pin_w"] / 2, xp[1] - G["pin_w"] / 2)
        parts.append(stadium(c1, c2, G["web_pin_r"], *xs))
        # web B: pin 2 to the rear main, with its counterweight
        xs = (xp[1] + G["pin_w"] / 2, mains[bay + 1] - hw)
        parts.append(stadium(c2, o, G["web_pin_r"], *xs))
        parts.append(sector(G["cw_r"], G["cw_half_angle"], pin_dir(i2) + 180, *xs))
        feats.append(("webs", f"bay {bay+1}", f"x {xa:.1f}-{mains[bay+1]-hw:.1f}", f"3 x {G['web_t']} thick, {2*G['web_pin_r']:.0f} wide; counterweights R{G['cw_r']:.0f} on the outer two"))
    # front: seal journal and propeller flange with pilot
    xf_back = G["flange_back_x"]
    xf_front = xf_back - G["flange_t"]
    xc = jspan[0][0] - G["thrust_collar_l"]
    parts.append(cyl(G["seal_d"] / 2, xf_back, xc))
    parts.append(cyl(G["thrust_collar_d"] / 2, xc, jspan[0][0]))
    feats.append(("thrust collar", "T", f"x {xc:.1f}-{jspan[0][0]:.1f}", f"dia {G['thrust_collar_d']:.0f} [E; at least the King F5382 thrust-flange OD, Q]; its rear face is M1's front thrust face"))
    fl = cyl(G["flange_od"] / 2, xf_front, xf_back)
    for k in range(G["flange_bushings"]):
        c = radial(30 + 60 * k, G["flange_bc"] / 2)
        fl = fl.cut(Part.makeCylinder(G["flange_bushing_bore"] / 2, G["flange_t"] + 2, V(xf_front - 1, c.y, c.z), X_AX))
    parts.append(fl)
    parts.append(cyl(G["pilot_d"] / 2, xf_front - G["pilot_l"], xf_front))
    feats.append(("propeller flange", "F", f"x {xf_front:.2f}-{xf_back:.2f}", f"OD {G['flange_od']:.0f}, {G['flange_t']} thick; 6 bushing bores {G['flange_bushing_bore']} on a {G['flange_bc']} circle (4.750 in); pilot dia {G['pilot_d']:.0f} x {G['pilot_l']:.0f} [Q]"))
    feats.append(("seal journal", "S", f"x {xf_back:.1f}-{xc:.1f}", f"dia {G['seal_d']:.0f}"))
    # rear snout: steps down toward the rear; every ring slides on from the
    # rear and one centre bolt clamps hub, reluctor and cam gear against the
    # M4 shoulder. Each seat carries a key slot at P1's angle (clocking).
    x = jspan[3][1]
    keyed = []
    for name, d, l in (("cam-gear seat", G["cam_gear_seat_d"], G["cam_gear_seat_l"]),
                       ("reluctor seat", G["reluctor_seat_d"], G["reluctor_seat_l"]),
                       ("damper-hub seat", G["hub_seat_d"], G["hub_seat_l"])):
        parts.append(cyl(d / 2, x, x + l))
        keyed.append((d, x, l))
        feats.append((name, "", f"x {x:.1f}-{x+l:.1f}", f"dia {d:.0f}, key slot {G['key_w']:.0f} wide x {G['key_depth']:.0f} deep at P1's angle"))
        x += l
    x_end = x

    shape = parts[0]
    for p in parts[1:]:
        shape = shape.fuse(p)
    shape = shape.removeSplitter()
    for d, x0, l in keyed:
        slot = Part.makeBox(l + 0.02, G["key_w"], G["key_depth"] + 1, V(x0 - 0.01, -G["key_w"] / 2, d / 2 - G["key_depth"]))
        shape = shape.cut(slot)
    tap = Part.makeCylinder(G["center_bolt_tap_d"] / 2, G["center_bolt_depth"], V(x_end - G["center_bolt_depth"], 0, 0), X_AX)
    shape = shape.cut(tap)
    feats.append(("centre bolt", "", f"x {x_end - G['center_bolt_depth']:.1f}-{x_end:.1f}", f"M16 x 1.5 tapped ({G['center_bolt_tap_d']} drill) x {G['center_bolt_depth']:.0f} deep; clamps hub, reluctor and cam gear"))

    # oil drillings: each pin from its nearer main, entering the main
    # journal 90 deg behind the pin and leaving the pin 60 deg ahead of
    # its outermost point [E]; final exit angle from the bearing load
    # polar at rev B
    for i, xp_, c in pins:
        bay = i // 2
        xm = mains[bay] if i % 2 == 0 else mains[bay + 1]
        a = radial(pin_dir(i) - 90, G["main_d"] / 2)
        b = c + radial(pin_dir(i) + 60, G["pin_d"] / 2)
        A = V(xm, a.y, a.z)
        B = V(xp_, b.y, b.z)
        d = B - A
        L = d.Length
        u = d * (1 / L)
        drill = Part.makeCylinder(G["oil_hole_d"] / 2, L + 6, A - u * 3, u)
        shape = shape.cut(drill)
        feats.append(("oil drilling", f"O{i+1}", f"main x {xm:.1f} to pin x {xp_:.1f}", f"dia {G['oil_hole_d']:.0f}, straight, {L:.0f} long, no plugs"))
    return shape, feats, (xf_front - G["pilot_l"], x_end)


shape, feats, span = build()
assert shape.isValid(), "H-301 solid is not valid"
assert len(shape.Solids) == 1, f"H-301 is {len(shape.Solids)} solids"
doc = App.newDocument("H301")
o = doc.addObject("Part::Feature", "H301")
o.Shape = shape
o.Label = "H-301 Rev B crankshaft, 4340 VAR (AMS 6414), nitrided"
Import.export([o], os.path.join(OUT, "H-301.step"))
mesh_ok = True
try:
    import MeshPart
    m = MeshPart.meshFromShape(Shape=shape, LinearDeflection=0.3, AngularDeflection=0.3)
    m.write(os.path.join(OUT, "H-301.stl"))
except Exception as e:      # renders are optional
    mesh_ok = False
bb = shape.BoundBox
info = dict(
    part="H-301", mass_kg=round(shape.Volume * RHO, 2), volume_mm3=round(shape.Volume),
    box_mm=[round(bb.XLength, 1), round(bb.YLength, 1), round(bb.ZLength, 1)],
    x_span=[round(span[0], 2), round(span[1], 2)], solids=len(shape.Solids), valid=shape.isValid(),
    features=feats, stl=mesh_ok,
)
json.dump(info, open(os.path.join(OUT, "h301.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in info.items() if k != "features"}))
