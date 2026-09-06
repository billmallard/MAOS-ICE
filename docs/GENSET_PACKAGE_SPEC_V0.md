# Genset Package Interface Control Document — V0

## Document Control

- **ICD ID:** MAOS-ICE-ICD-001
- **Title:** Engine-agnostic genset package interface (coupling, coolant, CAN/control, fault semantics)
- **Revision:** V0.1 (draft — corrected per SYSTEMS/STRUCTURES review)
- **Status:** Draft
- **Effective date:** N/A (design-phase reference; not yet released)
- **Owner repository:** `MAOS-ICE`
- **Owner(s):** PROPULSION
- **Reviewer(s) requested:** SYSTEMS (bus voltage DG-004, CAN contract), STRUCTURES (mount datum and loads), SAFETY (endurance / sustained-boost / cooling FMEA lines), MANUFACTURING (coupling and cooling buildability)
- **Related issue(s) / PR(s):** [AER-609](/AER/issues/AER-609) (this document), parent [AER-56](/AER/issues/AER-56), context `makerplane/briefs/propulsion_reset.md` §4, `makerplane/decisions/ORG-003-design-phase-constraints.md`, `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md`, `COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md`
- **Revision history:** V0 (2026-09-05, initial draft, PR #20) → V0.1 (2026-09-06, this revision) corrects the mount-siting claim per STRUCTURES' [AER-670](/AER/issues/AER-670) review and records SYSTEMS' conditional DG-004 concurrence per [AER-669](/AER/issues/AER-669); neither review is a full close-out, both trails stay open per the Open Issues table.

Built on `INTERFACE_CONTROL_DOCUMENT_TEMPLATE.md`. Every number below carries a tag: **MFR** (manufacturer-published spec), **SOURCED** (a documented figure not from the core vendor — a related MAOS-ICE document, forum/community data, or a cited third party), **EXTRAP** (extrapolated from a related/analog source), **ASSUM** (an assumption this document is making, including every ORG-003 credited-power line).

---

## Purpose and Scope

**What this controls.** The interface between a mass-produced internal-combustion core (any of the shortlist in §3, or a future one) and everything else in the MAOS series/parallel-hybrid propulsion chain that the core does not itself provide: the mechanical coupling to a PM generator, the coolant loop, the fuel/air/exhaust envelope, the CAN/control contract for fixed-operating-point generator duty, and the fault/telemetry semantics the rest of the airplane depends on.

**What this explicitly does not control.** Which core wins. No engine-specific number lives in this section — every number specific to a candidate core lives in §3's shortlist table. This ICD is written so that swapping the core (Hayabusa for Viking, Viking for a Li Auto range-extender) changes only §3, not §§1–2, 4–6. Also out of scope: the battery pack interface (Systems/Propulsion joint, separate document), the propulsion-motor-to-prop interface (`COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md`), and airframe firewall-forward structural design (Structures' consult, requested, not yet returned as of this draft — see Open Issues).

**Why this document exists now, engine-agnostic, before a core is picked.** Per `propulsion_reset.md` §4: whatever core wins, someone has to build the coupling, the cooling, the fixed-point control, and the endurance data — no vendor sells these for a generator-duty aircraft installation. Making the *interface* the product, rather than a spec bolted to one engine, is what turns "find the engine" from the critical path into a commodity-shopping exercise. This is Bill's stated interest (issue AER-609 opening: *"I am especially interested in 'a genset package around a mass-produced core: yes'"*) and is separable from, and can proceed in parallel with, the AER-56 architecture-reset divergent pass.

**Consumed inputs and their status:**

