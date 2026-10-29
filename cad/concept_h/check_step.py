import Part
for pn in ("H-101","H-102","H-201"):
    s=Part.read(OUT+'/'+pn+'.step')
    print(pn, s.isValid(), len(s.Solids), [ (round(x.Volume/1e3,1), tuple(round(v) for v in x.CenterOfMass)) for x in s.Solids])
