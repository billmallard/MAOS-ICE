"""Concept H, 200 hp member: coarse STEP envelope of each surviving casting
(AER-3331, after the rulings on MANUFACTURING envelope v1 section 9.5).
Revised by AER-3442 to crank H-301: the bank pitch, main positions and pin
offsets are read from h301_params.json (the file H-301's STEP is built
from), and the deck and liner from h_stack.json (written by
analysis/engine_crank/stack_h.py, the rod / piston / liner pick), so the
castings and the crank cannot drift apart.

Three part numbers, four castings per engine:
  H-101  crankcase half LH, cylinder bank merged (9.5 #1), A357-T6
  H-102  crankcase half RH, cylinder bank merged, A357-T6
  H-201  cylinder head, one part number on both banks (9.5 #3), A356-T6;
         the RH bank takes it rotated 180 deg about the vertical axis

COARSE: near-net as-machined shape. Walls, ribs, bolt flanges, oil
cross-drillings, fillets and draft are not drawn. Datum pads and critical
bores are drawn and listed in PART_LIST.md, which this script writes.
Nothing here has been made, measured or run.

Frame (engine, mm): x along the crank axis from the case front face
(propeller end) to the rear; y up; z outboard, +z the LH bank. The case
split plane is z = 0.

Run (from the MAOS-ICE checkout; see README.md):
  cp cad/concept_h/h_castings.py cad/concept_h/h301_params.json cad/concept_h/h_stack.json /maos-work/shared/cad/aer3331_h/
  maos freecad -c "OUT='/workspace/cad/aer3331_h'; exec(open(OUT + '/h_castings.py').read())"
"""
import json
import math
import os

import FreeCAD as App
import Import
import Part
from FreeCAD import Vector as V

OUT = globals().get("OUT", os.getcwd())
RHO = 2.68e-6            # kg/mm^3, A356 / A357

# ------------------------------------------------------------- parameters
CRANK = json.load(open(os.path.join(OUT, "h301_params.json")))     # H-301 Rev A
STACK = json.load(open(os.path.join(OUT, "h_stack.json")))         # stack_h.py pick
P = CRANK["pitch"]       # main spacing = bore pitch along a bank (H-301: 122.0)
DP = P - 111.8           # growth per bay over the AER-3331 draw (LS 4.400 in pitch)
BORE = 104.8             # finished bore in the liner (LS7)
X0 = CRANK["x_main0"]    # front main centre
MAINS = [X0 + k * P for k in range(4)]
_lh = CRANK["main_w"] / 2 + CRANK["web_t"] + CRANK["pin_w"] / 2
PIN_OFF = {"LH": _lh, "RH": _lh + CRANK["pin_w"] + CRANK["web_t"]}   # crankpin from its bay's front main (40.35 / 81.75)
DECK = STACK["deck"]     # split plane to deck: 50.8 + rod + compression height + 0.5 (stack_h.py)
LINER_BOTTOM = STACK["liner_bottom"]    # liner bottom from the crank axis (stack_h.py)
CASE_L = 560.0 + 3 * DP  # case length; the rear timing bay keeps its AER-3331 depth
CAM_Y = -130.0           # cam below the crank, in the split plane
CAM_BORE = 59.0          # LS cam journal 55 mm + bushing [E]
MAIN_HOUSING = 64.0      # 60 mm journal + catalog shells [Q: confirm against a shell listing]
LIFTER = 21.4            # LS lifter 0.842 in
GALLERY = 14.0           # ruling 6: 14 mm main gallery, 20 x D from each end
GAL_Y, GAL_Z = -105.0, 100.0
REG_LOWER = 116.0        # liner lower (O-ring) register [Q: Darton MID prep drawing]
BARREL_OD = REG_LOWER + 2 * 6.0   # cast lower barrel round each liner bottom, 6 mm wall [E]
REG_LOWER_Z = LINER_BOTTOM        # the O-ring register runs to the sleeve's bottom, where Darton's O-rings sit
JACKET = 127.0           # open-deck jacket around the liner
REG_UPPER = 131.4        # liner flange seat; stepped: upper >= jacket >= lower (ruling 5)
FLANGE_SEAT = 13.0       # depth of the flange seat below the deck [Q]
HEAD_STUD_DRILL = 9.5    # M11 stud tap drill (LS head-bolt size)
STUD_Y = 64.0
MAIN_STUD = 11.0
MAIN_STUD_Y = 85.0

