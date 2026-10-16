# Engine program documents (ORG-009)

The open, liquid-cooled piston engine family: 100, 200 and 300 hp. It is experimental, untested, and not certified or certifiable.

The older documents one level up (`docs/*.md`) are the hybrid and genset history. They were mined for vendor evidence, and they do not set direction.

| Document | What it is | Owner |
|---|---|---|
| [REQUIREMENTS.md](REQUIREMENTS.md) | v0 requirements; every line tagged Bill's brief or proposed | PROPULSION |
| [ARCHITECTURES.md](ARCHITECTURES.md) | seven engine concepts with physics floors (phase 0); ranked in RANKING_PHASE1.md | PROPULSION |
| [DRIVE_AND_PROP.md](DRIVE_AND_PROP.md) | nine ways to match engine to propeller (phase 0); ranked in RANKING_PHASE1.md | PROPULSION |
| [RANKING_PHASE1.md](RANKING_PHASE1.md) | phase 1: auto-gas concepts and drive options ranked for the 200 hp member; convergence pick; radiator sizing (AER-3326) | PROPULSION |
| [RECOST_PHASE1B.md](RECOST_PHASE1B.md) | phase 1b: concept H re-costed on MANUFACTURING's estimates, the $22k test, turbo versus supercharger (AER-3329) | PROPULSION |
| [FAILURE_LEDGER.md](FAILURE_LEDGER.md) | single failures and what they leave, held for SAFETY | PROPULSION |
| [MANUFACTURING_ENVELOPE.md](MANUFACTURING_ENVELOPE.md) | what can be cast, machined, cut or bought, at what price (v0, AER-3321; v1 adds concept H estimates and normalizer sourcing, AER-3328) | MANUFACTURING (committed verbatim) |
| [sources/](sources/) | vendor data, prices and masses, with read dates | PROPULSION |

The numbers come from the scripts in [`analysis/engine_phase0/`](../../analysis/engine_phase0/) and [`analysis/engine_phase1/`](../../analysis/engine_phase1/). Rerun them rather than trusting the tables.
