import Part, json, math
from FreeCAD import Vector as V
OUT = globals().get("OUT")
crank = Part.read(OUT + "/H-301.step")
cases = {pn: Part.read(OUT + "/" + pn + ".step") for pn in ("H-101", "H-102")}
res = {}
for a in range(0, 360, 15):
    c = crank.copy(); c.rotate(V(0, 0, 0), V(1, 0, 0), a)
    res[a] = {pn: round(c.common(s).Volume, 1) for pn, s in cases.items()}
worst = max(max(v.values()) for v in res.values())
bb = crank.BoundBox
out = dict(angles_deg=list(range(0, 360, 15)), overlap_mm3=res, worst_mm3=worst,
           crank_x=[round(bb.XMin, 1), round(bb.XMax, 1)])
print(json.dumps(out))
json.dump(out, open(OUT + "/crank_in_case.json", "w"), indent=1)
