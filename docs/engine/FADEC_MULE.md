# A FADEC flight mule on a bought conversion: the engine, the FADEC swap, and the airframe question

Owner: PROPULSION. Issue: AER-3631, which follows AER-3525. Date: 2026-10-21.

Status: analysis only. Nothing has been bought, quoted (AER-3330), built, run or flown. On 2026-10-21 Bill accepted the AER-3525 card: drop the Hayabusa, and fly the program's FADEC on a bought conversion instead (HAYABUSA_PLATFORM.md section 12). This document picks the engine, plans the FADEC substitution and states the airframe options. It decides no airframe: that choice is Bill's, and is on AER-3631 as one card. This is an experimental engine program. Nothing in it is certified, certifiable or flight-ready.

Numbers come from [`analysis/engine_mule/mule.py`](../../analysis/engine_mule/mule.py) (tables in `mule_tables.md` beside it). Tags: **[S]** vendor or official source, **[F]** forum, listing or secondary, **[E]** PROPULSION estimate with its method in the script, **[A]** assumed, **[nf]** not found. Source keys (AMn, VKn, OTn for engines; AFn, FAAn for airframes and rules) are in [`sources/FADEC_MULE_SOURCES_2026-10-21.md`](sources/FADEC_MULE_SOURCES_2026-10-21.md). **None of the costs is a quote.**

## 1. The answer

**The engine: the Aeromomentum AM15.** The AM13 is the cheaper fallback on the same engine family. The Viking 130 is the wrong mule.

- **The AM15 is the easiest engine for an open two-lane ECU to take over.** It is port-injected, its stock ECU is a MicroSquirt [S AM9], and its ignition takes logic-level inputs. The program's ECU can drive its injectors and coils directly.
- **The Viking 130 is direct-injected** (a Honda Fit L15, not a Mitsubishi [S VK1, VK3]). That needs a 65 V peak-and-hold injector stage and control of a high-pressure pump, which no open ECU in the program's set drives. Haltech does not support that engine at all [S OT4]. Its ECU is closed, and Viking has password-locked an owner's retune [F VK18].
- **The AM15 is the cheapest per horsepower and the lightest** of the three that ship with a gearbox: **$13.0k-14.1k, 185 lb (84 kg)** [S AM3]. The Viking 130 is $15.0k and 220 lb [S VK1, VK3].
- **Gearbox field record.** No AM15 or AM13 gearbox failure was found; the one AM13 NTSB report was a builder's cowling [S AM13]. Aeromomentum has one service bulletin on bearing-retainer screws, which came loose three times on vibrating installations [S AM10]. On the Viking side, a Viking 110 dual-ECU select switch was the finding in a fatal accident [S VK13], and forums report two gearbox flange fatigue failures [F VK17].

**The FADEC plan** (section 3):
- **What it keeps of the vendor's kit:** the gearbox, injectors, rail, pumps, throttle body, cam sensor, knock sensor, starter and alternator.
- **What it replaces:** the ECU and harness, and the coil packs if they turn out to be wasted-spark.
- **What it adds:** a second lane, a program trigger wheel read by two sensors, duplicate sensors, a lane-B battery and, optionally, a second injector per cylinder.
- **Cost:** about **$2.7k-7.1k**, or **$3.6k-10.3k** with the second injectors. With the engine and a propeller stand, everything before an airframe is **$18.1k-29.4k** [E].
- **What a single failure leaves:**
  - a lane failure (ECU, sensor, power feed): **100 %**;
  - a plug or coil failure: **70-72 %**, because the bought head has one plug per cylinder;
  - one wasted-spark coil pack, if that is what is fitted: **40-44 %**, because each pack fires two cylinders. The plan converts to coil-on-plug for that reason.
- **The mule is a reduced-redundancy exception to R-25,** as the Hayabusa would have been. It tests the lanes, not the second plug.

**What carries over to concept H:** the lane architecture, arbitration, isolation, sensor set, control laws, CAN-FIX publishing, harness rules and test procedures. That is about 70-80 % of the FADEC work [E, judgment].
- **Proposal:** give H-301's reluctor (CRANK_H301 item 7) the mule's tooth pattern and sensor part. The decoder and trigger hardware then carry over too.
- **What does not carry over:**
  - spark-lane independence at two plugs per cylinder, which is the R-25 element H most needs;
  - the wastegate law;
  - the 6-cylinder calibration;
  - H's rpm range and torsional system.

