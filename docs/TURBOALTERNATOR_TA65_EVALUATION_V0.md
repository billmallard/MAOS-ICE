# AantFarm TA65-1 Recuperated Turboalternator — MAOS Fit Evaluation (v0)

**Status:** Evaluation complete — disposition: watchlist (not a current-path candidate)
**Date:** 2026-07-24
**Trigger:** Product announced at Oshkosh / AirVenture 2026 week
**Source:** AantFarm TA65-1 datasheet (`AantFarm_DataSheet_TA65_proof_3.22.23.pdf`, aantfarm.com — note the proof is dated March 2023; the design predates the 2026 announcement by several years. Confirm current spec status with vendor.)
**Related:** `ENGINE_SELECTION_DOWNSELECT_V1.md`, `PROPULSION_CANDIDATE_MATRIX_V1.md`, aerocommons article `2026-04-05-maos-1g1b2m-architecture-decision.md`

Scope note: R&D guidance for Experimental Amateur-Built development; not a certification claim.

---

## 1. What It Is

A 30 kg recuperated gas turbine with an integrated 60 kVA alternator — a
"turboalternator." There is no output shaft: the product of the machine is
3-phase AC electrical power. Target market is UAVs and ground power units;
the datasheet marks it **currently in development**.

This is a different category from every engine previously evaluated. All
prior candidates are prime movers that require MAOS to add a generator,
coupling, reduction drive, and cooling system. The TA65 *is* the generator.
It is, almost exactly, the "recuperated small turbine" the candidate matrix
wished existed when it noted the Allison 250-E3 regenerative prototype as an
M250 part-power mitigation that never reached production.

### Datasheet summary (sea level, ISO standard day)

| Parameter | Value |
|---|---|
| Main alternator output | 60 kW @ 705 VAC RMS 3-ph, 1267 Hz (65 kVA, PF ≈ 0.92) @ 1010 C TIT |
| Starter alternator | 5 kW @ 450 V, 3-ph (alternate voltages available) |
| Mass, complete engine w/ accessories | **30 kg (66 lb)** |
| Fuel | JP-4, JP-5, JP-8, Jet A, Jet A-1 (no mogas) |
| Fuel flow at rated power, SL | ~26 kg/hr (chart read) |
| Heat rejection (oil + alternators) | **4.5 kW total** |
| Attitude limits | pitch ±45°, roll ±30° |
| Envelope | 905 mm L × 708 mm max W (exhaust flare) × ~381 mm H |
| Architecture | 1.5-spool, two-stage axi-centrifugal compressor, two-stage radial-axial turbine, reverse-flow annular burner, **multi-pass annular exhaust recuperator** |
| Customer-provided | Output rectifier/power conditioner, start battery (225 V), air filter, alternator oil cooler, engine oil cooler, fuel boost pump (5 psi above true vapor pressure) |

### Derived performance vs altitude (1010 C TIT chart, PF 0.923 applied)

| Altitude | Electric out (kW) | Fuel (kg/hr) | SFC (g/kWh electric) |
|---|---:|---:|---:|
| SL | 60.0 | 26.0 | 433 |
| 5,000 ft | ~53.5 | ~22.5 | ~420 |
| 10,000 ft | ~47 | ~19.5 | ~414 |
| 15,000 ft | ~40.5 | ~16.5 | ~406 |
| FL180 (extrapolated) | ~37 | ~14.6 | ~400 |

Lapse ≈ 1.4 kVA per 1,000 ft, near-linear across the published band. Charts
end at 15,000 ft; FL180 is a linear extrapolation and FL250 (stretch target)
is well outside published data. Thermal efficiency at SL rated power ≈ 19%
(fuel LHV basis) — genuinely good for a 60 kW-class turbine, which is the
recuperator earning its keep. No part-load SFC data is published; turbines
throttle poorly, though recuperation flattens the part-load curve.

---

## 2. Fit Against MAOS Requirements

Anchors: `ICE-SYS-001` (100–230 kW continuous class), the 1G1B2M power
budget (155 KTAS cruise = 80 kW prop shaft = **96 kW ICE shaft**, or in
electric terms **~90 kW at the bus** after motor + controller losses
(~0.90)), and the candidate-matrix mission (700–1,000 NM, 160 KTAS min,
FL180 min).

### Single unit: fails, and altitude is the killer

- 60 kW SL electric is **60% of the 100 kW continuous floor** — and that is
  the best case.
