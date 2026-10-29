# Suzuki Hayabusa (GSX1300R) as an aircraft-engine core: research notes

Read date for every source: **2026-10-19**. Source numbers [n] refer to the list at the end.

How the sources are labelled:
- **Primary**: Suzuki press kit or brochure, Suzuki owner's or service manual, Suzuki parts catalogue (RevZilla OEM fiche shows Suzuki part numbers and US prices).
- **Secondary**: magazines and spec aggregators.
- **Forum**: owner or builder posts.
- **Snippet**: the figure came from a search-engine summary because the page itself was blocked (HTTP 403). Do not rely on these without checking.
- **Unverified (memory)**: not backed by a source I fetched.

Generations: Gen1 = 1999-2007, 1299 cc (Suzuki gives 1,298 cm³). Gen2 = 2008-2020, 1340 cc (Suzuki JP gives 1,339 cm³). Gen3 = 2021 on, 1340 cc.

The dyno charts were read from the chart URLs given with sources 16-19; the images are not committed (third-party copyright).

---

## 1. Engine specifications by generation

| Item | Gen1 (1999-2007) | Gen2 (2008-2020) | Gen3 (2021 on) |
|---|---|---|---|
| Bore x stroke | 81 x 63 mm [1] ("81×63") | 81.0 x 65.0 mm [1][4][11] | 81.0 x 65.0 mm [5] ("81.0 mm x 65.0 mm (3.19 in. x 2.56 in.)") and [13] |
| Displacement | 1,298 cm³ [1][2] | 1,340 cm³ [11] (Suzuki JP: 1,339 [1]) | 1,340 cc [5][13] |
| Compression ratio | 11.0:1 [3] (secondary). **Conflict:** [9] says Gen2 went "to 12.5:1 from 11.5:1" | 12.5:1 [11] ("12.5 : 1") | 12.5:1 [5][13] |
| Claimed crank power | 128.7 kW (175 PS) at 9,800 rpm [1] | 145 kW (197 PS) at 9,500 rpm [1]. US sites quote 194 hp (145 kW) at 9,500 [4] | 138 kW (188 PS) at 9,700 rpm [1]. AU: 140 kW at 9,700 [20] |
| Claimed torque | 138.2 Nm at 7,000 rpm [1] | 155 Nm at 7,200 rpm [1] | 149 Nm at 7,000 rpm [1]. AU: 150 Nm at 7,000 [20] |
| Redline / rev limiter | "hang on to the 11,000rpm redline" [46] (secondary, used-bike test, generation not stated). No Suzuki figure found | Not found in a Suzuki document | Gen3 manual: tach red zone exists and a limiter acts in neutral. **No rpm value given** [13] |
| Valve train | DOHC, 16 valves [3] | DOHC, 16 valves, titanium valves [9] | DOHC, 16 valves, titanium valves, higher-rate springs [5] |
| Cam drive | Chain. Same cam chain part 12760-24F01 on all three generations [26][40][42] | Chain [40] | Chain [26] |
| Cam chain tensioner | Parts fiche shows the adjuster set 12800-24F11 with a spring **and** an oil hose to the tensioner (12835-24F00) [42]. Note that [9] says Gen2 is "now hydraulically operated", which implies Gen1 was not. **Unresolved** | "The cam chain tensioner is now hydraulically operated" [9]. "accomplished hydraulically" [8]. Fiche shows adjuster 12830-15H01 plus an oil hose [40] | Press kit: "redesigned to minimize chain runout… Teflon coating on the slipper" [5]. Fiche: adjuster 12830-15H10 plus "HOSE, CAM CHAIN TNSN ADJ OIL" 12835-15H00 [26]. This means oil-pressure (hydraulic) adjustment carried over from Gen2 |
| Crank type | 180° flat-plane inline-4: **unverified (memory)**. Firing order 1-2-4-3 [14] fits a 180° crank | same | same |
| Balancer | Gear-driven counterbalancer (secondary search summary). A "Counter Balancer" appears in used-part listings [24] | Single balancer shaft (2014 fiche) | "A gear-driven balancer shaft is timed to the crankshaft" [5]. One shaft and one balancer weight in the fiche [31] |
| Rod and main bearings | Plain shell bearings, colour-coded for selective fit [42] | Plain shell bearings. Service data: big-end clearance 0.032-0.056 mm, main journal clearance 0.010-0.028 mm, crank pin OD 37.976-38.000 mm, journal OD 39.982-40.000 mm [12, p.320] | Plain shells: "BEARING, CRANK PIN" in 4 colour grades and "BEARING, CRANKSHAFT" in 5 grades, plus thrust shims [25] |
| Connecting rods | Not found | "chrome-molybdenum steel-alloy… shot peening" [9] | New design, 3 g lighter, more rigid [5] |
| Pistons | Not found for the OEM part. Aftermarket forged kits exist. | "Redesigned **forged** three-ring aluminum-alloy pistons" with chrome-nitride coating [9] | "three-ring, aluminum-alloy slipper pistons… reducing the weight of each piston by 26 grams" [5]. **Forged or cast is not stated: not found** |
| Piston cooling | Not found | Service manual lists a "Piston cooling oil jet bolt" [12, p.339] | Not found |
| Cylinder bores | SCEM-plated cylinders [2] | Bore 81.000-81.015 mm, piston-to-bore clearance 0.035-0.045 mm [12, p.320] | SCEM coating, U-shaped cut-outs between bores to vent pumping pressure [5] |
| Lubrication | Wet sump [3]. Oil capacity: not reliably found | Wet sump. Oil change 3,100 ml, with filter 3,300 ml, overhaul 4,000 ml [12, p.339]. Oil pressure 200-500 kPa at 3,000 rpm and 60 °C [12, p.339] | Wet sump [5]. Oil change 3,200 ml, with filter 3,400 ml, overhaul 4,100 ml [13] |
| Oil pump | Not found | One pump assembly: "Do not attempt to disassemble the oil pump. The oil pump is available only as an assembly" [12, p.338]. Rotor type (trochoid?) not stated | **One** pump assembly, 16400-24F01, gear-driven (drive gear NT34, driven gear NT37), relief valve 16440-24F00 [29]. Press kit: 54% more oil flow to the crank "without changing the oil pump" [10] |
| Oil cooler | Not found | 10-row core [8] | "large-capacity air-cooled oil cooler" below the radiator [5]. Part 16600-10L00 [30] |
| Compression pressure (service) | Not found | 1,400-1,800 kPa, minimum 1,000 kPa [12, p.320] | Not found |

