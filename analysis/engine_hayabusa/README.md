# Hayabusa platform evaluation (AER-3525)

Scripts behind `docs/engine/HAYABUSA_PLATFORM.md`. Each prints markdown tables; the committed `*_tables.md` are their output. Rerun rather than trusting the tables.

| Script | What it does | Reuses |
|---|---|---|
| `rating_busa.py` | motorcycle ratings as BMEP and piston speed; knock-limited CR at sustained full throttle on MON 85; the aircraft takeoff and MCP rating with implied volumetric efficiency; boost needed for 150-200 hp; radiator system at the Hayabusa's MCP | `engine_phase1/knock.py`, `engine_phase1/radiator.py` (imported, unchanged) |
| `torsional_busa.py` | crank torque from a cylinder-pressure cycle plus reciprocating inertia, its firing orders, and the alternating torque at the gear mesh of a damped geared drive, against the Rotax 912 and concept B; the one-cylinder-dead case | phase-0 two-inertia window method (`engine_phase0/torsional.py`) |
| `mass_cost_busa.py` | installed dry mass, first-engine cost (basis 1), builder hours, and a durability bracket from Radical race hours | `engine_phase0/cost_floor.py` lines; the gearbox from CRANK_AND_SCALING section 5 |

```
python3 rating_busa.py > rating_busa_tables.md
python3 torsional_busa.py > torsional_busa_tables.md
python3 mass_cost_busa.py > mass_cost_busa_tables.md
```

Python 3 with numpy and scipy (numpy 2: `np.trapezoid`). Sources: `docs/engine/sources/HAYABUSA_SOURCES_2026-10-19.md`.
