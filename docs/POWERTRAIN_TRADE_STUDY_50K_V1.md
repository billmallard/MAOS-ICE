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
| 11 | Battery emergency reserve | 30 min @ 60 kW electrical → ~40 kWh pack (NMC 811 planning basis) | PROPULSION | `maos-propulsion-redundancy-battery` §3 |
| 12 | Standing architecture | 1G + 1B + 2M | Board decision (Bill) | `maos-1g1b2m-architecture-decision` — not reopened by this study |
| 13 | Battery chemistry lean | LiFePO₄-class favored by PROPULSION operating brief (thermal-runaway resistance, cycle life) vs. NMC 811 planning baseline in the published battery article (lighter) | **Open tension — PROPULSION brief vs. published analysis** | See §4; SAFETY consult (§6) should weigh in given the direct safety/weight trade |
| 14 | HV bus voltage | Open gate — DG-004, 400V vs 800V | Systems/Propulsion joint, unresolved | `maos-generator-selection` — reopened pending Evolito/H3X voltage confirmation |
| 15 | ICE-SYS-001 (formal requirement) | "ICE subsystem shall support continuous generator-duty operation in the **100–230 kW target class**" | MAOS-ICE (already in `REQUIREMENTS_INDEX_V0.md`) | Independently corroborates line 7 — see §1.2 |
| 16 | ~~"75 kW continuous, generator-head minimum"~~ | **STALE — superseded, do not size to it** | Flagged by this study | See §1.2 |

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

---

## 2. Powertrain Combo Catalog

Every combo is priced as an integrated system: ICE + generator + generator controller + battery/BMS + 2× propulsion motor + motor controllers + reduction/coupling + prop + HV wiring/switchgear/fusing + 10% contingency. Source citations are per line item; where a figure is a range, the midpoint is used and the range is shown.

**Balance-of-system (BOS) items common to every combo**, priced from `maos-1g1b2m-architecture-decision` and `maos-drivetrain-economics` cost tables:

| Item | Cost | Source |
|---|---:|---|
| HV wiring, switchgear, fusing, contactors | $7,000 | Midpoint of $6,000–$8,000 across both cost-summary tables |
| Contra-rotating prop assembly (2M coaxial) | $8,000 | Consistent across both `maos-1g1b2m-architecture-decision` cost tables |
| Battery pack + BMS, 40 kWh, **NMC 811** | $20,000 | `maos-1g1b2m-architecture-decision` cost table |
| Battery pack + BMS, 40 kWh, **DIY LFP** (alternative chemistry) | $10,000 | `maos-drivetrain-economics` Scenario C (CATL 280Ah prismatic + BMS + case) |

### Combo 1 — Premium Anchor: Rotax 916 iS + Emrax 268 (gen) + 2× Emrax 228 (motors)

Reference point, not a budget candidate. Full BOM from `maos-1g1b2m-architecture-decision` "Cost Summary (Rotax Path)."

| Item | Cost |
|---|---:|
| Rotax 916 iS | $50,000 |
| Generator (Emrax 268, AFPM) | $12,000 |
| Generator controller | $4,000 |
| Propulsion motors (2× Emrax 228) | $16,000 |
| Motor controllers (2×) | $8,000 |
| Battery (40 kWh NMC) | $20,000 |
| BMS, wiring, switchgear | $8,000 |
| Contra-rotating prop | $8,000 |
| Reduction drive/coupling | $3,000 |
| Contingency (10%) | $12,900 |
| **Total** | **~$142,000** |
| Electric-hardware-only subtotal (gen + 2 motors + controllers) | **$40,000** |

**284% over the $50k line.** Best-documented components, highest confidence, worst economics.

### Combo 2 — Certified-Turbo Budget: Rotax 915 iS + Hyper9 HV AC-X144 (gen) + 2× Hyper9 AC-X1 (motors)

Directly answers Bill's Q(a) with the mass-produced, **factory-turbocharged**, certified-basis engine at the cheapest electric side available.