**The airframe question** (section 4): five routes, from **$18k (no airframe yet) to $66k-174k** in total. The cheapest flying route is a used Rotax 912 E-AB, re-engined with the AM15: **$65k-138k**, before resale of the Rotax. A re-engine is a major change: the FSDO must reply in writing, and then at least 5 h of Phase I follow [S FAA1, FAA3]. The card on AER-3631 asks Bill which route, and the ground tests come first in every route.

**Two findings the board should know:**
1. **The vendors' ratings sit above the donor engines' own published torque.** The AM15's 120 hp at 5,800 rpm is 15 % above the Suzuki G15A's peak torque, and needs volumetric efficiency at the top of the naturally aspirated range. The Viking 130's 130 hp at 5,400 is 11 % above the Honda's peak torque, and needs volumetric efficiency above 1. Neither claim is shown to be wrong; both are unmeasured. Test G1 measures them before the program quotes either number.
2. **The ECU swap is the failure mode the field already shows.** A Zenith CH 750 lost its Viking 130 after a replacement ECU ran lean and lifted the head gasket [F VK15]. A Viking 110 aircraft was lost with two aboard after a dual-ECU select switch cut power [S VK13]. The ground-test sequence (section 3.4) is built around these two cases.

## 2. Picking the conversion (item 1)

### 2.1 The candidates

Every automotive conversion found for sale new with its own gearbox, in the 90-150 hp class. Purpose-built aero engines (Rotax, UL Power, Jabiru, D-Motor) are excluded. SkyTrax sells gearboxes only [S OT7]. The Edge Performance EPeX is no longer listed [S OT10]. The V8 conversions are out of class [F AM15].

| | Aeromomentum AM15 | Aeromomentum AM13 | Viking 130 | Viking 90 / 175 (port-injected Vikings) |
|---|---|---|---|---|
| Price, contents | **$13,000-14,100**: engine, gearbox, starter, alternator, ECU, harness [S AM3] | **$11,500-12,600**, same contents [S AM2] | **$15,000**: engine, 40 A alternator, throttle body, ECU, harness, starter [S VK3] | $11,550 / $19,000 [S VK2] |
| Mass, vendor figure | **185 lb, 84 kg**, "dry", undefined [S AM3] | 170 lb, 77 kg [S AM2] | **220 lb, 100 kg**, undefined [S VK1] | 159 lb [F] / 250 lb [S VK6] |
| Vendor rating | 120 hp at 5,800; propeller 2,240 [S AM3] | 105 hp at 5,800 [S AM2] | 130 hp at 5,400; propeller 2,400 [S VK1] | 90 hp at 5,800 / 175 hp at 6,800 |
| Maximum continuous | not published; cruise at 65 % or less [S AM9] | as AM15 | not published | not published |
| Donor | Suzuki G-series 1.5 L SOHC 16V, 75 x 84.5 mm, CR 9.5 [S AM9; OT14] | G-series 1.3 L, 74 x 75.5, CR 10.1 | Honda Fit L15 1.5 L DOHC, **direct injection**, CR 11.5, VTC [S VK1; F VK23] | Mitsubishi 1.2 L 3-cylinder / Honda K20 |
| Gearbox | 2.588:1 helical, Guibo rubber coupling, "rated to 225 hp" [S AM3, AM7] | the same box | 2.33:1, 3-gear, rubber spider coupling [S VK8; F VK16] | the same box |
| TBO claim | 2,000 h [S AM3] | 2,000 h | not published | not published |
| Fuel | 90 AKI (93 high-power), up to 10 % ethanol [S AM9] | as AM15 | 89+ octane, scale not stated; E10 [S VK1, VK14] | |

### 2.2 The rating check (`mule.py` section 1)

Each claim as BMEP, against the donor's own published peak torque. The implied volumetric efficiency is the check the inputs cannot fake (Heywood eq. 2.41; brake fuel-conversion efficiency 0.30-0.33 at rich full throttle [A]).

| Engine | Claim | BMEP | Implied eta_v | Donor's peak torque as BMEP | Claim over donor peak torque | Power at the claimed rpm, torque held at the donor's peak (an upper bound) |
|---|---|---|---|---|---|---|
| AM15 | 120 hp at 5,800 | 12.4 bar | 0.94-1.03 | 10.7 bar (128 N m at 3,200) [F OT14] | 1.15 | **104 hp** |
| AM13 | 105 hp at 5,800 | 12.5 bar | 0.94-1.04 | not sourced | - | - |
| Viking 130 | 130 hp at 5,400 | 14.4 bar | 1.09-1.20 | 13.0 bar (154.6 N m at 4,600) [S OT15] | 1.11 | **117 hp** |