## 2. Dyno curves (stock bikes)

The Gen2 values were read off a chart by eye and the Gen3 values off a Dynojet chart. Expect about ±2 units of reading error. As a cross-check, hp = lb-ft × rpm / 5252 agrees within about 1 hp at each point.

| rpm | Gen2 rear-wheel hp | Gen2 rear-wheel lb-ft | Gen3 2022 rear-wheel hp | Gen3 2022 rear-wheel lb-ft |
|---|---|---|---|---|
| 5,000 | ~86 | ~90.5 | ~87 | ~91 |
| 6,000 | ~110 | ~96 | ~110 | ~96.5 |
| 7,000 | ~140 | ~105 | ~137 | 103.0 (peak, labelled) |
| 8,000 | ~161 | ~106 | ~153 | ~100.5 |
| Peak | 180 hp at 9,500; 107 lb-ft at 7,500 [16] | | 170.3 hp at 9.8k; 103.0 lb-ft at 7.0k (chart legend) [18] | |

Notes on the curves:
- **Gen2 [16] (secondary):** motostatz.com. The test bench is not named, and the chart is a redrawn curve, not a dyno printout. The bike in the picture has an Akrapovic exhaust, so it may not be stock. Treat as indicative only.
- **Gen3 [18] (tuner):** BT Moto, Dynojet, "CF: STD Smoothing: 5". The red trace is labelled stock, run on 93 octane pump fuel. All figures are **rear-wheel**.
- **Other stock Gen3 rear-wheel results:**
  - 173 hp at 9,800 and 106 lb-ft at 6,900 on Jett Tuning's rear-wheel dyno [19]
  - 175.06 whp at 9.74k and 109.06 lb-ft at 6.88k on a Dynojet [17]
- No crank-dyno curve was found for any generation.

## 3. Engine mass

