# MAOS Powertrain Trade Study — Integrated Combos Toward $50k (v1)

**Status:** Analysis — Experimental Amateur-Built Category. Not a certification claim, not a hardware commitment.
**Date:** 2026-08-09
**Owner:** PROPULSION
**Origin:** [AER-57](/AER/issues/AER-57) — "Propulsion trade study - exhaustive powertrain catalog + ranked scorecard toward $50k," child of [AER-56](/AER/issues/AER-56)
**Standing architecture (not reopened here):** 1G + 1B + 2M series hybrid per `2026-04-05-maos-1g1b2m-architecture-decision`. This document evaluates **components within that architecture** — one ICE-generator set, one battery, two propulsion motors on a coaxial contra-rotating prop. Twin-ICE ("2G") pairings explored earlier in `PROPULSION_CANDIDATE_MATRIX_V1.md` (Config B, Path H2/H3) are **out of scope here**, not because they score badly, but because they reopen an architecture question AER-57 does not authorize revisiting.

**Extends, does not restart:** `2026-04-05-maos-engine-comparison-matrix`, `2026-04-05-maos-generator-selection`, `2026-04-05-maos-drivetrain-economics`, `2026-04-05-maos-propulsion-redundancy-battery`, `ENGINE_SELECTION_DOWNSELECT_V1.md`, `PROPULSION_CANDIDATE_MATRIX_V1.md`, `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md`, `MOTOR_CONTROLLER_TRADE_MATRIX.md`, `TURBOALTERNATOR_TA65_EVALUATION_V0.md`.

---

## 0. Cost Scope

**Default scope (per AER-56/AER-57), pending Bill's answer on the open cost-boundary question in AER-56:**

> Total **installed powertrain hardware cost** = ICE + generator/rectifier + generator controller + battery pack + BMS + 2× propulsion motors + motor controllers + reduction/coupling + prop(s). New parts, single experimental-build quantity, **ex-airframe, ex-installation-labor.**

