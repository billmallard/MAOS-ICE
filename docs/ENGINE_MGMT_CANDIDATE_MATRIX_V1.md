# Engine Management System — Candidate Matrix V1

**Status:** Research / Preliminary — Experimental Amateur-Built Category  
**Date:** 2026-04-20  
**Scope:** Hayabusa engine management candidates for generator-duty operation in the MAOS series-hybrid architecture (Paths H1–H4 in `PROPULSION_CANDIDATE_MATRIX_V1.md`)

---

## 1. Safety Classification Context

The standard aircraft-EFI safety argument — "ECU failure = engine stops = loss of thrust = emergency" — **does not apply directly to MAOS**. The Hayabusa in Paths H1–H4 drives a generator; it is not directly coupled to the propeller. The propulsion motor is driven electrically from the DC bus.

This changes the fault consequence chain:

```
ECU failure → engine stops → generator output drops → battery buffer sustains bus
           → 8–12 min full-power flight window available (15–25 kWh buffer per PROP_MATRIX_V1)
           → commanded descent and landing, not emergency
```

This does **not** make ECU failure acceptable — it must be detected (ICE-FLT-001), logged (ICE-FLT-003), and responded to via the MAOS derate/shutdown state machine (ICE-SYS-003). But it **does** mean:

- A non-redundant ECU is a lower-severity single point of failure than in a direct-drive aircraft
- Graceful degradation (derate rather than hard stop) is more achievable and more valuable than immediate redundancy
- The ECU is **not required to be aviation-certified** for the Experimental Amateur-Built category
- The primary gate for engine management is **integration maturity and telemetry quality**, not type certification

---

## 2. Selection Criteria

Criteria are weighted for generator-duty operation in a series-hybrid. Weights differ from a conventional aircraft installation.

| Criterion | Weight | Rationale |
|---|---|---|
| CAN bus / telemetry integration | 25% | ICE-IF-005 requires telemetry to FCS/logging each control cycle; CAN is the MAOS bus standard |
| Proven reliability at sustained load | 20% | Generator duty = near-constant RPM/MAP for hours; different stress profile than variable-throttle automotive |
| Tunability for constant-speed operation | 15% | Generator operating point is fixed; tune complexity is low but control authority over RPM/load matters |
| Fault detection and reporting | 15% | ICE-FLT-001 through 004; ECU must report sensor faults, not just fail silently |
| Open architecture / integration flexibility | 15% | MAOS requires custom startup/run/derate/shutdown state machine; ECU must be commandable or wrappable |
| Acquisition cost | 10% | Prototyping cost is a real constraint at this project stage |

---

## 3. Candidates

### 3.1 MegaSquirt MS3-Pro

**Source:** Bowling & Grippo / DIYAutoTune  
**URL:** https://www.msextra.com/

**Overview:**  
The MS3-Pro is the top-tier MegaSquirt variant, featuring a 100 MHz ARM Cortex-M4 MCU, full sequential injection and ignition for up to 8 cylinders, and onboard CAN. It is the de-facto standard for high-performance motorcycle engine conversions in motorsport and is the most common EFI platform in the Hayabusa aftermarket community.

**Specification summary:**

| Parameter | Value |
|---|---|
| MCU | 100 MHz ARM Cortex-M4 |
| Injection channels | Up to 12 sequential |
| Ignition outputs | Up to 8 coil-on-plug |
| Analog inputs | 12 configurable |
| Onboard MAP/baro sensors | Yes |
| CAN bus | Yes — proprietary protocol, 50 Hz broadcast |
| SD card logging | Yes |
| Boost control | Yes (PWM output) — required for turbo Hayabusa |
| Approximate cost | $600–$900 USD |
| Source model | Closed firmware, open communication protocol spec |

**Hayabusa community experience:**  
Active. Documented Hayabusa builds in MSEXTRA forum (e.g., `viewtopic.php?t=73018`). Turbo Hayabusa tuning is well-supported. Throttle body mapping and crank trigger setup are established. No aircraft-specific Hayabusa builds documented, but tuning data is transferable.

