# MAOS Powertrain Trade Study — Integrated Combos Toward $50k (v3)

**Status:** Analysis — Experimental Amateur-Built Category. Not a certification claim, not a hardware commitment.
**Date:** 2026-08-09 (v2 and v3 sections both added same day as v1.1)
**Owner:** PROPULSION
**Origin:** [AER-57](/AER/issues/AER-57) — "Propulsion trade study - exhaustive powertrain catalog + ranked scorecard toward $50k," child of [AER-56](/AER/issues/AER-56). **v2 origin:** [AER-65](/AER/issues/AER-65) — Bill's 2026-08-09 ruling on the four AER-56 calls (whole-powertrain scope confirmed, used/salvage sourcing permitted, bench test deferred, Donut Labs purpose separately scoped) turned his **iterate** into this pass. **v3 origin:** a same-day follow-up comment on AER-65 (R3) — Bill widens ICE sourcing to Chinese/Russian/Eastern European engines and asks for the Donut Labs ring/hub motor as a candidate row. §1–§8 below are v1.1, unchanged except where §9 explicitly revises a number. §9 is the v2 delta. **§10 is the v3 delta — read it alongside §9.6, which it tests against but does not change.**
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

---

## 9. v2 — Used/Salvage Sourcing Re-Score (AER-65)

**Trigger:** Bill's ruling on the four AER-56 calls, delivered via structured interaction and confirmed in a follow-up comment (2026-08-09): (1) the $50k target buys the **whole installed powertrain, new-parts-equivalent scope, single build** — not electric-hardware-only; (2) **used/salvage is fair** inside that number; (3) **iterate** — another engineering pass on cost, not the funded bench endurance test; (4) Donut Labs purpose is a separate prose thread, not a re-score input here. R1/R2 do not reopen the architecture (§ header) or change the cost-scope boundary from what §0 already assumed as its default — §0's boundary **was already the whole-installed-hardware scope**, so nothing in §1–§8 needs re-deriving for scope. What changes in v2 is purely a second price column: **realistic used/salvage sourcing**, priced with the same rigor and the same refusal to fabricate a number that v1 applied to new parts.

### 9.0 What "used/salvage, sourced" means here

Per Bill's R2 and Elon's "show sourced line items with price provenance, not estimates": every used/salvage figure below is tagged one of three ways —

- **SOURCED** — a specific current listing, classified ad, or in-repo cost table with a market/date anchor.
- **EXTRAPOLATED** — a discount ratio observed on a sourced comparable component, applied to a different but related part because no direct listing was found this pass. Flagged explicitly; not to be read as a quote.
- **ESTIMATE** — PROPULSION's own placeholder for integration/labor/adaptation cost with no vendor quote behind it (the same category v1 already used for things like the Hyper9-to-Hayabusa reduction drive). Flagged explicitly.

No line item is silently priced as if a salvage part were free of engineering or condition risk. §9.5 covers the one line item — the battery — where that risk is flight-critical, not just a BOM number.

### 9.1 Sourced used/salvage market data (2026-08-09 web pass)

