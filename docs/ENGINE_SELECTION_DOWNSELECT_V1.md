# MAOS-ICE Engine Selection Downselect (v1)

Purpose: maintain a formal, versioned shortlist of ICE prime movers for MAOS generator-drive architecture.

Scope note: This matrix is R&D guidance for Experimental Amateur-Built development and is not a certification claim.

## Source Baseline

This document is seeded from the published program analysis and then maintained in-repo as the formal downselect artifact.

- `aerocommons/content/articles/2026-04-05-maos-engine-comparison-matrix.md`
- `docs/ARTICLE_KNOWLEDGE_MIGRATION_2026Q2.md`

## Selection Criteria

1. Continuous power for generator drive role
2. Engine mass impact on subsystem and aircraft budgets
3. Power-to-weight ratio
4. Cooling architecture suitability
5. Reliability and operating precedent
6. Fuel compatibility (mogas preference)
7. Acquisition and lifecycle cost
8. Availability and lead-time practicality

## Candidate Comparison Matrix

| Engine | Displacement | Power (hp/kW) | Weight (kg) | HP/kg | Cooling | Fuel | Aviation Use | Cost Est. | Status |
|---|---|---|---:|---:|---|---|---|---|---|
| Flygas GAS 418S | 1,800 cc | 180 hp / 132 kW @ 5,800 RPM | < 85 | 2.2 | Liquid | 98 octane / mogas | UAV, experimental | EUR20k-EUR30k (est) | Viable |
| UL Power UL520iS | 3,120 cc | 200 hp / 147 kW @ 5,800 RPM | ~118 | 1.7 | Liquid heads / air cylinders | Mogas | Experimental and kit support | USD45k-USD55k | Viable |
| Kawasaki I4 Turbo | 999 cc | 148 hp / 110 kW max continuous (200 hp / 149 kW takeoff) | 85 dry | 1.74 cont / 2.35 TO | Liquid | Mogas + FADEC | Experimental derivatives | USD15k-USD25k (est) | Viable (packaging/integration risk) |
| Kawasaki I6 Turbo | 2,069 cc | 350 hp / 261 kW max continuous (375 hp / 280 kW takeoff) | 127 dry | 2.76 cont / 2.95 TO | Liquid | Mogas + FADEC | Experimental derivatives | TBD | Marginal (oversized for current architecture) |
| Rotax 912 iS | 1,352 cc | 100 hp / 73.5 kW @ 5,800 RPM | 72 | 1.39 | Liquid heads / air cylinders | Mogas | Widely used LSA/experimental | USD28k-USD32k | Viable (low margin) |
| Rotax 915 iS | 1,352 cc | 141 hp / 103.5 kW @ 5,800 RPM | 83 | 1.70 | Liquid heads / air cylinders | Mogas | Proven LSA/experimental | USD42k-USD48k | Viable |
| Rotax 916 iS | 1,352 cc | 160 hp / 118 kW @ 5,800 RPM | ~85 | 1.88 | Liquid heads / air cylinders | Mogas | New certified family | USD50k+ | Viable |
| Viking 130 | 1,500 cc | 130 hp / 97 kW cont | 108 dry | 1.20 | Liquid | Mogas | Experimental, Honda-based | USD14k-USD18k | Viable (heavy) |
| Aeromomentum AM13 | 1,300 cc | 100 hp / 73.5 kW @ 5,500 RPM | 68 | 1.47 | Liquid | Mogas | Experimental | USD12k-USD16k | Viable (marginal power margin) |
| Aeromomentum AM15 | 1,500 cc | 115 hp / 84.5 kW @ 5,500 RPM | 75 | 1.53 | Liquid | Mogas | Experimental | USD14k-USD18k | Viable |
| Hirth F-30 | 1,494 cc | 85 hp / 62 kW @ 6,500 RPM | 62 | 1.37 | Liquid | Mogas | Ultralight, experimental | EUR12k-EUR16k | Marginal (under target power) |
| Honda CB650 (modified) | 2,596 cc | 67 hp / 50 kW stock | 140-160 installed | 0.42-0.48 | Liquid | Mogas | No direct aviation pedigree | USD7k-USD12k + mods | Marginal |
| Honda CB500 (modified) | 942 cc | 47 hp / 35 kW stock | 130-150 installed | 0.31-0.36 | Liquid | Mogas | No direct aviation pedigree | USD5k-USD10k + mods | Marginal |
| Hirth F-23 | 1,006 cc | 50 hp / 37 kW @ 6,500 RPM | 45 | 1.11 | Liquid | Mogas | Ultralight, experimental | EUR8k-EUR12k | Disqualified |

