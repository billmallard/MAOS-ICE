## Duty, 200 hp at 3,300 rpm

| Altitude | ISA dT | ambient p (bar) | T1 (K) | PR required | compressor power (kW), eta 0.72 / 0.60 | compressor out (C), 0.72 / 0.60 | corrected flow (lb/min) |
|---|---|---|---|---|---|---|---|
| 0 ft | +0 | 1.013 | 288.1 | 1.06 | 1.0 / 1.2 | 21 / 23 | 21.2 |
| 0 ft | +20 | 1.013 | 308.1 | 1.06 | 1.1 / 1.3 | 42 / 43 | 21.9 |
| 8,000 ft | +0 | 0.753 | 272.3 | 1.43 | 6.6 / 7.9 | 40 / 48 | 27.7 |
| 8,000 ft | +20 | 0.753 | 292.3 | 1.43 | 7.1 / 8.5 | 63 / 72 | 28.7 |
| 12,000 ft | +0 | 0.644 | 264.4 | 1.68 | 9.5 / 11.3 | 50 / 62 | 31.9 |
| 12,000 ft | +20 | 0.644 | 284.4 | 1.68 | 10.2 / 12.2 | 74 / 87 | 33.1 |

## Turbocharger: turbine expansion ratio and back-pressure cost at 3,300 rpm

| Case | compressor power (kW) | turbine ER needed | p3 (bar) | p3 - p2 (bar) | pumping (kW) | share of 149 kW |
|---|---|---|---|---|---|---|
| 12,000 ft ISA+20, eta_c 0.72 | 10.2 | 1.33 | 0.90 | -0.10 | -1.5 | -1.0% |
| 12,000 ft ISA+20, eta_c 0.6 | 12.2 | 1.41 | 0.95 | -0.05 | -0.7 | -0.5% |
| 12,000 ft ISA+0, eta_c 0.72 | 9.5 | 1.30 | 0.88 | -0.12 | -1.7 | -1.2% |
| 12,000 ft ISA+0, eta_c 0.6 | 11.3 | 1.38 | 0.93 | -0.07 | -1.0 | -0.7% |
| 8,000 ft ISA+20, eta_c 0.72 | 7.1 | 1.22 | 0.95 | -0.05 | -0.7 | -0.5% |
| 8,000 ft ISA+20, eta_c 0.6 | 8.5 | 1.27 | 0.99 | -0.01 | -0.1 | -0.1% |
| SL, gate open, p3 - p2 = 0.10 bar | 0 | - | - | +0.10 | +1.4 | +1.0% |
| SL, gate open, p3 - p2 = 0.20 bar | 0 | - | - | +0.20 | +2.9 | +1.9% |

Negative p3 - p2 is a pumping gain: at altitude the turbine inlet sits below the normalized manifold.

## Supercharger on a fixed ratio: what the rpm does to the boost

Ratio set so the Rotrex makes PR 1.68 at 3,300 rpm, 12,000 ft ISA+20.

| rpm | PR | manifold (bar) | power at that rpm, % of rated | drive power (kW), eta 0.72 / 0.60 |
|---|---|---|---|---|
| 3300 | 1.68 | 1.00 | 100% | 10.7 / 12.8 |
| 3000 | 1.54 | 0.91 | 83% | 7.4 / 8.8 |
| 2800 | 1.46 | 0.86 | 73% | 5.7 / 6.8 |
| 2570 | 1.38 | 0.81 | 63% | 4.1 / 4.9 |

## Climb at full throttle with the ground-adjustable propeller (3b), 80 kt, ISA

ISA, because the propeller law is calibrated at sea-level ISA. The supercharger ratio is still the ISA+20 design above.

| Altitude | rpm, turbo | net power, turbo (% of 200 hp) | rpm, supercharger | net power, supercharger | rpm, no normalizer | net power, no normalizer |
|---|---|---|---|---|---|---|
| 0 ft | 2570 | 78% | 2516 | 73% | 2570 | 78% |
| 8,000 ft | 2899 | 88% | 2822 | 81% | 2523 | 58% |
| 12,000 ft | 3087 | 94% | 2856 | 74% | 2494 | 49% |

The supercharger is throttled to 1.00 bar wherever it could make more, but is still charged its full head times the engine flow. That is an upper bound on its drive power at low altitude; the real figure depends on how it is unloaded (bypass or inlet throttle), which is not modelled.

## Loss of the normalizer: power left at full rpm (Gagg-Ferrar)

- 8,000 ft ISA: sigma 0.786, 76% of rated, about 152 hp
- 12,000 ft ISA: sigma 0.693, 65% of rated, about 131 hp