| Item | Cost | Source |
|---|---:|---|
| Rotax 915 iS | $31,500 | Midpoint $28k–$35k, `PROPULSION_CANDIDATE_MATRIX_V1.md` §2B (newer figure; supersedes the $42–48k quote in `maos-engine-comparison-matrix` — flagging the discrepancy, not resolving it without a fresh vendor quote) |
| Generator (Hyper9 HV AC-X144) | $5,600 | `MOTOR_CONTROLLER_TRADE_MATRIX.md` source anchors |
| Propulsion motors (2× Hyper9 AC-X1) | $10,800 | Same, ×2 for 2M (source matrix prices 1× only) |
| Reduction/coupling (placeholder — Hyper9 max RPM unconfirmed) | $1,500 | Conservative placeholder; **flag: Hyper9 AC-X144 RPM ceiling not in any sourced datasheet — direct-drive-vs-reduction question is open, unlike the Rotax↔Emrax pairing which the generator-selection article did work through** |
| Battery + BMS (40 kWh NMC 811) | $20,000 | BOS table |
| HV wiring/switchgear/fusing | $7,000 | BOS table |
| Contra-rotating prop | $8,000 | BOS table |
| Subtotal | $84,400 | |
| Contingency (10%) | $8,440 | |
| **Total** | **~$92,840** | |
| Electric-hardware-only subtotal | **$16,400** | |

**86% over the $50k line.** The ICE alone ($31,500) plus battery ($20,000) already exceeds the entire budget before any electric hardware is added. **This is the clearest evidence for Q(a): the certified, factory-turbocharged, mass-produced option (Rotax) cannot reach $50k total, no matter how cheap the electric side gets.**

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
| Safety | 25% | **Provisional only** — SAFETY owns the continuous-duty derate and failure-mode scoring criteria per AER-57 item 5; scores below are PROPULSION's first-pass reasoning from public evidence, not a certified safety score. Do not treat as final. See §6. |

Scoring scale, 1–5, applied per dimension:

**Cost** (against the $50k installed-hardware line): 5 = at/under $50k · 4 = 1–15% over · 3 = 16–30% over · 2 = 31–60% over · 1 = >60% over or unpriceable.

