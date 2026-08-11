# Combo 3 — Price-vs-Capability Frontier: Corrected Machine × Single/Twin Motor Lever (AER-73)

**Status:** Paper-first trade study. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment. No endurance/runtime validation performed — per Bill's 2026-08-11 direction, the goal here is closing the number on paper.
**Date:** 2026-08-11
**Owner:** PROPULSION
**Origin:** [AER-73](/AER/issues/AER-73), child of [AER-56](/AER/issues/AER-56). Supersedes the pass/fail framing in `COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md` (PR #16) per Bill's 2026-08-11 requirement update (R1′) and adds the single-propulsion-motor lever (R4).

**Read the verdict first if you're short on time: §4.**

---

## 0. What changed since PR #16, and why this document exists

Two requirement updates landed on AER-56 on 2026-08-11 and were routed to this issue:

- **R1′ — the $50k number, sharpened and reframed.** $50k now buys the **entire drivetrain excluding the propeller**: prime mover + generator(s) + propulsion motor(s) + battery, installed, single build. This *tightens* the old R1 (which excluded only airframe/install labor, and implicitly included the prop) and *reframes* the deliverable: **it is a price-vs-capability frontier, not a pass/fail gate.** If nothing clears $50k, the job is to report what the achievable knee of the curve buys.
- **R4 — a single propulsion motor is now admissible**, pending SAFETY's ruling on the total-loss-of-thrust/forced-landing case ([AER-81](/AER/issues/AER-81), open, not yet answered as of this pass). This removes the twin-motor *mandate* it does not remove the twin-motor *option* — both are scored below.

**What is not reopened here:** the 1G+1B+xM series-hybrid architecture, the turbo-Hayabusa prime mover, the EMRAX 268 generator selection (passed its kill gate in PR #16 — 117 kW continuous MV/CC clears the 96 kW cruise floor with 22% margin), and the ~700V DC DG-004 bus proposal. Those stand. What's new here is: (1) recasting cost as a two-column frontier instead of one pass/fail number, and (2) adding single-motor propulsion candidates alongside the twin-268 baseline.

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

### Package B — Single EMRAX 348 (R4 lever; single conventional prop)

**EMRAX 348 MV/CC** (MFR datasheet v1.5, pulled fresh this pass): 162 kW continuous S1, 425 Nm continuous torque, 230 A_RMS continuous, 43.5 kg, 830V peak-power voltage (same MV-winding voltage-ceiling logic as the 268 — HV winding actually delivers *less* continuous power at this bus voltage, same non-obvious finding as PR #16 §1.1). Clears the 155 kW climb floor **alone, with only a 4.5% margin** — thin, and worth stating plainly against Package A's 51%.

**Controller:** the 348's continuous current (230 A_RMS) exceeds the BAMOCAR D3-700/400's single-unit rating (200 A_RMS) — the only 700V-class BAMOCAR variant with public documentation found. Rather than invent an unsourced bigger controller, this uses EMRAX's own supported **2×UVW parallel-winding configuration** (documented on the 348 datasheet) with **2× BAMOCAR D3-700/400** — the same already-sourced/qualified controller used on the generator, each carrying ~115 A (well inside its 200 A rating). This reuses a known part instead of extrapolating a new one, at the cost of not saving a controller.

| Item | All-new | Used/salvage |
|---|---:|---:|
| EMRAX 348 MV/CC | $18,000 **EXTRAP** (range $16,000–$22,000, scaled from the 268's $12,000 by both continuous-power ratio [$16,600] and mass ratio [$23,800] — no vendor quote; midpoint used) | $9,000 **EXTRAP** (no 348 used listing found in this pass — the 268's ~50% used/new ratio applied as a placeholder, flagged low-confidence) |
| 2× BAMOCAR D3-700/400 | $10,000 | $5,000 |
| **Motor package total** | **$28,000** | **$14,000** |
| Electric-hardware-only (gen + motor) | $45,000 | $22,500 |
| Drivetrain subtotal (excl. prop) | $71,500 | $46,000 |
| **+10% contingency → Total (excl. prop)** | **$78,650 (57% over)** | **$50,600 (1.2% over)** |

**Capability:** generator unchanged (117 kW/22% margin). Climb: 162 kW continuous vs. 155 kW floor — **4.5% margin, a real pass under S1 continuous duty, but far thinner than Package A's 51%.** **No motor-out redundancy** — this is a single point of failure for 100% of thrust, the exact case [AER-81](/AER/issues/AER-81) (open, unanswered) was chartered to rule on. **This package is not adoptable until AER-81 closes.** Reserve unchanged.
**Mass (installed, incl. prop, motor+controllers only shown here):** 43.5 kg (motor) + 17 kg (2× controller) = 60.5 kg — **essentially flat vs. Package A's 60.8 kg.** Non-obvious finding: consolidating into one bigger motor is **not** a meaningful mass lever by itself, because axial-flux motor mass scales close to linearly with continuous power/torque — you need the same total capability either way. The real mass (and cost) win from single-motor is the **simpler single conventional prop instead of the coaxial contra-rotating assembly**, and a simpler single-nacelle mount — neither is priced/weighed here (no sourced delta for a conventional vs. contra-rotating prop of this class was found this pass); flagged as an open item for AERO/STRUCTURES, likely worth a few kg and a few hundred to ~$2–4k, not a large lever, EXTRAP-direction only.
**Torque/gyroscopic — does NOT cancel.** A single prop disk has a real, uncancelled torque reaction and a real gyroscopic moment in maneuvering flight. This is a new structural/handling contract item that did not exist under Package A's contra-rotating arrangement — **flagged to STRUCTURES and AERO now**, not resolved here.

### Package C — Single EMRAX 268 (cheapest single-motor floor; capability-reduced)

Reuses the generator-side unit (§2) in the propulsion role: **1× EMRAX 268 MV/CC + 1× BAMOCAR D3-700/400.**

**Does not clear the 155 kW max-climb (1,200 fpm) floor — 117 kW is 25% short.** Included specifically because Bill asked "if we can't hit $50k, what CAN we build, and what are the tradeoffs" — this is the answer at the cheap end of the curve, with the tradeoff stated plainly rather than buried.

**Controller headroom note:** the 268's 220 A_RMS continuous current is slightly above the single BAMOCAR D3-700/400's 200 A rating (9% over) — a real, small integration gap. Either a mild current/thermal derate on the motor (still exceeds the reduced-climb target below) or the 2-controller 2×UVW approach (Package B's fix, at extra cost) resolves it. Priced here with the single-controller (cheaper, tighter-margin) configuration.

| | All-new | Used/salvage |
|---|---:|---:|
| Electric-hardware-only (gen + motor, symmetric) | $34,000 | $17,000 |
| Drivetrain subtotal (excl. prop) | $60,500 | $43,500 |
| **+10% contingency → Total (excl. prop)** | **$66,550 (33% over)** | **$47,850 (UNDER $50k by 4.3%)** |

**Capability:** generator unchanged (117 kW/22% margin). Climb: 117 kW vs. 155 kW max-climb floor — **25% short, does not close.** Against the *reduced* 700 fpm/~120 kW no-battery-climb target from the standing power-budget table: 117 kW is ~2.5% short of that figure too, though that figure is defined as an ICE-side target, not a clean motor-side comparison — flagged, not asserted as a pass. **This package is only viable if AERO/Elon relaxes the max-climb-rate requirement — a requirements call, not an engineering one, and not made here.** Same single-point-of-failure exposure as Package B, pending AER-81.
**Mass (motor+controller only):** 21.9 + 8.5 = 30.4 kg — a **real** ~30 kg lighter than Packages A/B, because this is genuinely less machine, not repackaged capability.

---

## 4. Verdict — the frontier, and the honest knee of the curve

| Package | Motors | Cost (new) | Cost (used) | Climb margin | Redundancy | Gates |
|---|---|---:|---:|---:|---|---|
| A — Twin EMRAX 268 | 2 | $85,250 (71% over) | **$57,200 (14% over)** | 51% | Motor-out safe (survivor clears cruise) | Systems concurrence on DG-004 (unchanged, pending) |
| B — Single EMRAX 348 | 1 | $78,650 (57% over) | **$50,600 (1.2% over)** | 4.5% | None — total-loss-of-thrust | **AER-81 (SAFETY, open)**; 348 price is EXTRAP |
| C — Single EMRAX 268 | 1 | $66,550 (33% over) | **$47,850 (under $50k)** | **−25% (fails max climb)** | None — total-loss-of-thrust | **AER-81 (SAFETY, open)**; requires AERO/Elon to relax climb-rate requirement |
| Combo 1 (reference, unchanged) | 2 (EMRAX 228) | $130,900 (162% over*) | — not re-scored this pass | −3% (own shortfall, PR #16 §1.4) | Motor-out (both EMRAX) | *Old R1 figure, includes prop; not re-split to R1′ this pass |

**No package clears $50k on new parts.** On used/salvage, one package clears it outright (C, capability-reduced) and one comes within 1.2% (B, resting on unsourced pricing). Nothing clears it with both full climb margin and full redundancy — that combination (Package A) lands at $57,200, 14% over.

**What this actually says to Bill's question ("if we can't make that price point, what CAN we make, and what are the tradeoffs"):**

- **The single biggest lever in this whole frontier is used/salvage electric hardware, not the single-motor architecture change.** Package A used ($57,200) is already closer to $50k than Package B new ($78,650) or Package C new ($66,550) — the R2 used/salvage lever (confirmed 2026-08-09) outweighs the R4 single-motor lever by a wide margin. This matches AER-65's own finding on the disqualified selection: the saving came from used electric hardware, not the engine, not a Tesla drive unit.
- **The single-motor lever (R4) buys real money (Package A used → B used: $57,200 → $50,600, a further $6,600/12%) but it is not free.** It costs the twin-motor redundancy the architecture currently has, thins the climb margin from 51% to 4.5%, opens a new uncancelled-torque/gyroscopic item for Structures and Aero, and rests one input (348 pricing) on an unsourced extrapolation rather than a real quote. And it cannot be adopted at all until AER-81 rules on the total-loss-of-thrust case it creates.
- **Package C is the honest floor of the curve.** It is the only package under $50k on used pricing, and it buys that by giving up 25% of climb capability outright — not a rounding error, a real requirement breach that needs an explicit relax-the-climb-rate decision from AERO/Elon, not a quiet substitution.
- **Recommendation, offered not decided:** if the frontier is being used to pick a working baseline now, **Package A (used/salvage) is the only point on this curve that keeps both the climb margin and the motor-out safety case intact**, at 14% over — a materially better position than Combo 1's 162% over, with no open safety gate. Packages B and C are real, priced options for further squeezing the number, but both are gated on AER-81 and (for C) on a requirements relaxation neither PROPULSION nor SAFETY owns.

---

## 5. Open items

1. **AER-81 (SAFETY) — total-loss-of-thrust ruling.** Packages B and C cannot be adopted until this closes. Not owned here.
2. **Systems concurrence on DG-004** — unchanged open item from PR #16, still pending, applies to all three packages (all run the same ~700V bus).
3. **EMRAX 348 real vendor quote** — §3 Package B's motor and used-price figures are EXTRAP. A real quote would tighten or invalidate the "1.2% over" headline number.
4. **Prop match, all packages** — PR #16's open item (EMRAX 268's 4,500 RPM/250 Nm characteristic vs. the old AC-X1 assumption) still applies to Package A. Packages B/C need a **new** prop sizing exercise entirely (single conventional prop, not coaxial contra-rotating) — not started this pass. AERO consult needed, successor to AER-71.
5. **Torque reaction / gyroscopic — Packages B/C.** Uncancelled net torque and a real gyroscopic moment on a single prop disk is a new structural/handling item. Flagged to STRUCTURES and AERO, not analyzed here.
6. **Conventional-prop cost/mass delta (Packages B/C)** — not priced or weighed this pass; likely a few kg and low-thousands-of-dollars favorable delta vs. the coaxial contra-rotating assembly, EXTRAP-direction only, no sourced figure.
7. **HV wiring real BOM at the corrected current class** — unchanged open item from PR #16, applies to all packages.
8. **Combo 1 not re-split to R1′** — its $130,900/162%-over figure still includes the prop under the old R1 definition; not re-computed against the new prop-excluded boundary this pass. Directionally the delta is small relative to the size of the gap.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1 — 2026-08-11. Price-vs-capability frontier across three propulsion-motor packages (twin EMRAX 268 / single EMRAX 348 / single EMRAX 268) × two cost bases (all-new / realistic used-salvage), responding to Bill's 2026-08-11 R1′ (frontier, not pass/fail) and R4 (single-motor admissibility pending SAFETY) requirement updates on AER-56.*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
