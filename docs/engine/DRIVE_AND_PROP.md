# Drive and propeller match, phase 0: the divergence pass

Owner: PROPULSION. Issue: AER-3320 (ORG-009, 2026-10-16). Status: **divergence pass.** These options are **not ranked**; the order implies nothing, and ranking is phase 1. Nothing here has been built or tested.

Bill's brief names the propeller as a constraint. A car can change gear; a fixed-pitch propeller cannot change pitch. So this pass evaluates a transmission (CVT or stepped) that lets a cheap fixed-pitch propeller work at higher airspeeds, and every alternative to it.

## Method

**Model.** `analysis/engine_phase0/prop_match.py` is a blade-element / momentum (BEM) model with:

- Glauert/McCormick annulus momentum;
- Prandtl tip loss;
- swirl;
- a thin cambered section with a soft post-stall plateau;
- a compressibility drag rise above Mach 0.72.

**Every option uses the same two-blade propeller**, so differences come from how each drive and pitch strategy lets the engine and propeller meet, not from blade design. That makes it a comparative tool, not a propeller design.

**Reference case.** The 200 hp member (149 kW), normalized, so the same shaft power is available at sea level and at 8,000 ft. Speeds up to 100 kt are evaluated at sea-level ISA; 120 kt and above at 8,000 ft ISA. That is the issue's assumed climb-to-150-180-KTAS cruise. There is no airframe (MAOS is paused).

- **Direct drive**: 2,700 rpm, 1.88 m (74 in) diameter.
- **Reduction drive**: propeller at 2,300 rpm, 2.03 m (80 in).
- **Engine at full throttle**: power versus rpm follows P/P_r = (n/n_r)(1 + 0.25(1 - n/n_r)). That is a broad, naturally aspirated torque curve, ASSUMED. Redline is never exceeded; where a fixed-pitch propeller would overspeed, the engine is throttled back to redline.

**What each cell means.** Each cell is **thrust power / rated shaft power**, followed by (propeller efficiency, usable shaft fraction). It is the share of the engine's rating that becomes useful work on the airframe, with the propeller-efficiency loss, the drive loss, and any power the pitch strategy cannot use all charged against it. It does not depend on the airframe's drag.

**Sanity checks.**

- **Cruise**: peak efficiency of 0.88-0.89 at 165-180 kt is the right class for a clean metal or composite propeller (McCormick).
- **Climb and static, the weakest outputs**: static thrust comes out at a figure of merit of about 0.35-0.4 against the momentum-ideal 5.33 kN. Real propellers reach about 0.6-0.75. The crude post-stall model under-predicts, so **static thrust here is good for rank order only, not for a takeoff-distance number.** The 60-180 kt efficiencies sit in the realistic range.

**Family scaling (untested).** The 100 and 300 hp members behave the same way at the same power and advance-ratio coefficients. At 300 hp, a three-blade propeller is needed to stay within tip Mach at a similar diameter. That was not computed in this pass.

**Prices and masses.** `sources/PROP_AND_DRIVE_SOURCES_2026-10-16.md`, all read 2026-10-16.

**Torsional vibration.** `analysis/engine_phase0/torsional.py`, a two-inertia window. See the torsional section below.

## Results across the speed range (200 hp member)

