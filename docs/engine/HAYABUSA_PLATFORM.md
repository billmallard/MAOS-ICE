# The Suzuki Hayabusa as a starting platform: a serious evaluation

Owner: PROPULSION. Issue: AER-3525 (MANUFACTURING pricing: AER-3526). Date: 2026-10-19.
Status: **exploration, not a ruling.** Bill asked for this in conversation on 2026-10-19. Nothing here changes REQUIREMENTS section 12 or the family plan (R-1). Nothing here has been built, weighed, run or flown. This is an experimental engine design; nothing in it is certified, certifiable or flight-ready.

Numbers come from [`analysis/engine_hayabusa/`](../../analysis/engine_hayabusa/): `rating_busa.py` (rating, knock, boost, radiator), `torsional_busa.py` (crank torque and the geared drive) and `mass_cost_busa.py` (mass, cost, labor, durability bracket), with their tables beside them. Tags: **[S]** sourced, **[F]** forum or a search snippet only, **[E]** PROPULSION estimate with its method in the script, **[A]** assumed. Source keys: [Hn] specifications, [Dn] durability and dual-lane, [Pn] aviation and reduction drives, all in [`sources/HAYABUSA_SOURCES_2026-10-19.md`](sources/HAYABUSA_SOURCES_2026-10-19.md). **None of the costs is a quote.**

## 1. The answer

**Recommendation: do not start the platform on the Hayabusa.** It is a cheap way to get an engine *running*. It is not the cheapest *credible* way to get one *flying*, and as a product it loses to engines builders can already buy.

**The strongest case against it:**

1. **Nobody sells a reduction drive for it, and the one Hayabusa aircraft found was lost.** No Hayabusa PSRU was found from any vendor in about 18 searches [P section 1]. The Bugatti 100P replica flew on two Hayabusas driving through the motorcycles' own wet clutches, locked in 6th gear. On its third flight the forward engine surged to about 10,000 rpm just after liftoff, and the airplane stalled and crashed, killing the pilot (NTSB CEN16FA307) [P1-P4]. The NTSB named an engine anomaly of undetermined cause. The builders' team concluded that the forward clutch slipped. So the program would have to design, qualify and support the drive itself. That drive is the hardest part of any automotive conversion.
2. **It does not beat what a builder can buy today.** First engine, built to this program's standard (two lanes, dry sump, our gearbox): **$19.0k / $29.7k / $46.4k** (low / mid / high), **112-140 kg** installed dry, for **113-139 hp** at takeoff. The Aeromomentum AM15 is **$13.0k-14.1k** with its gearbox, starter, alternator and ECU, at **83.9 kg** and 120 hp, against **113-139 hp** for the Hayabusa. Even the low end of the Hayabusa band costs more and weighs 28 kg more.
3. **R-25 (two independent lanes) needs head work nobody has done.** The stock head has one plug per cylinder. On that head, one coil or plug failure leaves **about 72 % of MCP**, against R-25's 90 %. It also drives the gear mesh into torque reversal near 3,400 rpm (section 5). No twin-plug Hayabusa head exists anywhere [D section B7]. The injectors are the good news: there are two per cylinder.
4. **There is no evidence for a long life at aircraft load.** The only high-load data are Radical race cars, which rebuild their 1340 engines every 90-100 hours [F, D1-D2]. Scaled to aircraft rpm, that is **about 100-370 h**, against R-40's 2,000 h. No generator, marine, airboat or aircraft hours were found at all.

**The strongest case for it:**

1. **The core is cheap and plentiful.** A used Gen 2 engine is **$3.0k-3.8k** [S, H24]. Over 200,000 Hayabusas have been built [H43].
2. **It makes more than the 100 hp member needs.** That is **113-139 hp at the flange for takeoff** and **88-110 hp at MCP**, at a BMEP no higher than the motorcycle's own and at Rotax 912-class MCP BMEP.
3. **It is fully liquid-cooled, with two injectors per cylinder.** Gen 2 has eight 280 cc/min injectors [H14, D39]. Either set alone could carry the aircraft takeoff rating at about 58 % duty [E]. Standalone ECUs already support it (Haltech, MoTeC, MBE) [D39, D44, D47].
4. **A soft-coupled gearbox can tame its torque pulses.** In the program's own model the gear-mesh torque ratio at idle comes out about the same as a Rotax 912's.

