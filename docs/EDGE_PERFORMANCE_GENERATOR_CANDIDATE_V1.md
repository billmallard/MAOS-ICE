# Edge Performance (Rotax 912/914 Conversions) — Generator Candidate Evaluation (AER-78)

**Status:** Evaluation against the pinned AER-57 envelope. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment.
**Date:** 2026-08-11
**Owner:** PROPULSION
**Origin:** [AER-78](/AER/issues/AER-78), child of [AER-56](/AER/issues/AER-56). Bill named Edge Performance AS on AER-56 as a mass-produced-block ICE lead to score against the same envelope `POWERTRAIN_TRADE_STUDY_50K_V1.md` (AER-57, MAOS-ICE PR #14) used.

**Read this first if you're short on time: §6.**

**A note on which "Combo 3" this compares against.** AER-57's original Combo 3 ($55,990, 12% over $50k) is **stale**. `COMBO3_DETAILED_ENGINEERING_V1.md` (AER-68, PR #15) found the NetGain Hyper9 HV AC-X144/AC-X1 line it was built on has a manufacturer-published continuous rating of **38 kW** — a 60% shortfall against the 96 kW generator floor and a hard ceiling, not a pending-evidence question like the ICE side. `COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md` (AER-73, PR #16) replaced it with EMRAX 268 (MV winding, combined cooling), which passes: **$94,050 total / $51,000 electric-hardware-only (88% over $50k) / ≈634 kg installed.** That is the number this document compares Edge Performance against — not the stale $55,990 figure the AER-78 issue text cites, which no longer reflects a combo that can actually deliver the mission's electrical floor. (Neither AER-68 nor AER-73 has merged as of this pass — both are open PRs — but their finding is not in question; it is a manufacturer-datasheet fact, not a judgment call.)

---

## 1. What Edge Performance actually is

Edge Performance AS (Bømlo, Norway, founded 2007) is an aftermarket shop that converts new or existing Rotax 912/914-family engines: EFI (Autronic SM4 ECU replacing the OEM carburetor/injection), turbocharging or supercharging, big-bore kits, and forged internals for the high-output variants. They are not a from-scratch engine manufacturer — the core block is a genuine Rotax casting, new or customer-supplied, that Edge tunes and re-injects. This matters for two reasons in opposite directions: it inherits Rotax's decades of block/case/gearbox field history (unlike a from-scratch design), but it does **not** inherit Rotax's own published continuous-power rating once tuned, because the whole point of the conversion is to move the engine off Rotax's original power curve.

**Product line sourced this pass** (edgeperformance.no, badasspowersports.com [US dealer], stolcreek.com [US dealer], Facebook, KITPLANES, Plane+Pilot — web pass 2026-08-11):

| Model | Type | Peak power | Peak torque | TBO (mfr-stated) | Price (new) |
|---|---|---:|---:|---:|---:|
| **EP912STi** (headline product, named in AER-78) | Turbo, EFI, 912ULS core | **154 HP / 114.8 kW** | 182 Nm | Not stated for this specific model | **€28,000 ≈ $32,340** (crate-new 912ULS core included; 1.155 EUR/USD, 2026-08-10) |
| EP915ECi | NA big-bore, 1484cc | 120 HP / 89.5 kW | — | Not stated | Not published |
| EP916ECi | NA big-bore, 1621cc | 130 HP / 96.9 kW | — | Not stated | Not published |
| EP917Ti | Turbo | 160–180 HP / 119–134 kW | — | **1,200 hr** | 45,000 (currency not confirmed this pass — flag) |
| EP918Ti | Turbo | 185 HP / 138 kW | — | **2,000 hr** | Not published |

Sourcing quality note: the reseller pages (STOL Creek, BadAss) disagree with each other and with Edge's own site on some specs — one dealer lists EP912STi as "naturally aspirated, 160 hp," which contradicts Edge's own site and Facebook post (turbo, 154 hp) and every independent aviation-press source (KITPLANES, Plane+Pilot). **This document uses Edge's own site + Facebook + press coverage as the higher-confidence source (154 HP / 182 Nm, turbocharged, 912ULS core) and flags the dealer-page discrepancy as an evidence-quality problem with this vendor's public spec surface, not resolved here.**

**Real, sourced differentiator vs. Hayabusa/H2: Edge has an actual endurance/TBO program.** KITPLANES reports Edge has torn down engines at 200, 500, 1000, 1200, 1500, and 2000 flight hours, and two of their five catalogued turbo variants carry manufacturer-stated TBO figures (1,200 hr and 2,000 hr). **No motorcycle-engine candidate in this catalog (Hayabusa, Kawasaki H2) has any endurance data at all, at any duty cycle.** This is a genuine, sourced evidence-class improvement — but see §3 for why it does not, by itself, resolve the specific gating question this document was asked to close.

---

## 2. The gating question: what continuous rating would Edge stand behind for generator duty?

**Answer: none is published, for any model, at any duty cycle.** Every spec above is a single headline crank number (dyno peak), the same evidentiary shape as the Hayabusa's "190 hp" figure SAFETY already ruled is not continuous-duty evidence (AER-62 §1). The TBO/teardown program (§1) demonstrates the engine survives normal GA duty — climb, cruise, descent, varying throttle and RPM — for the stated hours. It does not demonstrate, and does not claim to demonstrate, sustained fixed-RPM/fixed-load output at a single generator-duty operating point for hours on end. Those are different questions, and Edge's own literature does not answer the second one.

**Applying SAFETY's existing interim rule (AER-62 §1, unchanged and not re-litigated here) exactly as it was applied to Hayabusa:** *"credit no more than 50% of documented steady-state output, defaulting to 50% of stock rated crank output where none exists."* No steady-state figure exists for any Edge model, so the default applies:

| Model | Stock rated crank output | Credited continuous (50%) | vs. 96 kW floor |
|---|---:|---:|---|
| **EP912STi** (headline product) | 114.8 kW | **57.4 kW** | **Below floor by 38.6 kW (40%)** |
| EP917Ti (180 HP variant) | 134.2 kW | 67.1 kW | Below floor by 28.9 kW (30%) |
| EP918Ti (largest catalogued) | 138.0 kW | 69.0 kW | Below floor by 27.0 kW (28%) |
| *For reference — Hayabusa (Combo 3)* | *140 kW* | *~70 kW* | *Below floor by 26 kW (27%)* |

**This is the finding the issue asked not to gloss: under the same standard already applied to Hayabusa, Edge Performance's headline product credits worse than Hayabusa (40% short vs. 27% short), and even Edge's largest, best-documented, TBO-published catalogued engine (EP918Ti) still credits marginally worse than Hayabusa (28% vs. 27% short) — because Edge's turbo tunes target a lower absolute peak than a full aftermarket-boost Hayabusa build (114–138 kW peak vs. Hayabusa's 200–250 kW proven boost-ceiling headroom, itself only headroom evidence, not continuous evidence, per AER-62 §1). No catalogued Edge product clears the 96 kW floor on credited numbers.** To clear 96 kW credited under this rule at all, a documented peak of ≥192 kW / 257 HP would be needed — no Edge product approaches that.

