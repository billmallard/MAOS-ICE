## 1. Crank torque at takeoff, full throttle (mid inertias and masses)

| Engine | rpm | IMEP (bar) | peak cylinder pressure (bar) | mean torque (N m) | major order | its amplitude (N m) | amplitude / mean | 2nd-order inertia part alone (N m) |
|---|---|---|---|---|---|---|---|---|
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 7,000 | 14.6 | 71 | 156 | 2 | 280 | 1.80 | 449 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 5,800 | 12.8 | 64 | 138 | 2 | 88 | 0.63 | 238 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 5,800 | 11.9 | 56 | 282 | 4 | 184 | 0.65 | 44 |

## 2. Two-inertia window (phase-0 method), firing band idle to 105 %

| Engine | J_e (kg m^2) | J_p reflected (kg m^2) | firing band (Hz) | soft: k below (N m/rad) | stiff: k above (N m/rad) |
|---|---|---|---|---|---|
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 0.020 | 0.070 | 57 - 245 | 1,264 | 57,664 |
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 0.050 | 0.070 | 57 - 245 | 2,372 | 108,231 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 0.030 | 0.102 | 47 - 203 | 1,274 | 58,876 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 0.060 | 0.102 | 47 - 203 | 2,076 | 95,894 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 0.050 | 0.174 | 120 - 406 | 14,124 | 394,717 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 0.080 | 0.174 | 120 - 406 | 19,925 | 556,841 |

## 3. Alternating torque at the gear mesh, divided by mean torque, worst point idle to 105 % on a propeller curve

Coupling tuned so the first mode sits at a fraction of the idle major-order frequency. Above 1.0 the mesh torque reverses.

The last row per engine is stiff tuning: f1 at 1.25 x the major-order frequency at 105 % rpm.

| Engine | f1 / idle firing frequency | k (N m/rad, crank side) | f1 (Hz) | wind-up at takeoff mean torque, crank side (deg) | worst ratio, mid inertias | at rpm | worst ratio, light engine + heavy propeller + heavy pistons | ratio at takeoff rpm, mid |
|---|---|---|---|---|---|---|---|---|
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 0.50 | 833 | 28 | 10.7 | 1.09 | 1,700 | 1.22 | 0.04 |
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 0.70 | 1,633 | 40 | 5.5 | 2.88 | 1,700 | 3.22 | 0.07 |
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 1.50 | 7,497 | 85 | 1.2 | 9.09 | 2,424 | 9.13 | 0.26 |
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 3.00 | 29,989 | 170 | 0.3 | 11.10 | 2,424 | 12.55 | 1.61 |
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 5.40 | 97,322 | 306 | 0.1 | 5.58 | 1,700 | 6.72 | 3.70 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 0.50 | 747 | 23 | 10.6 | 1.27 | 1,400 | 1.41 | 0.02 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 0.70 | 1,464 | 33 | 5.4 | 3.38 | 1,400 | 3.73 | 0.03 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 1.50 | 6,721 | 70 | 1.2 | 14.87 | 2,001 | 15.87 | 0.11 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 3.00 | 26,883 | 140 | 0.3 | 13.39 | 2,122 | 14.84 | 0.66 |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 5.44 | 88,315 | 254 | 0.1 | 7.01 | 2,482 | 7.70 | 1.68 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 0.50 | 7,289 | 60 | 2.2 | 0.54 | 1,800 | 0.59 | 0.02 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 0.70 | 14,286 | 84 | 1.1 | 1.49 | 1,800 | 1.63 | 0.03 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 1.50 | 65,599 | 180 | 0.2 | 7.08 | 2,680 | 7.69 | 0.15 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 3.00 | 262,394 | 360 | 0.1 | 3.48 | 5,320 | 3.76 | 2.11 |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 4.23 | 521,461 | 508 | 0.0 | 1.95 | 2,130 | 2.12 | 1.31 |

## 4. One cylinder dead (a single-plug engine losing one coil, plug or injector), soft coupling at 0.5 x idle firing frequency

All orders to 3 x z/2 are summed (half-orders appear when a cylinder stops firing). The live cylinders are held at the
IMEP that keeps the same mean torque the propeller curve asks for, until they reach the takeoff IMEP (then rpm falls).

| Engine | f1 (Hz) | crank rpm where order 0.5 / 1 / 1.5 cross f1 | worst ratio, all live | worst ratio, one dead | at rpm | worst ratio, one dead, in flight (above 45 % rpm) | at rpm | brake power left at the MCP rpm, one dead (share of MCP) |
|---|---|---|---|---|---|---|---|---|
| Hayabusa I4, aircraft takeoff 7,000 rpm, 2.92:1 | 28 | 3,400 / 1,700 / 1,133 | 1.09 | 4.75 | 1,700 | 3.24 | 3,407 | 72% |
| Rotax 912 ULS, flat-4, 5,800 rpm, 2.43:1 | 23 | 2,800 / 1,400 / 933 | 1.27 | 5.04 | 1,400 | 3.41 | 2,742 | 71% |
| Concept B flat-8 (phase 0), 5,800 rpm, 2.4:1 | 60 | 7,200 / 3,600 / 2,400 | 0.54 | 2.44 | 1,800 | 1.78 | 3,563 | 85% |
