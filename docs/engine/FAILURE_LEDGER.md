# Engine failure-mode ledger, v0 (seed)

Owner: PROPULSION, holding it for SAFETY, which is paused (ORG-009). Issues: AER-3320 (seed), AER-3326 (phase 1: FL-24 to FL-29).

This is a seed, not a hazard analysis. It records every single failure that phase 0 raised and what each leaves the pilot, so SAFETY inherits a list when it resumes. Nothing here has been tested. "Leaves" is a design intent or a physics expectation, not a demonstrated result.

| ID | Item | Single failure | What it leaves the pilot | Source / owner of the fix |
|---|---|---|---|---|
| FL-1 | Reduction drive (concepts B, C, E, G; drive options 2, 5) | gearbox, quill shaft or spline failure | total loss of thrust | DRIVE_AND_PROP.md option 2; NTSB ERA14LA130, NYC95LA137 |
| FL-2 | Reduction drive | first torsional mode inside the firing band | fatigue failure of shaft, spline or crank, which becomes FL-1 | DRIVE_AND_PROP.md torsional window; a plain quill shaft lands inside the band |
| FL-3 | CVT (option 4) | belt or variator failure | total loss of thrust | DRIVE_AND_PROP.md option 4 |
| FL-4 | CVT (option 4) | ratio frozen | fixed ratio: weak climb, or throttled cruise | DRIVE_AND_PROP.md option 4 |
| FL-5 | Two-speed gearbox (option 5) | shift fails into neutral | total loss of thrust; the design must not allow neutral | DRIVE_AND_PROP.md option 5 |
| FL-6 | In-flight adjustable propeller (option 6) | pitch runaway fine / coarse | overspeed (throttle back) / weak climb; the design must fail frozen | DRIVE_AND_PROP.md option 6 |
| FL-7 | Constant-speed propeller (option 7) | oil-pressure loss to a single-acting hub | goes to fine: full power, overspeed risk at speed | DRIVE_AND_PROP.md option 7 |
| FL-8 | FADEC-governed electric pitch (option 9) | both lanes or actuator lost | must freeze at last pitch; the FADEC becomes propeller-critical | DRIVE_AND_PROP.md option 9; REQUIREMENTS R-25 |
| FL-9 | Self-adjusting governing hub (option 8a) | hub stuck | fixed pitch at stuck pitch, undetectable in flight | DRIVE_AND_PROP.md option 8 |
| FL-10 | FADEC / ignition | one lane lost | at least 90 % MCP, no pilot action (requirement R-25, untested) | REQUIREMENTS R-25 |
| FL-11 | Coolant pump | single pump failure | at least 5 min at MCP, then 50 % power (requirement R-23, untested); a single electric pump does not meet it | REQUIREMENTS R-23; MANUFACTURING envelope section 4 |
| FL-12 | Knock on low-octane or high-ethanol fuel | wrong fuel or fuel-map selection | detonation damage: piston, ring land, head gasket. Mitigation: pilot fuel map, knock sensing as backstop (R-13) | REQUIREMENTS R-12/R-13; ARCHITECTURES concept A |
| FL-13 | Fuel system, ethanol | vapor lock in a hot-day climb | power loss or stoppage; designed out by tank-pressurized fuel (R-16) | REQUIREMENTS R-16 |
| FL-14 | 100LL on a closed-loop FADEC | lead-poisoned O2 sensor | wrong mixture if the FADEC trusts it; must run open-loop on 100LL (R-17) | REQUIREMENTS R-17 |
| FL-15 | Structural casting (case, head) | porosity behind an oil gallery or bearing web | oil loss or web crack | MANUFACTURING envelope section 7, item 1 |
| FL-16 | Structural casting | unverified T6 | low fatigue strength in case or head | MANUFACTURING envelope section 7, item 2 |
| FL-17 | Main bearing bores | misalignment across case halves | bearing distress | MANUFACTURING envelope section 7, item 3 |
| FL-18 | Liners | wrong interference or protrusion | head-gasket leak, coolant in oil | MANUFACTURING envelope section 7, item 4 |
| FL-19 | Builder-cut valve seats | wrong width or concentricity | burnt valve, which is a cylinder loss | MANUFACTURING envelope section 7, item 5 |
| FL-20 | Diesel head and case (concept E) | peak-pressure fatigue in sand-cast A356-T6 | head-gasket or deck failure, which is power loss | ARCHITECTURES concept E; open MANUFACTURING question |
| FL-21 | Radial master/link rods (concept D) | link-pin or master-rod fatigue | catastrophic engine failure | ARCHITECTURES concept D |
| FL-22 | Wankel apex seals (concept G) | seal failure | progressive power loss on one rotor | ARCHITECTURES concept G |
| FL-23 | Turbocharger / wastegate (A, B, C, E, F, G) | wastegate stuck closed / open | overboost (FADEC must cut fuel or spark) / loss of altitude power only | ARCHITECTURES normalizing; phase 1 |
| FL-24 | Crank, concept H (direct-drive flat-6) | crank first torsional mode (about 260 Hz) meets the 6th firing order at about 2,600 rpm, inside the cruise band | crank or crank-nose fatigue crack; a crank failure is a total loss of thrust. Mitigation: a 6th-order pendulum damper or a published restricted-rpm band, then a dynamometer torsional survey before flight | RANKING_PHASE1.md section 6; `torsional_h.py` (assumed stiffnesses, +/-20 %) |
| FL-25 | Crank pendulum damper (if FL-24 is fixed that way) | bushing or pin wear detunes the damper | FL-24 returns, without a cockpit cue. Mitigation: an inspection interval on the damper pins and bushings, set at the first teardown (R-41) | RANKING_PHASE1.md section 6 |
| FL-26 | Intercooler (concept H, all turbo concepts) | intercooler leak, bypass or blockage at altitude | charge at about 76 C at 12,000 ft ISA+20, which is about 0.9 of a point of knock-limited CR lost. The FADEC must see the charge temperature (IAT after the cooler) and derate spark or boost; knock sensing is the backstop (R-13) | RANKING_PHASE1.md section 3; `knock.py` |
| FL-27 | Coolant loop, fully liquid-cooled cylinders (R-21) | loss of coolant: hose, radiator core or liner seal | lumped estimate: about 1 minute at MCP and about 2 minutes at 50 % power before the metal climbs 100 K (about 70 kJ/K of engine metal against 109 kW at MCP). Air-cooled cylinders would keep some margin; fully jacketed ones do not. The pilot needs a coolant-pressure or level annunciation, not just temperature | RANKING_PHASE1.md section 8; estimate, not a test |
| FL-28 | Radiator duct | blocked inlet (bird, debris) or a closed cowl flap at climb | coolant overheat at MCP; reduce power and raise speed. The ram-air margin at 70 KIAS is the design margin (core plus duct loss under the free-stream dynamic pressure) | `radiator.py` |
| FL-29 | Ground-adjustable propeller (drive pick 3b) | blade-retention clamp torque loss | blade pitch change or blade release: a vibration emergency. Mitigation: clamp torque on the condition-inspection list (R-39) and a witness mark | DRIVE_AND_PROP.md option 3; RANKING_PHASE1.md section 7 |
