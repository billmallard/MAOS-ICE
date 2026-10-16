"""Bottom-up first-article parts-and-services cost floor per concept (AER-3320).

Builder labor excluded. Low/high band in 2026 USD. Each line is tagged:
  [S-MFG] sourced in MANUFACTURING envelope v0 (AER-3321, read 2026-10-16)
  [E]     PROPULSION estimate, method in the comment
  [Q]     unquoted; the band is a placeholder until MANUFACTURING quotes it
This is a first-article floor for ranking in phase 1, not a price.

Run: python3 cost_floor.py
"""

FAMILY_HP = (100, 200, 300)

# per-cylinder catalog set (piston, rings, rod, shells, valves, springs, injector, coils)
PER_CYL = {
    "SI": (450, 750),         # [S-MFG] section 4 sanity check
    "CI": (700, 1100),        # [E] SI set + common-rail injector (~$250-350) - spark coils
    "OP": (900, 1800),        # [Q] two custom port-controlling pistons, rods, liner with ports
    "ROT": (1800, 3000),      # [Q] 13B-class rotor, rotor housing, apex/side seals per rotor, aftermarket
}
DUAL_LANE_PER_CYL = (50, 100)        # [S-MFG] second D585-class coil per cylinder (~$48-51), SI only
CRANK = (3400, 6300)                 # [S-MFG] custom billet 4340, Crower/Bryant/Moldex
CASE_HALF = (1000, 2500)             # [S-MFG worked example, E] bureau mold + pour + T6 + impregnation
FIRST_OP = (500, 2000)               # [Q] job-shop first-op per casting
HEAD = (500, 1200)                   # [E] bureau rate scaled to a ~1/3-volume casting, plus T6/impreg
SEATS_GUIDES_PER_CYL = (100, 250)    # [S-MFG] valve work line items, per cylinder
LINER_PER_CYL = (150, 400)           # [S-MFG] Darton set ~$600/4 plus install share
CAM = (500, 1500)                    # [Q] donor/regrind/custom billet cam
MACHINE_SHOP = (800, 2000)           # [S-MFG] align hone, decks, balance; x1.3 for 2026 applied below
FADEC = (1500, 4000)                 # [E] two lanes: 2x ECU (Speeduino ~$440 pair to SDS ~$2.4k pair, ENGINE_MGMT_CANDIDATE_MATRIX_V1) + sensors + harness
NORM = {"turbo": (1200, 3000), "sc": (1500, 3500), "none": (0, 0)}   # [E]
COOLING_PER_100KW = (500, 1200)      # [E] radiator + EWP115 ($225 [S-MFG]) + oil cooler + hoses
START_ALT = (400, 900)               # [E] catalog automotive starter + alternator
DRIVE = {"direct": (300, 800), "gear": (1500, 5000), "optrain": (2500, 6000)}  # [Q] catalog gears+case+bearings+soft coupling
FUEL = {"SI": (400, 800), "CI": (1200, 2500), "OP": (1200, 2500), "ROT": (400, 800)}  # [E] CI adds HP pump + rail
EXHAUST = (300, 800)                 # [E]
MISC = (600, 1500)                   # [E] gaskets, fasteners, oil pump, filters, seals

# concept: cycle, cylinders per member, heads per member, cams per member,
# crank multiplier (throws / extra cranks), case scale per member, norm, drive
CONCEPTS = {
    "A": dict(cy="SI", n=(2, 4, 6), heads=(2, 4, 6), cams=(1, 1, 1), crank=(0.8, 1.0, 1.2), case=(0.8, 1.0, 1.4), norm="turbo", drive="direct"),
    "B": dict(cy="SI", n=(4, 8, 12), heads=(2, 4, 6), cams=(2, 4, 6), crank=(0.8, 1.1, 1.4), case=(0.6, 0.9, 1.2), norm="turbo", drive="gear"),
    "C": dict(cy="SI", n=(2, 4, 6), heads=(2, 4, 6), cams=(1, 1, 1), crank=(0.7, 0.8, 1.0), case=(0.6, 0.9, 1.2), norm="turbo", drive="gear"),
    "D": dict(cy="SI", n=(3, 7, 9), heads=(3, 7, 9), cams=(1, 1, 1), crank=(1.0, 1.1, 1.2), case=(0.8, 1.1, 1.3), norm="sc", drive="direct"),
    "E": dict(cy="CI", n=(3, 6, 8), heads=(1, 2, 2), cams=(2, 4, 4), crank=(0.8, 1.1, 1.3), case=(0.7, 1.0, 1.4), norm="turbo", drive="gear"),
    "F": dict(cy="OP", n=(2, 4, 6), heads=(0, 0, 0), cams=(0, 0, 0), crank=(1.6, 2.0, 2.4), case=(0.8, 1.1, 1.4), norm="turbo", drive="optrain"),
    "G": dict(cy="ROT", n=(2, 4, 6), heads=(0, 0, 0), cams=(0, 0, 0), crank=(0.8, 1.2, 1.6), case=(0.4, 0.6, 0.8), norm="turbo", drive="gear"),
}
# coolant+oil heat per member (kW) from engine_floor.py; SI ~0.87 P, CI ~0.70 P, OP 0.59 P, ROT 1.4 P
HEAT = {"SI": (78, 156, 234), "CI": (52, 104, 156), "OP": (43, 88, 131), "ROT": (104, 207, 311)}


def add(t, rng, k=1.0):
    return (t[0] + rng[0] * k, t[1] + rng[1] * k)


def member(c, i):
    t = (0.0, 0.0)
    n = c["n"][i]
    t = add(t, PER_CYL[c["cy"]], n)
    if c["cy"] == "SI":
        t = add(t, DUAL_LANE_PER_CYL, n)
    if c["cy"] in ("SI", "CI"):
        t = add(t, LINER_PER_CYL, n)
        t = add(t, SEATS_GUIDES_PER_CYL, n)
    t = add(t, CRANK, c["crank"][i])
    t = add(t, CASE_HALF, 2 * c["case"][i])
    castings = 2 + c["heads"][i]
    t = add(t, FIRST_OP, castings)
    t = add(t, HEAD, c["heads"][i])
    t = add(t, CAM, c["cams"][i])
    t = add(t, MACHINE_SHOP, 1.3)
    t = add(t, FADEC)
    t = add(t, NORM[c["norm"]])
    t = add(t, COOLING_PER_100KW, HEAT[c["cy"]][i] / 100)
    t = add(t, START_ALT)
    t = add(t, DRIVE[c["drive"]])
    t = add(t, FUEL[c["cy"]])
    t = add(t, EXHAUST)
    t = add(t, MISC)
    return t


if __name__ == "__main__":
    print("| Concept | 100 hp | 200 hp | 300 hp |")
    print("|---|---|---|---|")
    for k, c in CONCEPTS.items():
        cells = [f"${member(c, i)[0]/1000:.0f}k - ${member(c, i)[1]/1000:.0f}k" for i in range(3)]
        print(f"| {k} | " + " | ".join(cells) + " |")