- At FL180 output falls to ~37 kW — **~40% of the ~90 kW cruise electric
  requirement**. The aircraft cannot cruise on one TA65 at any target
  altitude; a 40 kWh battery covering a ~53 kW deficit lasts under an hour.
- The under-appreciated problem is the lapse-rate mismatch: every
  turbocharged piston candidate (Rotax 915/916, DeltaHawk compound-boosted)
  holds rated power well into the teens, while the TA65 loses ~30% by
  15,000 ft. The turbine is strongest exactly where the hybrid least needs
  it (SL, where the battery already covers takeoff) and weakest where the
  requirement lives (cruise altitude).

**Verdict: not a candidate for the 1G role in 1G+1B+2M. This is not
"a bit under-powered" — it is a 2.4x shortfall at cruise altitude.**

### Multi-unit closure: 3x is the honest number

| Config | SL electric | FL180 electric | Cruise verdict |
|---|---:|---:|---|
| 1x | 60 kW | ~37 kW | No — 40% of requirement |
| 2x | 120 kW | ~74 kW | No — ~146 KTAS max at FL180, zero recharge margin; meets 100 kW floor at SL only |
| 3x | 180 kW | ~111 kW | Yes — 90 kW cruise + ~21 kW recharge margin; meets floor across envelope |

A 3x installation covers 1,000 fpm climb at SL solo (180 kW vs ~132 kW
electric required) and the FL180 cruise point with margin. A 2x installation
is a ~145–150 KTAS / FL120–150 aircraft — below the 160 KTAS minimum
mission target.

---

## 3. System-Level Comparison (3x TA65 vs current paths)

Generator-side installed mass estimates. TA65 accessories estimated:
3x rectifier/conditioner ~20 kg, oil coolers/plumbing ~10–15 kg. Piston
paths include generator, controller, coupling, and radiators.

| System | Gen-side mass | Electric out SL / FL180 | SFC (g/kWh electric) | Fuel, 1,000 NM mission* | Mass + mission fuel |
|---|---:|---:|---:|---:|---:|
| **3x TA65** | ~120 kg | 180 / 111 kW | 400–433 (+part-load unknown) | ~270–290 kg Jet A | ~390–410 kg |
| **Rotax 916 iS + Emrax 268** | ~120 kg | ~105 / ~105 kW | ~305 | ~196 kg mogas | ~316 kg |
| **DHK235A4 + Emrax 268** | ~195 kg | ~160 / ~150 kW | ~245 | ~157 kg Jet A | ~352 kg |
| **M250-C20B + gen (part power)** | ~150 kg | large | ~600–760 | >400 kg Jet A | >550 kg |

*7.2 hr at ~90 kW bus (6.45 hr @ 155 KTAS + 45 min reserve).

Readings:

1. **Fuel penalty vs pistons is real but bounded:** +38% over the Rotax
   path (~+80 kg on the max mission), +70% over DeltaHawk. Far better than
   the M250 at part power — the recuperator plus multi-unit operation
   avoids the part-load SFC trap that defines Path T.
2. **On mass, it is a wash with the Rotax path** at max mission, and it
   wins on any shorter mission (fixed mass advantage, fuel penalty scales
   with time). It decisively beats DeltaHawk on dry mass and loses on fuel.
3. **At SL the power density is unmatched** (2.0 kW/kg electric bare,
   ~1.5 installed vs ~0.85–0.9 for the piston systems) — but altitude lapse
   erodes the advantage to roughly parity at FL180.

### What 3x buys that no current path has

- **Real generation redundancy.** The 1G1B2M decision explicitly deferred
  2G redundancy on cost (two Rotax 915s ≈ $90k before electrics). With
  three gensets, one failure at cruise leaves ~74 kW at FL180 — a
  continue-at-reduced-speed event, not an emergency. The failure ladder
  improves a full rung.
- **Unit-count power modulation.** Turbines hate part load; a 3x fleet can
  run 2 units at design point and modulate the third (or shut it down),
  keeping each machine near its SFC sweet spot. This is an architecturally
  clean answer to the turbine part-load problem — quantized power instead
  of throttled power.
- **The entire coupling problem set disappears.** No generator selection,
  no reduction drive, no torsional analysis, no motorcycle-engine TBO
  campaign, no RPM matching. Direct AC out to a rectifier.
