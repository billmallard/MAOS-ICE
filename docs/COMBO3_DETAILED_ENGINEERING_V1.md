# Combo 3 — Detailed Engineering Spec + Sourced BOM (AER-68)

**Status:** Detailed engineering pass on a downselected architecture. Experimental Amateur-Built category. Not a certification claim, not a hardware commitment.
**Date:** 2026-08-10
**Owner:** PROPULSION
**Origin:** [AER-68](/AER/issues/AER-68), child of [AER-56](/AER/issues/AER-56). Moves Combo 3 (`POWERTRAIN_TRADE_STUDY_50K_V1.md` §2, §9, §10 — MAOS-ICE PR #14) from trade study into detailed design per Bill's direction. **This document does not reopen the architecture** (1G + 1B + 2M series hybrid, coaxial contra-rotating prop, per `2026-04-05-maos-1g1b2m-architecture-decision`) or the component selection (turbo Hayabusa → belt-reduced NetGain HyPer9 HV generator → 2× HyPer9 propulsion motors → 40 kWh LFP battery). It sources, packages, and thermally sizes that package, and it hunts disqualifiers as directed.

**Read the verdict first if you're short on time: §8.**

---

## 0. What changed since the trade study, and why it matters

The trade study (`POWERTRAIN_TRADE_STUDY_50K_V1.md` §8 item 7) carried an open item: *"confirm the Hyper9 HV AC-X144's actual continuous power rating and max RPM — a peak 88 kW oddly listed lower than a rated 120 hp/89.5 kW figure, likely a transcription issue."* This document closes that item, and the answer changes the disposition of the whole combo. See §7.1 — read it before trusting any number below as a green light.

**Vendor attribution correction, made once here and carried through the rest of this document:** "Hyper9 HV AC-X144" and "Hyper9 AC-X1" are products of **NetGain Motors, Inc.** (Lockport, Illinois), not Cascadia Motion and not Enstroj/Emrax — three real but unrelated companies that share no corporate or technical lineage with NetGain. The matched controller line ("HyPer-Drive," model numbers NGM-ACX120 / NGM-ACX144) is built by **SME Group** (Italy), acquired by Dana Inc. in 2019. **AC-X1 and AC-X144 are the same physical motor frame** (same casting, same 229 mm × 355 mm envelope, same 59 kg mass) — they differ only in stator winding, which sets the machine's voltage/current split at a given power, not its physical size or its power ceiling. This is a correction to the design-basis document, not a re-litigation of the component choice.

---

## 1. Sourced BOM — mass, envelope, price, evidence class

Evidence tags follow the trade study's own convention, extended for hardware data: **MFR** = manufacturer datasheet/spec page, **VENDOR** = reseller listing, **FORUM** = anecdotal/community-sourced, **PROXY** = general (non-Hayabusa-specific or non-aviation-specific) literature applied as a stand-in, **EXTRAP** = PROPULSION's own calculation or estimate from a sourced input, **ESTIMATE** = placeholder with no vendor quote behind it at all (same category the trade study already used for the reduction drive).

| # | Item | Price (new) | Price (used/salvage) | Mass | Envelope (L×W×H or ⌀×L) | Evidence | Source |
|---|---|---:|---:|---:|---|---|---|
| 1 | Suzuki Hayabusa Gen3 1340cc, used, bare | $4,000 (trade study midpoint) | same | **~85–91 kg bare engine** | **No sourced bare-engine envelope exists at all** — neither Suzuki nor any swap-kit builder publishes one. EXTRAP from comparable inline-4 1300cc sportbike block+head+sump swap dimensions: **~500×480×450 mm** | FORUM (mass, two independent builder threads); EXTRAP (envelope) | hayabusa.org, locostbuilders.co.uk forums |
| 2 | Aftermarket turbo kit (RCC Turbos Gen3 Stage 1, or equiv.) + conversion (cooling reroute, mounts, ECU) | $6,250 (kit) + conversion labor — trade study carries $4,000 combined turbo+conversion, **below the RCC kit's own list price alone; flag the gap** | same | **~12–20 kg added** (turbo, piping, wastegate; base kit has **no intercooler, no BOV** — charge-air temp is unmanaged in the base config, a real flag for a sustained-duty application) | Concentrated around the manifold/turbo/piping; no intercooler in base kit so no separate core volume to size yet | VENDOR (kit contents, price); EXTRAP (mass) | rccturbos.com |
| 3 | Belt reduction, Hayabusa (~6,500 RPM operating point) → generator input, ~2:1–2.3:1 | $1,500 | same | **~10–15 kg** — no vendor product found in this power class; closest analogs (supercharger drive kits, kart reduction drives) support the ratio mechanically but none is priced/massed at ~100 kW+ continuous | ~300×250×150 mm | ESTIMATE (unchanged from trade study; still no sourced product) | — |
| 4 | Generator: NetGain HyPer9 HV, motor+controller kit (AC-X144 + HyPer-Drive X144) | $5,600 | $3,950 | Motor **59 kg** + controller **4.1 kg** = **63.1 kg** | Motor: ⌀229×355 mm. Controller: 210×160×85 mm | MFR (motor mass/envelope, go-ev.com); VENDOR (kit price, EV West) | go-ev.com, evwest.com |
| 5 | Propulsion motors: NetGain HyPer9, motor+controller kit ×2 (AC-X1 + HyPer-Drive X1) | $10,800 ($5,400 ea) | $7,900 ($3,950 ea) | 2× (motor 59 kg + controller 3.5 kg) = **125 kg** | Each motor: ⌀229×355 mm. Each controller: 210×160×80 mm | MFR (mass/envelope); VENDOR (kit price) | go-ev.com, evwest.com |
| 6 | Battery pack: 40.3 kWh LFP, 45S1P, CATL/EVE-280Ah-class prismatic cells, DIY | $10,000 | $8,600 (salvage, provisional pending AER-67) | Bare cells 45×5.34 kg = 240.3 kg; **finished pack ~300–336 kg** applying a 33% packaging-overhead ratio independently derived from a real Tesla SR pack teardown (328.6 kg bare → 438 kg finished) | Not a single sourced envelope — cell stack alone is 45×71.7 mm = 3.2 m if stacked in one row, so real packaging is multi-row/modular. EXTRAP module footprint pending an actual pack layout: **~1,200×600×250 mm** | MFR (cell spec); EXTRAP (pack mass, cross-validated below) | EVE LF280K-class datasheet; batterydesign.net Tesla teardown |
| 7 | BMS: Orion BMS 2, extended enclosure | ~$2,145 | not surveyed | **4.01 kg** | 406×174×82 mm | VENDOR/MFR | orionbms.com |
| 8 | HV wiring, switchgear, fusing, contactors | $7,000 (trade study BOS baseline — **priced under an implicit low-current assumption, see §7.2**) | same | **~25 kg EXTRAP, flagged low-confidence** — no sourced aviation-grade contactor/cable product found rated for the real continuous current this bus will carry (§7.2) | n/a — distributed | ESTIMATE, now flagged inadequate | — |
| 9 | Engine coolant radiator, installed (core + tanks + mounts) | not separately priced by trade study (folded into "conversion") | — | **~26 kg** (see §4.1 derivation) | ~0.19 m² frontal area core | EXTRAP from two sourced analogs (Rotax 915iS OEM spec; Long-EZ/AC-Aero PWR-core build) | rotaxowner.com SI-PAC-010; alongwayroundtheworld.com |
| 10 | Oil cooler, installed | folded into conversion | — | **~4 kg** | ~53 in² (344 cm²) core | EXTRAP from Rotax 914 (turbo) OEM spec | rotax-owner.com 914 install manual |
| 11 | Electric-side liquid cooling loop (gen + 2 motor coldplates, HX, pump, lines) — sized to **rated continuous** electric losses only, see §4.2 | not priced separately | — | **~7 kg** | n/a | EXTRAP from NASA TM-20205011477 full-loop specific power (§4.2) | NASA GRC/AIAA 2020-3571 |
| 12 | Battery thermal loop (coldplate/HX, pump, lines) | not priced separately | — | **~7 kg** | n/a | EXTRAP, same NASA specific-power basis, imperfect analog (§4.3) | Same |
| 13 | Coaxial contra-rotating prop assembly (2 disks + hub/pitch mechanism) | $8,000 (trade study BOS baseline) | same | **~40 kg** EXTRAP, no vendor quote exists for this specific configuration | ⌀~1.1–1.3 m stack, ~0.6 m axial length incl. hub | ESTIMATE, unchanged category from trade study; AERO consult requested (§5, §9) | — |
| 14 | Contingency (10%, per trade study convention) | ~$5,300 | ~$5,100 | not applicable to mass | — | — | — |

**Installed powertrain total mass: ≈ 738 kg (1,627 lb).** Full derivation and the MTOW comparison are in §6.

**Cost total (new): ≈$56,450, essentially unchanged from the trade study's $55,990** (the corrections above are physical/mass corrections, not cost corrections — the RCC turbo-kit price gap in row 2 is the one line that nudges cost up slightly and is noted, not yet resolved into a new total). **This document does not re-run the cost trade** — §9 v2/v3 of the trade study stands as the cost authority; this pass is additive on mass, envelope, cooling, and prop.

---

## 2. Packaging / Mounting Envelope Summary

For Structures' mount design and a packaging check against boom/airframe geometry. **I do not have access to the live Onshape model in this pass** (no CAD tool connection available to this run) — every clearance call below is a bounding-envelope statement only, not a verified fit against real boom/pod geometry. That check is a named open item (§9).

| Component | Envelope | Mounting notes |
|---|---|---|
| Engine + turbo | ~650×550×500 mm (bare engine EXTRAP + turbo/piping growth) | Firewall-forward or pod-forward, per standing 1G architecture. Needs induction air, turbo downpipe/exhaust routing, and coolant/oil line runs to the radiator/oil-cooler bay — none of which is sited yet. |
| Belt reduction | ~300×250×150 mm | Mounts between engine output and generator input shaft; alignment tolerance for a 2:1–2.3:1 belt drive at ~6,500 RPM input is a real machining/mounting-stiffness requirement, not a bolt-together afterthought. |
| Generator (AC-X144) | ⌀229×355 mm, 63 kg incl. controller | Radial-flux motor — mounts on a shaft line, needs the belt-reduction pulley on one end and a coolant coldplate connection if liquid-cooled variant is used (§4.2 — likely required). |
| 2× propulsion motors (AC-X1) | ⌀229×355 mm ea, 62.5 kg ea incl. controller | Both drive the coaxial contra-rotating prop hub — see §5 for whether a reduction stage is needed between motor and prop (finding: likely not, at the sizing in §5). |
| Battery pack | ~1,200×600×250 mm module footprint (EXTRAP, pre-layout) | **SAFETY (AER-62 §4) requires physical/thermal zoning away from HV bus wiring, contactors, and motor-controller electronics** — a shared bay is a common-cause hazard against the aircraft's sole emergency reserve. This constrains where the ~1,200×600×250 mm volume can go; it cannot simply share the electronics bay. |
| Coaxial contra-rotating prop | ⌀~1.1–1.3 m stack, ~0.6 m axial length | Per standing architecture, mounted at the boom near the aft pod (boom tip ruled out per architecture notes). Geometric clearance against the boom root and empennage is **not verified in this pass** — needs live geometry (§9). |
| Radiator + oil cooler | ~0.19 m² + small oil-cooler core | Needs a forward-facing or NACA-duct inlet with real ducted airflow, not incidental — the stock-motorcycle-radiator baseline this whole class of engine ships with is explicitly road-duty-sized, not continuous-aviation-duty-sized (§4.1). |

---

## 3. (Folded into §1/§2 above per Bill's requested format — every BOM line already carries its envelope.)

---

## 4. Cooling Budget — 96 kW cruise / 155 kW climb

**Read this section's framing carefully: the two headline power points Bill named (96 kW cruise, 155 kW climb) are the mission's electrical demand, not necessarily what any single piece of hardware here can physically sustain.** Where a component's own rated continuous capability is below the mission point, I compute the heat load at both: (a) the component's own rated-continuous operating point (a real, achievable steady state), and (b) what heat *would* result if it were pushed to the mission-required power (a number that exposes the shortfall, not a viable design point — see §7 for why that gap is disqualifying, not just a cooling problem).

### 4.1 Engine (coolant + oil)

No Hayabusa-specific or motorcycle-genset thermal-balance data exists anywhere public (confirmed by dedicated research pass). The best sourced full-load, turbocharged-engine thermal split found is Caterpillar 3412C TA (turbodiesel, load-tested): **36% shaft / 37% exhaust / 27% cooling (22% coolant + 5% oil)**. This is a PROXY — diesel, not gasoline SI — used because it is the only real load-tested turbocharged split found; the generic SI "thirds" rule (33/33/33) is noted as a secondary sanity check and would push cooling load somewhat higher, not lower, so the Cat split is the less conservative of the two available proxies.

| Mission point | ICE output | Fuel energy in (÷0.36) | Coolant (22%) | Oil (5%) | Exhaust (37%, informational — not radiator's load) |
|---|---:|---:|---:|---:|---:|
| Cruise | 96 kW | 267 kW | **58.7 kW** | **13.3 kW** | 98.7 kW |
| Climb (conservative, ICE-equivalent) | 155 kW | 431 kW | **94.7 kW** | **21.5 kW** | 159.3 kW |

The climb figure treats the full 155 kW bus demand as if the ICE alone had to produce it — the real architecture splits this with the battery, and the actual ICE-side split for a derated Hayabusa (credited ~70 kW, §7.1 of the trade study) is unresolved. **This is deliberately the conservative (larger) sizing case, per "size it honestly."**

**Radiator sizing**, cross-checked against two real, sourced analogs:
- Rotax 915iS OEM coolant radiator (best-in-class aviation-optimized): 30 kW at 500 cm², 1.10 kg → **0.06 kW/cm², 27.3 kW/kg** (core only).
- A real homebuilder liquid-cooled-Lycoming-conversion radiator install (Long-EZ, AC-Aero LIO-390, PWR racing cores), fully dimensioned and weighed: 63.4 kW at 1,340 cm² combined core, **17.3 kg full installed system** (radiators + pumps + lines + coolant) → 0.047 kW/cm², **~3.7 kW/kg full-system**.

Sizing to the climb load (94.7 kW coolant): **frontal core area ≈ 1,580–2,000 cm² (0.16–0.20 m²)**; **installed mass ≈ 3.5 kg (bare core, best case) to 26 kg (full installed system with pumps/lines/coolant)**. I adopt **~26 kg installed** as the BOM number — it is the fuller, more honest figure, since a bare core alone is not what goes on the aircraft.

**Explicit caveat carried from the engine-side research, unresolved here:** the stock Hayabusa road radiator (≈374×216 mm, ≈0.052 m² frontal area) is sized for a road vehicle's variable duty and ram/road-airflow — it is not a continuous-100%-duty design and is not being proposed as the flight radiator. The ~0.19 m² sizing above is a purpose-built replacement, not the stock part.

**Oil cooler sizing**, from Rotax 914 (turbocharged, closest real analog): 10 kW at 160 cm² minimum → **0.0625 kW/cm²**, cross-validated by an independent aviation OEM datasheet (Stewart-Warner/SouthWind LCHX curves, 0.15–0.46 kW/in² ≈ 0.023–0.071 kW/cm² at 100°F ITD — the Rotax figure sits inside this band). Sizing to climb (21.5 kW): **≈344 cm² (53 in²) core**. Mass EXTRAP from motorsport bar-and-plate coolers of similar heat class (Setrab data, ~6–9 kW/kg): **≈3–4 kg installed**.

### 4.2 Generator + inverter, 2× motor + inverter

**This is the section that changes the combo's disposition — read §7.1 for the full finding; this subsection only carries the thermal-sizing consequence of it.**

NetGain publishes a real continuous power rating for this motor family, air-cooled: **38 kW @ 3,300 RPM** (generator role, AC-X144) and **38 kW @ 3,300 RPM each** (motor role, AC-X1 ×2, so 76 kW combined). Vendor-claimed (third-party, EV Europe — not a NetGain factory figure) liquid-cooled continuous is **40–50 kW**, unverified.

At the machine's own **rated continuous** point (94% peak efficiency, vendor-claimed; ~97% controller efficiency assumed by analogy to the NASA HLMC inverter's 98.3% at a comparable power class):

| Component | Rated continuous power | Loss (6% motor + ~3% controller ≈ 9% combined, conservative) | Heat |
|---|---:|---:|---:|
| Generator (AC-X144) | 38 kW | 9% | 3.4 kW |
| 2× motors (AC-X1) | 76 kW combined | 9% | 6.8 kW |
| **Total, at rated-continuous operation** | **114 kW combined** | — | **~10.3 kW** |

Sizing a liquid-cooling loop to this real, achievable heat load, using NASA/TM-20205011477's directly-measured full-loop specific power for a 54–68°C coolant electric-powertrain loop (**1.3–3 kW/kg**, fixed-wing case): **mass ≈ 3.4–7.9 kg**. I adopt **~7 kg** (conservative end) as the BOM figure.

**What happens if the mission point is applied instead (96 kW through the generator, 155 kW combined through the motors):** scaling losses linearly (itself optimistic — real machines don't hold efficiency constant well past their rated point) gives ~8.6 kW generator loss and ~14 kW combined motor loss, ~23 kW total — a heavier loop, sizeable but not implausible on paper. **The reason this isn't a valid design point is not the cooling loop's size — it's that 96 kW and 155 kW combined both exceed the machines' own published continuous ratings before cooling is even considered.** NetGain's air-cooled heatsink is rated to 150°C max, and the matched controller thermal-shuts-down at 95°C with derating starting at 80°C. Pushing sustained current well past the rated point is not "run it hotter and cool harder" — it's operating outside the envelope the manufacturer validated at all, continuous-duty TBO/insulation-life unknown, in exactly the same evidentiary position SAFETY already flagged for the Hayabusa ICE (§1.3 of the trade study) — except here it's the electric machines, and the shortfall is worse in percentage terms (§7.1).

### 4.3 Battery pack thermal

At climb (30–60 kW draw from a 40.3 kWh, 45S1P/144V pack ≈ 0.75–1.5C), two independent estimates bracket the heat load:
- Direct I²R from cell datasheet DC resistance (1.5 mΩ conservative datasheet ceiling): **3–12 kW** across that C-rate range.
- Independent academic calorimetry on a comparable prismatic LFP cell, normalized: **~8.2 kW at 1C** (≈40 kW draw) for this pack size — sits above the datasheet-DCR estimate, suggesting the datasheet figure may itself be optimistic for an aged/real-world cell.

**Design basis: 8–12 kW sustained at the top of the climb power band.** LFP's thermal-runaway margin is large (runaway onset ~200–270°C vs. a 45–60°C safe continuous ceiling — a >150°C margin per cell datasheets and academic abuse-testing), so the active-cooling question here is about **staying under the 45–60°C continuous-operation band for cycle life and capacity**, not runaway avoidance. Sizing a cold-plate loop to 8–12 kW at the same NASA specific-power basis (1.3–3 kW/kg, though a battery loop typically runs colder than the 54–68°C motor/inverter loop this figure was measured at, which would make it heavier per kW, not lighter — flagged as an imperfect analog): **mass ≈ 4–9 kg**. I adopt **~7 kg**.

### 4.4 Cooling drag — first-order estimate, not a duct-specific calculation

Gudmundsson's cooling-drag framework (installed-vs-uninstalled momentum-drag difference) and published GA rule-of-thumb figures put cooling drag at roughly **5–15% of total aircraft drag** for a typical single, rising toward 25%+ for a poorly optimized installation (sources range 7% [AOPA-cited consulting figure] to 25% [NASA cowling-history figure] to as high as 35% in less-favorable citations — genuine spread in the literature, not a single number). Applied to the trade study's own computed cruise drag (D = 826 N, §1.1 of the trade study): **cooling drag ≈ 58–124 N (13–28 lbf)**, i.e. **an additional 4.6–9.9 kW of thrust power at cruise TAS** not currently reflected in AERO's L/D = 14 figure (a "clean" L/D estimate conventionally excludes powerplant-installation drag, which is added afterward — this is a genuine, sourced, additive item to flag to AERO, not resolvable from this side of the interface alone).

**This is a bounding estimate from literature ratios, not a momentum-theory calculation against real duct/inlet geometry** — that calculation needs the boom/pod CAD, which I don't have access to this pass (§9).

### 4.5 Cooling system mass rollup

| Item | Mass |
|---|---:|
| Engine coolant radiator, installed | 26 kg |
| Oil cooler, installed | 4 kg |
| Electric-side loop (gen + 2 motors, rated-continuous sizing) | 7 kg |
| Battery thermal loop | 7 kg |
| **Total cooling system** | **~44 kg** |

This is **not a showstopper by mass** — 44 kg is a small fraction of the ~738 kg powertrain total. **The showstopper is that the electric side cannot be cooled into meeting the mission power point at all, at any mass** — see §7.1. Cooling mass and cooling drag are real, honestly-sized penalties, but they are not what kills this combo; §7.1 is.

---

## 5. Propeller Spec Matched to the Motors

**Architecture is not open here** — per `2026-04-05-maos-1g1b2m-architecture-decision`, the combo already specifies a single **coaxial contra-rotating** prop assembly, each disk driven by one of the two AC-X1 motors. This resolves the "single vs. twin" question the issue asked me to close: it's neither — it's one coaxial installation with two counter-rotating disks, not two separate propellers on the boom.

### 5.1 Motor-side inputs

- AC-X1 continuous rating: 38 kW @ 3,300 RPM, max 8,000 RPM (MFR).
- AC-X1 continuous torque: not published; my own inference from continuous power ÷ angular velocity: **≈110 N·m** — flagged as computed, not a vendor figure, and to be checked against the (image-only, not machine-readable in this pass) NetGain performance curve before it's load-bearing for a shaft/hub stress calc.

### 5.2 First-cut disk sizing — actuator-disk (momentum) theory

Using the trade study's own cruise numbers (§1.1): thrust required D = 826 N, V = 79.7 m/s (155 KTAS), and the trade study's own back-solved installed propeller efficiency (≈0.82, still an AERO-unconfirmed number per that document's own flag). Assuming installed efficiency runs at ~87–90% of ideal (loss-free) actuator-disk efficiency for a well-designed prop (η_ideal ≈ 0.94), and solving the standard actuator-disk relation for disk area:

- **A ≈ 0.99 m² → D ≈ 1.12 m (44 in)** at an assumed cruise density altitude (ISA 8,000 ft, ρ ≈ 0.963 kg/m³ — altitude not yet confirmed by AERO, flagged).
- Implied disk loading: T/A ≈ 831 N/m² — higher (more heavily loaded, smaller diameter) than a typical low-RPM GA prop of this power class (which would run ~1.8–2.0 m at ~200–400 N/m²), consistent with a **high-RPM, small-diameter, direct-drive** design point rather than a conventional geared low-RPM prop.

### 5.3 Tip speed / direct-drive feasibility check

Running the AC-X1 **direct-drive at its rated continuous 3,300 RPM** (55 rev/s) against the ~1.12 m diameter above:

- Rotational tip speed: π × 1.12 m × 55 rev/s ≈ **193.5 m/s**
- Helical tip speed (vector sum with 79.7 m/s forward speed): **≈209.3 m/s**
- At ISA 8,000 ft (a ≈ 336 m/s): **helical tip Mach ≈ 0.62**

This sits comfortably under the ~0.85–0.9 helical-Mach ceiling generally used to avoid compressibility drag rise and disproportionate noise. **Finding: a compact (~44 in), high-RPM, direct-drive coaxial disk pair is plausible without a motor-to-prop reduction stage**, at this first-cut sizing — a materially different answer than the Hayabusa-to-generator side, which does need a reduction (§5.2 of the trade study). This also favors packaging near the boom/aft-pod location (smaller diameter, better clearance) versus a larger low-RPM alternative.

### 5.4 Thrust at cruise and climb

- Cruise: T = 826 N (185.7 lbf), at 80 kW shaft power (per AERO's published figure), ≈82% installed efficiency (AERO-unconfirmed, flagged in the trade study since 2026-08-09 and still not closed).
- Climb (max, 155 kW bus): applying 94% motor efficiency to get shaft power (155 kW × 0.94 ≈ 146 kW shaft), and holding the same ≈82% installed prop efficiency as a first-cut (AERO should refine this — off-design efficiency at climb speed/RPM is not the same number as cruise): **thrust power ≈ 119.5 kW ÷ V_climb**. Climb speed (V_y) isn't published in the material available to this pass — **flagged as a missing AERO input needed to convert this to a thrust figure**, not fabricated here.

### 5.5 What this section does NOT close

This is PROPULSION's own first-cut sizing (actuator-disk theory plus a tip-speed check), not a validated blade-element or CFD design. Per the issue's own instruction, **AERO owns propeller aerodynamics** — blade count, activity factor, airfoil selection, and a real BEM/CFD efficiency check (including the contra-rotating swirl-recovery term and any duct/pylon interference near the boom) are AERO's call, not mine to assert. **A consult issue to AERO is being opened alongside this document (§9)** with the sizing above as the starting input, plus a request to confirm the ≈0.82 propeller efficiency figure this whole chain still rests on unconfirmed since the original trade study flagged it 2026-08-09.

**Geometric clearance (ground/boom/fuselage) is not verified in this pass** — no live geometry access this run (§9).

---

## 6. Mass Statement

| Group | Mass |
|---|---:|
| Engine + turbo kit | 105 kg |
| Belt reduction (engine→generator) | 12 kg |
| Generator + controller | 63 kg |
| 2× propulsion motors + controllers | 125 kg |
| Battery pack (finished, incl. packaging overhead) | 320 kg |
| BMS | 4 kg |
| HV wiring/switchgear/fusing/contactors | 25 kg |
| Cooling system (radiator, oil cooler, electric loop, battery loop) | 44 kg |
| Coaxial contra-rotating prop assembly | 40 kg |
| **Total installed powertrain mass** | **≈738 kg (1,627 lb)** |

**Cross-check:** the battery-pack figure here (320 kg / 706 lb) was derived independently in this pass (cell count from pack-voltage/energy targeting, packaging overhead from a real Tesla-pack teardown ratio) and lands almost exactly on the trade study's own independently-cited figure — "706 lbs for 40 kWh [LFP]" (§4 of the trade study, sourced from `maos-propulsion-redundancy-battery`). Two independent derivations agreeing this closely is a real, if partial, validation of the overall mass-estimation approach used in this document.

**Against MTOW (2,600 lb / 1,179 kg): the powertrain alone is ≈62.6% of MTOW.** This is far outside the range typical of GA piston singles, where powertrain (engine + fuel system, excluding fuel itself) usually runs 20–30% of MTOW even before accounting for this being a hybrid architecture carrying both an ICE and a full battery reserve. It also directly collides with a number already on the record: the trade study (§4) cites a **1,200 lb useful-load target** the battery weight was already competing against for space. This powertrain's 1,627 lb is **427 lb (36%) over that entire useful-load figure by itself, before crew, payload, or any range-extending fuel beyond what's needed for the base mission is counted.** I am not asserting a formal empty-weight/useful-load violation here — I don't own the aircraft's mass-properties ledger and don't know whether "useful load" in that citation is meant to include the powertrain or sit alongside it — but the magnitude of the gap is large enough that it needs a formal reconciliation with Structures/mass-properties, not a wait-and-see. See §7.3 and §9.

---

## 7. Adversarial Disqualifier Hunt

Per the issue's explicit mandate, I went looking for a reason this doesn't work. I found two independent ones, plus a mass finding that compounds both. Ranked by how hard they are to argue with.

### 7.1 — HEADLINE FINDING: the generator cannot deliver the required continuous power, on the manufacturer's own published numbers

The trade study flagged the AC-X144's continuous rating as an unresolved evidence gap (§8 item 7, quoted above). It is now resolved, and it is bad news: **NetGain's own published continuous rating for the HyPer9 HV (AC-X144), air-cooled, is 38 kW at 3,300 RPM** — corroborated independently across the manufacturer's own site (go-ev.com) and three resellers (EV West, EVolve Electrics, Thunderstruck-EV). The best-case alternative — a third-party (EV Europe, not NetGain) liquid-cooled variant claim — tops out at an **unverified 40–50 kW continuous**.

Against the mission's **96 kW continuous cruise floor** (§1 line 7 of the trade study, itself independently corroborated by MAOS-ICE's own formal requirement ICE-SYS-001), this is a **48–60% shortfall on manufacturer-published data — not a pending-bench-test question like the ICE side (§1.3 of the trade study), a documented ceiling today.**

This is a **harder** finding than the already-known Hayabusa engine shortfall (credited ~70 kW vs. 96 kW required, a 27% gap, and that one at least has a path to being resolved upward by a bench program). The generator's number is a hard, manufacturer-published, air-cooled-class-appropriate rating on a machine that costs $5,600 — and that price is itself a tell in hindsight: a genuine 96 kW-continuous liquid-cooled aviation-class generator (Emrax 268 at ~72 kW continuous, or H3X HPDM-180R) costs $12,000–$40,000+, not $5,600. The Hyper9 line is a real, well-documented product — it's just an EV-conversion-class machine being asked to do a job roughly 2–2.5× past its rated continuous envelope.

**Compounding finding on the motor side:** the two AC-X1 propulsion motors have the identical rating structure (same frame, same 38 kW continuous each) — **76 kW combined**, against an 80 kW cruise shaft-power target (a near-miss, uncomfortably tight) and **far short of the 155 kW combined climb bus demand** (a 51% shortfall even crediting the unverified liquid-cooled 40–50 kW/motor claim). The motor controllers are independently current-limited too (750–760 A air-cooled peak, vendor-noted "2 min max" duration) — climb at MAOS's mission profile plausibly runs longer than 2 minutes, which is a second, independent ceiling on the same finding.

**Why this is not "just needs bigger cooling":** §4.2 already shows the cooling-loop mass to reach the rated-continuous point is small (~7 kg) — cooling isn't the constraint. The constraint is the machine's own insulation/thermal design ceiling (150°C heatsink max, controller thermal shutdown at 95°C) and continuous-duty life at that current, which is a **machine-design limit, not a heat-exchanger-sizing limit**. Pushing more coolant at it does not raise the rating NetGain has qualified the part to.

### 7.2 — HV bus voltage mismatch: this is not the 400V-class bus the requirement envelope assumes

The trade study's requirement envelope (line 15) lists HV bus voltage as an **open gate — DG-004, 400V vs 800V**, and its own recommendation text (§7) describes "a 400V-class bus" in the Combo 3 narrative. **The actual NetGain HyPer9 HV line is a 90–180V DC machine (144V nominal) — the AC-X1 side is 55–130V DC (≤120V nominal). Neither is remotely 400V-class.** This isn't a typo-level gap; it's two full voltage classes apart.

At the real 144V nominal bus: **cruise current ≈ 667 A continuous (96 kW ÷ 144V), climb ≈ 1,076 A (155 kW ÷ 144V)** — roughly **2.8× the current a 400V-class assumption would have implied** for the same power. The trade study's $7,000 BOS wiring/switchgear/fusing line item, and every combo's cost/mass baseline built on it, was priced against an implicit lower-current design point. I could not find a single sourced aviation-grade contactor or cable product in this pass rated for continuous four-figure-amp DC switching at this scale — that's a real, unresolved sourcing gap on top of being a mass and I²R-loss driver the BOM hasn't priced or weighed correctly (§1 row 8's ~25 kg figure is my own extrapolation, flagged low-confidence, likely an underestimate).

This finding stands **independent of §7.1** — even if the generator's power ceiling were somehow not a problem, the bus voltage this hardware actually operates at was never the bus voltage the architecture's own requirement line assumed.

### 7.3 — Mass: 62.6% of MTOW, and 427 lb over the cited useful-load figure

Already derived in §6. Not independently disqualifying the way §7.1 is (mass problems have levers — smaller reserve, different chemistry, lighter cooling), but it **compounds** §7.1 and §7.2 rather than offsetting them: fixing the power shortfall by paralleling a second generator or upsizing to a liquid-cooled variant (the most direct fix for §7.1) adds mass and cost on a combo that is already mass-heavy and was only 2% over the $50k cost line before any of this pass's findings.

### 7.4 — What did NOT turn out to be a disqualifier

Per the mandate to report this plainly either way: the **reduction-drive practicality** question (Hayabusa→generator) remains what the trade study already found — mechanically well-precedented, not a blocker. The **prop-side reduction** question (§5.3) resolves favorably — direct-drive at 3,300 RPM checks out on tip Mach at a first-cut sizing. **Cooling mass and cooling drag are real and honestly sized (§4), but small relative to the powertrain total and not, by themselves, a showstopper.** The disqualifier here is electrical, not thermal.

---

## 8. Verdict

**Not a validated-so-far-with-open-gates result. This is a named disqualifier, on manufacturer-published data, independent of the bench-test-pending finding the trade study already carried.**

Combo 3 as specified — turbo Hayabusa → belt-reduced NetGain HyPer9 HV (AC-X144) generator → 2× NetGain HyPer9 (AC-X1) propulsion motors → 40 kWh LFP battery — **cannot deliver the 96 kW continuous cruise / 155 kW climb mission envelope through its electric machines, on the manufacturer's own continuous power ratings, independent of whether the Hayabusa engine side ever clears its own bench-test gate.** The generator is rated for 38 kW continuous against a 96 kW requirement (a 60% shortfall); the two propulsion motors combined are rated for 76 kW continuous against an 80 kW cruise target (uncomfortably tight) and a 155 kW climb target (a 51% shortfall even at the unverified liquid-cooled claim). This sits on top of, and is measured against different hardware than, the trade study's already-known ICE-side shortfall (§1.3) — it does not get resolved by the same bench program, because it is not a duty-cycle-derate question, it is a manufacturer-rated ceiling on different hardware entirely.

**What this does and does not mean for the board:**

- **It does not mean no combo works.** Combo 1 (Rotax 916 iS + Emrax) remains, per the trade study's own §7, the architecturally distinct fallback that doesn't depend on any of this — Emrax's continuous ratings are real and don't carry this problem, at ~2.6× the cost.
- **It does mean Combo 3 as currently specified needs a different electric machine, not a different cooling system or a different bus.** The generator and motor selection — not the ICE, not the battery, not the prop — is the load-bearing failure here. A fix plausibly looks like: a genuinely 96 kW+-continuous-rated generator (which, per §7.1's own cost-sanity-check, likely costs $12k–$40k+, not $5.6k) and/or paralleling multiple Hyper9-class units (which reopens the cost and mass pictures this whole trade study series has been trying to hold the line on).
- **This is a real, first-class result per the issue's own framing** ("A named showstopper with its number and evidence is a first-class result, not a failure"), not a rejection of the detailed-engineering effort. The BOM, packaging, and cooling work in §1–§6 stand on their own regardless of the electric-machine finding and are directly reusable once a corrected generator/motor selection is made.

**What remains unproven even setting §7.1–§7.2 aside**, for the record: the Hayabusa continuous-duty bench program (trade study §7, unchanged by this pass), the propeller efficiency figure AERO has not yet confirmed (§1.1 of the trade study, still open), the propeller's own AERO-validated sizing (§5.5, consult opened this pass), the boom/pod geometric clearance check for both the prop and the radiator/duct (no live geometry access this pass), and the HV bus/wiring re-sizing implied by §7.2.

**Escalating to AER-56 (parent) as directed**, with this document's §7.1 and §7.2 as the headline findings for Elon/Bill's disposition call: iterate Combo 3 with a corrected electric-machine selection, or move to Combo 1 as the working baseline while a corrected Combo-3-class option is sourced.

---

## 9. Open Items / Consults

1. **AERO consult opened** (child issue, alongside this document) — propeller aerodynamic sizing/BEM check against the §5.2–§5.3 first-cut, and confirmation of the ≈0.82 propeller efficiency figure open since the original trade study (2026-08-09).
2. **Corrected generator/motor selection** — the direct consequence of §7.1. Candidates to screen: Emrax (continuous ratings are real, already priced in Combo 1 at the motor role), H3X HPDM-180R (already catalogued, ~$20-40k/unit), or paralleling multiple Hyper9-class units (cost/mass consequence not yet modeled). This is naturally a follow-on trade study, not resolved here.
3. **HV bus voltage (DG-004)** — this document's §7.2 finding makes the open gate more urgent: whatever generator/motor replaces the Hyper9 line should have its native voltage class checked against DG-004 before another combo gets built on an unstated voltage assumption.
4. **Live geometry access** — no Onshape/CAD connection was available in this pass; boom/pod clearance for the prop (§5.5) and the radiator/duct inlet siting (§4.4) both need it. Owner: whoever holds the live model connection for this run cadence.
5. **Bare-engine envelope and turbo-kit added-mass/envelope** — no manufacturer or vendor source exists for either; §1 rows 1–2 rest on forum anecdote and PROPULSION's own extrapolation. A real measurement (a bare engine on a scale, a fitted turbo kit measured) would close this cheaply.
6. **HV wiring/switchgear mass and sourcing at real current** — §7.2's ~25 kg figure is low-confidence; no sourced product was found at the ~700–1,076 A continuous class this bus actually needs. Needs a Systems/PROPULSION joint sourcing pass.
7. **Battery pack real envelope** — §1 row 6's module footprint is pre-layout EXTRAP; a real 45S pack layout (module count, busbar routing, coldplate integration) hasn't been drawn.
8. **Cooling drag** — §4.4 is a literature-ratio bound, not a duct-specific momentum-theory calculation. Needs real inlet/duct geometry to tighten, and needs to be fed back to AERO as an addition to the L/D = 14 figure, not assumed already included in it.
9. **Climb speed (V_y)** — not found in the material available to this document; needed to close §5.4's climb thrust number. AERO input.
10. All open items already carried by the trade study (§8, §9.7 of `POWERTRAIN_TRADE_STUDY_50K_V1.md`) remain open and are not superseded by this document — the Hayabusa bench-endurance program in particular remains a live, separate gate even though this document's own finding (§7.1) is now the more binding constraint.

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 1 — 2026-08-10. Detailed engineering pass on Combo 3 per AER-68: sourced BOM with mass/envelope (§1), packaging summary (§2), cooling budget at 96 kW cruise / 155 kW climb (§4), propeller first-cut sizing matched to the AC-X1 motors (§5), full mass statement vs. MTOW (§6), and an adversarial disqualifier hunt (§7) that surfaces a manufacturer-data-sourced generator/motor continuous-power shortfall (§7.1) and an HV bus voltage mismatch (§7.2) — both independent of, and more binding than, the trade study's already-known Hayabusa bench-test gate. Verdict: named disqualifier, not a validated-with-open-gates result (§8).*
*R&D guidance for Experimental Amateur-Built development. Not a certification claim.*