| Option | Static thrust | 60 kt | 80 kt | 100 kt | 120 kt | 150 kt | 165 kt | 180 kt |
|---|---|---|---|---|---|---|---|---|
| 1 Direct drive, fixed pitch (pitch set for 130 kt) | 2.64 kN | 0.54 (0.59, 0.92) | 0.65 (0.74, 0.88) | 0.73 (0.81, 0.90) | 0.81 (0.82, 0.98) | 0.69 (0.88, 0.79) | 0.53 (0.88, 0.59) | 0.30 (0.85, 0.36) |
| 2 Fixed reduction, fixed pitch (larger, slower prop, set for 130 kt) | 2.56 kN | 0.54 (0.60, 0.92) | 0.65 (0.76, 0.87) | 0.72 (0.82, 0.90) | 0.80 (0.83, 0.98) | 0.67 (0.88, 0.78) | 0.49 (0.89, 0.56) | 0.25 (0.84, 0.31) |
| 3a Ground-adjustable, climb setting (80 kt) | 2.97 kN | 0.62 (0.63, 0.99) | 0.74 (0.74, 1.00) | 0.70 (0.82, 0.86) | 0.45 (0.86, 0.52) | 0.11 | overspeeds | overspeeds |
| 3b Ground-adjustable, cruise setting (165 kt) | 2.33 kN | 0.49 (0.55, 0.90) | 0.61 (0.73, 0.83) | 0.68 (0.81, 0.84) | 0.76 (0.82, 0.92) | 0.84 (0.87, 0.97) | 0.88 (0.88, 1.00) | 0.70 (0.89, 0.79) |
| 4a CVT + fixed pitch, CVT efficiency 0.88 (ASSUMED) | 2.15 kN | 0.48 (0.54, 1.00) | 0.63 (0.71, 1.00) | 0.71 (0.80, 1.00) | 0.73 (0.83, 1.00) | 0.77 (0.87, 1.00) | 0.78 (0.88, 1.00) | 0.78 (0.89, 1.00) |
| 4b CVT + fixed pitch, CVT efficiency 0.94 (sensitivity, UNSOURCED) | 2.20 kN | 0.49 (0.52, 1.00) | 0.65 (0.69, 1.00) | 0.75 (0.80, 1.00) | 0.77 (0.82, 1.00) | 0.82 (0.87, 1.00) | 0.83 (0.88, 1.00) | 0.83 (0.89, 1.00) |
| 5 Two-speed gearbox + fixed pitch (cruise blade, low gear 1.25:1, 0.97) | 2.27 kN | 0.48 (0.55, 0.89) | 0.62 (0.73, 0.88) | 0.67 (0.81, 0.86) | 0.73 (0.83, 0.91) | 0.81 (0.87, 0.96) | 0.85 (0.88, 1.00) | 0.70 (0.89, 0.82) |
| 6 / 7 / 9 In-flight adjustable or constant speed, direct (2,700 rpm) | 2.62 kN | 0.63 (0.63, 1.00) | 0.74 (0.74, 1.00) | 0.80 (0.80, 1.00) | 0.82 (0.82, 1.00) | 0.86 (0.86, 1.00) | 0.88 (0.88, 1.00) | 0.89 (0.89, 1.00) |
| 7 Constant speed behind a reduction (prop 2,300 rpm, 2.03 m) | 2.54 kN | 0.64 (0.65, 1.00) | 0.74 (0.75, 1.00) | 0.80 (0.81, 1.00) | 0.82 (0.83, 1.00) | 0.86 (0.87, 1.00) | 0.87 (0.88, 1.00) | 0.87 (0.89, 1.00) |
| 8a Self-adjusting, governing hub (Aeromatic class; 5 % rpm droop ASSUMED) | 2.30 kN | 0.61 (0.63, 1.00) | 0.72 (0.74, 1.00) | 0.79 (0.80, 1.00) | 0.81 (0.82, 1.00) | 0.86 (0.87, 1.00) | 0.87 (0.88, 1.00) | 0.89 (0.89, 1.00) |
| 8b Self-adjusting, flex blade (Prince P-tip class; +/-1 deg ASSUMED) | 2.70 kN | 0.55 (0.59, 0.92) | 0.65 (0.74, 0.88) | 0.72 (0.81, 0.90) | 0.80 (0.82, 0.97) | 0.77 (0.87, 0.88) | 0.64 (0.89, 0.72) | 0.45 (0.88, 0.52) |

"overspeeds" means the propeller cannot absorb usable power without exceeding redline; the engine must be throttled to near idle at that speed.

**What the table says, without ranking.**

