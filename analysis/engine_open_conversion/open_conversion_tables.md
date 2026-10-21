## 1. Ratings: what each core is asked for, as BMEP and piston speed

The core's own ceiling is its car peak-torque BMEP (the highest it reaches anywhere on the car curve). Takeoff power at the flange is crank power x 0.97.

| Core | Point | rpm | crank kW | BMEP (bar) | piston speed (m/s) | car peak-torque BMEP (bar) | car peak-power BMEP (bar) | margin to car peak torque |
|---|---|---|---|---|---|---|---|---|
| Suzuki K15B (in production, port injection) | 100 hp takeoff | 5,800 | 76.9 | 10.9 | 16.4 | 11.9 | 10.5 | 8% |
| Suzuki K15B (in production, port injection) | 90 hp MCP | 5,500 | 69.2 | 10.3 | 15.6 | 11.9 | 10.5 | 13% |
| Subaru EZ36 (2007-2019, out of production) | 200 hp takeoff | 5,000 | 153.8 | 10.2 | 15.2 | 11.6 | 10.5 | 12% |
| Subaru EZ36 (2007-2019, out of production) | 180 hp MCP | 4,700 | 138.4 | 9.7 | 14.3 | 11.6 | 10.5 | 16% |
| GM LS3 (crate engine still sold) | 300 hp takeoff | 4,400 | 230.6 | 10.1 | 13.5 | 11.7 | 10.5 | 13% |
| GM LS3 (crate engine still sold) | 270 hp MCP | 4,100 | 207.6 | 9.8 | 12.6 | 11.7 | 10.5 | 16% |

Yardsticks (HAYABUSA_PLATFORM section 2): Rotax 912 ULS 11.2 bar / 11.8 m/s at takeoff; concept H 10.3 bar / 11.2 m/s; Viking and Aeromomentum about 16 m/s.

**Aeromomentum's own ratings, as BMEP** (a check the vendor's figures cannot fake; crank power assumed):

| Model | rated | rpm | BMEP if at the crank (bar) | piston speed (m/s) |
|---|---|---|---|---|
| AM13 (1.298 L) | 100 hp | 5,800 | 11.9 | 14.6 |
| AM15 (1.497 L) | 120 hp | 5,800 | 12.4 | 16.3 |
| AM20T (1.998 L, turbo) | 260 hp | 5,800 | 20.1 | 16.6 |

## 2. R-25 on a one-plug-per-cylinder core: MCP left after one coil or plug fails

Method as torsional_busa.py section 4: ((z-1)/z x IMEP - FMEP) / BMEP at the MCP point, FMEP 1.6 bar [A]. Two ECUs, two crank sensors and two power feeds can be made dual on any core; the plug and its coil cannot, unless the head has two plugs per cylinder.

| Core | cylinders | MCP BMEP (bar) | MCP left, one cylinder dead | R-25 asks |
|---|---|---|---|---|
| Suzuki K15B (in production, port injection) | 4 | 10.3 | 71% | 90 % |
| Subaru EZ36 (2007-2019, out of production) | 6 | 9.7 | 81% | 90 % |
| GM LS3 (crate engine still sold) | 8 | 9.8 | 85% | 90 % |
| Aeromomentum AM13 / AM15 (one plug, one ECU, as sold) | 4 | 10.5 | 71% | 90 % |
| Concept H (two plugs per cylinder by design) | 6 | 9.3 | about 97-99 % (one plug of two lost per cylinder; not computed here) | 90 % |

## 3. Installed dry mass (R-37 definition)

**B-100, Suzuki 1.5 L I4 core, program gearbox**

| Line | low (kg) | high (kg) |
|---|---|---|
| core with OE starter and alternator, no OE manifolds [E: AM15 complete 83.9 kg less its gearbox; K15B 85 kg, secondary] | 72.0 | 85.0 |
| program gearbox with coupling and slip clutch [MFG AER-3633] | 6.0 | 10.0 |
| adapter plate and flywheel hub [E] | 2.0 | 4.0 |
| second FADEC lane: ECU, crank sensor, harness [E, as HAYABUSA] | 2.0 | 3.0 |
| second generator for lane B (R-25) [E] | 2.0 | 4.0 |
| exhaust, 4-into-1 stainless [E] | 4.0 | 7.0 |
| intake plenum and filter [E] | 1.5 | 3.0 |
| oil system for aircraft attitudes: baffled sump or accumulator [E] | 0.5 | 2.0 |
| fuel pumps and filters at the engine [E] | 1.0 | 2.0 |
| **Installed dry, naturally aspirated** | **91** | **120** |
| with the program's normalizer (R-5, R-7) | 105 | 142 |

