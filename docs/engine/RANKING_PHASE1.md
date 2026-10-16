# Engine phase 1: ranking and convergence for the 200 hp member

Owner: PROPULSION. Issue: AER-3326 (follows AER-3320; ORG-009). Date: 2026-10-16.
Status: **ranking pass. The convergence pick is stated in section 1. Nothing here has been built, run or tested.** This is an experimental engine design. Nothing in it is certified, certifiable or flight-ready.

Every number comes from a script in `analysis/engine_phase1/` (rerun commands in its README) or from the phase-0 scripts it reuses, unless a source is named. The phase-0 fidelity boundary still applies: masses are +/-25 % extrapolations and costs are first-article floors with unquoted lines.

## 1. The answer

**Convergence pick for the 200 hp member: concept H.** It is a flat-6 with the GM LS7 bore and stroke (104.8 x 101.6 mm), liquid-cooled, normalized by a turbocharger, direct drive at 3,300 rpm takeoff. It flies a **ground-adjustable propeller as the baseline**, and the engine provisions for a constant-speed propeller as an upgrade.

H is concept A's architecture (flat, direct drive) with concept C's cylinder module. It was written in this pass because the ranking showed that A's layout and C's module each won where the other lost. **Among the five concepts the issue named, A ranks first.** H is the pick because it ties A on the matrix and beats it on the evidence (section 4).

H has a flown analog of almost exactly its cylinder, rpm and fuel: the **UL Power UL520iS**. That engine is a 105.6 x 100 mm air-cooled flat-6, direct drive, rated 200 hp at 3,300 rpm and 185 hp at 2,800 rpm. It runs CR 8.7 on MOGAS of MON 88 or better, and weighs 93.3 kg dry and 108 kg ready to fly (ulpower.com, read 2026-10-16). Its cylinder sweeps 876 cc, against the LS7's 876 cc.

**The 200 hp member, for the board** (concept H, first article, 2026 USD):

| Line | Value | Method |
|---|---|---|
| Takeoff / MCP | 200 hp at 3,300 rpm / 180 hp (R-3); MCP held to 12,000 ft, takeoff to 8,000 ft (ruling 3) | `member_200.py` |
| Displacement, BMEP, piston speed | 5.26 L, 10.3 bar, 11.2 m/s; implied sea-level ηv 0.91 | phase-0 `engine_floor.py` method |
| Installed dry mass (R-37 definition) | **134 kg**, +/-25 % (target 150 kg, proposed) | UL520iS 108 kg ready to fly, x1.10 sand-cast, + water jackets, turbo, second ECU lane |
| Cooling system (R-38) | **about 26 kg** installed (22.8-29.6 kg across the core geometries), was 6-42 kg | `radiator.py`, section 8 |
| Installed dry + cooling | **about 160 kg** | |
| Part count | **342 non-fastener parts, 86 unique part numbers, about 250 fasteners** | `member_200.py` BOM enumeration |
| Cost floor | **$23.2k / $36.8k / $58.4k** (low / mid / high) against **$22k ruled** | phase-0 line items + cylinder-block castings + crank damper |
| Fuel burn at takeoff | 46.2 kg/h (310 g/kWh class value); knock-limited CR about 8.4 on 91 AKI, so about +5.7 % fuel against CR 10 | `knock.py` |

**The cost target is not met at the mid estimate by any candidate.** It is within reach only if the unquoted lines land at the bottom of their bands. The job-shop first-op machining of six castings ($3k-12k) is the largest line. The billet crank ($3.9k-7.2k) and the castings themselves ($4.4k-10.9k) are next. That is why the MANUFACTURING quote (section 9) is the next decision point. It is not yet a reason to change the ruling: the quote may land at the low end. If it does not, the escalation to Bill will state what relaxing $22k buys.

## 2. Requirements this ranking is scored against

All four card rulings of 2026-10-16 (REQUIREMENTS section 12) apply:

