## Raw metrics, 200 hp member

| Criterion | weight | trace | A | B | C | D | G | H |
|---|---|---|---|---|---|---|---|---|
| cost floor mid, $k | 0.25 | Bill ruling 2: <= $22k | 36 | 46 | 34 | 52 | 32 | 37 |
| parts, non-fastener | 0.15 | brief: fewer parts | 254 | 555 | 264 | 411 | 288 | 342 |
| installed dry + cooling, kg | 0.15 | R-37 (proposed) | 202 | 145 | 176 | 190 | 168 | 153 |
| drive / torsional risk, 0-10 | 0.15 | brief: propeller constraint; FL-1/FL-2 | 10 | 5.60 | 3.87 | 10 | 6 | 9 |
| fuel-burn index (BSFC x knock CR cost) | 0.10 | rulings 1 (auto gas); R-12 | 1.09 | 1.03 | 1.03 | 1.09 | 1.13 | 1.06 |
| made-from-files, 0-10 | 0.10 | brief: made from files; envelope | 6.67 | 5 | 5 | 3.33 | 2.50 | 6.67 |
| family members served, of 3 | 0.10 | ruling 4: two modules | 2 | 2 | 2 | 2 | 2.50 | 2 |
| (cost floor low end, $k, for the $22k test) | - | - | 22.6 | 28.3 | 20.7 | 31.9 | 21.5 | 23.2 |

## Weighted scores, ratio normalization

| Concept | cost | parts | mass | drive | fuel | files | family | total | rank |
|---|---|---|---|---|---|---|---|---|---|
| A | 8.8 | 10.0 | 7.2 | 10.0 | 9.4 | 10.0 | 8.0 | 9.01 | 1 |
| H | 8.7 | 7.4 | 9.4 | 9.0 | 9.7 | 10.0 | 8.0 | 8.82 | 2 |
| G | 10.0 | 8.8 | 8.6 | 6.0 | 9.1 | 3.8 | 10.0 | 8.30 | 3 |
| C | 9.5 | 9.6 | 8.2 | 3.9 | 10.0 | 7.5 | 8.0 | 8.19 | 4 |
| D | 6.1 | 6.2 | 7.6 | 10.0 | 9.4 | 5.0 | 8.0 | 7.33 | 5 |
| B | 7.0 | 4.6 | 10.0 | 5.6 | 10.0 | 7.5 | 8.0 | 7.32 | 6 |

Share of weight draws ranking each concept first: centred / flat Dirichlet
| A | B | C | D | G | H |
|---|---|---|---|---|---|
| 69% / 57% | 0% / 0% | 1% / 2% | 0% / 0% | 7% / 10% | 24% / 31% |

## Weighted scores, minmax normalization

| Concept | cost | parts | mass | drive | fuel | files | family | total | rank |
|---|---|---|---|---|---|---|---|---|---|
| H | 7.6 | 7.1 | 8.5 | 8.4 | 7.0 | 10.0 | -0.0 | 7.20 | 1 |
| A | 7.8 | 10.0 | 0.0 | 10.0 | 4.0 | 10.0 | -0.0 | 6.35 | 2 |
| G | 10.0 | 8.9 | 5.9 | 3.5 | 0.0 | -0.0 | 10.0 | 6.24 | 3 |
| C | 9.2 | 9.7 | 4.5 | -0.0 | 10.0 | 6.0 | -0.0 | 6.04 | 4 |
| B | 3.3 | 0.0 | 10.0 | 2.8 | 9.6 | 6.0 | -0.0 | 4.32 | 5 |
| D | 0.0 | 4.8 | 2.2 | 10.0 | 3.6 | 2.0 | -0.0 | 3.11 | 6 |

Share of weight draws ranking each concept first: centred / flat Dirichlet
| A | B | C | D | G | H |
|---|---|---|---|---|---|
| 9% / 15% | 0% / 2% | 5% / 11% | 0% / 0% | 19% / 21% | 67% / 51% |

## Leave-one-criterion-out (ratio normalization): winner when a criterion is removed

| removed | winner | runner-up |
|---|---|---|
| cost | A (9.09) | H (8.87) |
| parts | H (9.07) | A (8.83) |
| mass | A (9.33) | H (8.71) |
| drive | C (8.95) | A (8.83) |
| fuel | A (8.96) | H (8.72) |
| files | A (8.90) | G (8.80) |
| family | A (9.12) | H (8.91) |