| Component | New (v1 baseline) | Used/salvage figure | Tag | Source |
|---|---:|---:|---|---|
| Hyper9 HV AC-X144 (generator role) | $5,600 | $3,950 (midpoint of $2,500–$5,400) | SOURCED | `MOTOR_CONTROLLER_TRADE_MATRIX.md` Pairing B2, EV-West/used-market anchors dated 2026-04-16 (already in-repo; not a fresh listing) |
| Hyper9 AC-X1 (motor role, ×2) | $5,400 ea. | $3,950 ea. | EXTRAPOLATED | Same B2 range, applied to the propulsion-motor role — B2 itself only prices one used unit against one new unit; applying the same used-unit price to both roles assumes the AC-X1 and AC-X144 HV command similar used prices as the same base machine. No direct used-AC-X144-HV listing found this pass. |
| Tesla Model 3 rear drive unit, bare-pull (no kit, no T-2C) | $9,900 (EV West "starter kit" — itself a refurbished pull, not new; Tesla does not sell drive units new) | $2,000–$4,000, midpoint $3,000 | SOURCED (search-result-extracted from a 2025-dated market summary; direct page fetch returned HTTP 410, so treat as a secondary citation, not a live listing — corroborated directionally by real current bare-DU asking prices visible in Tesla-parts marketplace listings surfaced the same search) | "How Much Is a Tesla Motor in 2025?" (Recharged) via 2026-08-09 search snippet |
| EV Controls T-2C VCU (required for any Tesla DU, new or used — firmware-locked, no salvage market) | $2,699 | $2,699 (no change — sole-source new item) | SOURCED (unchanged from v1/`MOTOR_CONTROLLER_TRADE_MATRIX.md`) | EV West, 2026-04-22 |
| Rotax 915 iS | $31,500 (v1 midpoint quote) | $35,000 (156-hr low-time unit, incl. harness/ECU/hoses/intercooler) | SOURCED | rotax-owner.com classified ad, found 2026-08-09 |
| Rotax 916 iS | $50,000 | No direct listing found | EXTRAPOLATED — see finding below | — |
| Emrax 268 (generator role, Combo 1) | $12,000 | $3,780–$8,000, midpoint $5,890 | SOURCED | eBay listings, found 2026-08-09 |
| Emrax 228 (motor role ×2, Combo 1) | $8,000 ea. | $3,920 ea. (same ~49% used/new ratio as Emrax 268, applied) | EXTRAPOLATED | No direct Emrax 228 used listing found this pass |
| Suzuki Hayabusa, complete pre-built turbo engine (single opportunistic listing) | — | $2,500 | SOURCED, but see caveat | mpsracing.com garage-sale listing, found 2026-08-09; **Gen1 engine (~172 hp base), not the Gen3 (~190 hp) this study's derate table (§1.3) is keyed to** — a lower-base-rating engine credits even less continuous power under SAFETY's 50%-of-documented-steady-state rule, so this is not a drop-in substitute for the Gen3 figures used elsewhere without re-running §1.3's table. One-off listing, not a repeatable channel. Not used in the headline combo totals below — see the Combo 3 footnote. |
| Salvage Tesla Model 3 Standard-Range/RWD battery pack, 60 kWh (genuine CATL LFP prismatic cells — same chemistry SAFETY ruled as baseline in AER-62 §3, not NMC) | — (v1's new baseline is a $10,000 DIY 40 kWh LFP pack) | $3,700–$4,500, midpoint $4,100, for **60 kWh** — oversized relative to the 40 kWh requirement, at under half the DIY-new price | SOURCED | eBay OEM salvage listings, part-number class 1666968-99-C, found 2026-08-09 | **See §9.5 — this line is cost-only-sourced, not safety-creditable yet.** |

**A finding this pass surfaced that matters as much as any single price:** used/salvage sourcing is a large, real lever for **commodity automotive- and motorcycle-derived components** (Hayabusa, Hyper9, Tesla DU, Emrax, EV battery packs) — 25–70% off new depending on the part — and **close to no lever at all for certified aviation-specific hardware** (Rotax). The one Rotax used-market listing found ($35,000 for a 915 iS) is *above* v1's new-parts quote ($31,500), not below it. Certified engines hold value tightly on a thin, low-supply used market; there is no salvage-yard analog for a Part 33-adjacent powerplant the way there is for a wrecked EV or a parted-out sportbike. **This is a first-principles reason, not a data artifact, to expect the whole used/salvage lever to concentrate on the electric side and the motorcycle-ICE side of any combo, and to do essentially nothing for the Rotax-anchored combos (1, 2).** The scored results below bear this out.

### 9.2 Two-column BOM per combo

Battery shown in two used/salvage states: **(new)** keeps the $10,000 DIY-LFP baseline; **(salvage, provisional)** credits the $4,100 salvage-pack line **plus** the integration cost that line does not include on its own (§9.5) — shown for completeness but explicitly not creditable toward a final number until [AER-67](/AER/issues/AER-67) rules. Reduction/coupling, HV wiring/switchgear/fusing, and the contra-rotating prop are bespoke or safety-critical items with no salvage channel identified this pass — carried at v1's new price in both columns.

| Combo | New total (v1.1) | Used/salvage total (new battery) | Used/salvage total (salvage battery, provisional) | Electric-hardware-only, used |
|---|---:|---:|---:|---:|
| 1 — Premium Anchor (Rotax 916 + Emrax) | $130,900 (+162%) | $115,203 (+130%) | $113,663 (+127%) | $25,730 (was $40,000) |
| 2 — Certified-Turbo Budget (Rotax 915 + Hyper9) | $81,840 (+64%) | $76,835 (+54%) | $75,295 (+51%) | $11,850 (was $16,400) |
| **3 — H-Budget-Solo (Hayabusa + Hyper9) — LEAD** | **$55,990 (+12%)** | **$50,985 (+2%)** | **$49,445 (−1.1%, i.e. under)** | **$11,850 (was $16,400)** |
| 4 — H-Budget-Robust (Hayabusa + Tesla DU generator) | $63,689 (+27%) | $54,559 (+9%) | $53,019 (+6%) | $15,099 (was $23,399) |
| 6 — Kawasaki H2 Budget | $65,890 (+32%) | $60,885 (+22%)¹ | $59,345 (+19%)¹ | $11,850 (was $16,400) |
| 5, 7, 8 | Unchanged from v1.1 | Not re-priced — see note | Not re-priced | — |

¹ Using the midpoint of the already-used $8k–$18k Kawasaki H2 range ($17,000, unchanged from v1). An aggressive low-end-of-range reading ($12,000 engine, same $4,000 conversion) plus the provisional salvage battery brings Combo 6 to **$53,845 (+8%)** — shown for completeness, not used as the scored figure, because "low end of a stated range" is not a listing the way the Combo 3/4 figures above are.

**Combos 5, 7, 8 are not re-priced in v2.** Combo 5 (H3X HPDM-180R ×3) is aerospace-boutique hardware with no secondary market — there is no salvage channel to price, which is itself the finding, not an oversight. Combos 7 (DeltaHawk) and 8 (AantFarm) remain entirely unpriced on new parts in v1.1; used/salvage pricing is not meaningful to add on top of "no price exists at all."

### 9.3 Bill's hypothesis, tested directly: does "used Hayabusa + used Tesla/EV drive unit" close the 12%?

**Read literally — swap Combo 4's generator for a used Tesla drive unit — no, it does not close.** Combo 4 fully used/salvage-sourced (used Hayabusa, used bare-pull Tesla DU + mandatory T-2C, used Hyper9 propulsion motors) lands at **$54,559 (+9%)**, or **$53,019 (+6%)** crediting the still-provisional salvage battery. Better than v1's new-parts $63,689, but not under $50k either way. The reason is a fixed cost the used market cannot discount: the **$2,699 EV Controls T-2C VCU is mandatory for any Tesla drive unit, new or salvage** — the inverter firmware is proprietary and won't take an external command without it (§5.2 background, `MOTOR_CONTROLLER_TRADE_MATRIX.md`). That tax, plus DIY mounting/prep hardware a bare pull doesn't include ($1,500, ESTIMATE), means a used Tesla DU generator line ($7,199) is **more expensive than a used Hyper9 HV generator line ($3,950)** — the Tesla path buys generator headroom (220 kW peak vs. the 96 kW floor), not cost savings, exactly as v1 already found for the new-parts case. Used/salvage sourcing does not change that verdict.

**Read as "aggressively used/salvage-source the whole lead combo" — yes, narrowly, and only with an asterisk.** Combo 3 (Hayabusa + Hyper9, not Tesla) fully used/salvage-sourced reaches **$50,985 (+2%)** without touching the battery, and **$49,445 (−1.1%, under the line)** if the salvage battery is credited. The lever that actually closes most of the gap is the **used Hyper9 generator and motors** ($11,850 vs. $16,400 new — a $4,550 swing, larger than the battery's own $1,400–$5,900 swing depending on how it's counted), not the ICE (already used-sourced in v1) and not a Tesla drive unit (which, per §9.3 above, isn't the cheaper path even used).

**Net answer to Bill's specific hypothesis:** the *Tesla drive unit* half of it doesn't hold up as a cost lever, even sourced aggressively. The *used/salvage broadly* half of it does — just via the Hyper9 electric side, not the Tesla DU, and it gets there by inches, not by a wide margin.

### 9.4 Re-scored ranking (used/salvage, cost dimension only)

Performance and Safety scores are **unchanged from §3.2** — sourcing a component used doesn't change which engine/generator/motor it is, so the derate status (§1.3), the ECU severity ruling, and the zero-sustained-duty-data flags all carry over unchanged. Only the Cost sub-score moves, using the same 1–5 scale defined in §3.1.

| Rank basis | Combo | Cost (used, no battery credit) | Cost (used, salvage battery) | Weighted score (no battery credit) | Weighted score (salvage battery) |
|---|---|---:|---:|---:|---:|
| — | 3 — H-Budget-Solo | 4 *(1–15% over, same bucket as new)* | **5** *(at/under)* | 2.80 *(unchanged bucket)* | **3.20** |
| — | 4 — H-Budget-Robust | 4 *(up from 3)* | 4 *(no further bucket change)* | 2.80 *(up from 2.40)* | 2.80 |
| — | 1 — Premium Anchor | 1 *(unchanged bucket)* | 1 *(unchanged)* | 2.65 *(unchanged)* | 2.65 |
| — | 8 — 3× AantFarm (reference, not re-derived) | — | — | 2.55 *(carried)* | 2.55 |
| — | 6 — Kawasaki H2 Budget | 3 *(up from 2)* | 3 *(midpoint reading)* | 2.40 *(up from 2.00)* | 2.40 |
| — | 2 — Rotax 915 Budget | 2 *(up from 1)* | 2 *(unchanged bucket)* | 2.35 *(up from 1.95)* | 2.35 |
| — | 5 — H-Premium-Technical | 1 *(unchanged, no used channel)* | 1 | 1.35 *(unchanged)* | 1.35 |

**A scoring-scale artifact worth naming, not hiding:** under the no-battery-credit reading, Combo 3 and Combo 4 tie at 2.80 — the discrete cost bucket (1–15% over = score 4) doesn't distinguish Combo 3's 2% over from Combo 4's 9% over, even though Combo 3 is $3,574 cheaper in absolute dollars and is the only one of the two with any realistic path under the line at all. **The recommendation in §9.6 goes on absolute dollars and on which combo can actually clear $50k, not on the tied weighted score.** Once the battery question resolves (either direction), Combo 3 either pulls clearly ahead (if credited) or the tie holds (if not) — nothing in §9.5 can make Combo 4 the better answer, because Combo 4's own generator-line cost is fixed by the T-2C tax regardless of how the battery question resolves.

**DES-INT-001 second architecture — unaffected.** Combo 1 remains the architecturally distinct fallback per v1.1 §7: even fully used/salvage-sourced it's $113,663–$115,203 (127–130% over), nowhere near budget contention, which is exactly why it works as "the proof the mission is achievable today, at a known, high, certain cost, if the Hayabusa bet doesn't pay off." Used/salvage sourcing doesn't change that role.

### 9.5 Safety gate — the salvage battery is not a cost-only decision

Every used/salvage line item in §9.1–§9.4 **except the battery** is the same category of decision SAFETY already ruled on in AER-62: buying a used Hayabusa, a used Hyper9, or a used Rotax changes *how much wear-and-hours history is unknown* on a component whose failure mode is already FMEA'd (engine-out, generator-out) and already carries the interim continuous-duty derate or a real manufacturer rating. `maos-drivetrain-economics`'s own existing mitigation — buy low-mile, inspect carefully, run break-in hours on a test stand before flight — already covers this class of risk, and nothing about buying it used moves it into a new hazard category. **PROPULSION is treating those lines as cost-only decisions**, consistent with Bill's R2 framing.

**The battery is different, and PROPULSION is not pricing it as if it weren't.** Per SAFETY's own AER-62 §3 ruling, the battery is *"the sole emergency reserve standing between an ICE/generator failure and total propulsion loss, with no peer battery to fall back on"* in the 1G architecture. A salvage Tesla pack — even one built on the SAFETY-ruled-correct LFP chemistry — carries unknowns a used Hayabusa doesn't: unknown donor-vehicle collision/flood/thermal-event history, unknown cycle count and depth-of-discharge history, and a factory BMS that's vehicle-locked and must be re-hosted on unproven aftermarket hardware (the same category of problem as the Tesla-drive-unit/T-2C precedent, but on the pack that has no backup if it's wrong). **This is why the $8,600 "salvage, provisional" figure in §9.1–§9.4 is not the sourced $4,100 pack price alone** — it already carries PROPULSION's own $4,500 of unsourced ESTIMATE placeholders (aftermarket BMS $2,000, cell-health requalification labor $1,500, repackaging/mounting $1,000) precisely because pricing the bare pack price alone would understate what actually has to happen before that pack can go on the aircraft.

**[AER-67](/AER/issues/AER-67) is open to SAFETY**, asking for: provenance/history acceptance criteria, condition-testing thresholds, a ruling on whether aftermarket-BMS re-hosting is a new hazard class needing its own interim derate (analogous to the ICE's 50%-of-documented-steady-state rule), and a remaining-capacity credit policy so the reserve-duration math doesn't quietly assume fresh-pack capacity from a used pack. **Until AER-67 answers, the salvage-battery column in §9.2/§9.4 is not creditable toward a final $50k determination** — it is shown so the board can see the shape of the number, not adopted as the basis for a yes.

### 9.6 Is the whole-powertrain target met ≤$50k under used/salvage — plainly

**Not yet cleared, and cleared only by a hair once it is.**

- **Without the salvage battery (the only fully-resolved-today number): $50,985, 2% ($985) over the line.** This is the closest any combo has come in either version of this study, closed almost entirely by used/salvage sourcing on the Hyper9 generator and motors — not by the engine, and not by a Tesla drive unit.
- **With the salvage battery credited (provisional, pending AER-67): $49,445, ≈1.1% ($555) under the line.** This is a real result, not a rounding trick — but it rests on a battery-sourcing path SAFETY has not yet ruled acceptable, priced with $4,500 of PROPULSION's own unsourced integration-cost estimates layered on a $4,100 sourced pack price.

**Recommendation on disposition:** given a margin this thin (1–2% either side of the line, well inside the noise of a BOM built on midpoints, ranges, and one extrapolated engine price), report this to Elon as **"target essentially met, margin negligible, one open safety gate away from a clean under-$50k number"** rather than an unqualified yes or a trigger to reconsider build-our-own. Build-our-own remains not triggered — the same conclusion as v1.1 §7, now on firmer ground: a real, under-$50k-or-a-hair-over path exists using entirely off-the-shelf used/salvage components, no from-scratch engineering required to reach it.

**The lead combo does not change.** Combo 3 (turbo Hayabusa + Hyper9 HV generator + 2× Hyper9 AC-X1 motors + 40 kWh LFP battery) was the lead in v1.1 on new-parts pricing and remains the lead — now more clearly so — on used/salvage pricing. Everything else in §7's recommendation (the bench-endurance evidence gate, the DES-INT-001 fallback to Combo 1, the market re-evaluation triggers) is unchanged by this pass; §9 revises the cost picture, not the engineering disposition.

### 9.7 Open items — v2 additions

1. **[AER-67](/AER/issues/AER-67) — closed, SAFETY.** Ruling: conditional acceptance. A qualifying salvage pack may count toward the ≤$50k cost figure now (unchanged from §9.6); it earns **zero** safety credit toward the verified 40 kWh reserve until (a) per-unit acceptance testing and (b) a *named, bench-validated* aftermarket BMS close. §9.8 below is PROPULSION's first pass at (b) — candidates named, not yet validated. Does not change the $50,985 / $49,445 figures in §9.6; the salvage-battery column remains provisional exactly as stated there.
2. **Vendor/listing refresh needed:** the Recharged Tesla-DU bare-pull citation (§9.1) is a search-snippet extraction from a page that returned HTTP 410 on direct fetch — treat as directionally sound, not as a live quote, until a current listing is pulled directly.
3. **No direct used-market listing found** for Rotax 916 iS or Emrax 228 — both used EXTRAPOLATED ratios from a comparable sourced component (§9.1). Low priority given neither combo is within reach of budget contention regardless.
4. **Gen1 turbo Hayabusa single-listing ($2,500, §9.1)** is not folded into any scored total — it's a real but non-repeatable data point, and it's a lower-base-rating engine than the Gen3 this study's derate table assumes. Flagged for the weekly-cadence follow-on (AER-59) to watch for a repeatable Gen3-equivalent used-turbo-engine market, not acted on here.
5. **All other v1.1 open items (§8) carry forward unchanged** — the bench endurance program, the AERO/PROPULSION altitude-floor item, the ICE-FLT-001 turbo-fault-mode confirmation, the Hyper9 HV AC-X144 datasheet pull, and the DeltaHawk/AantFarm vendor quotes. None of them are resolved or superseded by this cost-focused pass, per Bill's explicit deferral of the bench test (AER-65 item 5).

### 9.8 Aftermarket BMS candidates for salvage-pack re-hosting (AER-67 follow-on, AER-59 weekly desk pass, 2026-08-09)

**Status: names candidates only — does not close AER-67's safety gate.** SAFETY's AER-67 ruling asked for a *named* aftermarket BMS, bench-validated for protection limits, active cell-balancing, and fail-safe behavior on communication/watchdog loss, before any salvage-pack capacity counts toward the verified reserve. No BMS product had been proposed as of that ruling. Per Bill's standing "iterate first, don't fund yet" posture, this is desk research (product identification and datasheet/vendor-page review), not a bench spend — nothing below is validated, and nothing here changes the $0 safety credit in §9.6/§9.7 item 1.

| Candidate | Balancing | Protection limits | Fail-safe on comms/watchdog loss | Price (indicative) | Integration risk |
|---|---|---|---|---|---|
| **Orion BMS 2** (Ewert Energy Systems) | **Passive** (dissipative), current not published | Per-cell OV/UV, per-channel over-temp, pack over-current (CCL/DCL) — configurable, widely documented | Dual CAN 2.0B; community-documented practice is to drive contactors open on a fault/timeout, but the vendor page does not itself state default watchdog timeout behavior — needs the full manual pulled before this is a confirmed spec | $820 (24-cell) – $1,680 (180-cell) base unit; our ~90–108S pack lands near the top of that band. Add current sensor, thermistor harness, wiring — call it $2,000–$2,700 all-in, unquoted | Largest EV-conversion install base and community track record of any candidate here; but **passive balancing does not meet SAFETY's "active cell-balancing" spec as stated** — flagged below, not silently substituted |
| **Elithion Lithiumate** (Pro) | **Passive** (dissipative, "top balance") | OV/UV/over-current/over-temp protection stated; built-in contactor drivers with precharge | Contactor-driver hardware present; comms-loss/watchdog behavior not documented on the public pages pulled this pass — needs a vendor RFQ/spec call | **Quote-only, not published** — itself an open item, not a number | Modular to 255 cells / 16 banks, comfortably covers our series count with margin; longest-standing EV-conversion-market vendor of the three, but least pricing transparency and, like Orion, **passive not active balancing** |
| **Batrium** (WatchMon CORE + CellMate K9 cell monitors) | Not confirmed this pass — CellMate K9 balancing type/current not stated on the vendor page fetched; the discontinued LongMon predecessor's balancing spec also wasn't published | Configurable via WatchMon CORE rules engine (general description only, no threshold list pulled) | Optional expansion board offers 3 mechanical + 3 solid-state relays for external contactor control; default watchdog-timeout behavior not confirmed | Not confirmed for a full ~100S kit — only component prices found (LongMon ~$28, WatchMon CORE ~$314), not a system total | Explicitly markets to both EV traction and stationary storage; scales to 250 cells. **Weakest-confirmed candidate of the three on this pass** — needs a direct vendor spec pull before it's rankable against the other two |

**The honest finding, stated plainly: "active" cell-balancing does not appear to exist, off-the-shelf, at our series count (~90–108S) in this market segment.** The one product confirmed this pass with true active (2A bidirectional) balancing — REC's "Active BMS" — is a 4-cells-per-unit product built for 12V/48V marine and solar systems; REC's own large-series product for EV-scale packs (the Q/2Q series, 16S per board, CAN, chainable) is **passive-balancing only**, the same pattern as Orion and Elithion. Chaining ~25 of the small 4S active-balance units to cover a ~100S pack is technically conceivable but multiplies board count and failure points well beyond anything with a track record — not a real candidate for a flight-critical reserve on this pass. All three named candidates above do mature, well-documented **passive** balancing at automotive series-count instead. This is worth SAFETY seeing directly: either passive balancing is acceptable for the bench-validation gate (the market's proven answer), or the active-balancing bar as stated rules out the entire mature EV-conversion BMS market and points toward a custom or industrial-ESS-derived solution — a materially different, likely more expensive path. Not escalating this as a blocker (per Elon's standing note, nothing here moves the cost or safety score — it is still $0 credit either way) but flagging it so the distinction isn't lost when a bench program is scoped.

**Shared integration risk, all three candidates equally:** the Tesla SR+/RWD pack is a CATL cell-to-pack (CTP) structural pack, not a conventional modular pack with per-module sensing boards and accessible cell taps. Any of the three BMS's above needs a from-scratch harness tapping ~90–108 individual cell-group voltage points from a pack not designed for that kind of teardown access. That harness-fabrication task is a real, nontrivial cost and schedule risk independent of which BMS wins — it belongs in any future bench-program estimate, not folded into a single vendor's risk column.

**If/when Bill authorizes a bench spend, PROPULSION's ranking for what to bench first:** Orion BMS 2 first (price maturity, largest install base, most-documented protection/CAN behavior — the passive-vs-active gap needs a SAFETY answer before or alongside the bench, not after), Elithion Lithiumate second (headroom on cell count, needs an RFQ to get a real price), Batrium held pending a direct vendor spec pull — not enough confirmed this pass to place it.

---

## 10. v3 — Widened ICE Sourcing (China/Russia/Eastern Europe) + Donut Ring-Motor Candidate Row (AER-65, R3)

**Trigger:** Bill's 2026-08-09 comment on AER-56, relayed by Elon as R3 on AER-65: engine sourcing is geographically unrestricted — Chinese, Russian, and Eastern European mass-produced engines are explicitly fair game alongside the turbo-Hayabusa baseline, catalogued as named rows with sourcing/support risk surfaced (not pre-excluded). Separately, the Donut Labs ring/hub motor is added as a candidate motor line (packaging: tail-boom root, per a parallel CAD-marketing thread) — a low-commitment catalog entry, not a re-opened architecture study. Everything in §0–§9 stands; this section only adds rows and re-tests whether the wider net beats §9.6's finding.

### 10.1 Widened ICE/generator prime-mover catalog

| Candidate | Origin | Type | Credited cont. power | Weight | Price (new) | Sourcing/support risk | Disposition |
|---|---|---|---:|---:|---:|---|---|
| **Zongshen CA550T** | China | Turbocharged, liquid-cooled, opposed-4, purpose-built aviation, **published TBO** | 106.6 kW / 145 hp (manufacturer continuous rating — no SAFETY interim derate needed, §1.3 doesn't apply) | 80 kg / 176 lb (incl. prop reduction gearbox) | **$63,144 CAD ≈ $45,300 USD** (CAD→USD at 1.394, 2026-08-08 rate; SOURCED, CKD Aero shop listing) | **Low-moderate.** China's largest piston aircraft-engine manufacturer by volume; real Western distribution exists — ZS AeroEngines Central Europe (Poland) and CKD Aero (Canada) — unlike most rows below. No US export-control regime targets this class of Chinese civil good today. Parts/service network is thin and unproven at North American scale relative to Rotax's decades-deep network. | **Priced below (Combo 9).** The only turbocharged, non-Hayabusa/H2 candidate in this catalog with a manufacturer-published continuous rating *and* TBO (1,000 hr) — a real safety-case improvement over every Hayabusa/H2 combo's zero-sustained-duty-data flag (§1.3). Costs as much as Rotax; does not solve the cost problem. |
| Chinese automotive 1.5T turbo I4 (Geely/Chery/Great Wall class — e.g. Chery E4T15C, Geely BHE15) | China | Turbocharged, water-cooled, automotive, mass-produced at automotive (millions/yr) scale | 73–133 kW / 98–178 hp class, per-model (SOURCED spec sheets, made-in-china.com/carnewschina.com listings) | Not confirmed for a specific model this pass | **No fixed price found** — B2B listings are wholesale-quote-only; a new-crate estimate of $2,000–5,000 and a salvage-pull estimate of $500–1,500 are PROPULSION's own EXTRAPOLATION from the commodity-automotive-parts pattern in §9.1, **not sourced quotes** | **High.** No identified standalone-unit import/distribution channel to the US for these specific engine families — they ship inside Chinese-domestic-market vehicles not sold in North America. Sourcing would mean parting out a non-US-market vehicle or finding an unsurveyed industrial/genset OEM channel. | **Not priced as a combo.** The disqualifying factor isn't cost, it's engineering readiness: **no aviation/homebuilt conversion precedent was found** for this engine family — unlike the Hayabusa, which has a decades-deep motorsport/homebuilt aftermarket-turbo-to-generator ecosystem (§5.2) that is itself load-bearing for why Combo 3 is buildable at all. Adopting this engine would mean originating that ecosystem from zero: cooling-system redesign, bellhousing/mount fabrication, ECU integration — costs this catalog has never had to price for any other row. Flagged as a watchlist item, not evaluated further. |
| **Verner 9V** (9-cylinder radial) | Czech Republic (Eastern Europe) | **Naturally aspirated**, air-cooled radial, purpose-built aviation | 101.4 kW / 136 hp (manufacturer continuous rating) | 238 lb / 108 kg | $27,500 (SOURCED, scalebirds.com 2024 price list — flag: list may be stale by ~2 yr) | **Low.** 20+ year EU ultralight-aviation manufacturer (Vikýřovice, Czech Republic) with existing US dealer/support coverage per KITPLANES and EAA AirVenture coverage — genuinely mass-produced within the small-aviation-engine category, not a one-off shop build. | **Priced below (Combo 10).** Not turbocharged — doesn't literally answer Bill's turbo question — but is the cheapest engine in the entire catalog (new or used) with a genuine manufacturer continuous rating and no SAFETY derate exposure. The real "is there a cheaper Rotax" answer, just not the "is there a cheap turbo" answer. |
| Vedeneyev M14P (9-cylinder radial) | Russia | Naturally aspirated, air-cooled radial | 268 kW / 360 hp — **2–3× oversized** for this application | ~476 lb / 216 kg — >2× the incumbent Rotax 916 iS | ~$46,000 (2019-dated quote; SOURCED but stale, not re-quoted this pass) | **High.** Sole manufacturer is Voronezh Mechanical Plant, a Russian state-affiliated, defense-adjacent enterprise. Genuine sanctions/export exposure for a US-based open-source project attempting new-production sourcing; parts network was already documented as thinning pre-2022 (kitplanes.com, "New Life for Old Radials"), before geopolitical risk is even counted. | **Disqualified on power/weight mismatch alone, before sourcing risk is considered.** 2–3× the power class this mission needs and more than double the incumbent's weight — no plausible combo closes with this engine regardless of price. Not priced as a combo. Listed per R3's instruction to surface, not pre-exclude. |
| Anhui Haery "Lark HFE" | China | Turbocharged, **heavy-fuel** (Jet-A/diesel-cycle), 4-stroke | ~112 kW / 150 hp class (vendor-stated; no independent civil rating found) | 98 kg / 216 lb dry | **No public price found** | **Very high.** Developed for and deployed on the CH-4 medium-altitude military UAV program; no identified civil sales channel. A US-based open-source purchase attempt plausibly runs into the same export-control category as the drone program it was built for. | **Not pricing — unsourceable for this project as a practical matter.** Flagged for completeness per R3's "surface the number and the risk honestly, ranked, not pre-decide it" instruction. The heavy-fuel/Jet-A capability is a genuine GA-relevant feature worth remembering if a civil derivative or civil-market equivalent ever surfaces — that is the only reason it stays on the catalog rather than being dropped. |

### 10.2 Combo 9 — Zongshen Budget: Turbo Zongshen CA550T + Hyper9 HV AC-X144 (gen) + 2× Hyper9 AC-X1 (motors) + LFP battery

| Item | Cost (new) | Cost (used/salvage) |
|---|---:|---:|
| Zongshen CA550T | $45,300 | $45,300 — **no used/salvage channel identified**; recent Western-market import with no secondary-market history, unlike Hayabusa/Rotax (§9.1's certified-hardware finding applies here even though the engine's *origin* is a commodity-manufacturing country — it's sold and priced as aviation hardware, not automotive/motorcycle hardware, and inherits aviation hardware's thin-used-market economics regardless of where it's built) |
| Generator (Hyper9 HV AC-X144) | $5,600 | $3,950 (§9.1) |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | $7,900 (§9.1) |
| Reduction/coupling (Zongshen→generator input — **the engine's integral gearbox is prop-RPM-matched, not generator-RPM-matched; this is a separate, unresolved coupling design, same evidence-gate category as §5.2**) | $1,500 (ESTIMATE, same placeholder basis as every other combo) | $1,500 |
| Battery + BMS (40 kWh LFP) | $10,000 | $10,000 (new) / $8,600 (salvage, provisional — pending AER-67, §9.5) |
| HV wiring/switchgear/fusing | $7,000 | $7,000 |
| Contra-rotating prop | $8,000 | $8,000 |
| Subtotal | $88,200 | $83,650 (new batt) / $82,250 (salvage batt) |
| Contingency (10%) | $8,820 | $8,365 / $8,225 |
| **Total** | **~$97,020 (+94%)** | **~$92,015 (+84%) / ~$90,475 (+81%)** |
| Electric-hardware-only subtotal | $16,400 | $11,850 |

**Reads exactly like Combo 2 (Rotax 915), not like Combo 3.** A manufacturer-rated, TBO-published, no-derate-needed turbo engine costs as much as a certified Western one — because it's priced and sold as aviation hardware, the same finding §9.1 already made for Rotax, just from a different country of origin. Country of manufacture doesn't override "priced/sold as aviation hardware, thin used market" — that's the load-bearing variable, not the flag on the box.

### 10.3 Combo 10 — Verner Budget: Verner 9V (NA radial) + Hyper9 HV AC-X144 (gen) + 2× Hyper9 AC-X1 (motors) + LFP battery

| Item | Cost (new) | Cost (used/salvage) |
|---|---:|---:|
| Verner 9V | $27,500 | $27,500 — no used-market listing found this pass (low-volume manufacturer; expect a thin secondary market by inference, not confirmed) |
| Generator (Hyper9 HV AC-X144) | $5,600 | $3,950 |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | $7,900 |
| Reduction/coupling | $1,500 (ESTIMATE) | $1,500 |
| Battery + BMS (40 kWh LFP) | $10,000 | $10,000 (new) / $8,600 (salvage, provisional) |
| HV wiring/switchgear/fusing | $7,000 | $7,000 |
| Contra-rotating prop | $8,000 | $8,000 |
| Subtotal | $70,400 | $65,850 (new batt) / $64,450 (salvage batt) |
| Contingency (10%) | $7,040 | $6,585 / $6,445 |
| **Total** | **~$77,440 (+55%)** | **~$72,435 (+45%) / ~$70,895 (+42%)** |
| Electric-hardware-only subtotal | $16,400 | $11,850 |

Cheapest engine in the whole catalog with a real continuous rating and no derate exposure, and it still lands 42–55% over the line even fully used/salvage-sourced — the electric side and BOS items (unaffected by which engine is chosen) are more than half the total by themselves. Not turbocharged, so it doesn't answer Bill's literal question, but it is the honest answer to "does a cheaper no-derate-needed alternative to Rotax exist": yes, at roughly half Rotax 916's price, still nowhere near budget contention.

### 10.4 Does the wider net find "the" lightweight mass-produced turbo ICE — plainly

**No.** Neither Zongshen (Combo 9) nor Verner (Combo 10, not even turbocharged) beats Combo 3's economics, used/salvage or not. The Chinese-automotive-turbo bucket is the one candidate class that *could* theoretically beat Hayabusa on unit cost, but it fails on engineering readiness, not price — there is no aftermarket conversion ecosystem to inherit the way the Hayabusa combos do, and pricing a from-zero conversion program is exactly the "build-our-own" question §7 already scoped and declined to open. The Russian and Chinese-military-UAV rows are disqualified/unsourceable for reasons independent of price. **§9.6's finding stands unchanged: Combo 3 (turbo Hayabusa + Hyper9 electric side + LFP battery) remains the lead combo, at $50,985 (+2%, no battery credit) to $49,445 (−1.1%, salvage battery, pending AER-67).** The wider geographic net was worth running — it surfaced a genuine safety-case improvement (Zongshen's TBO/no-derate rating) worth remembering for a future pass if the bench-endurance program (§7) comes back negative on Hayabusa — but it does not change today's cost recommendation.

### 10.5 Donut Labs ring/hub motor — candidate row, not scored

Added per R3 as a candidate propulsion-motor line (replacing/augmenting the Hyper9 AC-X1 role), reflecting Bill's active interest in packaging a ring/hub motor around the tail-boom root — tracked separately as CAD-marketing work, not re-opened here.

| Spec | Value | Source |
|---|---|---|
| Model (closest fit to our per-motor power class) | "17-inch" motor | donutlab.com/motor, 2026-08-09 |
| Power (vendor-stated, "up to") | 150 kW | Vendor spec sheet — **UNVERIFIED, no independent test found for this product line** |
| Torque (vendor-stated, "up to") | 1,200 Nm | Same |
| Mass | 21 kg / 46 lb | Same |
| Continuous vs. peak rating | **Not published** | Not disclosed on vendor spec sheet |
| Efficiency, voltage, cooling method | **Not published** | Not disclosed |
| Price | **Not published** | No public pricing found |
| Aviation use / independent validation | **None found** | See caveat below |

**Why "not credible until independently supported" is not PROPULSION editorializing — it's a documented pattern from the same company.** Donut Lab (an Estonia-based spin-off of Verge Motorcycles) markets a separate solid-state battery product with parallel "up to" performance claims. VTT (an independent Finnish testing institute) ran third-party validation on that battery in 2026: it confirmed the fast-charging claim but found actual energy density at **297 Wh/kg against a claimed 400 Wh/kg** — a real, sourced, ~26% shortfall between vendor claim and independent measurement, on the one Donut Lab product line that has been independently tested to date. The motor line has not been independently tested at all as of this pass. **This is direct evidence for exactly the caution the wake comment asked for, not an assumption**: treat every "up to" figure on the motor spec sheet as an unverified ceiling, not a design number, until a comparable independent test exists for the motor itself.

**Integration reality, same category as every rim-drive note in this catalog:** a ring/hub motor at the tail-boom root is architecturally a rim-drive installation, not a drop-in swap for the coaxial-shaft-driven Hyper9 AC-X1 pairing this study has priced everywhere else. Per PROPULSION's own standing rim-drive findings (marine rim-drive's "cooling is free" and "no bearing needed" properties do not transfer to air — air's volumetric heat capacity is roughly three orders of magnitude below water's, and a large-diameter mechanical bearing at rim tip speed is a genuinely hard problem), any Donut-based propulsion path needs its own first-principles thermal and bearing-support sizing before a mass or a cost can be trusted — the vendor spec sheet answers none of that, because it's a ground-vehicle/wheel-hub product, not an aviation one.

**Disposition: watchlist candidate row, not scored.** No price exists to build a combo with, no continuous rating exists to check against the §1 envelope, and no independent validation exists for the specific claims that would matter (power, efficiency, thermal). Per the wake comment's own framing, this stays a low-commitment catalog entry — a deeper architecture study is warranted only if Donut Labs engages directly with sourced, aviation-relevant data.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1.1 — 2026-08-09. Revises v1.0 to fold in the SAFETY consult ruling ([AER-62](/AER/issues/AER-62)): interim ICE continuous-duty derate (§1.3), revised Performance and Safety scores (§3.2), resolved battery chemistry ruling (§4), and closed consult (§6). The lead recommendation (Combo 3) is unchanged; its basis is not — see §7.*
*Version 2 — 2026-08-09. Adds §9: two-column (new/used-salvage) re-score of every priceable combo per Bill's AER-56 ruling (whole-powertrain scope confirmed, used/salvage sourcing permitted, bench test deferred). Directly tests and substantially rejects the "Tesla drive unit as a cost lever" reading of Bill's hypothesis (§9.3) while confirming a narrower "used/salvage broadly" reading gets the lead combo to within 2% of the line unconditionally and marginally under it pending a new SAFETY consult ([AER-67](/AER/issues/AER-67)) on salvage-battery provenance. Lead recommendation (Combo 3) and its bench-test evidence gate (§7) are unchanged.*
*Version 3 — 2026-08-09. Adds §10: widens the ICE/generator candidate pool per R3 (Bill, via AER-65 comment) to Chinese, Russian, and Eastern European mass-produced engines, cataloged with sourcing/support risk as an explicit column; prices two new combos (Zongshen CA550T, Verner 9V) that do not beat Combo 3; disqualifies or flags-unsourceable two rows (Vedeneyev M14P, Anhui Haery Lark HFE) on power-mismatch and export-control grounds respectively; adds the Donut Labs ring/hub motor as an unscored watchlist candidate row with an independent-testing caution grounded in that company's own battery-product test record. Lead recommendation (Combo 3) and its bench-test evidence gate (§7) are unchanged.*
*Version 3.1 — 2026-08-09. Adds §9.8 (AER-59 weekly desk pass): names three aftermarket BMS candidates (Orion BMS 2, Elithion Lithiumate, Batrium) against the exact spec surface in AER-67's now-closed ruling — protection limits, active balancing, fail-safe on comms/watchdog loss — plus price lines and integration-risk notes. Desk research only, no bench spend; closes none of AER-67's safety-credit gate by itself. Surfaces one substantive finding: mature active (not passive) cell-balancing does not appear to exist off-the-shelf at our ~100S series count in the current EV-conversion BMS market — flagged for SAFETY, not self-resolved. §9.6/§9.7 figures and the Combo 3 recommendation are unchanged.*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