# head (local frame: x along the row, centred on the middle cylinder; y up;
# z from the deck outboard)
H_L, H_W, H_T = 380.0 + 2 * DP, 180.0, 110.0
VALVE_TILT = math.radians(15.0)      # all six valve axes parallel (ruling 4)
V_IN, V_EX = -26.0, 26.0             # valve x offsets from the cylinder centre
SEAT_IN, SEAT_EX = 55.0, 43.0        # seat-insert bores, 2.00 in / 1.55 in valves [E]
GUIDE = 12.7                         # catalog guide OD [Q]
PORT_IN, PORT_EX = 38.0, 32.0
PLUG = 14.0                          # 14 mm plugs, two per cylinder (R-25)
INJ = 14.5                           # EV14 lower O-ring bore [E]
CHAMBER, CHAMBER_D = 100.0, 8.0


def cyl(r, p0, p1):
    d = p1 - p0
    return Part.makeCylinder(r, d.Length, p0, d)


def box(x0, x1, y0, y1, z0, z1):
    return Part.makeBox(x1 - x0, y1 - y0, z1 - z0, V(x0, y0, z0))


def fuse(base, parts):
    return base.fuse(parts).removeSplitter() if parts else base


def cut(base, parts):
    return base.cut(parts) if parts else base


def lobes():
    """12 cam lobes, four per bay at 22 mm pitch; LH and RH alternate."""
    out = {"LH": [], "RH": []}
    for k in range(3):
        c = (MAINS[k] + MAINS[k + 1]) / 2
        for j, off in enumerate((-33, -11, 11, 33)):
            out["LH" if j % 2 == 0 else "RH"].append(c + off)
    return out


def cylinders(side):
    return [MAINS[k] + PIN_OFF[side] for k in range(3)]


FEATURES = {}
PADS = {}               # rough (as-cast) datum pads per part: (role, centre, outward normal, dia)
PAD_PROUD = 3.0         # every pad of a part stands this far proud of its as-cast face

# Machining stock (MANUFACTURING on AER-3442, from ISO 8062:1994, now 8062-3):
# stock per side = RMA + CT/2. One-off chemically bonded (binder-jet, furan)
# sand light alloy: CT10-12 (Table A.2), RMA grade F-H (Table B.1). Plan on
# CT11 / RMA G until the foundry states the grade it holds; the first-article
# layout may then reduce it. [MANUFACTURING's figures; the 2023 tables not checked]
STOCK = {
    "H-101": ("ISO 8062 - CT11 - RMA 4 (G)", "5.0 / 6.8 / 10", 7.0, "the split face (datum A) and the deck"),
    "H-102": ("ISO 8062 - CT11 - RMA 4 (G)", "5.0 / 6.8 / 10", 7.0, "the split face (datum A) and the deck"),
    "H-201": ("ISO 8062 - CT11 - RMA 4 (G)", "4.8 / 6.5 / 9.5", 7.0, "the deck (datum A)"),
}