**Reading it.**
- The Suzuki is rated at 71 kW (95 hp) at 6,000 rpm in the car [F OT14].
- The Honda makes its 130 hp at 6,500 rpm, not 5,400 [S OT15].
- Both aircraft ratings may rest on intake, cam or calibration changes the vendors do not describe. The AM15 page title itself says "117 hp to 147 hp".
- **For the mule this decides little. For the program's comparison tables it matters:** REQUIREMENTS section 7 and HAYABUSA_PLATFORM section 6 quote these vendor ratings as yardsticks. Until a stand measures them, they are vendor claims, and the donor-consistent figure for the AM15 is **about 95-104 hp**.

### 2.3 What R-25 can and cannot reach on each

R-25 asks for two plugs, two coils, two ECUs, two crank sensors and two power feeds per engine, with no shared connector, and at least 90 % of MCP after any single electrical or electronic failure.

| R-25 element | AM15 / AM13 | Viking 130 |
|---|---|---|
| Two plugs per cylinder | **No.** One plug per cylinder [F AM17]. A second plug is a head modification of a bought engine, with the seat-ligament risk of FL-60 and a void warranty. Not taken | **No.** One plug per cylinder [inf from the plug part number, S VK1]. Same answer |
| Two coils per cylinder | No: one plug means one coil. **The vendor's "coil packs" are likely wasted-spark** [S AM9 wording; inf], which puts two cylinders on one coil. The fix is coil-on-plug: one coil per cylinder, still single | No. One coil per cylinder, igniter in the coil [inf] |
| Two injectors per cylinder | **Reachable.** Port injection: a second injector per cylinder in a new or bossed intake manifold, on lane B. Either one alone needs 200-226 cc/min at 85 % duty on E15 (`mule.py` section 3), so a catalog EV14 of 250-300 cc/min covers it | **Not reachable in practice.** One DI injector per cylinder into the chamber. A second needs a head bore |
| Two ECUs | **Yes.** The program's two lanes replace the MicroSquirt | Yes in principle, but each lane needs a DI driver stage and high-pressure pump control |
| Two crank sensors | **Yes.** A program trigger wheel on the front pulley with two Hall sensors, plus the vendor's sensor as a cross-check | Yes, the same way |
| Two power feeds | **Partly.** One alternator [S AM3]. Lane B runs on its own battery, sized for a stated number of minutes. A second generator has no drive pad | Partly, the same way (40 A alternator [S VK3]) |
| At least 90 % after any single failure | **No.** A lane failure leaves 100 %. A plug or coil failure leaves 70-72 % (section 3.3) | No, for the same reason |

**Both are reduced-redundancy exceptions to R-25 at the plug and coil.** That was also the Hayabusa's position on its stock head (FL-52). The Rotax 912 iS does not meet R-25's "no shared connector" either (HAYABUSA_PLATFORM section 5). **The AM15 reaches more of R-25 than the Viking**, because the AM15 can take a second port injector per cylinder and the Viking cannot.

### 2.4 The ECU interface

| | AM15 / AM13 | Viking 130 |
|---|---|---|
| Stock ECU | **MicroSquirt**, single, plug-and-play harness [S AM9]. The intro page and Kitplanes say "Bosch" [S AM7; F AM14]; **unresolved, the first thing to check on a delivered engine** | Viking-supplied, maker not disclosed, single, password-protected [S VK3; F VK18] |
| Injection | Port, one per cylinder, "semi-sequential" [S AM2, AM3]. The MicroSquirt has 2 saturated injector channels for up to 4 high-impedance injectors each [S OT18], so the injectors are **very likely high-impedance** [inf] | **Direct injection**: a high-voltage peak-and-hold driver and a high-pressure pump spill valve [inf, general DI practice] |
| Coils | The MicroSquirt has 4 logic-level ignition outputs [S OT18], so the coils or their igniters take **logic-level inputs** [inf]. "Coil packs", likely 2 wasted-spark packs [S AM9 wording] | Coil-on-plug with igniter, likely [inf] |
| Can our ECU drive them directly | **Yes, on the evidence**: the rusEFI uaEFI drives 6 high-impedance injectors and 6 logic-level coils [S OT16] | **No open ECU in the program's set does**; Haltech does not support the engine [S OT4]; MoTeC and Link are reported to [F OT6] |
| Crank and cam trigger | **Not known which wheel Aeromomentum fits** [nf]. G13BB engines vary by market: VR crank and Hall cam, or cam only [F OT12]. rusEFI has a modified G13B decoder [S OT1]. Because the stock ECU is a MicroSquirt, the pattern is already decoded by open-lineage firmware | 60-2 Hall crank, 3-tooth Hall cam, per Haltech for the L engine; not confirmed for the DI L15B [S OT4] |
| Throttle | cable, likely: no electronic throttle in the manual [inf, AM9] | "throttle body" supplied, cable or electronic not stated [S VK3] |
| Variable valve timing | none: SOHC G-series [inf] | VTC, and Viking's handling of it is not stated [F VK23] |
| Data out | CAN and RS232 [S AM9] | data logger and EIS, protocol not stated [S VK2] |
| Third-party ECU precedent | none found [nf] | Viking 110: the HU708 replacement ECU, about 5 years flying, open schematics [F VK21]. Viking 130: none found |