1. auto gas;
2. 200 hp first, at no more than $22k;
3. MCP to 12,000 ft and takeoff power to 8,000 ft density altitude;
4. two cylinder sizes allowed across the family.

The rest are the brief (fewer parts, made from files, the propeller as a constraint) and the proposed lines (R-12 91 AKI rated, R-37 mass). Diesel concepts E and F stay on file in ARCHITECTURES.md, **unranked**, as the issue says.

## 3. Knock on pump gas: the criterion phase 0 could only argue

Phase 0 named knock as concept A's killer without a number. `knock.py` puts one on it.

**Method.**

- The knock index is K = t_burn / τ_endgas: a one-step Livengood-Wu integral with the Douaud-Eyzat delay correlation (Heywood ch. 9).
- The burn time is half a bore (two plugs per cylinder, R-25) divided by a turbulent flame speed that tracks mean piston speed.
- The threshold is calibrated on five engines that run, each at its rated fuel:

| Engine | Bore x stroke (mm) | rpm | CR | Fuel octane | K |
|---|---|---|---|---|---|
| Rotax 912 ULS (liquid-cooled heads) | 84 x 61 | 5,800 | 10.8 | MON 85 | 3.19 |
| UL520iS (air) | 105.6 x 100 | 3,300 | 8.7 | MON 88 | 1.74 |
| Lycoming O-320-E2D (air) | 130.2 x 98.4 | 2,700 | 7.0 | 80/87 avgas | 1.63 |
| Lycoming O-360-A1A (air) | 130.2 x 111.1 | 2,700 | 8.5 | 91/96 avgas | 1.93 |
| Lycoming IO-360-A (air) | 130.2 x 111.1 | 2,700 | 8.7 | 100LL | 1.54 |

**The four air-cooled engines agree within 25 %**, which is evidence that the index captures what bore and rpm do. The Rotax, the only anchor with liquid-cooled heads, sits **1.9x higher**: that is the credit a liquid-cooled head and a modern chamber may buy, and this design has both. The ranking uses the air-cooled threshold, which is conservative. The CRs for the Lycoming and Rotax anchors come from secondary sources; the type certificate data sheets were not read.

**Result on 91 AKI (MON 85, R-12):**

| Concept | Knock-limited CR (air-cooled threshold; range to the liquid-cooled credit) | Ideal fuel-burn cost against CR 10 |
|---|---|---|
| A flat-4, 130 mm bore, 2,750 rpm | 7.7 (7.6-9.2) | +8.8 % |
| B flat-8, 86 mm, 5,800 rpm | 9.1 (8.9-10.9) | +3.0 % |
| C V4, 104.8 mm, 4,700 rpm | 9.2 (9.0-11.0) | +2.5 % |
| D radial-7, 114.3 mm, 2,400 rpm | 7.6 (7.5-9.1) | +9.2 % |
| **H flat-6, 104.8 mm, 3,300 rpm** | **8.4 (8.2-10.0)** | **+5.7 %** |

On 87 AKI (about MON 82, R-13), every CR drops by about 0.25-0.3.

**Hot charge at altitude.** At 12,000 ft on an ISA+20 C day the compressor delivers about 76 C. With no intercooler, that is about 0.9 of a point of knock-limited CR. An intercooler bringing the charge to about 45 C costs about 4 kW of heat to air. **The intercooler is a requirement, not an option**, and the phase-0 turbo mass allowance already includes it.

## 4. Concept ranking, 200 hp member

**Method.** A weighted-sum decision matrix (multi-attribute value scoring), in `rank.py`.

- Raw metrics carry units and come from named scripts.
- They are normalized two ways, ratio-to-best and min-max, and both rankings are shown.
- Robustness is tested by 20,000 Monte Carlo weight draws centred on the stated weights (Dirichlet, concentration 20), and 20,000 from a flat Dirichlet (any weighting equally likely).
- A leave-one-criterion-out test shows what each criterion is carrying.

