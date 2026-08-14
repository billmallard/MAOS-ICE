# Combo 3 Iteration — Corrected Electric-Machine Selection + DG-004 Re-Derivation (AER-73)

**Status:** Kill-gate + DG-004 + packaging/cooling/mass delta pass. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment.
**Date:** 2026-08-10
**Owner:** PROPULSION
**Origin:** [AER-73](/AER/issues/AER-73), child of [AER-56](/AER/issues/AER-56). Responds to the disqualifying finding in `COMBO3_DETAILED_ENGINEERING_V1.md` (AER-68, MAOS-ICE PR #15) §7.1–§7.2: the NetGain HyPer9 HV line cannot deliver the mission's continuous power floor and runs at a 144V-class bus the requirement envelope never assumed.

**Scope discipline, per the issue's own instruction:** the kill-gate and DG-004 re-derivation below are decision-independent and run now. **Rank-scoring the surviving selection against Combo 1 as THE working baseline is explicitly gated on Bill's disposition on AER-56 (confirmation `f6c71029`, still pending as of this pass) and is NOT done here.** This document sources, prices, weighs, and thermally sizes a corrected selection — it does not choose between Combo 1 and a corrected Combo 3.

**Read the verdict first if you're short on time: §5.**

---

## 0. What this document does and does not reopen

Unchanged from `COMBO3_DETAILED_ENGINEERING_V1.md`: the 1G+1B+2M series-hybrid architecture, the coaxial contra-rotating prop, and the turbo-Hayabusa prime mover are not reopened. What changes here is the **generator and propulsion-motor selection only** — replacing the disqualified NetGain HyPer9 HV (AC-X144/AC-X1) line. The AER-68 sourced BOM, packaging summary, and cooling-budget *methodology* are reused; the electric-machine line items and everything downstream of them (cooling loop sizing, HV wiring current class, mass rollup) are recomputed.

---

## 1. Kill Gate — does a 96 kW+-continuous-capable, cost/mass-credible machine class exist?

Per the issue's mandate, three candidate classes were sourced and screened before any packaging/cooling rework: **EMRAX** (named in AER-68 §9 item 2 as a real, already-partially-used candidate — Combo 1 already runs an EMRAX 268 generator), **H3X HPDM-180/250** (already catalogued in the trade study as Combo 5), and **paralleled Hyper9-class units** (named explicitly in this issue).

### 1.1 EMRAX 268 — PASSES the gate

Pulled the manufacturer's current datasheet directly (EMRAX 268 datasheet v1.6, emrax.com, 2025/2026 edition — MFR, primary source, not a reseller page):

| Winding | Cooling | Continuous power S1 | Continuous current | Continuous torque | Mass |
|---|---|---:|---:|---:|---:|
| MV (medium voltage) | Combined (air+liquid) | **117 kW** | 220 A_RMS | 250 Nm | 21.9 kg |
| HV (high voltage) | Combined | 100 kW | 130 A_RMS | 250 Nm | 21.9 kg |
| LV (low voltage) | Combined | 117 kW | 550 A_RMS | 250 Nm | 21.9 kg |

Peak power (60s): 210 kW at 4,500 RPM (limiting speed for all windings). Peak efficiency 96%. Operating voltage range 100–830 Vdc; all windings tested to 833V max.

**Non-obvious finding worth flagging for the record:** the "HV" winding is *not* the best choice for maximum continuous power on an ~800V bus — it delivers *less* continuous power (100 kW CC) than the "MV" winding does at the same bus voltage (117 kW CC), because the HV winding's higher turns-count hits the 830V test-voltage ceiling before it reaches its current-limited continuous rating (datasheet note: "HV option is operating at speeds lower than its limiting, due to 830V voltage limitations"). **The MV winding, not the HV winding, is the correct pick for an ~700–830V bus** — this is a real, non-obvious lesson about EMRAX's winding-selection logic, not a naming convention to pattern-match on.

**Against the mission floor:** generator role needs 96 kW continuous — MV/CC clears it at **117 kW, a 22% margin** (real manufacturer S1 rating, not a peak/dyno figure — the same evidentiary standard AER-68 §7.1 held the HyPer9 to and found it failed). Two propulsion motors combined need 155 kW continuous for climb — 2× EMRAX 268 MV/CC = **234 kW combined, a 51% margin**.

One more corroborating, unverified-in-this-pass data point from EMRAX's own product page: "268 is the first electric engine certified for use in General Aviation by EASA." **Flagged as an MFR marketing claim, not independently verified here** — MAOS targets Experimental Amateur-Built, not EASA type certification, so this isn't load-bearing for this project, but if true it is real third-party evidence this machine class was engineered to aviation continuous-duty standards, not EV-conversion-market standards — a different evidentiary class than the HyPer9's "$5,600 tell" (AER-68 §7.1).

**EMRAX 268 is already used in Combo 1** (as the generator, paired with undersized EMRAX 228 motors — see §1.4 below for a finding on that pairing). It is not a novel or unvetted component to this project.

### 1.2 H3X HPDM-180/250 — screened, does not pass the cost gate

Already catalogued as Combo 5 in `POWERTRAIN_TRADE_STUDY_50K_V1.md` §2: 1 gen + 2 motors at $20k–$40k/unit → **$60k–$120k electric-hardware-only, ≥200% over the $50k line**, before ICE/battery/BOS. Re-confirmed current-generation specs this pass (h3x.tech): HPDM-180 = 180 kW continuous / 16 kg (13.9 kW/kg); HPDM-250 = 200 kW continuous, up to 250 kW peak / 15 kg. Power density is genuinely exceptional — roughly 4–5× EMRAX 268's kW/kg — but **no public pricing exists and the company's own positioning is "premium priced."** No price discovered in this pass that would change Combo 5's existing ≥200%-over disposition. **Kept on the watchlist per the existing catalog entry, not advanced** — this is a frontier-hardware extrapolation (per the profile's own standard for citing H3X-class components), not a sourced BOM candidate at this budget tier.

