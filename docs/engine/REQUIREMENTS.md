# Engine family requirements, v0 (draft)

Owner: PROPULSION. Issue: AER-3320 (engine program phase 0, ORG-009, 2026-10-16).
Status: **draft. Bill ruled on the four phase-0 card calls on 2026-10-16 (section 12); everything else is still open.** This is an
experimental engine design. Nothing in it is certified, certifiable or
flight-ready, and nothing in it has been built or tested.

## How to read this

Every requirement carries one tag:

- **[BRIEF]**: Bill's brief of 2026-10-16, as carried in the PROPULSION profile
  ("Why this engine exists"). The ORG-009 decision file
  (`makerplane/decisions/ORG-009-engine-program-and-airframe-pause.md`) was
  **not readable this pass**: it is not on `maos-workspace` main on GitHub
  (ORG-001 to ORG-008 only, checked 2026-10-16). The brief text is therefore
  the profile copy. If ORG-009 differs, ORG-009 wins and this file is updated.
- **[PROPOSED]**: PROPULSION's proposal. It stands until Bill confirms or
  corrects it. Where it is one of the four questions on the phase-0 card, it
  says **(card)**.
- **[BILL RULED 2026-10-16]**: Bill accepted the phase-0 card (section 12).
  Only the scope the card carried is ruled; the rest of the line stays
  [PROPOSED].

Numbers come from four places, each named where used:

- `analysis/engine_phase0/` scripts in this repo: physics floor, prop match,
  torsional window and cost floor. Rerun commands are in that folder's README.
- `sources/COMPARABLE_ENGINES_2026-10-16.md`: vendor data, read 2026-10-16.
- `sources/PROP_AND_DRIVE_SOURCES_2026-10-16.md`: prop and drive hardware,
  read 2026-10-16.
- `MANUFACTURING_ENVELOPE.md`: MANUFACTURING's envelope v0 (AER-3321).

## 1. Family and ratings

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-1 | A family at **100, 200 and 300 hp**, scaled by adding cylinders around common parts (a shared cylinder, head, piston and valvetrain module, or better). | BRIEF | |
| R-2 | The family number is **takeoff power**: 5 minutes, sea-level ISA, measured **at the propeller flange**, so reduction-drive losses are inside it. | PROPOSED | Rotax rates 912 ULS at 100 hp takeoff for 5 min [R1][R3] |
| R-3 | **Maximum continuous power (MCP) at least 90 % of takeoff**: 90 / 180 / 270 hp. | PROPOSED | MCP/takeoff is 94 % on the 912 ULS (69/73.5 kW), 86 % on the 916 iS (101/117 kW), 92.5 % on the UL520iS (185/200 hp) [sources]. Rating takeoff equal to continuous, Lycoming-style, costs about 10 % more displacement for the same family number. |
| R-4 | **Duty cycle for design and test**: takeoff 5 min; climb at MCP up to 30 min; cruise at 55-75 % power for multi-hour legs, the dominant share of engine hours; descent at low power without shock cooling (liquid cooling helps here). No aerobatic or inverted-oil requirement in v0. | PROPOSED | GA practice; no airframe exists (MAOS paused, ORG-009) |

## 2. Normalizing and critical altitude

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-5 | **Normalized, not boosted.** A turbocharger or supercharger holds sea-level power against density altitude. It does not raise rated power. | BRIEF | |
| R-6 | Reading of R-5 for spark ignition: manifold pressure at rated power is **no more than about 1.0 bar absolute at sea level**, so rated BMEP stays naturally-aspirated class (about 10-11.5 bar). The compressor exists to hold that manifold pressure to the critical altitude. | PROPOSED | `engine_floor.py`; see ARCHITECTURES.md |
| R-7 | **Critical altitude (card): MCP held to 12,000 ft density altitude; takeoff power held to 8,000 ft density altitude.** | BILL RULED 2026-10-16 | Covers hot-day takeoff from high-elevation fields and a useful cruise band. Cost per altitude in the table below. |
| R-8 | Reading of R-5 for diesel: **R-5 as written makes diesel uneconomic.** Holding a diesel to 1 bar manifold doubles displacement and roughly doubles mass. The proposal: a diesel may run its turbocharger at sea-level boost as part of its combustion system, and normalizing applies on top. **This is a relaxation of the brief and is on the card.** | PROPOSED | Finding F-1 below |