def case_half(side):
    """Build the half on the +z side; RH is mirrored to -z at the end."""
    cs = cylinders(side)
    feats = []
    shell = box(0, CASE_L, -178, 150, 0, 135).cut(box(8, CASE_L - 8, -170, 142, 0, 127))
    add = []
    for i, xm in enumerate(MAINS):
        x0, x1 = (35, 70) if i == 0 else (xm - 10, xm + 10)
        add.append(box(x0, x1, -170, 142, 0, 127))
    for xl in lobes()[side]:
        add.append(cyl(16, V(xl, CAM_Y, 18), V(xl, CAM_Y, 135)))
    add.append(cyl(15, V(0, GAL_Y, GAL_Z), V(CASE_L, GAL_Y, GAL_Z)))
    dowels = [(18, 134), (CASE_L - 18, -162)]
    for x, y in dowels:
        add.append(cyl(12, V(x, y, 0), V(x, y, 30)))
    bx0, bx1 = cs[0] - 72, cs[-1] + 72
    add.append(box(bx0, bx1, -72, 72, 127, DECK))
    for c in cs:   # lower barrels: the liner's O-ring end seals in metal, not in the open crank bay
        add.append(cyl(BARREL_OD / 2, V(c, 0, LINER_BOTTOM), V(c, 0, 127.5)))
    add.append(cyl(18, V(bx0 - 12, 0, 185), V(bx0 + 5, 0, 185)))
    pads = [((30, 120, 135), (0, 0, 1)), ((CASE_L - 40, 120, 135), (0, 0, 1)), ((CASE_L - 100, -160, 135), (0, 0, 1)),
            ((60, 150, 60), (0, 1, 0)), ((CASE_L - 60, 150, 60), (0, 1, 0)),
            ((0, 100, 80), (-1, 0, 0))]
    zs_ = 1 if side == "LH" else -1
    roles = ["primary 1", "primary 2", "primary 3", "secondary 1", "secondary 2", "tertiary"]
    PADS["H-101" if side == "LH" else "H-102"] = [
        (r, (x, y, zs_ * z), (n[0], n[1], zs_ * n[2]), 25.0) for r, ((x, y, z), n) in zip(roles, pads)]
    for (x, y, z), n in pads:
        add.append(cyl(12.5, V(x, y, z), V(x, y, z) + V(*n) * PAD_PROUD))
    s = fuse(shell, add)

    cuts = []
    cuts.append(cyl(MAIN_HOUSING / 2, V(-1, 0, 0), V(CASE_L + 1, 0, 0)))
    cuts.append(cyl(40, V(-1, 0, 0), V(8.1, 0, 0)))                          # front seal
    cuts.append(cyl(CAM_BORE / 2, V(8, CAM_Y, 0), V(CASE_L + 1, CAM_Y, 0)))
    cuts.append(cyl(100, V(CASE_L - 8.1, -60, 0), V(CASE_L + 1, -60, 0)))    # rear timing opening
    cuts.append(box(80, 480 + 3 * DP, -178.1, -169.9, 0, 115))                # sump opening
    for xl in lobes()[side]:
        cuts.append(cyl(LIFTER / 2, V(xl, CAM_Y, 0), V(xl, CAM_Y, 135.1)))
    cuts.append(cyl(GALLERY / 2, V(-1, GAL_Y, GAL_Z), V(CASE_L + 1, GAL_Y, GAL_Z)))
    for x, y in dowels:
        cuts.append(cyl(6, V(x, y, -0.1), V(x, y, 20)))
    for xm in MAINS:
        for y in (MAIN_STUD_Y, -MAIN_STUD_Y):
            cuts.append(cyl(MAIN_STUD / 2, V(xm, y, -0.1), V(xm, y, 135.1)))
    for c in cs:
        cuts.append(cyl(REG_LOWER / 2, V(c, 0, REG_LOWER_Z - 0.1), V(c, 0, 150)))
        cuts.append(cyl(JACKET / 2, V(c, 0, 150), V(c, 0, DECK - FLANGE_SEAT)))
        cuts.append(cyl(REG_UPPER / 2, V(c, 0, DECK - FLANGE_SEAT), V(c, 0, DECK + 0.1)))
    studs = sorted({round(c + d, 1) for c in cs for d in (-P / 2, P / 2)})
    for x in studs:
        for y in (STUD_Y, -STUD_Y):
            cuts.append(cyl(HEAD_STUD_DRILL / 2, V(x, y, DECK - 60), V(x, y, DECK + 0.1)))
    ring = [(cs[1] - 1.5 * P, -STUD_Y), (cs[1] + 1.5 * P, -STUD_Y)]
    for x, y in ring:
        cuts.append(cyl(8, V(x, y, DECK - 10), V(x, y, DECK + 0.1)))
    cuts.append(cyl(11, V(bx0 - 12.1, 0, 185), V(cs[0] - 50, 0, 185)))       # coolant inlet
    s = cut(s, cuts)

    zs = 1 if side == "LH" else -1
    feats += [
        ("datum A", "split face, z = 0, machined in setup A (4-axis)", "flat 0.05 [E]"),
        ("datum B / C", f"dowel holes 12 mm at (x, y) = {dowels}, reamed in setup A", "H7"),
        ("rough datums", "3 pads on the outer case face, 2 on the top face, 1 on the front face, 25 mm dia x 3 mm proud: setup A locates on these (table below)", "as cast"),
        ("main housings", f"4 x {MAIN_HOUSING} mm at x = {[round(x, 1) for x in MAINS]}, y = z = 0; line-bored on the doweled pair (setup B), then align-honed; front main carries the thrust faces", "catalog shell housing fit [Q]"),
        ("cam bore", f"{CAM_BORE} mm (bushed), y = {CAM_Y}, z = 0, in the split plane", "bushing press fit [Q]"),
        ("lifter bores", f"6 x {LIFTER} mm along z at y = {CAM_Y}, x = {[round(x, 1) for x in lobes()[side]]}", "LS lifter fit"),
        ("liner registers", f"3 cylinders at x = {[round(c, 1) for c in cs]}; lower register {REG_LOWER} mm (O-rings) from z = {zs * REG_LOWER_Z:.0f}, jacket {JACKET} mm, flange seat {REG_UPPER} mm x {FLANGE_SEAT} deep; all bored from the deck in setup B, stepped lower <= upper", "per Darton MID prep drawing [Q]"),
        ("liner", f"Darton MID {BORE} mm, {DECK - LINER_BOTTOM:.1f} mm long, fitted uncut, bottom at z = {zs * LINER_BOTTOM:.1f}; its O-ring end seals in a cast lower barrel, {BARREL_OD:.0f} mm OD, from z = {zs * LINER_BOTTOM:.1f} to the case wall. Liner and barrel clear the crank by 4.6 mm or more (stack_h.py section 5)", "bought; O-ring land and axial location [Q] with Darton"),
        ("lower barrel end faces", f"3 per half, faced to z = {zs * LINER_BOTTOM:.1f} in setup A from the open split-face side (an as-cast end at CT11, about +/-2.2 mm, could take the 4.6 mm crank clearance to 2.4 mm)", "+/-0.3 [E] to datum A"),
        ("deck", f"z = {zs * DECK:.0f}, open deck; head studs M11 x 8 at x = {studs}, y = +/-{STUD_Y}; ring-dowel counterbores 16 mm at {[(round(x, 1), y) for x, y in ring]}", "flat 0.05 [E]"),
        ("main gallery", f"{GALLERY} mm, drilled {CASE_L / 2:.0f} mm from each end at y = {GAL_Y}, z = {zs * GAL_Z:.0f}; threaded plugs, sealant, staked", "ruling 6"),
        ("main studs", f"8 x {MAIN_STUD} mm through holes at each main, y = +/-{MAIN_STUD_Y}", ""),
        ("coolant inlet", f"22 mm bore in a 36 mm boss on the bank's front end, y = 0, z = {zs * 185}", ""),
    ]
    if side == "RH":
        s = s.mirror(V(0, 0, 0), V(0, 0, 1))
    FEATURES["H-101" if side == "LH" else "H-102"] = feats
    return s


