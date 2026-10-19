# Suzuki Hayabusa: durability under sustained high load, and feasibility of dual-lane control

Research date (read date for every source): **2026-10-19**. Each claim cites a source number [n] from the list at the end.

Labels used:
- **forum**: a claim posted on a user forum. It is not verified by a manufacturer.
- **snippet**: the target page blocked fetching (403/410/429). The quote comes from the search-engine summary of that page.
- **unverified (memory)**: not found in a source this session.
- **calc**: arithmetic done in this note.

---

## Part A: Durability

### A1. Racing cars: rebuild intervals and power

| Application | Engine / power | Rebuild interval | Type of source | Ref |
|---|---|---|---|---|
| Radical SR3, 1500 (RPE, Suzuki-based) | 1500 cc. Wikipedia lists the SR3 RSX at "256 bhp (260 PS; 191 kW)". | "Under race conditions, the engine should run for no more that 40 hours before being returned to the factory for a rebuild" and "Engines which are not raced, regularly cover 90 hours without requiring attention". "Warranty is valid up to a maximum of 40 hours of total running time" counts total run time, not only time on load. | forum quoting Radical warranty text | [1], [3] |
| Radical SR3, 1340 | "205 bhp (208 PS; 153 kW) @ 9,500 rpm" | "The 1500 engines require overhauls every 40 hours but the 1340's are less stressed and can go 90 to 100 hours between overhauls." The Spring Mountain shop recommends 80 h for the 1340. One owner says some have stretched to 200 h. | forum (registry admin CharleyH) | [2], [3] |
| Radical rebuild cost | n/a | "A certified shop will cost you between $6k and 10k ... the Gear Drive Unit overhauled ... between $2k and 4k" | forum | [2] |
| Contents of a Radical 1500 rebuild | 1500: "stroked crank, clutch basket, and valve train changes". About 13.5:1 CR, against 12.5:1 for the 1340. | Parts replaced in one 1500 overhaul: "new 1st gear (driven), 2nd gear (driven), 5th gear (output H/D), 6th gear (output H/D)...clutch plates...all of the bearings...cam chain and...cam chain guides. ... very common for the starter clutch cover to be replaced due to cracking." | forum | [4] |
| Radical SR3 1500 Turbo | "Powertec Inline-four Turbocharged", "316 bhp (320 PS; 236 kW)" | not found | Wikipedia | [3] |
| Powertec RPA V8 (SR8) | Two Hayabusa-pattern heads on a Powertec block. 2.7 L makes 430 hp, 3.2 L makes up to 500 hp. | Wikipedia does not give one | Wikipedia | [5] |
| Westfield Megabusa / Caterham Hayabusa | Mistral 1400 then 1540 (Caterham) | No published interval. Owners report: "Road use should never kill a Hayabusa if maintained". Failures come from "oil starvation, lack of maintenance or serious track abuse". One full engine and gearbox refresh cost £3,500. | forum (snippet), SBD customer story | [6], [7] |
| Dallara hillclimb, Hayabusa 1585 cc | SBD throttle bodies, MBE9A4 | "the whole engine/SBD/MBE package has been pretty much fault free"; "16 runs altogether" at Harewood | vendor customer story | [8] |
| Formula 1000 / F1000 | n/a | **Not found.** Searches tried: "Formula 1000 F1000 SCCA Hayabusa engine rebuild interval hours". | n/a | — |
| Sidecar (F1 / F2) and 24 h endurance with a Hayabusa | n/a | **Not found.** Searches tried: "sidecar racing Hayabusa engine F2 OR endurance 24 hour Hayabusa engine reliability". One search summary claimed a Yoshimura SERT "Hayabusa" won Le Mans 24 h. That is a search-summary error: SERT raced the GSX-R1000 (unverified (memory)). The claim is excluded. | n/a | — |
| BAC Mono | n/a | Not a Hayabusa engine. BAC uses Ford-based Mountune/Cosworth engines (unverified (memory)). Not researched. | n/a | — |