**CAN integration notes:**  
MS3 broadcasts ECU data at 50 Hz on configurable CAN IDs. The protocol is proprietary (not DroneCAN/UAVCAN/J1939). A MAOS CAN bridge will be required to translate MS3 broadcast frames into MAOS internal message format. The MS3 CAN spec is published and parseable. Estimated bridge implementation: medium complexity.

**Strengths for MAOS:**
- Most Hayabusa-specific tuning knowledge in the community
- Boost control output covers turbo path
- SD logging supports endurance test campaign data capture
- CAN output satisfies ICE-IF-005 with bridge

**Weaknesses:**
- Proprietary CAN protocol requires custom bridge
- No native dual-sensor redundancy architecture
- Not designed for safety-critical systems (manufacturer disclaimer)
- External watchdog required for ICE-FLT-001 compliance

---

### 3.2 SDS EFI EM-6

**Source:** Simple Digital Systems  
**URL:** http://www.sdsefi.com/aircraft.html

**Overview:**  
The EM-6 is a purpose-built aviation EFI system with a 20+ year track record in Experimental Amateur-Built aircraft. It uses batch-fire (grouped) injection rather than sequential, emphasizing simplicity and reliability over tuning flexibility. As of research date: 1,700+ aviation units shipped, 475,000+ flight hours accumulated, three Reno Sport Class gold wins (2010+).

**Specification summary:**

| Parameter | Value |
|---|---|
| Injection type | Batch-fire (grouped by bank) |
| Ignition | Direct-fire capable (variant dependent) |
| Cylinders supported | 4, 6, 8 (4D, 6D, 8D variants) |
| Tuning interface | Proprietary LCD programmer; no laptop required |
| CAN bus | **None native** |
| Analog output | RPM, MAP, EGT signals available on analog pins |
| Redundancy architecture | **Dual-ECU capable** — two EM-6 units can be wired for primary/backup switching |
| Approximate cost | $1,125–$1,242 USD (4D variant) |
| Source model | Closed source / proprietary |

**Aviation track record:**  
Best in class for Experimental Amateur-Built aircraft. Routinely installed in RV-series, Bearhawk, and custom conversions. The dual-ECU architecture (primary/backup with manual or automatic failover) is the closest any of these candidates comes to aviation-grade redundancy without a full FADEC.

**CAN integration notes:**  
No CAN bus. Integration with MAOS ICE-IF-005 would require an intermediate microcontroller reading analog outputs (RPM pulse, MAP voltage, EGT thermocouple) and publishing to the MAOS CAN bus. This is achievable but adds a translation layer, adds a potential failure point, and means MAOS only sees derived data — not raw ECU health state.

**Strengths for MAOS:**
- Highest demonstrated reliability in aircraft context — 475,000+ flight hours
- Dual-ECU configuration provides genuine fault tolerance
- Batch-fire acceptable for constant-speed generator duty (identical fuel delivery to sequential at fixed operating point)
- Proven in extreme conditions (Reno air racing)

**Weaknesses:**
- No CAN bus — requires analog bridge for MAOS integration
- No open architecture — cannot inject MAOS derate commands into ECU; state machine must act on throttle servo or fuel pump relay externally
- No SD logging — test campaign data capture requires external instrumentation
- No boost control output — turbo Hayabusa (Configs B/C) requires separate boost controller

---

### 3.3 Speeduino

**Source:** Open-source community project  
**URL:** https://speeduino.com / https://github.com/speeduino/speeduino

**Overview:**  
Speeduino is a fully open-source EFI controller based on the Arduino Mega 2560 (or Teensy 4.1 for CAN-capable builds). Firmware, hardware schematics (KiCad, CERN OHL v2), and documentation are all publicly available. It uses TunerStudio as its tuning interface — the same software used by MegaSquirt — and implements a comparable feature set at roughly one-third the cost.

**Specification summary:**