**The plan does not depend on the vendor's trigger wheel.** It fits the program's own wheel (section 3.2), so the unknown wheel is a check, not a blocker.

### 2.5 The gearbox's field record

| | Aeromomentum (all AM models) | Viking |
|---|---|---|
| Design | helical, 8620 gears, billet case, Guibo rubber coupling "designed to last to TBO" [S AM7; F AM14] | own design, helical, rubber spider coupling; an upgraded box with stronger bearings on the current 130 [F VK22] |
| Field claim | highest-time box 5,500 h in an airboat [F AM14]. Fleet size not published [nf] | 100 Viking 110s delivered and 25 reported flying by 2016 [F VK11]; "over 900 Viking engines in Zenith aircraft" [S AF7] |
| Service bulletins | SB 12/2/19: bearing-retainer screws came loose 3 times on vibrating installations; now safety-wired, checked before each flight [S AM10] | coupling SB (the bolted part replaced so the rubber can float) [F VK16]; flywheel and drive-flange SB [F VK17] |
| Failures found | **none of the gearbox**. NTSB WPR20LA035 (AM13): builder's cowling, overheat [S AM13]. AM15 fuel-rail bracket crack, forced landing [F AM16] | two in-flight fatigue failures of the gearbox input flange ears, at 130 h and about 800 h [F VK17, snippet]; one coupling lobe lost, 2022 [F VK16] |
| Limits that bind the mule | propeller inertia 6,000 kg cm^2 or less; "do not operate where there is a torsional resonance" with untested propellers [S AM9] | gearbox TBO and inspection interval not published [nf] |

The Aeromomentum record is thinner, not cleaner: with no fleet size, no failures found is weak evidence. It is still the better record of the two.

### 2.6 The pick, and what could reverse it

**AM15.** Over the AM13 it costs $1.5k more and weighs 15 lb more. In return it has the lower compression ratio (9.5 against 10.1), which leaves more knock margin for the fuel tests on 91 AKI and E15 (R-12, R-15). It also has more power for an instrumented airframe in Phase I. The AM13 is the fallback if the airframe route favors a lighter engine. Everything in section 3 applies to both unchanged.

Four checks on a delivered engine could change the plan; none of them changes the pick:
1. The ECU is a MicroSquirt, not a Bosch unit.
2. The injectors are high-impedance.
3. The coils take logic-level inputs, and whether they are wasted-spark packs.
4. The throttle is a cable.

If (2) or (3) fails, the plan adds a peak-and-hold or igniter stage. That is about $0.1k-0.3k more [E]. A Viking would only come back if Bill wanted the Viking 175 (K20, port-injected) for power. It carries the same gearbox record.

## 3. The FADEC substitution plan (item 2)

### 3.1 Architecture

- **Two lanes, both always computing; one drives.** Each lane is a rusEFI-class open ECU (uaEFI, $275 [S OT16], or Proteus, $800 [S OT17]). Each has its own sensors, power feed, fuse and harness, with no shared connector. That is the hardware assumed in ARCHITECTURES.md's FADEC line. The program firmware is a fork with the lane logic added. Which board goes into concept H stays open.
- **A program-designed lane isolation and arbitration board** sits between the lanes and the actuators.
  - A hardware watchdog on each lane hands the outputs to the other lane when its heartbeat stops or its self-check fails.
  - Each injector has a high-side switch per lane, so a shorted-on driver in the idle lane cannot hold an injector open.
  - Each coil input takes a logic OR from the active lane only.