**A fair caveat, not a self-certified exception:** Edge's evidence base (a real TBO/teardown program, a genuine Rotax core with decades of case/gearbox field history) is qualitatively stronger than Hayabusa's (zero endurance data of any kind, no aviation precedent at all). Per this profile's standing rule against self-certifying safety criteria, PROPULSION is not adjusting the derate rule here — that call belongs to SAFETY, the same as it did in AER-62. **This is worth a targeted SAFETY question — does a real multi-hour variable-duty TBO program on an aviation-precedented core justify a less conservative default than "50% of peak" — but until SAFETY rules on it, the number credited above is what this document scores against, exactly as AER-62 requires.**

---

## 3. RPM-to-generator match — better than Hayabusa's, with one open engineering question

The Rotax 912/914 family (912ULS core under the EP912STi) runs a max continuous of **5,500 RPM** and a 5-minute takeoff/max of **5,800 RPM** — well-documented, published Rotax figures the trade study already cites for the un-modified 912/915/916 line. Edge's turbo conversion does not change these RPM limits (it changes cylinder pressure/boost, not the crank speed envelope).

The stock 912/914 ships with Rotax's own integral reduction gearbox (B or C gearbox, typically ~2.43:1), tuned to deliver **prop-speed output around 2,300 RPM** — the wrong output for this application. At that output speed, EMRAX 268 (limiting speed 4,500 RPM, continuous torque 250 Nm) is **torque-limited to roughly 60 kW** (P = τ·ω at 250 Nm × 2,300 RPM ≈ 60 kW) — short of the 96 kW floor by itself, independent of the ICE-side derate question above.