**Takeaway.** The best published evidence of hours at high load comes from Radical's warranty and rebuild rule as quoted by owners: **40 h total run time** for the high-compression 1500, and **about 80 to 100 h** for the 1340. This is at about 200 to 260 bhp in cars weighing about 500 to 570 kg. At rebuild, the parts found worn are the gearbox (gears 1, 2, 5, 6), clutch, all bearings, the cam chain and its guides, and a cracked starter-clutch cover [2][4].

### A2. Failure modes by generation

| Failure mode | Generation | Evidence | Frequency | Community fix | Ref |
|---|---|---|---|---|---|
| Cam chain tensioner spring breaks, chain jumps teeth, valves hit pistons | Gen1, 1999 to 2000 | NHTSA 99V270000 covered about 2,670 units. It was superseded by 00V319000: "the spring in the cam chain tension adjuster can break. excessive slack will develop in the cam chain, allowing the chain to jump". The fix was "a new oil-damped ratchet-type cam chain tension adjuster ... new tension adjuster oil supply hose and a new cam chain guide." | 8,511 units recalled under 00V319000 | Fit the recall tensioner. Racers fit an APE manual tensioner (forum). | [9], [10] |
| Cam chain and guide wear in race cars | Gen2 (K8) and RPE | "Many of the engine failures that I have heard about were due to either transmission failure or cam chain related." A DSR-forum thread is titled "K8 Hayabusa Cam/Timing Chain Failure"; it returned 403 and could not be read. | not stated | Replace the chain and guides at each rebuild | [4], [11] |
| Second gear jumps out (dogs wear) | Gen1 mainly | "The Gen1 engine has 4 dog engagement, the gears are not undercut on the 2/6 drive dogs. This is where most of the problems occurred"; "Gen2 engine has 5 dog engagement and undercutting on the 2/6 drive dogs" | "most of the problems" (forum) | Undercut the gears (APE, Schnitz). Caveat: "The transmission needs to have no damage on it". | [12] forum |
| Rod bearing spun | all; race cars | "I spun a rod bearing (Cyl 1)" (Radical owner). The DSR "conrod blow up" and "Oiling Issue" threads returned 403. Snippet from [13]: the stock low-oil-pressure switch "comes on around 10 psi" and an Accusump fixed a Radical's oiling problem. | anecdotal | Dry sump or Accusump, an oil pressure gauge with an alarm, and oil kept at 80 to 100 °C | [4] forum, [13] forum (snippet) |
| "#2 rod bearing" as a named pattern | — | **Not found.** Searches tried: "Hayabusa spun rod bearing common cause...", "Hayabusa rod bearing failure oil starvation land speed Bonneville". | — | — | — |
| Oil surge or starvation under sustained lateral or braking g | all wet-sump car installs | "The hayabusa is the one engine we and many others have failed to control with billet wet sumps"; "the swinging pick up sump will not suffice"; "if you want total peace of mind go dry sump" (Andy B, sump maker). One Radical owner: dry sumped and "never once had an issue with oil pressure." | not stated | Dry sump | [14] forum |
| Oil pressure drops at high oil temperature | all | SBD: 80 to 100 °C gives "in the region of 7psi" at idle and a "60 – 70psi" peak. At 120 °C or more, idle can fall "as low as 2psi" and peak "down to 35psi". | — | Oil cooler; keep oil at 80 to 100 °C | [15] |
| Regulator/rectifier fails (charging) | Gen2, 2008 to 2010 | Suzuki recall 11V108: "insufficient adhesion between the power module and the rectifier case ... can lead to engine stalling and/or a no-start condition." | recall | Fit the revised R/R. Many owners move to a MOSFET R/R (unverified (memory)). | [16] |
| Stator failure | all | Only generic statements found. No Hayabusa-specific rate. | not found | — | [17] snippet |
| Turbo engine fails during a land-speed return run | Gen1/Gen2 turbo | Jim Cole, 2021 BMST: "the engine finally let go" on a return run near 209 mph. No cause given. | single event | — | [18] |
| Turbo head gasket, pistons, rings | turbo | **No Hayabusa-specific source found.** Searches tried: "Hayabusa turbo head gasket failure copper gasket O-ring head studs boost". The results were generic or for other engines. One build used "ARP cylinder/head studs" (snippet, [19]). | — | Copper gasket with O-ring, ARP studs (generic practice) | — |
| Valve or seat problems | — | **Not found** as a Hayabusa pattern. Radical rebuilds include valve work [2]. | — | — | — |

