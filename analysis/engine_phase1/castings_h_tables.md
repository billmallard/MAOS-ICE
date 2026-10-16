## Regression: MANUFACTURING's six-casting result, re-aggregated

first-op first engine $9.8k-33.9k; NRE-once marginal $1.7k-4.6k; NRE $7.2k-26.7k; castings q1 $6.2k-14.7k, q5 $5.1k-11.2k (envelope 9.3: $9.8k-33.9k; $1.7k-4.6k; $7.2k-26.7k; $6.2k-14.7k, $5.1k-11.2k)

## Per casting after the rulings

| Part | Qty / engine | Part numbers | First-op qty 1 | First-op marginal, NRE once | NRE per part number | Casting qty 1 | Casting qty 5 |
|---|---|---|---|---|---|---|---|
| case half, bank merged | 2 | 2 | $2.4k-8.3k | $0.7k-1.8k | $1.7k-6.5k | $1.5k-3.1k | $1.3k-2.5k |
| head, one part number, 4-axis | 2 | 1 | $2.1k-7.3k | $0.4k-1.1k | $1.7k-6.2k | $0.9k-2.4k | $0.7k-1.7k |

| Per engine | Six castings (9.3) | Four castings (rulings) | Change |
|---|---|---|---|
| first-op, first engine (all NRE) | $9.8k-33.9k | $7.2k-24.4k | -2.6k / -9.5k |
| first-op, each of 5, NRE once | $1.7k-4.6k | $1.5k-3.5k | -0.2k / -1.1k |
| program NRE, once | $7.2k-26.7k | $5.1k-19.2k | -2.1k / -7.5k |
| castings, first engine | $6.2k-14.7k | $4.9k-10.9k | -1.2k / -3.7k |
| castings, each of 5 | $5.1k-11.2k | $4.1k-8.4k | -1.0k / -2.8k |

## What each ruling buys, applied one at a time (first-op + castings, per engine)

| Casting set | Basis 1: first engine | Basis 2: each of 5, NRE once | Program NRE |
|---|---|---|---|
| six castings (9.3) | $15.9k-48.6k | $6.8k-15.8k | $7.2k-26.7k |
| #1 bank merged into case half | $14.2k-43.3k | $5.7k-12.8k | $6.8k-25.5k |
| #1 + #3 one head part number | $12.3k-36.3k | $5.7k-12.7k | $5.1k-19.2k |
| #1 + #3 + #4 head on 4-axis | $12.1k-35.3k | $5.6k-11.9k | $5.1k-19.2k |

## Head: 4-axis against 5-axis, per head (one part number either way)

- 5-axis: marginal first-op at a batch of 10 heads $0.3k-1.0k
- 4-axis: marginal first-op at a batch of 10 heads $0.2k-0.6k

## Scrap the merge adds (RT before first-op; P_SCRAP assumed)

- p = 0.05 per pour: expected scrap per engine, separate $0.5k, merged $0.6k, merge adds $0.1k (high-end casting cost)
- p = 0.20 per pour: expected scrap per engine, separate $2.0k, merged $2.2k, merge adds $0.2k (high-end casting cost)

## Liner mass per cylinder

- Darton MID wet liner: 2.76-2.96 kg iron; x6 = 16.6-17.8 kg
- dry sleeve, closed deck: 1.15 kg iron + 1.12 kg A356 = 2.27 kg; x6 = 13.6 kg
- wet-liner penalty: 2.9-4.1 kg per engine (not the 15-18 kg gross: the dry option needs its own aluminum wall and deck)
- iron alone, MID against a 3 mm dry sleeve: 9.6-10.8 kg per engine (the saving if the sleeve's aluminum wall is left out)
- wet liner, 5.6 mm wall: about 2.78 kg; hoop stress at 70 bar peak 66 MPa
- wet liner, 3.5 mm wall: about 1.82 kg; hoop stress at 70 bar peak 105 MPa

## Main oil gallery

- oil heat 27 kW at 200 hp -> 60 L/min at a 15 K oil rise; 25 x D over 280 mm per side -> D >= 11.2 mm
- 12 mm: 23 x D per side, 8.9 m/s, Re 10687, full-flow drop over 560 mm 0.49 bar (upper bound)
- 14 mm: 20 x D per side, 6.5 m/s, Re 9161, full-flow drop over 560 mm 0.24 bar (upper bound)

## HMC envelope for the doweled pair

- pair 563 x 331 x 470 mm (z across both decks): swing needed about 833 mm
- pair 563 x 331 x 650 mm (z across both decks): swing needed about 960 mm

## 200 hp cost floor, concept H (low / mid / high; mid = geometric mean)

| Step | Basis 1: first engine, carries all NRE | Basis 2: each engine of 5, NRE paid once |
|---|---|---|
| 0. Phase 1 as published (RANKING_PHASE1 section 1) | $23.2k / $36.8k / $58.4k | $23.2k / $36.8k / $58.4k |
| 1. Envelope 9.7 line items, six castings | $35.8k / $55.9k / $87.3k | $26.7k / $38.1k / $54.5k |
| 2. + rulings 9.5 #1-#4 (four castings) | $32.0k / $48.7k / $74.1k | $25.5k / $35.9k / $50.6k |
| 3. + MACHINE_SHOP double counts removed | $31.7k / $48.0k / $72.8k | $25.1k / $35.2k / $49.3k |

Program NRE outside basis 2 (CAM + fixtures, four castings, three part numbers): $5.1k-19.2k once.
Basis 2 with that NRE spread over 5 engines instead: $26.1k - $53.2k.

### Line items, step 3

| Line | Basis 1 | Basis 2 |
|---|---|---|
| first-op | $7.2k-24.4k | $1.5k-3.5k |
| castings | $4.9k-10.9k | $4.1k-8.4k |
| crank | $6.6k-9.4k | $6.6k-9.4k |
| catalog per-cylinder set | $2.7k-4.5k | $2.7k-4.5k |
| normalizing | $2.0k-4.5k | $2.0k-4.5k |
| FADEC | $1.5k-4.0k | $1.5k-4.0k |
| liners | $1.8k-2.7k | $1.8k-2.7k |
| cooling | $0.8k-1.9k | $0.8k-1.9k |
| seats and guides | $0.6k-1.5k | $0.6k-1.5k |
| cam | $0.5k-1.5k | $0.5k-1.5k |
| misc | $0.6k-1.5k | $0.6k-1.5k |
| crank damper | $0.4k-1.5k | $0.4k-1.5k |
| starter, alternator | $0.4k-0.9k | $0.4k-0.9k |
| drive (direct) | $0.3k-0.8k | $0.3k-0.8k |
| fuel | $0.4k-0.8k | $0.4k-0.8k |
| exhaust | $0.3k-0.8k | $0.3k-0.8k |
| second coil per cylinder | $0.3k-0.6k | $0.3k-0.6k |
| machine shop | $0.3k-0.6k | $0.3k-0.6k |