Normalizing cost versus critical altitude (200 hp spark-ignition member, ISA, compressor efficiency 0.70, 1.08 bar manifold target, from `engine_floor.py`):

| Critical altitude | Pressure ratio | Compressor work | Share of rated power | Compressor outlet, ISA |
|---|---|---|---|---|
| 8,000 ft | 1.43 | 6.8 kW | 4.5 % | 41 C |
| 12,000 ft | 1.68 | 9.6 kW | 6.4 % | 51 C |
| 16,000 ft | 1.97 | 12.5 kW | 8.4 % | 61 C |

With a turbocharger, the exhaust supplies this work. It costs back-pressure (pumping work) and adds a wastegate loop to the FADEC. With a mechanical supercharger, it comes off the crankshaft: the engine must make the table's share of extra gross power at altitude, or lose it. On an ISA+20 C day, outlet temperature rises by about 25 C. Above roughly 12,000 ft on a hot day, that calls for an intercooler or a knock-limited derate. This is an estimate to verify in phase 1.

## 3. Fuel

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-9 | **Diesel is preferred but Bill suspects it is harder to execute; US auto gas in the 80-96 octane range is acceptable; ethanol must be tolerated.** | BRIEF | |
| R-10 | **First family member's fuel: auto gas.** Diesel concepts stay in ARCHITECTURES.md for later family members; R-8 is not ruled. | BILL RULED 2026-10-16 | card item 1; ARCHITECTURES.md carries both |
| R-11 | **Octane scale.** The fuel requirement is written in **AKI, (RON+MON)/2**: the number posted on US pumps (ASTM D2699: the antiknock index "in accordance with Specification D4814" is what is "posted on retail dispensing pumps in the U.S." [E6]). Knock margin is **designed and verified against MON**, because sustained full-throttle aircraft duty is the severe, MON-like case. Rotax and UL Power already specify a MON floor (MON 85 and MON 88). | PROPOSED | [R3][R4][U1] |
| R-12 | **Rated power on 91 AKI (MON 85 or better), E0-E15.** This is the same floor as the Rotax 912/915/916 (min AKI 91 / RON 95 / MON 85 [R3][R5]). | PROPOSED | |
| R-13 | **Safe continuous operation on 87 AKI E10** at a published derate of **no more than 10 % of rated power**, through a pilot-selected fuel map, with knock sensing as a backstop, not as the primary protection. | PROPOSED | Alternative for Bill: rate the engine on 87 AKI. That costs about one point of compression ratio, which is about 3-4 % more fuel burn (ideal Otto efficiency at 9:1 versus 8:1 is 0.585 versus 0.565, Heywood ch. 5). |
| R-14 | Bill's "80-96": **80 AKI is not a US pump grade**. The lowest common grades are 85-86 AKI at altitude in mountain states. The proposal reads Bill's range as "regular through premium". | PROPOSED | the 87/89/91/93 ladder was *not* verified from a primary source; ASTM D4814 Appendix X1 is paywalled [E5] |
| R-15 | **Ethanol: full tolerance E0 to E15** at rated power. E15 is the highest blend sold for general road vehicles (EPA: 10.5-15 %, 2001-and-newer vehicles [E1]). Every fuel-wetted part must be E15-compatible: FKM or PTFE elastomers, stainless or anodized aluminum, no natural rubber or cork, no fibreglass tanks (Jabiru prohibits alcohol in its fibreglass tanks [J3]). FADEC closed-loop lambda compensates the stoichiometric shift (about 14.7 for E0, 14.1 for E10, 13.8 for E15, by mass-weighted mixing of 14.7 and 9.0). **E85 is not required**: it needs about 40 % more fuel flow and costs about 27 % of range by energy per litre. | PROPOSED | [E1][J3]; stoichiometry by method stated |
| R-16 | Ethanol raises vapor pressure. The fuel system is **pressurized from the tank** (tank-mounted pump, return line) so vapor lock in a climb on a hot day is designed out, not managed. | PROPOSED | |
| R-17 | **100LL** tolerated as an occasional alternate. Lead poisons wideband O2 sensors, so the FADEC must run open-loop on 100LL. Oil-change interval is shortened on leaded fuel (Rotax-style practice; interval to be set). | PROPOSED | |
| R-18 | If diesel: **Jet A, Jet A-1, JP-8 and EN 590 / ASTM D975 No. 2 diesel**, as the Continental CD-135 accepts [D4]. Ethanol does not apply. | PROPOSED | [D4] |
| R-19 | Year-round E15 is **not settled law**. Summer sale still runs on emergency waivers, and the House passed H.R. 1346 in May 2026 with no Senate passage found [E2][E3][E4]. R-15 covers E15 whether or not it becomes year-round, so no change is needed either way. | PROPOSED (watch item) | |

