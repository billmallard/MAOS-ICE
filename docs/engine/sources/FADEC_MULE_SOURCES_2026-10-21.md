# Sources for FADEC_MULE.md (AER-3631), retrieved 2026-10-21

Two research passes, public web only, no vendor contact and no quotes (AER-3330). Part A covers the engines, part B the airframes and FAA rules, part C the few sources PROPULSION added. Tags: **[S]** vendor or official, **[F]** forum, listing, magazine or other secondary, **[nf]** not found, **[inf]** an inference, not a sourced fact. Pages that returned 403 are marked "snippet": the fact comes from a search-engine excerpt only.

---

# Part A. Engines

Research date: 2026-10-21. Public web only, no vendor contact.
Tags: **[S]** = vendor or official source (vendor site, vendor manual, NTSB, open-source code). **[F]** = forum or secondary press. **[nf]** = not found. **[inf]** = my inference, not a sourced fact.
Source keys refer to the numbered list at the end. Where a page could not be fetched (HTTP 403) and the fact comes only from a search-engine snippet, it says "(snippet)".

---

### 0. The Viking 130 is Honda-based, not Mitsubishi-based (a correction to the research prompt)

- The Viking 130 is a **Honda Fit 1.5 L, 4-cylinder, direct-injected** engine [S: VK1, VK3, VK8].
- The only Mitsubishi-based Viking is the **Viking 90**, a 1.2 L 3-cylinder Mitsubishi Mirage engine [S: VK4, VK8, VK10]. That engine is the 3A92 family [inf: Mirage 1.2 L 3-cyl; the code is not stated by Viking].
- The Viking 140T uses a GM 1.2 L turbo 3-cylinder (Chevrolet Trax / Buick Encore / Opel) [S: VK8].
- The Viking 150, 175 and 195T are Honda engines [S: VK5, VK6, VK7, VK8].

---

### 1. Summary table (vendor list figures)

| Engine | Donor | Price (USD) and contents | Mass (vendor figure) | Rating | Ratio | ECU |
|---|---|---|---|---|---|---|
| Aeromomentum AM13 | Suzuki G-series 1.3 L SOHC 16V I4 (1298 cc, 74x75.5, CR 10.1) [S AM2, AM9] | $11,500 (bed mount, 2-gear) to $12,600 (aft mount, 3-gear). Includes engine, gearbox, starter, alternator, ECU, wiring and mounting ears [S AM2] | 170 lb "dry" [S AM2] | 105 hp @ 5800 (prop 2240) [S AM2]; older page: 100 hp, with options of 112 hp @ 5800 and 126 hp @ 6500 [S AM2 old URL ?p=161] | 2.588:1, gearbox "rated to 225 hp" [S AM2] | MicroSquirt, single [S AM9] |
| Aeromomentum AM15 | Suzuki G-series 1.5 L SOHC 16V (1497 cc, 75x84.5, CR 9.5) [S AM3, AM9] | $13,000 to $14,100, same contents [S AM3] | 185 lb dry (upright) [S AM3] | 120 hp @ 5800 (prop 2240) [S AM3]; the page title says "117 hp to 147 hp" | 2.588:1 [S AM3] | MicroSquirt, single [S AM9] |
| Aeromomentum AM13T | 1397 cc "16V DOHC", turbo; donor not stated [S AM4] | $16,100 to $17,200 [S AM4] | 200 lb [S AM4] | 140 hp @ 5800 [S AM4] | 2.588:1 [S AM4] | "FADEC", semi-sequential [S AM4] |
| Aeromomentum AM15T | 1497 cc "16V DOHC" turbo [S AM5] | $17,700 to $18,800 [S AM5] | 215 lb [S AM5] | 160 hp @ 5800 [S AM5] | 2.588:1 [S AM5] | "FADEC" [S AM5] |
| Aeromomentum AM20T | 1998 cc, 86x86, DOHC 16V, CR 10.5; donor not disclosed [S AM6, AM14] | $27,995; 300 hp version $29,700 [S AM6] | 285 lb [S AM6] | 260 hp @ 5800; 300 hp @ 6200 with a 5-minute limit [S AM6] | not stated [nf] | "EFI" [S AM6] |
| Aeromomentum AM10 / AM12 | AM10 is a 1.0 L 3-cylinder [F AM15] | AM10 $9,995 (Kitplanes 2023) [F AM14] | 139 lb at the low end of the range [F AM14] | nf | nf | nf. **Not listed on the current Aeromomentum site** [S AM1] |
| **Viking 130** | Honda Fit 1.5 L DI I4 (73 x 89.5 mm, CR 11.5:1) [S VK1, VK3] | **$15,000.** Includes engine, 40 A alternator, throttle body, ECU, wire harness and starter, "a complete running engine" [S VK2, VK3]. Older prices: $11,995 (Kitplanes 2023 [F AM14]; Wikipedia); AUD-market reseller $16,500 to $17,490 USD landed in Melbourne [F VK22] | **220 lb** (no definition given) [S VK1]. Wikipedia: 178 lb dry and 224 lb installed with fluids [F] | 130 hp @ 5400. Takeoff 5400 engine / 2400 prop; cruise 4900 / 2100 [S VK1] | **2.33:1** [S VK1] | Viking-supplied, single. Maker not disclosed [S VK18 shows "our ECU vendor"] |
| Viking 90 | Mitsubishi Mirage 1.2 L 3-cyl [S VK4] | $11,550, same contents as the 130 [S VK2, VK4] | 159 lb [F VK10, AM14] | 90 hp @ 5800 [F VK10] | 2.33:1 (all Vikings) [S VK8] | Viking [S VK4] |
| Viking 140T | GM 1.2 L turbo 3-cyl, DI [S VK8, F AM15] | $17,000 [S VK2] ($16,500 in Kitplanes 2025 [F AM15]) | 215 lb [F VK10] | 150 hp @ 5800 [F VK10] (140 hp in the name) | 2.33:1 | Viking |
| Viking 150 | Honda 1.8 L SOHC (HR-V) [S VK5, VK8] | $16,100 [S VK2] | 239 lb [S VK5] | 150 hp @ 5800 [S VK5] | 2.33:1 [S VK5] | Viking |
| Viking 175 | Honda K-series 2.0 L, port-injected [S VK6] | $19,000 [S VK2] | 250 lb [S VK6] | 175 hp @ 6800 (prop 2900); takeoff 5800/2500 [S VK6] | 2.33:1 [S VK6] | Viking |
| Viking 195T | Honda Accord 1.5 L DI turbo I4 [S VK7] | $24,000 [S VK2] | 290 lb [F VK10] | 195 hp @ 5400 [F VK10] | 2.33:1 | Viking |
| SkyTrax (Yamaha snowmobile engines) | Yamaha Apex / Nytro / Sidewinder | **Gearbox only**: Apex box $4,999; Sidewinder/Nytro box $5,799 [S OT7]. No complete engine is listed for sale | nf | Apex stock about 150 hp [F OT9 snippet] | nf | stock Yamaha ECU or an aftermarket ECU, chosen by the builder [F] |
| Edge Performance EPeX (Yamaha 998 cc) | Yamaha Genesis/Apex 4-cyl | Historic prices: 150 hp €15,000 and 200 hp €20,500 [F snippet]; about 30 sold by 12/2022 [F OT8] | "no more than a Rotax 914" [F OT9] | 150 to 300 hp | nf | nf. **Not shown on the current Edge home page** [S OT10]. Status uncertain |

Pricing figures marked as "Kitplanes 2023/2025" are older than the vendor pages and are superseded by them.

---

### 2. Aeromomentum (Stuart, FL): AM13 and AM15 in detail

### 2.1 Price, mass, rating
- Prices and contents are in the table above [S AM2, AM3]. A $2,000 deposit is required, and delivery is about 8 weeks after the deposit [S AM4, AM5].
- Mass is "dry weight" and the vendor does not define what it includes. Kitplanes says the weight range for the product line is 139 to 285 lb "with PSRU, starter, alternator, ECU" [F AM14].
- Operating limits from the installation manual: 1800 to 5800 rpm normal operating, 6500 rpm redline. Cruise "should be 65% or less". Fuel flow at 65% cruise: about 4.2 gph (AM13) and 5.2 gph (AM15). Normal cruise timing is 34 to 36 degrees [S AM9].
- **Continuous rating: [nf].** The vendor publishes no separate takeoff and maximum-continuous figures. The only rated point is 5800 rpm.
- TBO: 2000 h for the AM13 and AM15; 1500 h for the AM13T and AM15T; 1800 h for the AM20T [S AM2, AM3, AM4, AM5, AM6].