### A3. Turbo durability

| Build | Boost / power | Parts changed | Durability evidence | Ref |
|---|---|---|---|---|
| Stock-internal guidance | — | "Your stock pistons can handle 500 hp, rods 300 hp and clutch with heavy duty springs 300 hp." | forum (T 24, gsx1400owners, 2019) | [20] |
| NLR "Hayaboosta" street turbo (2002) | "12-14 psi" normally and "18 psi" on a button; about 340 to 350 bhp | water-cooled intercooler | "the key to a reliable turbo bike is an intercooler". No mileage given. | [21] |
| Palatov turbo track car | 6 psi gave 225 hp at 10,000 rpm. Target 350 to 400 hp at an 11,000 rpm redline. | New low-CR pistons, "Carillo connecting rods", dry sump | Power kept at about 400 hp to meet "endurance and durability goals" | [22] |
| Hass compound-turbo land-speed engine | "564 horsepower at only 18 pounds of boost", methanol | billet crank, Carrillo rods, JE pistons, ZX14-journal coated bearings, about 110 lb valve springs | Bearings changed to "help the bearings survive" | [23] |
| Vance & Hines streamliner | turbo 1300, "expected to make 500 or 600 horsepower" | — | Dyno tested. No duration given. | [24] |

- **Long-duration turbo use, or a steady-state dyno pull longer than 1 minute: not found.** Searches tried: "Hayabusa turbo land speed Bonneville sustained full throttle...", "Hayabusa turbo street build 10 psi stock bottom end how long miles reliable forum".
- The closest evidence of sustained turbo running is the Radical SR3 1500 Turbo at 316 bhp [3]. No interval for it was found.

### A4. Generator, marine, airboat, hovercraft, industrial, or aircraft use

**Not found** with service hours. Searches tried:
- "Hayabusa airboat OR hovercraft engine hours reliability"
- "\"Hayabusa\" airboat engine"
- "Hayabusa generator OR power plant OR marine OR jet boat engine Hayabusa hours service"
- "Suzuki Hayabusa engine powered aircraft homebuilt reduction drive flying"

The only related hit was a Hayabusa-powered jet-ski novelty article, with no hours given [25].

### A5. Suzuki service schedule

| Item | Gen2 (2008 to 2020) | Gen3 (2021+) | Ref |
|---|---|---|---|
| Oil and filter | 6,000 km / 4,000 mi | "every 3750 miles or 6000 km" | [26], [27] |
| Spark plugs | Replace at 12,000 and 24,000 km. Spec NGK CR9EIA-9. | every 2 services, about 12,000 km | [26], [27] |
| Valve clearance | inspect at 24,000 km / 14,500 mi | "every four services, or 15000 miles / 24000 km" | [26], [27] |
| Coolant | "every 4 years or 48,000 km" | — | [26] |

These figures come from a secondary site that says it is quoting the Suzuki owner's or service manual. The manual itself was not read.

### A6. Oiling

- **Wet-sump capacity.**
  - Amsoil lookup (snippet; the page returned 403): 2009 Gen2 1300 is "3.5 quarts", about 3.3 L. 2025 Gen3 is "4.3 quarts with filter change", about 4.1 L [28].
  - These figures need checking against the manual. A Gen2 total of about 4.0 to 4.4 L is unverified (memory).
- **Sump depth: not found.**
- **Gen3 changes:** "54% more oil flow to the crankshaft", and oil jets on gears 4, 5 and 6 [29].

