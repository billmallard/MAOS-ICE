# Engine phase-1 analysis scripts (AER-3326)

These scripts rank the auto-gas concepts and the drive options for the 200 hp member, and size the radiator. They reuse the phase-0 models in `../engine_phase0/` unchanged, loaded by path. They need Python 3 with numpy and scipy (tested with numpy 2.5.2 and scipy 1.18.1).

| Script | Produces | Used in |
|---|---|---|
| `knock.py` | knock-limited compression ratio per concept on MON 85 and MON 82, calibrated on five running engines | RANKING_PHASE1.md section 3 |
| `member_200.py` | variant H physics floor; part count and cost floor for every candidate at 200 hp | sections 2, 4, 5 |
| `rank.py` | weighted decision matrix, two normalizations, Monte Carlo over weights, leave-one-out | section 4 |
| `torsional_h.py` | multi-mass torsional model of the direct-drive crank and propeller, with order crossings | section 6 |
| `drive_match.py` | phase-0 BEM propeller model run at concept H's rpm (3,300) | section 7 |
| `drive_rank.py` | drive and propeller ranking at concept H's rpm | section 7 |
| `radiator.py` | radiator and oil cooler at MCP / Vy / ISA+20 C, with a 12,000 ft cross-check | section 8 |
| `h_quote_estimate.py` | MANUFACTURING's bottom-up first-op and casting estimate for concept H (AER-3328) | MANUFACTURING_ENVELOPE.md section 9 |
| `cost_v1.py` | 200 hp cost floor on envelope v1, builder and first-engine bases; H, H with DFM levers, A | RECOST_PHASE1B.md sections 3, 5 |
| `rank_v1.py` | the phase-1 ranking rerun on v1 costs | RECOST_PHASE1B.md section 4 |
| `normalizer_h.py` | turbo versus supercharger: duty, back-pressure, rpm-dependent boost, climb power | RECOST_PHASE1B.md section 6 |
| `castings_h.py` | concept H after the 9.5 rulings: four castings, scrap, liner mass, gallery, HMC envelope, cost floor on both bases | CASTINGS_H.md |

To regenerate every table:

```sh
cd analysis/engine_phase1
python3 knock.py > knock_tables.md
python3 member_200.py > member_200_tables.md
python3 rank.py > rank_tables.md
python3 torsional_h.py > torsional_h_tables.md
python3 radiator.py > radiator_tables.md
python3 h_quote_estimate.py > h_quote_estimate_tables.md
python3 cost_v1.py > cost_v1_tables.md
python3 rank_v1.py > rank_v1_tables.md
python3 normalizer_h.py > normalizer_h_tables.md
python3 castings_h.py > castings_h_tables.md
python3 drive_match.py --json drive_match.json > drive_match_tables.md   # about 20 s
python3 drive_rank.py > drive_rank_tables.md                             # reruns drive_match, about 20 s
```

The `*_tables.md` and `drive_match.json` files committed beside the scripts are the outputs of exactly these commands at the commit that added them.

## Fidelity boundary

Read this before trusting any number. The phase-0 boundary (`../engine_phase0/README.md`) still applies to everything reused from it.

- **Knock** is a one-step Livengood-Wu index with the Douaud-Eyzat delay correlation. It is calibrated on four air-cooled engines, which agree within 25 %, and on one liquid-cooled-head engine, which sits 1.9x higher. It ranks geometries; it does not predict a knock limit for a head that does not exist yet. The avgas anchors read the lean rating as MON, which is an approximation.
- **Part count** is a bill-of-materials enumeration by part class, written from each concept's layout. It is not a drawing tree. Fasteners are an estimate.
- **Cost** is the phase-0 line items plus one added line: the cylinder-jacket castings phase 0 left out. The job-shop first-op line is still unquoted and is the largest line on the bill.
- **Torsional**: every inertia and stiffness is assumed from catalog-class dimensions. Mode frequencies are good to perhaps +/-20 %. Excitation amplitude is not computed, so a crossing is a flag for the dynamometer survey, not a stress.
- **Cost v1** (`cost_v1.py`): every v1 line is MANUFACTURING's [E] on sourced rates, not a quote. Concept A's casting envelopes are PROPULSION's, scaled from H's.
- **Castings** (`castings_h.py`): MANUFACTURING's estimator with PROPULSION's hour and fixture deltas for the post-ruling casting set ([E], named in the script); the casting boxes come from the coarse STEP in `cad/concept_h/`. The scrap rate and the 70 bar peak pressure are assumed.
- **Normalizer** (`normalizer_h.py`): 1-D, ideal gas, assumed efficiencies; the compressor map is not checked. The propeller law is a rho n^3 approximation calibrated at one point; it gives the rpm trend, not the value.
- **Radiator**: the Chang-Wang j-factor is a published correlation, but its geometry range was not checked against this core. The liquid-side resistance, the f/j ratio, duct losses and the system line items are assumed. Vy is assumed (there is no airframe).
