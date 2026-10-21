# Open conversion against concept H and a bought Aeromomentum (AER-3632)

The script behind `docs/engine/OPEN_CONVERSION_VS_H.md`. It prints markdown tables; the committed `open_conversion_tables.md` is its output. Rerun it rather than trusting the tables.

| Section | What it does | Reuses |
|---|---|---|
| 1 | each core's aircraft rating as BMEP and piston speed, against the car's own peak-torque BMEP; Aeromomentum's ratings read the same way | - |
| 2 | MCP left when one cylinder's coil or plug fails on a one-plug core (R-25) | the method of `engine_hayabusa/torsional_busa.py` section 4 |
| 3 | installed dry mass (R-37) for each option, with and without the program's normalizer; concept H at 100 / 200 / 300 hp | `engine_crank/scaling_sweep.py` (concept H's model, unchanged) |
| 4 | cost on R-35's definition, basis 1 (first engine) and basis 3 (a builder from published files) | `engine_phase0/cost_floor.py` lines; MANUFACTURING's AER-3633 estimates |
| 5 | weeks to a first ground run and a first flight, as the longest chain through a task list; builder hours | - |

```
python3 open_conversion.py > open_conversion_tables.md
```

Python 3 with numpy and scipy (imported through `scaling_sweep.py`). Sources: `docs/engine/sources/OPEN_CONVERSION_SOURCES_2026-10-21.md`.