**The workable path is the same one already used for Combo 1 (Rotax 916 + Emrax) and the corrected Combo 3 (Hayabusa + Emrax): couple the generator to the engine at crank speed, before the integral prop-reduction gearbox, not after it.** At 5,500–5,800 RPM crank speed against EMRAX 268's 4,500 RPM limiting speed, the needed reduction is **≈1.22:1–1.29:1** — a *smaller* ratio than the corrected Hayabusa path's 1.44:1 (AER-73 §3), and far smaller than the original ~2:1–2.3:1 Hayabusa-to-Hyper9 ratio. This is a genuinely favorable finding for Edge on mechanical grounds.

**The open question this document does not resolve:** taking power off the crank *before* the integral gearbox means bypassing or removing Rotax's stock reduction unit — which also houses the torsional shock-absorbing slipper clutch protecting the crank/prop-shaft interface from prop-strike and combustion-torque-ripple loading. Neither Edge nor Rotax publishes a rated PTO or accessory pad on the 912/914 capable of carrying full continuous generator torque (~165–200 Nm at the reduced RPM) — this is a **novel mechanical adaptation**, not a documented, precedented one the way the belt-reduction-off-the-output-shaft approach is for Hayabusa (§5.2 of the trade study, "well-documented in motorsport applications"). **Flagged as an open engineering item, same evidence-gate category as every other reduction-drive line in this catalog — not fabricated as solved.**

---

## 4. Integrated combo BOM — Edge EP912STi + EMRAX 268 ×3 (1 gen + 2 motors) + LFP battery

Reuses the corrected Combo 3 electric side (AER-73) exactly — same generator/motor class, same bus, same battery, same BOS convention — swapping only the ICE line and the reduction/coupling line to reflect §3's findings. This is the only apples-to-apples way to score Edge against the *current, correct* Combo 3, not the stale Hyper9-based one.