| Input | Owner | Status |
|---|---|---|
| Mission demand curve (96 kW cruise-bus floor, 155 kW climb-bus floor, FL180) | AERO / AER-68 | **Carried in as the current best-available figure, not re-validated here.** These derive from the now-released 2,600 lb MTOW baseline (ORG-003 Ruling 2) and will re-derive per architecture when AERO closes the mission-energy loop. Used in this document as the sizing target for the genset's electrical output; flagged ASSUM where load-bearing. |
| HV bus voltage (DG-004) | SYSTEMS / PROPULSION, joint | **Conditional concurrence received (AER-669, 2026-09-06).** SYSTEMS offers conditional concurrence at **~700 Vdc nominal** — correcting this ICD's original "~700–800 Vdc" framing, which conflated the proposed nominal with the BAMOCAR controller's 780–800 V *overvoltage protection ceiling*, not a nominal-voltage range. Full conditions are on AER-669. This document now carries **~700 Vdc nominal (ASSUM, pending SYSTEMS' conditions closing)** as its working bus-voltage figure — see Open Issues. |
| Mount datum, envelope, load path (aft pod / boom root) | STRUCTURES / AER-69 | **Reviewed and corrected (AER-670, 2026-09-06).** The prior draft of this row overstated AER-69 v2: the boom-root CAD envelope (⌀686×914 mm) is sited for the **2× propulsion motors + prop hub** (60.8 kg, twin-EMRAX-268 package), not for an ICE or generator. **The genset core's mount station has never been sited by STRUCTURES** — AER-69 v2 §9 item 1 carries "engine + turbo siting" as an unresolved open item, and the belt/direct-drive-reduction+generator group rides wherever the engine lands, so its station is open too. There is no STRUCTURES-confirmed envelope for the genset core anywhere in the airframe today. This ICD specifies the mounting **pattern**, not a location, and the siting decision itself — not a missing measurement of an agreed location — is the open item; see Open Issues. |
| SAFETY cooling/endurance FMEA lines (AER-62) | SAFETY | Received as a design input, not released. ORG-003 Ruling 1 confirms these stay FMEA-owned risk lines, not a design-phase power cap. |

---

## Interface Participants

- **Producer / source system:** the IC engine core (any shortlisted candidate, §3) plus its integral accessories (oil pump, water pump, alternator/starter where retained, factory ECU where usable).
- **Consumer / sink system:** the PM generator machine (§2), the MAOS HV bus (DG-004, jointly Systems/Propulsion), the airframe coolant/air/exhaust provisions (Systems), the MAOS CAN bus and its control/telemetry consumers (FCS, logging, SAFETY monitoring).
- **Additional participants:** MANUFACTURING (coupling and cooling buildability), the bench-rig test stand (§6) as a stand-in consumer during development.

---

## Operational Context

- **Flight phase relevance:** climb, cruise, and (for a parallel-hybrid or as a battery-charging trickle) descent. The genset is not sized for takeoff boost — that load is carried by the battery buffer per the architecture's power-split (out of scope here; see the AER-56 reset architecture comparison).
- **Ground operation relevance:** engine start, warm-up to operating coolant temperature before load application, and shutdown cool-down (turbo-tune candidates need a forced idle/cool-down period before shutdown — standard turbocharger practice, ASSUM 60–120 s at low load, core-specific figure TBD per candidate).
- **Normal mode behavior:** fixed-RPM, fixed (or narrowly scheduled) load, closed-loop-governed generator duty — the core holds a target RPM against generator electrical load, not a pilot throttle input. This is the operating regime that makes Fallback 2 in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §5.2 viable and is the central simplification this interface exploits relative to a variable-throttle aircraft engine installation.
- **Degraded mode behavior:** derate (reduced RPM/load target) or commanded shutdown per the state machine in §5.5; battery buffer sustains the bus per the reserve sizing carried in from the architecture (`maos-propulsion-redundancy-battery`, open item on re-sizing per §5.3 of the reset brief — not resolved here).

---

## Interface Definition

### 1) Mechanical Interface

**Mounting datum and pattern.** The interface uses a **flywheel/bellhousing-style mounting pattern** — a bolt circle on the engine's flywheel-housing face plus a spigot/pilot bore for radial location, the same geometry class as an SAE automotive bellhousing pattern (SAE J617/J620 families) or a motorcycle-engine's own output-shaft flange, whichever the core presents natively. This is the mechanically simplest engine-agnostic datum because every mass-produced core in §3 already terminates its crankshaft at one of these two flange families — the package adapts *to* the core's native flange with a machined adapter plate, rather than requiring the core to be modified to a MAOS-specific pattern.

| Element | Spec | Tag |
|---|---|---|
| Primary mounting reference | Engine's native flywheel-housing bolt circle + pilot spigot (bellhousing-class) or output-shaft flange (motorcycle-class) | ASSUM (interface choice) |
| Adapter plate | One per core family, machined to the core's native pattern on one face and a common MAOS generator-mount pattern on the other | ASSUM — this is the one part in the whole package that is core-specific by design, and is intentionally the cheapest part to re-manufacture when the core changes |
| Engine-side vibration isolation | Engine mounts per core manufacturer's recommended mount stiffness/damping class (motorcycle engines: solid or semi-rigid per motorsport practice; automotive-derived cores: OEM elastomer mount class, adapted) | ASSUM, core-specific — carried to STRUCTURES as a mount-load input once a core is shortlisted |
| Envelope | **Not yet fixed — see Open Issues.** No station has been sited for the genset core anywhere in the airframe (corrected per STRUCTURES' AER-670 review — the boom-root CAD volume is sited for the propulsion motors, not this package); siting is the open item, not a missing dimension of an agreed location. | **Blocked on STRUCTURES siting decision** |
| Mass budget (engine + coupling + adapter, excl. generator/controller/cooling/BOS) | Per-core, §3 table | MFR/SOURCED per row |
| Fastener standard | Aviation-grade (AN/MS) fasteners at all structural joints; automotive-OEM fasteners retained only inboard of the adapter plate (engine's own internal hardware) | ASSUM |

**Shaft interface — PM generator on the crank/output-shaft nose.** The generator is coupled directly to the core's crank (or output shaft, for a motorcycle-class core) with **no belt reduction** — the generator's winding is selected so its rated/limiting speed matches the core's generator-duty operating RPM (§2). This deletes the belt-and-pulley reduction stage every prior MAOS-ICE Hayabusa combo priced (`COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md` §3 row 2, $1,500/12 kg for a 1.44:1 reduction), at the cost of constraining the generator winding choice to whatever speed the core actually turns at its rated operating point.

| Element | Spec | Tag |
|---|---|---|
| Coupling type | Torsionally-damped rigid or flexible disc coupling (motorsport/industrial-genset standard — avoids the backlash and maintenance burden of a chain/belt reduction, and there is no ratio to get wrong) | ASSUM |
| Torsional analysis | **Not performed in this draft.** A reciprocating IC engine's torque is pulsed (firing-order harmonics), not smooth like a turbine; the coupling and generator rotor must survive that torsional excitation at the generator's continuous torque rating without resonance in the operating RPM band. This is a named open item, not assumed benign. | **Open — needs a torsional/vibration analysis pass before any core is committed to hardware** |
| Overspeed/overtorque protection | Shear pin or slip-clutch element in the coupling, sized to the generator's continuous torque rating (protects the generator, not the engine, from a fault that drives RPM or load outside the operating envelope) | ASSUM |

### 2) Electrical Interface

- **Power source and bus:** the genset feeds the MAOS HV DC bus (DG-004). **Nominal voltage: ~700 Vdc (SYSTEMS conditional concurrence, AER-669, 2026-09-06 — conditions not yet closed, see Open Issues).** The earlier "~700–800 Vdc" figure conflated the proposed nominal with the BAMOCAR controller's 780–800 V overvoltage protection ceiling; that was a precision error, not a range.
- **Steady-state power budget:** genset electrical output target is the mission cruise-bus floor, currently carried in at **96 kW continuous** (ASSUM, traces to AER-68, itself traceable to the now-released 2,600 lb MTOW baseline — will re-derive).
- **Rectification/regulation:** engine-agnostic — whichever PM machine and controller are selected (§2.2 below) present a controlled DC output to the bus; this ICD does not specify a machine-agnostic rectifier because the machine candidates in §2.2 (EMRAX, H3X, Evolito) each pair with their own matched inverter/controller, not a generic rectifier bridge.
- **Connector and pinout reference:** TBD — deferred to the CAN/power-harness design once a machine is selected; not load-bearing for this ICD's engine-agnostic claim.
- **Grounding / shielding notes:** engine block and generator housing bonded to airframe ground independently (per the Viking-lesson independence principle in §5.5); HV cabling shielded per the existing EMRAX/BAMOCAR installation practice already documented in `COMBO3_CORRECTED_ELECTRIC_MACHINE_V1.md`.

#### 2.1 Generator machine matched to core speed

The design principle (per the issue's mandate): **choose the PM machine by the core's actual generator-duty operating RPM, not the reverse.** A 100 kW-class machine wound for 6,000–7,000 rpm is lighter than the same power class wound for 4,500 rpm, because winding count and mass scale with torque (P = τω), and torque, not power, is what drives copper/lamination mass. Deleting the reduction stage only pays off if the machine's rated speed is actually near the core's operating point — forcing a mismatched machine onto a core via a reduction defeats the point of this section.

| Candidate | Continuous rating | Rated/limiting speed | Mass | Torque class | Tag | Speed-match verdict |
|---|---|---|---|---|---|---|
| **EMRAX 268, MV winding, combined cooling** | 117 kW | 4,500 RPM (limiting speed for all windings) | 21.9 kg (motor only) | 250 Nm continuous | MFR (EMRAX 268 datasheet v1.6) | Matches a **motorcycle-class core throttled down** (Hayabusa Gen3's efficient generator-duty band is 5,000–7,000 rpm) only via a modest reduction (~1.1–1.4:1) — does not achieve the "belt deleted" goal on its own at Hayabusa's natural band, but is close enough that a very light single-stage step-up could be argued not to count as the "heavy belt reduction" this section is trying to delete. Direct match candidate for a **low-speed automotive-derived core** idled at ~4,500 rpm generator duty. |
| **EMRAX 228** | HV 55 kW / MV 64 kW / LV 75 kW (combined cooling) | Same family limiting-speed class as EMRAX 268 (~5,000 RPM class per datasheet family; exact 228 figure not re-pulled this pass) | ~20 kg class (EXTRAP — not re-sourced this pass, prior BOM entries priced it but did not carry mass) | Lower torque class than 268 | MFR/EXTRAP | Undersized for the 96 kW generator floor at every winding (best case 75 kW, 22% short) — **not a generator-role candidate at this mission's power level**; included per the issue's ask for completeness, and because it is already in the BOM as a motor-role machine (Combo 1). |
| **H3X HPDM-250** | 180 kW continuous confirmed (per PROPULSION's 2026-08-30 weekly watch pass), up to 250 kW peak | **Not confirmed for the -250 variant specifically.** The related HPDM-180R uses an integral 6.7:1 planetary gearbox bringing a ~20,000 RPM internal core down to a ~3,000 RPM external shaft. Whether HPDM-250 shares that gearbox/output-speed class or is a different (possibly higher-output-speed) design was **not found in this pass.** | 18.7 kg | Not sourced | MFR (power/mass) / **EXTRAP-then-unknown (speed)** | **Cannot score the speed-match claim without a vendor answer.** If HPDM-250 shares the HPDM-180R's ~3,000 RPM external interface, it's a clean near-direct match to a DeltaHawk-class low-speed core (2,600 RPM max, per `PROPULSION_CANDIDATE_MATRIX_V1.md`) but a poor match to any motorcycle- or automotive-turbo-class core without a step-down — the opposite mismatch direction from the belt-reduction problem this section is trying to solve. Named as a vendor question in §7. |
| **Evolito E800** | 110 kW continuous | **2,000 RPM** rated, 3,000 RPM transient | 28.3 kg (complete LRU incl. controls/inverter) | 800 Nm rated | MFR (per the 2026-08-30 catalog entry, sourced to Evolito's CAA type-certification filing for Electra's EL9) | Clean near-direct match to a **low-speed, high-displacement core** (DeltaHawk-class, 2,600 RPM max) — the same coupling advantage DHK235A4/HPDM-180R already have. **Poor match to any turbocharged motorcycle or 1.5–2.0 L automotive-turbo core**, all of which peak power well above 2,000 rpm; would require a step-up, reintroducing the reduction stage this section tries to delete. |
| **Automotive series-hybrid generator machine (representative: Toyota/Lexus Hybrid Synergy Drive "MG1" generator, e.g. Prius/Highlander/RX-family)** | **No manufacturer continuous rating found — these are not sold as standalone components and Toyota does not publish a fixed-RPM continuous duty spec.** Community reverse-engineering (openinverter.org and adjacent EV-conversion projects) documents peak figures in the 30–45 kW class depending on generation, but at *transient*, planetary-split, variable-RPM duty — not the fixed-RPM, fixed-load, hours-long duty this application needs. | Native operating range extends past 10,000 RPM (planetary e-CVT split, not a fixed generator point) | ~10–15 kg class (EXTRAP, community teardown reports) | Low (small rotor, high-speed design) | **SOURCED (community) / ASSUM (fitness for this duty)** | **Cannot be scored against the mission floor.** A single unit is almost certainly undersized (30–45 kW peak, unknown continuous) against the 96 kW floor even before the fixed-load-duty question is answered. Included because it is the most publicly documented "automotive series-hybrid generator" class available without a vendor quote; the honest finding is that **this class needs a manufacturer or tear-down-sourced continuous rating before it can be scored at all**, and on peak-power class alone it looks too small for a single-unit solution at this mission's floor. Named as a vendor/sourcing question in §7 — a fresh pull against Nissan e-POWER's or Honda i-MMD's generator-motor spec (not the ICE core) may find a larger unit, since those systems run larger displacement cores and correspondingly larger generator machines. |

**Reading this table honestly:** only **Evolito E800** (2,000 RPM) and, by family inference, **H3X HPDM-180R-class hardware** (~3,000 RPM) are confirmed matched to a *low-speed* core (DeltaHawk class). **None of the five candidates is a confirmed clean speed match to a Hayabusa-class motorcycle core's 5,000–7,000 rpm generator-duty band or to a 4,000–6,000 rpm automotive-turbo core** — EMRAX 268 (4,500 RPM) is the closest, needing only a light step-up rather than the ~2:1–2.3:1 reduction a lower-speed machine would need. This is a genuine finding, not a gap in research effort: **the market's aviation-class high-power PM machines (H3X, Evolito) are being developed for turbine/low-speed-diesel-class cores (their design partners are DeltaHawk-, turboshaft-, and diesel-class programs), not motorcycle- or automotive-turbo-class cores** — the speed mismatch runs the other direction from what a Hayabusa/automotive-core program needs. EMRAX's motorsport heritage, by contrast, is native to the higher-RPM automotive/motorcycle band, which is exactly why it has been this catalog's working choice for the Hayabusa path to date, and is also the case where "delete the belt" comes closest to true without further vendor data.

**Vendor questions this table could not close (see §7 for the routed list):** H3X HPDM-250 native output speed and whether it shares the HPDM-180R integral gearbox; a manufacturer or credible teardown continuous rating for a Nissan e-POWER or Honda i-MMD generator machine (larger displacement core, likely a larger generator than the Toyota HSD family); EMRAX 228's exact mass (present in prior BOM cost lines but not re-verified against the datasheet this pass).

### 3) Candidate-core shortlist mapped onto the interface

Every ORG-003 credited-power figure below applies **Ruling 1's design-phase credit rule**: manufacturer continuous rating where published; otherwise **75% of documented rated crank output for the planned tune**, tagged ASSUM. This supersedes the withdrawn 50%-of-peak interim rule for design-phase sizing (endurance/sustained-boost/cooling risk stays FMEA-owned per SAFETY, not folded into this credit number).

| Core | Stock/tune rated output | ORG-003 credited power | Mass (bare/dressed) | Cost (new) | Cost (used/salvage) | Sourcing path | Interface-adaptation cost | Tag |
|---|---|---|---|---|---|---|---|---|
| **Turbo Hayabusa Gen3 (GSX-1300RR, turbo kit)** | 140 kW (stock N/A rating cited in this catalog's turbo-tune context) → per ORG-003's own worked example, credited at **105 kW** | 105 kW (75% of 140 kW) | ~55 kg bare + 10–15 kg aviation dress (cooling reroute, mounts, intake/exhaust) | $8,000 (used 1340cc + turbo kit + conversion, per `POWERTRAIN_TRADE_STUDY_50K_V1.md` §9.1 Scenario C) | Same figure — this line is already an all-used BOM | Motorcycle salvage market (abundant); turbo kit aftermarket (established Hayabusa-turbo ecosystem) | **Lowest of the shortlist** — an entire motorsport/homebuilt aftermarket-turbo-to-generator ecosystem already exists for this specific engine (`PROPULSION_CANDIDATE_MATRIX_V1.md` §5.2); belt reduction to EMRAX 268 (§2.1) already priced at $1,500/12 kg | SOURCED (mass/cost), ASSUM (credited power, per ORG-003 worked example) |
| **Viking 195T (Honda L15B7 1.5T core)** | 145 kW stock (per ORG-003's worked example) → credited **109 kW** | 109 kW (75% of 145 kW) | Not sourced this pass (Viking does not publish dry weight for the 195T on the pages reviewed; a sibling model, Viking 130, is 108 kg dry per `ENGINE_SELECTION_DOWNSELECT_V1.md`) — EXTRAP that 195T sits in a similar 100–120 kg class | $20,495 complete, ECU included (per `propulsion_reset.md` §5, citing Viking's own product page) | Not established — Viking sells complete units, not a salvage-common core; a bare Honda L15B7 could be sourced from wrecked-Civic salvage far cheaper, but then loses Viking's aviation dress/ECU/prop-speed-reduction work entirely | Viking direct purchase (quote-only per the reset brief's own outstanding-question list) or self-adapt a salvage Honda L15B7 | **Comes pre-adapted for aviation** (Viking's own bellhousing/mount/ECU work) — lowest integration-labor cost of the shortlist if bought complete, at the highest sourced unit price | SOURCED (rated output, price), EXTRAP (mass), ASSUM (credited power) |
| **Aeromomentum AM20T** | 260 hp / 194 kW peak (per `propulsion_reset.md` §5.2) → credited **145 kW** (75% of 194 kW) | 145 kW | 143 kg (per `propulsion_reset.md` §5.2) | $29.7k (per `propulsion_reset.md` §5.2) | Not established — Aeromomentum sells new units; no salvage market found | Aeromomentum direct purchase | Comes with Aeromomentum's own PSRU/mount design for a tractor/pusher prop installation, not a generator-duty bellhousing pattern — **adapting this specific model to the flywheel/bellhousing datum in §1 is unscoped work**, distinct from buying it for its originally intended direct-prop-drive role | SOURCED (mass/price/peak power, via the reset brief's citation trail), ASSUM (credited power) |
| **Automotive series-hybrid core — Li Auto 1.5T range extender** | 110 kW peak (per `propulsion_reset.md` §3, citing Li Auto's own launch materials), 40.5% peak thermal efficiency | **No stock "rated crank output for generator duty" distinct from the 110 kW peak was found** — applying the 75% rule to the only published figure gives **~83 kW ASSUM**, short of the 96 kW floor by ~14% at a single-unit-only reading. This may be conservative (a range-extender engine's peak *is* its generator-duty rating, since it has no other operating mode — unlike a Hayabusa's peak, which is a road-going transient figure) — flagged as a vendor question rather than resolved by assumption. | Not sourced | Not sourced (China-domestic-market vehicle; not sold as a standalone unit in the US) | **High — same "no standalone import channel" finding `POWERTRAIN_TRADE_STUDY_50K_V1.md` §9.6 already made for the general China-automotive-turbo class.** A genuine range-extender core (this and BYD/Nissan/Honda below) ships as a sealed, tuned generator package inside a vehicle not imported to the US; sourcing means parting out a non-US-market car or finding an unsurveyed industrial-genset OEM channel. | **Unscoped and likely large** — this class was designed from the factory to already do most of what §1's coupling exists to build (it already drives a generator at a near-fixed operating point), so if sourcing is solved, the coupling/control adaptation could be the *smallest* of the shortlist; but the sourcing problem itself is the largest | SOURCED (peak power, efficiency), ASSUM (credited power — flagged, not confident) |
| **Automotive series-hybrid core — BYD DM-i 1.5T** | Not independently sourced this pass beyond the reset brief's naming it as a search-space entry | — | — | — | — | Same China-domestic sourcing problem as Li Auto, likely worse (DM-i is a much higher-volume, more China-market-specific platform) | Unscoped | **Named, not evaluated — no published spec pulled this pass.** Vendor/spec question in §7. |
| **Automotive series-hybrid core — Nissan e-POWER 1.5 VC-Turbo** | Not independently sourced this pass | — | — | — | — | VC-Turbo (variable compression) is a globally-marketed Nissan/Infiniti engine family (not China-domestic-only) — plausibly the **most sourceable** of the automotive-series-hybrid rows if e-POWER-spec units or donor vehicles reach the US/import-friendly markets | Unscoped | **Named, not evaluated — no published spec pulled this pass.** Vendor/spec question in §7 — this is the automotive-series-hybrid row most likely to be actually sourceable and deserves the next research pass. |
| **Automotive series-hybrid core — Honda 2.0 Atkinson (i-MMD, e.g. Accord/CR-V Hybrid)** | 109 kW peak (per `propulsion_reset.md` §5.2, citing Honda's own two-motor-hybrid press materials), **naturally aspirated — no altitude compensation** | Sea-level credited **~82 kW** (75% of 109 kW) — but the reset brief already flags the FL180 altitude-lapse consequence explicitly: **"~60 kW at FL180"** for this specific engine, because it has no forced induction to hold power with altitude. This is the one core on this shortlist where the ORG-003 sea-level credit number is not the number that matters — the altitude-derated figure is. | Not sourced (a complete i-MMD assembly's dry mass was not pulled this pass) | Not sourced as a standalone part — sold inside the vehicle | **Most abundant salvage source on this entire shortlist** — the Accord/CR-V Hybrid i-MMD system is high-volume, US-market, and already salvage-abundant (per `propulsion_reset.md` §5.2's own characterization) | US domestic salvage yards / wrecked-hybrid parts sellers | Unscoped, but likely the cheapest sourcing problem of the automotive-series-hybrid rows — **disqualified on altitude performance, not sourcing, at this credited-power reading** | SOURCED (peak power, lapse note), ASSUM (sea-level credit) |

**Shortlist read, plainly:** at the ORG-003 credit rule, **Aeromomentum AM20T (145 kW) and Viking 195T (109 kW) clear the 96 kW cruise floor with the most margin and the least sourcing risk**, at $29.7k and $20.5k respectively, both new-only. **Turbo Hayabusa (105 kW, $8,000 used) clears the floor at the lowest cost**, carrying forward this catalog's standing evidence gap (no sustained-duty data — ORG-003 Ruling 1 keeps this a pre-flight bench gate, not a design-phase disqualifier). **The automotive-series-hybrid class is the most interesting on paper and the least evaluated in practice** — Li Auto's own peak figure barely credits to the floor and the sourcing channel for all four rows is either unproven (Li Auto, BYD) or unresearched this pass (Nissan, Honda); Nissan VC-Turbo is flagged as the next research target because it is the only row in that class sold in globally-distributed vehicles. Honda's i-MMD is disqualified specifically by its FL180 altitude lapse, not by cost or sourcing — the one core on this table where naturally-aspirated breathing, not evidence or price, is the limiting fact.

### 4) Fluid / Air Interface

**Coolant contract.**

The physics floor, computed from first principles rather than assumed, because no core on the shortlist has a published aviation-installed coolant-loop spec:

- At a representative ~100 kW-class continuous electrical output target and a turbocharged spark-ignition BSFC of ~300–310 g/kWh (the figure this catalog already uses for the Hayabusa/H2 class, `PROPULSION_CANDIDATE_MATRIX_V1.md`), fuel energy input at that output is **≈310–360 kW** (BSFC 300–310 g/kWh, gasoline LHV ≈43.5 MJ/kg → ≈3.3–3.75 kWh fuel-energy-in per kWh shaft-out, i.e. ~27–30% brake thermal efficiency). EXTRAP.
- Applying a standard SI-engine full-load heat balance (brake work ~28–30%, coolant ~28–30%, exhaust ~35–40%, radiation/accessory/charge-air losses ~5–8% — a commonly cited automotive/motorsport thermodynamics split, not core-specific data) gives **coolant heat rejection on the order of the shaft power itself: ≈90–110 kW for a 100 kW-class continuous electrical target.** EXTRAP — **this is a bound from an engine-class heat balance, not a measured number for any candidate core, and the bench dyno run (§6) is the item that actually closes it**, per SAFETY's own AER-62 cooling flag.
- Turbocharged cores add a **separate charge-air (intercooler) heat load**, not folded into the coolant number above — order-of-magnitude 15–25 kW for a modest boost tune, core- and boost-level-specific, **not sized in this draft** (named open item, §7).

| Parameter | Value | Tag |
|---|---|---|
| Coolant medium | Water/glycol (aviation/motorsport standard mix, e.g. 50/50 or per core manufacturer spec) | ASSUM |
| Heat to reject, coolant loop, 100% continuous duty at FL180 | **≈90–110 kW for a ~100 kW-class continuous core** (see derivation above); scales per-core with the credited power in §3 | EXTRAP |
| Heat to reject, charge-air cooler (turbo cores only) | **~15–25 kW, order-of-magnitude, not core-specific** | EXTRAP, flagged low-confidence |
| Coolant temperature limits | Core manufacturer's own spec where published (not found this pass for any shortlist core specifically); ASSUM ceiling ~105–110°C (automotive/motorsport SI-engine coolant standard) pending a per-core datasheet pull | ASSUM |
| Flow rate | Not sized this pass — depends on the core's own water-pump curve and the radiator's core selected once a candidate is down-selected | **Open** |
| Installed airflow at FL180 | **The central physics point this section exists to make explicit:** air density at FL180 (ISA, ~5,486 m) is ≈0.629 kg/m³, ~51% of sea-level density. A motorcycle radiator sized against road-speed ram air at sea-level density will be meaningfully undersized for the same mass-flow-based heat rejection at FL180's installed airflow, independent of any power-derate question. This is SAFETY's AER-62 cooling flag, restated quantitatively: the fix is a larger frontal/core area and/or forced (not passive ram) airflow, sized at the FL180 density point, not a bigger motorcycle radiator core. | EXTRAP (density figure is a standard-atmosphere calculation; the sizing consequence is this document's own reasoning) |

**Cooling package mass bound (physics floor, per [[cooling-flow]] tradecraft — bracket with two independent analogs rather than one unsourced guess):**

- **Best-case bound (bare radiator core only):** using the sourced Rotax 915iS aviation analog (27.3 kW/kg, bare core) → a 100 kW coolant load bounds to **≈3.7 kg core mass** — not a realistic installed BOM figure, but the floor.
- **Realistic bound (full installed system):** using the sourced homebuilder liquid-cooled-Lycoming-conversion analog (3.7 kW/kg, full system: radiator, pump, lines, coolant, mounts) → a 100 kW coolant load bounds to **≈27 kg installed**, before the charge-air cooler, oil cooler, and ducting/cooling-drag structure are added.
- **This document's working cooling-package mass allowance: ~30–40 kg** (full coolant loop + oil cooler; charge-air cooler for turbo cores adds an unsized delta, §7 open item), pending CFD/bench confirmation. This is **PROPULSION's own estimate**, ASSUM-tagged, not a vendor or measured figure.

**Structural asks this mass figure does not cover (per STRUCTURES' AER-670 review).** The 30–40 kg is component mass only; it does not price two structural asks that follow from the FL180 forced-airflow requirement above: (1) a skin cutout in the pod's aft structure sized for the cooling inlet — worth costing against the eventual pod pressurization boundary (v1.1) now, since framing the opening once is cheaper than retrofitting it after the pod becomes a pressure vessel; (2) a dedicated mount for the radiator/pump/lines — AER-69's mass-fraction structure estimate (§5) carries engine/generator/motor/battery mount groups only, with no cooling-package mount line yet. Both are named STRUCTURES open items, not resolved by this document — see Open Issues.

**Fuel, air and exhaust envelope.**

- **Fuel:** mogas (all shortlist candidates except the diesel-class DeltaHawk/turboshaft alternatives this ICD does not cover); fuel system interface (pump, rail pressure, return) is core-native and out of scope for this ICD beyond the airframe fuel-tank/line provisioning SYSTEMS owns.
- **Air (intake):** core-native intake, routed to an airframe-provided cold-air inlet sized for the core's rated mass airflow at FL180 density (not sized this pass — a follow-on item once a core is shortlisted).
- **Exhaust:** core-native exhaust manifold/turbo housing, routed to an airframe-provided exhaust exit; **exhaust heat (~35–40% of fuel energy input, per the heat-balance split above) is not recovered in this design** — it is dumped overboard, same as any piston GA installation. No exhaust heat-recovery function (e.g., turbocompounding) is scoped in this v0.

### 5) Software / Protocol Interface — CAN/control contract for fixed-operating-point generator duty

This section closes the open PROPULSION action item from `POWERTRAIN_TRADE_STUDY_50K_V1.md` §6 / AER-62: *"confirm ICE-FLT-001's fault-detection set actually covers turbocharged-engine-specific fault modes (overboost, detonation, boost-control runaway)."*

- **Transport:** CAN bus (native on a Teensy 4.1-class Speeduino build, per `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §3.3; requires a bridge for MegaSquirt MS3-Pro's proprietary protocol or an analog-signal bridge for SDS EM-6, which has no native CAN). **Wire format not yet committed — open per SYSTEMS' AER-669 review.** RPM, coolant temp, fuel pressure and MAP map directly onto existing canfix-spec parameter IDs (512–513, 548–549, 540–541, 542–543); this document should commit to CAN-FIX as the transport rather than the "MAOS internal message format" label carried in the prior draft. No CAN-FIX parameter yet covers the ICE-SYS-003 state machine or the turbo fault flags (overboost/detonation/boost-control-runaway) — needs a parameter-allocation ask on the pattern `RESERVE_DEGRADED_ANNUNCIATION_V1.md` used for IDs 570–571. See Open Issues.
- **Message schema:** ICE-SYS-002 (publish operating state each control cycle: RPM, MAP, coolant temp, fuel pressure, fault flags, minimum set).
- **Encoding / rate:** not fixed in this v0 — inherits whichever ECU's native broadcast rate is used (MS3-Pro: 50 Hz configurable) or a MAOS-defined rate for a Speeduino-native implementation.

#### 5.1 Fixed-operating-point generator duty state machine (ICE-SYS-003)

| State | Entry condition | ECU/engine behavior | MAOS bus behavior |
|---|---|---|---|
| **Startup** | Commanded start | ECU runs native crank/start sequence to idle; warm-up to minimum coolant temp before load acceptance | Bus does not accept generator load from this unit until warm-up complete and RPM/temp within run-envelope |
| **Run** | Warm-up complete, load commanded | ECU holds target RPM under closed-loop control against generator electrical load (the operating-point scheduler, ICE-SYS-004) | Bus receives rated generator output; MAOS logs RPM/MAP/coolant-temp/fault-flag telemetry each cycle |
| **Derate** | A detected fault (§5.2) that does not require immediate shutdown, or a MAOS-commanded load-shed | ECU reduces target RPM/load to a bounded safe operating point | Bus receives reduced generator output; battery buffer makes up the shortfall per the architecture's power-split |
| **Shutdown** | MAOS-commanded shutdown, or an ECU/MAOS-detected fault requiring immediate stop, or pilot-commanded | Fuel cut (MAOS cuts fuel-pump relay if the ECU does not respond to a soft command — per `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §7 ICE-FLT-002); for turbo cores, a forced cool-down period before full shutdown is preferred where achievable, but is not assumed available in a fault-driven emergency shutdown | Bus generator output drops to zero; battery buffer sustains bus per the reserve sizing (open item, not resolved here) |

#### 5.2 Telemetry and fault semantics (ICE-FLT-001 through 004), including turbocharger-specific fault modes

The generic fault set already in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §7 (overtemp, overspeed, low oil — ICE-FLT-001) is retained. This ICD adds the turbo-specific detection criteria that document flagged as missing:

| Fault mode | Requirement | Detection criterion (this document's proposal) | Response |
|---|---|---|---|
| **Overboost** | ICE-FLT-001 (extended) | Boost pressure exceeds the tune's target by a defined margin (ASSUM: +15% of target gauge boost) sustained beyond a debounce window (ASSUM: 500 ms, to reject transient spikes). **Telemetry point under review (AER-669):** canfix-spec's existing 572–573 "Upper Deck Pressure" parameter may be the more correct fault-criterion input than Manifold Absolute Pressure — not resolved in this revision, see Open Issues. | Derate: MAOS/ECU commands wastegate toward open / cuts boost-control duty cycle; if boost pressure does not recover within a bounded window, shutdown |
| **Detonation** | ICE-FLT-001 (extended) | Knock sensor (if fitted — not assumed present on every shortlist core) exceeds a calibrated threshold at the fixed generator-duty operating point; **where no knock sensor exists, this fault mode is undetectable and stays an open risk**, named plainly rather than assumed covered | Derate: retard ignition timing / reduce boost; if knock persists, shutdown. **Core-dependent — a knock-sensor-equipped core (most modern automotive-turbo cores) is preferred over one without (some motorcycle-derived builds) precisely because this fault mode is otherwise unmonitorable.** |
| **Boost-control runaway** | ICE-FLT-001 (extended) | Wastegate actuator commanded closed but MAP continues to rise beyond the overboost threshold above, or actuator position feedback (if fitted) disagrees with commanded position beyond a threshold | Immediate shutdown — this is the fault mode with the least graceful degradation path, since it indicates the boost-control loop itself has failed, not just an operating-point excursion |
| **Sensor loss (crank trigger, MAP, TPS, coolant temp)** | ICE-FLT-004 | Per `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §5.2's fallback chain (cam-only → fixed operating point → shutdown) — unchanged by this document, reproduced here for completeness since it is core-agnostic | Per the existing fallback chain |
| **Fault logging** | ICE-FLT-003 | Timestamped, SD card or MAOS logging node, both preferred | N/A |

**Honest boundary:** the detonation-detection criterion above is only as good as the core's own knock-sensor provision. This is now a **named selection criterion for any turbocharged core on the shortlist** (§3), not just a control-software question — a core without a knock sensor (or without one that survives the bellhousing-adapter conversion) is carrying an unmonitored fault mode, and that should weigh in the eventual core downselect alongside cost and mass.

### 6) Bench-rig outline and cost

Per ORG-003 Ruling 1: the continuous-duty derate is a **pre-flight evidence bar**, not a design-phase cap — this section outlines what closes that bar. **Not funded by this issue; Bill funds it when a candidate works on paper**, per the issue's own instruction.

**Test article:** whichever core is shortlisted for a first build, mounted to a dynamometer or resistive/battery-buffered load bank standing in for the generator electrical load, instrumented per SAFETY's AER-62 cooling-sizing flag (`POWERTRAIN_TRADE_STUDY_50K_V1.md` §5, folded in here as the bench-program's instrumentation requirement) and this document's turbo-fault criteria (§5.2).

| Item | Spec | Basis / cost | Tag |
|---|---|---|---|
| ECU/control | Speeduino on Teensy 4.1 | Phase 1 recommendation already scoped in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §6; ~$170–220/unit, multiple units buildable in parallel for redundant test cells | SOURCED |
| Load bank or dynamometer | Resistive load bank sized to the core's credited power (§3), or a proper dyno if load-bank heat rejection at the test site is impractical | Not priced this pass — a real quote depends on site and whether MANUFACTURING/a local dyno shop is used vs. a purpose-built bank; **named as an open costing item**, not guessed | **Open** |
| Instrumentation | Oil temperature, head/CHT-equivalent temperature, coolant temperature — logged continuously over the full run, not spot-checked at hour 1 (per SAFETY's explicit instruction); turbo-specific: boost pressure, wastegate duty cycle/position, knock sensor (if fitted) | Per SAFETY's AER-62 §1 cooling flag and this document's §5.2 fault criteria | SOURCED (requirement), not priced |
| Duration | 500+ hours at fixed generator-duty RPM/load — the figure this catalog has used consistently since `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §6 | SOURCED (prior program scoping) | — |
| Estimated cost | **Not priced in this draft.** A defensible number needs a dyno/load-bank site quote and fuel-burn-over-500-hours estimate (at the core's BSFC and credited power, fuel cost alone is on the order of $3,000–6,000 for a 100 kW-class core over 500 hours at commodity mogas prices — EXTRAP, not a full program budget) | EXTRAP (fuel-only slice), **rest of the program cost is an open item** | **Open — see §7** |

**What this bench program would decide, concretely:** whether the shortlisted core's credited power (§3) can be raised past the ORG-003 75%-of-rated ASSUM figure toward its manufacturer-rating-equivalent (if the endurance run demonstrates sustained full-rated output), or whether it reveals a thermal, detonation, or wear failure that caps the core below its ASSUM credit — the same two-sided outcome `POWERTRAIN_TRADE_STUDY_50K_V1.md` §7 already described for the Hayabusa path specifically, now stated as an engine-agnostic bench-program outcome.

---

## Timing and Determinism

- **End-to-end latency budget:** not fixed in this v0 — a fixed-RPM generator-duty control loop is far less latency-sensitive than a variable-throttle flight-critical control (the whole point of Fallback 2 in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §5.2), so this is a lower-priority open item than the fault-detection and cooling questions above.
- **Jitter budget:** not fixed.
- **Synchronization requirements:** CAN broadcast rate should be fast enough that a MAOS-side derate/shutdown command reaches the ECU within the fault-response windows named in §5.2 (500 ms debounce example) — needs a control-loop timing pass once a specific ECU/bridge combination is chosen.
- **Scheduler assumptions:** none beyond the state machine in §5.1.

---

## Fault Semantics and Safety Behavior

Reproduced/extended from §5.2 above per the ICD template's structure:

- **Fault detection criteria:** §5.2 table.
- **Fault annunciation signals:** CAN fault flags per ICE-FLT-001/003, consumed by FCS/logging and (per the severity classification already ruled in `ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` §1) by the crew alerting path for a Hazardous-classified clean/detected/commanded engine-out event.
- **Fail-operational behavior:** derate state (§5.1) — reduced generator output, battery buffer makes up the shortfall.
- **Fail-safe behavior:** shutdown state (§5.1) — fuel cut, battery buffer sustains bus per the (not-yet-resolved) reserve sizing.
- **Reversion mode and trigger logic:** none specified — a fixed-RPM genset that has derated or shut down is not expected to self-recover in flight; this is a design choice worth flagging, not an oversight (auto-restart of a degraded IC engine mid-flight is its own hazard).
- **Crew / operator alert expectations:** per SAFETY's existing severity ruling (Hazardous, declare emergency, divert) — unchanged by this document, which does not revisit the severity classification itself.

---

## Verification and Acceptance

| Requirement / Interface Clause | Verification Method | Evidence Artifact | Pass Criteria |
|---|---|---|---|
| Mechanical coupling survives generator continuous torque without resonance | Analysis (torsional/vibration study, §1) then bench test | Torsional analysis report + bench vibration data | No resonance peak within the operating RPM band at the generator's continuous torque rating |
| Coolant loop rejects 100% continuous heat load at FL180-representative installed airflow | Analysis (this document's §4 bound) then CFD (`maos-openfoam`) then bench/flight test | This ICD's heat-balance derivation; CFD case; bench thermal-soak data | Coolant temperature stays within the core manufacturer's limit at sustained full load, tested airflow representative of FL180 density |
| Fixed-operating-point control (ICE-SYS-003/004) holds target RPM under generator load | Bench test | Bench RPM/load trace over the 500-hour program | RPM holds within a defined band (not yet numerically specified) of target across the full load range and duration |
| Turbo fault detection (overboost, detonation, boost-control runaway) | Bench test, deliberately induced faults where safe to do so | Bench fault-injection log | Each fault mode detected and responded to per §5.2 within its response window |
| Endurance / sustained-duty evidence (ORG-003 pre-flight bar) | Bench test, 500+ hours | Bench thermal/mechanical trend data, full run | No thermal, detonation, or wear failure at the credited continuous power point |

- **SIL references:** none yet.
- **HIL references:** none yet.
- **Bench test references:** §6 of this document.
- **Regression suite linkage:** none yet — this is a hardware program, not software-only.

---

## Change Management

- **Backward compatibility policy:** the adapter plate (§1) is the only core-specific mechanical part by design; a core swap should not require re-deriving §§1–2, 4–6.
- **Versioning policy:** this is V0 — expect at least one revision once STRUCTURES returns an envelope and SYSTEMS closes DG-004.
- **Deprecation policy:** N/A at V0.
- **Required reviewers by domain:** SYSTEMS (bus voltage, CAN), STRUCTURES (mount datum/loads), SAFETY (FMEA lines), MANUFACTURING (buildability).

---

## Open Issues and Risks

| # | Issue | Owner | Action |
|---|---|---|---|
| 1 | DG-004: SYSTEMS has offered conditional concurrence at ~700 Vdc nominal (AER-669, 2026-09-06) but the conditions have not yet closed | SYSTEMS / PROPULSION | Track AER-669 to closure; this document carries ~700 Vdc nominal (ASSUM) pending that close |
| 2 | STRUCTURES has not sited a mount station for the genset core anywhere in the airframe — corrected from the prior "no dimensions found" framing per STRUCTURES' AER-670 review; the boom-root CAD envelope belongs to the propulsion motors, not this package. If the core ultimately sites at boom-root, the installed mass (≈126–223 kg per §3/§4, core+generator+cooling) is 2.1×–3.7× what that envelope's nacelle bracket was load-cased against (1,126 N·m ultimate, sized for two EMRAX-268 pancake motors), and a reciprocating core there would add two load cases not in that case today: vibration-isolated mount topology (rigid-mount was assumed) and a fire zone/firewall requirement (none needed for an electric-only nacelle) | STRUCTURES (blocked on AER-608's architecture pick; STRUCTURES' own AER-69 stays correctly blocked on the same) | This ICD specifies a mounting *pattern*, not a location, until siting lands; the mass/load-case mismatch above is carried forward for the next AER-69 revision |
| 3 | Torsional/vibration analysis of the direct-coupled generator shaft not performed; deleting the belt reduction (vs. AER-69 v2's ~1.44:1 belt-reduction assumption) removes belt-tension mount loads but puts the full pulsed reciprocating-engine torque directly into the coupling with no belt-slip damping | PROPULSION / STRUCTURES, joint | Named as a pre-hardware-commitment gate in §1; this is also the analysis that sizes the coupling/generator-mount fatigue case, per STRUCTURES' AER-670 review |
| 11 | Cooling package's ~30–40 kg allowance (§4) is component mass only — it does not price a pod-skin inlet cutout (worth sizing against the eventual v1.1 pressurization boundary now) or a dedicated structural mount for the radiator/pump/lines (AER-69 §5's mass-fraction ledger has no cooling-package mount line today) | PROPULSION / STRUCTURES, joint | Named per STRUCTURES' AER-670 review; needs a cutout size and mount-load estimate once a core/cooling-package geometry is shortlisted |
| 12 | CAN transport not committed to CAN-FIX; no CAN-FIX parameter allocated for the ICE-SYS-003 state machine or the turbo fault flags (overboost/detonation/boost-control-runaway); canfix-spec's 572–573 "Upper Deck Pressure" may be the more correct Overboost telemetry point than MAP | SYSTEMS / PROPULSION | Named per SYSTEMS' AER-669 review; needs a parameter-allocation ask on the `RESERVE_DEGRADED_ANNUNCIATION_V1.md` (IDs 570–571) pattern |
| 4 | Charge-air (intercooler) heat rejection not sized for any turbo candidate | PROPULSION | Order-of-magnitude only (§4); needs a boost-tune-specific pass once a core is shortlisted |
| 5 | H3X HPDM-250's native output speed (vs. the HPDM-180R's known 3,000 RPM/6.7:1-gearbox figure) — unconfirmed | Vendor (H3X) | Email/quote request — same outstanding-vendor-contact class as the Evolito/ProLogium/Viking questions already on the propulsion_reset brief's list |
| 6 | No manufacturer or credible teardown continuous rating found for any automotive-series-hybrid generator *machine* (as opposed to its ICE core) | Vendor / community sourcing | Named in §2.1; Nissan e-POWER and Honda i-MMD flagged as the more promising research targets than Toyota HSD (which is confirmed too small) |
| 7 | Nissan e-POWER VC-Turbo and BYD DM-i 1.5T core specs not independently pulled this pass | PROPULSION (weekly watch) | Add to the next weekly market-watch pass — Nissan flagged as the most sourceable of the automotive-series-hybrid rows |
| 8 | Bench-rig cost not fully priced — only a fuel-cost slice is estimated | PROPULSION | Needs a dyno/load-bank site quote before Bill can fund the program |
| 9 | Detonation detection is unmonitorable on any core without a knock sensor | PROPULSION (core downselect criterion) | Named as a selection criterion in §5.2, not resolved by this document |
| 10 | Coolant temperature limits and flow rate not sourced for any shortlist core specifically | PROPULSION | Needs a per-core datasheet pull once a candidate is down-selected |

## Approvals

- **Engineering owner:** PROPULSION (draft, this document)
- **Safety reviewer:** SAFETY — requested, not yet reviewed
- **Integration reviewer:** SYSTEMS, STRUCTURES — requested, not yet reviewed
- **Date:** 2026-09-05 (V0 draft)

---

*Version 0 — 2026-09-05. Initial engine-agnostic genset package ICD per AER-609: mechanical coupling/mounting pattern (§1), generator-machine-to-core-speed matching across EMRAX 268/228, H3X HPDM-250, Evolito E800, and an automotive-series-hybrid generator candidate (§2.1), a seven-core shortlist mapped onto the interface with ORG-003 credited power (§3), a first-principles coolant/charge-air heat-rejection bound using the two-analog cooling-mass method (§4), the CAN/control state machine and turbo-specific fault semantics closing the open ICE-FLT-001 action item from AER-62 (§5), and a bench-rig outline with an unpriced cost gap named rather than guessed (§6). No core is recommended — this document is interface-first per the issue's own rule, and does not rank the shortlist beyond noting which rows clear the mission floor at the least sourcing risk.*

*Version 0.1 — 2026-09-06. Corrections from the requested SYSTEMS ([AER-669](/AER/issues/AER-669)) and STRUCTURES ([AER-670](/AER/issues/AER-670)) reviews: DG-004 updated from an unresolved ~700–800 Vdc range to SYSTEMS' conditional ~700 Vdc nominal concurrence (the 780–800 V figure was the BAMOCAR overvoltage ceiling, not a nominal-range bound); the mount-datum row corrected from an overstated "AER-69 v2 places the assembly at boom root" claim to the accurate state — no station has been sited for the genset core, and the boom-root CAD volume belongs to the propulsion motors; the resulting mass/load-case mismatch (§ Open Issues #2), the coupling fatigue joint-ownership with STRUCTURES (#3), a cooling-package structural-mount and inlet-cutout gap (#11), and a CAN-FIX transport/parameter-allocation gap (#12) are added as open items. Neither review is a full close — DG-004's conditions and STRUCTURES' siting decision remain open.*
