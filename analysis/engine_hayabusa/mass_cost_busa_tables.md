Propeller torque at takeoff: 408 N m (105 kW crank, 7,000 rpm, 2.92:1).

## 1. Installed dry mass (R-37 definition)

| Line | low (kg) | high (kg) |
|---|---|---|
| engine with its integral gearbox, clutch, starter and stator [F, H21 H22] | 86.0 | 92.0 |
| dry-sump conversion, net of the wet pan: pump, tank, lines [E] | 2.0 | 4.0 |
| reduction gearbox at 0.020-0.036 kg per N m of propeller torque [E] | 8.2 | 14.7 |
| adapter plate and soft coupling [E, MFG] | 2.0 | 4.0 |
| two-lane FADEC: second ECU, second coils, second crank sensor, harness [E] | 2.5 | 4.0 |
| second generator for lane B (R-25 two power feeds) [E] | 2.0 | 4.0 |
| exhaust, 4-into-1 stainless [E] | 4.0 | 7.0 |
| intake plenum and air filter [E] | 1.5 | 3.0 |
| engine mount, 4130 tube bed with isolators [E, MFG] | 3.0 | 5.0 |
| fuel pumps and filters at the engine [E] | 1.0 | 2.0 |
| **Installed dry, naturally aspirated** | **112** | **140** |
| + normalizer (turbo + intercooler), if fitted | 126 | 161 |
| radiator, oil cooler and coolant system (separate line, R-38) | 20.1 | 21.4 |
| installed with the cooling system, NA | 132 | 161 |

Per takeoff horsepower at the flange (113-139 hp): 0.81-1.24 kg/hp, NA, installed dry.

## 2. First-engine cost, basis 1 (R-35 definition: parts and services, no labor, no propeller)

| Line | low | high |
|---|---|---|
| used Gen 2 core, 7k-32k miles (eBay snapshot) [S, H24] | $3,000 | $3,820 |
| aircraft-duty rebuild parts: cam chain and tensioner, all shells, rings, gaskets [S partial H39-H42, E] | $1,000 | $1,500 |
| 11:1 pistons for sustained full throttle on MON 85 (knock section) [E] | $700 | $1,100 |
| machine shop: crack test of crank and rods, valve job, inspection [E] | $500 | $1,200 |
| dry sump: SBD kit GBP 1,160 ex VAT plus tank, lines and fittings [S D30 + E] | $1,943 | $2,343 |
| reduction gearbox, proven-class, made (none to buy, P section 1) [E, CRANK_AND_SCALING 5] | $2,900 | $9,800 |
| adapter plate and crank-side hub [MFG AER-3526] | $1,100 | $4,500 |
| torsional elastic coupling [MFG AER-3526] | $300 | $1,000 |
| FADEC, two lanes (cost_floor.py, same line as H) [E] | $1,500 | $4,000 |
| second coil per cylinder, 4 x D585 class (cost_floor.py) [S-MFG] | $200 | $400 |
| second plug per cylinder: sleeved plug tubes, two scrap heads, section, fixture, prove-out [MFG AER-3526; outside the envelope until a section proves it] | $2,100 | $7,300 |
| second crank sensor and trigger wheel [E] | $100 | $300 |
| second generator and regulator for lane B (cost_floor START_ALT as the allowance) [E] | $400 | $900 |
| cooling at 81 kW (cost_floor.py rate per 100 kW) [E] | $405 | $972 |
| fuel system, two pumps, E15-rated hoses (cost_floor.py) [E] | $400 | $800 |
| exhaust (cost_floor.py) [E] | $300 | $800 |
| intake plenum and filter [E] | $200 | $500 |
| engine mount, 4130 tube bed, 4 isolators, jig; builder TIG (shop route $3.0k-8.4k) [MFG AER-3526] | $1,400 | $3,700 |
| misc: fasteners, seals, filters (cost_floor.py) [E] | $600 | $1,500 |
| **Total, naturally aspirated** | **$19,048** | **$46,435** |

Low / mid / high: $19.0k / $29.7k / $46.4k.
With a normalizer: $21.0k / $32.7k / $50.9k.
Of which lines any engine in the program needs (gearbox, FADEC, cooling, fuel, exhaust, mount, misc): $9.8k-29.2k; the Hayabusa-specific core, rebuild, pistons, dry sump and head work: $9.2k-17.3k.
The dual-lane hardware beyond one FADEC line (second plug, coils, sensor, generator): $2.8k-8.9k.

## 3. Builder labor (not in R-35's cost)

| Task | hours |
|---|---|
| teardown, inspection, rebuild with new pistons | 30-50 |
| dry sump fit | 10-20 |
| gearbox, adapter and coupling fit and alignment | 40-100 |
| FADEC wiring, two lanes, and calibration on the stand | 60-140 |
| cooling, exhaust and intake fabrication | 40-80 |
| engine mount welding, builder TIG, skill B3 (MFG AER-3526) | 40-80 |
| first runs and a torsional survey on the stand | 20-40 |
| **Total** | **240-510** |

## 4. Durability bracket: Radical race hours scaled to aircraft MCP rpm

| Wear law, hours as rpm^-k | race mean rpm | aircraft MCP rpm | life multiplier | equivalent aircraft hours to a Radical-class rebuild |
|---|---|---|---|---|
| k = 1 | 7,500 | 5,800 | 1.29 | 116-129 |
| k = 1 | 7,500 | 6,500 | 1.15 | 104-115 |
| k = 1 | 9,000 | 5,800 | 1.55 | 140-155 |
| k = 1 | 9,000 | 6,500 | 1.38 | 125-138 |
| k = 3 | 7,500 | 5,800 | 2.16 | 195-216 |
| k = 3 | 7,500 | 6,500 | 1.54 | 138-154 |
| k = 3 | 9,000 | 5,800 | 3.74 | 336-374 |
| k = 3 | 9,000 | 6,500 | 2.65 | 239-265 |

Band: 104-374 h. Against R-40's 2,000 h TBO target.
