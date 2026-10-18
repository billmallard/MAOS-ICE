# Crank routes and the 200 hp scaling sweep (AER-3411)

These scripts back `docs/engine/CRANK_AND_SCALING.md`. They reuse the phase-1 models in `../engine_phase1/` unchanged (`castings_h.py`, `knock.py`, `torsional_h.py`, `normalizer_h.py`, `drive_rank.py`), loaded by path. They need Python 3 with numpy, scipy and matplotlib (tested with matplotlib 3.11.2).

| Script | Produces | Used in |
|---|---|---|
| `crank_routes.py` | crank cost model calibrated on three sourced anchors; routes 1-5 costed on the first-engine basis; press-fit slip, roller big-end L10, cast-crank fatigue, 180-degree V6 firing and couples, 3-throw torsion; the mass-production crank survey | sections 2, 3 |
| `scaling_sweep.py` | the 200 hp sweep over 4/6/8 cylinders and 2,600-6,000 rpm, by crank route, and the mass-production cranks on the same model | section 4 |
| `plot_sweep.py` | `sweep_200hp.png` (called by `scaling_sweep.py --plot`) | the figure at the top |
| `normalizer_redo.py` | turbo against supercharger with the supercharger's ratio set at the climb rpm | section 6 |
| `drive_rank_v2.py` | the phase-1 drive ranking with the gearbox scored as proven-class | section 5 |

To regenerate every table and the figure:

```sh
cd analysis/engine_crank
python3 crank_routes.py > crank_routes_tables.md
python3 scaling_sweep.py --plot > scaling_sweep_tables.md
python3 normalizer_redo.py > normalizer_redo_tables.md
python3 drive_rank_v2.py > drive_rank_v2_tables.md   # about 15 s; reruns drive_match.py
```

Every figure is an estimate or an assumption unless a source is named; sources are in `docs/engine/sources/CRANK_SOURCES_2026-10-18.md`. None is a quote.