| Criterion | Weight | Traces to | A | B | C | D | G | H |
|---|---|---|---|---|---|---|---|---|
| Cost floor mid, $k | 0.25 | ruling 2, $22k | 36.5 | 45.6 | 33.6 | 52.5 | 32.0 | 36.8 |
| Parts, non-fastener | 0.15 | brief: fewer parts | 254 | 555 | 264 | 411 | 288 | 342 |
| Installed dry + cooling, kg | 0.15 | R-37 | 202 | 145 | 176 | 190 | 168 | 153 |
| Drive / torsional risk, 0-10 | 0.15 | brief: propeller; FL-1/FL-2 | 10 | 5.6 | 3.9 | 10 | 6.0 | 9 |
| Fuel-burn index (BSFC x knock CR cost) | 0.10 | rulings 1, R-12 | 1.09 | 1.03 | 1.03 | 1.09 | 1.13 | 1.06 |
| Made-from-files, 0-10 | 0.10 | brief; envelope | 6.7 | 5.0 | 5.0 | 3.3 | 2.5 | 6.7 |
| Family members the module serves, of 3 | 0.10 | ruling 4 | 2 | 2 | 2 | 2 | 2.5 | 2 |
| *Cost floor low end, $k* | | *$22k test* | *22.6* | *28.3* | *20.7* | *31.9* | *21.5* | *23.2* |

How the judgment-based rows are scored:

- **Drive risk.** Direct drive scores 10: there is no gearbox, so FL-1 (total loss of thrust) does not exist, and the drive sits on the stiff side of the torsional window. A geared drive scores 3 + 3 x (the soft-coupling stiffness it needs / the easiest geared case), so the hardest-to-tune gearbox scores lowest. H loses a point for the crank damper it may need (section 6).
- **Made-from-files.** 10 / (1 + the number of custom precision parts with no catalog source beyond the crank):
  - A: aviation-priced pistons (0.5).
  - B, C: a gear set.
  - D: master and link rods, plus a supercharger gear train.
  - G: a multi-piece eccentric shaft, the trochoid housing supply, and a gear set.
  - H: a pendulum damper (0.5).
- **Family.** Members served smoothly by the 200 hp module: no 2- or 3-cylinder member, and ηv no higher than 0.97.

**Results.**

| Normalization | Order | First place in centred / flat weight draws |
|---|---|---|
| Ratio-to-best | **A 9.01**, H 8.82, G 8.30, C 8.19, D 7.33, B 7.32 | A 69 % / 57 %; H 24 % / 31 %; G 7 % / 10 % |
| Min-max | **H 7.20**, A 6.35, G 6.24, C 6.04, B 4.32, D 3.11 | H 67 % / 51 %; G 19 % / 21 %; A 9 % / 15 % |

**Among the five named concepts (A, B, C, D, G), A is first under both normalizations.** Remove H from the min-max table and A (6.35) leads G (6.24).

Leave-one-out (ratio):

- A wins with any one criterion removed, except two cases.
- Remove parts and H wins.
- Remove drive risk and C wins. **That is the whole case against C: its gearbox.** C is the cheapest piston concept and has the best knock margin, but it puts a gearbox behind four big cylinders, the hardest torsional case in the set.

**Why H over A, when the matrix calls them a tie.** Four reasons, each outside the matrix's arithmetic:

1. **Evidence.** H's cylinder, rpm and fuel class fly today in the UL520iS. A's 130 mm bore at 11 bar on 91 AKI has no running anchor. The Lycoming cylinders it copies run on 91/96 or 100LL avgas.
2. **Mass.** H is inside the proposed 150 kg (134 kg). A misses it by 33 kg at the central estimate.
3. **Pistons.** H uses the LS-class automotive piston catalog (Wiseco forged, $155-280 each, sourced in the envelope). A uses the Lycoming 540 aviation catalog, priced [Q]. The cost model gives both the same per-cylinder price, which **flatters A**.
4. **Fuel.** H's knock margin costs about 3 points less fuel than A's.