**B-200, Subaru EZ36 core, program gearbox**

| Line | low (kg) | high (kg) |
|---|---|---|
| core with OE starter and alternator [E: no OEM figure found; Eggenfellner E6 3.0 L package about 159 kg with gearbox, secondary] | 125.0 | 145.0 |
| program gearbox with coupling and slip clutch [MFG AER-3633] | 10.0 | 16.0 |
| adapter plate and flywheel hub [E] | 3.0 | 5.0 |
| second FADEC lane [E] | 2.5 | 4.0 |
| second generator for lane B [E] | 2.0 | 4.0 |
| exhaust, two 3-into-1 [E] | 6.0 | 10.0 |
| intake [E] | 2.0 | 4.0 |
| oil system for aircraft attitudes [E] | 1.0 | 4.0 |
| fuel pumps and filters [E] | 1.0 | 2.0 |
| **Installed dry, naturally aspirated** | **152** | **194** |
| with the program's normalizer (R-5, R-7) | 166 | 216 |

**B-300, GM LS3 crate core, program gearbox**

| Line | low (kg) | high (kg) |
|---|---|---|
| long block with starter and alternator [F: 375 lb undressed to 435 lb dressed, sources conflict] | 175.0 | 197.0 |
| program gearbox, about 840 N m at 2,550 propeller rpm, 0.020-0.036 kg per N m [E, CRANK_AND_SCALING 5] | 17.0 | 30.0 |
| adapter plate and flywheel hub [E] | 3.0 | 6.0 |
| second FADEC lane [E] | 3.0 | 4.5 |
| second generator for lane B [E] | 2.0 | 4.0 |
| exhaust, two 4-into-1 [E] | 8.0 | 14.0 |
| intake [E] | 3.0 | 5.0 |
| oil system for aircraft attitudes [E] | 1.0 | 5.0 |
| fuel pumps and filters [E] | 1.0 | 2.0 |
| **Installed dry, naturally aspirated** | **213** | **268** |
| with the program's normalizer (R-5, R-7) | 227 | 289 |

**Aeromomentum AM15, as sold (baseline)**

| Line | low (kg) | high (kg) |
|---|---|---|
| AM15 with gearbox, starter, alternator, ECU, harness [S, A3: 185 lb] | 83.9 | 83.9 |
| exhaust header and muffler (sold separately) [E] | 4.0 | 7.0 |
| **Installed dry, naturally aspirated** | **88** | **91** |
| with the program's normalizer (R-5, R-7) | 102 | 112 |

**Aeromomentum AM13, as sold (baseline)**

| Line | low (kg) | high (kg) |
|---|---|---|
| AM13 with gearbox, starter, alternator, ECU, harness [S, A2: 170 lb] | 77.1 | 77.1 |
| exhaust header and muffler [E] | 4.0 | 7.0 |
| **Installed dry, naturally aspirated** | **81** | **84** |
| with the program's normalizer (R-5, R-7) | 95 | 106 |

**B0, AM15 with the program FADEC in place of its ECU**

| Line | low (kg) | high (kg) |
|---|---|---|
| AM15 as sold [S] | 83.9 | 83.9 |
| exhaust [E] | 4.0 | 7.0 |
| second FADEC lane, second crank sensor; the AM ECU removed [E] | 1.5 | 2.5 |
| second generator for lane B [E] | 2.0 | 4.0 |
| **Installed dry, naturally aspirated** | **91** | **97** |
| with the program's normalizer (R-5, R-7) | 105 | 119 |

**Summary against R-37** (proposed: 90 / 150 / 210 kg):