### 2.2 Donor engine, injection, ignition
- "The AM family of engines are based on the well proven Suzuki G series automotive, light truck, marine and outboard base engines… aluminum block and head with single overhead cam and 16 valves. Fuel and ignition are controlled by an open source port fuel injection system." [S AM9]
- Kitplanes: "Suzuki is the source of the 1300 and 1500 engines… others are non-Suzuki and cannot be revealed" [F AM14]. The bore, stroke and displacement match G13BB (1298 cc) and G15A (1497 cc) [inf].
- Injection:
  - Port injection, one injector per cylinder [S AM9: "four extremely small, laser-drilled nozzle holes… if any of these (16) tiny orifices become blocked, that cylinder will run lean", which implies 4 injectors with 4 holes each].
  - The vendor product pages say "Semi Sequential Injection" [S AM2, AM3]. The intro page says "sequential fuel injection" [S AM7].
  - **Injector impedance: [nf].**
- Ignition:
  - The manual refers to "coil packs" [S AM9], and the intro page says "dual coil ignition" [S AM7]. I read that as 2 wasted-spark coil packs [inf].
  - 1 spark plug per cylinder [F AM17].
  - **Whether the igniter is inside the coil or driven by the ECU: [nf].**
- Knock sensor: listed in the intro page [S AM7]. The ECU senses RPM, CLT, MAP and IAT, and there is a **narrow-band O2** sensor [S AM9].
- Fuel system: return-type, with **two positive-displacement electric pumps in parallel**, a 5 µm final filter, and 43 psi relative to manifold pressure (about 30 psi at idle) [S AM9].
- Fuel: standard versions need 90 AKI or better; high-power versions need 93 AKI. Engine parts tolerate up to 10% ethanol. With 100LL, Alcor TCP treatment is recommended [S AM9].
- Throttle:
  - **Cable or drive-by-wire is not stated [nf].** The G-series is a cable-throttle engine and nothing in the manual mentions an electronic throttle, so cable is likely [inf].
- VVT:
  - G13BB/G15A are SOHC engines without VVT [inf].
  - SB 12/2/19 mentions a "**cam phase cover**" at the prop end of the head and asks owners to check it for oil leaks [S AM10]. It is most likely the cam-sensor cover [inf], but this is not confirmed.

### 2.3 ECU
- "The AM family of engines use the **MicroSquirt ECU**. The complete engine wiring harness is provided and is plug and play… Do not modify or extend the wires provided." [S AM9, 2022 manual V2]
- Conflict: the Aeromomentum intro page [S AM7] and Kitplanes [F AM14, AM15] say "**Bosch** FEDEC/engine management". These may refer to an older configuration or to Bosch sensors, injectors and coils. **This is unresolved** and is the first thing to verify on a delivered engine.
- **Single ECU. No dual or backup ECU is offered** [S AM9: the only redundancy described is that the engine runs on battery or alternator alone]. A forum thread on Aeromomentum redundancy discusses adding a second MicroSquirt, but no vendor product exists [F AM17].
- ECU data is available over **CAN** and RS232 serial. The Aeromomentum "AeroGraph" gauge reads the ECU over CAN [S AM9].
- Warranty: 2 years, or 1 year from first run, or 200 h, whichever comes first. It is void for "modifications" and "operation outside manufacturer's recommendations" [S AM11]. The manual also says "Please do not modify the supplied wiring harness" [S AM10]. **Removing the ECU will almost certainly void the warranty** [inf].

### 2.4 Trigger patterns (Suzuki G13BB / G15A)
- G13BB sensors: on a 2004 European Jimny, the **crank sensor is a VR 2-wire sensor and the cam sensor is a Hall 3-wire sensor**. Australian late-model G13BB engines reportedly have **a cam sensor only** [F OT12]. Configurations differ by market.
- Older distributor G13B: 12 teeth in the distributor with no sync feature. Haltech says this is "not directly supported" and requires removing teeth to leave a 4-tooth pattern; the distributor pickup is a reluctor (VR) [S OT5].
- G13BB: "3 teeth for every cylinder at 91°, 61° and 6° BTDC" (VR, distributor engines) [F OT13 (snippet)]. One snippet says the 2005+ Swift COP version uses 36-2-2-2 crank and 2-tooth cam [F (snippet), **unverified and probably a different engine (M-series)**].
- Aftermarket support by name:
  - rusEFI has `TT_SUZUKI_G13B` (a modified 4+1 style trigger, not the factory pattern [F]), plus `TT_SUZUKI_G16B` (marked "we assume this is NOT ready"), `TT_SUZUKI_36_2_2` and `TT_SUZUKI_K6A` [S OT1].
  - Speeduino has a Suzuki K6A decoder only, and nothing for the G-series [S OT3].
  - MegaSquirt MS2/Extra has "Suzuki Swift" and "Suzuki Vitara" spark modes [F (snippet), unverified].
- **Which trigger wheel Aeromomentum actually fits (factory or a custom 36-1 or 4+1 wheel) is not known [nf].** This decides whether an open ECU can use their sensors unchanged. Because the vendor uses a MicroSquirt, the pattern is already decoded by an open-source-lineage ECU, which is encouraging [inf].

### 2.5 Gearbox
- Kitplanes: "All AeroMomentum engines use a **helical, spur-gear** prop reduction gearbox. Custom 8620 alloy gears, designed in-house… The highest time gearbox so far logged **5500 hours in an airboat** with no issues." [F AM14]
- Vendor: "all gear design with the same TBO as our engines"; billet aluminium case; "**German made Guibo rubber dampening donut** that also is designed to last to TBO"; "designed for 4 cylinder engines up to **210 hp**" [S AM7].
  - The product pages say "rated to **225 hp**" [S AM2–AM5].
  - Both figures are below the AM20T's 260 to 300 hp, so the AM20T presumably uses a different box. That box is not documented [nf].
- Two-gear or three-gear versions are offered (the three-gear version changes the rotation direction or offset) [S AM2].
- Limits:
  - Maximum prop-flange moment of inertia 6000 kg·cm² (2050 lb·in²) [S AM9].
  - "With other propellers [than the tested Luga] do not operate where there is a torsional resonance or failure will result" [S AM9].
- Gearbox oil is GL-5 80W-90 [S AM9].
- Service bulletin 12/2/19 [S AM10]:
  - Gearbox main-bearing retainer screws (M6/M8): "We have had **3 instances** of these screws coming loose over time… on engines that had a noticeable vibration."
  - New engines ship with the screws safety-wired. Owners must torque-seal and inspect the screws before each flight, or fit drilled screws.
  - The same SB covers starter wiring gauge, a cam-phase cover oil leak, radiator support and coolant bleeding.
- Fleet size and hours: **not published** [nf]. The vendor's "planes with our engines" page lists 7 airframe types and no counts [S AM12].

### 2.6 Field record (Aeromomentum)
- **NTSB WPR20LA035**, 29 Nov 2019, Zenith CH701 N701WJ, Byron CA, AM13 S/N AM0314A at 115 h [S AM13]:
  - Partial power loss from overheating and detonation. Probable cause: the builder's improper cowling (no aft venting).
  - Not an engine, gearbox or ECU defect.
- AM15 forced landing, about March 2022 (Kevin Perreau): **the fuel-rail bracket cracked**. The vendor attributed it to items hung off the rail; other owners reported cracked brackets anyway, and the vendor committed to a stronger bracket [F AM16].
- RV-12 owners on VAF report quality and installation problems, and one AM15-HP RV-12 had off-field and precautionary landings before the owner switched engines [F (snippet), VAF pages blocked].
- AAIB/ATSB: nothing found [nf].
- No Aeromomentum gearbox failures were found in NTSB records or forums [nf]. Absence of evidence is weak here because the fleet size is unknown.

### 2.7 ECU replacement by owners
- **No public report found** of an owner replacing the Aeromomentum MicroSquirt with SDS, EFII or another ECU [nf]. The HBA thread on redundancy discusses ideas only [F AM17].

---

### 3. Viking Aircraft Engines (Edgewater, FL): Viking 130 in detail

