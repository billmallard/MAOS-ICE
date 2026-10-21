## 1. The motorcycle ratings, as published

| Generation | bore x stroke (mm) | Vd (L) | CR | peak power | BMEP at peak power | Sp at peak power | peak torque | BMEP at peak torque |
|---|---|---|---|---|---|---|---|---|
| Gen 3 (2021-) | 81.0 x 65.0 | 1.340 | 12.5 | 138 kW (185 hp) at 9,700 | 12.8 bar | 21.0 m/s | 149 N m at 7,000 | 14.0 bar |
| Gen 2 (2008-2020) | 81.0 x 65.0 | 1.340 | 12.5 | 145 kW (194 hp) at 9,500 | 13.7 bar | 20.6 m/s | 155 N m at 7,200 | 14.5 bar |
| Gen 1 (1999-2007) | 81.0 x 63.0 | 1.298 | 11.0 | 129 kW (173 hp) at 9,800 | 12.1 bar | 20.6 m/s | 138 N m at 7,000 | 13.4 bar |

## 2. Knock-limited compression ratio at sustained full throttle, MON 85 (knock.py)

| rpm | Sp (m/s) | CR limit, air-cooled threshold | CR limit, liquid-cooled-head credit (Rotax 912 anchor) | stock CR | margin at stock CR (liquid credit) |
|---|---|---|---|---|---|
| 5,500 | 11.9 | 9.2 | 10.9 | 12.5 | -1.6 |
| 6,000 | 13.0 | 9.4 | 11.2 | 12.5 | -1.3 |
| 6,500 | 14.1 | 9.6 | 11.4 | 12.5 | -1.1 |
| 7,000 | 15.2 | 9.8 | 11.7 | 12.5 | -0.8 |
| 7,500 | 16.2 | 10.0 | 11.9 | 12.5 | -0.6 |
| 9,700 | 21.0 | 10.7 | 12.8 | 12.5 | +0.3 |

Lower-compression pistons at CR 11.0: ideal Otto power ratio 0.966 against CR 12.5.

## 3. The aircraft rating (Gen 2 or Gen 3: same 81 x 65 mm and CR; Gen 3 curve; CR 11 pistons), crank and propeller flange

| Point | rpm | Sp (m/s) | BMEP (bar) | crank (kW / hp) | flange, gearbox 0.97-0.98 (hp) | fuel (L/h) | implied eta_v | coolant / oil heat (kW) |
|---|---|---|---|---|---|---|---|---|
| Takeoff, 5 min, eta_v-capped | 6,500 | 14.1 | 12.0 | 87 / 117 | 113-114 | 33 | 1.01 | 68 / 14 |
| Takeoff, 5 min, eta_v-capped | 7,000 | 15.2 | 12.0 | 94 / 126 | 122-123 | 35 | 1.01 | 74 / 15 |
| Takeoff, 5 min, motorcycle WOT curve | 6,500 | 14.1 | 13.0 | 95 / 127 | 123-124 | 35 | 1.06 | 72 / 15 |
| Takeoff, 5 min, motorcycle WOT curve | 7,000 | 15.2 | 13.5 | 105 / 141 | 137-139 | 38 | 1.09 | 80 / 17 |
| MCP | 5,800 | 12.6 | 10.5 | 68 / 91 | 88-89 | 24 | 0.86 | 50 / 11 |
| MCP | 6,500 | 14.1 | 11.5 | 83 / 112 | 109-110 | 32 | 1.01 | 67 / 14 |

## 4. Against the yardsticks

| Engine | takeoff | BMEP at takeoff | Sp at takeoff | MCP | BMEP at MCP | Sp at MCP | MCP / takeoff | source |
|---|---|---|---|---|---|---|---|---|
| Rotax 912 ULS | 99 hp at 5,800 | 11.2 bar | 11.8 m/s | 93 hp at 5,500 | 11.1 bar | 11.2 m/s | 94% | COMPARABLE_ENGINES [R1][R3] |
| Rotax 915 iS (turbo) | 139 hp at 5,800 | 15.9 bar | 11.8 m/s | 133 hp at 5,500 | 16.0 bar | 11.2 m/s | 95% | COMPARABLE_ENGINES [R5] |
| Rotax 916 iS (turbo) | 157 hp at 5,800 | 17.9 bar | 11.8 m/s | 135 hp at 5,500 | 16.3 bar | 11.2 m/s | 86% | COMPARABLE_ENGINES [R6] |
| Concept H (200 hp member) | 200 hp at 3,300 | 10.3 bar | 11.2 m/s | 180 hp at 3,300 | 9.3 bar | 11.2 m/s | 90% | RANKING_PHASE1 / CRANK_AND_SCALING |
| **Hayabusa, aircraft rating (this script)** | 117-141 hp crank at 6,500-7,000 | 12.0-13.5 bar | 14.1-15.2 m/s | 91-112 hp crank at 5,800-6,500 | 10.5-11.5 bar | 12.6-14.1 m/s | | |

## 5. Boost: what 150-200 hp at the flange asks of a 1.34 L core

| Target at the flange | rpm | crank kW needed (gearbox 0.975) | BMEP | against Rotax 915 takeoff BMEP | against Rotax 916 takeoff BMEP | Sp | manifold pressure for that BMEP (bar abs, scaled from the NA point) |
|---|---|---|---|---|---|---|---|
| 130 hp | 6,500 | 99 | 13.7 bar | 0.86x | 0.77x | 14.1 m/s | 1.14 |
| 130 hp | 7,000 | 99 | 12.7 bar | 0.80x | 0.71x | 15.2 m/s | 1.06 |
| 130 hp | 7,500 | 99 | 11.9 bar | 0.75x | 0.66x | 16.2 m/s | 0.99 |
| 150 hp | 6,500 | 115 | 15.8 bar | 0.99x | 0.88x | 14.1 m/s | 1.32 |
| 150 hp | 7,000 | 115 | 14.7 bar | 0.92x | 0.82x | 15.2 m/s | 1.22 |
| 150 hp | 7,500 | 115 | 13.7 bar | 0.86x | 0.77x | 16.2 m/s | 1.14 |
| 175 hp | 6,500 | 134 | 18.4 bar | 1.16x | 1.03x | 14.1 m/s | 1.54 |
| 175 hp | 7,000 | 134 | 17.1 bar | 1.08x | 0.96x | 15.2 m/s | 1.43 |
| 175 hp | 7,500 | 134 | 16.0 bar | 1.00x | 0.89x | 16.2 m/s | 1.33 |
| 200 hp | 6,500 | 153 | 21.1 bar | 1.32x | 1.18x | 14.1 m/s | 1.76 |
| 200 hp | 7,000 | 153 | 19.6 bar | 1.23x | 1.09x | 15.2 m/s | 1.63 |
| 200 hp | 7,500 | 153 | 18.3 bar | 1.15x | 1.02x | 16.2 m/s | 1.52 |

## 6. Radiator and oil cooler at the Hayabusa's MCP (radiator.py, R-22 case: MCP, 80 KIAS, sea level ISA+20)

| MCP crank (kW) | coolant / oil heat (kW) | installed system (kg), grid range | design point: radiator face (cm^2), system (kg), drag (% MCP) |
|---|---|---|---|
| 68 | 55 / 12 | 19.3-22.7 | 1,760, 20.1, 1.2 % |
| 83 | 68 / 14 | 20.1-24.2 | 2,186, 21.1, 1.2 % |
| 134 (concept H, for reference) | 109 / 23 | 22.8-29.6 | 3,657, 24.6, 1.3 % |
