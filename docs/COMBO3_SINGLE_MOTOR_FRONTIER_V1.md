# Combo 3 — Price-vs-Capability Frontier: Corrected Machine × Single/Twin Motor Lever (AER-73)

**Status:** Paper-first trade study. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment. No endurance/runtime validation performed — per Bill's 2026-08-11 direction, the goal here is closing the number on paper.
**Date:** 2026-08-11 (V1), corrected 2026-08-11 (V2 — see §0.1)
**Owner:** PROPULSION
**Origin:** [AER-73](/AER/issues/AER-73), child of [AER-56](/AER/issues/AER-56). Supersedes the pass/fail framing in `COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md` (PR #16) per Bill's 2026-08-11 requirement update (R1′) and adds the single-propulsion-motor lever (R4).

**Read the verdict first if you're short on time: §4.**

---

## 0. What changed since PR #16, and why this document exists

Two requirement updates landed on AER-56 on 2026-08-11 and were routed to this issue:

- **R1′ — the $50k number, sharpened and reframed.** $50k now buys the **entire drivetrain excluding the propeller**: prime mover + generator(s) + propulsion motor(s) + battery, installed, single build. This *tightens* the old R1 (which excluded only airframe/install labor, and implicitly included the prop) and *reframes* the deliverable: **it is a price-vs-capability frontier, not a pass/fail gate.** If nothing clears $50k, the job is to report what the achievable knee of the curve buys.
- **R4 — a single propulsion motor is now admissible**, pending SAFETY's ruling on the total-loss-of-thrust/forced-landing case ([AER-81](/AER/issues/AER-81), open, not yet answered as of this pass). This removes the twin-motor *mandate* it does not remove the twin-motor *option* — both are scored below.

**What is not reopened here:** the 1G+1B+xM series-hybrid architecture, the turbo-Hayabusa prime mover, the EMRAX 268 generator selection (passed its kill gate in PR #16 — 117 kW continuous MV/CC clears the 96 kW cruise floor with 22% margin), and the ~700V DC DG-004 bus proposal. Those stand. What's new here is: (1) recasting cost as a two-column frontier instead of one pass/fail number, and (2) adding single-motor propulsion candidates alongside the twin-268 baseline.

### 0.1 V2 correction — two things changed after V1 posted

1. **SAFETY ruled on AER-81 (2026-08-11).** Headline: twin-motor mandate lifted, but a *bare* single winding-set/single-inverter motor is **not admissible**. Redundancy must come from (a) a dual-wound motor with two independent winding sets, each on its own independent inverter channel, independent gate-drive/control power, physically/thermally separated, or (b) two physically separate motor+inverter units — see full requirements (R1–R5) applied package-by-package in §3 and §4 below.
2. **Self-caught datasheet error, found while re-verifying Package B against the SAFETY ruling.** Package B's V1 text cited "162 kW continuous S1" for the EMRAX 348 MV/CC, sourced to "datasheet v1.5." Re-pulled directly from EMRAX's current **v1.6 datasheet (June 2025)** and parsed against its positioned table cells (not just flattened text, to avoid column misalignment) — the actual MV/CC continuous power S1 is **145 kW**, not 162 kW. Independently cross-checked against EMRAX's own product-page summary spec ("PEAK | CONTINUOUS POWER: 340 kW | 145 kW"), which matches. The EMRAX 268 baseline figure (117 kW continuous MV/CC) was re-checked the same way against its own v1.6 datasheet and is confirmed correct — no change there. **Consequence: Package B fails the 155 kW climb floor by 6.5% at full rated power, before any redundancy tax — it is disqualified on capability alone, independent of AER-81.** See §3 Package B and §4.

---

## 1. Method

**Cost columns.** Two columns per package, both installed, single build, drivetrain only (prime mover + generator + propulsion motor(s) + battery — **prop excluded per R1′**):

- **All-new:** every line item at new/retail pricing where a new-market price exists.
- **Realistic used/salvage:** electric machines and controllers at sourced used-market prices (R2, confirmed by Bill: used/salvage is fair inside the number). The ICE line is used-sourced in *both* columns — no viable new-crate Hayabusa price exists (motorcycle engines aren't sold as bare crate units at this budget tier), so both columns carry the same AER-57-sourced used figure. This is flagged, not hidden.

**Sourcing tags**, carried forward from prior docs in this series: **MFR** (manufacturer datasheet), **FORUM/VENDOR** (marketplace or reseller listing), **EXTRAP** (scaled estimate, no direct quote — flagged explicitly, never presented as sourced).

**Mass** is reported installed, inclusive of the propeller assembly (Structures/CG needs total installed mass regardless of how the $50k line is drawn — the cost and mass boundaries are not the same boundary).

**Capability** is reported against the standing mission floors: 96 kW continuous cruise (generator electrical floor), 155 kW climb bus demand (max/1,200 fpm climb, electrical), and the 40 kWh/30-min/60 kW emergency battery reserve (unchanged — not re-examined this pass).

---

## 2. Common line items (all packages)

| Item | All-new | Used/salvage | Evidence |
|---|---:|---:|---|
| Hayabusa 1340cc + turbo kit + conversion | $8,000 | $8,000 (same) | FORUM — AER-57 sourcing (~$4,500 used engine + ~$4,000 conversion). **No new-crate price exists; both columns are used-sourced.** |
| Belt reduction (Hayabusa → generator input, ~1.44:1) | $1,500 | $1,500 | Unchanged from PR #16 §3 row 2 |
| Battery + BMS, 40 kWh LFP | $10,000 | $10,000 | Unchanged from AER-68/PR#16. **Salvage lever exists but is not separated here:** AER-65 (v2 trade study) found a salvage LFP pack nets ~$1,540 after ~$4,500 of unsourced BMS-integration placeholders, and AER-67 (SAFETY) rules a salvage pack may count toward *cost* but may not be *safety-credited* as the sized reserve until a named aftermarket BMS is bench-validated. Carrying that finding forward unchanged rather than re-litigating it — this line stays flat in both columns until AER-67's BMS-validation gate clears. |
| HV wiring/switchgear/fusing/contactors | $7,000 | $7,000 | EXTRAP placeholder, not re-quoted to the corrected current class this pass either — open item #3 from PR #16 still stands |
| Generator: 1× EMRAX 268 MV (CC) + BAMOCAR D3-700/400 | $17,000 ($12,000 + $5,000) | $8,500 ($6,000 + $2,500) | MFR (motor, reused from AER-65/68); **used motor price this pass**: sourced comps range $2,500–$8,000 (Endless Sphere surplus listing £2,500 ≈ $3,200; eBay used $8,000; DIYElectricCar bundled system $7,350 incl. inverter) — midpoint $6,000 used as the realistic figure, motor-only. Controller used price ($2,500) carried from PR #16 §3 row 3 (forum listing, not re-quoted). |

**Tesla-drive-unit note, carried forward per Bill's flag — not re-investigated:** AER-65 tested the Tesla-drive-unit-as-generator hypothesis directly and rejected it as a cost lever; the mandatory ~$2,699 VCU eats the salvage saving. Not revisited here.

---

## 3. Propulsion-motor packages — the frontier

### Package A — Twin EMRAX 268 (current AER-73 baseline, unchanged; 2-motor coaxial contra-rotating prop)

2× (EMRAX 268 MV/CC + BAMOCAR D3-700/400): **$34,000 new / $17,000 used** (2 × the generator-side unit cost above).

| | All-new | Used/salvage |
|---|---:|---:|
| Electric-hardware-only (gen + 2 motors) | $51,000 | $25,500 |
| Drivetrain subtotal (excl. prop) | $77,500 | $52,000 |
| **+10% contingency → Total (excl. prop)** | **$85,250 (71% over)** | **$57,200 (14% over)** |

**Capability:** generator 117 kW continuous (22% margin/96 kW); climb 2×117 kW = 234 kW combined (51% margin/155 kW). Each motor carries only ~50% load during shared climb (77.5 kW of 117 kW rated) — real headroom, not a paper margin. **Motor-out redundancy:** losing one motor leaves 117 kW available, which clears the 96 kW cruise floor outright — the aircraft can sustain cruise-equivalent thrust on the surviving motor. Reserve: 40 kWh/30 min/60 kW, unchanged.
**Mass (installed, incl. prop):** ≈634 kg — unchanged from PR #16 §4.4 (architecture untouched).
**Torque/gyroscopic:** coaxial contra-rotating — cancels, per PR #16/AER-69's existing finding.

**AER-81 safety-column read (R1–R5):**
- **R1 — satisfied via (b), no new technology.** STRUCTURES's live-CAD pull (AER-69) confirms this is already two physically separate motor+inverter units (two conventional EMRAX 268 + BAMOCAR pairs on a coaxial contra-rotating prop), not a shared-stator arrangement — the clean path SAFETY named. Nothing to add here.
- **R3 — the "motor-out" redundancy above is a real partial capability, not a full limp-home.** The surviving motor clears the 96 kW *cruise* floor, not the 155 kW *climb* floor — a motor-out event mid-climb loses climb capability and continues at cruise-equivalent thrust only. State this plainly rather than reading "motor-out safe" as "unaffected."
- **R5 — common-cause not yet cleared.** Both motor+inverter units currently sit on the same ~700V DG-004 bus segment, the same battery/generator chain, and (per PR #16's cooling budget) an unconfirmed coolant-loop split. R1(b)'s protection is only as good as these being genuinely independent — **open item, not yet confirmed with Systems/Structures** (see §5).
- **R2/R4 (safety numbering) — unchanged from the standing baseline.** No FIT-rate data sourced for the EMRAX 268 + BAMOCAR class this pass (open item). The single-generator, single-battery, unsegmented-bus SPOFs (AER-62/AER-74) are untouched by this package choice — Package A's motor-level redundancy does not extend to them.

### Package B — Single EMRAX 348 — **DISQUALIFIED on capability, corrected this pass (see §0.1)**

**EMRAX 348 MV/CC** (MFR datasheet **v1.6, re-pulled and position-parsed this pass — supersedes V1's v1.5 figure**): **145 kW continuous S1** (not 162 kW), 425 Nm continuous torque, 230 A_RMS continuous, 43.5 kg, 830V peak-power voltage (same MV-winding voltage-ceiling logic as the 268 — HV winding actually delivers *less* continuous power at this bus voltage, same non-obvious finding as PR #16 §1.1). Independently corroborated against EMRAX's own product-page summary spec (340 kW peak / 145 kW continuous). The 268 baseline (117 kW) was re-checked the same way against its v1.6 datasheet and holds.

**Climb: 145 kW vs. the 155 kW floor — 6.5% SHORT, not a 4.5% margin over.** V1's headline number was wrong. This package **fails the mission floor at full rated power, before any redundancy tax and independent of AER-81** — it does not clear the gate to even reach the safety-column question below. No published EMRAX 348 winding/cooling combination (including the custom LV+43%/LV+100%/HV+42% variants on the same v1.6 datasheet) reaches 155 kW continuous. Carrying it in the frontier below only to show why it is out.

**Controller/redundancy note, also corrected:** V1's rationale for 2× BAMOCAR D3-700/400 (current-sharing, since 230 A_RMS exceeds a single unit's 200 A rating) is still sound on its own terms. But **both the 268 and 348 v1.6 datasheets state plainly: "All values given are for a standard 3 phase UVW version, please consult EMRAX on 2x UVW values"** — EMRAX does not publish performance numbers, nor confirm electrical/thermal isolation, for the 2×UVW configuration. Whether 2×UVW gives genuinely fault-isolated, independent winding sets (satisfying AER-81's R1a) or is a current-splitting reconfiguration of one winding with no fault containment is **not established from public data** — a direct EMRAX consult would be needed before this could ever be used to satisfy R1, on top of the capability failure above.

| Item | All-new | Used/salvage |
|---|---:|---:|
| EMRAX 348 MV/CC | $18,000 **EXTRAP** (range $16,000–$22,000, scaled from the 268's $12,000 by both continuous-power ratio and mass ratio — no vendor quote; midpoint used) | $9,000 **EXTRAP** (no 348 used listing found in this pass — the 268's ~50% used/new ratio applied as a placeholder, flagged low-confidence) |
| 2× BAMOCAR D3-700/400 | $10,000 | $5,000 |
| **Motor package total** | **$28,000** | **$14,000** |
| Electric-hardware-only (gen + motor) | $45,000 | $22,500 |
| Drivetrain subtotal (excl. prop) | $71,500 | $46,000 |
| **+10% contingency → Total (excl. prop)** | **$78,650 (57% over)** | **$50,600 (1.2% over)** |

Cost table left as-is for reference (the EXTRAP price inputs are unaffected by the kW correction) — **but the cost is moot: this package does not clear the climb floor regardless of price, and is dropped from the recommendation in §4.**

**Mass (installed, incl. prop, motor+controllers only shown here):** 43.5 kg (motor) + 17 kg (2× controller) = 60.5 kg — essentially flat vs. Package A's 60.8 kg; not the deciding factor here.
**Torque/gyroscopic — does NOT cancel.** A single prop disk has a real, uncancelled torque reaction and a real gyroscopic moment in maneuvering flight — moot for this package now, noted for completeness only.

### Package C — Single EMRAX 268 (cheapest single-motor floor; capability-reduced)

Reuses the generator-side unit (§2) in the propulsion role: **1× EMRAX 268 MV/CC + 1× BAMOCAR D3-700/400.**

**Does not clear the 155 kW max-climb (1,200 fpm) floor — 117 kW is 25% short.** Included specifically because Bill asked "if we can't hit $50k, what CAN we build, and what are the tradeoffs" — this is the answer at the cheap end of the curve, with the tradeoff stated plainly rather than buried.

**Controller headroom note:** the 268's 220 A_RMS continuous current is slightly above the single BAMOCAR D3-700/400's 200 A rating (9% over) — a real, small integration gap. Either a mild current/thermal derate on the motor (still exceeds the reduced-climb target below) or the 2-controller 2×UVW approach (Package B's fix, at extra cost) resolves it. Priced here with the single-controller (cheaper, tighter-margin) configuration.

| | All-new | Used/salvage |
|---|---:|---:|
| Electric-hardware-only (gen + motor, symmetric) | $34,000 | $17,000 |
| Drivetrain subtotal (excl. prop) | $60,500 | $43,500 |
| **+10% contingency → Total (excl. prop)** | **$66,550 (33% over)** | **$47,850 (UNDER $50k by 4.3%)** |

**Capability:** generator unchanged (117 kW/22% margin). Climb: 117 kW vs. 155 kW max-climb floor — **25% short, does not close.** Against the *reduced* 700 fpm/~120 kW no-battery-climb target from the standing power-budget table: 117 kW is ~2.5% short of that figure too, though that figure is defined as an ICE-side target, not a clean motor-side comparison — flagged, not asserted as a pass. **This package is only viable if AERO/Elon relaxes the max-climb-rate requirement — a requirements call, not an engineering one, and not made here.**
**Mass (motor+controller only):** 21.9 + 8.5 = 30.4 kg — a **real** ~30 kg lighter than Packages A/B, because this is genuinely less machine, not repackaged capability.

**AER-81 safety-column read (R1–R3):** **as priced above, this is exactly the bare single winding-set/single-inverter configuration SAFETY ruled inadmissible** — §3 above explicitly chose the single-BAMOCAR-D3-700/400 config over the 2-controller fix "at extra cost." Making it R1-compliant means either the same unsourced 2×UVW path Package B's correction flagged as unverified (see §3 Package B), or a second physically separate motor+inverter unit — which erodes or eliminates this package's only selling point (being the cheapest floor) and still does not close the 25%-short climb gap. **This package does not clear R1 as currently specified, on top of already failing the climb requirement.** R3: no limp-home applies as written — a motor-out event here is total loss of thrust, full stop.

---

## 4. Verdict — the frontier, and the honest knee of the curve

**Both open gates from V1 have since resolved, and both cut the same direction — against B and C, not against A.** AER-81 ruled (2026-08-11): bare single motor/inverter is inadmissible. And the corrected EMRAX 348 datasheet figure (§0.1, §3) independently disqualifies Package B on capability, before the safety ruling is even applied.

| Package | Motors | Cost (new) | Cost (used) | Climb margin | AER-81 (R1) status | Gates |
|---|---|---:|---:|---:|---|---|
| A — Twin EMRAX 268 | 2 | $85,250 (71% over) | **$57,200 (14% over)** | 51% | **Satisfies R1(b)** — two physically separate motor+inverter units, per AER-69 | R5 common-cause (bus/battery/coolant sharing) unconfirmed; Systems concurrence on DG-004 (unchanged, pending) |
| B — Single EMRAX 348 | 1 | $78,650 (57% over) | $50,600 (1.2% over) | **−6.5% (fails climb — corrected, was reported as +4.5%)** | Not reached — fails on capability first | **Disqualified this pass, independent of AER-81.** 348 price still EXTRAP; 2×UVW redundancy path unverified with vendor even if capability were fixed |
| C — Single EMRAX 268 | 1 | $66,550 (33% over) | $47,850 (under $50k) | **−25% (fails max climb)** | **Fails R1** as priced (bare single winding/inverter) | Fails climb *and* R1; would need AERO/Elon climb-rate relaxation *and* an R1 fix that erodes its cost advantage |
| Combo 1 (reference, unchanged) | 2 (EMRAX 228) | $130,900 (162% over*) | — not re-scored this pass | −3% (own shortfall, PR #16 §1.4) | Motor-out (both EMRAX) | *Old R1′ figure, includes prop; not re-split this pass |

**The frontier has effectively collapsed to one candidate.** Package A is the only package that clears the climb floor and satisfies AER-81's R1 without relying on unverified vendor claims. Packages B and C are kept in the document (not deleted) so the "what did we rule out and why" record is honest and auditable, per V1's own framing — but neither survives to the recommendation below.

**What this actually says to Bill's question ("if we can't make that price point, what CAN we make, and what are the tradeoffs"):**

- **The used/salvage lever (R2) is still the single biggest lever in this frontier** — Package A used ($57,200) beats either single-motor package's *new* pricing, confirming AER-65's original finding: the saving is in used electric hardware, not architecture.
- **The single-motor lever (R4) did not pay off as scored in V1.** Package B's apparent 12% further saving over Package A used was built on a wrong manufacturer number; corrected, it doesn't clear the mission floor at any price. Package C never cleared the floor and, applied against AER-81, also can't clear the safety bar without giving up its price advantage. Neither is a live option right now — not "pending a gate," genuinely disqualified.
- **Recommendation, offered not decided: Package A (used/salvage), $57,200, 14% over $50k.** It is the only point on this frontier that clears climb, satisfies AER-81's R1 without new unresolved technology, and beats Combo 1 by a wide margin (162% over). Remaining opens before it's adoptable: Systems concurrence on DG-004, and naming/closing the R5 common-cause items (§5).
- If Bill wants to keep pushing toward $50k, the honest next levers are **further used/salvage sourcing on Package A's own line items** (motor/controller prices here are already midpoint estimates with a real spread — see §2 evidence column) or a **fresh single-motor candidate with a real, vendor-confirmed R1-compliant redundant-winding option** — not a re-scoring of B or C as currently specified.

---

## 5. Open items

1. **R5 common-cause on Package A — needs Systems/Structures confirmation.** Name explicitly whether the two motor+inverter channels share a bus segment, LV control supply, coolant loop, connector, or firmware. Not confirmed either way this pass — this is what stands between "R1(b) satisfied on paper" and "R1(b) satisfied in the installed system."
2. **Systems concurrence on DG-004** — unchanged open item from PR #16, still pending.
3. **R2 (safety numbering) — FIT-rate/field-reliability sourcing for the EMRAX 268 + BAMOCAR class**, split windings vs. power electronics, per AER-81's requirement. Not sourced this pass.
4. **Prop match, Package A** — PR #16's open item (EMRAX 268's 4,500 RPM/250 Nm characteristic vs. the old AC-X1 assumption) still applies. Successor to AER-71, AERO consult needed.
5. **HV wiring real BOM at the corrected current class** — unchanged open item from PR #16.
6. **Combo 1 not re-split to R1′** — its $130,900/162%-over figure still includes the prop under the old R1 definition; not re-computed against the new prop-excluded boundary this pass. Directionally the delta is small relative to the size of the gap.
7. **If B or C is to be revisited:** would need (a) for B, a real vendor consult with EMRAX confirming 2×UVW winding-set electrical/thermal independence and its actual continuous-power rating in that configuration (not published), and separately AERO/Elon relaxing the climb-rate requirement by >6.5%; (b) for C, the same climb-rate relaxation (>25%) plus an R1-compliant redundancy fix, which would need to be priced fresh since it was not costed in this pass. Neither is in progress — flagged as the reopening condition, not started.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1 — 2026-08-11. Price-vs-capability frontier across three propulsion-motor packages (twin EMRAX 268 / single EMRAX 348 / single EMRAX 268) × two cost bases (all-new / realistic used-salvage), responding to Bill's 2026-08-11 R1′ (frontier, not pass/fail) and R4 (single-motor admissibility pending SAFETY) requirement updates on AER-56.*
*Version 2 — 2026-08-11. Applies AER-81's SAFETY ruling (R1–R5) package-by-package; corrects the EMRAX 348 continuous-power figure from an unverified 162 kW to the manufacturer's published v1.6 figure of 145 kW, which disqualifies Package B on capability independent of AER-81. Frontier recommendation narrows to Package A (used/salvage, $57,200, 14% over $50k).*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