### 3.1 Price, mass, rating
- $15,000 for "130 HP Engine, 40A alternator, throttle body, ECU, wire harness and starter. A complete running engine." [S VK3] The engine-options page says "engines at $9,995" (stale) [S VK9].
- Mass: 220 lb with no definition given [S VK1]. Kitplanes 2025 lists Viking weights "with PSRU, exhaust, alternator" [F AM15].
- Ratings:
  - 130 hp @ 5400. Takeoff 5400 engine rpm / 2400 prop rpm; cruise 4900 / 2100; idle 1400 to 1600 [S VK1].
  - **There is no separate maximum-continuous rating [nf].**
- CR 11.5:1. Fuel: "100LL (MUST use TCP/Decalin) 89+ Octane". Fuel pressure 43 psi [S VK1].
  - Up to 10% ethanol is permitted (Viking 110 handbook as quoted by NTSB) [S VK14].
- Spark plugs: NGK DILZKAR7C11S or Denso DXE22HCR11S [S VK1]. These are Honda L15B-family iridium plugs [inf], with 1 plug per cylinder [inf].
- **TBO: not published [nf].**
- Maintenance:
  - Oil every 50 h.
  - Gearbox oil (75W-90 or 75W-140) is changed every hour for the first 10 h, then at each oil change [S VK1].

### 3.2 Donor, injection, ignition
- Honda Fit 1.5 L direct-injected I4 [S VK1, VK3]. The engine code is probably L15B1 [inf: US Fit 2015–2020 DI].
- Viking states it uses Honda's "gasoline direct injection system and variable valve timing" [F VK23, aero-news 2016/2020].
  - **How Viking controls the VTC (actively, or locked) is not stated [nf].**
- Injection is **direct injection**. That means 1 high-pressure DI injector per cylinder (solenoid DI injectors need a roughly 65 V boost peak-and-hold driver) and a cam-driven high-pressure pump with a spill-valve solenoid [inf, general DI practice].
  - **This is the biggest single obstacle for an open two-lane ECU** [inf].
  - Haltech states that the Honda L15 DI variants "are all equipped with Direct Injection and are **not supported by Haltech**" [S OT4]. Only MoTeC M1 (M122/M142 L15 package) and Link G4+/G4X Force are mentioned as running the L15B [F OT6 (snippet)].
- Ignition type: [nf]. The Honda L-series uses coil-on-plug with an igniter integrated in the coil [inf]. Viking: "One ignition coil per cylinder with optional dual ECU" [F VK10].
- Throttle: Viking ships a "throttle body" [S VK3]. **Whether it is the Honda DBW body or a cable body is [nf].**

### 3.3 ECU
- Viking 110 (2009–about 2016):
  - A "custom designed dual ECU (engine computer)" designed by **Mark Hubelbank**, with PC-adjustable software [F VK21 (snippet)].
  - AvWeb 2014: "dual FADEC controls" [F VK12].
- Viking later issued **SB "Viking 110 Wiring Upgrade": "Remove ECU select switch to operate on a single computer only… Disregard and tape the ECU 2 wire. Solder ECU 1 and SELECT together"** [S VK13, quoted by the NTSB]. In other words, Viking **withdrew the dual-ECU failover on the 110 and went to a single ECU.**
- Current engines (130 and others):
  - A single ECU from an undisclosed "ECU vendor". The calibration is a "32 x 32" MAP × rpm fuel map set on a brake dyno [F VK18, Viking post 2018].
  - After an owner retuned his ECU, Viking **password-protected the software** [F VK18].
  - Updates are done by "trading ECUs with Jan. No charge" (2014) [F VK20]. Owners still send ECUs in for updates in 2025 [F VK19].
- Dual ECU:
  - "optional dual ECU" according to a third-party summary [F VK10].
  - **Not offered on Viking's current store pages** [S VK2]. The store sells a "Gen 2 Viking View" EIS ($1,400; $1,550 turbo) and a data logger ($450), not a backup ECU.
- Kitplanes 2025 describes "Electronic ignition and fuel injection and no traditional mixture knob" and does not name the ECU maker [F AM15].
- **Who makes the current Viking 130 ECU, and whether it is a reflashed OEM Honda ECU or a custom unit, is [nf].** DI makes a custom low-cost unit less likely; a reflashed OEM Honda ECU is plausible but unproven [inf].

### 3.4 Trigger patterns (Honda L15)
- Haltech's "L engine" article (L12/L13/L15) says the crank wheel is **60-2, Hall effect**, and the **cam has 3 teeth (2 large + 1 small), Hall effect** [S OT4].
  - Caveat: Haltech does not support the DI L15B, so that article may describe port-injected L15A engines. **The L15B trigger is not confirmed [nf].**
- Older Honda K/D-series patterns are 12+1 crank and 4+1 cam (rusEFI `TT_HONDA_K_CRANK_12_1`, `TT_HONDA_K_CAM_4_1`) [S OT1]. The Viking 175 (K20) would use these [inf].
- rusEFI has no named L15B trigger. Speeduino has Honda D17 and J32 decoders only [S OT1, OT3]. A generic 60-2 missing-tooth decoder is supported by all open ECUs [inf].

### 3.5 Trigger pattern (Mitsubishi 3A92, Viking 90)
- rusEFI source: `TT_36_2_1_1` is commented "Mitsubishi 3 cyl and 6 cyl", and there is a separate `TT_VVT_MITSUBISHI_3A92` cam decoder [S OT1, OT2]. 3A92 has MIVEC VVT [F].
- Speeduino has a 36-2-1 (4B11) decoder but no 36-2-1-1 [S OT3].
- The Viking 90 injection type (port or DI) is not stated [nf]. The 3A92 is a port-injection engine [inf].

### 3.6 Gearbox
- Viking's own design, 2.33:1, "3 gear gearbox for Lycoming style propeller rotation" [S VK8]. Wikipedia describes the 110's box as "helical gear reduction" [F VK11].
  - In 2014 the ratios were 2.32, 2.42 and 2.53 [F VK12].
  - Kitplanes 2025 summary wording on a clutch was not confirmed in its verbatim text [nf].