def head():
    d = V(0, math.sin(VALVE_TILT), math.cos(VALVE_TILT))
    cs = [-P, 0.0, P]
    s = box(-H_L / 2, H_L / 2, -H_W / 2, H_W / 2, 0, H_T)
    s = s.cut(box(-182 - DP, 182 + DP, -82, 82, 20, 72))       # coolant jacket (printed core)
    s = s.cut(box(-185 - DP, 185 + DP, -85, 85, 80, H_T + 0.1))  # rocker box, open to the cover
    add = []
    studs = [(x, y) for x in (-1.5 * P, -0.5 * P, 0.5 * P, 1.5 * P) for y in (STUD_Y, -STUD_Y)]
    for x, y in studs:
        add.append(cyl(11, V(x, y, 0), V(x, y, 80)))
    for c in cs:
        for xv in (c + V_IN, c + V_EX):
            p0 = V(xv, 0, CHAMBER_D)
            add.append(cyl(11, p0, p0 + d * 76))
        add.append(cyl(PORT_IN / 2 + 6, V(c + V_IN, 5, 18), V(c + V_IN, 90, 50)))
        add.append(cyl(PORT_EX / 2 + 6, V(c + V_EX, -5, 18), V(c + V_EX, -90, 50)))
        add.append(cyl(14, V(c + 8, 38, 7), V(c + 8, 90, 39)))
        add.append(cyl(14, V(c - 8, -38, 7), V(c - 8, -90, 39)))
        add.append(cyl(12, V(c + V_IN, 90, 72), V(c + V_IN, 40, 40)))
        add.append(box(c + V_IN - 24, c + V_IN + 24, 90, 93, 22, 78))       # intake flange pad
        add.append(box(c + V_EX - 22, c + V_EX + 22, -93, -90, 22, 78))     # exhaust flange pad
    for sx in (-1, 1):   # coolant bosses on the top face at both ends: reachable on 4-axis
        add.append(cyl(18, V(sx * (172 + DP), 80, 46), V(sx * (172 + DP), H_W / 2 + 5, 46)))
    pads = [((-181 - DP, -81, H_T), (0, 0, 1)), ((181 + DP, -81, H_T), (0, 0, 1)), ((0, 81, H_T), (0, 0, 1)),
            ((-150 - DP, -90, 95), (0, -1, 0)), ((150 + DP, -90, 95), (0, -1, 0)),
            ((-H_L / 2, 60, 95), (-1, 0, 0))]
    roles = ["primary 1", "primary 2", "primary 3", "secondary 1", "secondary 2", "tertiary"]
    PADS["H-201"] = [(r, (x, y, z), n, 20.0) for r, ((x, y, z), n) in zip(roles, pads)]
    for (x, y, z), n in pads:
        add.append(cyl(10, V(x, y, z - (PAD_PROUD if n[2] else 0)), V(x, y, z) + V(*n) * PAD_PROUD))
    s = fuse(s, add)
    # angled bosses overshoot the deck plane; clip to the head's envelope
    s = s.common(box(-H_L / 2 - 10, H_L / 2 + 10, -H_W / 2 - 5, H_W / 2 + 5, 0, H_T + 5))

    cuts = []
    for c in cs:
        cuts.append(cyl(CHAMBER / 2, V(c, 0, -0.1), V(c, 0, CHAMBER_D)))
        for xv, seat in ((c + V_IN, SEAT_IN), (c + V_EX, SEAT_EX)):
            p0 = V(xv, 0, CHAMBER_D)
            cuts.append(cyl(seat / 2, p0 - d * 1, p0 + d * 10))
            cuts.append(cyl(GUIDE / 2, p0 + d * 10, p0 + d * 85))
        cuts.append(cyl(PORT_IN / 2, V(c + V_IN, 5, 18), V(c + V_IN, 93.1, 51)))
        cuts.append(cyl(PORT_EX / 2, V(c + V_EX, -5, 18), V(c + V_EX, -93.1, 51)))
        cuts.append(cyl(PLUG / 2, V(c + 8, 38, 7), V(c + 8, 90.1, 39)))
        cuts.append(cyl(PLUG / 2, V(c - 8, -38, 7), V(c - 8, -90.1, 39)))
        cuts.append(cyl(INJ / 2, V(c + V_IN, 90.1, 72), V(c + V_IN, 40, 40)))
    for x, y in studs:
        cuts.append(cyl(6, V(x, y, -0.1), V(x, y, 80.1)))
    for x in (-1.5 * P, 1.5 * P):
        cuts.append(cyl(8, V(x, -STUD_Y, -0.1), V(x, -STUD_Y, 10)))           # ring dowels
    for sx in (-1, 1):
        cuts.append(cyl(11, V(sx * (172 + DP), 78, 46), V(sx * (172 + DP), H_W / 2 + 5.1, 46)))
    for x in (-0.5 * P, 0.5 * P):
        for y in (40, -40):
            cuts.append(cyl(4, V(x, y, -0.1), V(x, y, 23)))                    # coolant transfer [Q]
    s = cut(s, cuts)

    FEATURES["H-201"] = [
        ("datum A", "deck face, z = 0, machined in setup A (4-axis)", "flat 0.05 [E]"),
        ("datum B / C", f"ring-dowel counterbores 16 mm at x = +/-{1.5 * P:.1f}, y = {-STUD_Y}, symmetric so one part fits both banks", "H7"),
        ("rough datums", "3 pads on the rocker-cover rail, 2 on the exhaust (bottom) face, 1 on the front end face, 20 mm dia x 3 mm proud: setup A locates on these (table below)", "as cast"),
        ("valve axes", f"all six parallel, tilted {math.degrees(VALVE_TILT):.0f} deg toward the intake side in the y-z plane; inline along the row at x = c {V_IN:+.0f} (intake) and c {V_EX:+.0f} (exhaust), c in {cs}", "ruling 4: every axis normal to x"),
        ("seat-insert bores", f"intake {SEAT_IN} mm, exhaust {SEAT_EX} mm, 10 mm deep on the valve axis", "catalog insert press fit [Q]"),
        ("guide bores", f"{GUIDE} mm on the valve axis, through to the rocker box", "catalog guide press fit [Q]"),
        ("spark plugs", f"2 per cylinder, {PLUG} mm: set A from the top face at x = c + 8, set B from the bottom face at x = c - 8; each set parallel", "R-25, ruling 4"),
        ("injector bosses", f"3 x {INJ} mm from the top face into the intake port", ""),
        ("ports", f"intake {PORT_IN} mm to the top face, exhaust {PORT_EX} mm to the bottom face (opposite faces; see ruling 4)", ""),
        ("head studs", f"8 x 12 mm clearance at x = +/-{0.5 * P:.1f}, +/-{1.5 * P:.1f}; y = +/-{STUD_Y}", "matches H-101/102 deck"),
        ("coolant", f"22 mm bosses on the top face at x = +/-{172 + DP:.1f} (one plugged on each bank; they are also the two core-sand exits, ruling 7); 4 placeholder 8 mm deck transfer holes", "transfer holes [Q] with the liner"),
        ("chambers", f"3 x {CHAMBER} mm, {CHAMBER_D} mm deep (placeholder shape)", ""),
    ]
    return s