| Member | Option | NA (kg) | normalized (kg) | R-37 |
|---|---|---|---|---|
| 100 hp | A, concept H (scaling_sweep model; its 9 kg turbo is in the figure) | - | 110-111 | 90 |
| 100 hp | B-100, Suzuki 1.5 L I4 core, program gearbox | 91-120 | 105-142 | 90 |
| 100 hp | Aeromomentum AM15, as sold (baseline) | 88-91 | 102-112 | 90 |
| 100 hp | Aeromomentum AM13, as sold (baseline) | 81-84 | 95-106 | 90 |
| 100 hp | B0, AM15 with the program FADEC in place of its ECU | 91-97 | 105-119 | 90 |
| 200 hp | A, concept H (scaling_sweep model; its 9 kg turbo is in the figure) | - | 143-145 | 150 |
| 200 hp | B-200, Subaru EZ36 core, program gearbox | 152-194 | 166-216 | 150 |
| 200 hp | Aeromomentum AM20T, turbocharged to its rating (breaks R-5) [S, A6: 285 lb] | - | 129 (boosted, not normalized) | 150 |
| 300 hp | A, concept H (scaling_sweep model; its 9 kg turbo is in the figure) [extrapolated: module not designed] | - | 174-177 | 210 |
| 300 hp | B-300, GM LS3 crate core, program gearbox | 213-268 | 227-289 | 210 |

Concept H at 200 hp is 148-158 kg on phase 1b's own build-up (RECOST_PHASE1B section 7); the sweep model gives 143-145 kg. The sweep is used here so the three members are on one model.

## 4. Cost, R-35 definition (no labor, no propeller, no engine mount)

**B-100, Suzuki 1.5 L I4 core, program gearbox**

| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |
|---|---|---|---|---|
| used core, Suzuki M15A / K15B class [MFG AER-3633] | $600 | $1,500 | $600 | $1,500 |
| teardown, crack check, rebuild to the program's measurement sheet; builder assembles [MFG] | $1,500 | $3,800 | $1,500 | $3,800 |
| program gearbox, catalog gear pair, billet case [MFG] | $3,300 | $9,600 | $2,700 | $8,100 |
| adapter plate and drilled OE flywheel as hub [MFG] | $1,100 | $2,800 | $800 | $2,100 |
| FADEC, two lanes (cost_floor.py, same line as H) [E] | $1,500 | $4,000 | $1,500 | $4,000 |
| second crank sensor and trigger [E] | $100 | $300 | $100 | $300 |
| second generator and regulator for lane B (cost_floor START_ALT) [E] | $400 | $900 | $400 | $900 |
| cooling at 78 kW to coolant and oil (cost_floor rate) [E] | $390 | $936 | $390 | $936 |
| fuel system, two pumps, E15-rated (cost_floor) [E] | $400 | $800 | $400 | $800 |
| exhaust (cost_floor) [E] | $300 | $800 | $300 | $800 |
| intake plenum and filter [E] | $200 | $500 | $200 | $500 |
| oil system for aircraft attitudes: baffles, pickup, accumulator or dry sump [E] | $300 | $1,200 | $300 | $1,200 |
| misc: fasteners, seals, filters (cost_floor) [E] | $600 | $1,500 | $600 | $1,500 |
| **Total, naturally aspirated** | **$10,690** | **$28,636** | **$9,790** | **$26,436** |

**B-100 alt, new Aeromomentum long block behind the program gearbox**

| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |
|---|---|---|---|---|
| Aeromomentum AM15 long block, new [S, A12: $4,295] | $4,295 | $4,295 | $4,295 | $4,295 |
| program gearbox, catalog gear pair [MFG] | $3,300 | $9,600 | $2,700 | $8,100 |
| adapter plate and hub [MFG] | $1,100 | $2,800 | $800 | $2,100 |
| FADEC, two lanes (cost_floor.py, same line as H) [E] | $1,500 | $4,000 | $1,500 | $4,000 |
| second crank sensor and trigger [E] | $100 | $300 | $100 | $300 |
| second generator and regulator for lane B (cost_floor START_ALT) [E] | $400 | $900 | $400 | $900 |
| cooling at 78 kW to coolant and oil (cost_floor rate) [E] | $390 | $936 | $390 | $936 |
| fuel system, two pumps, E15-rated (cost_floor) [E] | $400 | $800 | $400 | $800 |
| exhaust (cost_floor) [E] | $300 | $800 | $300 | $800 |
| intake plenum and filter [E] | $200 | $500 | $200 | $500 |
| oil system for aircraft attitudes: baffles, pickup, accumulator or dry sump [E] | $300 | $1,200 | $300 | $1,200 |
| misc: fasteners, seals, filters (cost_floor) [E] | $600 | $1,500 | $600 | $1,500 |
| **Total, naturally aspirated** | **$12,885** | **$27,631** | **$11,985** | **$25,431** |