| Dry-sump vendor | Product | Price | Status | Ref |
|---|---|---|---|---|
| SBD Motorsport (UK) | OS-DSK-BUSA-02: billet pan, twin-stage scavenge pump, remote PRV, Gen1/Gen2 | £1,160 ex VAT / £1,392 inc VAT | in production | [30] |
| Armstrong Race Engineering | "Hayabusa / Suzuki 1400 DSR" cast pan | not listed | "NO LONGER IN PRODUCTION" | [31] |
| Dailey Engineering | Hayabusa kit | not found. Dailey kits for other engines cost $4,699 to $9,945 (snippet). | not confirmed for Hayabusa | [32] snippet |
| Pace Products, Arias | — | not found | — | — |
| Radical | Radical cars are dry-sumped | forum: "My radical hayabusa is dry sumped" | — | [14] |

Why racers fit a dry sump: the stock and billet wet sumps cannot control oil surge in hard cornering and braking. Swing pickups "will not suffice". An Accusump is "a sticking plaster" [14].

---

## Part B: Dual-lane feasibility

### B7. Twin-plug heads

- **Hayabusa twin-plug head (commercial or one-off): not found.** Searches tried:
  - "Hayabusa twin spark plug head second spark plug per cylinder"
  - "\"Hayabusa\" \"dual ignition\" OR \"twin plug\" OR \"two spark plugs\" aircraft OR drag OR \"land speed\" head"
- **Stock plug thread.** NGK CR9EIA-9: "Thread Diameter: 10 mm", thread length 19 mm, hex 16 mm. It fits "SUZUKI GSX1300R HAYABUSA 2008–2022" [33]. Gen1 also uses an M10 plug (CR9E), unverified (memory).
- **Space for a second plug between the valves in the pent-roof: no source found.**
  - In a 4-valve pent-roof with a centre plug, a second plug normally has to go at the chamber edge, between an intake and an exhaust valve or near the squish band, from the side of the head.
  - On the Hayabusa that side area holds cam-chain or coolant passages. This is unverified (memory) and needs measurement on a sectioned head.
- **Precedent for twin plugs in 4-valve motorcycle heads:**
  - **Ducati Testastretta 11° DS**, 4-valve L-twin: "twin-plug cylinder heads for smoother, more efficient combustion" [34]. Ducati says each plug is "managed independently" (snippet of [35]; the page had an expired certificate).
  - **BMW R1200 hexhead (4-valve boxer)**, twin-spark: "the auxiliary spark plug ... arranged at the outer edge of the cylinder"; "primaries fire just before TDC but secondaries fire at TDC" [36] (snippet, forum and magazine).
  - **KTM 690 LC4 (4-valve single)**: "twin ignition featuring plug-selective mapping" [37] (snippet).
  - **Rotax 912 iS / 915 iS (aviation)**: two plugs per cylinder; see B9.
  - **Aprilia** 4-valve twin-plug: forum thread title only [38].

### B8. Injectors

| Gen | Injectors | Flow | Staging | Ref |
|---|---|---|---|---|
| Gen1 (1999 to 2007) | 4 | 330 cc/min | none | [39] |
| Gen2 (2008 to 2020) | 8: "4x primary and 4x secondary injectors that are staged" | 280 cc/min each | The upper injectors are used "above 7000rpm and gives an increase of approximately 5bhp" | [39], [40] |
| Gen3 (2021+) | "Four primary fuel injectors that spray ... into the intake pipes. Four additional Suzuki Side Feed Injectors (S-SFI) are set above the throttle body in the side of the intake funnels." | not found | Staging schedule not found | [29], [41] |

- **Can one set alone supply full power?**
  - SBD: "there was no advantage in running 8 injectors" on Gen1, and Gen2 gains only about 5 bhp from the uppers [40].
  - **calc:** 4 × 280 = 1,120 cc/min for the Gen2 primaries. Inputs, all unverified (memory): about 145 kW, BSFC about 0.30 kg/kWh when rich at full throttle, petrol density 0.74.
  - That gives about 44 kg/h ≈ 59.5 L/h ≈ 990 cc/min, so about **88 % duty on the primaries alone at full power**. That is marginal.
  - At a moderate cruise load (about 50 to 60 %), one set at about 45 to 55 % duty would be enough.
  - The upper set alone would also flow 1,120 cc/min. However, it sprays into the bellmouth, so mixture response and atomisation differ at low load. There is no test data.
  - **A lane split by injector set (lane A = primaries, lane B = secondaries) is physically plausible on Gen2 and Gen3, but no source has demonstrated it.**