## 4. Cooling

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-20 | **Liquid cooled.** | BRIEF | |
| R-21 | Heads **and** cylinders liquid-cooled. The Rotax 912/915/916 cools heads by liquid and cylinders by air [R1]; the proposal is fully liquid-cooled. Pressurized glycol-water; waterless coolant as a builder option. | PROPOSED | |
| R-22 | Size the radiator for **MCP continuous at Vy climb on an ISA+20 C sea-level day**. Heat to coolant and oil at takeoff, by family member and cycle, from `engine_floor.py` (Heywood ch. 12 energy-balance fractions): | PROPOSED | |

| Member | Spark ignition: coolant / oil | Diesel 4-stroke: coolant / oil |
|---|---|---|
| 100 hp | 65 / 13 kW | 40 / 12 kW |
| 200 hp | 129 / 27 kW | 80 / 24 kW |
| 300 hp | 194 / 40 kW | 120 / 36 kW |

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-23 | **Coolant-pump failure** must leave at least **5 minutes at MCP and a continued flight at 50 % power**. The proposal is either a mechanical primary pump, or two electric pumps on separate feeds. One electric pump alone does not meet this. MANUFACTURING lists an electric pump (EWP115, $225) as a part-count win and flagged its failure mode for this ledger. | PROPOSED | envelope section 4 |

## 5. Ignition and engine management

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-24 | **Dual-lane electronic ignition. Computer engine management (FADEC).** | BRIEF | |
| R-25 | **Two independent lanes**: two spark plugs per cylinder (spark ignition), two coils, two ECUs, two crank-position sensors, two power feeds, and no shared single connector. **Any single electrical or electronic failure leaves at least 90 % of MCP**, with no pilot action needed to keep the engine running. | PROPOSED | the old ECU matrix found true dual-lane impossible on a converted Hayabusa (`docs/ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` section 4); a clean-sheet engine can provision it from the start |
| R-26 | **Single power lever.** The FADEC owns mixture, spark timing, wastegate or supercharger bypass, and propeller rpm if a variable-pitch propeller is chosen. | PROPOSED | |
| R-27 | Engine data and annunciations are published to pyEfis over **CAN-FIX** from day one. The key set is a later handoff to AVIONICS, not part of phase 0. | PROPOSED | |

## 6. Made from files

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-28 | **Every part is printed, cut, cast from a printed mold, machined by an off-the-shelf service, or bought off the shelf.** | BRIEF | |
| R-29 | **Structural castings (crankcase, cylinder module, head) come from a binder-jet bureau or a foundry pouring a printed pattern**, in A356/A357-T6, X-rayed or pressure-tested, and impregnated. Hobby casting is limited to covers, plenums and fit-check prototypes. | PROPOSED | MANUFACTURING envelope finding 3 |
| R-30 | **Precision lives on catalog parts** (liners, bearing shells, seat inserts, guides). Bore, stroke, rod length, valve size and head-gasket bore are picked from catalog families. | PROPOSED | envelope findings 2 and 4 |
| R-31 | One local job-shop first-op machining step per casting is accepted. AeroCommons publishes a shared fixture set so repeat engines get cheaper. | PROPOSED | envelope finding 1 and section 2.2 |
| R-32 | **Ease of assembly and maintenance are primary. Fewer parts. Substantially lower cost.** | BRIEF | |
| R-33 | **A cylinder module can be replaced without splitting the crankcase or removing the engine.** Target: no more than 4 hours, B1 builder skill. | PROPOSED | the 4 hours is a target with no comparator found yet |
| R-34 | Part count is a tracked design output per family member. No numeric target in v0, because no sourced part count for a comparable engine was found; phase 1 sets it. | PROPOSED | |

