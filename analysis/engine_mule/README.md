# FADEC flight mule (AER-3631)

The script behind `docs/engine/FADEC_MULE.md`. It prints markdown tables; the committed `mule_tables.md` is its output. Rerun rather than trusting the table.

| Script | What it does |
|---|---|
| `mule.py` | each vendor's rating as BMEP and implied volumetric efficiency against the donor engine's published torque; power left after one lane, coil, coil-pack or injector failure on a 4-cylinder; the second-injector size for E15; the cost of the FADEC substitution and of each airframe route |

```
python3 mule.py > mule_tables.md
```

Python 3, standard library only. Sources: `docs/engine/sources/FADEC_MULE_SOURCES_2026-10-21.md`.