- **Aftermarket parts:**
  - Injector Dynamics ID1050X, ID1300X and ID1750X sold as "Hayabusa Gen 2 – 8 injector" sets [42].
  - Power Commander V "secondary fuel module" for 2008 to 2016 [43].
  - MoTeC GPR supports "two injectors per cylinder" [44].

### B9. Standalone ECUs and the Rotax lane architecture

| ECU | Hayabusa support | Price | Redundant / dual ECU | Ref |
|---|---|---|---|---|
| MoTeC M1 GPR Motorcycle package | Generic port-injected motorcycle package. Supports "two injectors per cylinder". No Hayabusa-specific package found. | M141 ECU $3,995 (GSpeed). Package licence extra. | Firmware failover for dual reference sensors only. No dual-ECU failover found. | [44], [45], [46] |
| Haltech Elite (2-connector) | Haltech KB article "Hayabusa" for Gen1/Gen2. The OEM igniter is inside the stock ECU, so an "external igniter (such as a Haltech HPI4) is required". | not found | not found | [39] |
| MBE 9A4 (via SBD) | "Hayabusa Gen1 1300-1600cc ECU & Wiring Harness" | £1,231.50 ex VAT | not found | [47] |
| AEM Infinity 30-7106 + harness 30-3550 | Plug and play for 2002 to 2007 | discontinued; price not found | not found | [48] snippet |
| Link G4X/G5 | No Hayabusa plug-in found. Wire-in only. | not found | not found | — |
| MaxxECU | No Hayabusa plug-in found | not found | not found | — |
| Speeduino | No Hayabusa material found | — | — | — |
| rusEFI | No Hayabusa material found | — | A forum concept for two units, active plus standby, with diode-OR outputs. "Having 2 ECUs connected to the same sensor will skew values for both". rusEFI is "only endorsed for off-road use and for non-aviation purposes". | [49] forum |

**Rotax 912 iS lane arrangement (the 915 iS is described as similar but was not checked in its own manual).** Source: official Rotax Installation Manual, 912 i Series, Ed.2 Rev.1, Feb 2020 [50].

- **ECU, ch. 76-00-00 p.2.** "The core of the EMS is the engine control unit (ECU), which consists of two modules. These modules will be denoted by LANE A and LANE B, each one capable of taking over control, regulation and monitoring of the engine. In error-free engine operation, both LANES are turned ON. During engine control by LANE A, LANE B ensures that the engine operation can be maintained after a failure..."
- **Sensors and actuators.** "A huge quantity of sensors ... and actuators (e.g. ignition coils) of the engine is designed with redundancy. In this case, each of the sensors or actuators is connected to a LANE ... Non-redundant sensors (e.g. oil pressure sensors) are connected to one LANE only".
- **Power.** "The generator (generator A or generator B) always supplies the complete EMS (both LANES A and B). The assumption that generator A supplies LANE A and generator B supplies LANE B is false."
- **Ignition, ch. 74-00-00 p.2.** "It is completely doubled up. Either of the ECU's can operate the double ignition coils."
- **Fuel, ch. 73-00-00 p.2.**
  - "two electric pumps connected in series with bypass valves and engine will operate with either one or both pumps running."
  - "There are 2 injectors per cylinder (8 in total). During engine run both injectors per cylinder are in operation. If a failure is detected in any one injector the injection period of the other one on that cylinder is adjusted for compensation. The ECU operates all fuel injectors."
  - "Parallel hydraulic operation of the fuel pumps is not permitted."