- **~13.5 kW total heat rejection for 180 kW SL** vs ~60–80 kW of
  radiator + oil load for an equivalent piston system. This nearly
  eliminates cooling drag — worth several percent of cruise drag, i.e.
  real range recovered against the SFC penalty (not quantified here).
- Packaging freedom: three compact 30 kg pods instead of one ~120–195 kg
  engine bay. Counterweight: three fire zones, three fuel feeds, three
  inlets to filter (FOD protection is customer-provided).

---

## 4. Integration Flags

- **Bus voltage:** 705 VAC rectifies to ~950 VDC uncontrolled — above the
  decided 400 V bus and above the H3X 850/900 V class. A customer-provided
  rectifier/power conditioner is required regardless, so this becomes an
  active-rectifier/buck design point; the datasheet notes alternate output
  voltages are available (at minimum for the starter alternator). A ~950 V
  native output would fit an 800 V-class architecture far more naturally
  than 400 V — this candidate adds weight to the 800 V side of the open
  D-001 revisit.
- **Start system wants 225 V** — a DC-DC feed or bus tap; three units can
  share one start supply (sequential starts).
- **In-flight restart envelope unpublished** — matters if cruise strategy
  shuts a unit down.
- **Roll attitude limit ±30°** — a standard steep turn is 45° bank. Likely
  an oil-system sustained-attitude limit rather than a transient one
  (UAV/GPU heritage), but this must be clarified with the vendor before the
  concept goes anywhere.
- **Fuel doctrine:** Jet A only. Fully aligned with Path T/D Jet-A-forward
  thinking; ends mogas optionality (Path H doctrine) for any aircraft that
  adopts it.
- **Noise:** unmuffled small-turbine exhaust, partially tempered by the
  recuperator. No data published.

---

## 5. Risks and Unknowns

| Item | Severity | Note |
|---|---|---|
| Price unknown | **High** | UAV/defense market pricing likely. 3 units + 3 rectifiers must clear a <$100k total-propulsion budget target — plausibly the single disqualifier |
| Development status | **High** | Datasheet marked "currently in development"; proof dated 2023. Production status, lead time unknown |
| No TBO / overhaul data | High | No published life, overhaul cost, or field history |
| Part-load SFC unpublished | Medium | Mitigated by unit-count modulation, but the real curve is needed for mission math |
| No experimental-aviation precedent | Medium | UAV/GPU target market; no known manned installation |
| Altitude model ends at 15,000 ft | Medium | FL180 figures here are extrapolated; FL250 stretch target is unexplored |
| Attitude limits | Medium | See §4 |

---

## 6. Disposition

**Watchlist — do not open a funded path.** The single-unit product does not
meet the requirement floor and is disqualified for the current 1G
architecture on power alone. The 3x multi-genset concept is architecturally
attractive (redundancy, no coupling engineering, near-zero cooling drag,
quantized turbine operation) and mass-competitive with the Rotax path, at a
~+40% fuel burn and an unknown — likely prohibitive — acquisition cost on
an in-development product.

Rule of thumb from the math: the concept becomes interesting if a unit
lands somewhere below ~$30–35k with a real TBO, because 3x units + power
electronics then competes with the Rotax-916-path total while adding
redundancy no piston single can offer.

### Evidence gates (vendor inquiry — before any further work)

1. Unit price, production timeline, and lead time; availability to
   experimental amateur-built builders (not just UAV OEMs).
2. Part-load SFC curve (or fuel flow vs electrical load at fixed altitude).
3. TBO / overhaul model and cost.
4. Main alternator alternate-voltage options; recommended rectifier
   topology; whether an 800 V-class DC output package exists.
5. Altitude performance model above 15,000 ft (FL180–FL250).
6. Attitude limits: sustained vs transient; windmilling/restart envelope.
7. Noise data, inlet filtration recommendation, fire-detection/suppression
   guidance for manned installation.

### Confidence

| Claim | Confidence | Basis |
|---|---|---|
| Datasheet specs (60 kW, 30 kg, 26 kg/hr, 4.5 kW rejection) | High | Vendor datasheet (proof, 2023) |
| Altitude lapse to 15,000 ft | High | Datasheet charts (read from graph) |
| FL180 extrapolation | Medium | Linear extension of published trend |
| 3x mission fuel (~270–290 kg) | Medium | Full-load SFC + unknown part-load penalty |
| Accessory mass estimates (rectifiers, coolers) | Low-Medium | Engineering estimate; no vendor data |
| Pricing assessment | Low | No published pricing; market-class inference |