## 7. Cost per family member

**Definition (proposed):** first-article parts-and-services cost to the builder, 2026 USD, **excluding builder labor and the propeller**. It includes the reduction drive, normalizing, FADEC, starter, alternator, radiator and exhaust.

Comparable engines (price as read 2026-10-16; source keys in `sources/COMPARABLE_ENGINES_2026-10-16.md`):

| Class | Engine | Price, USD | Basis |
|---|---|---|---|
| 100 hp | Aeromomentum AM15 (120 hp, incl. gearbox, starter, alternator, ECU) | 13,000-14,100 | vendor [A1] |
| 100 hp | Viking 130 (no radiator or exhaust) | 15,000 | vendor [V3] |
| 100 hp | Rotax 912 ULS | 26,498 | Australian dealer snippet, page unopened, currency basis not stated [R7] |
| 100 hp | Continental O-200-D, UL260iS, Jabiru 2200 | not found | "contact us" or no list |
| 150-200 hp | Rotax 915 iS / 916 iS | 51,591 / 59,381 | Australian dealer snippet, ex-GST [R7] |
| 180 hp | Lycoming O-360-A1F6, factory new | 87,668 + 30,000 core | Air Power [L4] |
| 300 hp | Continental IO-550-D, new | 67,578 + 22,000 core | Air Power [C4] |
| 300 hp | Lycoming IO-540-K1A5, new | 124,826 + 36,000 core | Air Power [L5] |
| 150 hp diesel | Continental CD-155 | 47,515 (2018 list) | AOPA [D11] |
| 180 hp diesel | DeltaHawk DHK180 | 60,000 (target, press) | Kitplanes [D13] |

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-35 | **Cost targets (card): 100 hp no more than $15k; 200 hp no more than $22k; 300 hp no more than $30k**, first article, as defined above. | BILL RULED 2026-10-16 for 200 hp and 300 hp; 100 hp PROPOSED (not on the card) | about one quarter of the certified engine at 300 hp; parity with the cheapest conversion at 100 hp |
| R-36 | **Finding F-2: at 100 hp no concept meets R-35 at first article.** The cost floor (`cost_floor.py`) is **$15k-47k at 100 hp, $20k-68k at 200 hp and $26k-86k at 300 hp** across the seven concepts. The fixed lines (billet crank, cases, first-op machining, FADEC, turbo) are about 60 % of the bill at 100 hp and do not shrink with cylinder count. **"Substantially lower cost" holds at 200-300 hp and fails at 100 hp** against a $13-14k automotive conversion. This is on the card. | PROPOSED | cost_floor.py; the high end is driven by the unquoted job-shop first-op line [Q] |

## 8. Mass per family member

**Definition (proposed):** "installed dry". This is the engine with reduction drive, normalizing system, FADEC, starter, alternator and exhaust. It excludes fluids, radiator and propeller. The radiator and coolant are a separate line, because they scale with the airframe's cooling design.

Comparables (vendor definitions differ; read 2026-10-16):