**Of the three roles Bill named** (section 8): as a **development mule** it is possible but not the best choice (score 4 of 10). As a **starter product** it is a poor choice (2 of 10). As a **dead end** it is the likeliest outcome if it is taken on as a platform (6 of 10). **A better mule exists for each purpose.**
- For FADEC, cooling, propeller and instrumentation work in flight, carry the program's FADEC on a bought conversion with a proven drive, such as the AM15.
- To retire concept H-EZ36's risks (if Bill takes that variant, AER-3411), run a ground mule on a used Subaru EZ36 behind the program's gearbox. That tests the actual donor crank and a gearbox of the right size.

**Did the killers show up?** Yes. Two of the three findings I would recommend against were found: no drive exists, and the build is not cheaper than buying. Section 9 has the detail.

## 2. Usable power for aircraft duty (question 1) and fuel (question 5)

**Generation recommended: Gen 2 (2008-2020).** Its bore, stroke and compression ratio are the same as Gen 3's (81 x 65 mm, 1,340 cc, 12.5:1) [H1, H5, H11]. It has a cable throttle; Gen 3's ride-by-wire would be a single-failure power loss (FL-58). Its injector flow is published (eight at 280 cc/min). Its 24-2 crank trigger is documented [H14]. It is also the cheapest used core with low miles. Its cam-chain tensioner needs care (FL-54).

**The motorcycle ratings** [H1]:

| Generation | Peak power | BMEP at peak power | Piston speed at peak | Peak torque | BMEP at peak torque |
|---|---|---|---|---|---|
| Gen 3 | 188 PS at 9,700 rpm | 12.8 bar | 21.0 m/s | 149 N m at 7,000 | 14.0 bar |
| Gen 2 | 197 PS at 9,500 | 13.7 bar | 20.6 m/s | 155 N m at 7,200 | 14.5 bar |
| Gen 1 | 175 PS at 9,800 | 12.1 bar | 20.6 m/s | 138 N m at 7,000 | 13.4 bar |

**The aircraft rating**, set from three limits:
- **Piston speed:** a band between the Rotax 912 (11.2 m/s at MCP) and the Viking and Aeromomentum conversions (about 16 m/s).
- **BMEP:** no higher than the motorcycle's own full-throttle torque at that rpm. Gen 3 stock rear-wheel dyno [H18] divided by 0.94 [E] to get to the crank.
- **Implied volumetric efficiency:** a check the inputs cannot fake. It is printed on every row.