| Item | Value | Source / grade |
|---|---|---|
| Suzuki-published engine mass (with or without gearbox) | **Not found.** The service manual's engine removal and installation pages give no mass [12, p.245] | — |
| "A Hayabusa engine is around the 90kg mark" / "1.3 Hayabusa 92kg" | 90-92 kg. Not stated what is included, and no poster says they weighed one | Forum [21] |
| "Shipping weight of a bare busa engine is 190 lbs" (86 kg). "Around 200lbs complete with transmission and all liquids" | 86-91 kg | Snippet / forum [22]. Original page returned 403 |
| Radical V8 (two Hayabusa-derived blocks) | "95kg dry with induction" | Forum [21]. Not relevant to an I4 |
| Westfield Megabusa / Radical / Suzuki crate-engine published mass | Not found. Wikipedia gives only the Megabusa car curb weight, "from 440 kg" [49] (snippet) | — |
| Whole motorcycle | Gen1: 215 kg dry [2]. Gen2: 220 kg dry, 266 kg wet [8]. Gen3: 264 kg curb (US) [5]; 262 kg running order (Brazil) [13] | Primary / secondary |

The gearbox and clutch sit inside the crankcase (see section 4), so every "engine" figure above already includes them. There is no "without transmission" variant.

## 4. Drivetrain

| Item | Gen1 | Gen2 | Gen3 |
|---|---|---|---|
| Primary reduction | Not found | 1.596 (83/52) [11][12, p.555] | 1.596 (83/52) [13]. Primary driven gear "NT:83" [35] |
| 1st | Not found | 2.615 (34/13) | 2.615 (34/13) [13] |
| 2nd | — | 1.937 (31/16) | 1.937 (31/16) |
| 3rd | — | 1.526 (29/19) | 1.526 (29/19) |
| 4th | — | 1.285 (27/21) | 1.285 (27/21) |
| **5th** | — | **1.136 (25/22)** | **1.136 (25/22)** |
| **6th** | — | **1.043 (24/23)** | **1.043 (24/23)** |
| Final drive | Not found | 2.388 (43/18), 530 chain, 114 links [11][12] | 2.388 (43/18), RK GB50GSVZ5, 114 links [13] |
| Overall crank-to-output-sprocket ratio in 6th | — | 1.596 × 1.043 = 1.665 (calculated) | same |
| Gearbox integral to crankcase | Yes, 6-speed constant-mesh in the engine cases | Yes | Yes: "Oil jets in the crankcase spray lubricating oil on the fourth, fifth, and sixth gears" [5]. Countershaft and driveshaft are in the engine fiche [36] |
| Clutch | Wet multi-plate with "Back-torque limiter" [3] | Wet multi-plate, hydraulic release [4][8] | "Wet, multi-plate type, SCAS-equipped" [5]: SCAS is Suzuki's assist-and-slipper ("back-torque-limiting") clutch, hydraulically operated [5] |
| Cush/damper in the primary driven gear | Fiche sells only the complete "GEAR ASSY, PRI DRIVEN" (Gen3 21200-24810, US$545.01 [35]); no separate damper part. Brock's instructions tell you to inspect the "outer basket and backing plate springs" [47]. A tuner describes a sprung hub with springs between the primary gear and the clutch outer (forum). **No Suzuki statement found** | same | same |

## 5. Fuel and ignition