| Class | Engine | Dry mass |
|---|---|---|
| 100 hp | Rotax 912 ULS (with gearbox) / 912 iS Sport | 56.6 / 63.6 kg [R1][R4] |
| 100 hp | UL260iS dry / ready to fly | 60.1 / 72.9 kg [U1] |
| 100 hp | Continental O-200-D (all accessories) | 89.3 kg [C1] |
| 100-120 hp | Aeromomentum AM15 / Viking 130 | 83.9 / 99.8 kg [A1][V1] |
| 140-160 hp | Rotax 915 iS / 916 iS (incl. gearbox, turbo, intercooler, exhaust) | 82.2 / 85.8 kg [R5][R6] |
| 180 hp | Lycoming O-360-A1A (incl. accessories, baffles) | 131.5 kg [L1] |
| 180 hp | Jabiru 5100 | 117 kg [J4] |
| 200 hp | UL520iS dry / ready to fly | 93.3 / 108 kg [U4] |
| 300 hp | Lycoming IO-540-K1A5 / Continental IO-550-D | 212.7 / 209.4 kg [L2][C2] |
| diesel | CD-135/155 (incl. gearbox, turbo, FADEC) / AE300 / SMA SR305 | 134 / 185 / 195 kg [D3][D6][D14] |

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-37 | **Installed dry mass no more than 90 kg (100 hp), 150 kg (200 hp), 210 kg (300 hp).** That is no heavier than the certified air-cooled engine of the same power, like for like, with a stretch goal of within 25 % of the Rotax/UL class. | PROPOSED | the physics-floor estimates in ARCHITECTURES.md run from 72 kg (concept B, 100 hp) to 271 kg (concept E, 300 hp), +/-25 %; several concepts miss at 300 hp. Phase 1b: concept H on sourced liners and normalizer is about 148-158 kg at 200 hp, at the limit (RECOST_PHASE1B.md section 7) |
| R-38 | Radiator, coolant and oil cooler installed system: carried as a separate line. Phase 0 bounded it at 3.7-27 kW per kg of rejected heat (about 6-42 kg at 200 hp). **Phase 1 sizing at R-22's case (MCP, Vy assumed 80 KIAS, sea level ISA+20 C): about 26 kg (22.8-29.6 kg across core geometries), a 2,890 cm^2 radiator and an 880 cm^2 oil cooler at 50 mm core depth, with 1.3 % of MCP in cooling drag.** The 12,000 ft ISA+20 C case needs about 20 % less face, so sea level is the sizing case. | PROPOSED | `analysis/engine_phase1/radiator.py`; RANKING_PHASE1.md section 8 |

## 9. Inspection and overhaul

Comparables (read 2026-10-16):

| Engine | TBO |
|---|---|
| Rotax 912 ULS / 912 iS / 916 iS | 2,000 h [R2][R4][R6] |
| Rotax 915 iS | **1,200 h** [R5] |
| UL Power (serials 250000 and up) | 2,000 h / 12 yr; below that serial, 1,500 h [U5] |
| Jabiru 2200 / 3300 | 2,000 h, top-end inspection at 1,000 h [J3] |
| Continental O-200-D / IO-550-D | 2,200 h / 1,900 h, 12 yr [C1][C2] |
| Lycoming O-360 / IO-540-K | 2,600 h factory new, 2,000 h after overhaul, 12 yr (SI 1009BF, 2026-07-20) [L3] |
| CD-135 / CD-155 | 2,100 h TBR, 12 yr [D1][D4] |
| Austro AE300 / AE330 | 1,800 h [D8][D9] |
| SMA SR305-230 | 2,400 h (press) [D15] |
| Rotax inspection | 100 h or 12 months (owner forum citing the maintenance manual, not the manual itself) [R8] |

| ID | Requirement | Tag | Basis |
|---|---|---|---|
| R-39 | **Condition inspection every 100 h or 12 months**: borescope every cylinder, oil analysis, differential compression or leak-down, FADEC fault-log download. | PROPOSED | experimental-amateur norm; Rotax 100 h / 12 mo [R8] |
| R-40 | **Design-life target 2,000 h TBO**, at parity with Rotax 912 / UL / Jabiru / CD-135. | PROPOSED | |
| R-41 | **The operating interval starts provisional, not at 2,000 h.** Lead engines get teardown inspections at 25, 100 and 300 h, then extend on condition in fleet steps. A new engine type earns its TBO; it is not assigned one. | PROPOSED | honest state: there are zero hours on any of this |

## 10. Excluded and deferred

| ID | Requirement | Tag |
|---|---|---|
| R-42 | **Not electric, for now.** Track solid-state cells past 400 Wh/kg (Bill expects about two years). Do not design for them. | BRIEF |
| R-43 | **The propeller is a named constraint.** Evaluate a transmission (CVT or otherwise) and every alternative. See DRIVE_AND_PROP.md. | BRIEF |
| R-44 | No airworthiness claim of any kind. Experimental-amateur-built context; untested designs are labeled untested. | PROPOSED (standing rule) |
| R-45 | Phase 0 excludes CAD, part drawings, the FADEC design and the SAFETY review. SAFETY is paused, so PROPULSION keeps the failure ledger (`FAILURE_LEDGER.md`). | from AER-3320 |

## 11. Findings: brief requirements that make the problem unsolvable or uneconomic

These go to Bill on the phase-0 card. Each states what relaxing it buys.