### 1.3 Paralleled Hyper9-class units — screened, fails on cost, mass, and does not fix the voltage problem

Named explicitly in the issue as an option to price. NetGain's own documentation confirms paralleling is supported ("multiple systems can be combined for heavy-weight and racing vehicles"). Priced out:

- **Generator role:** needs ≥96 kW continuous → minimum 3× AC-X144 in parallel (3×38 kW = 114 kW, 19% margin). Cost: 3×($5,600 motor + $4,000 controller) = **$28,800**.
- **Motor role:** needs ≥155 kW combined → minimum 5× AC-X1 units split unevenly across the two contra-rotating disks (4 units = 152 kW, a 2% shortfall; 5 units = 190 kW, real margin but asymmetric — 3 on one disk, 2 on the other, or a summing gearbox on each). Cost: 5×($5,400 + $4,000) = **$47,000**.
- **Electric-hardware-only total: $75,800** — already **more expensive** than the EMRAX-268×3 solution below ($51,000, §3), for a mechanically worse outcome (8 total machines vs. 3; multiple motors ganged per prop disk instead of EMRAX's clean 1-motor-per-disk direct-drive).
- **Mass: 8×(59 kg motor + ~4 kg controller) ≈ 504 kg** for the electric machines alone — more than 5× EMRAX's 91 kg for 3 units. Disqualifying on mass by itself.
- **Does not resolve DG-004:** paralleling adds current capacity, not voltage. The bus stays at Hyper9's native 144V regardless of unit count, so AER-68 §7.2's 667–1,076A-class current problem persists unchanged, just distributed across more parallel conductors.

**Paralleled Hyper9 is dominated by EMRAX 268×3 on cost, mass, and mechanical complexity, and does not fix the voltage-class finding that helped disqualify the original selection. Not advanced.**

### 1.4 A finding on Combo 1's own motor selection, surfaced by applying the same rigor

Combo 1 (the existing $130,900 fallback) pairs an EMRAX 268 generator with **2× EMRAX 228** propulsion motors. Pulling EMRAX 228's own datasheet-class continuous ratings (combined cooling): HV 55 kW, MV 64 kW, LV 75 kW. **Two EMRAX 228 motors combined, even at the best-case LV winding, deliver only 150 kW continuous — short of the 155 kW climb floor by 3%.** This is the same category of check that disqualified the HyPer9 AC-X1 pairing (AER-68 §7.1), just a much smaller shortfall. It does not retroactively disqualify Combo 1 (3% is not 51%, and Combo 1's own role in the catalog is "known-expensive proof the mission is achievable," not a budget candidate), but it means **Combo 1 as currently BOM'd has never actually been shown to clear the climb floor either** — worth a note back to the trade study, not a re-litigation here. It is also the direct reason this document uses EMRAX 268 (not 228) for the propulsion-motor role in the corrected Combo 3 below.

**Kill gate verdict: EMRAX 268 (MV winding, combined cooling) passes** — a real, manufacturer-published, non-EV-conversion-class continuous rating clears both the 96 kW generator floor (22% margin) and, in pairs, the 155 kW climb floor (51% margin), at a cost and mass that beats every other screened alternative. Proceeding to DG-004 and the corrected BOM below.