| Parameter | Value |
|---|---|
| MCU | Arduino Mega 2560 (base) or Teensy 4.1 (CAN builds) |
| Injection channels | Up to 4 fully sequential (4-cyl) |
| Ignition outputs | Up to 4 coil-on-plug |
| Analog inputs | Configurable |
| CAN bus | **Yes** — native on Teensy builds; MCP2515 "Beetle" expansion board for Mega builds |
| CAN protocol | Configurable; can implement custom broadcast format |
| SD card logging | Via TunerStudio or expansion |
| Boost control | Yes (PWM output) |
| Approximate cost | $170–$220 USD (kit/PCB) |
| Source model | **Fully open source** — firmware (GPL), hardware (CERN OHL v2) |

**Aviation track record:**  
Minimal. Community discussion exists (HomebuiltAirplanes.com forum threads) but no documented flight hours in experimental aircraft as of 2026-04. This is the primary risk vs. MegaSquirt and SDS.

**CAN integration notes:**  
Speeduino on Teensy 4.1 supports native CAN. The broadcast protocol is configurable in firmware — a MAOS-specific CAN message layout can be implemented directly without a bridge. The open firmware also enables custom handling of MAOS derate/shutdown commands, making it the most integrable option at the firmware level. This is architecturally superior to the other candidates for MAOS-ICE purposes.

**Strengths for MAOS:**
- Fully open source — can implement MAOS-native CAN messages, state machine integration, and fault reporting directly in firmware
- Lowest cost — relevant for bench test campaign (multiple units) and iteration
- Native CAN on Teensy 4.1 satisfies ICE-IF-005 without a bridge
- Full sequential injection and ignition for 4-cyl Hayabusa
- TunerStudio compatibility means community tuning profiles are transferable from MegaSquirt

**Weaknesses:**
- **No aircraft track record** — no flight hours, no established experimental aviation precedent
- Arduino/Teensy MCU is commodity hardware, not hardened for vibration or temperature extremes
- Community is smaller and younger than MegaSquirt; Hayabusa-specific tuning profiles less developed
- No manufacturer support — issues resolved via GitHub and forum only
- Requires more integration effort for a flight vehicle (hardening, testing, documentation)

---

## 4. Comparison Matrix

| Criterion | Weight | MS3-Pro | SDS EM-6 | Speeduino |
|---|---|---|---|---|
| CAN / telemetry integration | 25% | 3 — CAN present but proprietary bridge needed | 1 — no CAN; analog bridge only | **5** — native CAN, fully configurable protocol |
| Proven reliability at sustained load | 20% | 3 — motorsports proven, no aviation hours | **5** — 475,000+ flight hours | 1 — no documented flight hours |
| Tunability for constant-speed operation | 15% | 4 — strong community, Hayabusa profiles | 3 — batch-fire adequate, less flexible | 4 — TunerStudio compatible, fully tunable |
| Fault detection and reporting | 15% | 3 — sensor faults logged, no watchdog | 3 — dual-ECU failover, no CAN health reporting | 3 — open firmware enables custom fault handling |
| Open architecture / integration flexibility | 15% | 2 — closed firmware, CAN spec published | 1 — closed, no command interface | **5** — fully open, MAOS commands implementable |
| Acquisition cost | 10% | 3 — $600–$900 | 2 — $1,125–$1,242 | **5** — $170–$220 |
| **Weighted score** | | **2.85** | **2.85** | **3.55** |

*Scores 1–5 per criterion; weighted score = sum(weight × score).*

---

## 5. ECU Redundancy Architecture

True dual-lane redundancy (Rotax-style — independent injectors, spark plugs, sensors, and processors per cylinder) is not achievable on the Hayabusa without modifications that are not practically available: a second fuel rail and second spark plug per cylinder each require significant engine rework. This section documents what redundancy *is* achievable and the residual risks that remain.

### 5.1 ECU Warm-Standby Failover

A warm-standby architecture covers ECU processor failure without requiring engine hardware modification. Both ECUs are powered and processing live sensor data simultaneously. Only the primary ECU's outputs are connected to injectors and coils; output switching is controlled by a hardware watchdog relay, not software.