**What H gives up.** 88 more parts than A (six cylinders, not four). A 1.73 m propeller at 3,300 rpm with a static tip Mach of 0.88, against A's 1.88 m at 2,700 (louder, and about 3 points of cruise efficiency, section 7). And a crank mode that crosses the 6th firing order in the cruise band (section 6).

**What would flip the pick back to A:**

- the MANUFACTURING quote shows the extra cylinder-bank casting area costs more than A's aviation pistons;
- or the 6th-order crossing cannot be moved or damped with a catalog-class part;
- or Bill weighs noise and part count above mass.

**The rest, ranked and why:**

- **G** (third) is cheapest at the mid estimate, but it carries the worst made-from-files score and the largest radiator. Counting the seals, it is not the "few parts" engine it looks like: 288 parts, of which 152 are seals and seal springs.
- **C** (fourth): the gearbox.
- **D** and **B** (last): D's master and link rods, and 16 castings. B's 555 parts across 8 cylinders and 32 valves.

## 5. Concept H, the family, and what the second cylinder size is for

| Member | Layout | Vd | rpm | BMEP | ηv SL | Installed dry (+ cooling mid) | Note |
|---|---|---|---|---|---|---|---|
| 100 hp | flat-4, same module | 3.51 L | 2,700 | 9.5 bar | 0.83 | 80 kg (+10) | comfortable; smooth (flat-4, not a twin) |
| 200 hp | flat-6 | 5.26 L | 3,300 | 10.3 bar | 0.91 | 134 kg (+20; radiator sizing says about 26) | the pick |
| 300 hp | flat-8, same module | 7.01 L | 3,400 | 11.3 bar | **0.99** | 182 kg (+29) | **over the 0.97 airflow edge; and tip Mach at 3,400 rpm** |

**One module serves 100 and 200 hp.** That fixes F-3's rough 2-cylinder 100 hp, and it frees the second cylinder size (ruling 4) for 300 hp. At 3,300 rpm, 300 hp needs about 7.9 L, so the second module is about 1.3-1.5 L per cylinder in a flat-6. That module is phase 2 work.

**100 hp derivative feasibility note (the issue asks no more than this).** It is feasible on the 200 hp module at 2,700 rpm, at 80 kg. The cost floor is about $19k-49k, so **F-2 still stands: 100 hp misses its proposed $15k at first article.** The derivative's advantage is shared tooling and shared fixtures, not a lower bill.

## 6. Torsional vibration: the multi-mass check phase 0 asked for

