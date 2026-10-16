# Engine phase-0 analysis scripts (AER-3320)

These scripts produce the physics floors behind `docs/engine/`. They need Python 3 with numpy and scipy (tested with numpy 2.5.2 and scipy 1.18.1).

| Script | Produces | Used in |
|---|---|---|
| `engine_floor.py` | displacement, BMEP, piston speed, airflow check, heat balance, normalizing compressor duty, mass estimate per concept and family member | ARCHITECTURES.md, REQUIREMENTS.md |
| `prop_match.py` | blade-element/momentum propeller match for each drive and pitch strategy, static to 180 kt (about 15 s) | DRIVE_AND_PROP.md |
| `torsional.py` | two-inertia torsional window per drive layout | DRIVE_AND_PROP.md |
| `cost_floor.py` | first-article parts-and-services cost band per concept and family member | ARCHITECTURES.md, REQUIREMENTS.md |

To regenerate every table:

```sh
cd analysis/engine_phase0
python3 engine_floor.py --json floor.json > floor_tables.md
python3 prop_match.py --json prop.json > prop_tables.md
python3 torsional.py > tv_tables.md
python3 cost_floor.py > cost_tables.md
```

The `*_tables.md` and `*.json` files committed beside the scripts are the outputs of exactly these commands at the commit that added them.

## Fidelity boundary

Read this before trusting any number.

- **Mass** is analog scaling, +/-25 %. It is extrapolation, not design.
- **BSFC and heat split** are class values inside Heywood's ranges, not measurements of these engines.
- **Propeller static thrust** is under-predicted: figure of merit about 0.35-0.4 against about 0.6-0.75 real, from the crude post-stall model. Use static thrust for rank order only. The efficiencies from 60 to 180 kt are in the realistic range.
- **The torsional model is a window, not an analysis.** Its inertias are assumed.
- **Cost** mixes MANUFACTURING-sourced lines, PROPULSION estimates and unquoted placeholders, each tagged in the script.