Every combo below shows:
- **Total installed hardware cost** (scored against the $50k line)
- **Electric-hardware-only subtotal** (generator + 2× motors + controllers) broken out separately, so a re-score against a narrower boundary (e.g., "electric side only," which is closer to what `MOTOR_CONTROLLER_TRADE_MATRIX.md`'s existing budget track scores) is a one-line lookup, not a redo.

If Bill's answer on AER-56 changes the boundary (e.g., includes installation labor, or excludes prop/reduction as "airframe"), every combo's total re-derives from the same line-item table — nothing here needs re-research, only re-summation.

---

## 1. Requirement Envelope — Owner and Reason on Every Line

This is Step 1 per AER-57: reconcile the ICE power requirement before sizing anything to it.

| # | Parameter | Value | Owner | Reason / Traceability |
|---|---|---|---|---|
| 1 | MTOW | 2,600 lb | AERO | Mission baseline cited in `maos-1g1b2m-architecture-decision` power budget |
| 2 | Cruise speed floor | 155 KTAS | AERO | AER-57 mission floor |
| 3 | L/D at cruise | 14 | AERO | `maos-1g1b2m-architecture-decision` power budget |
| 4 | Drivetrain efficiency (generator × controller × motor) | 0.84 | PROPULSION | `maos-1g1b2m-architecture-decision`; electrical chain only, excludes prop efficiency |
| 5 | Implied propeller efficiency | ≈0.82 (not separately published) | **Derived by PROPULSION — flag for AERO to confirm or correct** | Back-solved below (§1.1); needed to reconcile the published 80 kW shaft figure with the aero power equation. Not yet an owned, published number. |
| 6 | Cruise shaft power at prop | 80 kW / 108 hp | AERO | `maos-1g1b2m-architecture-decision` power budget table |
| 7 | **Cruise ICE electrical requirement (continuous)** | **96 kW / 128 hp** | Derived: PROPULSION, from AERO inputs #1–4, #6 | 80 kW ÷ 0.84 = 95.2 → 96 kW. **This is the mission-traceable ICE continuous minimum.** |
| 8 | Climb 700 fpm ICE requirement | 120 kW / 161 hp | AERO/PROPULSION | Power budget table; ICE alone, negligible battery draw — this is the working "no-battery-climb" target the Rotax 916 iS baseline was picked against |
| 9 | Climb 1,000 fpm bus demand | 141 kW electrical | AERO/PROPULSION | Power budget table; ICE supplies its rated output, battery supplies the remainder |
| 10 | Climb 1,200 fpm (max) bus demand | 155 kW electrical | AERO/PROPULSION | Power budget table; battery supplies ~30 kW of this at the Rotax-916-class ICE baseline |
| 11 | Battery emergency reserve | 30 min @ 60 kW electrical → ~40 kWh pack | PROPULSION | `maos-propulsion-redundancy-battery` §3. **Open item:** SAFETY (AER-62 §5) flags this duration/power basis for re-examination — it was sized in a 2G context where generator loss is a double-fault; under 1G it's single-string. Not resolved here; tracked to the weekly-cadence follow-on (AER-59). |
| 12 | Standing architecture | 1G + 1B + 2M | Board decision (Bill) | `maos-1g1b2m-architecture-decision` — not reopened by this study |
| 13 | Battery chemistry | **LiFePO₄ (LFP) — SAFETY-ruled baseline for every combo** | SAFETY (AER-62 §3), resolving the tension below | LFP is simultaneously cheaper (§4) and safer (thermal-runaway resistance on the aircraft's sole emergency reserve) than NMC 811. NMC 811 is not a scorecard default — it requires an explicit, named risk acceptance from Bill (see §4). |
| 14 | ICE interim continuous-duty derate (zero-sustained-duty-data engines) | 50% of documented steady-state output, defaulting to 50% of stock rated crank output where none exists | SAFETY (AER-62 §1) | Applies to every Hayabusa/H2 candidate in §2 — see new §1.3. Caps their credited continuous power **below** the 96 kW floor on paper today. |
| 15 | HV bus voltage | Open gate — DG-004, 400V vs 800V | Systems/Propulsion joint, unresolved | `maos-generator-selection` — reopened pending Evolito/H3X voltage confirmation |
| 16 | ICE-SYS-001 (formal requirement) | "ICE subsystem shall support continuous generator-duty operation in the **100–230 kW target class**" | MAOS-ICE (already in `REQUIREMENTS_INDEX_V0.md`) | Independently corroborates line 7 — see §1.2 |
| 17 | ~~"75 kW continuous, generator-head minimum"~~ | **STALE — superseded, do not size to it** | Flagged by this study | See §1.2 |

### 1.1 Sanity check on line 5 (first-principles close)

Aero power required in level cruise: `P = D·V = (W/(L/D))·V`.
W = 2,600 lb = 11,565 N. L/D = 14 → D = 826 N. V = 155 KTAS = 79.7 m/s.
`P = 826 × 79.7 ≈ 65.8 kW` — this is **thrust power**, not shaft power at the prop.

The published table states 80 kW shaft power at the prop for the same condition. Dividing: 65.8 / 80 = 0.82. That implies a propeller efficiency of ≈82% was used (a normal, defensible cruise-prop figure) to go from thrust power to shaft power, but it is not stated as an owned assumption anywhere in the source article. **Action for AERO:** confirm the propeller efficiency figure used in the 80 kW shaft-power line, or correct it if a different value applies. This does not change the ICE requirement conclusion below — it closes the energy balance so the 96 kW figure can be trusted rather than merely repeated.

### 1.2 The reconciliation: which number is real

Two incompatible ICE power figures exist in the corpus:

- `maos-engine-comparison-matrix` (2026-04-05): **"75 kW (100 hp) minimum for generator head drive,"** framed as a **SINGLE variant (1× engine, 75 kW generator)** vs. **TWIN variant (2× engines, 150 kW total)**.
- `maos-1g1b2m-architecture-decision` (2026-04-05, same day): power budget requires **96 kW ICE at cruise**, up to **155 kW at max climb**.

**Finding: the 75 kW figure is stale and traces to a superseded redundancy philosophy, not to the mission.**

The 75 kW number's origin is visible in `maos-generator-selection`: *"Continuous power per unit: 65–80 kW... Basis: Single generator failure must sustain flight."* That is an **N+1 twin-generator redundancy sizing rule** — split ~150 kW of total requirement across two generator units so that *either one alone* could sustain the aircraft if its twin fails. It is a sound rule **for a 2G architecture**. It is meaningless for the architecture MAOS actually adopted.

`maos-1g1b2m-architecture-decision` explicitly rejected 2G on cost (two Rotax 915 iS ≈ $90k before electronics) and selected **1G** — one generator, no generator-redundancy peer to size against. In 1G, the single ICE-generator set has no twin to share load with; it must cover the full mission power itself, with the **battery**, not a second generator, providing the failure reserve. The 75 kW "either-unit-alone" sizing logic doesn't apply to a fleet of one.

The number that actually traces to the mission is **96 kW continuous at cruise**, rising to **155 kW bus demand at max climb** (ICE plus battery contribution above the ~118–120 kW Rotax-916-class baseline). This is confirmed independently: **MAOS-ICE's own formal requirement, ICE-SYS-001, already states "100–230 kW target class"** — meaning the in-repo requirements were already corrected past the stale article figure, just not reconciled back to the article itself.

**Consequence for the existing engine matrix — say so plainly:** every "✅ Viable" call in `maos-engine-comparison-matrix` and `ENGINE_SELECTION_DOWNSELECT_V1.md` was made against the 75 kW bar. Re-run against the real 96 kW floor:

| Engine | Cont. power | vs. 75 kW (old bar) | vs. 96 kW (real floor) |
|---|---:|---|---|
| Rotax 912 iS | 73.5 kW | "Viable, low margin" | **Fails** — below the real floor |
| Aeromomentum AM13 | 73.5 kW | "Viable, marginal" | **Fails** |
| Viking 130 | 97 kW | Comfortably viable | **Passes, ~1 kW margin — effectively zero recharge headroom** |
| Rotax 915 iS | 103.5 kW | Comfortably viable | Passes, ~7.5 kW (7%) margin — tight |
| Rotax 916 iS | 118 kW | Comfortably viable | Passes, ~22 kW (23%) margin — this is why it was picked as the architecture's baseline |
| Hirth F-30, Hirth F-23, Honda CB500/CB650 | ≤62 kW | Already marginal/disqualified | Still disqualified, worse |

**Two previously-"viable" engines (Rotax 912 iS, Aeromomentum AM13) flip to fails.** This does not change the shortlist leaders (Rotax 915/916 iS were already the top picks), but it does mean the matrix's "conservative fallback" and "budget-conscious" rows are no longer defensible and should be struck in a follow-on erratum to `ENGINE_SELECTION_DOWNSELECT_V1.md`.

**Recommendation:** treat 96 kW continuous as the ICE electrical-output floor for any single-engine candidate in this study, and treat ~118–120 kW as the *preferred* target (the level at which 700 fpm climb needs no battery assist, matching the accepted architecture baseline). Do not size to 75 kW. This does not bounce to Elon — it traces cleanly to AERO's mission inputs plus the board's own 1G architecture decision; it just was never reconciled against the older article.

### 1.3 SAFETY ruling: interim continuous-duty derate for zero-sustained-duty-data engines

Per the SAFETY consult ([AER-62](/AER/issues/AER-62) §1, closed 2026-08-09): neither the Hayabusa nor the Kawasaki H2 has a manufacturer continuous rating — motorcycles aren't rated that way — and neither has any fixed-RPM/fixed-load endurance data at the planned generator-duty point. SAFETY's interim rule, in force until the 500+ hr bench program (§7) supersedes it: credit no more than 50% of the highest documented *steady-state* output for the planned tune, defaulting to 50% of stock rated crank output where no steady-state figure exists.

Applied to this catalog's own sourced numbers (`PROPULSION_CANDIDATE_MATRIX_V1.md` §1):

| Engine (combos) | Stock rated crank output (source) | Interim credited continuous (50%) | vs. 96 kW floor |
|---|---:|---:|---|
| Hayabusa Gen3 (Combos 3, 4, 5) | 140 kW / 190 hp | **~70 kW** | **Below floor by ~26 kW (27%)** |
| Kawasaki H2 (Combo 6) | 147–158 kW (factory supercharged, no lower-boost catalog variant) | **~74–79 kW** | **Below floor by ~17–22 kW** |

**This is a harder finding than this document's original provisional Performance scores implied.** As documented today — before the bench program runs — no Hayabusa- or H2-based combo has a credible basis for claiming it clears the reconciled 96 kW continuous floor. §3.2 rescores Performance for Combos 3, 4, 5, and 6 accordingly. The bench endurance test named in §7 is therefore not a confidence-building formality on top of an already-adequate design — it is the test that determines whether the lead combo clears the mission floor at all.

This also retracts a claim used earlier in this document's first draft: "drag-race heritage shows 200+ kW is achievable" is peak, transient, road-airflow-cooled output, and SAFETY is explicit that it is **not valid continuous-duty margin evidence** (AER-62 §1). The Rotax-class engines (Combos 1, 2) are unaffected — Rotax publishes genuine manufacturer continuous ratings for an aviation-type engine, not peak/dyno figures, so the interim derate does not apply to them.

---

## 2. Powertrain Combo Catalog

Every combo is priced as an integrated system: ICE + generator + generator controller + battery/BMS + 2× propulsion motor + motor controllers + reduction/coupling + prop + HV wiring/switchgear/fusing + 10% contingency. Source citations are per line item; where a figure is a range, the midpoint is used and the range is shown.

**Balance-of-system (BOS) items common to every combo**, priced from `maos-1g1b2m-architecture-decision` and `maos-drivetrain-economics` cost tables:

| Item | Cost | Source |
|---|---:|---|
| HV wiring, switchgear, fusing, contactors | $7,000 | Midpoint of $6,000–$8,000 across both cost-summary tables |
| Contra-rotating prop assembly (2M coaxial) | $8,000 | Consistent across both `maos-1g1b2m-architecture-decision` cost tables |
| Battery pack + BMS, 40 kWh, **DIY LFP** — SAFETY-ruled baseline (§1 line 13, §4) | $10,000 | `maos-drivetrain-economics` Scenario C (CATL 280Ah prismatic + BMS + case) |
| Battery pack + BMS, 40 kWh, **NMC 811** (shown for reference only — requires Bill's named risk acceptance to use, §4) | $20,000 | `maos-1g1b2m-architecture-decision` cost table |

### Combo 1 — Premium Anchor: Rotax 916 iS + Emrax 268 (gen) + 2× Emrax 228 (motors)

Reference point, not a budget candidate. Full BOM from `maos-1g1b2m-architecture-decision` "Cost Summary (Rotax Path)."

| Item | Cost |
|---|---:|
| Rotax 916 iS | $50,000 |
| Generator (Emrax 268, AFPM) | $12,000 |
| Generator controller | $4,000 |
| Propulsion motors (2× Emrax 228) | $16,000 |
| Motor controllers (2×) | $8,000 |
| Battery (40 kWh **LFP**, per SAFETY chemistry ruling §1 line 13) | $10,000 |
| BMS, wiring, switchgear | $8,000 |
| Contra-rotating prop | $8,000 |
| Reduction drive/coupling | $3,000 |
| Contingency (10%) | $11,900 |
| **Total** | **~$130,900** |
| Electric-hardware-only subtotal (gen + 2 motors + controllers) | **$40,000** |

**162% over the $50k line** (originally 284% with the as-published NMC 811 pack; re-priced to LFP per the SAFETY chemistry ruling — §1 line 13, §4). Chemistry change doesn't move the cost-score bucket (still deep in ">60% over"). Best-documented components, highest confidence, worst economics.

### Combo 2 — Certified-Turbo Budget: Rotax 915 iS + Hyper9 HV AC-X144 (gen) + 2× Hyper9 AC-X1 (motors)

Directly answers Bill's Q(a) with the mass-produced, **factory-turbocharged**, certified-basis engine at the cheapest electric side available.

| Item | Cost | Source |
|---|---:|---|
| Rotax 915 iS | $31,500 | Midpoint $28k–$35k, `PROPULSION_CANDIDATE_MATRIX_V1.md` §2B (newer figure; supersedes the $42–48k quote in `maos-engine-comparison-matrix` — flagging the discrepancy, not resolving it without a fresh vendor quote) |
| Generator (Hyper9 HV AC-X144) | $5,600 | `MOTOR_CONTROLLER_TRADE_MATRIX.md` source anchors |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | Same, ×2 for 2M (source matrix prices 1× only) |
| Reduction/coupling (placeholder — Hyper9 max RPM unconfirmed) | $1,500 | Conservative placeholder; **flag: Hyper9 AC-X144 RPM ceiling not in any sourced datasheet — direct-drive-vs-reduction question is open, unlike the Rotax↔Emrax pairing which the generator-selection article did work through** |
| Battery + BMS (40 kWh **LFP**, per SAFETY chemistry ruling §1 line 13) | $10,000 | BOS table |
| HV wiring/switchgear/fusing | $7,000 | BOS table |
| Contra-rotating prop | $8,000 | BOS table |
| Subtotal | $74,400 | |
| Contingency (10%) | $7,440 | |
| **Total** | **~$81,840** | |
| Electric-hardware-only subtotal | **$16,400** | |

**64% over the $50k line** (originally 86% over with the as-published NMC 811 pack; re-priced to LFP per the SAFETY chemistry ruling). Still >60% over — chemistry doesn't move the cost-score bucket. The ICE alone ($31,500) plus battery ($10,000) still exceeds the entire budget before any electric hardware is added. **This remains the clearest evidence for Q(a): the certified, factory-turbocharged, mass-produced option (Rotax) cannot reach $50k total, no matter how cheap the electric side gets.**

### Combo 3 — H-Budget-Solo: Turbo Hayabusa + Hyper9 HV AC-X144 (gen) + 2× Hyper9 AC-X1 (motors) + LFP battery

| Item | Cost | Source |
|---|---:|---|
| Hayabusa 1340cc (used) + turbo kit + conversion (cooling reroute, mounts, ECU) | $8,000 | `maos-drivetrain-economics` Scenario C; consistent with `maos-1g1b2m-architecture-decision` motorcycle-path cost table ($4,500 engine + $4,000 conversion ≈ $8,500) |
| Generator (Hyper9 HV AC-X144) | $5,600 | `MOTOR_CONTROLLER_TRADE_MATRIX.md` |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | Same, ×2 |
| Reduction/coupling (belt, ~2:1–2.3:1, Hayabusa→generator input) | $1,500 | See §5.2 — mechanically well-precedented |
| Battery + BMS (40 kWh **LFP**) | $10,000 | BOS table — LFP chemistry, see §4 |
| HV wiring/switchgear/fusing | $7,000 | BOS table |
| Contra-rotating prop | $8,000 | BOS table |
| Subtotal | $50,900 | |
| Contingency (10%) | $5,090 | |
| **Total** | **~$55,990** | |
| Electric-hardware-only subtotal | **$16,400** | |

**12% over the $50k line — closest of any combo evaluated.** With NMC 811 instead of LFP, this combo is $65,990 (32% over); swapping to LFP alone closes ~$10k of the gap. See §4 for the chemistry trade this creates.

### Combo 4 — H-Budget-Robust: Turbo Hayabusa + Tesla Model 3 rear DU + T-2C (gen) + 2× Hyper9 AC-X1 (motors) + LFP battery

Same ICE and propulsion side as Combo 3; swaps the generator for one with much larger continuous-power headroom over the 96 kW floor, at higher cost.

| Item | Cost | Source |
|---|---:|---|
| Hayabusa 1340cc + turbo + conversion | $8,000 | Same as Combo 3 |
| Generator (Tesla M3 rear DU + T-2C VCU) | $12,599 | `MOTOR_CONTROLLER_TRADE_MATRIX.md` ($9,900 + $2,699); generator-mode noted as "capable in principle," not bench-validated |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | Same as Combo 3 |
| Reduction/coupling | $1,500 | Same basis as Combo 3 |
| Battery + BMS (40 kWh LFP) | $10,000 | BOS table |
| HV wiring/switchgear/fusing | $7,000 | BOS table |
| Contra-rotating prop | $8,000 | BOS table |
| Subtotal | $57,899 | |
| Contingency (10%) | $5,790 | |
| **Total** | **~$63,689** | |
| Electric-hardware-only subtotal | **$23,399** | |

**27% over the $50k line.** The premium over Combo 3 buys generator headroom (Tesla DU peaks at 220 kW vs. our 96 kW requirement — comfortable margin) at the cost of an unvalidated automotive VCU generator-mode claim.

### Combo 5 — H-Premium-Technical: Turbo Hayabusa + H3X HPDM-180R (gen) + 2× HPDM-180R (motors)

Reference/benchmark only — not detailed BOM'd here since it is already well-covered in `PROPULSION_CANDIDATE_MATRIX_V1.md` (Path H4) and `MOTOR_CONTROLLER_TRADE_MATRIX.md` (B6). Electric-hardware-only subtotal: **$60k–$120k** for 3 units (1 gen + 2 motors) at $20k–$40k/unit. Adding ICE + battery + BOS pushes total well past $150k. **≥200% over the $50k line.**

### Combo 6 — Kawasaki H2 (factory-supercharged) + Hyper9 HV (gen) + 2× Hyper9 AC-X1 (motors) + LFP battery

Answers Bill's Q(a) from a second angle: a mass-produced motorcycle engine that is **factory forced-induction** (supercharged, not aftermarket-turboed like the Hayabusa path).

| Item | Cost | Source |
|---|---:|---|
| Kawasaki H2/H2R (used) + conversion | $17,000 | Midpoint $8k–$18k engine (`PROPULSION_CANDIDATE_MATRIX_V1.md` §2A) + $4,000 conversion (same class of work as Hayabusa) |
| Generator (Hyper9 HV AC-X144) | $5,600 | Same as Combo 3 |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | Same as Combo 3 |
| Reduction/coupling | $1,500 | Same basis |
| Battery + BMS (40 kWh LFP) | $10,000 | BOS table |
| HV wiring/switchgear/fusing | $7,000 | BOS table |
| Contra-rotating prop | $8,000 | BOS table |
| Subtotal | $59,900 | |
| Contingency (10%) | $5,990 | |
| **Total** | **~$65,890** | |
| Electric-hardware-only subtotal | **$16,400** | |

**32% over the $50k line.** More expensive than the Hayabusa path for no clear performance edge (similar power class, same unvalidated-TBO risk, *less* community tuning depth — the Hayabusa/MegaSquirt-Speeduino ecosystem documented in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` has no H2 equivalent). Kept on the catalog because Bill asked specifically about factory forced-induction, but it does not beat the Hayabusa combos on any axis.

### Combo 7 — DeltaHawk DHK235A4 + generator + 2× motors — **UNPRICED, not rankable**

DHK235A4: 175 kW continuous, FAA type-certificated (first clean-sheet certified piston in ~50 years), best SFC of any candidate (~221–227 g/kWh vs. Rotax's ~280 g/kWh), Jet-A/JP-8/SAF/diesel fuel flexibility, and — notably for the RPM-matching question — a **2,600 RPM max output** that pairs almost directly with the H3X HPDM-180R's ~3,000 RPM generator input (≈1.15:1 step-up, vs. Hayabusa's ~2:1–2.3:1 reduction). Mechanically, this is the *easiest* coupling problem of any candidate in this study.

**No public price exists.** `PROPULSION_CANDIDATE_MATRIX_V1.md` lists "contact mfr" for every DHK variant. FAA-TC'd piston engines of this class have historically priced well into six figures once support/warranty terms are included, which would disqualify it on cost alone — but that is an inference, not a quote. **This combo cannot be scored against the $50k line without a DeltaHawk vendor quote.** Retained on the catalog as a documented, evidence-gated option, not scored in §3.

### Combo 8 — 3× AantFarm TA65-1 turboalternator — reference, already disqualified/watchlist

Already fully evaluated in `TURBOALTERNATOR_TA65_EVALUATION_V0.md`. A single unit fails the requirement outright (60 kW SL / ~37 kW at FL180, vs. a ~90 kW electric-bus cruise need — a 2.4× shortfall at altitude). A 3× installation closes the envelope with margin and adds genuine generation redundancy the 1G architecture otherwise lacks, at +38% fuel burn vs. the Rotax path and **unknown, "likely prohibitive"** cost for three in-development turboalternators plus rectifiers. Not rankable against $50k for the same reason as Combo 7 — no price exists. Disposition unchanged from the existing evaluation: **watchlist, evidence gates before any funded work** (see that document §6).

---

## 3. Scoring

### 3.1 Weights (stated, traceable)

| Dimension | Weight | Rationale |
|---|---:|---|
| Cost | 40% | AER-57's central ask is a cost-vs-performance-vs-safety *breakthrough* toward a named $50k target; cost is the binding constraint this study exists to resolve |
| Performance | 35% | Meeting the reconciled 96–155 kW envelope (§1) with real margin, not the stale 75 kW bar |
| Safety | 25% | Scored per SAFETY's ruling ([AER-62](/AER/issues/AER-62), closed 2026-08-09) — derate criteria, failure-mode severity classification, and chemistry ruling. No longer provisional. See §6 for the ruling and §3.2 for the applied rubric. |

Scoring scale, 1–5, applied per dimension:

**Cost** (against the $50k installed-hardware line): 5 = at/under $50k · 4 = 1–15% over · 3 = 16–30% over · 2 = 31–60% over · 1 = >60% over or unpriceable.

**Performance** (against §1's reconciled envelope, using **credited** continuous power — SAFETY's interim derate per §1.3 applies where an ICE has zero sustained-duty evidence): 5 = clears 118–120 kW no-battery-climb target with real margin, full envelope closed cleanly · 4 = clears 96 kW cruise floor with ≥10% margin, climb needs the architecturally-accepted battery assist · 3 = clears 96 kW with <10% margin or carries an unconfirmed vendor-data risk on a critical component · 2 = does not clear the 96 kW floor on credited numbers, or multiple critical unknowns · 1 = fails the mission envelope outright.

**Safety** (per SAFETY's rubric, §6): ceiling of 3 until the ICE-FLT/ICE-SYS fault-detection chain is bench-verified and a phase/altitude floor is set (neither closed for any combo today); within that ceiling, scored on zero-sustained-duty-data flags and chemistry per the worked pass in §3.2.

### 3.2 Scored combos

**Revised per SAFETY's ruling (AER-62, closed 2026-08-09).** Safety scores below apply SAFETY's rubric directly (§6). Performance scores are re-derived by PROPULSION using SAFETY's interim continuous-duty derate (§1.3) — this moves several combos, not just the safety column. Cost scores are unchanged by the ruling except where the LFP chemistry swap (§1 line 13, §4) shifted a total; neither shift changed a cost-score bucket.

| Rank | Combo | Total installed cost | Electric-hardware-only | Cost (40%) | Performance (35%) | Safety (25%) | Weighted score |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | **Combo 3 — H-Budget-Solo** (turbo Hayabusa + Hyper9 HV gen + 2× Hyper9 AC-X1 + LFP) | $55,990 (+12%) | $16,400 | 4 | 2 | 2 | **2.80** |
| 2 | Combo 1 — Premium Anchor (Rotax 916 + Emrax, LFP-adjusted) | ~$130,900 (+162%) | $40,000 | 1 | 5 | 2 | **2.65** |
| 3 | Combo 8 — 3× AantFarm (reference, not re-derived — see note) | Unknown, "likely prohibitive" | n/a | 1 | 4 | 3 | **2.55** |
| 4 | Combo 4 — H-Budget-Robust (turbo Hayabusa + Tesla M3 DU gen + 2× Hyper9 AC-X1 + LFP) | $63,689 (+27%) | $23,399 | 3 | 2 | 2 | **2.40** |
| 5 | Combo 6 — Kawasaki H2 budget | $65,890 (+32%) | $16,400 | 2 | 2 | 2 | **2.00** |
| 6 | Combo 2 — Rotax 915 budget (LFP-adjusted) | ~$81,840 (+64%) | $16,400 | 1 | 3 | 2 | **1.95** |
| 7 | Combo 5 — H-Premium-Technical (Hayabusa + 3× HPDM-180R) | ~$150k+ (+200%+) | $60k–$120k | 1 | 2 | 1 | **1.35** |
| — | Combo 7 — DeltaHawk | Unpriced | Unpriced | — | — | — | **Not scored — blocked on vendor quote** |

The ranking reorders (Combo 1 moves from a 3-way tie into outright 2nd; Combo 5 drops from tied-1st to last of the scored combos) but **the lead does not change** — Combo 3's cost advantage is large enough to absorb the Performance and Safety corrections. What does change materially: the lead combo no longer reads as "performing well, safety unproven." It reads as "cheapest path, currently short of the mission floor on paper, safety-capped pending the same evidence." See §7.

**Performance notes behind the scores (revised per §1.3):**
- Combo 3 (score 2, down from 3): under SAFETY's interim derate, credited Hayabusa continuous output (~70 kW) sits **below** the 96 kW floor. The "drag-race heritage" margin claim is retracted (§1.3) — not valid continuous-duty evidence. Separately, the Hyper9 HV AC-X144's *continuous* rating is still not clearly published (peak 88 kW oddly listed lower than the "rated 120 hp/89.5 kW" figure — likely a transcription issue, needs a fresh datasheet pull, §8).
- Combo 4 (score 2, down from 4): same Hayabusa ICE as Combo 3 — the Tesla DU generator's large headroom (220 kW peak) doesn't help; the ICE, not the generator, is the bottleneck under the interim derate.
- Combo 5 (score 2, down from 5): same Hayabusa ICE as Combos 3/4. The original score of 5 credited H3X's aviation-grade generator/motor maturity as if it also resolved the ICE-side risk — it doesn't, by the same logic SAFETY applied to correct this combo's safety score below.
- Combo 6 (score 2, down from 3): Kawasaki H2's factory-supercharged rating (147–158 kW) is a peak dyno figure, not a continuous one; under the same interim derate its credited continuous (~74–79 kW) also sits below the 96 kW floor.
- Combo 1 (score 5, unchanged): Rotax 916 iS publishes a genuine manufacturer continuous rating for an aviation-type engine, not a peak/dyno figure — clears the floor with real margin; the interim derate doesn't apply.
- Combo 2 (score 3, unchanged): Rotax 915 iS's published continuous rating (103.5 kW) clears 96 kW with a <10% margin; no derate needed.
- Combo 8 (score 4, unchanged): turboalternator, not a reciprocating ICE — SAFETY's interim derate rule targets zero-sustained-duty-data piston engines specifically and doesn't apply to this technology.

**Safety notes (per SAFETY's worked pass, AER-62 §4):**
- Combo 1 (2, down from 4): mature components don't offset a chemistry choice against the sole emergency reserve — scored against the as-published NMC 811 basis this combo carried until this revision (§2 now shows the LFP-adjusted BOM).
- Combo 2 (2, down from 3): same chemistry correction as Combo 1.
- Combo 3 (2, down from 3): zero-sustained-duty-data flag alone caps it at 2 even with LFP chemistry credited; turbo-continuous-duty risk is tracked as its own FMEA line (§1.3), not folded numerically into this score.
- Combo 4 (2, down from 3): same ICE risk as Combo 3.
- Combo 5 (1, down from 4) — **the largest correction**: the original score credited H3X's generator/motor maturity for a risk that sits entirely on the engine side. Same Hayabusa zero-data flag as Combo 3/4, plus chemistry isn't specified in this catalog and defaults to the NMC 811 planning basis per the architecture-decision article — a second flag.
- Combo 6 (2, unchanged): zero-sustained-duty-data flag, offset by clear LFP chemistry.
- Combo 8 (3, not re-derived): SAFETY flagged this as a special case — three independent turboalternator units is a genuine generation-redundancy improvement the 1G-specific rubric doesn't model, offset by zero production/endurance data on an in-development product. Carried at the prior score pending a dedicated follow-up with SAFETY, not forced through the formula above.

**Blanket ceiling (applies to every row):** per SAFETY's rubric, no combo in this catalog exceeds **Safety = 3** until (a) the ICE-FLT/ICE-SYS fault-detection and derate/shutdown state machine is bench-verified end to end for the specific ECU/engine pairing, and (b) a minimum altitude/phase floor for the Hazardous-not-Catastrophic failure credit (§6) is set as a formal requirement. Neither gate is closed today for any combo.

---

## 4. Battery Chemistry — Resolved by SAFETY Ruling (AER-62)

PROPULSION's own operating brief leaned toward a LiFePO₄-class pack for thermal-runaway resistance and cycle life. The published `maos-propulsion-redundancy-battery` analysis leaned toward NMC 811 as the "practical near-term" planning baseline specifically because LFP is *heavier* — 706 lbs for 40 kWh vs. NMC 811's 441 lbs, a 265 lb penalty most of the weight budget cannot absorb on top of everything else competing for the 1,200 lb useful-load target.

This trade study's own cost finding cuts the other way from how that tension was framed: swapping a combo's battery from NMC 811 to LFP is simultaneously **cheaper** ($10,000 vs. $20,000 at 40 kWh) and **safer** (thermal-runaway resistance) — for Combo 3 specifically, it's the single change that gets the leading combo from 32% over the $50k line to 12% over.

**SAFETY's ruling (AER-62 §3): LFP is the safety-ruled baseline chemistry for every combo in this catalog, not only the cost-motivated lead one.** This pack is not a convenience battery — in the 1G architecture it is the **sole** emergency reserve standing between an ICE/generator failure and total propulsion loss, with no peer battery to fall back on. NMC 811 is specifically the highest-nickel, least thermally stable mainstream NMC formulation — the property that trades against thermal stability is exactly the one it was selected for (energy density). Putting that chemistry next to the aircraft's only emergency reserve is compounding risk in the wrong place. §2's BOM tables for Combos 1 and 2 (previously priced with NMC 811) are updated above to the LFP baseline; neither combo's cost-score bucket changes as a result — both remain far over budget regardless of chemistry.

**The weight gap should close via the power/duration lever, not the chemistry lever.** `maos-propulsion-redundancy-battery` §5 Lever 1 already names it: reducing the emergency-power assumption from 60 kW (full IFR approach capability) to 40 kW (powered descent) cuts the reserve to ~26 kWh, which brings LFP's weight down to roughly parity with today's 60 kW/NMC-811 baseline (~459 lb vs. 441 lb). That is a mission-requirements question — what "get the plane on the ground" actually needs — and routes to AERO/Elon/Bill (tracked as an open item, §1 line 11), not to a chemistry substitution that trades away thermal-runaway margin on the emergency system itself.

**If the board wants NMC 811 anyway for weight reasons after that lever is examined, that is a named risk acceptance for Bill, not a scorecard default.** This document does not assume it.

**Independent of chemistry:** SAFETY also flags that the battery bay must be physically/thermally zoned away from HV bus wiring, contactors, and motor-controller electronics — a pack co-located with those items in a shared bay is a common-cause hazard that could take out the emergency reserve and the power-delivery hardware simultaneously. This is a Structures/Systems requirements-list item, not scored here.

---

## 5. Bill's Two Specific Asks

### 5.1 Is there a lightweight, mass-produced, turbocharged ICE that wins as the generator prime mover?

**Yes and no, depending on what "turbocharged" is allowed to mean — and the distinction matters for the answer.**

- **Factory-turbocharged, mass-produced, aviation-certified basis (Rotax 915/916 iS):** real, proven, best documented — and **cannot reach $50k total** (Combo 2: $92,840, 86% over). The ICE alone ($28k–$35k) plus the battery ($20k) exceeds the entire budget before a single dollar of electric hardware is spent. This does not win.
- **Mass-produced base engine, turbocharged as a proven aftermarket modification (Hayabusa + turbo kit):** the Hayabusa itself is genuinely mass-produced (Suzuki, decades of production, deep used-market supply at $3k–$8k). Turbocharging it is not a factory option but is a **well-proven aftermarket path** — drag-racing heritage puts reliable *transient* street-boost output at 300+ hp, meaning the engine can run well below its boost ceiling in this application. **This is boost-ceiling headroom, not continuous-duty margin evidence** — per SAFETY's ruling (§1.3), it says nothing about credited *continuous* generator-duty output, which is capped well below this figure until the bench program runs. This is what "turbo Hayabusa" means throughout this catalog, and it is the cost leader (Combo 3, 12% over $50k) — but see §1.3/§7 for what that leadership currently rests on.
- **Factory-supercharged, mass-produced (Kawasaki H2):** a genuine factory-forced-induction alternative, evaluated as Combo 6. It costs more than the Hayabusa path for no offsetting performance or safety advantage and loses on community/tuning maturity. Does not win.

**Net answer:** the mass-produced engine that "wins" is the Hayabusa, but only once turbocharging is understood as a proven aftermarket modification rather than a factory feature. The factory-turbo/certified answer (Rotax) is real but too expensive to hit the target on its own — its cost, not its technical merit, disqualifies it here.

### 5.2 The Hayabusa RPM-to-generator matching problem

**Quantified mismatch:** the Hayabusa's efficient constant-speed generator-duty operating point sits in the 5,000–7,000 RPM band (below its 10,000+ RPM peak-power redline, which generator duty never needs to approach). Every generator candidate evaluated needs a *lower* input speed:

| Generator | Max/rated input RPM | Reduction needed from a ~6,500 RPM Hayabusa operating point |
|---|---:|---|
| H3X HPDM-180R | ~3,000 RPM (at its integral 6.7:1-geared interface) | ~2.2:1 |
| Emrax 268 | 5,000 RPM | ~1.3:1 |
| Hyper9 HV AC-X144 | **Unconfirmed — no datasheet RPM figure in any source reviewed** | Unknown — flagged evidence gap |
| Tesla M3 rear DU (via T-2C) | Not applicable as a direct-coupled generator input in the sourced data | N/A — T-2C generator-mode question is separate from RPM coupling |

**Does it close?** Mechanically, yes. A single-stage belt or chain reduction in the 1.5:1–3.5:1 range is explicitly documented as "well-documented in motorsport applications" (`maos-drivetrain-economics`, `PROPULSION_CANDIDATE_MATRIX_V1.md` §2A) and is priced into every Hayabusa combo above at $1,500. Toothed belt is preferred for low noise/maintenance. **Direct drive is not an option for any Hayabusa-generator pairing evaluated here** — even the lowest-RPM-ceiling generator (Emrax 268 at 5,000 RPM) still sits below a sensible Hayabusa cruise RPM, unlike the Rotax↔Emrax pairing where direct drive was judged feasible.

**What does not close — the real evidence gate:** every MAOS-ICE document that has touched this path flags the same single risk, independently, repeatedly: **there is no sustained-duty endurance data for a motorcycle engine at fixed-RPM, fixed-load generator duty.** `PROPULSION_CANDIDATE_MATRIX_V1.md` calls it "the critical gate for Configs B and C." `ENGINE_SELECTION_DOWNSELECT_V1.md` lists it as a minimum-evidence item. `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md`'s Phase 1 recommendation (Speeduino on a bench rig) exists specifically to start generating this data. This study does not resolve that gap — it confirms it is still the load-bearing unknown for the leading combo.

**Thermal at steady generator load:** the physics argument for why this should be *easier*, not harder, than automotive/motorcycle duty is sound and already documented (`maos-drivetrain-economics`: constant RPM, constant throttle, constant mixture for hours is "closer to an industrial genset application" than variable-demand riding, and industrial gensets routinely run automotive-derived engines at high duty cycles for this reason). Sound reasoning is not the same as bench evidence. **This is the evidence gate named in §7.**

**A cooling-system flag from SAFETY (AER-62 §1), distinct from the power-derate question:** industrial genset conversions are validated with cooling systems *sized for continuous 100% heat rejection*. A motorcycle radiator is sized for a road vehicle's variable duty and ram-air/road-speed-driven airflow — which won't match this airframe's actual installed cooling airflow at altitude either. An engine run at a conservative RPM/load derate can still wear out early if the cooling system was never re-sized for sustained full-load heat rejection at the installed condition. This is a PROPULSION/Systems thermal-design item and should be named instrumentation in the bench program (oil temp, head/CHT-equivalent temp, coolant temp trends over the full 500-hour run, not just at hour 1) — added to §7's evidence-gate scope.

**Turbocharging gets its own derate flag, tracked separately (SAFETY, AER-62 §1):** continuous boost for hours is a different stress regime than transient drag-strip boost — turbo bearing life, wastegate control stability, and intercooler thermal saturation are validated (informally, by the aftermarket community) against seconds of boost, not sustained duty. This is a distinct FMEA line item per combo, not a modifier folded into the ICE continuous-power derate in §1.3.

---

## 6. SAFETY Consult — Closed (AER-62)

Per AER-57 item 5, PROPULSION did not self-certify the safety score. [AER-62](/AER/issues/AER-62) was opened to SAFETY and closed 2026-08-09. Full ruling: [SAFETY Consult Response](/AER/issues/AER-62#document-safety-consult-response). Three headline rulings, folded into §1.3, §3.2, and §4 above:

1. **Continuous-duty derate:** interim cap of 50% of documented steady-state output (defaulting to 50% of stock rated crank output where none exists) for any ICE with zero fixed-RPM/fixed-load endurance data — today, every Hayabusa/H2 combo. See §1.3.
2. **ECU failure-mode severity:** the graceful-degradation argument in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §1 is directionally sound but was built on a stale, misattributed battery-buffer figure (8–12 min/15–25 kWh — traced to a takeoff-boost figure in its own source document, not the ICE-failure buffer, and superseded by the standing 40 kWh/30-min figure) and contradicts `maos-1g1b2m-architecture-decision`'s own "declare emergency" classification of the same event. SAFETY's ruling: classify ICE/generator loss as **Hazardous** (not "not an emergency"), conditional on verified fault detection and an altitude/phase floor — neither of which exists yet. A non-graceful/uncommanded ECU failure mode, or a loss below that floor, stays **Catastrophic**. `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §1 has been corrected to match (erratum, §8).
3. **Chemistry:** LFP is the safety-ruled baseline for every combo (§4), not just the cost-motivated lead one.

**Two items SAFETY named for other owners, not resolved by this document:**
- **Owner: AERO/PROPULSION jointly.** A minimum altitude/phase floor above which the 30-minute reserve credit is assumed usable. Until set, departure/initial-climb-phase ICE loss should be treated as Catastrophic by default, not Hazardous.
- **Owner: PROPULSION.** Confirm ICE-FLT-001's fault-detection set actually covers turbocharged-engine-specific fault modes (overboost, detonation, boost-control runaway) for the Hayabusa/H2 combos — today it lists only the generic overtemp/overspeed/oil-pressure/sensor-plausibility set.

Both are carried forward as open items (§8), not closed by this revision.

---

## 7. Recommendation

**(A) Downselect, conditional on a bench test the lead combo does not yet pass on paper — not "no viable answer today."**

**Lead combo: Combo 3 — H-Budget-Solo.** Turbo Hayabusa (used, ~$4k engine + ~$4k turbo/conversion) → belt-reduced (~2:1–2.3:1) to a Hyper9 HV AC-X144 generator → 400V-class bus → 2× Hyper9 AC-X1 propulsion motors → 40 kWh LFP battery/BMS → coaxial contra-rotating prop. **Current best estimate: $55,990 installed, 12% over the $50k line** — the closest of every combo evaluated, and the only one within plausible reach of the target through ordinary sourcing decisions already visible in the BOM (used-market component sourcing, contingency trim, LFP already applied).

**Read this plainly, per SAFETY's ruling (§1.3, §3.2): on the credited numbers this document can defend today, Combo 3's ICE does not clear the 96 kW continuous floor (~70 kW credited vs. 96 kW required).** This is not a "nice-to-validate" margin question anymore — it is a "does not currently meet the requirement" finding, held provisional-conservative only because no engine in this class has ever been rated for continuous duty in the first place. The recommendation below is a bet that real steady-state performance is materially better than the conservative interim number, backed by the physical reasoning in §5.2 (generator duty should be gentler than motorcycle duty) — not a claim that the requirement is already met.

**The evidence gate that would confirm or kill it:** a bench endurance test — Hayabusa at fixed generator-duty RPM and load, 500+ hours, per the Phase 1 program already scoped in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §6 (Speeduino/Teensy 4.1 instrumentation), **instrumented for sustained thermal (oil/CHT-equivalent/coolant trends over the full run, not just hour 1) per SAFETY's cooling-sizing flag (§5.2), and tracking turbo-specific continuous-boost wear as its own line item, not folded into the power number.** This single test is now the load-bearing decision, not a confidence-builder on top of one. A secondary, cheaper gate — a fresh Hyper9 HV AC-X144 datasheet pull confirming actual continuous rating and max RPM — should run in parallel; it is unpriced (a phone call/email) and resolves a real but smaller flag on the lead combo.

**DES-INT-001 compliance — second architecture kept alive, reframed.** The original draft named Combo 4 (same Hayabusa ICE, Tesla DU generator) as the second architecture. That no longer holds up: Combo 4 shares Combo 3's exact ICE-side shortfall (§1.3) — a bigger generator doesn't retire an engine-side risk. **Combo 1 — Premium Anchor (Rotax 916 iS + Emrax, LFP-adjusted, $130,900, 162% over)** is the architecturally distinct second path per DES-INT-001: it is the only combo in this catalog whose viability does **not** depend on the same unresolved bench-test evidence gap, because Rotax publishes a real continuous rating. It is not close to $50k, and isn't meant to be — it is the proof that the *mission* is achievable today, at a known, high, certain cost, if the Hayabusa bet doesn't pay off. **What would eliminate one of these two:** the bench program showing the Hayabusa genuinely cannot sustain ≥96 kW continuous at fixed-RPM generator load (thermal, detonation, or TBO failure) eliminates Combo 3 — and, by the shared-ICE finding above, Combo 4 and Combo 6 with it — leaving Combo 1 as the only standing path pending a cost-reduction lever nobody has found yet. A positive bench result (credited continuous power revised upward past 96 kW) does not eliminate Combo 1; it just makes Combo 3 the clear winner outright.

**Why not "no viable answer today," even with the derate finding:** the gap between the lead combo and the $50k target is a cost/sourcing question already answered by the BOM (12% over, closing through ordinary means). The gap between the lead combo and the *mission floor* is a separate, evidence question this document cannot close by reasoning alone — and that is exactly what a named evidence gate is for. Nothing here shows the Hayabusa *can't* do it; SAFETY's own physical-reasoning check (§5.2) is that generator duty should be gentler than the duty cycle the engine already survives on the street. The honest disposition is: a real, priced, near-budget path exists, and it is not yet proven — not "no options exist."

**Build-our-own path — not triggered, briefly scoped for the record.** Unchanged in disposition: because a ≤$50k-adjacent, evidence-gated path exists and has not been eliminated, the build-our-own decision gate is not opened by this study. If the bench test *fails*, the fallback is Combo 1 at ~2.6× budget — at that point "no viable ≤$50k answer today" becomes the live disposition, and build-our-own becomes a real question, most plausibly not a from-scratch engine but a from-scratch **generator coupling/reduction package** purpose-built for motorcycle-engine generator duty (the ICE itself and the electric machines are not the parts in question — the interface and the duty-cycle validation are). That scoping is a follow-on task, not this document's job.

**Market re-evaluation trigger (for the weekly-cadence follow-on issue, AER-59):** re-run this scorecard if (a) the bench program produces a result, positive or negative — this is now the primary near-term trigger, ahead of any market development; (b) H3X, Evolito, or a comparable aerospace-grade axial-flux vendor publishes a sub-$15k/unit price at 90kW+ continuous — this would flip Combo 5-class options into budget contention; (c) a Hyper9-class generator's confirmed continuous rating and RPM ceiling change the Performance score on Combo 3; or (d) DeltaHawk (Combo 7) or AantFarm (Combo 8) publish pricing — both are technically strong and currently unscored purely on missing price data.

---

## 8. Open Items / Next Actions

1. **SAFETY consult — closed** ([AER-62](/AER/issues/AER-62)), ruling folded into §1.3, §3.2, §4, §6.
2. **Erratum applied — `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §1** — corrected the stale battery-buffer citation (8–12 min/15–25 kWh → 40 kWh/30 min) and reclassified ICE/generator loss as Hazardous-conditional per SAFETY's ruling, replacing the "not an emergency" framing.
3. **AERO/PROPULSION joint, open** — set a minimum altitude/phase floor above which the 30-min battery reserve credit is assumed usable (SAFETY, §6). Until set, departure/initial-climb ICE loss should default to Catastrophic, not Hazardous, in any FHA.
4. **PROPULSION, open** — confirm ICE-FLT-001's fault-detection set covers turbocharged-engine-specific fault modes (overboost, detonation, boost-control runaway) for the Hayabusa/H2 combos; today it lists only the generic overtemp/overspeed/oil-pressure set (SAFETY, §6).
5. **Bench endurance program — elevated priority.** Per §7, this is no longer a risk-reduction nice-to-have; it is the test that determines whether the lead combo meets the mission floor at all. Should become a tracked child issue promptly, instrumented per §5.2/§7 (sustained thermal trends, turbo-continuous-duty wear as a separate line item).
6. **AERO confirmation** on the implied ~0.82 propeller efficiency (§1.1) — closes the traceability chain fully; does not change any conclusion here but should not stay an inferred number.
7. **Vendor datasheet pull — Hyper9 HV AC-X144** — confirm actual continuous power rating and max RPM. Now resolves both a Performance flag and part of the derate baseline on the lead combo.
8. **Vendor quotes — DeltaHawk DHK235A4, AantFarm TA65-1** — both combos are unscored purely on missing price; either could reshuffle the ranking if priced near budget-track expectations.
9. **Erratum to `ENGINE_SELECTION_DOWNSELECT_V1.md`** — strike Rotax 912 iS and Aeromomentum AM13 from the "viable" recommendation rows per §1.2; they fail the reconciled 96 kW floor.
10. **Reserve-duration adequacy re-check** — SAFETY flags (§6, AER-62 §5) that the 30-min/60kW reserve was sized in a 2G context (generator loss = double-fault); under 1G it's single-string. Not resolved here; owned by AERO/PROPULSION, tracked to the weekly-cadence follow-on (AER-59).
11. **Combo 8 (3× AantFarm) safety scoring** — SAFETY flagged this as a named exception the 1G-specific rubric doesn't model cleanly; needs a dedicated follow-up with SAFETY rather than forcing it through §3.2's formula.
12. **Cost-scope re-score** — pending Bill's answer on the AER-56 cost-boundary question; every combo's total is a re-summation away from a different boundary (§0).

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1.1 — 2026-08-09. Revises v1.0 to fold in the SAFETY consult ruling ([AER-62](/AER/issues/AER-62)): interim ICE continuous-duty derate (§1.3), revised Performance and Safety scores (§3.2), resolved battery chemistry ruling (§4), and closed consult (§6). The lead recommendation (Combo 3) is unchanged; its basis is not — see §7.*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