## Working Recommendations

### Single-engine variant (1x engine, 75 kW generator)

| Priority | Engine | Rationale |
|---|---|---|
| Best overall | Rotax 916 iS | High confidence package with strong support and margin |
| Best value-performance balance | Rotax 915 iS | Proven reliability with solid power reserve |
| High-performance option | Flygas GAS 418S | Exceptional power density; needs availability/cost closure |
| Budget-conscious path | Viking 130 | Meets power at lower acquisition cost but higher mass |
| Conservative fallback | Rotax 912 iS | High supportability, limited margin |

### Twin-engine variant (2x engines, 150 kW total)

| Priority | Engine | Rationale |
|---|---|---|
| Best overall | Rotax 915 iS (2x) | Proven, balanced, and supportable |
| High-performance option | Flygas GAS 418S (2x) | Strong power-to-weight pending procurement confidence |
| Best value | Viking 130 (2x) | Cost-favorable with clear mass trade penalty |
| Budget alternative | Aeromomentum AM15 (2x) | Lower cost, less field-proven |

## Preliminary Dimensional Reference (Packaging)

These values are preliminary planning inputs for CAD envelope studies and must be replaced by vendor installation drawings before commitment.

Brochure caveat: values are target specifications, and dry weight excludes radiator and exhaust.

| Engine | Dimensions (H x W x L) |
|---|---|
| Kawasaki I4 Turbo | 670 mm x 640 mm x 600 mm |
| Kawasaki I6 Turbo | 550 mm x 580 mm x 850 mm |

## Kawasaki Brochure Evidence Notes

Observed from `docs/prepare_for_take_off_dl.pdf`:

1. "Hybrid Propulsion" is shown visually as a product-line row, including engine imagery with an attached cylindrical module suggestive of a generator/motor package.
2. No explicit generator model, electrical output (kW), voltage, mass, cooling load, or coupling interface specification is provided in text.
3. Inline 4 turbo is listed with "Gearbox: Optional" and output shaft speed of 8,500 rpm.
4. Inline 6 turbo is listed with "Integrated Gearbox" and output shaft speed of 2,600-2,800 rpm.

Implication for MAOS trade work: brochure evidence supports a likely hybrid-intent architecture signal, but does not yet provide enough hard data to treat a packaged genset as confirmed hardware.

## Online Evidence Snapshot (2026-04-16)

1. Official Kawasaki Motors news lists a strategic partnership with Dronamics and links to an official PDF release (`global.kawasaki.com/news_250918-1e.pdf`).
2. The official Kawasaki-Dronamics PDF confirms aero piston engine integration activity for the Black Swan UAV platform and full-lifecycle cooperation (R&D integration engineering, flight testing, and validation).
3. The official Kawasaki-Dronamics PDF does not provide generator package specifications (no generator power rating, voltage, mass, cooling load, or electrical architecture details).
4. AIN and FLYER coverage are consistent on the core engine program trajectory (inline 4 and inline 6, certification target around 2030, hydrogen/e-fuel transition intent).
5. VoltAero-related reporting (GlobalAir summary quoting AirVenture statements) describes a separate hybrid power unit architecture using a Kawasaki H2SX-derived thermal engine plus electric motor (HPU 210), but this is a partner system and not explicit proof that Kawasaki's new clean-sheet inline 4 includes a standardized bundled generator product.

Working conclusion: there is strong evidence of hybrid and integration intent, but still no public, official spec sheet for a Kawasaki inline-4 packaged genset offering.

## Weight-Budget Reality Check

The historical internal target of `< 65 kg` per engine is not met by most viable candidates. Current guidance is to treat this as an integration negotiation input, not an automatic reject criterion.

## Minimum Evidence Required Before Final Downselect

1. Vendor-confirmed pricing and lead time (date-stamped).
2. Continuous-power thermal sustainment evidence for expected mission duty cycle.
3. Generator coupling compatibility (RPM band, reduction strategy, torsional implications).
4. Support model and spare strategy acceptable for experimental owner-operator context.
5. Verified fit against current aircraft-level mass and CG budget assumptions.

## Next Actions

1. Request formal quotes and lead times for Rotax 915 iS, Rotax 916 iS, Flygas GAS 418S, and Viking 130.
2. Publish reduction-drive assumptions for each top candidate in a follow-on coupling note.
3. Run weighted scoring review at S1-C trade closure board and record disposition.