def report(name, label, s):
    bb = s.BoundBox
    ok = s.isValid() and len(s.Solids) == 1
    return dict(pn=name, label=label, valid=ok, solids=len(s.Solids),
                volume_l=s.Volume / 1e6, mass_kg=s.Volume * RHO,
                box_mm=[round(bb.XLength, 1), round(bb.YLength, 1), round(bb.ZLength, 1)])


def export(doc, pn, label, s):
    o = doc.addObject("Part::Feature", pn)
    o.Label = f"{pn} {label}"
    o.Shape = s
    Import.export([o], os.path.join(OUT, f"{pn}.step"))   # keeps the label as the STEP product name
    s.exportStl(os.path.join(OUT, f"{pn}.stl"))
    return o


def place_head(s, side):
    h = s.copy()
    if side == "LH":
        h.translate(V(cylinders("LH")[1], 0, DECK))
    else:
        h.rotate(V(0, 0, 0), V(0, 1, 0), 180)
        h.translate(V(cylinders("RH")[1], 0, -DECK))
    return h


doc = App.newDocument("concept_h")
parts = [("H-101", "Crankcase half LH, bank merged, A357-T6", case_half("LH")),
         ("H-102", "Crankcase half RH, bank merged, A357-T6", case_half("RH")),
         ("H-201", "Cylinder head, both banks, A356-T6", head())]