- Torsional coupling:
  - A rubber "spider/plate" (three-lobe) coupling. Viking issued a service bulletin replacing an earlier bolted "push-fit" part so the rubber damper can float [F VK16, Jan Eggenfellner's reply].
  - The Australian reseller lists a "torsion damper" and an "upgraded gearbox… stronger bearings… 2 kg lighter" for the current 130 [F VK22].
  - A proposed rework (VAF) adds a CrMo flywheel and a **Centaflex** coupling with 3 × M12 bolts [F VK17 (snippet)].
- Field record (forum):
  - "In the last 6 months there have been **2 in-flight fatigue failures of the gearbox input drive flange ears**… one failed at **130 hours** total, the second at approximately **800 hours**… both during take-off, one causing total loss of the airplane." Viking said only engines not complying with the flywheel/drive-flange bulletin were at risk; the poster says the 130 h failure was compliant [F VK17 (snippet), VAF "Viking 110 notice", about 2022, page blocked].
  - Zenith 701 / Viking 110 (Hubelbank), 29 Oct 2022: the gearbox rubber coupling lost one of its three lobes and holed the cowling and radiator. Viking blamed non-compliance with an SB issued about 8 years earlier [F VK16].
  - A positive data point: "disassembled one after around 500 hours of intensive demo and cross country flights, it still looked like new" (2017) [F VK24].
- Gearbox TBO and inspection interval: [nf].
- Fleet: "By August 2016 the company had delivered 100 engines and had 25 reported flying" (Viking 110) [F VK11]. There are no current figures [nf].

### 3.7 Accidents and incidents (Viking)
- **NTSB ERA23FA023**, 17 Oct 2022, Aventura II N32856, Miramar FL, **2 fatal**, Viking 110 (dual-ECU installation) [S VK13]:
  - There had been an earlier in-flight shutdown and restart (11 Oct 2022) with the throttle stationary.
  - In the post-accident run the engine lost power after several minutes. The cause was the **ECU select switch / dual-ECU wiring** not modified per the Viking SB. After isolating the ECUs, the engine ran normally.
  - Probable cause: the pilot's failure to remove the ECU select switch per the SB.
  - **This is directly relevant to two-lane failover design.**
- **NTSB ERA23FA188**, 11 Apr 2023, RV-12 N543GM, Climax NC, 1 fatal and 1 serious, Viking 110 at about 20 h [S VK14]:
  - Partial power loss at 400 ft AGL. Spark plug electrodes on cylinders 1 and 2 were "obliterated", likely from detonation on 87 AKI fuel early in the engine's life plus old auto fuel.
  - The NTSB also cites the pilots' decision-making.
- Zenith CH750 Cruzer N956GM, Louviers CO, Viking 130 (GA News, 28 Nov 2019, NTSB summary) [F VK15 (snippet; page 403)]:
  - The engine **seized after a replacement ECU with updated programming was installed**. The ECU ran the mixture too lean, which caused excessive head temperature and lifted the head gasket.
  - The NTSB number was not found [nf].
- Owners report a Viking 130 cold- or warm-start difficulty and occasional backfire that was not fixed by an ECU update (2024–2025) [F VK19]. Earlier, cold-start issues were fixed by ECU swaps (2014) [F VK20].
- AAIB/ATSB: nothing found [nf].

### 3.8 ECU replacement by owners (Viking)
- **Viking 110 → HU708**: Mark Hubelbank (the original 110 ECU designer, per VK21 snippet) built a new ECU, the "HU708". It has reportedly flown about 5 years, with **full hardware schematics and software source available**, and there is a groups.io support group "HondaFit708huECU" [F VK21 (snippet); groups.io page paywalled/402].
  - That owner's engine later had the 2022 gearbox coupling failure [F VK16]. Viking attributed it to coupling SB non-compliance, not to the ECU.
- **SDS** is mentioned as a supportable alternative for the Viking 110. Ross Farnham at SDS "has done Honda FIT configurations" [F (snippet), VAF]. No completed flight report was found [nf].
- Viking 130 owner retune: an owner bought tuning equipment and changed fuel and ignition parameters. Viking objected and password-locked the ECU [F VK18]. The outcome for the engine was not reported.
- **No report found of anyone running a third-party ECU on the DI Viking 130** [nf].

---

### 4. Other candidates (sold with gearbox)

- **Auto PSRU (LS3 + PSRU)**: $72,500 for 375 hp complete FWF, with centrifugal clutch [F AM15]. They also sell Subaru FWF kits with the 250Z PSRU [F]. These are too large for a mule of this class and are listed only for completeness.
- **LS aeroengines**: LS3 with a helical PSRU and SDS engine management [F AM15]. Also out of class.
- **SkyTrax / Aero Endeavors (Yamaha)**: gearboxes only ($4,999 Apex; $5,799 Sidewinder/Nytro). The builder supplies the engine and ECU [S OT7]. Not a "complete engine" product.
- **Edge Performance EPeX (Yamaha Genesis 998 cc)**: about 30 built by 12/2022 [F OT8]. Not visible on the current Edge site [S OT10]. Availability is unconfirmed.
- No currently-produced Subaru-, Suzuki- (other than Aeromomentum), Honda- (other than Viking) or Mitsubishi-based complete geared engine from another vendor was found [nf].
  - Eggenfellner's earlier Subaru/Honda company is defunct [F].
  - Edge's other products are Rotax-based and are excluded.

---

### 5. Key uncertainties
1. Aeromomentum ECU identity. The 2022 manual says **MicroSquirt**; the intro page and Kitplanes say **Bosch**. It is also unknown which trigger wheel and sensors are fitted (VR crank or Hall cam), and the injector impedance.
2. The ECU maker for the Viking 130 is unknown, as is whether it is a reflashed OEM unit. DI injector drive and HP-pump control would need a DI-capable driver stage in our ECU. Haltech explicitly does not support the L15 DI engines.
3. The L15B (DI) crank and cam patterns are unconfirmed. The Haltech 60-2 / 3-tooth cam data may be for the L15A.
4. Neither vendor publishes a maximum-continuous power, engine TBO (Viking), gearbox TBO, or fleet hours.
5. Viking gearbox and coupling history comes from forums only (VAF pages were blocked; I used snippets). There is no vendor SB index online.
6. Electronic versus cable throttle on both vendors is not stated.

---

### 6. Sources (all retrieved 2026-10-21)

**Aeromomentum**
- AM1 https://aeromomentum.com/
- AM2 https://aeromomentum.com/am13-100hp-to-126hp/ (also https://aeromomentum.com/?p=161)
- AM3 https://aeromomentum.com/am15-117hp-to-147hp/
- AM4 https://aeromomentum.com/am20-170hp/ (AM13T page; also ?p=236)
- AM5 https://aeromomentum.com/am15t-160hp/
- AM6 https://aeromomentum.com/am20t-230hp-300hp/
- AM7 https://aeromomentum.com/intro/
- AM8 https://aeromomentum.com/manual/ (?p=101), the manual and download index
- AM9 https://aeromomentum.com/wp-content/uploads/2022/07/AM13-and-AM15-Engine-Installation-Manual-V2.pdf (installation manual, 41 pp)
- AM10 https://aeromomentum.com/wp-content/uploads/2022/07/Installation-and-Service-Bulletins-2DEC19-3.pdf
- AM11 https://aeromomentum.com/warranty/ (also https://aeromomentum.com/wp-content/uploads/2022/07/AM-engine-warranty.pdf)
- AM12 https://aeromomentum.com/engines/
- AM13 NTSB WPR20LA035: https://data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/100634/pdf
- AM14 Kitplanes 2023 buyer's guide: https://www.kitplanes.com/inline-and-v-four-stroke-engine-buyers-guide-2023/
- AM15 Kitplanes 2025 buyer's guide: https://www.kitplanes.com/2025-engine-buyers-guide/
- AM16 Zenith forum, AM-15 engine failure: https://zenith.aero/forum/topics/engine-failure
- AM17 HBA forum, Aeromomentum redundancy: https://www.homebuiltairplanes.com/forums/goto/post?id=428952
- AM18 VAF AeroSalesEAB 147 hp thread (snippet only, 403): https://vansairforce.net/threads/aerosaleseab-147hp.189089/

**Viking**
- VK1 https://www.vikingaircraftengines.com/viking-130-engine
- VK2 https://www.vikingaircraftengines.com/new-products (store; prices)
- VK3 https://www.vikingaircraftengines.com/new-products/viking-130-hp-engines
- VK4 https://www.vikingaircraftengines.com/new-products/viking90engine
- VK5 https://www.vikingaircraftengines.com/viking-150-engine
- VK6 https://www.vikingaircraftengines.com/viking-175-engine
- VK7 https://www.vikingaircraftengines.com/new-products/viking-195-hp-turbocharged-engines
- VK8 https://www.vikingaircraftengines.com/engine-options
- VK9 https://www.vikingaircraftengines.com/what-we-do
- VK10 https://www.experimentalaircraft.info/homebuilt-aircraft/viking-aircraft-engines.php (third party)
- VK11 https://en.wikipedia.org/wiki/Viking_110
- VK12 https://avweb.com/press-releases/viking-aircraft-news-at-oshkosh/ (2014)
- VK13 NTSB ERA23FA023: https://data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/106139/pdf
- VK14 NTSB ERA23FA188: https://data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/107039/pdf
- VK15 GA News, N956GM Zenith CH750 Cruzer: https://www.generalaviationnews.com/2019/11/28/equipment-failure-n956gm-motley-gary-w-zenith-ch750-cruzer (403; snippet)
- VK16 Zenith forum, Viking gearbox emergency landing (2022): https://zenith.aero/forum/topics/emergency-landing
- VK17 VAF "Viking 110 notice" (403; snippet): https://vansairforce.net/threads/viking-110-notice.211562/
- VK18 Zenith forum, Viking "ECU Programming Shouldn't Be Changed" (2018): https://zenith.aero/forum/topics/those-who-can-and-those-who-can-t
- VK19 Zenith forum, Viking 130 cold weather starting (2024–25): https://zenith.aero/xn/detail/2606393:Comment:945380 (also :939964)
- VK20 Zenith forum, Honda Viking for STOL 750 (2014): https://zenith.aero/xn/detail/2606393:Comment:358451
- VK21 VAF "Viking 110 ECU" (HU708; 403; snippet): https://vansairforce.net/community/threads/viking-110-ecu.225052/post-1752852
- VK22 Swish Projects (AU reseller): https://swishprojects.com.au/shop/engines/viking-aircraft-engine/viking-130-hp-engine/
- VK23 Aero-News: https://www.aero-news.net/index.cfm?do=main.textpost&id=f4110750-7e12-4915-907c-e23a723a7dd8
- VK24 Pilots of America thread p.2: https://www.pilotsofamerica.com/community/threads/viking-aircraft-engines-thoughts-honda-piston-ae.103592/page-2
- VK25 Zenith forum, Viking 130 on 601XL (2022): https://zenith.aero/xn/detail/2606393:Comment:884460

**Other / ECU-support**
- OT1 rusEFI trigger enum: https://github.com/rusefi/rusefi/blob/master/firmware/controllers/algo/engine_types.h
- OT2 rusEFI Mitsubishi decoders: https://github.com/rusefi/rusefi/blob/master/firmware/controllers/trigger/decoders/trigger_mitsubishi.cpp
- OT3 Speeduino decoders: https://github.com/noisymime/speeduino/blob/master/speeduino/decoders.h
- OT4 Haltech, Honda L engine: https://support.haltech.com/portal/en/kb/articles/l-engine
- OT5 Haltech, Suzuki G13B: https://support.haltech.com/portal/en/kb/articles/g13b-engine
- OT6 HP Academy, L15B1 DI standalone (snippet): https://www.hpacademy.com/forum/road-tuning/show/standalone-install-on-honda-l15b1-enginedirect-injection
- OT7 SkyTrax store (Aero Endeavors): https://aeroendeavor.com/badlands-traveler-experimental-aircraft-stol-builder-assist/SKYTRAX-USA-c184908312
- OT8 Kitplanes "On the Edge" (Dec 2022): https://www.kitplanes.com/on-the-edge/
- OT9 Zenith forum, EPeX150i: https://zenith.aero/forum/topics/epex150i
- OT10 Edge Performance: https://www.edgeperformance.no/
- OT11 Auto PSRU: https://autopsrus.com/
- OT12 BigJimny forum, G13BB wiring (2021): https://bigjimny.com/index.php/forum/7-jimny-technical/67516-g13bb-wiring
- OT13 rusEFI forum, G13B/G13BB trigger (500 on fetch; snippet): https://www.rusefi.com/forum/viewtopic.php?p=51211

---

# Part B. Airframes and FAA rules

Research date: 2026-10-21 (all sources retrieved 2026-10-21). US program. Public web only.

Tags: **[S]** official or vendor source; **[F]** forum, listing, magazine or other secondary source; **[nf]** not found.

Engine context: Aeromomentum AM15, 120 hp at 5,800 rpm, 185 lb (84 kg) dry, 2.588:1 gearbox, "FADEC System Standard" [S AF1]. Viking 130, 220 lb (100 kg), 2.33:1 gearbox [S AF6]. Both ship with the maker's own ECU. Fitting the program's controller in place of that ECU would almost certainly be a "major change" under the § 21.93 definition ("appreciable effect on ... reliability, operational characteristics") [S FAA5]. That is my reading of the rule; the FAA has not confirmed it.

---

### 1. FAA rules that set the flight-test burden

### 1.1 Phase I hours for a new E-AB with a non-type-certificated engine
- **FAA Order 8130.2L** (dated 01/30/2026) is the current revision. It replaced 8130.2K (08/28/2024) [S FAA1, FAA2]. Para 15-4f(1), "Duration of Assignment to Flight Test Area (hourly-based)", says Phase I operating limitations should limit operations to the test area for at least:
  - "(a) Forty hours when a non-type-certificated engine, propeller, or engine/propeller combination is installed."
  - "(b) Forty hours if an installed type-certificated engine, propeller, or engine/propeller combination has been altered in a way that differs from an approved type design on a TCDS."
  - "(c) Twenty-five hours when an unaltered, type-certificated engine/propeller combination is installed."
  - "(e) Five hours after any major change."
  - 15-4f(2): "Phase I flight testing may be conducted in accordance with the task-based flight test program described in FAA AC 90-89, within an assigned flight test area." [S FAA1]
- **AC 90-89C** (2/14/23) is the current revision. It is titled "Amateur-Built Aircraft and Ultralight Flight Testing Handbook". The "...and Light-Sport..." title belonged to earlier revisions. Para 2.1.5: "Your original issued experimental certificate should be limited to operation within an assigned flight test area for a minimum of 25 hours when a type certificated (TC) engine/propeller combination is installed. A minimum of 40 hours is required when a non-TC'd engine, propeller, or engine/propeller combination is installed." [S FAA3]
- **Task-based alternative** (AC 90-89C 2.1.6.1): the AC lets builders use "a comprehensive, individualized task-based flight test plan to meet the objectives of the flight test, but according to certain completion criteria and possibly less than the typical 25 or 40 hours". Para 2.1.8 "Process": "Builders may utilize a task-based flight test plan without approval or submission to the [FSDO] or [MIDO]." The operating limitations must reference AC 90-89 to allow it. Para 2.1.9: if the criteria are not met, "test for the full 25 or 40 hours". [S FAA3]
- AC 90-89C also encourages the Additional Pilot Program, AC 90-116 (a second pilot in Phase I) [S FAA3, FAA4].
- AM15 and Viking are not type-certificated, so a new E-AB build needs **40 h, or the task-based plan** [S FAA1, FAA3].

### 1.2 Major change (engine or engine-controller swap) on an already-certificated E-AB
- **Order 8130.2L, Appendix D, operating limitation No. 22**, for § 21.191(d), (e), (g) [amateur-built], (h), (i), (k), (l): "After incorporating a major change per § 21.93 that was not presented to the FAA when this airworthiness certificate was issued, the following applies: **Notification of Major Changes.** The responsible Flight Standards Office where the aircraft is based must be notified and its response received in writing before flying this aircraft. ... **Operations.** Comply with § 91.319(b) using Phase I operating limitations. **Registry.** If the major change includes installing a different model of engine or a change of a fixed pitch from or to a controllable propeller, the aircraft owner must submit a revised FAA Form 8130-6 to update the aircraft's file in the FAA Aircraft Registration Branch, AFB-710." [S FAA1]
- The version of limitation 22 for § 21.191(a)&(b) has the same notification wording. It adds that "prior to showing compliance with § 91.319(b) after a major change, all operations must be conducted under day [VFR] conditions and over an area described by § 91.305", and gives the logbook statement wording [S FAA1].
- Limitation 22 for § 21.191(c)&(f): "the operator must obtain an R&D certificate to operate this aircraft." [S FAA1]
- **AC 90-89C 2.1.12**: "Usually the owner of the E-AB aircraft is required by the aircraft operating limitations to notify the responsible FSDO following a 'major change' as defined by § 21.93 ... the corresponding flight testing for a major change will require at least 5 hours minimum of supplemental Phase I flight testing be completed to comply with § 91.319(b). The aircraft owner then obtains concurrence from the FSDO as to the suitability of the proposed test area." Para 2.1.12.4: for a different engine type, "complete a revised FAA Form 8130-6 ... The aircraft remains in flight test for a minimum of 5 hours as specified in the operating limitations." [S FAA3]
- KITPLANES "Ask the DAR": "The FSDO may require additional time (more than 5 hours) depending on the extent of the modification." [F AF30]
- Bottom line: an engine swap, or a swap of the controller on an existing engine, on a flying E-AB means a written FSDO response before flight, then **at least 5 h** of return to Phase I. The FSDO can require more. The aircraft does not go back to 40 h by default [S FAA1, FAA3].
- § 21.93(a), definition of a major change: "A 'minor change' is one that has no appreciable effect on the weight, balance, structural strength, reliability, operational characteristics, or other characteristics affecting the airworthiness of the product. All other changes are 'major changes'." [S FAA5]
- § 91.319(b): no operation outside the assigned area until the aircraft is shown "controllable throughout its normal range of speeds and throughout all the maneuvers to be executed" and has "no hazardous operating characteristics or design features." § 91.319(a)(1): no operation "for other than the purpose for which the certificate was issued". § 91.319(d)(2): day VFR unless otherwise authorized. [S FAA6]

### 1.3 Can an E-AB be the test bed for an organization's engine program?
- § 21.191(g): "Operating an aircraft the major portion of which has been fabricated and assembled by persons who undertook the construction project solely for their own education or recreation." The 51% test decides whether an aircraft is eligible for certification. It is a test of who built it, not of who uses it [S FAA7].
- An organization can own an E-AB, but the builder has to be a person. DAR Mel Asberry (KITPLANES, 2015): "I've had several using an LLC, and that is not a problem". A corporation can be listed as owner, but "the builder must be an individual." [F AF31]
- § 91.319(f) restricts leasing only for § 21.191(i), (k) and (l) aircraft (the LSA-derived categories). The rule does not restrict leasing an E-AB under (g) [S FAA6]. § 91.319(a)(2) bars carrying persons or property for compensation in operations that need Part 119/121/125/129/133/137 authority [S FAA6].
- **FAA guidance on whether an organization's engine-development flights fit the E-AB "operating amateur-built aircraft" purpose of § 91.319(a)(1): [nf].** The purpose that clearly fits is § 21.191(a) R&D: "Testing new aircraft design concepts, new aircraft equipment, new aircraft installations, new aircraft operating techniques, or new uses for aircraft." [S FAA7] Order 8130.2L 4-6a(1)(a): "Using the same aircraft for overlapping programs is acceptable, and the program letter can outline one or more programs." [S FAA1] Whether one airframe can hold (g) and (a) at the same time, or has to be recertificated to R&D, is a FSDO question: **[nf] explicit FAA statement.**
- **R&D certificate requirements, § 21.193.** The applicant submits "(a) The experimental purpose ... (b) Enough information to describe the operation, equipment, or test ... (c) The estimated time or number of flights required ... (d) The areas over which flights will be conducted. (e) Enough data to identify the aircraft. (f) Except for a previously type certificated aircraft without an appreciable change in its external configuration, three-view drawings or three-view dimensional photographs". [S FAA8] Order 8130.2L 4-6a(1) says the ASI checks that the program letter covers purpose, time, area and drawings, with sample letters in Appendix C [S FAA1].
- An R&D certificate lasts **3 years** from issue or renewal (§ 21.181(a)(4)). Exhibition and amateur-built certificates are unlimited (§ 21.181(a)(5)) [S FAA9].
- Non-profit-specific R&D provisions: **[nf]**. The rules do not distinguish non-profit applicants.

### 1.4 Insurance for Phase I with an auto-conversion engine
- KITPLANES "Homebuilder's Insurance" (2026-03-20): some underwriters give "liability-only coverage until Phase I testing is complete, suspending hull coverage entirely". Others impose "substantially elevated deductibles—commonly 10% of agreed hull value during motion operations." On auto conversions: "underwriters view them as introducing additional mechanical uncertainty and parts availability concerns, leading to higher premiums or coverage restrictions." It gives an illustrative CH750 STOL with $75,000 hull at about $1,650 per year, and says hull costs run about 1.0–1.5% of agreed value. These are not Phase I or auto-conversion specific. [F AF27]
- BWI Aviation Insurance lists "Engine type (certified vs. auto conversion)" as a premium factor and publishes no figures [S AF28].
- Zenith forum (Carl Orton, 2018-05-27): "I could only obtain liability during my 40 hr phase 1 tests unless I obtained 5 hrs of dual in a Sonex" [F AF29].
- **Published premium for Phase I flight test of an E-AB with an AM15 or Viking engine: [nf].**

---

### 2. Options

### A. Buy a flying E-AB that already has an AM13/AM15 or Viking 110/130
**Where the engines go (vendor sources)**
- Viking: "With over 900 Viking engines in Zenith aircraft" [S AF7]. Firewall-forward kits for Zenith 750 STOL/Cruzer/Super Duty, 650, 701; Rans (incl. S21); Van's RV-12 to RV-7/9; Kitfox 3–7; Sonex; SeaRey; Just (Escapade, Highlander, SuperSTOL); Bathawk; Aventura. Viking also lists Murphy Rebel, Savannah, SP30, Hawk, Cozy MK4, Jabiru and others [S AF8].
- Aeromomentum: firewall-forward "assistance packages" for Zenith CH650/750, CH601/701, RV-12 (through dealer AeroSales LLC), Belite Chipper, Sonex Legacy, Sonex Onex, Kitfox 7, Aventura, SeaRey, Highlander, Fokker D7, powered parachutes [S AF2]. Aeromomentum publishes no customer gallery or installation count: **[nf]**.
- Zenith lists Viking (Zodiac, STOL CH 701/750) and Aeromomentum AM13/AM15 as third-party firewall-forward packages [S AF12].

**Current listings (October 2026)**
| Aircraft | Engine | Price | Notes | Source |
|---|---|---|---|---|
| 2019 Zenith 750 STOL | Viking 130 | $69,000 "reduced for quick sale" | 101 h since new, Whirlwind prop, MGL EFIS, posted 2026-09-22, Anderson SC | [F AF14] |
| 2019 Zenith CH 750 Cruzer | Viking 130 | $135,000 | Duc variable-pitch prop, IFR-capable panel; FLYING article 2026-08-06 citing AircraftForSale | [F AF15] |
| Zenith CH650B | Viking 130 HP, 0 h | price not captured | AeroTrader, updated 01/14/2026, Camden SC (search snippet only) | [F AF16] |
| Cherry BX2 (retractable) | "Honda Viking" | $35,000 | 280 h; one-off design, poor fit as a test bed | [F AF17] |
| Zenith 701 kit, about 60% complete | Viking 130 (0 h) | $25,000 | project, not flying | [F AF18] |
| Any flying aircraft with an Aeromomentum AM13/AM15 | — | **[nf]** | Barnstormers had only a loose AM15 147 hp engine at $10,000 (posted 2026-04-10) | [F AF19] |

- Flying Viking-powered price range found: **$69k–$135k** (2 data points) [F]. Flying Aeromomentum-powered: **[nf]**.
- Trade-A-Plane and Controller could not be read (JS block or HTTP 403), so this survey of those sites is incomplete.
- Time to first flight: buy, prebuy and condition inspection, fit the program ECU, notify the FSDO and wait for its written response, then fly at least 5 h of supplemental Phase I [S FAA1]. Calendar duration: **[nf]**.

### B. Buy a used Rotax-912 E-AB and re-engine it
**Used prices for Rotax 912 E-ABs on Barnstormers (Oct 2026) [F AF20]**
| Aircraft | Price | Notes |
|---|---|---|
| Rans S6S Coyote, 912ULS, 220 TT | $56,500 | posted 2026-10-04 |
| 2007 Rans S6S Coyote II, 912ULS | $40,000 | SOLD |
| 2015 Rans S-7 Courier, 912ULS, 90 TT | $88,500 | posted 2026-09-25 |
| Kitfox IV-1200, 912ULS 37 h SNEW | $49,000 | posted 2026-10-15 |
| 2015 Just SuperSTOL 912ULS | $99,000 | SOLD, prior non-moving damage |
| Zenith 750 STOL new (Oct 2025 AW cert) | $80,000 | engine not stated in snippet |
| Zenith 750 STOL quick-build kit + 912ULS (unflown) | $40,000 | kit, not flying |
Range found for flying Rotax 912 E-ABs: **about $40k–$99k** [F].

**Re-engine hardware (vendor list prices)**
- AM15 engine: $13,000 (bed mount, 2 gears), $13,600 (aft mount, 2 gears), $13,500 (bed mount, 3 gears), $14,100 (aft mount, 3 gears) [S AF1]. AM13: $11,500 (bed mount, 2 gears) [S AF3].
- Aeromomentum Zenith 650/750 package parts: Cowling System $2,530; Propeller System $2,130; Mounting System (mount, bushings, engine-to-mount hardware, "not mount to air frame") $1,237. Exhaust, cooling and fuel systems are priced separately [S AF4].
- Aeromomentum Zenith 601/701: cowling $2,530, prop $2,070, mount $1,137 [S AF4]. Kitfox 7 mounting system $1,642 [S AF4]. RV-12: cowling $2,230, prop $2,130, mount $1,237 [S AF4]. Sonex Legacy mounting system $242; the page lists the engine mount at quantity 0, so it is probably bushings and hardware only [S AF4]. Highlander engine mount system $1,600 [S AF4]. Universal nose bowl $790 [S AF2].
- Viking store: Viking 130 engine $15,000; engine mount $1,500; cowling $1,500; Duc 3-blade prop $3,520; installation service $4,800 at Viking or $6,200 at your location [S AF5].
- Zenith factory firewall-forward packages cover Rotax, UL Power, Continental and Lycoming only. Prices are "contact for quote" [S AF12].
- Offset from selling the removed Rotax: one used 912iS with 418 h was listed at $23,500 OBO (sold) [F AF21]. **[nf]** for a 912ULS market range.
- Weight: Aeromomentum's own comparison table gives Rotax 912 165 lb, AM13 170 lb, Viking 110/130 225 lb [S AF3]. AM15 is 185 lb [S AF1] and Viking 130 is 220 lb [S AF6]. Expect a weight-and-balance rework.
- Caveats from builders: an off-plans engine installation means fabricating the mount, exhaust, cooling and cowl, and can take longer than the airframe [F AF22]. A CH650 beta customer called the fitment of the Aeromomentum firewall-forward parts poor and went back to a Rotax 912ULS by 2021 [F AF23].
- Regulation: a re-engine is a major change. It needs a written FSDO response, at least 5 h of Phase I and a revised Form 8130-6 [S FAA1, FAA3].
- Swap labor hours or calendar time: **[nf]**.

### C. Build a kit from scratch
| Kit | Price (vendor) | Build time (vendor or magazine) | Source |
|---|---|---|---|
| Zenith STOL CH 750 | Airframe $28,250 + finishing (firewall-back) $10,475 = $38,725 | "less than 400 hours" (Zenith release, 2010) | [S AF9], [F AF10] |
| Zenith CH 750 Cruzer | $26,995 + $9,950 = $36,945 | about 400 h [nf from Zenith itself] | [S AF9] |
| Zenith CH 750 Super Duty / Super Cruzer | $33,790 + $12,990 (Super Cruzer intro price, July 2026) | SD "250-300 hours"; Super Cruzer "under 400 hours"; Super Cruzer approved engines 140–230 hp | [S AF9], [S AF11], [F AF24] |
| Kitfox Series 7 STi (firewall-back) | $49,995 (Rev F, 06/25) | "average build times are 1000 hours or an average of 18 months" | [S AF25] |
| Sonex-B / Waiex-B / Onex / Xenos-B / Highwing (complete airframe) | $35,700 / $36,700 / $25,450 / $42,500 / $39,000 (effective 2025-12-15); QB upgrade Sonex-B $16,000 | Sonex-B about 1,000 h; QB about 500 h (AOPA 2019) | [S AF26], [F AF32] |
| Van's RV-12iS (airframe subkits) | $825 + $5,600 + $14,100 + $12,300 + $18,800 = $51,625 (order form dated 2-5-24); powerplant kit with 912iS $33,870 [F] | "about 700-900 hours" | [S AF33], [S AF34], [F AF35] |

- Zenith price sheet file is dated 2-24 ("CH 750 SD CRZ 2-24-master"). Prices are F.O.B. factory and "subject to change" [S AF9].
- RV-12: Van's says the kit is E-LSA-oriented and that you can "mount the 912 iS Sport or the 912 ULS". Van's "do[es] not believe it is in the best interests of an RV-12 builder to delete, substitute or modify any component" and "no longer supplies the ULS engine option". The FAA found the kit E-AB eligible, and Aeromomentum sells an RV-12 package. So the RV-12 is Rotax-only as Van's supplies it, but not under E-AB rules [S AF33, AF34, AF4].
- Also note: § 21.191(i)(2) says "An experimental airworthiness certificate will not be issued under this paragraph (i)(2) for these aircraft after October 22, 2025". New E-LSA kit certificates are closed, so a new RV-12 kit would go E-AB (or § 21.191(k)) [S FAA7].
- Kit plus engine example from sourced figures only: CH 750 STOL firewall-back $38,725 + AM15 $13,000 + Aeromomentum cowl/prop/mount $5,897 = **about $57.6k**. Excludes exhaust, cooling, fuel, instruments, avionics, paint, shipping and crating. Avionics and finishing cost: **[nf]**.
- Time to first flight: build hours above, plus the 40 h or task-based Phase I [S FAA1, FAA3].

### D. Partner with an owner already flying an AM15 or Viking aircraft
- Viking has its own fleet: "We have built over 6 Zenith aircraft, fly them all over the country ... we did the Zenith Aircraft Superduty prototype!" [S AF7]. Jan Eggenfellner flew a Viking 110 Zenith CH 750 (STOL competition winner, 2014) [F AF13].
- Aeromomentum company demonstrator aircraft: **[nf]**.
- Published host or test-bed agreements between an engine or ECU developer and a private E-AB owner: **[nf]**.
- Rules: the owner's E-AB takes the major-change path (written FSDO response, at least 5 h Phase I) [S FAA1]. § 91.319(f) does not bar leasing a (g) aircraft [S FAA6]. Whether the program's use fits the E-AB purpose under § 91.319(a)(1): **[nf]** (see 1.3).
- Insurance stays with the owner's policy. Underwriter acceptance: **[nf]**.

### E. Ground-only (prop test stand, dyno, airboat-style stand)
- Commercial ~100 hp aircraft propeller test stand or test cell price: **[nf]**.
- Dyno: YourDyno water-brake instrumentation and control kit "From: $4,790.00 ex VAT/import tariffs". It works with existing DynoMITE, Stuska and other absorbers and does not include the absorber [S AF36]. The Land & Sea DYNOmite absorber kit has no published price: **[nf]** [S AF37].
- Aeromomentum has sold its engines to airboat customers for over 10 years (builder statement) [F AF22]. Airboat-hull test bed cost: **[nf]**.
- No FAA certificate is needed for ground running. This option does not produce flight data.

### F. The owner's own aircraft (if type-certificated)
- An uncertified engine plus a non-TC controller on a standard-category aircraft takes it out of its type design. The FAA path is an experimental certificate. Order 8130.2L 10-3a: "the altered aircraft is no longer in compliance with its TC; therefore, the aircraft does not have an effective airworthiness certificate under which to conduct the flight test. In these cases, the FAA may issue an experimental airworthiness certificate for R&D flight testing and/or showing compliance with airworthiness regulations." [S FAA1]
- 10-3 lets the standard certificate be "held in suspension" for "short term projects such as flight testing for an STC project". If the need "exceeds 30 days, verify the need is valid, and reverify the need every 30 days thereafter". To reinstate, the aircraft must be reconfigured "to the approved type design" [S FAA1].
- R&D lasts 3 years [S FAA9]. Program letter per § 21.193. Three-view drawings are not needed for a converted TC aircraft "without an appreciable change in its external configuration" [S FAA8].
- **Exhibition (§ 21.191(d))** covers air shows and film work, "exhibiting the aircraft's flight capabilities ... at air shows, motion picture, television", per 8130.2L ch. 12. It does not fit engine development [S FAA1, FAA7].
- Cost and time for an R&D certificate on a converted certificated airframe: **[nf]**. DAR fee anecdotes run $500 to $2,000, and the FSDO charges nothing [F AF38].

---

### 3. Sources
| Key | Title / description | URL | Retrieved |
|---|---|---|---|
| FAA1 | FAA Order 8130.2L, Airworthiness Certification of Aircraft (01/30/2026) | https://www.faa.gov/documentLibrary/media/Order/Order_8130.2L.pdf | 2026-10-21 |
| FAA2 | FAA Orders index (8130.2L current; 8130.2K superseded) / EAA news 2026-02-05 | https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.current/documentNumber/8130.2 ; https://www.eaa.org/eaa/news-and-publications/eaa-news-and-aviation-news/2026-02-05-airworthiness-certification-of-aircraft | 2026-10-21 |
| FAA3 | AC 90-89C, Amateur-Built Aircraft and Ultralight Flight Testing Handbook (2/14/23) | https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_90-89C.pdf | 2026-10-21 |
| FAA4 | AC 90-116, Additional Pilot Program for Phase I Flight Test | https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_90-116.pdf | 2026-10-21 (referenced, not read) |
| FAA5 | 14 CFR 21.93 (eCFR) | https://www.ecfr.gov/current/title-14/section-21.93 | 2026-10-21 |
| FAA6 | 14 CFR 91.319 (eCFR) | https://www.ecfr.gov/current/title-14/section-91.319 | 2026-10-21 |
| FAA7 | 14 CFR 21.191 (eCFR) | https://www.ecfr.gov/current/title-14/section-21.191 | 2026-10-21 |
| FAA8 | 14 CFR 21.193 (eCFR) | https://www.ecfr.gov/current/title-14/section-21.193 | 2026-10-21 |
| FAA9 | 14 CFR 21.181 (eCFR) | https://www.ecfr.gov/current/title-14/section-21.181 | 2026-10-21 |
| AF1 | Aeromomentum AM15 page (prices, 185 lb, FADEC standard) | https://aeromomentum.com/am15-117hp-to-147hp/ | 2026-10-21 |
| AF2 | Aeromomentum firewall-forward packages index | https://aeromomentum.com/parts/firewall-forward-packages/ | 2026-10-21 |
| AF3 | Aeromomentum AM13 page (price, comparison table) | https://aeromomentum.com/am13-100hp-to-126hp/ | 2026-10-21 |
| AF4 | Aeromomentum package pages: zenith-650-750, zenith-601-701, kit-fox-7, sonex-legacy, rv-12, highlander | https://aeromomentum.com/parts/firewall-forward-packages/zenith-650-750/ (and sibling slugs) | 2026-10-21 |
| AF5 | Viking store (engine, mount, cowl, install prices) | https://www.vikingaircraftengines.com/new-products | 2026-10-21 |
| AF6 | Viking 130 engine page (220 lb, 2.33:1) | https://www.vikingaircraftengines.com/viking-130-engine | 2026-10-21 |
| AF7 | Viking Zenith 750 STOL page (900+ in Zenith; own fleet) | https://www.vikingaircraftengines.com/zenith-750-stol | 2026-10-21 |
| AF8 | Viking aircraft types | https://www.vikingaircraftengines.com/aircraft-types | 2026-10-21 |
| AF9 | Zenith CH 750 price sheet (STOL/Cruzer/Super Duty) | https://zenithair.net/wp-content/uploads/2022/03/750-price-2-pages-4-22.pdf | 2026-10-21 |
| AF10 | Airframer: Zenith STOL CH 750 release (2010, <400 h) | https://www.airframer.com/news/release/8664 | 2026-10-21 |
| AF11 | Zenith STOL CH750 Super Duty intro (250-300 h) | https://zenithair.net/intro-stol-ch750-super-duty/ | 2026-10-21 |
| AF12 | Zenith firewall-forward packages | https://zenithair.net/firewall-forward-packages/ | 2026-10-21 |
| AF13 | Plane & Pilot, "Viking Engine Wins STOL Competition & Customers" (2014-09-30) | https://planeandpilotmag.com/viking-engine-wins-stol-competition-customers/ | 2026-10-21 |
| AF14 | Barnstormers Light-Sport/Zenith category (2019 Zenith 750 STOL Viking 130, $69,000; classified-2031934) | https://www.barnstormers.com/category-20499-Light-Sport--Zenith.html | 2026-10-21 |
| AF15 | FLYING, 2019 Zenith CH 750 Cruzer, $135,000 (2026-08-06) | https://www.flyingmag.com/this-2019-zenith-ch-750-cruzer-is-an-adventurous-aircraftforsale-top-pick/ | 2026-10-21 |
| AF16 | AeroTrader experimental listings (CH650B Viking 130; search snippet) | https://www.aerotrader.com/Experimental-Homebuilt/aircraft-for-sale?type=Experimental/Homebuilt%7C5976145 | 2026-10-21 |
| AF17 | Barnstormers Light-Sport/Homebuilt (Cherry BX2, classified-2053152) | https://www.barnstormers.com/category-20381-Light-Sport--Homebuilt.html | 2026-10-21 |
| AF18 | Barnstormers Kit Planes/Zenith (701 kit w/ Viking 130, classified-2071967) | https://www.barnstormers.com/category-20252-Kit-Planes--Zenith.html | 2026-10-21 |
| AF19 | Barnstormers AM-15 147 hp engine ad | https://www.barnstormers.com/classified-1800121-AEROMOMENTUM-AM-15-HP-147HP.html | 2026-10-21 |
| AF20 | Barnstormers categories Kitfox/Rans/Just/Zenith/Experimental (Rotax 912 listings) | https://www.barnstormers.com/category-20394-Light-Sport--Kitfox.html ; https://www.barnstormers.com/category-20437-Light-Sport--Rans.html ; https://www.barnstormers.com/category-20391-Light-Sport--Just-Aircraft.html ; https://www.barnstormers.com/category-20360-Light-Sport--Experimental.html | 2026-10-21 |
| AF21 | VAF: Rotax 912iS 418 h $23,500 OBO (sold) | https://vansairforce.net/threads/edit-sold-rotax-912is-with-418-hrs-23-500-obo.244309/ | 2026-10-21 |
| AF22 | Zenith.aero forum, AM15 builder comments / off-plans engine install | https://zenith.aero/xn/detail/2606393:Comment:626975 ; https://zenith.aero/xn/detail/2606393:Comment:700547 | 2026-10-21 |
| AF23 | Zenith.aero, Oliver Reik AM15 CH650 thread (2017–2021) | https://zenith.aero/xn/detail/2606393:Comment:626975 | 2026-10-21 |
| AF24 | AOPA, Zenith CH 750 Super Cruzer at AirVenture (2026-07-21) | https://aopa.org/news-and-media/all-news/2026/july/21/zenith-aircraft-debuts-ch-750-super-cruzer-at-airventure | 2026-10-21 |
| AF25 | Kitfox pricing brochure Rev F (06/25) | https://kitfoxaircraft.com/wp-content/uploads/Kitfox-Pricing-Brochure-RevF-070225-sm.pdf | 2026-10-21 |
| AF26 | Sonex price increases (notice 2025-11-14, eff. 2025-12-15) | https://www.sonexaircraft.com/price-increases-111425/ | 2026-10-21 |
| AF27 | KITPLANES, "Homebuilder's Insurance" (2026-03-20) | https://www.kitplanes.com/homebuilders-insurance/ | 2026-10-21 |
| AF28 | BWI Aviation Insurance, experimental aircraft insurance | https://bwifly.com/aviation-insurance/experimental-aircraft-insurance/ | 2026-10-21 |
| AF29 | Zenith.aero forum, insurance comment (2018-05-27) | https://zenith.aero/xn/detail/2606393:Comment:629564 | 2026-10-21 |
| AF30 | KITPLANES Ask the DAR, major changes | https://www.kitplanes.com/?p=15446 | 2026-10-21 |
| AF31 | KITPLANES Ask the DAR, LLC ownership (Mel Asberry, 2015-07-16) | https://www.kitplanes.com/?p=6888 | 2026-10-21 |
| AF32 | AOPA, "Budget buy: Sonex-B kit" (July 2019) | https://www.aopa.org/news-and-media/all-news/2019/july/pilot/budget-buy-sonex-b-kit | 2026-10-21 |
| AF33 | Van's RV-12iS E-LSA kit order form (2-5-24) | https://www.vansaircraft.com/wp-content/uploads/2024/02/12iSOrderForm20052024.pdf | 2026-10-21 |
| AF34 | Van's RV-12iS page (engines, 700-900 h, E-AB eligible) | https://www.vansaircraft.com/rv-12is/ | 2026-10-21 |
| AF35 | Plane & Pilot, "New Fuel-Injected RV-12" (powerplant kit $33,870) | https://planeandpilotmag.com/new-fuel-injected-rv-12/ | 2026-10-21 |
| AF36 | YourDyno water-brake instrumentation kit | https://yourdyno.com/product/water-brake-engine-dyno-kit/ | 2026-10-21 |
| AF37 | Land & Sea DYNOmite dynamometer (etesters catalog) | https://linux.etesters.com/catalog/1440777C-0A1E-4C47-BAE7-43F52478FE1A/dynomite-dynamometer | 2026-10-21 |
| AF38 | EAA forums, DAR inspection fees | https://eaaforums.org/archive/index.php/t-6839.html | 2026-10-21 |

---

# Part C. Added by PROPULSION

- OT14 Suzuki G15A: 1,493 cc, 75 x 84.5 mm, CR 9.5, 71 kW at 6,000 rpm, 128 N m at 3,200 rpm [F]. https://mymotorlist.com/engines/suzuki/g15a/ ; https://autospeed.com/cms/a_2893/article
- OT15 Honda, 2015 Fit overview: direct-injected 1.5 L DOHC i-VTEC, 130 hp at 6,500 rpm, 114 lb ft (154.6 N m) at 4,600 rpm [S]. https://hondanews.com/en-US/releases/release-0cbf1ed981f84e70be2f2c4d4b68d17e-2015-honda-fit-overview
- OT16 rusEFI uaEFI: from US$275, sequential fuel and spark to 6 cylinders, port injection, on-board wideband controller, knock input, CAN, SD logging; enclosure +$50 [S]. https://www.shop.rusefi.com/shop/p/uaefi-ultra-affordable-efi ; comparison table https://wiki.rusefi.com/ECU-Comparison/
- OT17 rusEFI Proteus: from US$800, no case; 16 low-side drivers, 12 x 5 V ignition outputs, 2 VR and 6 Hall inputs, dual CAN [S]. https://www.shop.rusefi.com/shop/p/spring-blade-cyy7n ; https://wiki.rusefi.com/Proteus-Manual/
- OT18 MicroSquirt: 2 saturated injector drivers (up to 4 high-impedance injectors each), 4 logic-level ignition outputs [S]. https://www.msextra.com/product-range/microsquirt/ ; https://diyautotune.com/blogs/technical-articles/megasquirt-systems-compared