---

## 2. DG-004 Re-Derivation

**Proposed by PROPULSION; DG-004 is jointly owned with Systems and this proposal requires Systems' concurrence before the gate closes.**

EMRAX 268's MV winding is tested to 833 Vdc and reaches its full 117 kW continuous rating on an ~800V-class bus (datasheet: "voltage required for peak power: 830 Vdc" for the MV winding). This lands almost exactly inside DG-004's original "400V vs 800V" framing — recommend closing the gate at **~700–800V DC nominal**, not the 144V the disqualified HyPer9 selection actually ran at.

**Continuous bus current, real operating points (not full-rated points):**

| Point | Power | Bus current @ 800V | Per-machine current (of 220A rated) |
|---|---:|---:|---:|
| Cruise (generator) | 96 kW | ≈120 A | ≈180 A |
| Climb (2 motors combined) | 155 kW | ≈194 A | ≈146 A each |

This is **roughly 5–6× lower current than the disqualified HyPer9-at-144V case** (667–1,076A, AER-68 §7.2) for the same power — the direct, load-bearing benefit of picking a machine whose native voltage class actually matches an aviation/EV-industrial-grade bus.

**Switchgear availability — checked, unlike the HyPer9 case where none was found:** TE Connectivity's KILOVAC and HARTMAN DC contactor lines are rated to 500A continuous at up to 900 Vdc, built to AS9100 (aerospace/defense QMS), UL-recognized. A real, sourced, currently-manufactured product family exists at this voltage/current class. This does not close sourcing a specific part number and integration (that's a real follow-on task, §6), but it answers the acceptance-criteria question in the affirmative: **aviation-grade switchgear exists at the re-derived current level.**

**Controller/inverter — sourced, matched to the MV winding's voltage class:** UNITEK BAMOCAR-PG-D3-700/400 — a real, currently-documented (2022/V3 manual) industrial 3-phase servo amplifier: 12–700V DC input (833V absolute max), 200 A_RMS continuous / 135 kVA continuous, liquid-cooled, 8.5 kg, 355×230×135mm, EN61800/EN50178/ISO26262-referenced. This is the standard controller pairing for EMRAX MV/HV-winding motors in the existing EV-conversion and Formula Student market (real listings found: EMRAX 228 HV + BAMOCAR D3-400 pairings). At our actual per-machine continuous currents (146–180A, above), it runs comfortably inside its 200A rating.

**Named integration constraint, not a blocker:** the D3-700/400's own overvoltage cutoff is 780–800V — a real ceiling requiring the bus regulated with margin below EMRAX's 833V absolute test limit. Recommend targeting **~700V nominal** (inside DG-004's original envelope, inside both components' rated windows, with headroom on both sides) rather than pushing to the 830V edge. This is a bus-regulation design task for whoever architects the HV bus (Systems, jointly), not resolved further here.

**DG-004 disposition proposed by this pass:** ~700V DC nominal bus, current-tolerant to instrumented cruise/climb currents of ~120–200A per line. **Requires Systems' sign-off to close.**

---

## 3. Corrected BOM — EMRAX 268 (MV/CC) × 3 (1 generator + 2 motors)

Reuses AER-68's non-electric-machine line items unchanged (Hayabusa engine/turbo, belt reduction, battery, prop, contingency convention). Only the generator, motor, and controller lines are replaced.