rep, objs = [], []
for pn, label, s in parts:
    objs.append(export(doc, pn, label, s))
    rep.append(report(pn, label, s))
hd = parts[2][2]
asm = [parts[0][2], parts[1][2], place_head(hd, "LH"), place_head(hd, "RH")]
aobj = []
for i, (s, lab) in enumerate(zip(asm, ("H-101", "H-102", "H-201 LH bank", "H-201 RH bank"))):
    o = doc.addObject("Part::Feature", f"asm{i}")
    o.Label = lab
    o.Shape = s
    aobj.append(o)
Import.export(aobj, os.path.join(OUT, "H-000_casting_set.step"))
Part.makeCompound(asm).exportStl(os.path.join(OUT, "H-000_casting_set.stl"))
clash = [round(asm[i].common(asm[j]).Volume, 1) for i, j in ((0, 1), (0, 2), (1, 3))]
bb = Part.makeCompound(asm).BoundBox

with open(os.path.join(OUT, "h_castings.json"), "w") as f:
    json.dump(dict(parts=rep, features=FEATURES, rough_pads=PADS, stock=STOCK, clash_mm3=clash,
                   set_box_mm=[round(bb.XLength, 1), round(bb.YLength, 1), round(bb.ZLength, 1)]), f, indent=1)