1. **A fixed-pitch propeller loses its usable power, not its efficiency.** At 180 kt, option 1's propeller is still 85 % efficient, but the engine can only use 36 % of its rating before redline. That is the brief's concern, in numbers: 0.30 against 0.89 for a variable-pitch propeller.
2. **A CVT recovers the power but not the propeller's efficiency, and pays its own loss.** With the engine held at rated rpm (usable fraction 1.00 everywhere), the fixed blade still runs off its best advance ratio at low speed (0.71 at 80 kt against 0.74 for constant speed). At an assumed 0.88 CVT efficiency, **option 4a delivers less thrust power than an in-flight-adjustable or constant-speed propeller at every speed from 60 to 180 kt**, and less static thrust. Even at the unsourced 0.94 it trails by 4-6 points from 150 to 180 kt. Against the cheap cruise-set ground-adjustable propeller (3b), the CVT at 0.88 wins at 80-100 kt and at 180 kt, and loses at 60 kt, from 120 to 165 kt, and on static thrust.
3. **A two-speed gearbox is nearly as good as a CVT where it matters**: 0.85 at 165 kt, against 0.78 for the CVT at 0.88. That is because its 0.97 efficiency beats a belt's, and two well-chosen ratios cover climb and cruise.
4. **At this fidelity, a fixed reduction drive does not improve the propeller.** The larger, slower propeller (option 2 against 1, option 7 against 6) lands within 1-2 points up to 150 kt. With fixed pitch it is 4-5 points worse at 165-180 kt, because the slower propeller hits redline sooner. A reduction drive's benefit is on the engine side: it lets a small, fast engine exist. Concept B is 72 kg at 100 hp against concept A's 108 kg. It also gives lower tip Mach and less noise.
5. **The flex-blade "self-adjusting" propeller is a better fixed-pitch propeller, not a governor.** It adds 8-15 points at 150-180 kt over option 1 (0.77 against 0.69 at 150 kt; 0.45 against 0.30 at 180 kt), under an ASSUMED +/-1 degree of flex.

## The options

### 1. Direct drive, fixed pitch

