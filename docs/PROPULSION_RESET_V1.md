# Propulsion Reset — Three Architectures on Mission Metrics, Benchmark is a Direct-Drive Pusher

**Status:** Design-phase analysis. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment.
**Date:** 2026-09-05 (v1.1: SAFETY consult AER-610 closure conditions P1–P4 addressed, §3/§3.1/§6/§7)
**Owner:** PROPULSION
**Origin:** [AER-608](/AER/issues/AER-608), child of [AER-56](/AER/issues/AER-56). Runs under `makerplane/decisions/ORG-003-design-phase-constraints.md` and `makerplane/briefs/propulsion_reset.md`. Supersedes `POWERTRAIN_TRADE_STUDY_50K_V1.md`'s scored recommendation (Package A) — that document's §1 and §1.3 carry an erratum note pointing here, not a re-score.
**Divergent pass** (seven architectures, physics floors, no ranking) posted to AER-608 before this document per ORG-003's divergence rule. This document sizes the three the issue asks for in full (A0, A1, A2) and carries the candidate-core catalogue and recommendation.

Every number below is tagged **MFR** (manufacturer-published), **SOURCED** (a real quote, listing, or dated third-party measurement), **EXTRAP** (scaled from a sourced number by an explicit, stated ratio), or **ASSUM** (an engineering assumption with no direct source, credited per ORG-003 where it's a power-derate figure). Where the design cannot close without a number PROPULSION does not own, that is stated as a block, not filled in.

---

## 0. Method — mission physics and the MTOW-closure loop

Per ORG-003 Ruling 2, **MTOW is an output, not an input.** Every cruise/climb power figure and every battery/fuel mass below is derived from the mission, then closed against the airframe's own mass — including the powertrain's own mass, which is why this is a loop, not a lookup.

**0.1 Cruise shaft power vs. weight.** Re-deriving `POWERTRAIN_TRADE_STUDY_50K_V1.md` §1.1's method (P = D·V, D = W/(L/D)) as a function of weight instead of a fixed 2,600 lb:

```
P_shaft_cruise (kW) = W(N) / (L/D) × V / η_prop
                    = 0.03088 × MTOW(lb)      [L/D = 14 clean, V = 155 KTAS = 79.73 m/s, η_prop = 0.82]
```

At the old 2,600 lb anchor this reproduces the published 80 kW shaft figure exactly (2,600 × 0.03088 = 80.3 kW) — the method is unchanged, only the anchor is now a variable. **L/D = 14 is the clean-configuration cruise value** (AERO, `maos-1g1b2m-architecture-decision`); the windmill-drag-corrected L/D 8.1–10.2 (AER-82/AER-454) applies only to the engine-out glide case in the failure ladders below, not to normal-operation power sizing. η_prop = 0.82 is PROPULSION's back-solved value, still flagged for AERO to confirm or correct (unchanged from the prior study).

**0.2 Climb power vs. weight — a named low-confidence extrapolation.** The only climb power data on record (120 kW ICE-alone/700 fpm, 141 kW bus/1,000 fpm, 155 kW bus/1,200 fpm) was derived for the 1G+1B+2M series-hybrid architecture at 2,600 lb. I scale these linearly with MTOW as a first-cut (`P_climb(x) = P_climb(2,600 lb) × x/2,600`) because no architecture-specific thrust-required-vs-speed climb curve exists for A0/A1's direct-mechanical configuration. **This is EXTRAP, not a real curve, and it is a named block on AERO**: a direct-drive pusher and a series-hybrid twin-motor coaxial installation do not necessarily share a climb power schedule, and linear MTOW-scaling of one architecture's number onto another is a coarse stand-in. Findings below that turn on climb margin are flagged accordingly.

**0.3 The reserve.** Per ORG-003 Ruling 3, the reserve is a powered descent from FL180, starting point ~40 kW. **AERO has not yet published the descent-profile-vs-time curve this needs** — this is a named block. In its absence I use the brief's own first-cut bound (`propulsion_reset.md` §2.3): 40 kW for ~39 min ≈ **26 kWh**, the higher end of the brief's 16–26 kWh range, as the sizing baseline (conservative side, since undersizing a flight-safety reserve is the wrong direction to round). A0 (no battery) has no powered reserve — its failure case is an unpowered glide, addressed in the failure ladder.

**0.4 The number I do not own: airframe-only empty weight.** MTOW = (airframe structure + systems + avionics, excluding powertrain, fuel/battery, crew, and payload) + crew/payload + powertrain + fuel/battery. STRUCTURES has not published this figure for the post-ORG-003, un-frozen airplane — the only real inconsistency check available (AER-69 v2's "1,200 lb useful load before crew/fuel/payload" at the old 2,600 lb MTOW) does not close (671 kg powertrain leaves ~510 kg for structure + systems + four people + fuel, which is not physically achievable — exactly why ORG-003 struck that MTOW). I am not going to manufacture false precision here. **This document uses an ASSUM placeholder of 750 kg** (bracket 700–800 kg), loosely anchored to composite 4-seat GA airframes of comparable span minus their powertrain (e.g., a Diamond DA40-class airframe-only figure), consistently across A0/A1/A2 so the *comparison* between architectures is valid even though the *absolute* MTOW numbers are not final. Crew + payload: 4 × 200 lb (170 lb FAA-average adult + 30 lb baggage share) = 363 kg, ASSUM, also not yet a published AERO/board target. **Fixed non-powertrain, non-fuel mass used throughout: 1,113 kg (2,454 lb).** STRUCTURES' real number is the next input that moves every MTOW below — this is the handoff this document is asking for.

**0.5 Fuel/energy closure.** For a given architecture, powertrain mass (excl. fuel) is fixed once components are chosen; fuel or battery mass is solved self-consistently against MTOW:

```
MTOW = 1,113 + M_powertrain(architecture) + M_fuel(MTOW)
```

M_fuel itself depends on cruise power, which depends on MTOW — solved as a fixed point (shown per architecture below) rather than iterated by hand-waving. A +8% fuel margin is carried on top of pure cruise burn for climb/taxi/start (separate from the emergency descent reserve, which is architecture-specific per §0.3).

---

## 1. Physics floor per chain type

Before any vendor part — the minimum installed mass and cost a chain of each type can plausibly reach, from first principles, at this mission's cruise power class (~90–130 kW shaft, see §2–4).

**Direct-drive.** Floor = one ICE at the best demonstrated installed power density for a turbocharged 4-stroke in this class (bare engines in the 1.5–2.5 kW/kg range are real and sourced — Hayabusa bare ~2.5 kW/kg, EXTRAP; Rotax 916 iS bare ~1.36 kW/kg MFR since its 85.8 kg already carries turbo/intercooler/reduction) times a GA installation tax (cooling, exhaust, mount, cowl) of roughly 1.15–1.4× bare mass (Gudmundsson-class GA integration figures, EXTRAP) + a prop (~15 kg). **Floor ≈ 0.65–1.0 kg installed per kW credited**, and the cost floor is whatever a mass-produced automotive- or motorcycle-derived block costs used ($1,500–8,000, SOURCED range across this catalog) plus a few thousand dollars of aviation-specific integration (mount, ECU, prop) — **no generator, no motor, no battery, no second conversion stage, and the lowest chain-efficiency loss of any option** (ICE thermal efficiency alone reaches the prop, ignoring a small reduction-gear loss).

**Parallel hybrid.** Floor = the direct-drive floor above **plus** one electric machine sized to the climb-boost delta (not full climb power, since the ICE still supplies its own share) plus a reserve-sized battery. The physics saving over series is that the mechanical path to the prop is unchanged — no generator, no double electrical conversion, so the *only* new mass is the boost machine, its controller, and the pack. The physics floor is therefore direct-drive's floor + (boost-motor mass, ~0.3–0.4 kg/kW continuous for a purpose-built aviation PM machine, EMRAX-class SOURCED) + (battery mass, chemistry-dependent, §0.3).

**Series hybrid.** Floor = an ICE sized to continuous cruise/charge power only (can, in principle, be *smaller* than direct-drive's climb-sized engine) **plus** a generator (≈4–5 kW/kg installed, EMRAX/H3X-class SOURCED) **plus** propulsion motor(s) sized to combined climb power **plus** power electronics **plus a second, lower-temperature cooling loop for the electric machines, distinct from the ICE's loop** — my own cooling-flow tradecraft (electric-side loops run 5–10× heavier per kW than an ICE coolant loop, because power electronics tolerate a much smaller coolant ΔT) says this is a first-order mass term, not a rounding error, and it was **not separately priced in the prior Package A figure**. This is the fundamental "carry two conversion chains" tax: you pay for a full electric drivetrain (generator + motors + controllers + electric cooling) *in addition to* the ICE, not instead of gearing/coupling hardware. The physics floor is inherently the heaviest of the three chain types; what it buys is placement freedom (the genset need not be on the thrust line) and a motor-level failure ladder instead of an engine-level one.

---

## 2. A0 — Direct-drive pusher (the benchmark)

Single ICE, single pusher prop, aft pod. No generator, no motor, no battery.

| Engine option | Credited power (method) | Bare/dry mass | Installed mass (+ tax) | Price new | Price used |
|---|---|---|---|---|---|
| **Rotax 916 iS** | **101 kW continuous, MFR** (137 hp @ 5,500 RPM — a real, published continuous rating, distinct from the 160 hp/118–120 kW takeoff rating); 118–120 kW available for climb (short-duration, standard piston practice, no derate) | 85.8 kg MFR (incl. turbo, intercooler, reduction gearbox) | 121 kg (+35 kg ASSUM/EXTRAP: radiator/oil cooler — explicitly excluded from the dry figure — exhaust, mount) | ~$57,000 SOURCED (dealer range $49,529–$64,099, midpoint) | ~$50,000 EXTRAP (certified hardware holds value on a thin used market — the catalog's own finding, §4 below) |
| **Viking 195T** | **109 kW ASSUM** (75% of 145 kW/195 hp documented rated output — Viking publishes no distinct continuous or generator-duty rating separate from peak); 145 kW available for climb (peak, short-duration standard practice) | 118 kg MFR (260 lb, "ready for installation" — radiator, exhaust, cowl, mount, prop explicitly **not** included) | 153 kg (+35 kg ASSUM/EXTRAP for the excluded items) | $24,000 MFR, current (supersedes the stale $20,495 figure in the brief) | ~$19,000 EXTRAP (automotive-block core has some used-market discount; Viking's integration kit does not) |

Prop (single pusher, composite, non-coaxial): 15 kg, ~$7,000 new / ~$5,000 used — EXTRAP, comparable GA composite pusher-prop class; not the $8,000/40 kg coaxial contra-rotating unit A2 needs.

**Closure (fixed-point solve, §0.5):**

| | Rotax 916 iS | Viking 195T |
|---|---|---|
| Powertrain (excl. fuel) | 121 + 15 = 136 kg | 153 + 15 = 168 kg |
| ICE thermal efficiency at cruise operating point | 0.32 ASSUM (Rotax's published BSFC class implies ~32–34%; used conservatively) | 0.30 ASSUM (automotive-tuned block, less aviation-specific optimization) |
| **MTOW (converged)** | **1,424 kg / 3,140 lb** | **1,474 kg / 3,251 lb** |
| Cruise power required | 97.0 kW | 100.4 kW |
| **Cruise margin vs. credited power** | **+4.0 kW / 4.0%** | **+8.6 kW / 8.6%** |
| Fuel (mission + 8% margin) | 175 kg (~64 US gal) | 193 kg (~71 US gal) |
| Climb (700 fpm anchor, EXTRAP scaling, §0.2) | 144.9 kW needed vs. 118–120 kW available — **~18% short** | 150.0 kW needed vs. 145 kW available — **~3% short, essentially closes** |

**Finding:** the best-evidence engine (Rotax, a real MFR continuous rating) clears cruise with almost no margin and falls meaningfully short on the climb extrapolation; the ASSUM-credited engine (Viking, a 75%-of-peak estimate) numerically closes both with more room, because its larger peak-power headroom (145 kW vs. Rotax's 118–120 kW) matters more here than its worse evidence class. **This is an evidence-quality-vs-performance-margin trade, not a clean win for either option**, and it is worth naming to Bill in those terms rather than picking one silently.

**Reserve after ICE loss:** none — unpowered glide at windmill-corrected L/D 8.1–10.2 (AER-454), same risk category as the GA-single fleet baseline (Hazardous, not Catastrophic, per AER-81's provisional classification — still gated on the open R7/R9 glide-configuration items).

---

## 3. A1 — In-line parallel hybrid

ICE mechanically coupled to the same prop shaft as a pancake motor; battery for climb boost and the powered-descent reserve.

**Finding, before sizing:** cruise power at the honestly-derived MTOW (§0) is already close to what a Rotax- or Viking-class engine delivers continuously — there is *not* the large "smaller cruise-only ICE" headroom the brief assumed at the old 2,600 lb anchor. A1's ICE cannot be meaningfully downsized from A0's without failing cruise once its own extra mass (motor + battery) is honestly counted.

| Component | Mass | Price new | Price used | Evidence |
|---|---|---|---|---|
| ICE (AM20T-class — see below for why Rotax doesn't close here) | 149 kg | $27,995 | ~$20,000 EXTRAP | MFR (mass, price); ASSUM (credited power) |
| Prop (shared, single pusher) | 15 kg | $7,000 | $5,000 | EXTRAP |
| Boost motor + controller (EMRAX 228-class) | 28 kg (13.5 kg motor, **MFR**, liquid-cooled variant, `EMRAX_228_datasheet_v1.6.pdf`, 2025-03 + ~14.5 kg controller/mounting, **EXTRAP**) | $10,000 EXTRAP | $5,000 **SOURCED** (two independent 2024–25 used listings: motor $2,500 + BAMOCAR D3-400-250 controller $2,500, DIY Electric Car Forums) | Motor mass and continuous power now **MFR**-sourced this pass (superseding last pass's EMRAX-268 mass-ratio scaling); controller mass/new price remain EXTRAP |
| Reserve/boost battery, 26 kWh, LFP | 208 kg | $6,500 | — | SOURCED ($250/kWh, `POWERTRAIN_TRADE_STUDY_50K_V1.md` §4/§9) |
| Reserve/boost battery, 26 kWh, ProLogium-class solid-state | 105 kg | **no price found** | — | Cell-level 381 Wh/kg is SOURCED/TÜV-verified (2026-09-02); pack-level 248 Wh/kg is **EXTRAP** (a 65% cell-to-pack derate I applied — no vendor pack spec exists; Elysian's 320–420 Wh/kg is an aspirational MoU target for a future aircraft pack, not a measured spec of this cell, confirmed this pass) |
| Wiring/contactors/misc | 10 kg | — | — | ASSUM |

**Why AM20T, not Rotax, for A1:** running the same closure with Rotax 916 iS (121 kg installed, 101 kW continuous) and the ProLogium pack gives MTOW 1,587 kg (3,499 lb), which needs 108.1 kW at cruise — **7% short of Rotax's own continuous rating.** Swapping to AM20T (149 kg, 146 kW ASSUM-credited) gives:

| | AM20T + ProLogium | AM20T + LFP |
|---|---|---|
| Powertrain (excl. fuel) | 149+15+28+105+10 = 307 kg | 149+15+28+208+10 = 410 kg |
| **MTOW (converged)** | **1,634 kg / 3,604 lb** | **1,753 kg / 3,865 lb** |
| Cruise power required | 111.3 kW | 119.4 kW |
| **Cruise margin vs. 146 kW ASSUM credit** | **+23.7%** | **+18.3%** |
| Fuel | ~214 kg | ~228 kg (EXTRAP, same method) |
| Climb (1,000 fpm anchor, EXTRAP scaling): ICE + boost motor combined | 195.6 kW needed vs. **210 kW available (146 kW AM20T ASSUM-credited + 64 kW EMRAX 228 MV/HV liquid-cooled continuous, MFR, `EMRAX_228_datasheet_v1.6.pdf` v1.6 2025-03)** — **+7.4% margin**, no longer resting on an unverified motor rating (superseded the prior pass's ~50 kW EXTRAP figure; the boost motor's real continuous S1 rating turns out higher than assumed, not lower) | similar, slightly worse |

**Reserve after ICE loss — scoped by fault mechanism per SAFETY's AER-610 ruling (§3.1):** for a **clean** ICE fault (fuel starvation, detonation, oil loss — the shaft keeps turning freely) the powered descent is real: motor + reserve battery, ~26 kWh at 40 kW pending AERO's profile, a genuine capability A0 does not have. For a **seizure** fault on either machine, the claim does **not** hold as stated: a rigid shared shaft lets a seized ICE or a seized motor mechanically lock the other out, taking the whole reserve with it — a common-cause mode AER-81's physically-separate coaxial motors never had to consider. This is now condition **P1** below, not a resolved capability. **Motor/inverter-out (clean fault):** ICE continues driving the prop unassisted (two independent torque paths on one shaft), losing boost/climb margin but not thrust. **Also open:** a double-fault case (any of battery, bus/contactor, motor windings, or motor controller failing silently first, erasing the reserve without annunciation, followed later by ICE failure) leaves A1 in exactly A0's unpowered-glide case with no warning the safety margin is gone — condition **P4** below.

### 3.1 SAFETY consult (AER-610) — closure conditions P1–P4

SAFETY closed [AER-610](/AER/issues/AER-610) with conditions, not a blanket pass (comment on AER-608, 2026-09-05): R1 was written for two *electrical* channels off a shared upstream bus/generator; A1's shared ICE+motor shaft is a new configuration that satisfies R1's intent for clean faults on either side but not for a shaft-seizure common-cause fault. Four conditions before A1's powered-descent reserve is a resolved safety case rather than a pending one:

- **P1 (PROPULSION + STRUCTURES) — coupling isolation.** Does the ICE↔motor↔shaft coupling include a freewheel, sprag clutch, or shear element that prevents a seizure on either machine from locking the shaft? **Not yet a design decision** — no coupling detail exists at this pass's fidelity (§3's mass/cost table treats the shaft as a bare mechanical join). **Engineering answer, ASSUM:** an overrunning (sprag) clutch on the motor's connection to the shaft is the standard mitigation for exactly this failure mode in automotive parallel-hybrid practice, and it is mechanically simple at this torque class — estimated **1–2 kg** added mass, not a first-order mass or cost item. What it does *not* resolve on its own: a clutch on the motor side protects the ICE from a seized motor, but an ICE seizure (a locked crankshaft) still locks the shaft downstream of the clutch unless the clutch (or a second one) sits between the ICE and the shared shaft instead. Which side (or both) needs the isolation element is a coupling-topology decision that lives with the physical mount and shaft design STRUCTURES owns for the boom-root/pod aft structure (AER-69) — opened as a child issue, not decided here. **Status: OPEN, child issue to STRUCTURES.**
- **P2 (PROPULSION, with AERO's climb curve) — ICE-alone climb.** Using the same EXTRAP method as §0.2/§3 (120 kW ICE-alone/700 fpm anchor at 2,600 lb, scaled linearly by MTOW — the only labeled ICE-alone climb data point on record, still cross-architecture EXTRAP pending AERO's real curve): AM20T's own rated/standard-tune output (194 kW MFR, not time-limited — the 300 hp variant *is* time-limited and is excluded from ASSUM credit per §5) against the scaled 700 fpm requirement gives **+16.7% margin at the ProLogium MTOW (166.3 kW required vs. 194 kW available) and +8.7% margin at the LFP MTOW (178.4 kW required vs. 194 kW available)**. Both are positive — satisfies the "positive-but-reduced is acceptable" bar SAFETY set, using a *lower* climb-rate target (700 fpm, not the combined-power 1,000 fpm case in §3's main table) consistent with "reduced." **Status: ANSWERED this pass (EXTRAP), still pending AERO's architecture-specific curve for a non-EXTRAP number.**
- **P3 (PROPULSION) — EMRAX 228-class boost motor+controller FIT-rate evidence.** Searched this pass (2026-09-05): EMRAX's own current datasheet (`EMRAX_228_datasheet_v1.6.pdf`, 2025-03) gives a real MFR continuous power rating (55/64/75 kW by air/liquid/combined cooling, all voltage variants) and mass (12.9–13.5 kg bare motor) — this **supersedes** the prior pass's EMRAX-268 mass-ratio EXTRAP and is now applied in §3's table and climb closure above. **What remains unresolved, and cannot be closed by further searching:** no FIT rate, MTBF, or any quantitative reliability/failure-rate figure is published anywhere for EMRAX motors or BAMOCAR-class controllers — not by EMRAX, not in any certification record found, not in the closest available literature (a 2024 CEAS Aeronautical Journal review of all-electric-aviation reliability surveys design-level challenges for this exact hardware class but publishes no component FIT rate). This is an evidence gap in the hardware itself, not a lookup PROPULSION can close with more effort. Per ORG-003, the bench SAFETY's R2 gate calls for is real, new data (a test program), not a citation — flagging this explicitly to SAFETY rather than filling it with an invented number. **Status: MFR power/mass sourced; FIT-rate evidence confirmed absent industry-wide — a named permanent gap until bench data exists, not a pending search.**
- **P4 (PROPULSION + SYSTEMS) — reserve-chain health annunciation.** SAFETY ruled the silent four-component latent-failure exposure (battery, bus/contactor, motor windings, motor controller) **not acceptable as residual risk**. Spec proposed this pass: a single latching "RESERVE DEGRADED" caution, OR-triggered by (a) pack SOC below the reserve-sizing threshold, (b) bus/contactor continuity failure, (c) motor winding fault flag, (d) motor controller fault flag — one annunciation, not four, so a pilot gets one unambiguous cue rather than a fault-isolation exercise mid-flight. This is an avionics/bus-health logic item, not a propulsion-hardware one; implementation sits with SYSTEMS (DG-004 bus owner) and the pyEfis rewrite. **Status: OPEN, child issue to SYSTEMS.**

---

## 4. A2 — Series hybrid, corrected (Package A's electric side, direct-coupled genset, re-sized pack)

Turbo Hayabusa (or equivalent) → EMRAX 268 generator → HV bus → 2× EMRAX 268 motors → coaxial contra-rotating prop → LFP or ProLogium reserve battery.

**Fixed electric-side components (independent of ICE choice), all SOURCED except cooling:**

| Component | Mass | Price new | Price used |
|---|---|---|---|
| Belt/reduction, ICE→generator | 12 kg | $1,500 | — |
| Generator: 1× EMRAX 268 MV + BAMOCAR D3-700/400, 117 kW continuous | 30.4 kg | $17,000 | $8,500 |
| 2× propulsion motors: EMRAX 268 MV + BAMOCAR, 234 kW combined continuous | 60.8 kg | $34,000 | $17,000 |
| Coaxial contra-rotating prop | 40 kg | $8,000 | $8,000 |
| **Electric-side cooling loop — NEW, not in the prior Package A 634 kg figure** | **~70 kg ASSUM/EXTRAP** | — | — |

The cooling addition: ~35 kW of electric-side heat at climb (≈10% loss across generator + 2 motors + controllers at combined ~350 kW capacity, ASSUM) at an installed specific mass of ~2 kg/kW rejected — my own two-analog bracket (OEM best-case ~0.5–1 kg/kW vs. a full-installed homebuilder/motorsport analog ~3–5 kg/kW, midpoint used) for a coolant loop that must run cooler than the ICE's own loop. **This has not been separately priced anywhere in the prior trade study and is a real mass this document is adding.**

**Closure — this is the headline finding.** Setting up the same fixed-point solve as A0/A1, but through the series chain (P_ICE_crank × 0.84 = P_shaft, the generator+bus+motor composite efficiency already established in the prior study):

| ICE option | Credited power | Installed mass | Subtotal (ICE + electric, ×1.10 contingency) | + Battery (ProLogium 105 kg) | **MTOW** | **ICE crank power required** | **Margin** |
|---|---|---|---|---|---|---|---|
| Turbo Hayabusa | 105 kW ASSUM (75% of 140 kW stock, ORG-003's own worked example) | 105 kg SOURCED | 350.0 kg | 455.0 kg | **1,858 kg / 4,097 lb** | **150.6 kW** | **−43% — does not close** |
| Aeromomentum AM20T | 146 kW ASSUM (75% of 194 kW rated — no MFR continuous label found) | 149 kg MFR | 398.4 kg | 503.4 kg | **1,916 kg / 4,224 lb** | **155.3 kW** | **−6% — does not close** |

Swapping the LFP pack in for ProLogium (heavier, 208 kg) makes both worse (Hayabusa: −53%; AM20T: still short), so **this is not a battery-chemistry problem — it is an ICE-sizing problem that the architecture's own mass drives.** Solving for the credited power that *would* self-consistently close A2 at this electric-side spec (holding installed-mass-per-credited-kW at AM20T's own ratio, ~1.02 kg/kW): **≈156 kW credited**, which at ORG-003's 75% ASSUM rule requires a **documented rated crank output of ~208 kW (279 hp)** — larger than any core currently in this catalog, including AM20T's boosted 300 hp/5-min-limited variant (which, being explicitly time-limited, does not qualify as "documented rated output for the planned tune" under the rule's own language). Zongshen CA550T's real 106.6 kW MFR continuous rating (no derate needed — the best evidence class of any core evaluated) is closer to Hayabusa's *credited* figure than to what A2 needs, and does not close either.

**Why this matters:** the series-hybrid mass premium (generator + 2 motors + controllers + the newly-added electric cooling loop + battery ≈ 350–450 kg before contingency) drives MTOW high enough that a genset sized to *that* MTOW's cruise power needs to be substantially bigger than anything this catalog has priced — which in turn would add its own mass, in a self-reinforcing spiral distinct from A0/A1's much smaller, closing margins. **A2 as specified in this issue (turbo Hayabusa-class core) does not close the mission on paper once MTOW is honestly re-derived from the real (non-2,600-lb) airframe mass** — independent of the ICE credit-rule dispute, independent of battery chemistry, and independent of the R1 safety question. This is a first-principles finding, not a sourcing gap: no currently-catalogued core is both cheap and big enough.

**Reserve after ICE/generator loss:** ~26 kWh at 40 kW (pending AERO's profile), same as A1, but with no mechanical fallback (unlike A1, there is no direct path from a dead electrical chain to the prop) — total loss of thrust on bus/battery failure regardless of ICE/generator health, an unpowered glide at the same windmill-corrected L/D as A0/A1, not yet separately verified for the coaxial contra-rotating configuration (R7 in AER-81/AER-454, open). **Motor-out (one of two):** admissible per AER-81's ruling (R1 satisfied by the physically separate coaxial units, per AER-69), remaining motor continues at reduced thrust.

**A second, independent reason A2 does not close: there is no sited envelope for the genset core, and the one real envelope in CAD is the wrong size.** STRUCTURES' review of `GENSET_PACKAGE_SPEC_V0.md` (AER-609, 2026-09-06, cross-linked on this issue) found that the boom-root nacelle (⌀686×914 mm) in the live AER-69 v2 CAD is sized and load-cased for the twin-EMRAX-268 *propulsion motors* (60.8 kg, rigid-mount, no fire zone) — the ICE genset core has never been sited by STRUCTURES at all (AER-69 v2 §9 item 1, open). If the core landed at that same nacelle anyway, a genset core + generator + cooling package per this document's own §4 figures runs **≈126–223 kg, 2.1×–3.7× the mass that envelope was designed to carry**, and introduces two load cases the nacelle concept never scoped: vibration-isolated mounting (target fₙ ≤ 13–20 Hz, vs. the rigid mount an electric motor allows) and a fire zone/firewall (fuel, oil, hot exhaust — an electric-only nacelle needs neither). This is on top of, not instead of, the power-closure gap above: even a hypothetical 208 kW-rated core that solved §4's power math would still have nowhere sited to go. **STRUCTURES should not spend real mount/firewall design effort on any A2 core until this issue's pending decision (below) resolves which architecture is being drawn.**

---

## 5. Candidate-core catalogue — the search spaces the board has not opened

Researched this pass, sourced and dated. Columns: evidence class per ORG-003's own taxonomy (OEM continuous / fleet rating / steady-state dyno / none), and the ORG-003-credited power that follows from it.

| Core | Rated/peak power | Evidence class | ORG-003 credited power | Mass | Price | Notes |
|---|---|---|---|---|---|---|
| **Rotax 916 iS** | 160 hp / 118–120 kW peak | **OEM continuous** (137 hp/101 kW, a genuine distinct rating) | **101 kW, MFR** | 85.8 kg dry (MFR) | $49,529–$64,099 (dealer, SOURCED) | Best evidence class of any option in this catalog |
| **Viking 195T** | 195 hp / 145 kW | None (no continuous label found, confirmed this pass) | 109 kW, **ASSUM** | 260 lb/118 kg dry (MFR) | **$24,000 current** (supersedes stale $20,495) | |
| **Aeromomentum AM20T** | 260 hp / 194 kW standard | None (TBO 1,800 hr stated against the standard rating, but not labeled "continuous") | 146 kW, **ASSUM** | **285 lb/129 kg** (supersedes stale 143 kg) | **$27,995** standard (supersedes stale $29,700, which is actually the 300 hp 5-min-limited variant at $29,700) | 300 hp variant is explicitly 5-min limited — does not qualify for ASSUM credit under ORG-003's "planned tune" language |
| **Turbo Hayabusa Gen3** | 140 kW stock | None — **confirmed this pass: no steady-state or continuous-duty dyno data exists anywhere for a turbo Hayabusa, at any power level.** Only peak dyno pulls and land-speed/drag single passes are documented. The "commission a 30-min steady pull" evidence path the brief proposed is real but **has not been done by anyone** — it would be new data, not a lookup. | 105 kW, ASSUM | 105 kg installed (SOURCED) | $8,000 used (SOURCED) | |
| **Zongshen CA550T** | 106.6 kW | **OEM continuous + published TBO (1,000 hr)** — no derate needed | **106.6 kW, MFR** | 80 kg incl. reduction gearbox | $45,300 | Best non-Rotax evidence class; costs as much as Rotax, doesn't solve cost |
| **DeltaHawk (DHK180/200/235)** | 175–235 hp class | OEM continuous (diesel, certificated) | per model, unchanged from prior catalog | ~195 kg (DHK235A4) | **No official price list exists.** Forum/dealer-reported FWF quotes: $100–125K (C172/RV-14 class, Oct 2025); $60K engine-only (Bearhawk, distinct from FWF) | Confirmed this pass — still quote-only |
| **H3X HPDM-180D** | 180 kW continuous | OEM spec (current product; **supersedes the HPDM-250, which no longer appears in H3X's lineup as of this pass** — treat any HPDM-250 figure as historical 2023–24 data) | n/a (motor/generator, not credited under the ICE rule) | **13 kg** (13.9 kW/kg continuous — better than the superseded HPDM-250's 18.7 kg) | No pricing found | Exceptional density; still unscoreable without a price |
| **Evolito E800** | 110 kW continuous | OEM spec, confirmed current (evolito.aero, rebranded from evolito.co.uk) | n/a | 28.3 kg (confirmed) | No pricing found | Type-cert submission to UK CAA ongoing (Electra EL9), no Aug/Sep 2026 news beyond that |
| **ProLogium Gen 3.5 cell** | — | Cell-level: **TÜV-verified, SOURCED** (381 Wh/kg, 2026-09-02 press release) | n/a | — | **No price found** | Pack-level Wh/kg **not published by ProLogium**; the 320–420 Wh/kg figure attached to this cell in some coverage is an Elysian Aircraft MoU **target for a future pack**, not a measured spec — confirmed this pass, don't conflate the two. No cycle-life or C-rate data published. |

**Automotive series-hybrid / range-extender engines — the new search space, assessed honestly:**

| Engine | Peak/rated power | Continuous rating | Weight | Standalone sourcing | Verdict |
|---|---|---|---|---|---|
| Li Auto 1.5T (L2E15M) range-extender | 113–115 kW (secondary Chinese media) | Unverified secondary claim of 65 kW rated generator output | **Not found anywhere** | **None found** — no teardown, reman, or standalone listing | Dead end for now: no weight, no primary-source continuous rating, no acquisition path |
| BYD DM-i 1.5T "Xiaoyun" | 136 kW (1.5T variant) | None published (BYD's architecture is parallel/series-switchable, not pure-series, so no dedicated generator rating exists) | Not found | None found | Dead end |
| Nissan e-POWER 1.5 VC-Turbo (KR15DDT) | 106 kW (Nissan Technical Review No. 89, 2023 — best-sourced of the four, but ambiguous whether engine-crank or generator-electrical) | Not distinctly published | Not found | None found for the ICE itself (only motor/generator-unit EV-conversion reuse precedent exists — not the engine) | Best-documented of the four, still not usable without weight and a real continuous figure |
| Honda i-MMD 2.0L Atkinson (naturally aspirated) | ~107 kW (2018 Accord Hybrid class, secondary-sourced) | None published | Not found | Best physical-acquisition path of the four (US salvage market, one SOURCED $1,179 longblock listing) — but **naturally aspirated**, so a standard NA altitude lapse (~50% power remaining at FL180/18,000 ft) disqualifies it for this mission's altitude floor regardless of continuous-rating or weight questions | Disqualified on altitude alone, independent of the missing data |

**Finding:** this search space, opened for the first time this pass, is **not yet a usable source of candidate cores** — none of the four automotive range-extender engines has a primary-source continuous rating, a published weight, or any standalone/genset conversion precedent. This is worth reporting plainly rather than assuming promise: the "lightweight mass-produced turbocharged ICE optimized for generator duty" product class Bill described exists in production vehicles, but none of it is documented, weighed, or sourceable as a standalone unit today. Closing this gap would mean a teardown/measurement program, not a literature search — a real, named cost if the board wants to pursue it further.

---

## 6. What's still needed — consults and blocks

- **STRUCTURES**: airframe-only empty weight (excl. powertrain/fuel/crew/payload) for the post-ORG-003 airplane. Every MTOW in this document is provisional on this number (§0.4). Separately, per AER-609 (2026-09-06): the ICE genset core has no sited mount station anywhere in CAD (§4) — this is now a blocking input to A2 specifically, not just a mass-properties refinement, and should not be worked further until the pending architecture decision (§7) resolves.
- **AERO**: (a) the powered-descent profile from FL180 (§0.3) — this document uses a first-cut 26 kWh/40 kW bound pending it; (b) a real climb thrust-required-vs-speed curve per architecture — the linear MTOW-scaling used in §2–4 is a named low-confidence extrapolation (§0.2); (c) confirmation or correction of η_prop = 0.82 (carried unresolved from the prior study).
- **SAFETY**: [AER-610](/AER/issues/AER-610) closed with conditions (2026-09-05) — A1 satisfies R1's intent for clean-fault cases, not for shaft-seizure common-cause faults. Four conditions (§3.1): **P1** OPEN, child issue to STRUCTURES (coupling freewheel/clutch); **P2** answered this pass (EXTRAP, pending AERO's real climb curve); **P3** MFR power/mass now sourced, FIT-rate evidence confirmed absent industry-wide (permanent gap pending bench data); **P4** OPEN, child issue to SYSTEMS (reserve-chain health annunciation).
- **SYSTEMS**: DG-004 HV bus voltage remains open and unchanged by this reset; A2's bus demand and heat load are unaffected by which of §4's two ICE options is chosen.
- **Cost gaps that block scoring, not engineering**: ProLogium pack pricing (chemistry can't be cost-compared until it has a price); H3X HPDM-180D and Evolito E800 pricing (both would materially shrink A2's electric-side mass if priced — H3X's 13 kg/180 kW continuous vs. EMRAX 268's 30.4 kg/117 kW per channel is a large enough density gap to revisit A2's closure math if either vendor ever quotes).

---

## 7. Recommendation

**A0 (direct-drive pusher) is the only architecture of the three that closes on paper today**, and it does so with the numbers this document derives rather than the numbers a fixed 2,600 lb MTOW implied. Between its two engine options, neither is a clean win: Rotax 916 iS carries the best evidence (a real continuous rating) but almost no cruise margin and a real climb shortfall on the (low-confidence) extrapolated climb curve; Viking 195T carries a weaker, ASSUM-credited rating but closes both cruise and climb with real margin because its peak-power headroom is larger. That trade is Bill's to weigh, not mine to pre-resolve.

**A1 (parallel hybrid) is the closest thing to a real contender against the benchmark**, but only with an ICE bigger than the brief assumed (AM20T-class, not Rotax-class) — once its own battery/motor mass is honestly counted, a cruise-sized-to-the-old-mission ICE doesn't clear cruise at its own honest MTOW. It buys a real powered-descent reserve A0 doesn't have, at a mass premium of roughly 170–300 kg over A0 depending on chemistry, with a climb margin now better evidenced than the prior pass (+7.4% combined, MFR-sourced boost-motor rating, §3) and one fully-answered condition on the reserve claim (ICE-alone climb, §3.1 P2). It still carries **two open SAFETY conditions before the reserve is a resolved capability rather than a pending one**: whether the shaft coupling isolates a seizure on either machine (P1, with STRUCTURES) and a reserve-chain health annunciation (P4, with SYSTEMS) — both now tracked as child issues, neither yet closed. A1 exists on paper regardless of P1/P4's outcome; what they gate is whether its powered-descent reserve can be credited as resolved in the failure ladder SAFETY signs off on.

**A2 (series hybrid) does not close** with any core currently in this catalog, independent of battery chemistry, independent of the R1 safety question, and independent of DG-004. This is the single most important finding in this document: the series architecture's own mass (generator + twin motors + controllers + the newly-identified electric-side cooling loop + reserve battery) drives MTOW high enough that no priced, ORG-003-creditable engine in this catalog is big enough to sustain cruise on the generator alone. Closing it needs either a genset core nobody has found yet (~208 kW rated, ~156 kW credited — bigger than anything catalogued), or a fundamental relaxation of what A2 is asked to do (accept continuous battery assist at cruise, which breaks the reserve-only battery philosophy and needs its own re-derivation), or the mission/MTOW target changing enough to lower the power requirement. A2 now carries a second, independent failure: STRUCTURES confirms (AER-609, §4) no mount station has ever been sited for a genset core, and the only real envelope in CAD is 2.1×–3.7× undersized for one. Even the missing 208 kW core, if found, would still need a firewall and an isolated mount designed from nothing.

**The one Bill decision that most changes the answer:** whether the mission accepts a bigger, heavier direct-drive-first airplane (A0/A1, closing today on paper) or whether series hybrid's placement-freedom and motor-level failure ladder (A2's real advantages, when it can be made to close) are worth funding the missing genset core — a real engine that does not yet exist in this catalog at any price. That is not a request-confirmation about a number to relax; it is a question about which unopened door to fund searching behind, and it is posted as a `request_confirmation` on this issue.

---

*Version 1 — 2026-09-05. First document under the ORG-003 reset. Supersedes `POWERTRAIN_TRADE_STUDY_50K_V1.md`'s scored recommendation; that document carries an erratum note in §1/§1.3 pointing here rather than a re-score of its combos.*

*Version 1.1 — 2026-09-05. Addresses SAFETY's AER-610 closure conditions P1–P4 (new §3.1): sources EMRAX 228's own datasheet for boost-motor mass/continuous power (superseding the prior EMRAX-268 mass-ratio EXTRAP, §3), recomputes A1's climb margin (+7.4%, up from a razor-thin unverified figure), computes ICE-alone climb margin for a boost-motor-out case (P2), confirms no FIT-rate/reliability data exists industry-wide for this motor class (P3), and scopes the powered-descent reserve claim between clean-fault and shaft-seizure cases pending two new child issues to STRUCTURES (P1) and SYSTEMS (P4).*

*Version 1.2 — 2026-09-06. Folds in STRUCTURES' AER-609 review (§4, §6, §7): the ICE genset core has no sited mount station anywhere in CAD, and the one real envelope (the boom-root nacelle, sized for twin propulsion motors) is 2.1×–3.7× undersized for a genset core plus cooling — a second, independent reason A2 does not close, on top of §4's power-closure gap. No numeric changes to A0/A1/the candidate catalogue.*