- **Forum detail** (rotax-owner.com, N. Kurtz / Jeff B) [51]:
  - Lanes are power buses split at the fuse box. X1 feeds "ignition coils, injectors, fuel pump 1, Lane A ECU computer"; X2 feeds the same for Lane B.
  - "the ECU does not power the ignition coils or the injectors; it controls them (via low-side switching)".
  - Pump 1 is on fuse F4 and pump 2 on F5.
  - Snippet: "spark plugs 1B-4B assigned to Lane A and 1T-4T assigned to Lane B".
  - The same thread says "there is no technical document explaining these details".
- **Kitplanes, 912 iS** [52]: "two automotive-type spark plugs per cylinder", "four coils mounted on top of the cylinders", and "two electric pumps contained in a single housing".
- **915 iS** (Wikipedia [53]): "dual channel Rockwell Collins ECUs", "dual ignition". TBO "started at 1200 hours".

**Implication.** Rotax's design is not two fully separate ECU-plus-actuator chains. It is one dual-module ECU with cross-strapped control: either lane can drive all coils and all injectors. Power buses are split per lane, there are two plugs per cylinder, and each cylinder has two injectors that both run in normal operation.

### B10. Fuel pumps

- **Hayabusa pressure.**
  - "The standard pressure is 3.2 bar" (forum, Locost) [54].
  - Snippet from DSR-forum search results: "Stock Hayabusa fuel systems are limited to 43psi", about 2.96 bar [55].
  - The Suzuki manual value was not read. About 300 kPa is unverified (memory).
- **Aviation dual-pump practice.**
  - Rotax: two electric pumps in series with bypass valves; the engine runs on either; "Parallel hydraulic operation ... not permitted" [50].
  - 14 CFR 23.955: each fuel system must ensure flow "at a rate and pressure established for proper engine ... functioning under each likely operating condition" (snippet) [56].
  - A rule specifically requiring two pumps was not located.

---

## Gaps

1. No published Radical **document**: the 40 h and 90 h figures are owners quoting Radical warranty text. No F1000, sidecar or endurance intervals were found.
2. No steady-state (more than 1 min) dyno data, and no long-duration turbo data.
3. No generator, marine, airboat, hovercraft or aircraft Hayabusa use with hours.
4. No Hayabusa twin-plug head exists in any source. Space for a second plug, and the head's water and oil passages, need physical measurement.
5. Gen3 injector flow and staging schedule not found. Whether one injector set alone can carry full power is a calculation only.
6. Suzuki manual not read directly for the service schedule, oil capacity, sump depth or fuel pressure.
7. Dailey, Pace and Arias Hayabusa dry sumps not confirmed. Link, MaxxECU, Speeduino and rusEFI Hayabusa support not confirmed. No commercial dual-ECU failover product was found in the motorsport ECUs.
8. Several DSR-forum threads (oiling, conrod failure, K8 cam chain) returned 403. Their content is known only from search snippets.

---

## Sources (all read 2026-10-19)