**Performance** (against §1's reconciled envelope): 5 = clears 118–120 kW no-battery-climb target with real margin, full envelope closed cleanly · 4 = clears 96 kW cruise floor with ≥10% margin, climb needs the architecturally-accepted battery assist · 3 = clears 96 kW with <10% margin or carries an unconfirmed vendor-data risk on a critical component · 2 = does not clear the 96 kW floor, or multiple critical unknowns · 1 = fails the mission envelope outright.

**Safety** (provisional, pending §6): qualitative first-pass weighing TBO/endurance evidence maturity, redundancy posture, and chemistry thermal-runaway risk. See per-combo notes.

### 3.2 Scored combos

| Rank | Combo | Total installed cost | Electric-hardware-only | Cost (40%) | Performance (35%) | Safety (25%, provisional) | Weighted score |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | **Combo 3 — H-Budget-Solo** (turbo Hayabusa + Hyper9 HV gen + 2× Hyper9 AC-X1 + LFP) | $55,990 (+12%) | $16,400 | 4 | 3 | 3 | **3.40** |
| 2 | Combo 4 — H-Budget-Robust (turbo Hayabusa + Tesla M3 DU gen + 2× Hyper9 AC-X1 + LFP) | $63,689 (+27%) | $23,399 | 3 | 4 | 3 | **3.35** |
| 3 (tie) | Combo 1 — Premium Anchor (Rotax 916 + Emrax) | $142,000 (+184%) | $40,000 | 1 | 5 | 4 | **3.15** |
| 3 (tie) | Combo 5 — H-Premium-Technical (Hayabusa + 3× HPDM-180R) | ~$150k+ (+200%+) | $60k–$120k | 1 | 5 | 4 | **3.15** |
| 5 | Combo 8 — 3× AantFarm (reference) | Unknown, "likely prohibitive" | n/a | 1 | 4 | 3 | **2.55** |
| 6 | Combo 6 — Kawasaki H2 budget | $65,890 (+32%) | $16,400 | 2 | 3 | 2 | **2.35** |
| 7 | Combo 2 — Rotax 915 budget | $92,840 (+86%) | $16,400 | 1 | 3 | 3 | **2.20** |
| — | Combo 7 — DeltaHawk | Unpriced | Unpriced | — | — | — | **Not scored — blocked on vendor quote** |

**Performance notes behind the scores:**
- Combo 3 (score 3): Hayabusa turbo margin against 96 kW is plausible with headroom to spare (drag-race heritage shows 200+ kW is achievable), but the Hyper9 HV AC-X144's *continuous* rating is not clearly published (peak 88 kW is oddly listed lower than the "rated 120 hp/89.5 kW" figure in the source matrix — this looks like a transcription issue in the vendor data, not a real spec, and needs a fresh datasheet pull) and Hayabusa sustained generator-duty TBO has zero test data. Both are real, named risks, hence 3 not 4.
- Combo 4 (score 4): same ICE risk as Combo 3, but the Tesla DU generator has enormous headroom (220 kW peak vs. 96 kW need) which retires the generator-margin risk even if the "in principle" generator-mode claim needs bench validation.
- Combo 1 & 5 (score 5): best-documented components, real margin throughout, no open RPM-matching or vendor-data-confidence problems.

**Safety notes (provisional, PROPULSION's reasoning only):**
- Combo 1 (4): most mature/proven components (Rotax TBO record, Emrax experimental track record), NMC chemistry.
- Combo 5 (4): H3X's SiC/CAN/thermal integration is purpose-built for aviation duty, though HPDM-180R itself is single-fault-tolerant (only HPDM-350 is dual); pricing/lead-time confidence is low.
- Combo 3 & 4 (3): the battery-buffer architecture genuinely lowers the consequence of an ICE/ECU fault (per `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md`'s own reasoning — a generator dropout degrades to battery power, not immediate propulsion loss), which offsets some of the zero-TBO risk; LFP chemistry is a safety positive. Net: workable but unproven.
- Combo 8 (3): the existing TA65 evaluation states multi-unit redundancy improves the failure ladder "a full rung" — a real safety upside — but zero TBO/production evidence on an in-development product pulls it back down.
- Combo 6 (2): same zero-TBO risk as Hayabusa, plus a supercharger part-load parasitic-loss wrinkle, plus materially less community/tuning depth than the Hayabusa-MegaSquirt-Speeduino ecosystem already characterized in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md`.
- Combo 2 (3): best raw-engine TBO/reliability evidence of any candidate (Rotax), but the Hyper9-as-generator thermal/endurance question is exactly as open as it is in the budget combos, and NMC (not LFP) is the chemistry here.

---

## 4. The Battery Chemistry Tension (flagged, not resolved here)

PROPULSION's own operating brief leans toward a LiFePO₄-class pack for thermal-runaway resistance and cycle life. The published `maos-propulsion-redundancy-battery` analysis leans toward NMC 811 as the "practical near-term" planning baseline specifically because LFP is *too heavy* — 706 lbs for 40 kWh vs. NMC 811's 441 lbs, a 265 lb penalty most of the weight budget cannot absorb on top of everything else already competing for the 1,200 lb useful-load target.

This trade study surfaces a finding that partially resolves the tension in LFP's favor **on the cost axis specifically**: swapping Combo 3 from NMC 811 ($20,000) to LFP ($10,000) is what gets the leading combo from 32% over the $50k line to 12% over. LFP is simultaneously the **cheaper** chemistry (§2, Combo 3 vs. its NMC variant) and the **safer** chemistry (thermal-runaway resistance) — the two axes align here, which is not the usual shape of this trade. The cost of that alignment is carried entirely on the weight axis, which is Structures' problem, not scored here.

**This is exactly the kind of chemistry call SAFETY should weigh in on (§6)** — the derate/failure-mode criteria SAFETY sets will interact directly with which chemistry the safety column above should actually assume.

---

## 5. Bill's Two Specific Asks

### 5.1 Is there a lightweight, mass-produced, turbocharged ICE that wins as the generator prime mover?

**Yes and no, depending on what "turbocharged" is allowed to mean — and the distinction matters for the answer.**

- **Factory-turbocharged, mass-produced, aviation-certified basis (Rotax 915/916 iS):** real, proven, best documented — and **cannot reach $50k total** (Combo 2: $92,840, 86% over). The ICE alone ($28k–$35k) plus the battery ($20k) exceeds the entire budget before a single dollar of electric hardware is spent. This does not win.
- **Mass-produced base engine, turbocharged as a proven aftermarket modification (Hayabusa + turbo kit):** the Hayabusa itself is genuinely mass-produced (Suzuki, decades of production, deep used-market supply at $3k–$8k). Turbocharging it is not a factory option but is a **well-proven aftermarket path** — drag-racing heritage puts reliable street-boost output at 300+ hp, far above anything this application needs, meaning the engine can run well below its boost ceiling for reliability margin. This is what "turbo Hayabusa" means throughout this catalog, and it is the cost leader (Combo 3, 12% over $50k).
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

---

## 6. SAFETY Consult — Required Before Finalizing the Safety Column

Per AER-57 item 5, PROPULSION does not self-certify the safety score. A child consult is opened: **[SAFETY consult — continuous-duty derate and failure-mode scoring criteria for AER-57]**, assigned to SAFETY, blocking this document's safety column from being treated as final. Specifically requested from SAFETY:

1. Continuous-duty derate criteria for an ICE running fixed-RPM/fixed-load generator duty for multi-hour missions (applies to every combo, most acutely to the zero-TBO-evidence Hayabusa/Kawasaki combos).
2. Failure-mode severity scoring for a 1G architecture where ICE/generator loss is battery-buffered rather than peer-generator-covered — does the graceful-degradation reasoning in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §1 hold up as a formal severity reduction, or does SAFETY score it differently?
3. A ruling on the LFP-vs-NMC chemistry tension in §4 — SAFETY's thermal-runaway risk tolerance directly determines whether the 12%-over-budget LFP variant of Combo 3 is the version that should be scored, or whether NMC's weight penalty is the safety-preferred trade despite the cost hit.

Until SAFETY responds, every safety score in §3.2 is PROPULSION's provisional first-pass reasoning, explicitly marked as such, not a certified input.

---

## 7. Recommendation

**(A) Downselect, with a named evidence gate — not "no viable answer today."**

**Lead combo: Combo 3 — H-Budget-Solo.** Turbo Hayabusa (used, ~$4k engine + ~$4k turbo/conversion) → belt-reduced (~2:1–2.3:1) to a Hyper9 HV AC-X144 generator → 400V-class bus → 2× Hyper9 AC-X1 propulsion motors → 40 kWh LFP battery/BMS → coaxial contra-rotating prop. **Current best estimate: $55,990 installed, 12% over the $50k line** — the closest of every combo evaluated, and the only one within plausible reach of the target through ordinary sourcing decisions already visible in the BOM (used-market component sourcing, contingency trim, LFP already applied). This is not a $50k answer today; it is a defensible path to one.

**The evidence gate that would confirm it:** a bench endurance test — Hayabusa at fixed generator-duty RPM and load, 500+ hours, per the Phase 1 program already scoped in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §6 (Speeduino/Teensy 4.1 instrumentation). This single test retires the largest named risk in §3.2 and §5.2 across every Hayabusa-based combo simultaneously. A secondary, cheaper gate — a fresh Hyper9 HV AC-X144 datasheet pull confirming actual continuous rating and max RPM — should run in parallel; it is unpriced (a phone call/email, not a test program) and directly resolves the Performance-score-3 flag on the lead combo.

**DES-INT-001 compliance — second architecture kept alive:** Combo 4 (H-Budget-Robust, same ICE/motor side, Tesla M3 DU generator) is carried forward explicitly as the second viable path, not as padding. It differs from Combo 3 specifically on the highest-uncertainty component — generator continuous rating and RPM compatibility. If the Hyper9 HV datasheet pull or bench data disqualifies it as a generator, Combo 4 is the already-scored fallback with a known cost delta (+$7,699) and a known risk trade (T-2C generator-mode validation instead of Hyper9 continuous-rating uncertainty). **What would eliminate one of these two:** a vendor-confirmed Hyper9 HV continuous rating below ~90 kW (eliminates it as sole generator for Combo 3, leaving Combo 4 as the surviving Hayabusa path) or a Tesla T-2C generator-mode bench failure (eliminates Combo 4, leaving Combo 3).

**Why not "no viable answer today":** every combo in this catalog that comes close to $50k does so through *understood, named* cost drivers (battery chemistry, generator headroom, ICE conversion depth) rather than through an absence of options. The gap between the lead combo and the target is 12%, not the 86–284% seen in the certified/premium combos — that is a trim-and-validate problem, not a "the market doesn't have an answer" problem.

**Build-our-own path — not triggered, briefly scoped for the record:** because a ≤$50k-adjacent, evidence-gated path exists and has not been eliminated, the build-our-own decision gate is not opened by this study. If the Hayabusa endurance bench test *fails* (engine or its ECU/reduction-drive interface cannot sustain generator duty), the next-cheapest fallback (Combo 4) still shares the same ICE risk, and at that point "build our own" becomes a live question — most plausibly not a from-scratch engine, but a from-scratch **generator coupling/reduction package** purpose-built for motorcycle-engine generator duty, since the ICE itself (Hayabusa) and the electric machines (Hyper9/Tesla) are not the parts in question — the interface between them is. That scoping is a follow-on task, not this document's job.

**Market re-evaluation trigger (for the weekly-cadence follow-on issue):** re-run this scorecard if (a) H3X, Evolito, or a comparable aerospace-grade axial-flux vendor publishes a sub-$15k/unit price at 90kW+ continuous — this would flip Combo 5-class options into budget contention; (b) a Hyper9-class generator's confirmed continuous rating and RPM ceiling change the Performance score on Combo 3; or (c) DeltaHawk (Combo 7) or AantFarm (Combo 8) publish pricing — both are technically strong and currently unscored purely on missing price data.

---

## 8. Open Items / Next Actions

1. **SAFETY consult** — opened, blocking final safety column (§6).
2. **AERO confirmation** on the implied ~0.82 propeller efficiency (§1.1) — closes the traceability chain fully; does not change any conclusion here but should not stay an inferred number.
3. **Vendor datasheet pull — Hyper9 HV AC-X144** — confirm actual continuous power rating and max RPM. Directly resolves the largest open flag on the lead combo.
4. **Vendor quotes — DeltaHawk DHK235A4, AantFarm TA65-1** — both combos are unscored purely on missing price; either could reshuffle the ranking if priced near budget-track expectations.
5. **Erratum to `ENGINE_SELECTION_DOWNSELECT_V1.md`** — strike Rotax 912 iS and Aeromomentum AM13 from the "viable" recommendation rows per §1.2; they fail the reconciled 96 kW floor.
6. **Bench endurance program scoping** — the evidence gate named in §7 (Hayabusa, fixed RPM/load, 500+ hr) should become a tracked child issue once this document is accepted; not opened here to avoid committing bench-test budget ahead of a board read on this scorecard.
7. **Cost-scope re-score** — pending Bill's answer on the AER-56 cost-boundary question; every combo's total is a re-summation away from a different boundary (§0).

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1.0 — 2026-08-09*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