**B-100 alt, used Suzuki core behind Aeromomentum's gearbox (bought standalone)**

| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |
|---|---|---|---|---|
| used core [MFG] | $600 | $1,500 | $600 | $1,500 |
| rebuild to the measurement sheet [MFG] | $1,500 | $3,800 | $1,500 | $3,800 |
| Aeromomentum gearbox complete GB1-A01 [S, A12: $2,495] and mounting plate set [S: $477] | $2,972 | $2,972 | $2,972 | $2,972 |
| fit check of the AM gearbox to the chosen core's face, hub [E] | $200 | $1,000 | $200 | $800 |
| FADEC, two lanes (cost_floor.py, same line as H) [E] | $1,500 | $4,000 | $1,500 | $4,000 |
| second crank sensor and trigger [E] | $100 | $300 | $100 | $300 |
| second generator and regulator for lane B (cost_floor START_ALT) [E] | $400 | $900 | $400 | $900 |
| cooling at 78 kW to coolant and oil (cost_floor rate) [E] | $390 | $936 | $390 | $936 |
| fuel system, two pumps, E15-rated (cost_floor) [E] | $400 | $800 | $400 | $800 |
| exhaust (cost_floor) [E] | $300 | $800 | $300 | $800 |
| intake plenum and filter [E] | $200 | $500 | $200 | $500 |
| oil system for aircraft attitudes: baffles, pickup, accumulator or dry sump [E] | $300 | $1,200 | $300 | $1,200 |
| misc: fasteners, seals, filters (cost_floor) [E] | $600 | $1,500 | $600 | $1,500 |
| **Total, naturally aspirated** | **$9,462** | **$20,208** | **$9,462** | **$20,008** |

**B-200, Subaru EZ36 core, program gearbox**

| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |
|---|---|---|---|---|
| used EZ36 core, delivered [MFG] | $1,500 | $4,600 | $1,500 | $4,600 |
| teardown, inspection, rebuild; builder assembles [MFG] | $3,200 | $7,200 | $3,200 | $7,200 |
| program gearbox, catalog module-4 pair, own case with the bellhousing face [MFG] | $5,100 | $13,900 | $4,200 | $11,800 |
| adapter plate and hub (a separate plate only if one gearbox serves both cores) [MFG] | $1,600 | $4,300 | $1,200 | $3,400 |
| FADEC, two lanes [E] | $1,500 | $4,000 | $1,500 | $4,000 |
| second crank sensor [E] | $100 | $300 | $100 | $300 |
| second generator for lane B [E] | $400 | $900 | $400 | $900 |
| cooling at 156 kW [E] | $780 | $1,872 | $780 | $1,872 |
| fuel system [E] | $400 | $800 | $400 | $800 |
| exhaust, two banks (cost_floor x 1.5) [E] | $450 | $1,200 | $450 | $1,200 |
| intake [E] | $300 | $800 | $300 | $800 |
| oil system for aircraft attitudes [E] | $400 | $1,500 | $400 | $1,500 |
| misc [E] | $600 | $1,500 | $600 | $1,500 |
| **Total, naturally aspirated** | **$16,330** | **$42,872** | **$15,030** | **$39,872** |

**B-300, GM LS3 crate core, program gearbox**