- **No pilot-operated lane-select switch is in the power path.** That is the Viking 110 lesson (NTSB ERA23FA023; `docs/ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` section 5.3). The pilot gets a lane-status annunciation and a lane test at run-up, as with magnetos.
- **With the optional second injector per cylinder,** each lane fires its own injector set at half the fuel. When one lane drops, the survivor doubles its pulse width within one cycle. That is the Rotax 912 iS pattern, with both injectors running in normal operation (HAYABUSA_PLATFORM section 5, from the Rotax 912 i installation manual).

### 3.2 What the program FADEC keeps, replaces and adds

| Vendor part | Fate | Why |
|---|---|---|
| Gearbox, Guibo coupling, starter, alternator | **keep** | the reason for buying the engine |
| Injectors, fuel rail, regulator (43 psi over manifold), two parallel pumps | **keep** | high-impedance port injectors drive directly (section 2.4). Each pump goes on a different lane's relay, so a lane loss keeps one pump |
| Throttle body and its TPS | **keep** the body. Lane A reads the stock TPS; **add** a second TPS track or sensor for lane B | cable throttle, so no electronic-throttle single point (as FL-58) |
| Crank sensor | **keep** as a third input, a cross-check on the program wheel | |
| Cam sensor | **keep**, buffered to both lanes. Its loss drops both lanes to crank-only operation: wasted spark from the coil-on-plug coils and batch injection, with power essentially unchanged | the one sensor still shared; FL-66 |
| Knock sensor | **keep** for lane A; **add** a second for lane B | R-13 knock backstop on each lane |
| Coolant and air temperature, MAP | **keep** for lane A; **add** a second set for lane B | |
| Narrow-band O2 | **replace** with two wideband sensors, one per lane | closed-loop lambda and ethanol content need a wideband; R-17 open-loop on 100LL |
| Coil packs | **replace** with 4 coil-on-plug coils (D585 class) **if** the packs are wasted-spark | one coil failure then loses one cylinder, not two (section 3.3) |
| MicroSquirt ECU and harness | **remove**, label and **keep on the shelf**: it is the baseline for test G1 and the ground spare | **not** carried as a switchable third lane: that switch is FL-62's failure mode |
| none | **add**: two lane ECUs; the isolation and arbitration board; a 36-1 program trigger wheel on the front pulley read by two Hall sensors; per-cylinder EGT; lane B's battery; two lane harnesses; optionally a second injector per cylinder | section 3.5 |

### 3.3 What each single failure leaves (`mule.py` section 2)

Full throttle at the takeoff rpm. BMEP from 10.7 bar (donor-consistent) to 12.4 bar (vendor claim), FMEP 1.5-2.2 bar [A].

| Single failure | Cylinders lost | Power left | Against R-25 (at least 90 %) |
|---|---|---|---|
| one lane: ECU, its battery or feed, its crank sensor, its MAP, TPS or temperature sensor | 0 | **100 %**, if the takeover works (tested in G3) | meets |
| cam sensor | 0 | about 100 %, both lanes in crank-only mode | meets, with a degraded-mode annunciation |
| one coil-on-plug coil, one plug or plug lead | 1 | **70-72 %** | **fails**: the reduced-redundancy exception |
| one injector, single injector per cylinder | 1 | **70-72 %** | **fails** |
| one injector, second injector per cylinder fitted | 0 | about 100 %, after a one-cycle lean step | meets |
| one wasted-spark coil pack, if the vendor's packs are kept | 2 | **40-44 %** | **fails badly**: the reason to convert to coil-on-plug |
| alternator | 0 | 100 % for the batteries' endurance, then lane A goes and lane B carries on its battery | meets for a stated time (FL-67) |

A dead cylinder also adds half and first orders to a geared 4-cylinder drive. On the Hayabusa, FL-52's method found a mesh torque reversal near 3,400 crank rpm. The AM15's coupling stiffness is not published, so this is open until the torsional survey in G3. Until then, flights carry a restricted-rpm advisory after any cylinder loss.

### 3.4 The ground-test sequence before flight

Each gate has an exit criterion. A gate that fails sends the work back, not forward. Every gate's logs and fault-injection records are published with the firmware tag they ran.