L = ["# Concept H casting set: part list (generated by `h_castings.py`; do not edit by hand)", "",
     "Coarse envelope models for quoting. Near-net as-machined shape; walls, ribs, the case perimeter flange and its",
     "bolts, oil cross-drillings, fillets and draft are not drawn. The foundry adds machining stock on every machined",
     "face to the ISO 8062 callout for each part below (stock per side = RMA + CT/2; plan on about 7 mm on the split",
     "face and the deck until the foundry states the grade it holds and the first-article layout shows less is enough).",
     "Route: binder-jet printed mold + foundry pour (envelope 1.2), degassed, T6 with a certificate, radiographed before",
     "first-op, impregnated after machining. Nothing here has been made or tested.", "",
     "| Part number | General tolerance and stock callout | Stock per side, CT10 / CT11 / CT12 (mm) | Plan on (mm) |",
     "|---|---|---|---|"]
for pn, (callout, band, plan, faces) in STOCK.items():
    L.append(f"| {pn} | `{callout}`; the RFQ asks the foundry which grade it holds, and its answer becomes the basis | {band} | {plan:.0f} on {faces} |")
L += ["",
     "| Part number | Description | Qty / engine | Material | Model box x/y/z (mm) | Model mass (kg) | STEP |",
     "|---|---|---|---|---|---|---|"]
for r in rep:
    qty = 2 if r["pn"] == "H-201" else 1
    mat = "A357-T6" if r["pn"] != "H-201" else "A356-T6"
    L.append(f"| {r['pn']} | {r['label']} | {qty} | {mat} | {' x '.join(str(v) for v in r['box_mm'])} | "
             f"{r['mass_kg']:.1f} | `{r['pn']}.step` |")
set_box = " x ".join(str(round(v, 1)) for v in (bb.XLength, bb.YLength, bb.ZLength))
L += ["", f"Casting set as assembled (`H-000_casting_set.step`, fit check only): {set_box} mm. "
      f"Overlap between mating parts in the model: {clash} mm^3 (case/case, case/head LH, case/head RH).", ""]
for pn in ("H-101", "H-102", "H-201"):
    L += [f"## {pn}: datums and critical features", "", "| Feature | Location and size | Fit / control |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in FEATURES[pn]]
    L += ["", f"### {pn}: rough datum pads (as cast; setup A, the foundry's first-article layout and the first-op fixture all use these)", "",
          "| Pad | Centre x, y, z (mm) | Face normal | Size | Height |", "|---|---|---|---|---|"]
    for role, c, n, d in PADS[pn]:
        L.append(f"| {role} | {', '.join(f'{v:.1f}' for v in c)} | {', '.join(f'{v:+.0f}' for v in n)} | {d:.0f} mm dia | "
                 f"{PAD_PROUD:.0f} mm proud of its as-cast face; every pad in the set at this one height |")
    L += ["", "All pads are cast in the same mould half as the face they stand on, kept off the parting line and the gates "
          "[Q: the foundry places the parting line and gates, then confirms]. The secondary and tertiary pads stand on walls drafted "
          "about 2 deg, so their stated height is what stops the draft moving the part in x-y at setup (AMC/ATI casting GD&T tip, via MANUFACTURING).", ""]
with open(os.path.join(OUT, "PART_LIST.md"), "w") as f:
    f.write("\n".join(L))
print(json.dumps(dict(parts=rep, clash_mm3=clash), indent=1))