| Line | basis 1 low | basis 1 high | basis 3 low | basis 3 high |
|---|---|---|---|---|
| LS3 long block, new crate (19435106: $7,677 sale to $9,656 MSRP) [S] | $7,677 | $9,656 | $7,677 | $9,656 |
| program gearbox, about 500 N m input; MFG's EZ36 line x 1.2 [E] | $6,100 | $16,700 | $5,000 | $14,200 |
| adapter plate and hub [E, MFG EZ36 line] | $1,600 | $4,300 | $1,200 | $3,400 |
| FADEC, two lanes [E] | $1,500 | $4,000 | $1,500 | $4,000 |
| second crank sensor [E] | $100 | $300 | $100 | $300 |
| second generator for lane B [E] | $400 | $900 | $400 | $900 |
| cooling at 234 kW [E] | $1,170 | $2,808 | $1,170 | $2,808 |
| fuel system [E] | $400 | $800 | $400 | $800 |
| exhaust, two banks (cost_floor x 1.5) [E] | $450 | $1,200 | $450 | $1,200 |
| intake [E] | $300 | $800 | $300 | $800 |
| oil system for aircraft attitudes [E] | $400 | $1,500 | $400 | $1,500 |
| misc [E] | $600 | $1,500 | $600 | $1,500 |
| **Total, naturally aspirated** | **$20,697** | **$44,464** | **$19,197** | **$41,064** |

**Aeromomentum AM13, as sold**

| Line | low | high |
|---|---|---|
| AM13 with gearbox, starter, alternator, ECU [S, A2] | $11,500 | $12,600 |
| radiator [S, A13] | $205 | $345 |
| exhaust header and muffler [S, A13: $735 + $139] | $874 | $874 |
| hoses, oil cooler, fuel system parts [E] | $600 | $1,300 |
| **Total** | **$13,179** | **$15,119** |

**Aeromomentum AM15, as sold**

| Line | low | high |
|---|---|---|
| AM15 with gearbox, starter, alternator, ECU [S, A3] | $13,000 | $14,100 |
| radiator [S, A13] | $205 | $345 |
| exhaust header and muffler [S, A13] | $874 | $874 |
| hoses, oil cooler, fuel system parts [E] | $600 | $1,300 |
| **Total** | **$14,679** | **$16,619** |

**B0, AM15 with the program FADEC in place of its ECU**

| Line | low | high |
|---|---|---|
| AM15 as sold [S] | $13,000 | $14,100 |
| radiator, exhaust, hoses [S + E, as above] | $1,679 | $2,519 |
| program FADEC, two lanes, less the AM ECU's $450 resale [E] | $1,050 | $3,550 |
| second crank sensor, second generator [E] | $500 | $1,200 |
| **Total** | **$16,229** | **$21,369** |

**Aeromomentum AM20T, as sold (turbocharged to 260 hp; breaks R-5)**

| Line | low | high |
|---|---|---|
| AM20T [S, A6] | $27,995 | $27,995 |
| radiator, exhaust, hoses [E, AM15 lines x 1.5] | $2,500 | $3,800 |
| **Total** | **$30,495** | **$31,795** |

**Summary** (low / mid / high; a bought engine is the same on both bases):