| Gate | Where | What | Exit criterion |
|---|---|---|---|
| **G0. Bench, hardware in the loop** | bench, no engine | Both lanes and the arbitration board on a crank and cam stimulator, with injector and coil load boxes. Fault injection on every row of section 3.3, plus lane power brown-out, a shorted output, a stuck heartbeat, and a corrupted CAN frame | every fault ends in the designed state; takeover gap measured and under one engine cycle at 5,800 rpm (about 21 ms) |
| **G1. Stand baseline on the vendor ECU** | propeller stand, AM15 as delivered | Run in to the vendor's schedule. Then map the vendor's calibration at 10-15 load points, recording power (propeller torque reaction), rpm, MAP, lambda, EGT per cylinder, coolant and oil temperatures, fuel flow and ignition advance. Torsional baseline: crank-speed ripple at idle and through the rpm range | a reference table the program FADEC must match; **the measured takeoff power, which replaces the vendor's 120 hp in the program's tables** |
| **G2. Each lane alone** | stand | Lane A alone, then lane B alone, on the program trigger wheel. Match G1 | power within 2 %, lambda within 0.02, EGT per cylinder within 25 C of G1 at every point [E criteria]; clean start hot and cold |
| **G3. Both lanes, faults on a running engine** | stand | Every row of section 3.3 at idle, at cruise (65 %) and at takeoff power, by pulling connectors and killing feeds through the board's test inputs. A torsional survey: all cylinders live, then one dead, from idle to takeoff, with crank-speed ripple and coupling temperature | measured power left per row; the takeover produces no rpm drop over 2 %; no half-order resonance inside the flight band, or a published restricted band |
| **G4. Fuels and knock** | stand | 91 AKI E0, E10 and E15 (R-12, R-15), and 100LL open-loop (R-17). Knock survey with the spark swept to borderline at takeoff and cruise, hot fuel, a hot-day restart | knock margin per fuel recorded; ethanol content estimated from the lambda correction within 3 points [E] |
| **G5. Endurance** | stand | 50 h [E] on a duty cycle of 10 % takeoff, 60 % cruise and 30 % idle and descent, with thermal cycling and vibration logged at the ECU enclosures. Oil analysis. Gearbox screw witness marks (Aeromomentum SB 12/2/19) | no unplanned lane switch; no fault without a logged cause; the borescope and the screws as at the start |
| **G6. Installed ground runs** | in the airframe | Electromagnetic compatibility with the radios and EFIS, taxi, run-ups, a lane test at every run-up, a full-power static run with a lane failed | as G3, in the installation |

Then Phase I. The FSDO must reply in writing first, then come at least 5 h of Phase I in the assigned area [S FAA1, FAA3], or 40 h if it is a new aircraft. A task-based plan under AC 90-89C is allowed [S FAA3]. The Phase I plan adds in-flight lane tests at altitude over a landable area, with the FADEC logging at full rate.

**Calendar time, G0 to G6: about 6-12 months of part-time work [E].** It is the same in every airframe route, because nothing flies before G5.

### 3.5 Mass and cost (`mule.py` section 4)

**Mass added over the vendor's kit: about 2.5-4 kg** [E]: the second lane, its battery, sensors and harness. That is the same line as the Hayabusa's second lane (HAYABUSA_PLATFORM section 6).

| Line | Low | High |
|---|---|---|
| Two lane ECUs [S OT16, OT17] | $650 | $1,600 |
| Lane isolation and arbitration board, two prototype spins [E] | $300 | $1,000 |
| Coil-on-plug conversion [S ARCHITECTURES; E] | $250 | $500 |
| Program trigger wheel and two Hall sensors [E] | $100 | $300 |
| Lane B's sensors: MAP, TPS, temperatures [E] | $150 | $400 |
| Two wideband sensors [E] | $200 | $300 |
| Lane B battery and feed, 30 min [E] | $300 | $800 |
| Two lane harnesses [E] | $400 | $1,200 |
| Hardware-in-the-loop bench [E] | $300 | $1,000 |
| **Substitution, one injector per cylinder** | **$2,650** | **$7,100** |
| Second injector per cylinder, rail and manifold [E] | $900 | $3,200 |
| Propeller test stand, instrumented [E] | $1,500 | $5,000 |
| AM15 [S AM3] | $13,000 | $14,100 |
| **Everything before an airframe** | **$18,050** | **$29,400** |

Builder labor is not in these lines. The firmware work is the program's FADEC work, which it does anyway.

### 3.6 What carries over to concept H, and what does not

Concept H: a flat-6, two plugs per cylinder, one port injector per cylinder, a turbo normalizer with a wastegate, about 3,300 rpm, one reluctor read by both lanes (CRANK_H301 item 7; RANKING_PHASE1 section 10).