| Point | rpm | Sp | BMEP | Crank | At the flange (gearbox 0.97-0.98) | Fuel | Implied eta_v |
|---|---|---|---|---|---|---|---|
| Takeoff, 5 min, low band (eta_v capped at 1.0, no tuned-intake credit) | 6,500-7,000 | 14.1-15.2 m/s | 12.0 bar | 87-94 kW | 113-123 hp | 33-35 L/h | 1.01 |
| Takeoff, 5 min, high band (the motorcycle's own curve, less the CR penalty) | 6,500-7,000 | 14.1-15.2 m/s | 13.0-13.5 bar | 95-105 kW | 123-139 hp | 35-38 L/h | 1.06-1.09 |
| MCP, hours | 5,800-6,500 | 12.6-14.1 m/s | 10.5-11.5 bar | 68-83 kW | 88-110 hp | 24-32 L/h | 0.86-1.01 |

The high takeoff band needs the motorcycle's tuned intake and exhaust lengths, which the dyno shows it achieves. A new aircraft intake has to keep them, or the low band applies.

**Against the yardsticks** (`rating_busa.py` section 4; sources COMPARABLE_ENGINES):

| Engine | Takeoff | BMEP at takeoff | Sp at takeoff | MCP | BMEP at MCP | Sp at MCP |
|---|---|---|---|---|---|---|
| Rotax 912 ULS | 100 hp (73.5 kW) at 5,800 | 11.2 bar | 11.8 m/s | 69 kW at 5,500 | 11.1 bar | 11.2 m/s |
| Rotax 915 iS, turbo | 141 hp (104 kW) at 5,800 | 15.9 bar | 11.8 m/s | 99 kW at 5,500 | 16.0 bar | 11.2 m/s |
| Concept H, 200 hp member | 200 hp at 3,300 | 10.3 bar | 11.2 m/s | 180 hp at 3,300 | 9.3 bar | 11.2 m/s |
| **Hayabusa, aircraft rating** | **113-139 hp at the flange, 6,500-7,000 rpm** | 12.0-13.5 bar | 14.1-15.2 m/s | **88-110 hp, 5,800-6,500 rpm** | 10.5-11.5 bar | 12.6-14.1 m/s |

**Where it lands.**
- It clears the 100 hp member (R-3: 90 hp MCP) with margin at the top of its MCP band, and misses by 2 hp at the bottom (5,800 rpm, 10.5 bar).
- It sits between the Rotax 912 and 915.
- It runs a Rotax 912 BMEP at **13-26 % higher piston speed**.
- It is nowhere near the 200 hp member.

**Knock: the stock compression ratio is too high for sustained full throttle on 91 AKI** (`rating_busa.py` section 2, knock.py's calibrated index, with the liquid-cooled-head credit).
- On MON 85 the limit is CR 11.2 at 6,000 rpm and 11.7 at 7,000. The stock 12.5:1 clears only at about 9,700 rpm, the motorcycle's peak, where the burn is fast.
- A motorcycle gets away with 12.5:1 because it holds full throttle for seconds and retards spark below the peak.
- **The aircraft rating assumes 11:1 pistons.** They cost about 3.4 % of power (ideal Otto ratio), and that cost is in the table above.
- Caveat: knock.py does not model the late intake-valve closing of a high-rpm cam. Late closing lowers the effective compression ratio at 6,500 rpm, so the true limit could be higher. A knock survey on the stand is the test (FL-57).

**Normalized or boosted?**
- **A normalizer (R-5) holds 113-139 hp to 12,000 ft. It does not add power.** It costs 14-21.5 kg and $2.0k-4.5k (the program's turbo lines).
- **150-200 hp needs boost, which R-5 rules out.** `rating_busa.py` section 5 gives the figures at 7,000 rpm:
  - 150 hp needs 14.7 bar, 0.92 x the Rotax 915's takeoff BMEP.
  - 175 hp needs 17.1 bar, 1.08 x the 915's, at about 1.26 bar of manifold pressure.
  - 200 hp needs 19.6 bar, 1.23 x the 915's and 1.09 x the 916's.
- **The Rotax 915 pays for its boost with a 1,200 h TBO, against 2,000 h for the 912** [R5].
- **So a boosted Hayabusa at 150-170 hp is Rotax 915-class BMEP at higher piston speed, on an engine with no aviation hours.** It would eat a durability margin nobody has measured. 200 hp is beyond any gasoline aviation precedent at this size. **Not a credible 150-200 hp engine.**

**Fuel (R-12, R-15, R-17).**
- **91 AKI:** the aircraft rating above is on MON 85 with 11:1 pistons. Suzuki's US manual asks for a minimum of 90 (R+M)/2 [H11].
- **Ethanol:** Suzuki's US manual allows **no more than 10 % ethanol** [H11]. E15 (R-15) is outside the maker's approval. The aircraft fuel system is new anyway: two pumps, FKM or PTFE hoses, E15-rated filters (the program's fuel line). The engine-side parts left are the injector O-rings and the fuel rail seals. They must be confirmed E15-compatible or replaced with FKM. The stock in-tank pump is not used.
- **100LL:** run open-loop, because lead poisons the wideband sensor (R-17, FL-14). Shorten the oil-change interval. No Suzuki statement on leaded fuel was found. Plug fouling with the fine-wire iridium plugs is the likely nuisance, and is untested.

## 3. Durability under continuous load (question 2)

**What exists** [D section A]:
- **Radical (Hayabusa-derived engines, race cars):** owners quote the warranty as 40 h of total running for the 1500 cc engine and 90-100 h for the 1340 (one shop says 80 h; some owners stretch to 200 h) [F, D1, D2]. The 1340 makes 205 bhp at 9,500 rpm [D3].
- **What a Radical rebuild replaces:** gearbox gears 1, 2, 5 and 6, the clutch, **all bearings**, the cam chain and guides, and often a cracked starter-clutch cover [F, D4].
- **Westfield and Caterham owners:** failures "usually from oil starvation, lack of maintenance or serious track abuse" [F, D6].
- **Generator, marine, airboat, hovercraft or aircraft use with hours: none found** [D section A4, P section 6]. The earlier MAOS generator studies found the same and set SAFETY's 50 % interim credit for that reason (`docs/POWERTRAIN_TRADE_STUDY_50K_V1.md` section 1.3).
- **Suzuki's own schedule:** oil every 6,000 km, plugs every 12,000 km, valve clearances every 24,000 km [D26, D27]. These figures come from a secondary site quoting the manual.

**A bracket on the overhaul interval** (`mass_cost_busa.py` section 4). Take Radical's 90-100 h. Scale it from a race mean of 7,500-9,000 rpm [A] to the aircraft's 5,800-6,500 rpm MCP. Bracket the wear law between sliding distance (hours go as 1/rpm) and an Archard law with inertia load (hours go as 1/rpm^3). The result is **about 100-370 h to a Radical-class rebuild.** This is not a TBO. Part of the Radical rebuild is gearbox wear, which an aircraft drive need not load. Race duty is also harsher than cruise in ways the rpm scaling does not capture. On the other hand, an aircraft spends 55-75 % of its hours at a load a race car only passes through.

**Realistic interval, with its evidence: provisional, of the order of 300 h, set by teardown, not by assumption.** Use R-41's teardowns at 25, 100 and 300 h. Nothing found supports R-40's 2,000 h. The Aeromomentum and Viking cores claim 1,500-2,000 h on automotive engines. That is a different class of core, and the claims are the vendors'.

**Known failure modes**, added to the ledger:

| Mode | Evidence | Ledger |
|---|---|---|
| Cam-chain tensioner and chain | Gen 1 tensioner recalls 99V270000 and 00V319000, 8,511 units [D9, D10]. Race-car users report Gen 2 (K8) tensioner chain failures and refit the earlier type [F, P38, P39] | FL-54 |
| Oil surge and starvation | "the one engine we and many others have failed to control with billet wet sumps", from a sump maker [F, D14]. Idle oil pressure "as low as 2 psi" above 120 C [D15]. A dry-sump kit is in production (SBD, GBP 1,160 ex VAT) [D30] | FL-55 |
| Rod and main bearings at sustained load | spun rod bearings in race cars [F, D4]; all bearings replaced at every Radical rebuild | FL-59 |
| Charging system | Gen 2 regulator recall 11V108 [D16] | FL-56 |
| Gearbox-driven torsional and clutch problems | the Bugatti 100P's clutch, as its builders concluded [P2, P4]; Radical gearbox wear [D4] | FL-53, FL-51 |
| Gen 1 second gear | not undercut, "where most of the problems occurred" [F, D12] | not carried: the aircraft drive does not use the gearbox's gears |

## 4. Reduction drive and torsional behavior (question 3)

**What exists to buy: nothing for the Hayabusa** [P section 1]. Nearby products:
- **Raven Redrives:** belt drives for automotive engines; production apparently ended in 2017 [P7, P8].
- **SkyTrax:** gear drives for Yamaha snowmobile engines only, e.g. 3.83:1, about 24 lb, $4,999 [P17-P19].
- **Rotax C gearboxes:** adapted to the Yamaha by builders [F, P16].

The Yamaha Genesis 4-cylinder conversions are the closest flying analog. They have a field claim of more than 200 flying (vendor, snippet) and owner reports of about 80 trouble-free hours [P14, P15]. Note a structural difference: the Yamaha has no gearbox, only a fixed countershaft with a rubber damper, and the PSRU bolts behind that [P12, P13].

**Ratio:** **about 2.9:1**, 7,000 crank rpm to 2,400 propeller rpm. MCP at 6,500 rpm then gives about 2,230 propeller rpm. That is the Rotax 912's propeller speed (2.43:1, 2,388 rpm), so the 912 propeller class and the program's ground-adjustable pick (3b) apply unchanged.

**Two drive layouts.**
- **(i) Through the motorcycle's primary gear (1.596:1), clutch and gearbox, locked in one gear,** with a second reduction behind the countershaft. The Bugatti did this, using 6th gear (1.043) [H12, P3]. It is the cheap layout, and it puts a slipping wet clutch in the torque path. **Design rule: no motorcycle clutch in the torque path** (FL-53). Lock the clutch pack solid, or replace it with a solid hub. The only element allowed to slip is a calibrated overload clutch at about 2-2.7 x rated torque, as on the Rotax (FL-41).
- **(ii) A gearbox on the crank end,** with the motorcycle gearbox left idle or emptied. This is cleaner, and it is a new adapter, a coupling and a gearbox: the program's own gearbox.

**Make, not buy:** the program's proven-class gearbox (CRANK_AND_SCALING section 5) at **$2.9k-9.8k** and **8-15 kg**, sized for 408 N m of propeller torque. MANUFACTURING prices the adapter plate and crank-side hub at $1.1k-4.5k and the elastic coupling at $0.3k-1.0k (AER-3526). Its flag stands as a PROPULSION load question, open: the Hayabusa case has no bellhousing, so a plate on a cover flange's small bolts cannot be the whole answer for the gearbox's overhung mass and reaction torque. The gearbox needs a tie into the mount structure.

**Torsional risk** (`torsional_busa.py`). The method: a cylinder-pressure cycle gives gas plus inertia torque. That is summed over the firing order and Fourier-split, then fed to a damped two-inertia drive with propeller damping. Inertias are assumed, with bands.

| | Hayabusa I4 at 7,000 rpm, 2.92:1 | Rotax 912 at 5,800, 2.43:1 | Concept B flat-8 at 5,800, 2.4:1 |
|---|---|---|---|
| Major order | 2 | 2 | 4 |
| Its amplitude at takeoff / mean torque | **1.80** | 0.63 | 0.65 |
| Reciprocating-inertia part of that order | 449 N m | 238 N m | 44 N m |
| Firing band, idle to 105 % | 57-245 Hz | 47-203 Hz | 120-406 Hz |
| Soft tuning: coupling stiffness below (crank side) | 1,300-2,400 N m/rad | 1,300-2,100 | 14,000-20,000 |
| Mesh alternating / mean torque, worst point, coupling at 0.5 x the idle firing frequency | 1.09 (1.22 bad case) | 1.27 (1.41) | 0.54 (0.59) |
| The same with the coupling 40 % stiffer (0.7 x) | 2.88 | 3.38 | 1.49 |
| Coupling wind-up at takeoff torque, soft case | 10.7 degrees | 10.6 | 2.2 |

**Reading it.**
- **Against concept B it is worse.** B's flat-8 fires twice as often and nearly cancels its inertia torque. It tolerates a coupling about 9 times stiffer, and its worst mesh ratio is half the Hayabusa's.
- **Against the Rotax 912 it is about equal when soft-coupled, and less forgiving when anything stiffens.** The raw pulse at takeoff is 2.9 times the 912's, relative to mean torque, because the Hayabusa's pistons reverse 1.2 times faster. With the coupling at half the idle firing frequency, as EPI advises [P22, P23], the mesh sees about what a 912's does. That needs a coupling as soft as the 912's: about 830 N m/rad on the crank side, 10.7 degrees of wind-up at takeoff torque, a mode near 28 Hz, and a resonance crossing at about 840 rpm during start and shutdown.
- **An aged coupling that is 40 % stiffer triples the idle mesh ratio** (FL-51).
- **A stiff (above-band) drive is worse at every point:** 3.7 times the mean at takeoff.

**Make vs buy:** make, on the Rotax pattern: a single gear stage, a soft coupling with friction, an overload clutch and a chip detector. Then survey it on the dynamometer with the real propeller before any flight (EPI: "test stand operation is not the same as flight" [P24]).

## 5. Dual lane and FADEC (question 4)

**What two truly independent lanes take on this engine:**

| R-25 element | On a stock Gen 2 | What it takes | Cost [E] |
|---|---|---|---|
| Two plugs per cylinder | one M10 plug per cylinder, central, coil on plug [D33] | a second plug machined into the chamber edge from outside the head, between an intake and an exhaust valve. No Hayabusa twin-plug head exists. The precedent is other 4-valve heads (Ducati Testastretta DS, BMW R1200 twin-spark, KTM 690) [D34-D37]. Feasibility depends on the water jacket, unmeasured | $2.1k-7.3k (MANUFACTURING, AER-3526): two scrap heads, a section, a fixture, sleeved plug tubes. **Outside the envelope until a sectioned head proves it** |
| Two coils per cylinder | four coils | four more D585-class coils | $0.2k-0.4k |
| Two injectors per cylinder | **already there: 8 x 280 cc/min, staged** [H14, D39] | lane A on the primaries, lane B on the secondaries; each set alone carries takeoff at about 58 % duty (161 against 280 cc/min). Untested: the secondaries spray into the bellmouth, so mixture at low load may differ [D section B8] | in the FADEC line |
| Two crank sensors | one reluctor pickup, 24-2 [H14] | a second pickup on the same wheel, or a second wheel | $0.1k-0.3k |
| Two ECUs | stock ECU | the program FADEC: two lanes | $1.5k-4.0k (same line as H) |
| Two power feeds | one stator, one regulator | a second generator for lane B | $0.4k-0.9k |
| Throttle | Gen 2 cable throttle; the secondary butterflies are ECU-driven | pin the secondary butterflies open or remove them. Gen 3's ride-by-wire is a single point (FL-58) | small |

**Is the head modifiable? Unknown, and that is the honest answer.** MANUFACTURING's read (AER-3526): the free spots at the chamber edge sit at the ends of the roof ridge, which face the next cylinder, so any approach is a steep compound angle that very likely crosses the water jacket. The workable form is a sleeved plug tube (M10 x 1.0, the stock thread) sealed at both walls; a welded boss is ruled out. The first risk is the ligament to the pressed-in valve-seat inserts: a bore too close loosens a seat, and a dropped seat destroys the engine (FL-60). The first step is to section a scrap head and measure that wall. If a scrap-head survey shows room for an M10 or M12 boss without breaking into the jacket, R-25 is met in full. Then a single lane failure loses one plug per cylinder, a few percent of power. If not, **the Hayabusa is a reduced-redundancy exception to R-25, and should be said so plainly:**
- **Injection, sensing, processing and power can be made dual. Ignition cannot.**
- **One coil or plug failure then leaves about 72 % of MCP** (`torsional_busa.py` section 4: (3/4 IMEP - FMEP) / BMEP).
- **It also adds half- and first-order torque to a drive tuned below idle.** The half order crosses the drive mode near **3,400 crank rpm**, in the descent band. There the mesh torque reverses at about **3.2 times the mean** (FL-52).

**For comparison, Rotax does not build two fully isolated chains either** [D50]. The 912 iS has one ECU with two modules (lanes). Either lane can drive all the coils and all the injectors. Each cylinder's two injectors both run in normal operation. Either generator supplies both lanes. R-25's "no shared connector" is stricter than the Rotax.

**Can the open FADEC be developed and flight-tested on this engine first?**
- **Developed on a stand: yes.**
- **Flight-tested: only after the drive is made and surveyed (section 4), and only on an airframe Bill provides** (the MAOS airframe is paused).
- **On a stock head the flight test would exercise a reduced-redundancy FADEC.** That is exactly the part of R-25 the program most needs to prove.

**What carries over to concept H** [E, judgment]: about **70-80 % of the FADEC work**.

Carries over:
- the lane architecture, power isolation and fault handling;
- the sensor set and CAN-FIX publishing to pyEfis (R-27);
- fuel, spark, lambda and ethanol control laws;
- knock control and calibration tools;
- the harness rules (the Viking lessons, `docs/ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` section 5.3).

Does not carry over:
- the trigger pattern, cylinder count, injector staging and rpm range;
- the wastegate law, if the mule is unboosted;
- **dual-plug lane switching, unless the head work succeeds.**

## 6. Installed mass and cooling (question 6)

`mass_cost_busa.py` section 1, on R-37's installed-dry definition. **The engine mass is the weakest number here.** No Suzuki or supplier figure was found. Forum posts give 86-92 kg with the integral gearbox, clutch, starter and stator [F, H21, H22]. The earlier MAOS studies' "about 55 kg bare" was derived from the whole bike's mass, and is not used. Weighing one core settles it.

| Line | kg |
|---|---|
| engine with integral gearbox, clutch, starter, stator [F] | 86-92 |
| dry sump, net [E] | 2-4 |
| reduction gearbox, 408 N m at the propeller [E] | 8-15 |
| adapter and soft coupling [E] | 2-4 |
| second-lane FADEC, coils, sensor, harness [E] | 2.5-4 |
| second generator [E] | 2-4 |
| exhaust, intake, mount, pumps [E] | 9.5-17 |
| **installed dry, naturally aspirated** | **112-140** |
| with a normalizer | 126-161 |
| radiator, oil cooler, coolant system (radiator.py at 68-83 kW MCP) | 20-21 (1,760-2,290 cm^2 radiator, 1.2 % of MCP in cooling drag) |

**Against the comparators** (installed-dry definitions differ by vendor; COMPARABLE_ENGINES):

| Engine | Takeoff | Dry mass | kg per takeoff hp |
|---|---|---|---|
| Rotax 912 ULS (with gearbox) | 100 hp | 56.6 kg | 0.57 |
| Rotax 915 iS (incl. gearbox, turbo, intercooler, exhaust) | 141 hp | 82.2 kg | 0.58 |
| Aeromomentum AM15 | 120 hp | 83.9 kg | 0.70 |
| Viking 130 (contents not defined) | 130 hp | 99.8 kg | 0.77 |
| **Hayabusa conversion, NA** | **113-139 hp** | **112-140 kg** | **0.81-1.24** |
| Concept H, 200 hp | 200 hp | 148-158 kg | 0.74-0.79 |

**It misses R-37's proposed 90 kg for the 100 hp member by 22-50 kg**, and it is the heaviest per horsepower of everything in the table. The integral gearbox and clutch, which the drive does not use, are a large part of the reason. Emptying the gear clusters is a possible lever, worth a few kilograms [E], and is not taken.

## 7. Cost, first-engine basis (question 7)

`mass_cost_busa.py` section 2, on R-35's definition (parts and services; no labor, no propeller), basis 1.

| Line | low | high |
|---|---|---|
| used Gen 2 core [S, H24] | $3.0k | $3.8k |
| rebuild parts, 11:1 pistons, machine-shop inspection [S partial, E] | $2.2k | $3.8k |
| dry sump (SBD kit plus tank and lines) [S + E] | $1.9k | $2.3k |
| reduction gearbox, made [E] | $2.9k | $9.8k |
| adapter plate and hub, elastic coupling, engine mount (builder TIG) [MFG, AER-3526] | $2.8k | $9.2k |
| FADEC, two lanes [E] | $1.5k | $4.0k |
| second lane beyond the FADEC: second plug (MFG), coils, sensor, generator [MFG + E] | $2.8k | $8.9k |
| cooling, fuel, exhaust, intake, misc [E] | $1.9k | $4.6k |
| **Total, naturally aspirated** | **$19.0k** (mid $29.7k) | **$46.4k** |
| with a normalizer | $21.0k (mid $32.7k) | $50.9k |

- **Core availability is not the issue.** The eBay snapshot showed about 33 complete engines among 100 listings [H24]. **No new crate engine was found** at any price, so every build starts from a used core of unknown history. That is another reason for the teardown and crack test.
- **Builder labor: 240-510 hours** [E], about half of it the gearbox, harness and FADEC calibration; the mount alone is 40-80 h of TIG at skill B3 (MANUFACTURING).
- **Where the money goes.** The lines any engine in this program needs (gearbox, FADEC, cooling, fuel, exhaust, mount) are $9.8k-29.2k. The Hayabusa-specific part is $9.2k-17.3k.

**Against the yardsticks:**

| Engine | Price, as defined in its source | Takeoff |
|---|---|---|
| Aeromomentum AM15, incl. gearbox, starter, alternator, ECU | $13.0k-14.1k [A1] | 120 hp |
| Viking 130, no radiator or exhaust | $15.0k [V3] | 130 hp |
| **Hayabusa conversion, NA, first engine** | **$19.0k / $29.7k / $46.4k** | **113-139 hp** |
| Rotax 912 ULS | $26.5k (Australian dealer, basis not stated) [R7] | 100 hp |
| Rotax 915 iS | $51.6k ex-GST (same dealer) [R7] | 141 hp |
| Concept H, 200 hp, basis 1 (CASTINGS_H section 6) | $31.7k / $48.0k / $72.8k | 200 hp |

**The proposed 100 hp target of $15k (R-35, not ruled) is missed even at the low end.**
- The Hayabusa is under the Rotax 912's $26.5k only at its low estimate; the mid is $3k over and the high end $20k over.
- It beats the 915 easily. But the 915 makes its power to altitude with a turbo, so the fair comparison there is $21.0k-50.9k.
- It does not beat the two conversions that already fly.
- Per takeoff horsepower it is about level with concept H's first engine: about $140-410 per hp against $160-360.

## 8. What it means for the program (question 8)

Scores are out of 10: 10 means it does the role well.

| Role | Score | Why | Carries forward to concept H | Thrown away |
|---|---|---|---|---|
| **(a) Development mule** | **4** | It runs cheaply on a stand: about $9-17k of Hayabusa-specific spend on top of work the program does anyway. It is weak in flight: a drive must be designed first, the stock head cannot exercise R-25, and it has no field record. As a FADEC mule it is beaten by a bought conversion with a proven drive. As a gearbox mule it is the wrong size for H-EZ36 (408 against 558 N m at the propeller) and the wrong firing order (I4 against flat-6) | FADEC (70-80 %); the radiator, duct and pump method (hardware about 60 % of H's size); propeller matching and test instrumentation; the test stand; gearbox design method and lessons, not the gearbox | the core, the pistons, the dry sump, the adapter, the mount, the head work, Hayabusa-specific harness and calibration |
| **(b) The 100 hp member, or a starter product** | **2** | Costs more and weighs more than the AM15 and Viking 130 that builders can buy today. It needs a program-designed drive with no field record, misses R-37 by 22-50 kg, and may need an R-25 exception. Its life is unknown, and the most likely evidence-based interval is a few hundred hours. There is no new-engine supply: every product would be a used core. It also does not fit R-1 or R-28 (made from files), which Bill already knew | as (a) | the whole product line: support, documentation and liability for a conversion |
| **(c) A dead end** | **6** | Likely if it is taken on as the platform. The drive, the head work and a durability program on an engine the family will not use are a year or more of work [E] that delays H. Taken narrowly as a ground FADEC rig, it is not a dead end | as (a) | as (a), plus the schedule |
| **(d) Added: a ground mule matched to H's own risks** | **7, if Bill takes H-EZ36** | A used Subaru EZ36 behind the program's gearbox on a stand tests the actual donor crank in aircraft duty (FL-43), the right-size gearbox and the 6-cylinder torsional system. It carries the FADEC work as well as the Hayabusa would. Too heavy to fly as is. Not costed here | crank, gearbox and torsional evidence for H-EZ36, plus all of (a) | the EZ36 block and heads, if H keeps its own castings |
| **(e) Added: a FADEC flight mule on a bought conversion** | **7** | An AM15-class engine ($13.0k-14.1k) with its proven gearbox, flown with the program's FADEC in place of its ECU, is the fastest route to FADEC flight hours. It has the same single-plug R-25 limit as the Hayabusa, and no injector redundancy unless its injectors are doubled (not checked). Needs an airframe | the FADEC, cooling, propeller and instrumentation work | the bought engine (resaleable) |

## 9. What kills it (question 9)

The findings that would make me recommend against it, and whether I found them:

1. **No credible drive. Found.** There is nothing to buy. The one Hayabusa aircraft drove through a motorcycle clutch, and its builders blame that clutch for a fatal loss of power. Its first-mode tuning has to match the Rotax 912's softness, and it tolerates a stiffened coupling less well (section 4). That is solvable, but it is the program's own engineering, not a purchase. It is also the same work H-EZ36 needs at a different size.
2. **No cost advantage over a bought conversion. Found.** The low end ($19.0k) is above the AM15's price with gearbox and ECU ($13.0k-14.1k), and 28 kg heavier.
3. **R-25 unmet on the stock head. Open.** It is decided by a scrap-head survey (AER-3526). If the second plug cannot be fitted, the Hayabusa is a reduced-redundancy exception: 72 % of MCP and a torque-reversal band after one coil failure.

## 10. Failure ledger

Added to `FAILURE_LEDGER.md`, each conditional on a Hayabusa route being taken:
- **FL-51:** the soft coupling stiffens with age.
- **FL-52:** a dead cylinder on a single-plug head.
- **FL-53:** a motorcycle clutch in the torque path (the Bugatti 100P case).
- **FL-54:** the cam chain and tensioner.
- **FL-55:** wet-sump oil surge and hot oil.
- **FL-56:** a single charging path.
- **FL-57:** knock at the stock compression ratio.
- **FL-58:** Gen 3 ride-by-wire.
- **FL-59:** the bottom end with no aviation hours.
- **FL-60:** the second-plug sleeve in a modified head (seat-insert ligament, sleeve leak).

## 11. What this pass did not do

- **No core was weighed, measured or run.** The engine mass (86-92 kg) is forum-only. No head was sectioned, so the second-plug question is open. Both are cheap to settle with one scrap core, but that is a purchase, and this pass was analysis only.
- **No quotes.** The gearbox is the program's [E]. The adapter, hub, coupling, mount and head work are MANUFACTURING's envelope estimates from **AER-3526** (2026-10-19), not quotes. None has a drawing behind it yet: the mount needs PROPULSION's mount-point drawing and an isolator stiffness, the head work a hole drawing after the section.
- **No crank-dyno curve.** The aircraft torque curve is a rear-wheel dyno divided by 0.94, anchored on Suzuki's 149 N m claim.
- **No Gen 3 injector flow, crank trigger pattern or limp-home throttle position** was found.
- **The torsional model** is two inertias with assumed inertias, an assumed rod length and an assumed coupling damping (zeta 0.08). It gives ratios between engines, not stresses. It does not include the crank's own modes, gear backlash or the propeller blades.
- **The durability bracket** rests on forum-quoted Radical intervals and an assumed wear law.
- **NTSB CAROL** was not searched directly, and neither were the AAIB or BFU. The NTSB final report on CEN16FA307 was read through quotes on other sites.
- **The EZ36 and AM15 mule roles (d) and (e) are scored, not costed.** The AM15's injector layout was not checked.

## 12. Bill's call

**Drop the Hayabusa as the starting platform, and if you want an early flying FADEC test bed, carry the program's FADEC on a bought conversion instead?** I recommend yes. The Hayabusa costs more and weighs more than the AM15 or Viking 130 once it has a drive and two lanes, the drive would be ours to invent, and its one aviation precedent was lost. If Bill wants to keep it, the cheapest next step is one scrap core, weighed and with its head sectioned: that settles the mass and the second-plug question for about $0.3k-1.7k (MANUFACTURING: two scrap heads and a section). The question is on AER-3525 as a card.