| Member | Option | basis 1, program's first engine | basis 3, builder from published files | with the normalizer, basis 1 |
|---|---|---|---|---|
| 100 hp | A, concept H (sweep model; turbo included) | $26.8k / $40.9k / $62.4k | about $22.8k / $34.7k / $62.4k [E: 0.85-1.0 x basis 1] | (included) |
| 100 hp | B-100, Suzuki 1.5 L I4 core, program gearbox | $10.7k / $17.5k / $28.6k | $9.8k / $16.1k / $26.4k | $12.7k / $20.5k / $33.1k |
| 100 hp | B-100 alt, new Aeromomentum long block behind the program gearbox | $12.9k / $18.9k / $27.6k | $12.0k / $17.5k / $25.4k | $14.9k / $21.9k / $32.1k |
| 100 hp | B-100 alt, used Suzuki core behind Aeromomentum's gearbox (bought standalone) | $9.5k / $13.8k / $20.2k | $9.5k / $13.8k / $20.0k | $11.5k / $16.8k / $24.7k |
| 100 hp | Aeromomentum AM13, as sold | $13.2k / $14.1k / $15.1k | $13.2k / $14.1k / $15.1k | $15.2k / $17.3k / $19.6k |
| 100 hp | Aeromomentum AM15, as sold | $14.7k / $15.6k / $16.6k | $14.7k / $15.6k / $16.6k | $16.7k / $18.8k / $21.1k |
| 100 hp | B0, AM15 with the program FADEC in place of its ECU | $16.2k / $18.6k / $21.4k | $16.2k / $18.6k / $21.4k | $18.2k / $21.7k / $25.9k |
| 200 hp | A, concept H (sweep model; turbo included) | $31.7k / $48.0k / $72.7k | about $27.0k / $40.8k / $72.7k [E: 0.85-1.0 x basis 1] | (included) |
| 200 hp | B-200, Subaru EZ36 core, program gearbox | $16.3k / $26.5k / $42.9k | $15.0k / $24.5k / $39.9k | $18.3k / $29.5k / $47.4k |
| 200 hp | Aeromomentum AM20T, as sold (turbocharged to 260 hp; breaks R-5) | $30.5k / $31.1k / $31.8k | $30.5k / $31.1k / $31.8k | breaks R-5 |
| 300 hp | A, concept H (sweep model; turbo included) [extrapolated] | $34.0k / $51.1k / $76.9k | about $28.9k / $43.5k / $76.9k [E: 0.85-1.0 x basis 1] | (included) |
| 300 hp | B-300, GM LS3 crate core, program gearbox | $20.7k / $30.3k / $44.5k | $19.2k / $28.1k / $41.1k | $22.7k / $33.3k / $49.0k |

Engine mount, every option, builder TIG [MFG]: 100 hp $1.4k-3.7k (basis 3 $1.3k-3.2k); 200 hp $1.8k-4.5k (basis 3 $1.6k-4.0k); 300 hp $2.0k-5.0k (basis 3 $1.8k-4.5k).

Concept H's basis 3 is not computed line by line. MANUFACTURING (AER-3633) reads a builder's quantity-one price as close to the first engine's, because a job shop writes its own CAM from a STEP; only published gating takes a real cut. 0.85-1.0 x basis 1 is that reading, not a build-up. Basis 2 (five engines, NRE paid once) is lower: $24.4k / $34.1k at 200 hp.

## 5. Program calendar to a first ground run and a first flight

Weeks from a go decision, low / high, as the longest chain through the task list below each option. Tasks without a dependency run in parallel. Every duration is [E] unless tagged. The airframe is assumed available when the engine is ready; it is not (MAOS is paused), and that is the same for every option.

| Option | first ground run (weeks) | first flight (weeks) | the chain that sets the first run |
|---|---|---|---|
| A, concept H 200 hp | 52-90 | 76-136 | crank: quote, make, nitride, grind, balance [S: 18-20 weeks lead] |
| B, open conversion, 100 hp Suzuki I4 | 30-60 | 50-100 | FADEC: two lanes to ground-run standard (shared; AER-3631 starts it) |
| B, open conversion, 200 hp EZ36 | 30-60 | 50-100 | FADEC: two lanes, 6 cylinders (shared) |
| Baseline: buy an AM15 | 5-14 | 13-30 | order and delivery [A: no lead time published] |
| B0, AM15 with the program FADEC (AER-3631) | 28-56 | 42-84 | FADEC: two lanes to ground-run standard (shared) |

<details><summary>A, concept H 200 hp: tasks</summary>

| Task | weeks | waits on |
|---|---|---|
| finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard | 26-52 | - |
| RFQ path exists (AER-3330, open since 2026-10-16) | 4-26 | - |
| crank: quote, make, nitride, grind, balance [S: 18-20 weeks lead] | 20-26 | finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard; RFQ path exists (AER-3330, open since 2026-10-16) |
| castings: print, pour, T6, RT, impregnate; one remake allowed [S envelope: 2-4 weeks per pour] | 6-12 | finish design: head detail, valvetrain, cam, oil and accessory drive, drawings to RFQ standard; RFQ path exists (AER-3330, open since 2026-10-16) |
| first-op machining and inspection [S envelope: 2-6 weeks] | 4-10 | castings: print, pour, T6, RT, impregnate; one remake allowed [S envelope: 2-4 weeks per pour] |
| FADEC: two lanes to ground-run standard (shared with B; AER-3631 starts it) | 26-52 | - |
| assembly, stand build, first run | 6-12 | crank: quote, make, nitride, grind, balance [S: 18-20 weeks lead]; first-op machining and inspection [S envelope: 2-6 weeks]; FADEC: two lanes to ground-run standard (shared with B; AER-3631 starts it) |
| stand program to flight: calibration, torsional survey, 50-100 h endurance, teardown | 16-30 | assembly, stand build, first run |
| installation in an airframe and taxi tests (airframe not chosen; MAOS paused) | 8-16 | stand program to flight: calibration, torsional survey, 50-100 h endurance, teardown |

