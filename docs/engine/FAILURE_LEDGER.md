# Engine failure-mode ledger, v0 (seed)

Owner: PROPULSION, holding it for SAFETY, which is paused (ORG-009). Issue: AER-3320.

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