1. https://radicalsportscarregistry.com/radicalforum/general-discussion/engine-hours-until-refresh/ (forum). "Under race conditions, the engine should run for no more that 40 hours before being returned to the factory for a rebuild"
2. https://radicalsportscarregistry.com/radicalforum/getting-started/why-do-the-engines-need-a-rebuild-every-40-hours/ (forum). "The 1500 engines require overhauls every 40 hours but the 1340's are less stressed and can go 90 to 100 hours"
3. https://en.wikipedia.org/wiki/Radical_SR3. "205 bhp (208 PS; 153 kW) @ 9,500 rpm"; "316 bhp (320 PS; 236 kW)"
4. https://radicalsportscarregistry.com/radicalforum/general-discussion/hayabusa-engine-questions-reliability-and-rebuilds/ (forum). "Many of the engine failures that I have heard about were due to either transmission failure or cam chain related."
5. https://en.wikipedia.org/wiki/Powertec_RPA. "loosely based on the 1.3 litres ... inline-four engine produced by Suzuki for their Hayabusa"
6. Westfield forum search results (snippet): https://forum.wscc.co.uk/forum/topic/135702-westie-megabusa-yes-or-no and https://www.locostbuilders.co.uk/viewthread.php?tid=190448. "failure usually coming from oil starvation, lack of maintenance or serious track abuse"
7. https://sbdmotorsport.co.uk/cars/caterham-hayabusa/. "Darren now has a 1540cc Mistral built Hayabusa in his Caterham"
8. https://sbdmotorsport.co.uk/cars/dallara-hayabusa-extreme/. "the whole engine/SBD/MBE package has been pretty much fault free"
9. https://www.vehiclesafetyrecalls.com/recall/99V270000 (snippet). "The spring in the cam chain tension adjuster can break"
10. https://www.vehiclesafetyrecalls.com/recall/00V319000. "a new oil-damped ratchet-type cam chain tension adjuster"
11. https://www.tapatalk.com/groups/dsrforum/k8-hayabusa-cam-timing-chain-failure-t7817.html (forum; 403, title only). "K8 Hayabusa Cam/Timing Chain Failure"
12. https://www.locostbuilders.co.uk/forum/3/viewthread.php?tid=191667 (forum). "Gen2 engine has 5 dog engagement and undercutting on the 2/6 drive dogs"
13. https://www.tapatalk.com/groups/dsrforum/oiling-issue-t9713.html (forum; snippet, 403). "low oil pressure switch that comes on around 10 psi"
14. https://www.locostbuilders.co.uk/viewthread.php?tid=194096 (forum). "The hayabusa is the one engine we and many others have failed to control with billet wet sumps"
15. https://sbdmotorsport.co.uk/ufaqs/hayabusa-oil-temperature-oil-pressure-levels. "as low as 2psi"
16. https://static.nhtsa.gov/odi/rcl/2011/RCMN-11V108-7900.pdf. "insufficient adhesion between the power module and the rectifier case"
17. https://www.justanswer.com/car/tan3v-hayabusa-suzuki-charging-issues.html (snippet). "overheating can cause failure and battery drain"
18. https://www.fim-moto.com/en/news/news-detail/article/tough-luck-and-lessons-learned-at-day-2-of-bonneville-motorcycle-speed-trials. "the engine finally let go"
19. https://grassrootsmotorsports.com/reader-rides/8755/2970/ (snippet). "ARP cylinder/head studs, and heavier valve springs". The search summary did not tie this quote to a single URL. This is the most likely page, but the attribution is uncertain and the page was not fetched.
20. https://gsx1400owners.org/forum/index.php?msg=55636 (forum). "Your stock pistons can handle 500 hp, rods 300 hp"
21. https://magazine.cycleworld.com/article/2002/2/1/hayaboosta. "the key to a reliable turbo bike is an intercooler"
22. https://www.enginelabs.com/?p=8013. "endurance and durability goals"
23. https://www.enginelabs.com/news/compounding-boost-in-a-hayabusa-land-speed-engine/. "564 horsepower at only 18 pounds of boost"
24. https://cycleworld.com/2014/02/06/streamliner-on-the-dyno-sam-wheeler-prepares-to-challenge-land-speed-record-at-bonneville. "expected to make 500 or 600 horsepower"
25. https://www.6speedonline.com/articles/yes-hayabusa-powered-jet-ski-thing-awesome/ (title only, not fetched)
26. https://maintenanceschedule.com/suzuki-hayabusa-gen-2-2008-2020-maintenance-schedule/. "Replace every 4 years or 48,000 km"
27. https://maintenanceschedule.com/?p=15776. "every four services, or 15000 miles / 24000 km"
28. https://www.amsoil.com/lookup/motorcycle/2009/suzuki/gsx-hayabusa/1300/ and https://www.amsoil.com/lookup/motorcycle/2025/suzuki/gsx-1300r-hayabusa/1340/ (snippet, 403). "4.3 quarts with filter change"
29. https://www.webbikeworld.com/2022-suzuki-hayabusa/. "54% more oil flow to the crankshaft"
30. https://sbdmotorsport.co.uk/?p=9290. "Pump removal in situ – no need to remove sump"
31. https://drysump.com/hayabusa-suzuki.htm. "NO LONGER IN PRODUCTION"
32. https://gspeed.com/products/gspeed-4-5-stage-dailey-dry-sump-kit (snippet; Dailey price range for other engines)
33. https://takatalo.fi/de/p79634/ngk-spark-plug-cr9eia-9. "Thread Diameter: 10 mm"
34. https://en.wikipedia.org/wiki/Ducati_Multistrada_1200. "twin-plug cylinder heads for smoother, more efficient combustion"
35. https://www.asphaltandrubber.com/news/second-generation-ducati-testastretta-11-dual-spark-plug/ (snippet; certificate expired). "each spark plug managed independently"
36. https://www.ukgser.com/community/threads/twin-spark-coils-position.384715/ and https://issues.cycleworld.com/article/2004/5/1/surge-protection (snippet). "arranged at the outer edge of the cylinder"
37. https://en.wikipedia.org/wiki/KTM_690_series (snippet). "twin ignition featuring plug-selective mapping"
38. https://forums.autosport.com/topic/6249-aprilia-4-valves-2-sparkplugs-per-cylinder (forum, title only)
39. https://support.haltech.com/portal/en/kb/articles/hayabusa. "8x injectors. 4x primary and 4x secondary injectors that are staged"
40. https://sbdmotorsport.co.uk/ufaqs/whether-to-use-4-or-8-injectors-on-hayabusa-engines/. "only increases performance when the upper injectors are used above 7000rpm"
41. https://www.globalsuzuki.com/motorcycle/smgs/products/2022hayabusa/. "dual fuel injectors feeding each cylinder"
42. https://www.t1racedevelopment.com/product/id1050x-hayabusa-gen-2/. "Hayabusa Gen 2 – 8 injector"
43. https://www.sportbiketrackgear.com/dynojet-suzuki-gsx-1300r-hayabusa-08-16-power-commander-v-secondary-fuel-module/ (title)
44. https://motec.com.au/products/GPR%20Motorcycle?catId=15 (snippet). "quad cam boosted engine with two injectors per cylinder"
45. https://gspeed.com/products/m141-ecu. "$3,995.00"
46. https://help.motec.com.au/m1/tune/1.5/Topics/MoTeC_System_Overview_1.5.html (snippet). "two Reference Sensor inputs for fail over protection"
47. https://sbdmotorsport.co.uk/product/mbe-busa-kit-1-01-hayabusa-gen1-1300-1600cc-ecu-wiring-harness/. "£1,231.50"
48. https://www.holley.com/products/discontinued_product/parts/30-3550 (snippet, 403). "Plug & Play Adapter Harness (PN 30-3550) for the 2002-2007 Suzuki GSX1300R"
49. https://www.rusefi.com/forum/viewtopic.php?p=50974 (forum). "Having 2 ECUs connected to the same sensor will skew values for both"
50. https://www.rotax-owner.com/pdf/IM_912_iSeries_ED2_R1.pdf. Rotax Installation Manual 912 i Series Ed.2 Rev.1. "Either of the ECU's can operate the double ignition coils." "The ECU operates all fuel injectors."
51. https://r3.rotax-owner.com/en/912is-technical-questions/11220-basic-description-of-generator-and-lane-system-operation?start=20 (forum). "the ECU does not power the ignition coils or the injectors; it controls them"
52. https://www.kitplanes.com/rotax-factory-tour/. "two automotive-type spark plugs per cylinder"
53. https://en.wikipedia.org/wiki/Rotax_915_iS. "dual channel Rockwell Collins ECUs"
54. https://locostbuilders.co.uk/viewthread.php?tid=173705 (forum). "The standard pressure is 3.2 bar"
55. https://www.tapatalk.com/groups/dsrforum/hayabusa-fuel-pressure-t2497.html (forum; snippet). "limited to 43psi"
56. https://www.govinfo.gov/content/pkg/CFR-2013-title14-vol1/pdf/CFR-2013-title14-vol1-sec23-955.pdf (snippet). "fuel flow at a rate and pressure established for proper engine ... functioning"