</details>

<details><summary>B, open conversion, 100 hp Suzuki I4: tasks</summary>

| Task | weeks | waits on |
|---|---|---|
| buy and rebuild a core [MFG: 1-3 + 3-8 weeks] | 4-11 | - |
| gearbox: rate, design, draw [E] | 8-16 | - |
| gearbox, adapter and hub: make [MFG: 4-8 weeks catalog pair] | 4-8 | gearbox: rate, design, draw [E] |
| FADEC: two lanes to ground-run standard (shared; AER-3631 starts it) | 26-52 | - |
| assembly, stand build, first run | 4-8 | buy and rebuild a core [MFG: 1-3 + 3-8 weeks]; gearbox, adapter and hub: make [MFG: 4-8 weeks catalog pair]; FADEC: two lanes to ground-run standard (shared; AER-3631 starts it) |
| stand program to flight: calibration, torsional survey with the real propeller, 50-100 h, teardown | 12-24 | assembly, stand build, first run |
| installation in an airframe and taxi tests | 8-16 | stand program to flight: calibration, torsional survey with the real propeller, 50-100 h, teardown |

</details>

<details><summary>B, open conversion, 200 hp EZ36: tasks</summary>

| Task | weeks | waits on |
|---|---|---|
| buy and rebuild a core [MFG: 1-3 + 3-8 weeks] | 4-11 | - |
| gearbox: rate, design, draw [E] | 10-20 | - |
| gearbox, adapter and hub: make [MFG: 4-8, custom pair 8-14 weeks] | 6-14 | gearbox: rate, design, draw [E] |
| FADEC: two lanes, 6 cylinders (shared) | 26-52 | - |
| assembly, stand build, first run | 4-8 | buy and rebuild a core [MFG: 1-3 + 3-8 weeks]; gearbox, adapter and hub: make [MFG: 4-8, custom pair 8-14 weeks]; FADEC: two lanes, 6 cylinders (shared) |
| stand program to flight | 12-24 | assembly, stand build, first run |
| installation in an airframe and taxi tests | 8-16 | stand program to flight |

</details>

<details><summary>Baseline: buy an AM15: tasks</summary>

| Task | weeks | waits on |
|---|---|---|
| order and delivery [A: no lead time published] | 4-12 | - |
| first run on the vendor's ECU (no program FADEC) | 1-2 | order and delivery [A: no lead time published] |
| installation in an airframe and taxi tests | 8-16 | first run on the vendor's ECU (no program FADEC) |

</details>

<details><summary>B0, AM15 with the program FADEC (AER-3631): tasks</summary>

| Task | weeks | waits on |
|---|---|---|
| order and delivery [A] | 4-12 | - |
| FADEC: two lanes to ground-run standard (shared) | 26-52 | - |
| first run on the program FADEC, on the stand | 2-4 | order and delivery [A]; FADEC: two lanes to ground-run standard (shared) |
| stand program to flight: FADEC fault injection, 25-50 h | 6-12 | first run on the program FADEC, on the stand |
| installation in an airframe and taxi tests | 8-16 | stand program to flight: FADEC fault injection, 25-50 h |

</details>

**Builder hours to a ready-to-install engine** (not in R-35's cost):

| Option | hours |
|---|---|
| A, concept H 200 hp | 300-630 |
| B, open conversion, 100 hp Suzuki I4 | 195-410 |
| B, open conversion, 200 hp EZ36 | 240-475 |
| Baseline: buy an AM15 | 40-160 |