| Item | Gen1 | Gen2 | Gen3 |
|---|---|---|---|
| US octane requirement | Not found | "premium unleaded gasoline with a minimum pump octane rating of 90 ((R+M)/2 method)" (US owner's manual, July 2008, 99011-15H51-03A) [11, p.14] | **Primary source not found.** A manualsnet "FAQ" says 91 octane [48]; this is unreliable and should be treated as unverified |
| Europe / other markets | UK gov E10 list for Suzuki Motorcycles: "2002 onwards: all motorcycles can use E10 with no problems"; for 1992-2001 "some models can use E10… contact their national importer" [45]. This affects Gen1 1999-2001 | E10 OK (2002+) [45] | Brazil manual: "gasolina premium sem chumbo com índice de octanagem de 95 ou superior" (premium unleaded, octane 95 or higher). **Scale (RON or AKI) not stated** [13, p.1-18]. E10 OK [45] |
| Ethanol wording | — | "Blends of unleaded gasoline and ethanol… 'GASOHOL', may be used… if the ethanol content is not greater than 10%." MTBE up to 15%. "DO NOT USE fuels containing more than 5% methanol" [11, p.14]. **E15: not mentioned, so not found** | Brazil manual allows Brazilian pump fuel "que contém entre 22% e 30% de etanol anidro" (22-30% anhydrous ethanol) [13, p.1-19]. That is a Brazil-market statement only. A US Gen3 manual statement was not found |
| Injectors | 4 (one per cylinder), "330cc/min" [14] (tuner knowledge base) | 8 (two per cylinder, each 12-hole). Primary aimed down the port, secondary aimed at the secondary throttle valve [9]. "4x primary and 4x secondary injectors that are staged. All are listed as 280cc/min" [14]. Upper injectors are used "above 7000rpm" [15] (tuner FAQ) | 8: "four primary fuel injectors… directly into the intake pipes. Four additional Suzuki Side Feed Injectors (S-SFI)… above the throttle body" [5]. Primary 15710-14J00 (×4, US$337.91 each); secondary 15710-17K10 (×4, US$249.07 each) [33]. **Flow rates not found** |
| Throttle bodies | 46 mm [3] | 44 mm twin-valve (SDTV) [9] | 43 mm tapered, ride-by-wire [5]. "BODY ASSY, ACCELERATOR" (twist-grip sensor) 13500-10L00 [33] |
| Spark plug | NGK CR9E or DENSO U27ESR-N (2001 owner's manual, as read by the fetch tool's summary) [52] | NGK CR9EIA-9 / DENSO IU27D (2019) [4] | NGK CR9EIA-9 or DENSO IU27D [5][13]. Thread size: M10 x 1.0 is **unverified (memory)**, inferred from NGK "C"-type coding |
| Plugs per cylinder / coils | 1. Coil-on-plug, Denso 2-pin coils; needs an external igniter with a standalone ECU; dwell 1.5 ms at 14 V [14] | 1 plug; 4 coils, 33410-24F11 [41] | 1. "independent ignition coil-caps in each cylinder" [5]. 4 × 33410-10L00, US$109.18 each [28] |
| Crank position sensor | Variable-reluctance ("Reluctor"). MY1999-2001: "8x"; MY2002-2007: "24-1" [14] | Variable reluctance, "24-2 Reluctor" [14]. Service data: resistance 180-280 Ω, peak voltage "3.0 V and more" [12, p.189] | **Not found** (tooth pattern and sensor part number were not identified in the fiche) |
| Cam position sensor | "Reluctor" [14] | "Hall Effect", 5 V supply [14]. Part 33220-01H01 [41] | Same part number, 33220-01H01, US$126.26 [28]. That suggests the same Hall sensor (inference) |
| Throttle control | Cable | Cable | Ride-by-wire, 32-bit dual-core ECM, CAN harness [5] |
| Fuel pump and pressure | In-tank | "Approx. 300 kPa (3.0 kgf/cm², 43 psi)" [12, p.363] (service manual, generation probably Gen2) | In-tank pump assembly 15100-17K00 with built-in regulator 15610-17K00 [32]. Pressure **not found** for Gen3 |
| Injector resistance | — | 11-13 Ω at 20 °C [12, p.189] | Not found |
| Charging | 3-phase AC generator | 3-phase | 400 W, oil-cooled three-phase stator [5] |

## 6. Prices

### 6a. New crate or complete engine

| Item | Result |
|---|---|
| Suzuki OEM part number for a complete engine | **Not found.** The US fiche has no engine-assembly part number. The largest assemblies are the crankcase set 11300-10810 (US$2,814.38) [38] and the cylinder head assembly 11100-10L00 (US$2,180.43) [37] |
| Suzuki / Radical crate price | Not found. Radical SR3 RSX uses an "RPE-Suzuki 1340" engine (snippet [51]); no price found |
| Old race-engine reference | A 2007 race-cars.com Radical advert: "new zero hour 1507 Hayabusa engine with JE pistons… Carillo Rods… for an additional $9500 USD" [23]. Old and modified, so not a stock price |

### 6b. Used / salvage complete engines

Snapshot from the eBay aggregator picclick [24], read 2026-10-19. Of 100 items shown, 33 were complete engines.

| Generation | Example listings (title wording, price) |
|---|---|
| Gen3 | "2022-2025 … Only 654 Miles" US$6,030.00. "2025 … 3,970 Miles 30 Day Warranty" US$4,999.26. "2022-2026 … 3K Guaranteed" US$5,300.00. "21-26 … Runs Clean" US$5,999.00. "22-25 … Runs Great" US$7,500.00. A crankcase/head assembly with a "READ" note: US$3,999.99 |
| Gen2 | "2016 … 7K Miles" US$3,734.99. "2018 … 9K Miles" US$3,734.99. "2017 … 10k" US$3,495.00. "2012 … 20k" US$3,195.00. "2014 … 30k" US$3,195.00. "2008 … 32K Miles" US$2,999.95. Guaranteed unit US$3,817.68 |
| Gen1 | US$2,249.99 (35k mi) to US$4,679.97. Typically about US$2,400-3,400 |

Summary of the snapshot: about 6 Gen3, 10 Gen2 and 17 Gen1 complete engines in one view.

### 6c. OEM parts, new (Suzuki part number, US retail price on RevZilla OEM, 2026-10-19)

| Part | Gen3 (2022) | Gen2 (2014) |
|---|---|---|
| Cam chain | 12760-24F01, $183.57 [26] | same part, $183.57 [40] |
| Cam chain tensioner adjuster | 12830-15H10, $231.88. Tensioner (slipper) 12811-10L00, $97.51 [26] | 12830-15H01, price not shown [40] |
| Piston (each) | 12111-10L00-0F0, $186.78. Ring set $98.28 [25] | 12111-15H00-0F0, $250.81 [39] |
| Connecting rod (each) | 12160-10L00, $147.72 [25] | 12160-15H00, $242.59 [39] |
| Main bearing shells | 12229-10L00-0x0, $17.04 each (6 needed); 12229-15H10-0x0, $16.12-17.36 each (4 needed) [25]. A full set is about $170 (calculated) | Not shown |
| Crank-pin bearing shells | 12164-10L00-0x0, $18.33 each (8 needed) [25] | — |
| Crankshaft | Crankshaft set 12000-10840, $1,619.28 [25] | 12000-15810, $2,070.21 [39] |
| ECU | Not listed in the 2022 fiche: **not found** | FI control unit 32920-15H81, no price [41]. Used Gen2 ECU 32920-15H80: $299.73-376.31 [24] |
| Wiring harness | Main harness 36610-10L30, $1,023.87. No.2 harness $210.14, No.3 harness $216.68 [34]. Used Gen3 harness $175-799.99 [24] | 36610-15HC2, no price [41] |
| Stator | 32101-24F22, $403.54. Rotor 32102-10L00, $477.37 [27] | 32101-24F30, no price. Rotor $858.27 |
| Others | Oil pump $221.31 [29]. Oil cooler $421.60 [30]. Throttle body $1,045.78 [33]. Fuel pump assembly $609.40 [32]. Ignition coil $109.18 [28]. Primary driven gear assembly $545.01 [35]. Crankcase set $2,814.38 [38]. Head $2,180.43 [37] | Gen2 throttle body $2,443.18 |

## 7. Production volume

| Item | Value | Source |
|---|---|---|
| Cumulative production | "cumulative series production of over 200,000 units"; sold in 48 countries | Suzuki Global news, 30 Jun 2023 [43] (primary) |
| When 200,000 was reached | "achieved accumulated production of 200,000 units" in 2022 | [44] (secondary) |
| Gen1 share | ">100,000 examples of the first generation": search snippet only, original page not identified | Snippet |
| India | 543 units in FY26; 2,943 cumulative | [50] (snippet) |
| Units per year, worldwide | Not found | — |

## Gaps / not found

These items were searched for and not found. Search terms are summarised.
- **Engine mass** from Suzuki, Westfield, Radical or any supplier. Searched: "Hayabusa engine weight kg", Megabusa, Radical RPE, shipping weight. Only forum figures of 86-92 kg were found.
- **New complete or crate engine** part number and price, from Suzuki or a race supplier.
- **Gen3 crank trigger pattern and CKP sensor.** Searched: Haltech/MoTeC/Link Gen3, 2022 24-2. Also **injector flow rates** for Gen3, and **fuel pressure** for Gen3.
- **US Gen3 owner's manual** octane and ethanol text. Searched: 99011-10L, manualslib, GSX1300RRQ. Only the Brazilian manual was retrieved. **E15** is not mentioned in any manual found.
- **Redline / limiter rpm** from Suzuki for any generation.
- **Gen1** compression ratio (11.0 vs 11.5 conflict), gear ratios, oil capacity and piston type.
- **Piston construction for Gen3** (forged or cast).
- **Primary-gear damper** confirmed in a Suzuki document.
- **Gen3 ECU** part number and price.
- **Crank-dyno curves**, and a Gen2 stock curve from a named test bench.
- **Units per year.**
- **180° crank**: stated from memory, not from a source.

## Sources (all read 2026-10-19)

1. Suzuki Digital Library, Hayabusa (GSX1300R) export models (JP): https://www.suzuki.co.jp/suzuki_digital_library/2_moto/sports_078.html
2. Global Suzuki digital archive, 1999 Hayabusa: https://www.globalsuzuki.com/motorcycle/smgs/digital-archive/2_bike/sports_078.php
3. suzukicycles.org, Hayabusa Gen1: https://suzukicycles.org/Hayabusa/GSX1300R-Hayabusa-1.shtml
4. suzukicycles.org, Hayabusa Gen2: https://suzukicycles.org/Hayabusa/GSX1300R-Hayabusa-2.shtml
5. Suzuki Motor of America, 2022 Hayabusa press brochure (ai3 02/03/2021), hosted at: https://library.rvusa.com/brochure/2022-Suzuki-Hayabusa.pdf
6. Global Suzuki, 2022 Hayabusa product page: https://www.globalsuzuki.com/motorcycle/smgs/products/2022hayabusa/
7. motorcyclespecs.co.za, 2021 Hayabusa: https://www.motorcyclespecs.co.za/model/suzu/suzuki_gsxr1300r_21.html
8. motorcyclespecs.co.za, 2012 Hayabusa: https://www.motorcyclespecs.co.za/model/suzu/suzuki_gsxr1300r%2012.htm
9. Gardner Web, "Suzuki Refines Hayabusa Engine" (2008): https://www.gardnerweb.com/articles/suzuki-refines-hayabusa-engine
10. motorcycleriders.net, 2022 Hayabusa engine details: https://www.motorcycleriders.net/topic/3352-2022-suzuki-hayabusa-engine-details/
11. Suzuki GSX1300R owner's manual (July 2008, 99011-15H51-03A), manualslib, pp. 13-14 and 136: https://www.manualslib.com/manual/2760502/Suzuki-Gsx1300r.html
12. Suzuki GSX1300R service manual (Gen2 era, 663 pp), manualslib, pp. 189, 245, 320, 338, 339, 363, 384, 555: https://www.manualslib.com/manual/926988/Suzuki-Gsx1300r.html
13. Suzuki Motos Brasil, GSX1300RRQ owner's manual (Gen3), pp. 1-18, 1-19 and the specifications pages: https://suzukimotos.com.br/storage/manual-proprietario/GSX-1300RRQ.pdf
14. Haltech knowledge base, Hayabusa: https://support.haltech.com/portal/en/kb/articles/hayabusa
15. SBD Motorsport FAQ, 4 vs 8 injectors: https://sbdmotorsport.co.uk/ufaqs/whether-to-use-4-or-8-injectors-on-hayabusa-engines/
16. MotoStatz, Gen2 Hayabusa (chart: https://motostatz.com/wp-content/uploads/2021/06/Suzuki-Hayabusa-Dyno-Chart.jpg): https://motostatz.com/08-20-gsx1300r-hayabusa-acceleration-and-top-speed
17. BT Moto, 2022 Hayabusa review (chart: https://bt-moto.s3.us-west-1.amazonaws.com/profile_bren/1722399529122-image11.png): https://bt-moto.com/blog/2022-suzuki-hayabusa-review-bt-moto-flash-and-velocity-stacks-impact
18. BT Moto, 2022 Hayabusa Stage 1 (chart: https://bt-moto.s3.us-west-1.amazonaws.com/wp-content/uploads/2022/10/STOCKVS.-STG1BROCKEXHAUSTSTOCKSTACKS-copy.jpg): https://bt-moto.com/product/2022-suzuki-hayabusa-stage-1-with-handheld-diagnostic-tool
19. Rider Magazine, 2022 Hayabusa road test: https://ridermagazine.com/2022-suzuki-hayabusa-road-test-review/
20. AMCN, 2022 Suzuki Hayabusa: https://amcn.com.au/editorial/2022-suzuki-hayabusa/
21. LocostBuilders forum, engine weights thread: https://locostbuilders.co.uk/viewthread.php?tid=187997
22. Search snippet attributing "190 lbs shipping weight" (tapatalk DSR forum, HTTP 403): https://www.tapatalk.com/groups/dsrforum/hayabusa-engine-weight-t5382.html
23. Radical Sports Car Registry, race-cars.com advert PDF: https://radicalsportscarregistry.com/wp-content/uploads/2018/08/88-Description-from-race-cars.com_.pdf
24. PicClick (eBay aggregator), "suzuki hayabusa complete engine": https://picclick.com/Popular/suzuki-hayabusa-complete-engine
25. RevZilla OEM, 2022 Hayabusa crankshaft: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/crankshaft?submodel=gsx1300rrqm2
26. RevZilla OEM, 2022 cam chain: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/cam-chain?submodel=gsx1300rrqm2
27. RevZilla OEM, 2022 magneto: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/magneto?submodel=gsx1300rrqm2
28. RevZilla OEM, 2022 electrical: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/electrical?submodel=gsx1300rrqm2
29. RevZilla OEM, 2022 oil pan / oil pump: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/oil-panoil-pump?submodel=gsx1300rrqm2
30. RevZilla OEM, 2022 oil cooler: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/oil-cooler?submodel=gsx1300rrqm2
31. RevZilla OEM, 2022 crank balancer: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/crank-balancer?submodel=gsx1300rrqm2
32. RevZilla OEM, 2022 fuel pump: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/fuel-pump?submodel=gsx1300rrqm2
33. RevZilla OEM, 2022 throttle body (E03/E28): https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/throttle-body-e03e28?submodel=gsx1300rrqm2
34. RevZilla OEM, 2022 wiring harness (E03/E28): https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/wiring-harness-e03e28?submodel=gsx1300rrqm2
35. RevZilla OEM, 2022 clutch: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/clutch?submodel=gsx1300rrqm2
36. RevZilla OEM, 2022 transmission: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/transmission?submodel=gsx1300rrqm2
37. RevZilla OEM, 2022 cylinder head: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/cylinder-head?submodel=gsx1300rrqm2
38. RevZilla OEM, 2022 crankcase: https://www.revzilla.com/oem/suzuki/2022-suzuki-hayabusa/crankcase?submodel=gsx1300rrqm2
39. RevZilla OEM, 2014 crankshaft: https://www.revzilla.com/oem/suzuki/2014-suzuki-hayabusa-gsx1300r/crankshaft?submodel=gsx1300ral4
40. RevZilla OEM, 2014 cam chain: https://www.revzilla.com/oem/suzuki/2014-suzuki-hayabusa-gsx1300r/cam-chain?submodel=gsx1300ral4
41. RevZilla OEM, 2014 electrical (E03) and wiring harness: https://www.revzilla.com/oem/suzuki/2014-suzuki-hayabusa-gsx1300r/electrical-gsx1300ral4-e03?submodel=gsx1300ral4
42. RevZilla OEM, 2005 cam chain and crankshaft: https://www.revzilla.com/oem/suzuki/2005-suzuki-hayabusa-gsx1300r/cam-chain?submodel=gsx1300r
43. Global Suzuki news, 30 Jun 2023 (25th anniversary): https://www.globalsuzuki.com/globalnews/2023/0630.html
44. Autocar Professional, 25th anniversary / 200,000 units: https://www.autocarpro.in/news-international/suzuki-unveils-25th%C2%A0anniversary-edition-of-flagship-hayabusa-over-200000-sold-worldwide-115691
45. UK Government E10 checker, Suzuki Motorcycles: https://check-vehicle-compatibility-e10-petrol.service.gov.uk/en/manufacturer/Suzuki%20Motorcycles
46. Visordown, used test, GSX1300R Hayabusa: https://www.visordown.com/reviews/used-bike/used-test-suzuki-gsx1300r-hayabusa
47. Brock's Performance, Hayabusa Clutch Cushion Kit instructions: https://brocksperformance.com/content/Instructions/Hayabusa/S13-CCK_S13-CCK-LC_F.pdf
48. manualsnet, 2023 Hayabusa owner's manual page (FAQ text, unreliable): https://manualsnet.com/suzuki/hayabusa-gsx1300r-2023
49. Wikipedia, Westfield Megabusa (snippet): https://en.wikipedia.org/wiki/Westfield_Megabusa
50. BikeAdvice, Hayabusa FY26 India sales (snippet): https://bikeadvice.in/suzuki-hayabusa-sales-fy26-india-new-milestone-unlocked/
51. Wikipedia, Radical SR3 (snippet: RPE-Suzuki 1340): https://en.wikipedia.org/wiki/Radical_SR3
52. Suzuki GSX1300R owner's manual (Aug 2001), manualslib: https://www.manualslib.com/manual/868326/Suzuki-Gsx1300r.html