**Carries over:**
- the lane architecture, the arbitration and isolation board, the watchdog and takeover logic, and their G0 and G3 fault-injection procedures;
- the sensor set and its duplication, and the CAN-FIX publishing to pyEfis (R-27);
- fuel, spark, lambda, ethanol-content and knock control laws, the calibration tools, and the per-cylinder EGT and knock surveys;
- the harness rules: no shared connector, per-output fusing, keyed connectors;
- **the trigger hardware, if H-301's reluctor takes the mule's tooth pattern and sensor part.** The proposal: a 36-1 wheel read by two Hall sensors on both engines. The decoder, the sensor, its bracket logic and the crank-only fallback then carry over unchanged. It costs nothing on H-301, whose wheel is not yet specified beyond its 46 x 12 seat. This proposal goes to Rev B of H-301.
- the stand, its instrumentation, the propeller-matching method, and the flight-test logging;
- the regulatory path, and flight hours on the lane logic.

**Does not carry over:**
- **Spark-lane independence at two plugs per cylinder.** That is the element of R-25 that H depends on and the mule cannot test: each H lane fires its own plug in every cylinder. The mule tests the takeover of coils and injectors, not two live spark lanes. A ground rig on H, or on an EZ36 (HAYABUSA_PLATFORM role (d)), has to prove it.
- The wastegate law and overboost protection (FL-30): the AM15 is not boosted. The AM15T is, at $17.7k [S AM5], but it adds a turbo with its own failure modes to the mule, and is not proposed.
- The 6-cylinder firing order, the calibration tables, and H's rpm range.
- The torsional monitoring of H's direct drive: the mule's is a geared 4-cylinder.

About **70-80 % of the FADEC work carries over** [E, judgment], the same share HAYABUSA_PLATFORM section 5 gave its mule. The missing share is the two-plug spark lanes.

## 4. The airframe question (item 3)

A flight mule needs an airplane, and the MAOS airframe is paused (ORG-009). This section states the routes and their costs. It does not choose one. Costs add the section 3.5 total ($18.1k-29.4k) to the airframe (`mule.py` section 5). The Zenith CH 750 is the reference airframe, because Aeromomentum sells a firewall-forward package for it: cowling $2,530, propeller $2,130, mount $1,237 [S AF4].

| Route | Airframe and installation | Total with the engine and FADEC | Time to first flight [E] | Main caveat |
|---|---|---|---|---|
| **B. Buy a used Rotax 912 E-AB and re-engine it with the AM15** (CH 750, Kitfox, Rans S-6/S-7 class) | $47k-109k: flying aircraft $40k-99k [F AF20], the AM15 package parts, and $1.5k-4k of exhaust, radiator and fuel work [E] | **$65k-138k**, before selling the Rotax (one 912iS sold at $23.5k [F AF21]) | the swap runs alongside G0-G5; then the FSDO letter and at least 5 h of Phase I; about 9-15 months in all | +20 lb on the nose against a Rotax 912 (185 against 165 lb [S AF3]): weight and balance redone. One CH 650 builder found the Aeromomentum parts fitted poorly [F AF23] |
| **C. Build a kit** (CH 750 STOL, firewall-back $38,725 [S AF9]) with the AM15 | $56k-74k, including $10k-25k for instruments, avionics and finish [E] | **$74k-103k** | 400-1,000 h of building [S AF10, F AF24], then 40 h or a task-based Phase I; about 18-30 months | the slowest route. Who builds it decides the certificate: an E-AB needs an individual builder doing the major portion, for education or recreation [S FAA7; F AF31] |
| **A. Buy a flying Viking 130 CH 750 and re-engine it with the AM15** | $76k-145k ($69k and $135k listings [F AF14, AF15]) | **$94k-174k**, before selling the Viking | as B | dearer than B with no gain. Flying it on its Viking instead would put the FADEC on a direct-injected engine (section 2.4). No flying AM13 or AM15 aircraft was for sale [F AF19] |
| **D. A host aircraft**: an owner already flying an AM15 lends it for the test | $2k-10k [E]: parts to return it to stock, an insurance increment, the owner's costs | **$20k-39k** | after G5, if a host exists. **None is known**, and no published host agreement was found [nf] | the owner's FSDO letter and Phase I; the insurer's acceptance; whether the program's purpose fits the aircraft's E-AB certificate (below) |
| **E. No airframe yet: ground stand only, airframe decided after G5** | $0 now | **$18k-29k** | no flight. G0-G5 are needed in every route anyway | flight hours wait. The airframe decision comes back in 6-12 months with measured stand data |