`torsional_h.py` models the crank as a lumped chain: propeller, flange, one inertia per throw, rear accessory gear. Segment stiffnesses come from G J / L_eq (Den Hartog; Ker Wilson's equivalent-length idea), solved as a generalized eigenproblem. Inertias and stiffnesses are assumed from catalog-class dimensions: 60 mm journals, LS-class piston and rod masses.

| Engine | Mode 1 / 2 / 3, J_prop 1.0 kg m^2 | Major-order crossings, idle to 105 % redline | Sensitivity, throw stiffness +/-30 % |
|---|---|---|---|
| **H flat-6, 3,300 rpm** | 261 / 768 / 1,274 Hz | **6th order at about 2,610 rpm**; 9th at about 1,740 rpm | mode 1 225-289 Hz: the 6th-order crossing moves to 2,250-2,890 rpm |
| A flat-4, 2,750 rpm | 295 / 841 / 1,330 Hz | 8th order at about 2,210 rpm; 6th order 5-10 % above redline | |

**Reading it.**

- **Mode 1 is the crank winding against the propeller**, with the propeller near a node. It barely moves with propeller inertia (0.6 to 2.5 kg m^2 changes it by under 4 %), so a propeller change will not fix it.
- **On H it meets the 6th order, a major order whose excitation adds in phase at every throw, in the cruise band** (UL's MCP is 2,800 rpm).
- Stiffening the crank by 30 % pushes the crossing to about 2,890 rpm, into the climb band. That is no better.
- The honest fixes are a **crank pendulum damper tuned to the 6th order** (the certified flat-sixes carry crank dampers; general practice, not sourced this pass), or a published restricted-rpm band. The cost floor carries $400-1,500 for the damper.
- A's crossings are an 8th-order one (weaker excitation) and a 6th order just above redline. **On torsional grounds alone, A is cleaner than H.**
- Fidelity: excitation amplitude is not computed, so this is a flag, not a stress. The final check is a torsional survey on the dynamometer before flight.

## 7. Drive and propeller ranking at concept H's rpm

`drive_match.py` reruns the phase-0 BEM model (same blade, same engine curve, same atmosphere rule) at 3,300 rpm. The propeller is 1.73 m (68 in), sized for tip Mach. The reduction cases use 1.375:1 to 2,400 rpm and 1.98 m. `drive_rank.py` scores the options:

- climb (80 kt) and cruise (165 kt) thrust-power fraction, 0.20 each;
- static thrust, 0.05;
- propeller + drive cost, scored against the engine's $22k, 0.20;
- mass, scored against 150 kg, 0.10;
- worst single failure, 0.25.

The single-failure scale: 10 means nothing fails beyond the blade; 4 means it fails to fine pitch with overspeed exposure; 1 means total loss of thrust.

| Rank | Option | 80 kt | 165 kt | Static | Prop + drive | Worst single failure |
|---|---|---|---|---|---|---|
| 1 | **3b Ground-adjustable, cruise setting** | 0.60 | 0.85 | 2.49 kN | $3,600, 8.5 kg | blade / clamp: none beyond the propeller |
| 2 | 8b Flex blade, +/-1 deg (UNVERIFIED: one owner price, 200 hp availability not confirmed) | 0.64 | 0.62 | 3.04 kN | about $1,900 | as fixed pitch |
| 3 | 1 Fixed pitch, 130 kt | 0.64 | 0.51 | 2.89 kN | $4,000, 7 kg | as fixed pitch |
| 4 | 3a Ground-adjustable, climb setting | 0.72 | overspeeds | 3.27 kN | $3,600 | as fixed pitch |
| 5 | **6/7/9 Variable pitch, direct, held at 3,300** | 0.72 | 0.85 | 3.03 kN | $14,800, 20 kg | oil loss to fine: overspeed exposure (FL-7) |
| 6 | 6/7/9 Variable pitch, UL schedule (3,300 takeoff / 2,800 MCP) | 0.72 | 0.81 | 3.03 kN | $14,800 | as above |
| 7 | 2 Reduction 1.375:1, fixed pitch | 0.65 | 0.50 | 2.52 kN | $6,250, 33 kg | **total loss (FL-1)** |
| 8 | 7 Constant speed behind 1.375:1 | 0.73 | 0.87 | 2.50 kN | $18,050, 46 kg | **total loss (FL-1)** |
| 9 | 5 Two-speed gearbox (UNPRICED) | 0.65 | 0.83 | 2.42 kN | not found | **total loss into neutral (FL-5)** |
| 10 | 4a CVT at 0.88 (UNPRICED) | 0.55 | 0.77 | 1.81 kN | not found | **total loss (FL-3)** |

Cells are thrust power / rated shaft power. Static thrust is for rank order only (phase-0 fidelity note). Without the unverified and unpriced options, the order is 3b > 1 > 3a > variable pitch > the geared options. 3b takes first place in 98 % of centred and 63 % of flat weight draws.

**What the table says.**

1. **Direct drive wins at H's rpm.** The reduction buys 1-2 points of cruise efficiency through lower tip Mach (0.80 against 0.95 at 180 kt). It costs 21-32 kg, and it brings back FL-1, the documented killer.
2. **The cheap baseline is a ground-adjustable propeller pitched for cruise.** It is within 0-4 points of a constant-speed propeller from 150 to 180 kt. Its weakness is climb: 0.60 against 0.72 at 80 kt, because the engine reaches only about 2,570 rpm at full throttle.
3. **The constant-speed upgrade is worth about 12 points of climb thrust power and more static thrust, for about $11,000 more.** That is the builder's call. The engine should not foreclose it, so H provisions a crank-nose oil feed (hydraulic, option 7) and a spare FADEC pitch channel (electric, option 9) from the start.
4. **The CVT and the two-speed rank last at this rpm as well.** Each adds a total-loss-of-thrust failure mode for less than a variable-pitch propeller delivers.
5. H's 3,300 rpm costs about 3 points of cruise efficiency against A's 2,700 rpm (0.85 against 0.88 at 165 kt, constant speed). That is the price of the smaller cylinder, and it is in the H-versus-A trade above.

## 8. Radiator at MCP / Vy / ISA+20 C (narrows R-38)

**The case.** `radiator.py` sizes the core at MCP (180 hp, 134 kW), held at Vy climb on a sea-level ISA+20 C day (35 C).

- **Heat.** BSFC 290 g/kWh at MCP (class value, assumed) gives 109 kW to coolant and 23 kW to oil.
- **Core model.** A louvered-fin flat-tube core with the Chang & Wang (1997) j-factor, epsilon-NTU crossflow (Kays & London), and a duct momentum drag with no Meredith heat recovery credited.
- **Vy.** Assumed 80 KIAS (there is no airframe), with 70 and 90 printed.

| Core depth | Face velocity | Radiator face | Oil cooler face | Core dp | Cooling drag | Installed system |
|---|---|---|---|---|---|---|
| 32 mm | 8 m/s | 3,660 cm^2 | 880 cm^2 | 246 Pa | 1.7 kW (1.3 % MCP) | 24.6 kg |
| **50 mm** | **8 m/s** | **2,890 cm^2** | **880 cm^2** | **347 Pa** | **1.7 kW (1.3 %)** | **26.0 kg** |
| 64 mm | 10 m/s | 2,210 cm^2 | 780 cm^2 | 588 Pa | 2.7 kW (2.0 %) | 25.6 kg |

The full grid (three depths, four face velocities) gives **22.8-29.6 kg and 0.8-3.0 % of MCP in drag**.

**Sanity checks.**

- The 50 mm core rejects 0.038 kW/cm^2. The two phase-0 analogs are 0.06 (Rotax 915, bare core) and 0.047 (a liquid-cooled Lycoming conversion, full system). The model is more conservative than either, which is expected at a 70 K inlet temperature difference.
- The system comes to 5.1 kW per kg, inside the 3.7-27 bound and near its full-system end, as it should be.
- Core plus duct loss stays under the free-stream dynamic pressure at 70 KIAS, so ram air is enough and no fan is needed in climb.

**The 12,000 ft ISA+20 cross-check** needs about 20 % less face. At the same indicated speed, the mass flow falls with the square root of density, but the 24 K colder air more than pays for it. **Sea level ISA+20 C is the sizing case**, as R-22 assumed.

**R-38 narrows from 6-42 kg to about 26 kg (22.8-29.6 kg).** The ranking above carried 20 kg for every piston concept. All of them reject the same heat, so the order does not change; G's line is about 1.3x larger.

**What it does not cover.** Coolant-side pressure drop and pump head, a real duct design, and the intercooler (about 4 kW, air-to-air, separate).

## 9. Handoffs

- **MANUFACTURING (AER-3328; AER-3321 is closed).** Part envelopes for concept H's crankcase half, cylinder-bank block and bank head, so that the job-shop first-op line and the bureau casting line get quoted. Also turbocharger, intercooler and supercharger sourcing added to the envelope. The envelopes are in the child issue and in section 10 below.
- **Elon and the board.** The 200 hp member's mass, cost and part count are in section 1.
- **AVIONICS.** Nothing new this pass; the CAN-FIX key set is still a later handoff (R-27).
- **Failure ledger.** FL-24 to FL-29 are added (`FAILURE_LEDGER.md`).

## 10. Part envelopes sent to MANUFACTURING (concept H, geometry intent, not CAD)

All are A356-T6, or A357-T6 where noted, cast through a binder-jet bureau with a foundry pour (envelope route 1.2), X-rayed or pressure-tested, and impregnated. Every precision bore houses a bought part (envelope finding 2). Sizes are bounding boxes, +/-15 %, from catalog-class dimensions: LS bore spacing class, 60 mm mains, a 111.8 mm bore pitch plus wet-liner jacket. Masses are estimates.

| Part | Qty per engine | Bounding box (mm) | Mass est. | Critical features (housings for bought parts) | First-op setups intended |
|---|---|---|---|---|---|
| Crankcase half, split at crank centerline (A357-T6: main webs carry propeller thrust and gyroscopic load) | 2 | 560 x 300 x 160 | 9-12 kg | 4 main-bearing housings (catalog shells), line-bored together after halves are doweled, then align-honed; thrust-bearing faces at the nose; cam bore (bushings); 12 lifter bores (catalog LS-class lifters); 2 cylinder-bank pad faces with stud bosses; split face with 2 dowels; oil galleries drilled and plugged, not cast (envelope 1.1) | 3: split face and dowels; mains, cam and lifter bores in one setup on the doweled pair; bank pads |
| Cylinder-bank block, 3 wet-liner bores with integral coolant jacket | 2 | 380 x 190 x 165 | 7-9 kg | 3 liner upper and lower register bores (catalog wet liner, 104.8 mm finished bore, O-ring seals); deck face (protrusion spec on the liner, not the casting); base pad to case; coolant inlet boss | 2: base pad, then deck plus registers in one setup |
| Bank head, 3 cylinders, 2 valves per cylinder, pushrod, cored coolant jacket | 2 | 380 x 180 x 110 | 9-11 kg | 6 seat-insert bores, 6 guide bores (catalog), 6 spark-plug bosses (2 per cylinder, R-25), 3 injector bosses, rocker-stand pads, deck face, intake and exhaust port flanges | 2: deck, then seat and guide bores normal to the valve axes (one compound setup or a tilting fixture) |

**Quote asked:** first-op machining per casting, at quantity 1 and 5; bureau mold + pour + T6 + impregnation per casting, at quantity 1 and 5; a catalog wet liner at 104.8 mm (LS class); and a 6-throw billet 4340 crank at 101.6 mm stroke with 60 mm mains and a propeller flange.

**Sourcing asked:**

- **Turbocharger.** About 0.24 kg/s corrected flow at a pressure ratio of 1.68 (12,000 ft critical altitude, 200 hp). A wastegate, and oil- and water-cooled bearing housing options.
- **Air-to-air intercooler.** About 4 kW at 0.13 kg/s.
- **Supercharger, for comparison.** Centrifugal and positive-displacement classes, at the same duty, with a bypass.

For each: price, mass, lead time, and whether it is a catalog part.

## 11. What this pass did not do

- **No quotes.** The cost floor still rests on unquoted job-shop and casting lines. The $22k test is decided by the quote, not by this document.
- **No knock measurement.** The index is calibrated on running engines and ranks geometries; it does not set this head's CR.
- **No torsional excitation amplitudes or damper design.** No propeller blade-mode survey.
- **No turbocharger-versus-supercharger trade** for H. It waits on MANUFACTURING's sourcing.
- **No CAD, no FADEC design** (out of scope).
- **The UL520iS "ready to fly" contents are not defined by UL.** H's mass anchor takes them as the closest match to R-37's "installed dry"; if they are not, H's mass moves.