| # | Item | Price (new) | Mass | Evidence |
|---|---|---:|---:|---|
| 1 | Hayabusa 1340cc + turbo kit + conversion | $8,000 | 105 kg | Same as AER-68 §1 rows 1-2 (unchanged, still FORUM/EXTRAP — no fresh sourcing done this pass) |
| 2 | Belt reduction, Hayabusa (~6,500 RPM) → generator input | $1,500 | 12 kg | **Ratio corrected this pass**: EMRAX 268's limiting speed is 4,500 RPM (MFR datasheet v1.6), not the trade study's earlier assumed 5,000 RPM — new ratio ≈1.44:1 (was ≈1.3:1). Still a single-stage, well-precedented reduction; mass/cost class unchanged. |
| 3 | Generator: EMRAX 268 MV + BAMOCAR D3-700/400 | $12,000 + $5,000 = $17,000 | 21.9 + 8.5 = 30.4 kg | MFR (motor price/mass, from AER-65/68's already-sourced EMRAX 268 figure — reused, not re-quoted); FORUM/VENDOR (controller price, $2,500 used / ~$5,000 new listings found this pass — updates AER-68's $4,000 generic-controller placeholder) |
| 4 | 2× Propulsion motors: EMRAX 268 MV + BAMOCAR D3-700/400 | 2×$17,000 = $34,000 | 2×30.4 = 60.8 kg | Same sourcing as row 3 |
| 5 | Battery + BMS (40 kWh LFP) | $10,000 | 320 kg | Unchanged from AER-68 §1 row 6 |
| 6 | HV wiring/switchgear/fusing/contactors | $7,000 (placeholder retained — not re-quoted to the lower current class this pass) | **~15 kg EXTRAP** (down from AER-68's 25 kg, reflecting the ~5-6× lower current; still flagged low-confidence pending a real BOM at the corrected current) | Kilovac/Hartman product family confirmed to exist (§2); specific part number and full BOS pricing not sourced this pass |
| 7 | Coaxial contra-rotating prop assembly | $8,000 | 40 kg | Unchanged from AER-68 §1 row 13 — **flagged: prop match needs AERO re-check**, EMRAX 268's 4,500 RPM/250 Nm continuous torque characteristic differs from the disqualified AC-X1's 3,300 RPM/110 Nm assumption §5 of AER-68 was built on |
| 8 | Contingency (10%) | $8,550 | — | Same convention as AER-68/trade study |
| | **Subtotal (pre-contingency)** | $85,500 | | |
| | **Total** | **≈$94,050** | | |
| | **Electric-hardware-only subtotal** | **$51,000** | | |

**88% over the $50k line.** Worse than Combo 3-as-specified's nominal 12% over — but Combo 3-as-specified doesn't actually clear the mission floor (AER-68 §7.1). This is the honest cost of a selection that does. It remains **substantially cheaper than Combo 1** (162% over, $130,900) and dramatically cheaper than the H3X path (≥200% over).

---

## 4. Cooling and Mass Delta vs. AER-68's Reusable Budget

### 4.1 Electric-side cooling — recomputed

AER-68 §4.2 sized the HyPer9 loop to its *rated-continuous* operating point (114 kW combined, 10.3 kW heat) because pushing it to the mission point wasn't a valid design point at all. Here, the mission point **is** inside the machines' rated envelope, so the honest sizing point is the actual mission draw: 96 kW (generator) + 155 kW (2 motors combined) = 251 kW combined, against EMRAX's 96% peak efficiency and a somewhat-conservative combined motor+BAMOCAR-inverter loss assumption of 6% (industrial IGBT inverter, not the exotic SiC/NASA-HLMC reference AER-68 used for its 9% figure — EMRAX's own datasheet efficiency map alone would support less):