```
Sensors ──┬──► Primary ECU ──► Watchdog pulse ──► Solid-state relay ──► Injectors / Coils
          │                         │
          └──► Backup ECU  ◄────────┘ (monitoring; outputs held off)
                                         relay trips if pulse stops → backup outputs connect
```

**Switchover trigger:** Hardware watchdog chip (not software) gates the output relay. Primary ECU pulses watchdog at 10 Hz. No pulse within ~150 ms → relay switches to backup ECU outputs. Switchover gap at constant generator RPM is survivable — the engine is at steady state and does not require rapid re-synchronisation.

**Independence requirements (Viking ECU lesson applied):**  
Viking Aircraft Engines implemented a dual-ECU system on their Honda conversions but shared power conditioning between units and provided no true output isolation. Community experience reported persistent failures and multiple ECU design revisions over several years, with some operators disabling the dual-ECU entirely. The failure mode was architectural, not component-level.

To avoid this failure pattern, both ECUs in the MAOS warm-standby must be independent in three specific ways:

| Element | Requirement |
|---|---|
| Power feed | Each ECU from a different bus node; independent fuses |
| Ground | Separate ground return paths to airframe |
| Output path | Solid-state relay on injector/coil side; no shared output wiring upstream of relay |

**What this covers:** ECU processor failure, firmware crash, board hardware fault, primary power supply failure  
**What this does not cover:** Sensor failures (crank trigger, MAP, TPS), injector/coil wiring faults, fuel pump failure

**Cost (Speeduino implementation):** ~$440 for two units + ~$30 solid-state relay

---

### 5.2 Sensor Fallback — Crank Trigger Failure

The residual risk in the warm-standby architecture is shared sensor inputs. A crank trigger failure — broken reluctor wheel, failed magnetic pickup, connector fault — affects both ECUs simultaneously. This section defines the limp-mode response.

The Hayabusa Gen3 has two independent position sensors:
- **Crank trigger:** 36-1 reluctor wheel + magnetic pickup; provides high-resolution RPM and position
- **Cam position sensor:** VVT cam sensor; fires once per 720° (one pulse per complete cycle); physically separate location and connector from crank trigger

These are on opposite ends of the engine. A failure mode that simultaneously disables both sensors requires a common-cause event (wiring harness destruction, severe mechanical failure) that likely signals a broader engine failure anyway.

**Fallback chain:**

```
Normal:      Crank 36-1 + cam sync  →  full sequential injection + coil-on-plug ignition
Fallback 1:  Cam sensor only        →  batch-fire injection + wasted spark; degraded, engine continues
Fallback 2:  No position signal     →  fixed operating point, open-loop (generator-duty specific)
Fallback 3:  Engine stops           →  battery buffer, survivable emergency, ordered descent
```

**Fallback 1 — Cam-only operation:**  
MS3-Pro and Speeduino both support cam-only operation. The ECU switches to batch-fire injection (all cylinders simultaneously) and wasted-spark ignition (each coil fires twice per revolution — once useful, once on the exhaust stroke). Efficiency drops and the engine runs rough, but it continues to produce power. At a fixed generator operating point this is sufficient to sustain reduced electrical output while the pilot executes a descent.

**Fallback 2 — Fixed operating point:**  
This fallback is only viable because of the generator-duty application. A variable-throttle aircraft engine cannot use it: if RPM is unknown, the fuel map is wrong at every point. For a generator held at a target RPM (e.g., 6,000 RPM) under electrical load, the ECU can enter an open-loop fixed mode: assume target RPM, apply fixed ignition advance and fixed injector duty cycle appropriate for that operating point. The generator load physically tends to hold RPM near the target. Engine power degrades but the generator continues producing.

This fallback must be explicitly programmed, bench-tested, and documented. It is not a default ECU behaviour in any of the three candidates; it requires custom implementation in the ECU firmware (straightforward in Speeduino; requires configuration table in MS3-Pro).