| # | Item | Price (new) | Mass | Basis |
|---|---|---:|---:|---|
| 1 | Edge Performance EP912STi (turbo, EFI, crate-new 912ULS core) | $32,340 | 81.5 kg | SOURCED — €28,000 × 1.155 EUR/USD (2026-08-10), Edge Facebook post; mass from STOL Creek/press, "with gearbox, overload clutch, turbocharger, intercooler, exhaust" — **includes the integral gearbox this combo doesn't use in that role (§3); actual installed mass with gearbox removed and a crank-PTO fitted instead is unconfirmed, could go either way** |
| 2 | Reduction/coupling, crank-PTO (novel) → generator input, ~1.22:1–1.29:1 | $1,500 (ESTIMATE, same placeholder basis as every other combo in this catalog) | 12 kg (ESTIMATE, by analogy to the Hayabusa belt-reduction line) | §3 — mechanically smaller ratio than Hayabusa's, but rests on an unprecedented PTO adaptation Hayabusa's path doesn't need |
| 3 | Generator: EMRAX 268 MV + BAMOCAR D3-700/400 | $17,000 | 30.4 kg | AER-73 §3 row 3, unchanged |
| 4 | 2× Propulsion motors: EMRAX 268 MV + BAMOCAR D3-700/400 | $34,000 | 60.8 kg | AER-73 §3 row 4, unchanged |
| 5 | Battery + BMS (40 kWh LFP) | $10,000 | 320 kg | AER-73 §3 row 5, unchanged |
| 6 | HV wiring/switchgear/fusing/contactors | $7,000 | ~15 kg | AER-73 §3 row 6, unchanged (same ~700V bus, same current class) |
| 7 | Coaxial contra-rotating prop assembly | $8,000 | 40 kg | AER-73 §3 row 7, unchanged — **same AERO re-check flag applies (EMRAX's 4,500 RPM/250 Nm operating point)** |
| 8 | Contingency (10%) | $10,984 | — | Same convention |
| | **Subtotal (pre-contingency)** | $109,840 | | |
| | **Total** | **≈$120,824** | **≈560 kg** | |
| | **Electric-hardware-only subtotal** | **$51,000** | | Identical to corrected Combo 3 — the electric side didn't change |

**142% over the $50k line.** For comparison, the ICE line alone is **$32,340 for Edge vs. $8,000 for Hayabusa (used + turbo kit + conversion)** — a $24,340 premium that is the entire reason Edge is more expensive than corrected Combo 3 overall. This is the same pattern this catalog has already found twice: a component sold and marketed as purpose-built/branded aviation hardware (Rotax core + factory-adjacent conversion shop, here; Zongshen CA550T in §10 of the trade study, there) prices like aviation hardware — no salvage-market discount exists for it the way one exists for a stripped motorcycle engine. **No used/salvage channel was found or is expected for Edge Performance conversions** — this is a boutique, low-volume shop (self-described "in-house development and testing by pilot-owners before public release"), an even thinner secondary market than mainstream Rotax's already-thin one (§9.1 of the trade study).

---

## 5. Weight — Edge's one clear, real advantage

| | Engine + turbo/EFI | Reduction/coupling | ICE-side total |
|---|---:|---:|---:|
| Hayabusa (corrected Combo 3, AER-73) | 105 kg | 12 kg | 117 kg |
| **Edge EP912STi** | **81.5 kg** | 12 kg (ESTIMATE) | **93.5 kg** |

**Edge is ≈23.5 kg (20%) lighter on the ICE side** — a genuine, sourced (for the engine itself) advantage, driven by the 912/914 platform's smaller displacement and lighter turbo/EFI package versus a full liquid-cooled inline-four motorcycle engine plus its own turbo/intercooler/exhaust conversion. This does not change the combo-level cost or performance disposition below, but it is real and worth keeping on record — if the ICE-side power/cost gap ever closes (e.g., a future Edge product at higher published boost, or a cost concession), the mass case is already favorable.

---

## 6. Verdict — does not close, on cost and performance; logged as a documented catalog entry, not a hedge in active contention

Scored on the same rubric as §3.1 of the trade study (Cost 40% / Performance 35% / Safety 25%, 1–5 scale):

| Dimension | Score | Basis |
|---|---:|---|
| **Cost** | **1** (>60% over) | $120,824 total, 142% over $50k. Even against the now-superseded $55,990 Hayabusa figure the AER-78 issue text cites, Edge is worse by a wide margin; against the current, correct $94,050 Combo 3 figure, Edge is **$26,774 (28%) more expensive**, entirely on the ICE line (§4). |
| **Performance** | **2** (does not clear 96 kW floor on credited numbers) | Credited continuous 57.4 kW vs. 96 kW floor (§2) — a *larger* shortfall in both absolute kW and percentage than Hayabusa's already-known shortfall. Even Edge's largest catalogued product (EP918Ti, 138 kW peak) still falls marginally short of Hayabusa's own credited number. |
| **Safety** | **2** (zero fixed-RPM/fixed-load generator-duty data, same category as every Hayabusa/H2 combo) | Real TBO/teardown program exists (§1) — qualitatively better evidence than Hayabusa's zero data — but it is variable-duty GA flight data, not the fixed-RPM/fixed-load evidence SAFETY's rule asks for, so it does not change the score under the existing ruling. Flagged in §2 as worth a targeted SAFETY question, not self-adjusted here. |

**Weighted score: 1×0.40 + 2×0.35 + 2×0.25 = 1.60.**

For context, corrected Combo 3 itself — once its cost is honestly restated at $94,050 (88% over, cost bucket also drops to score 1) — scores **1×0.40 + 2×0.35 + 2×0.25 = 1.60**, identical. The two combos land in the same coarse scoring bucket because the electric side (identical, $51,000, dominant cost driver) and the ICE-side performance/safety shortfall (same category for both) swamp the ICE-cost and ICE-mass differences that actually distinguish them. **Read the raw dollars, not just the bucket: Edge is $26,774 more expensive in absolute terms for a worse continuous-power margin.** The tie is a scoring-scale artifact, not a real equivalence — the same kind of artifact the trade study already flagged once for Combos 3/4 (§9.4).

**Answering the issue's three dispositions directly:**

1. **Does not beat or tie Combo 3 on cost or performance.** It is more expensive in absolute dollars against the current, correct Combo 3 baseline, and credits *less* continuous power against the mission floor under the same standard applied to every other candidate in this catalog. Not escalating a re-downselect.
2. **Not advanced as an active hedge above the existing catalog entries.** At a 1.60 weighted score it would rank at or below the weakest combos already on the board (Combo 5 scored 1.35 pre-correction; Combo 2 scored 1.95–2.35 depending on sourcing column) — it does not add hedge value the catalog doesn't already have, and its one real advantage (weight) doesn't move the cost or performance disposition.
3. **Does not close — stated exactly why, per the issue's own ask:**
   - **Continuous rating:** none published for any model; under the existing SAFETY interim rule, credited continuous (57.4 kW) is 40% below the 96 kW floor — worse than Hayabusa's already-known 27% shortfall.
   - **Cost:** $120,824 installed (142% over $50k), $26,774 more than the corrected Combo 3 baseline, driven entirely by the ICE line ($32,340 vs. $8,000) — Edge Performance is priced and sold as branded aviation hardware, not commodity motorcycle hardware, and inherits that pricing class regardless of the underlying Rotax block's mass-production status.
   - **Weight:** the one axis where Edge wins (93.5 kg ICE-side vs. 117 kg, −20%) — real, but not enough to offset the cost and performance gaps.
   - **RPM/reduction match:** mechanically favorable (≈1.22–1.29:1 vs. Hayabusa's 1.44:1, both far short of the original ~2:1–2.3:1 Hyper9-era assumption) but rests on an unprecedented crank-PTO adaptation neither Edge nor Rotax documents, unlike Hayabusa's well-precedented output-shaft belt reduction.

**One finding worth surfacing beyond the specific ask, not acted on here:** Combos 2, 4, and 6 in the original trade study also use the now-disqualified Hyper9 line (AER-68 §7.1) and have not yet received the same electric-side correction Combo 3 got in AER-73. Their scores in `POWERTRAIN_TRADE_STUDY_50K_V1.md` §3.2 are stale in the same way the $55,990 Combo 3 figure is. This is a real gap in the catalog's current state, separate from Edge Performance, and belongs on AER-59's list, not fixed inside this document.

---

## 7. Open items

1. **SAFETY question, not resolved here:** does Edge's real (if variable-duty) TBO/teardown program justify a less conservative interim derate than "50% of peak" for this specific engine class, distinct from a zero-data motorcycle engine? Named in §2; PROPULSION does not self-certify this.
2. **Crank-PTO feasibility** for generator coupling ahead of the integral reduction gearbox — no vendor or precedent found this pass (§3). A real engineering question, not assumed solved.
3. **Dealer-page spec inconsistency** (STOL Creek's "naturally aspirated, 160 hp" EP912STi vs. every other source's "turbo, 154 hp") — unresolved evidence-quality flag on this vendor's public spec surface (§1).
4. **EP912STi mass with the integral gearbox removed** — the sourced 81.5 kg figure includes a gearbox this combo's coupling approach doesn't use in that role (§4 row 1); actual as-installed mass is unconfirmed.
5. **EP917Ti price currency** — "45,000" found without a confirmed currency unit (§1); not load-bearing for this document's conclusion since EP917Ti costs more than EP912STi regardless, but should be corrected before any future pass cites it.
6. **Stale Hyper9-based scores for Combos 2, 4, 6** — flagged in §6, not fixed here; belongs on AER-59.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1 — 2026-08-11. Scores Edge Performance AS's Rotax 912/914 conversions (headline: EP912STi, 154 HP/182 Nm peak) as an integrated generator combo against the pinned AER-57 envelope (96 kW cruise / 155 kW climb), using the corrected (EMRAX 268-based) Combo 3 as the current-truth comparison point rather than the stale Hyper9-based $55,990 figure. Applies SAFETY's existing AER-62 interim continuous-duty derate rule unchanged. Verdict: does not close on cost or performance (§6); real TBO-program and weight advantages over Hayabusa are genuine but insufficient to offset a larger credited-continuous-power shortfall and a $26,774 cost premium over the corrected baseline.*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