- Heat at mission point: 251 kW × 6% ≈ **15 kW**
- Sizing a loop at the same NASA/TM-20205011477 specific-power basis (1.3–3 kW/kg) AER-68 used: mass ≈ 5–11.5 kg. Adopt **~10 kg** (AER-68's own convention of taking the fuller, more honest figure).

### 4.2 Battery and engine-side cooling — unchanged

Battery thermal loop (7 kg) and engine coolant/oil cooling (26+4=30 kg) are untouched — neither the battery chemistry/duty cycle nor the ICE side changed in this pass.

### 4.3 Cooling system mass rollup

| Item | AER-68 (HyPer9) | This pass (EMRAX 268) |
|---|---:|---:|
| Engine coolant radiator + oil cooler | 30 kg | 30 kg (unchanged) |
| Electric-side loop | 7 kg | **10 kg** |
| Battery thermal loop | 7 kg | 7 kg (unchanged) |
| **Total** | 44 kg | **47 kg** |

A small increase (+3 kg) despite the electric side now moving **2.2× more real power** (251 kW mission draw vs. 114 kW rated-continuous ceiling) — because EMRAX's 96% peak efficiency beats the assumption used for the disqualified machine, and because the mission point no longer requires pushing anything past its rated envelope.

### 4.4 Full mass statement

| Group | AER-68 (disqualified HyPer9 selection) | This pass (EMRAX 268 ×3) | Delta |
|---|---:|---:|---:|
| Engine + turbo kit | 105 kg | 105 kg | — |
| Belt reduction | 12 kg | 12 kg | — |
| Generator + controller | 63 kg | 30.4 kg | −32.6 kg |
| 2× propulsion motors + controllers | 125 kg | 60.8 kg | −64.2 kg |
| Battery pack | 320 kg | 320 kg | — |
| BMS | 4 kg | 4 kg | — |
| HV wiring/switchgear/fusing/contactors | 25 kg | ~15 kg | −10 kg |
| Cooling system | 44 kg | 47 kg | +3 kg |
| Coaxial contra-rotating prop | 40 kg | 40 kg | — |
| **Total installed powertrain mass** | **≈738 kg (1,627 lb)** | **≈634 kg (1,398 lb)** | **−104 kg (−14%)** |

**Against MTOW (2,600 lb / 1,179 kg): the corrected powertrain is ≈53.8% of MTOW**, down from AER-68's 62.6% — still well outside the 20-30% typical of a GA piston single, and still, per AER-68 §6, worth a formal reconciliation with Structures/mass-properties rather than a wait-and-see, but a real, non-trivial improvement driven entirely by EMRAX's higher power density at its *real* rated-continuous point.

---

## 5. Verdict

**The kill gate is passed, not stopped.** EMRAX 268 (MV winding, combined cooling) is a real, sourced, manufacturer-published-continuous-rated machine class that clears both the 96 kW generator floor (22% margin) and the 155 kW combined climb floor (51% margin using 2 units), at $94,050 total / $51,000 electric-hardware-only (88% over the $50k line) and ≈634 kg installed (14% lighter than the disqualified selection). H3X and paralleled-Hyper9 were both screened per the issue's mandate and both fail — H3X on unpriced-but-clearly->200%-over cost, paralleled Hyper9 on cost ($75,800 vs. $51,000), mass (504 kg vs. 91 kg for the electric machines alone), mechanical complexity, and failure to resolve the voltage-class problem at all.

**DG-004 is proposed closed at ~700V DC nominal**, current-rated for ~120-200A continuous per line — a real, sourced switchgear class exists at this level (TE Connectivity Kilovac/Hartman), unlike the disqualified selection's 667-1,076A/144V case where none did. **Requires Systems' concurrence to actually close** — this document proposes, it does not unilaterally decide a jointly-owned gate.

**What this document does not do, per the issue's explicit scope:** it does not rank-score this corrected selection against Combo 1 as the working baseline. That call — and any airframe-facing retarget — waits on Bill's disposition on AER-56 (confirmation `f6c71029`, pending). What's here is the input that disposition needs: a real, priced, weighed, thermally-sized answer to "does a corrected Combo 3 exist at a defensible cost and mass," so that whichever way Bill resolves AER-56, the next step doesn't start from zero.

---

## 6. Open Items

1. **Rank-scoring against Combo 1** — explicitly gated on AER-56 (confirmation `f6c71029`). Not done here.
2. **Systems concurrence on DG-004** — this document proposes ~700V nominal; Systems co-owns the gate and needs to sign off, particularly on bus regulation margin against the BAMOCAR controller's 780-800V overvoltage cutoff and EMRAX's 833V absolute test ceiling.
3. **HV wiring/switchgear real BOM** — §3 row 6's $7,000/~15kg figures are still placeholders carried forward, not re-quoted to the corrected current class. A real part-number-level BOM at ~120-200A/700V is a bounded Systems/PROPULSION joint task, not a re-opened kill gate question.
4. **Prop match re-check with AERO** — EMRAX 268's 4,500 RPM/250 Nm continuous characteristic is a materially different operating point than the disqualified AC-X1's 3,300 RPM/110 Nm assumption AER-68 §5 was built on. The actuator-disk sizing and tip-Mach check need re-running against the new motor, not assumed to carry over.
5. **Combo 1's own motor-side shortfall (§1.4)** — 2× EMRAX 228 combined (150 kW best case) is 3% short of the 155 kW climb floor. Small, not urgent, but should be corrected in the trade study record rather than left standing uncorrected now that it's been found.
6. **BAMOCAR D3-700/400 real procurement path** — pricing in §3 rests on used-market forum listings (~$2,500) and one non-current retail citation (~$5,000); a fresh vendor quote would tighten this before any purchase commitment.
7. **Live geometry access** — unchanged from AER-68 §9 item 4; still no Onshape/CAD connection this pass. Boom/pod clearance for the prop and radiator/duct siting remain unverified against real geometry.
8. **EASA-certification claim on EMRAX 268 (§1.1)** — cited from EMRAX's own marketing page, not independently verified. Not load-bearing for this project's Experimental Amateur-Built basis, but worth a citation check if it ever becomes relevant to a safety-case argument.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1 — 2026-08-10. Kill-gate screening of EMRAX 268, H3X HPDM-180/250, and paralleled Hyper9 as corrected electric-machine candidates for Combo 3 (§1); DG-004 bus-voltage re-derivation to ~700V nominal, proposed pending Systems concurrence (§2); corrected sourced BOM (§3); cooling and mass deltas against the reusable AER-68 budget (§4). Verdict: kill gate passed on EMRAX 268 (§5). Rank-scoring against Combo 1 explicitly deferred pending Bill's disposition on AER-56.*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