**Residual risk of Fallback 2:**  
The fixed operating point assumption breaks if something else is also wrong — fuel pressure drop, mechanical fault, load spike. In that scenario the engine stops and Fallback 3 applies. This is the honest boundary of the limp-mode chain.

**Requirement implication:**  
ICE-FLT-004 ("sensor loss shall not cause undefined controller outputs") explicitly covers this. The fallback chain above constitutes the defined behaviour required by that requirement. Each transition must be tested on the bench before any flight.

---

### 5.3 Lessons from Viking Aircraft Engines — ECU Failure Patterns

Viking Aircraft Engines (Edgewater, FL) has produced Honda-based aircraft engines for the Experimental Amateur-Built market since the early 2010s. Their dual-ECU implementation on the Honda L-series conversions provides a documented case study in what goes wrong when automotive ECU redundancy is adapted for aircraft use. The Honda engine itself has a strong reliability record in service; the ECU integration did not. Viking went through multiple ECU revisions and persistent community-reported issues before stabilising.

The following failure modes are drawn from forum records (Van's Air Force, Pilots of America), Viking service bulletins, and third-party documentation:

| Failure Mode | Root Cause | MAOS-ICE Design Response |
|---|---|---|
| Dual ECU did not provide redundancy | ECUs shared a common voltage regulator and power entry point; power supply failure killed both simultaneously | Each ECU fed from a different bus node; independent fuse; no shared regulator |
| ECU select switch caused intermittent faults | Mechanical switch became the single point of failure; multiple switch-induced dropouts with zero actual ECU failures | Output switching via solid-state relay triggered by hardware watchdog, not a pilot-operated or software-operated selector |
| Coil/injector short killed entire ignition bus | No per-output current protection; a single shorted coil propagated back to the ECU output rail | Individual fusing on each coil and injector output; fault on one cylinder drops that cylinder, not the ECU |
| Software cold-start failures persisted across multiple revisions | Limited field exposure at time of release; at least 4 ECU firmware iterations, mandatory reflash required before flight for pre-2018 software | Choose ECU with large established installed base; prioritise bench test hours before flight |
| Installer wiring damage burned ECUs | No polarity protection or physical constraints on the power entry wiring; incorrect installation destroyed hardware | Keyed connectors, polarity protection diode at ECU power input, explicit installer documentation — integration task for MAOS harness design regardless of ECU chosen |

**Summary of the Viking pattern:**  
Every failure mode above is architectural, not component-level. The individual ECU hardware and the Honda engine performed acceptably. The failure points were the system boundaries: power supply, output switching, harness protection, and field preparation. These are exactly the design elements that fall to MAOS to specify — not to the ECU vendor.

The Viking lessons reinforce the warm-standby design principles in Section 5.1 and the harness design requirements that apply to all three ECU candidates.

---

## 6. Phased Recommendation

The three candidates serve different phases of the program:

### Phase 1 — Bench / Endurance Test Campaign

**Recommended: Speeduino (Teensy 4.1)**

The endurance campaign is the primary technical risk gate for the Hayabusa path. It requires sustained-load logging, CAN telemetry to test instrumentation, and the ability to iterate the control calibration rapidly. Speeduino's open firmware, native CAN, and low cost make it the right tool for this phase. Multiple units can be built for parallel test cells. If a unit fails during bench testing, the cost is $200 and a GitHub issue, not a $1,000 replacement.

The endurance test should also serve as a reliability data collection exercise for Speeduino itself. 500+ hours at generator load on Speeduino generates flight-hour-equivalent data.

### Phase 2 — First Flight Vehicle

**Recommended: MegaSquirt MS3-Pro**

If Speeduino accumulates insufficient reliability evidence, or if the program timeline requires a known-quantity EFI, MS3-Pro is the transition path. The Hayabusa community knowledge is highest here, boost control is built in, and the CAN bridge implementation is bounded work. It remains the de-facto standard for high-performance motorcycle engine conversions.

### Phase 3 — Production / Refined Build

**Recommended: Re-evaluate based on bench evidence**

If Speeduino demonstrates strong bench reliability, the open-firmware integration advantage may justify it through to flight. If the program prioritizes demonstrated aviation flight hours, SDS EM-6 in a dual-ECU configuration is the credible option — despite its integration limitations, its track record is unmatched.

Alternatively, by the time MAOS reaches a production-intent build, the Kawasaki Aero FADEC engine (Path D, ~2030) may be available and renders this decision moot for that path.

---

## 7. Integration Requirements (All Candidates)

Regardless of ECU selection, the following are required by MAOS-ICE requirements and architecture:

| Requirement | Source | Notes |
|---|---|---|
| Publish operating state each control cycle | ICE-SYS-002 | CAN bridge or native CAN message; minimum: RPM, MAP, coolant temp, fuel pressure, fault flags |
| Startup / run / derate / shutdown states | ICE-SYS-003 | ECU controls fuel/ignition; MAOS state machine controls throttle position via servo or ECU command |
| Operating-point scheduler | ICE-SYS-004 | Generator load command → throttle position → ECU holds RPM via closed-loop control |
| Detect overtemp, overspeed, low oil | ICE-FLT-001 | ECU sensors + MAOS monitoring; ECU fault flags must be CAN-accessible |
| Degraded operation / commanded shutdown | ICE-FLT-002 | MAOS sends derate/shutdown command; ECU must respond or MAOS cuts fuel pump relay |
| Fault logging with timestamp | ICE-FLT-003 | SD card on ECU or MAOS logging node; both preferred |
| Sensor loss shall not cause undefined outputs | ICE-FLT-004 | ECU limp-home behavior must be characterized and tested; default to safe RPM or shutdown |

---

## 8. Open Questions

- [ ] Can Speeduino Teensy 4.1 sustain 500+ hours continuous operation in a vibration/temperature environment representative of an engine bay? No published data found.
- [ ] What is the MS3-Pro CAN bridge implementation effort for MAOS message format? Estimate: 1–2 weeks engineering.
- [ ] Does the Hayabusa Gen3 stock crank trigger wheel work with all three ECUs, or does it require modification? (Gen3 uses a 36-1 wheel + cam sensor — standard; should be compatible with all candidates.)
- [ ] SDS EM-6 dual-ECU failover: is failover automatic (output relay) or manual pilot action? Manual switchover is unacceptable for a generator application; automatic relay switching requires verification.
- [ ] Is boost control via the Speeduino PWM output sufficient for the turbo Hayabusa target boost levels (~0.5–1.0 bar), or is a dedicated boost controller required?

---

## 9. References

| Source | Notes |
|---|---|
| PROPULSION_CANDIDATE_MATRIX_V1.md | Hayabusa engine specs, Config B/C/H1-H4 architecture, sustained-duty risk identification |
| https://www.msextra.com/ | MegaSquirt MS3-Pro product specs and community documentation |
| http://www.sdsefi.com/aircraft.html | SDS EM-6 aviation track record and specification |
| https://speeduino.com | Speeduino project overview |
| https://github.com/speeduino/speeduino | Speeduino firmware (GPL), hardware schematics (CERN OHL v2) |
| https://wiki.speeduino.com/en/Canbus_Support2 | Speeduino CAN bus implementation details |
| MSEXTRA forum t=73018 | Hayabusa MS3 build thread — sensor wiring and crank trigger reference |
| https://vansairforce.net/threads/viking.133200/ | Van's Air Force — Viking ECU community discussion, dual-ECU failure patterns |
| https://vansairforce.net/threads/viking-110-ecu.225052/ | Van's Air Force — Viking 110 ECU wiring and single-point-of-failure analysis |
| https://sites.google.com/site/vikingaircraftengineissues/ | Viking Aircraft Engine Issues — third-party documentation of ECU revision history |
| https://www.vikingaircraftengines.com/service-bulletins-1 | Viking service bulletins — mandatory ECU software update history |