**Also considered, and not proposed:**
- **Bill's own certificated aircraft.** A non-certificated engine takes it out of its type design. It would fly on an Experimental R&D certificate, renewed every 3 years, with its standard certificate held in suspension, and it returns to standard only when rebuilt to the type design [S FAA1 10-3, FAA9]. The Continental E-225-8 class of airframe is also about twice the AM15's power.
- **Un-pausing the MAOS airframe:** that is an ORG-009 decision and not this issue's to cost.

**The rules that set the flight-test burden:**
- **A re-engine or ECU swap on a flying E-AB is very likely a major change** under 21.93: "appreciable effect on ... reliability, operational characteristics" [S FAA5]. The FAA has not confirmed this reading.
- Order 8130.2L Appendix D, limitation 22: the Flight Standards Office "must be notified and its response received in writing before flying this aircraft", then Phase I limitations apply [S FAA1]. AC 90-89C section 2.1.12: "at least 5 hours minimum of supplemental Phase I" [S FAA3]. The FSDO may require more [F AF30].
- **A new build with a non-type-certificated engine: 40 h** of Phase I (8130.2L 15-4f(1)(a)), or a task-based plan under AC 90-89C section 2.1.6 [S FAA1, FAA3].
- **Whose flights are these?** The 51 % rule decides who built an E-AB, not who flies it, and an organization may own one [S FAA7; F AF31]. **Whether an engine program's development flying fits an E-AB certificate's purpose (91.319(a)(1)) was not found stated by the FAA** [nf]. The clean path is an Experimental R&D certificate under 21.191(a): "new aircraft equipment, new aircraft installations" [S FAA7]. It needs a program letter under 21.193 and is renewed every 3 years [S FAA8, FAA9]. A DAR or the FSDO answers this before any purchase.
- **Insurance.** Phase I is often liability-only, or carries a hull deductible of about 10 % [F AF27, AF29]. Auto-conversion engines raise premiums [F AF27]. No premium for this case was found [nf].
- **The pilot** is not costed here. Phase I can carry a second pilot under AC 90-116 [S FAA3, FAA4].

**The card on AER-3631** asks Bill which route the program plans around. It recommends that nothing be bought until G5 passes, in any route, because the stand work comes first in all of them.

## 5. Failure ledger

Added to `FAILURE_LEDGER.md` as **FL-61 to FL-69**, each conditional on the mule route:
- **FL-61:** a replacement ECU's calibration runs lean at high power (the Viking 130 seizure case).
- **FL-62:** the lane-switching element itself cuts both lanes (the Viking 110 select switch, NTSB ERA23FA023).
- **FL-63:** the idle lane's driver fails shorted on, holding an injector open or a coil charged.
- **FL-64:** one software fault, identical in both lanes.
- **FL-65:** a single plug or coil per cylinder; a wasted-spark pack takes two cylinders.
- **FL-66:** the shared cam sensor, and the program trigger wheel read by both lanes.
- **FL-67:** one alternator, with lane B on its own battery.
- **FL-68:** the gearbox's bearing-retainer screws and its propeller and torsional limits, under the program's calibration.
- **FL-69:** the lean step when one lane of a split injector pair drops at takeoff.

## 6. What this pass did not do

- **Nothing was bought, weighed or run, and nothing was quoted** (AER-3330). Every cost above the vendor list prices is a PROPULSION estimate. MANUFACTURING has not priced the arbitration board, the manifold for the second injectors, the trigger-wheel bracket or the stand. Those go to MANUFACTURING for a DFM read only if Bill takes a route that builds them.
- **Not confirmed on the AM15:** the ECU (MicroSquirt or Bosch), the trigger wheel, the injector impedance, whether the coils are wasted-spark packs, and the throttle type. Section 2.6 says which of these would change the plan.
- **No MCP for either vendor,** and no AM13 donor rating. The rating check uses the donor car ratings from a secondary site for the Suzuki [F OT14] and from Honda for the Viking [S OT15].
- **The Viking gearbox and coupling history comes from forum snippets**; the VAF pages returned 403. The Viking 130 seizure report is a GA News snippet with no NTSB number found.
- **The torsional case with a dead cylinder on the AM15 is not computed:** the Guibo stiffness and the inertias are not published. G3 measures it.
- **The airframe listings come mostly from Barnstormers.** Trade-A-Plane and Controller could not be read, and two data points are not a market range. No calendar time for an FSDO reply was found; the time column is an estimate.
- **Who flies Phase I, and on what certificate, is open.** It goes to a DAR or the FSDO before any purchase.