| ID | Requirement it bends | Finding | What relaxing it buys |
|---|---|---|---|
| **F-1** | R-5 normalized-not-boosted, applied to diesel | Literally normalized, a 4-stroke diesel runs about 7.5 bar BMEP, so 100 hp needs 3.0 L and 6 cylinders (concept E-NA). At about 15-17 bar with sea-level boost it needs 1.5 L and 3 cylinders. | About **80 kg at 100 hp, 140 kg at 200 hp and 230 kg at 300 hp**, and half the cylinders (E versus E-NA, `engine_floor.py`, +/-25 %). Without the relaxation, a diesel family is heavier than an IO-540 at 200 hp. |
| **F-2** | R-32 substantially lower cost, at 100 hp | First-article floor $15-47k across the concepts (lowest: $15-39k, concept A) against a $13-14k automotive conversion. The fixed lines do not scale down. | Making **200 hp the first family member** puts the program where it beats the market: $20-52k for concept A at 200 hp, against $88k + core for a new O-360. 100 hp then follows as a derivative. |
| **F-3** | R-1 one shared cylinder module across 100/200/300 | A ~50 hp cylinder gives a 2/4/6 family, but the 100 hp member is a **2-cylinder** engine, with large torque pulsation and first- or second-order excitation into the propeller. A ~25 hp cylinder (Rotax-scale) gives 4/8/12; **12 cylinders at 300 hp breaks the part-count goal**. One module cannot give both a smooth 100 hp and a reasonable 300 hp. | **Two modules** (a ~25 hp cylinder for a 4-cylinder 100 hp, and a ~50 hp cylinder for 4/6-cylinder 200/300) buy a smooth 100 hp and a 6-cylinder 300 hp. They cost a second piston/head/valve set: about 2x the part numbers, a second casting set, a second crank. Or drop 100 hp from phase 1 (F-2). |
| F-4 | R-43 transmission for a fixed-pitch prop | Not a killer; see DRIVE_AND_PROP.md. A CVT recovers full engine power at low speed, but not propeller efficiency. At an assumed 0.88 belt efficiency it delivers less thrust power than an in-flight-adjustable prop at every speed from 60 to 180 kt. No flying piston-engine CVT was found. | Informational. Not on the card. |
| **F-5** | R-35 $22k at 200 hp (ruled) | Phase 1b, on MANUFACTURING's bottom-up estimates (envelope v1, [E], not quotes): concept H is **$26.7k / $38.1k / $54.5k** (low / mid / high) per engine if the program pays the tooling once ($7.2k-26.7k), and **$35.8k / $55.9k / $87.3k** if the first engine carries it. With DFM levers 1 and 4, $25.8k / $36.3k / $51.1k. No auto-gas candidate meets $22k even at the low end, on either reading; deleting the normalizer and the second ignition lane still leaves $23.5k. | **Escalated to Bill (AER-3329).** Relaxing to about $30k per builder keeps H as ranked (6 cylinders, about 338 parts, 148-158 kg, normalized to 12,000 ft); the mid estimate needs about $37k. RECOST_PHASE1B.md section 5. |

## 12. Bill's rulings on the phase-0 card (2026-10-16)

Bill accepted the card "Auto gas, 200 hp first, 12,000 ft, two cylinder
sizes?" on 2026-10-16 (AER-3320). The ruled scope is exactly what the card
said; nothing beyond it is implied.

| # | Ruling | Lines it settles |
|---|---|---|
| 1 | **Auto gas for the first family member.** | R-10; F-1 is moot for the first member. R-8 (diesel sea-level boost) is not ruled and returns to Bill only if a diesel member is taken up. |
| 2 | **200 hp is the first family member**, at **no more than $22k (200 hp) and $30k (300 hp)**, parts and services, first article. | R-35 (200/300 hp), F-2. 100 hp follows as a derivative; its $15k target was not on the card and stays proposed. |
| 3 | **MCP held to 12,000 ft density altitude, takeoff power to 8,000 ft.** | R-7 |
| 4 | **Two cylinder sizes are allowed** across the family. | F-3; R-1 reads as "common parts across the family, up to two cylinder modules". |

Phase 1 ranks the auto-gas concepts in ARCHITECTURES.md and the drive options
in DRIVE_AND_PROP.md against these rulings.