- **Physics floor**: row 1. Good at the speed it was pitched for, power-limited away from it: a pitch set for 130 kt gives 0.65 at 80 kt and 0.30 at 180 kt.
- **Mass**: propeller only, 12-18 lb (5.4-8.2 kg). MT 170 R 180-3E is 12 lb; Sensenich W74FM-49 wood is 18 lb. No drive mass.
- **Cost**: $3,600 (MT, Van's form) to $4,304 (Sensenich wood, ACS). No drive.
- **Torsional exposure**: the lowest of any option. The propeller bolts to a stiff crank flange, so the crank-and-prop first mode sits on the stiff side of the window (below). The remaining exposure is **propeller blade resonance excited by firing order**. Certified engine-propeller pairs carry restricted-rpm bands from vibration surveys for this reason (general practice, not sourced this pass). Any new engine needs that survey.
- **What its failure leaves the pilot**: there is nothing to fail but the blade and hub. A blade failure is a vibration emergency at any propeller.
- **Fit with the concepts**: only the direct-drive concepts A and D.

### 2. Fixed reduction drive, fixed pitch

- **Physics floor**: row 2. Within 1-2 points of row 1 up to 150 kt, and 4-5 points worse at 165-180 kt. The benefit is engine mass and tip Mach, not propeller efficiency.
- **Mass**: the gearbox. Marcotte M-300 is 47 lb (21 kg, *unverified*); Auto PSRUs 250Z is 70 lb (32 kg). Rotax's integral gearbox mass was not found separately. A builder gearbox from catalog gears is a phase-1 estimate [Q].
- **Cost**: the 250Z is $37,000 commercial, which is a product price, not a parts cost. A gears-and-case-from-files gearbox is $1.5-5k [Q] (`cost_floor.py`), plus the propeller ($2-4k).
- **Torsional exposure: the highest of any option.** A gearbox puts a spring (shaft, gear mesh, coupling) between two large inertias, the crank and the propeller. Its first mode must be tuned away from the firing band. The window table below shows that **a plain steel quill shaft lands inside the forbidden band for every geared concept.** That is the documented killer of aircraft reduction drives:
  - EPI: damaging torsional loads at 240-320 Hz, and a vendor's fatal failure.
  - Eggenfellner RV-9A, NTSB ERA14LA130: spline and PSRU input failure at 325 h, total loss of thrust.
  - NTSB NYC95LA137: PSRU shaft failure.
  - Rotax answers it with a dog-gear torsional shock absorber, an overload clutch, and (on the 915) a torsion shaft with 2-3 degrees of twist.
- **What its failure leaves the pilot**: a gearbox, shaft or spline failure is a **total loss of thrust**. It does not degrade.
- **Fit**: concepts B, C, E, F (whose gear train is the drive), G.

### 3. Ground-adjustable propeller

- **Physics floor**: rows 3a and 3b. The pilot chooses on the ground. The climb setting gives 0.74 at 80 kt but overspeeds above about 150 kt. The cruise setting gives 0.88 at 165 kt but only 0.61 at 80 kt and 2.33 kN static (the lowest of the fixed-pitch rows). It is option 1 with the pitch chosen per mission, not per flight phase.
- **Mass**: Warp Drive HP 2-blade is 7-8 lb; Whirlwind GA-200L 72 in (180 hp) is 18 lb; Sensenich 2G0M8 is 19-20 lb.
- **Cost**: Warp Drive from $972; Whirlwind GA-200L $2,915; Sensenich 2G0M8C72RG $4,338 (all ACS).
- **Torsional exposure**: as option 1 (direct) or 2 (geared). Composite blades shift blade-resonance frequencies against wood, so it needs its own survey.
- **What its failure leaves the pilot**: as fixed pitch, plus one more item: blade-retention clamp torque, an inspection item.

### 4. Continuously variable transmission (CVT) + fixed pitch

- **Physics floor**: rows 4a and 4b. Full engine power at every speed. The net result is set by the CVT's own efficiency, and **that efficiency is unsourced at 75-150 kW**: the research found only scooter-class literature and an untraceable "70-80 %" claim, which is not used. Row 4a assumes 0.88 (rubber V-belt class, ASSUMED); row 4b 0.94 (metal push-belt or toroidal class, UNSOURCED).
- **Mass**: not found. No flying CVT behind a piston engine was found, and the only multi-speed propeller drive found is a turbine patent concept (US6524068). PROPULSION will not publish an untraceable CVT mass. A phase-1 estimate would bound it from a snowmobile CVT and a metal-belt automotive CVT, labeled extrapolation.
- **Cost**: not found.
- **Torsional exposure**: mixed and unknown. A rubber belt adds compliance and damping, which helps put the first mode below idle. But a belt behind a 2-, 3- or 4-cylinder 4-stroke sees very large torque pulses, and belt life under them is undocumented at this power. Belted Air Power, a fixed-ratio belt, reports backfire shearing crank bolts.
- **What its failure leaves the pilot**: a belt or variator failure is a **total loss of thrust**. A ratio frozen at one setting degrades to option 2 at that ratio. Frozen at the climb end, the engine is throttled back above about 120 kt; frozen at the cruise end, climb and takeoff thrust are reduced.
- **Its sharpest finding**: nowhere in 60-180 kt does a CVT at 0.88 beat a variable-pitch propeller on thrust power. Its case rests on cost and simplicity at the propeller, and both of those are unknown.

### 5. Two-speed (stepped) gearbox + fixed pitch

- **Physics floor**: row 5. A cruise-pitched blade with a 1.25:1 low gear: 0.62 at 80 kt, 0.85 at 165 kt. Most of the CVT's benefit at gear efficiency (0.97, ASSUMED: one extra mesh).
- **Mass and cost**: not found. There is no flying example. A two-speed planetary from catalog gears is a phase-1 estimate [Q].
- **Torsional exposure**: as option 2, plus a shift transient: a torque step through the soft coupling at every shift.
- **What its failure leaves the pilot**: stuck in low gear gives the climb row, throttled at cruise speed. Stuck in high gear gives the cruise row with weak climb (0.62 at 80 kt). **A shift mechanism that fails into neutral is a total loss of thrust**, so the design must not allow a neutral state.

### 6. In-flight adjustable propeller (pilot-set pitch)

- **Physics floor**: the constant-speed row, **if the pilot sets pitch well**. Physically it is the same envelope (0.74 at 80 kt, 0.88 at 165 kt). The differences are workload, and over-speed protection that rests on the pilot.
- **Mass**: IVOprop UL 3-blade 72 in is 9 lb complete (to 100 hp); MTV-17/18 electric are 39-47 lb including spinner.
- **Cost**: IVOprop UL $1,854-2,129 (to 100 hp); IVOprop Magnum $3,700-4,168 (maker: *not recommended for Lycomings*); DUC Flash-R $4,263; MTV-17/18 $15,750-18,650.
- **Torsional exposure**: as the underlying drive (1 or 2).
- **What its failure leaves the pilot**:
  - **Actuator frozen**: a fixed-pitch propeller at the last setting (a row 1 or 3 equivalent at that pitch).
  - **Runaway to fine**: overspeed risk; the pilot throttles back, and power is limited at high speed.
  - **Runaway to coarse**: weak climb and takeoff thrust.
  - The design must make "freeze" the failure, not "run away".

### 7. Constant-speed propeller (hydraulic governor)

- **Physics floor**: rows 6/7. The envelope of this whole study: 0.63 at 60 kt, 0.74 at 80 kt, 0.88-0.89 at 165-180 kt, at full power everywhere.
- **Mass**:
  - 180-300 hp class: 36-51 lb. Whirlwind CS-300 72 in is 36 lb; MTV-12-B is 46-47 lb excluding governor; Hartzell C2YR is about 51 lb (*unverified*).
  - Rotax class: MT MTV-33 is 6.5 kg, with a 1 kg governor. E-Props Glorieuse is 4 kg including governor.
- **Cost**:
  - 180-300 hp: $12,463 (Hartzell C2YR, Van's Aug 2025) to $29,160 (Hartzell Explorer, IO-540), plus governor (PCU5000X $2,350).
  - Rotax class: E-Props Glorieuse about EUR 8,200 complete.
  - **3-8x a fixed-pitch propeller.**
- **Torsional exposure**: as the underlying drive. A constant-speed hub changes the propeller's inertia and blade modes against fixed pitch, so it needs its own survey.
- **What its failure leaves the pilot**: loss of oil pressure to a single-acting, non-counterweighted hub drives it to fine pitch (typical for non-aerobatic singles). Full power stays available, but with overspeed risk at high speed, so the pilot throttles back. Governor failure behaves similarly.
- **Fit**: hydraulic governors want engine oil pressure at the propeller flange. On a geared engine (concepts B, C, E, F, G) that means oil routed through the gearbox output shaft (MT does this for Rotax).

### 8. Self-adjusting propeller (no pilot control)

- **8a, governing hub (Aeromatic class)**: the blade's aerodynamic twisting moment is balanced against counterweights.
  - **Physics floor**: approximately constant speed between stops. Row 8a under an ASSUMED 5 % rpm droop at low speed.
  - **Mass**: 28-62 lb.
  - **Cost**: the product is **historical**. A 2015 forum post says the maker lost its PMA for new blades, and no current counterweight or centrifugal self-governing hub was found.
  - **TBO**: 600 h.
- **8b, flex blade (Prince P-tip class)**: the blade bends under load, about 4 in of pitch change from takeoff to cruise (maker).
  - **Physics floor**: row 8b, modeled as +/-1 degree at 0.75R (ASSUMED). It behaves as a better fixed-pitch propeller, not a governor.
  - **Cost**: about $1,900 (one owner report); mass not found.
  - The DUC "aerodynamic constant-speed effect" is a marketing claim with no data found.
- **Torsional exposure**: as the underlying drive. A flexing blade's modes move with load, so the survey must cover the whole speed range.
- **What its failure leaves the pilot**: nothing to operate. A stuck hub becomes a fixed-pitch propeller at whatever pitch it stuck. **Its weakness is that it cannot be checked in flight.**

### 9. Better than the list: FADEC-integrated electric constant speed (single lever)

- **Idea.** The engine already has a two-lane FADEC (REQUIREMENTS R-25/R-26). An electric pitch actuator in the hub (Airmaster-class), governed by the FADEC, turns option 6 into option 7 with no governor, no oil to the propeller, and one power lever. On this engine the step from "in-flight adjustable" to "constant speed" is software and a pitch-position sensor.
- **Physics floor**: the constant-speed row.
- **Mass**: Airmaster AP332, 12.1 kg including cockpit unit (to 120 hp, geared engines). E-Props Glorieuse, 4 kg including governor (Rotax class), is the hydraulic comparison.
- **Cost**: Airmaster price not found. The control is "free" only if the FADEC already carries the lanes for it.
- **Torsional exposure**: as the underlying drive.
- **What its failure leaves the pilot**:
  - **One FADEC lane lost**: the second lane keeps governing (R-25).
  - **Both lanes or the actuator lost**: pitch must **freeze**, which leaves a fixed-pitch propeller at the last setting. A runaway must be designed out: a self-locking actuator, the gearmotor class Airmaster uses.
  - **The FADEC becomes propeller-critical.** That raises the bar on R-25, and it goes on the ledger.

## Torsional vibration: the window every geared option must hit

**Two-inertia model, everything referred to the crank.** The first mode is f1 = (1/2 pi) sqrt(k (1/J_e + 1/J_p')), with J_p' = J_prop / ratio^2. Inertias are representative and **ASSUMED** until parts exist. The main firing order of a z-cylinder 4-stroke is z/2 per crank revolution, and it sweeps from idle to redline. The rule (ASSUMED, a rule of thumb) is to keep f1 at least 25 % away from that band:

- **soft**: below idle firing, the Rotax and EPI approach;
- or **stiff**: above redline firing.

| Case | J_prop referred to crank | Firing band | Soft: k below | Stiff: k above |
|---|---|---|---|---|
| A direct, 4-cyl 200 hp, 2,750 rpm | 1.400 kg m^2 | 23-92 Hz | 2,918 N m/rad | 109,948 N m/rad |
| A direct, 2-cyl 100 hp, 2,750 rpm | 0.900 | 13-46 Hz | 578 | 16,660 |
| B geared 2.4:1, 8-cyl 200 hp, 5,800 rpm | 0.243 | 120-387 Hz | 17,508 | 443,800 |
| C geared 2.0:1, 4-cyl 200 hp, 4,800 rpm | 0.400 | 50-160 Hz | 5,831 | 145,766 |
| E geared 1.6:1, 6-cyl diesel 200 hp, 3,900 rpm | 0.625 | 50-195 Hz | 9,571 | 355,390 |
| G geared 2.0:1, 4-rotor 200 hp, 4,600 rpm | 0.400 | 100-307 Hz | 20,213 | 464,091 |

**Reading it.**

- **A plain steel quill shaft**, 40 mm diameter and 300 mm long, has k = GJ/L, which is about 67,000 N m/rad. **That lands inside the forbidden window for every geared case** (B, C, E, G). A geared drive must therefore carry a **deliberately soft element**: an elastomer or spring coupling, of order 6,000-20,000 N m/rad, crank-referred. Or it must be made unusually stiff, which gear meshes and splines rarely allow at 145,000-464,000 N m/rad.
- **The soft path crosses resonance at every start and shutdown**, below idle. That is why Rotax pairs its soft element with a slipping or overload clutch, and why EPI warns against light flywheels.
- **Direct drive (A, D) sits naturally on the stiff side**: a crank flange is far stiffer than 110,000 N m/rad. Its exposure moves to the propeller blades' own modes. The 100 hp flat-twin is the hardest direct case: 13-46 Hz first-order excitation, at very large torque-pulse amplitude.
- **Fidelity boundary.** This window is not a torsional analysis. Phase 1 needs a multi-mass model of the chosen concept, with real crank, coupling and propeller stiffnesses and inertias, and damping. The final check is a measurement on the dynamometer before flight.

## Failure-mode summary for the ledger

Every row is copied into `FAILURE_LEDGER.md`. SAFETY is paused, so PROPULSION keeps the ledger.

| Option | Single failure | What the pilot has left |
|---|---|---|
| 1, 3 | blade or hub failure | vibration emergency; no degraded mode |
| 2 | gearbox, quill shaft or spline failure | **total loss of thrust** |
| 4 | belt or variator failure | **total loss of thrust** |
| 4 | ratio frozen | fixed reduction at that ratio: weak climb or throttled cruise |
| 5 | shift failure into neutral (must be designed out) | **total loss of thrust** |
| 5 | stuck in one gear | climb row or cruise row only |
| 6 | actuator frozen | fixed pitch at last setting |
| 6 | runaway fine / coarse | overspeed (throttle back) / weak climb |
| 7 | propeller oil-pressure loss (single-acting hub) | goes to fine: full power with overspeed risk at speed |
| 8a | hub stuck | fixed pitch at stuck pitch, undetectable in flight |
| 9 | one FADEC lane | none (second lane governs) |
| 9 | both lanes or actuator | must freeze: fixed pitch at last setting |
