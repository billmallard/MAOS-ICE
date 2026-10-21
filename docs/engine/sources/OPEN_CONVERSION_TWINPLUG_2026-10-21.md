# Factory twin-plug (2 spark plugs/cylinder) automotive engines, ~90-350 hp: research notes

Read 2026-10-21. Quotes are near-verbatim. Most were pulled through a page-summarising fetch tool, so check them against the live page before using them in a design document.
Source tags: [P] = primary or OEM press release, [W] = Wikipedia, [S] = secondary (spec site, retailer, journalism), [F] = forum, [SN] = search snippet only (page not opened).
Where something says "not found", the search turned up nothing. It does not mean the thing doesn't exist. The web-search budget ran out partway through. That left these open: HEMI weight from an OEM source, Lima 2.3 weight, L13A weight, used-core prices for most engines, and how the M112/M113 coils are wired.

## Summary table

| Engine | Layout / cc | Rated output | V/cyl | Block | Dry mass (source quality) | Years | In production 2026? | OEM twin-plug firing |
|---|---|---|---|---|---|---|---|---|
| Mercedes M112 (E24/E26/E28/E32/E37) | 90 deg V6, 2.4-3.7 L | E26 168-174 bhp@5500 / 240 Nm; E32 215-224 bhp@5700 / 315 Nm; E37 232-241 bhp@5750 / 344 Nm [T1] | 3 (SOHC) | Alusil aluminium [T1] | 160 kg (E24/E28/E32/E37) [T6, S, inclusions unstated] | 1996/97-2015 [T1] | No | One coil pack per cylinder feeding two plugs (pack has outputs "a"/"b") [T7, T9]. Exact coil topology unresolved [T8] |
| Mercedes M113 (E43/E50/E55) | 90 deg V8, 4.3/5.0/5.4 L | E43 275 hp@5750 / 400 Nm; E50 302 hp@5600 / 460 Nm; E55 342-362 hp / 510-530 Nm [T2] | 3 (SOHC) | Alusil aluminium [T2] | 196 kg (E43, E50) [T5, S, inclusions unstated] | 1997-2011 [T2] | No | Same family design as M112; ECU fires both plugs of a cylinder together [T8] |
| Chrysler Gen III HEMI 5.7 | 90 deg V8, 5.7 L | 345 hp/375 lb-ft (2003); 357-395 hp / 389-410 lb-ft (2009+) [T3]; 2026 Ram 1500 eTorque: 395 hp / 410 lb-ft [T12] | 2 (OHV pushrod) | Cast iron, aluminium heads [T3] | ~520-550 lb "dry", ~560 lb dressed [T15, S, no OEM source] | 2003-present | YES (Ram 1500 MY2026, Durango; Saltillo) [T12-T14] | Coil-on-plug. 2003-05: each coil drives its own plug plus, by wire, a plug in the companion cylinder (waste spark), pairs 1/6, 8/5, 4/7, 3/2. 2006+: dropped the cross wires [T11, SN] |
| HEMI 6.4 (392) | V8, 6.4 L | 470-485 hp / 470-475 lb-ft [T3]; Durango R/T 392: 475 hp / 470 lb-ft [T16] | 2 | Cast iron [T3] | not found | 2011-present | YES (Ram HD, Wrangler 392, Durango) [T14] | 16 plugs [T10] |
| HEMI 6.2 SC (Hellcat) | V8 supercharged | 707 hp+ (outside 350 hp class) [T3] | 2 | Cast iron | not found | 2015-present | YES (Durango Hellcat, Ram TRX) [T14] | 16 plugs [T10] |
| Honda L13A i-DSI | I4, 1.3 L | 63 kW (86 PS)@5700 / 119 Nm@2800 [T17]; 83-95 PS range [T18] | 2 (SOHC 8 V) | not found (L-series is aluminium; not sourced) | not found ("8% lighter" than previous Honda 1.3 L [T17]) | 2001-c.2008 i-DSI | No (not found in current models) | Sequential. Intake-side plug fires first, exhaust-side "shortly thereafter", phasing depends on speed and load [T17] |
| Honda L12A i-DSI | I4, 1.2 L | 78 PS@5700 / 110 Nm@2800 [T18] | 2 | not found | not found | 2002-2008 [T18] | No | as L13A |
| Ford 2.3 Lima twin-plug (and 2.5 1998-2001) | I4 SOHC, 2.3 L | 100 hp@4600 / 133 lb-ft@2600 (Ranger 1989-95) [T20]; W: 105 hp / 135 lb-ft [T19]; 2.5: 117-119 hp [T20] | 2 | Cast iron [T19] | not found | 1989 (Ranger), 1991 (Mustang) to 2001 [T19] | No | DIS. Two coil packs, intake-side and exhaust-side, both firing [T20, S paraphrase]. Waste-spark packs per general Ford DIS practice: not confirmed |
| Alfa Romeo Twin Spark 16V 2.0 | I4 DOHC, 1970 cc | 150-155 PS@6400 / 181-187 Nm [T21] | 4 | Cast iron, alloy head [T21] | not found | 1986-2009 (family) [T21] | No | 8V: both plugs fire together, symmetric. 16V: central main plug plus smaller secondary plug at the chamber edge [T21] |
| Nissan Z20/Z22/Z24 NAPS-Z | I4 SOHC 2V | Z24: 103-106 hp / 134-137 lb-ft [T22] | 2 | Cast iron, aluminium head [T22] | not found | 1979-1989 [T22] | No | not found |
| Porsche 964 (M64/01) / 993 (M64/05 etc.) | air-cooled flat-6, 3.6 L | 964: 250 PS@6100 / 310 Nm@4800 [T23] | 2 | Aluminium (not sourced here) | not found (one search snippet gave "1,350 kg", which is a car weight, rejected) | 964 1989-94; 993 1994-98 | No | Twin distributors (second driven by a belt from the first), twin coils and igniters; both plugs fire together [T24, F/S] |

Outside the brief, but relevant:
- Motorcycles: BMW boxers (R1100S, R1150 GS/R/RS/RT) went to dual ignition across the 2003 range, with "the plugs spark in parallel" [T25, SN]. The 2004+ R1200 Cruiser and other R1200s also have it [T25]. Ducati Multistrada (DS "Dual Spark") and Honda VT500 are listed [T4].
- Mazda rotaries (13B / Renesis) have two plugs per rotor (leading and trailing). That is from general knowledge; it was not sourced in this run. I could not confirm how many plugs the 8C single-rotor (MX-30 R-EV, in production) has.
- Nash Ambassador straight-8 (1932-48) [T4]: historic only.

## Production status of the HEMI, 2025-2026 (asked for explicitly)

- June 2025: Ram announced the 5.7 HEMI's return to the Ram 1500 for MY2026. The engine is "395 hp and 410 lb-ft of torque", is a $1,200 option on lower trims, and comes at no extra cost on Limited and Longhorn [T12, S].
- 2025-08-30: "the first batch of 2026 Ram 1500 pickups equipped with the HEMI" left Sterling Heights Assembly Plant. It is a "5.7-liter (345 cubic-inch) HEMI V8 with eTorque mild-hybrid system". Kuniskis: "we received 10,000 orders in the first 24 hours" [T13, S].
- 2026-01-22: "The goal for 2026 is to manufacture over 100,000 HEMI engines, more than tripling the 2025 output." 5.7 goes to Ram 1500 and Durango, 6.4 to Wrangler 392 and Ram HD, 6.2 SC to Durango Hellcat and Ram TRX. The engines are built at Saltillo, Mexico, with Dundee, Michigan expected to follow [T14, S].
- 2026-06-02: the 2027 Durango R/T 392 is billed as "the last opportunity for consumers to purchase a new Durango equipped with the HEMI V-8 engine". That ends the HEMI in the Durango only, not across Stellantis [T16, S].
- Conclusion: in 2026 the HEMI is the only factory twin-plug engine family in this power class that is still in volume production. The other engines on the list were out of production by 2015 or earlier.

## Aftermarket standalone ECU support

- HEMI: Holley Terminator X / X Max Gen III HEMI kits cover 2003-2013+ 5.7, 6.1 and 6.4. They are sold as a standalone EFI and include base maps. Price is about $1,950-2,500 [T26, SN; holley.com returned 403].
- M113: on HPAcademy, a builder going standalone was pointed to MaxxECU Race, Haltech Elite or MoTeC. The coils "appear to be dumb coils", so an igniter is needed. Advice: "firing dual plugs requires ... 8 ignition events" with two coils in parallel per output, or "leading/trailing" split timing if wanted. The builder chose to "fire the plugs together for each cylinder" [T8, F].
- L13A, Lima 2.3, Alfa TS, Nissan Z, 964/993: no dedicated standalone ECU kit found in this run. Generic ECUs (Haltech, Link, rusEFI, MegaSquirt) can drive extra coil outputs, but that is not sourced here.

## Aviation use

- Porsche PFM 3200 is the only factory-twin-plug car-engine lineage with documented certified aviation use. It is "derived from the engine used in the Porsche 911" [T27], has "dual electronic ignition", and makes "nearly 217 hp" at more than 5,000 rpm through a reduction gearbox to a 2,300 rpm propeller [T28]. N03: 217 hp at 5300 rpm, 403 lb [SN, T27-snippet]. About 80 engines were built and 41 Mooney M20L airframes; production ended in 1991 and the type certificate was surrendered on 2007-09-17 [T27]. Note that the PFM came from the 3.2 Carrera (a single-plug car engine) and Porsche added the dual ignition for aviation [SN]. It is not a 964 conversion.
- Mercedes M112/M113: no aircraft or PSRU conversion found (searched; results were only car swaps) [T29].
- Modern Gen III HEMI: no aircraft or PSRU conversion found. Searches returned Jeep swap kits and the WWII Chrysler XIV-2220 [T30]. Generic PSRU makers (e.g., autopsrus.com) claim a 150-550 hp range, but none names a HEMI or Mercedes application [T31, SN].
- Ford 2.3 twin-plug, Honda L13A, Alfa TS, Nissan Z: no aviation use found.

## Used-core price snapshot (thin)

- M112 3.2: eBay listings at EUR 400 + 100 shipping (W210 M112941, complete), EUR 1,046.90 (SLK M112947, incomplete), US$440 (183k mi assembly), GBP 395 [T32, SN, listing dates unknown].
- 5.7 HEMI: a forum post put a bare block at "around $300" [T33, F]. No complete-core price was found.
- The rest: not found (search budget exhausted).

## Key sources

| Key | URL | Read | Tag | Quote |
|---|---|---|---|---|
| T1 | https://en.wikipedia.org/wiki/Mercedes-Benz_M112_engine | 2026-10-21 | W | "two spark plugs per cylinder"; "silicon/aluminum (Alusil) engine blocks"; SOHC "3 valves per cylinder"; E37 "232-241 bhp at 5,750 rpm, 344 N-m"; "Introduced in 1996" |
| T2 | https://en.wikipedia.org/wiki/Mercedes-Benz_M113_engine | 2026-10-21 | W | "two spark plugs per cylinder"; "3 valves per cylinder (two intake, one exhaust)"; E50 "306 PS (225 kW; 302 hp) at 5,600 rpm", "460 N-m ... at 2,700 to 4,250 rpm"; 1997-2011 |
| T3 | https://en.wikipedia.org/wiki/Chrysler_Hemi_engine | 2026-10-21 | W | Gen III: "two spark plugs per cylinder" with "coil-on-plug (distributor-less) ignition"; cast-iron blocks, aluminium heads; 5.7 2009+ "357-395 horsepower", "389-410 lb-ft" |
| T4 | https://en.wikipedia.org/wiki/Dual_ignition | 2026-10-21 | W | lists Alfa Twin Spark, "Honda cars with the i-DSI series engines", "Chrysler's Modern Hemi engine", "Nissan NAPS-Z", Ford Ranger 1989 / Mustang 1991 4-cyl, Mercedes M112, M113; motorcycles Honda VT500, Ducati Multistrada, BMW R1100S |
| T5 | https://mymotorlist.com/engines/mercedes/m113-e50/ | 2026-10-21 | S | Weight "196" kg; years "1997-2008"; "296 - 306" hp, 460 Nm (inclusions not stated) |
| T6 | https://mymotorlist.com/engines/mercedes/m112-e32/ | 2026-10-21 | S | Weight "160" kg; "1997-2007"; "190 - 224" hp; E32 ML "354" hp (inclusions not stated). Same 160 kg on the E24/E28/E37 pages (SN) |
| T7 | https://w220.wiki/Ignition_system | 2026-10-21 | S (wiki) | "There is one coil pack per cylinder, which produces spark for two spark plugs per cylinder." |
| T8 | https://www.hpacademy.com/forum/general-tuning-discussion/show/standalone-ecu-for-twin-spark-v8/ | 2026-10-21 | F | M113 build: "It appears they're dumb coils, but I see Haltech does a suitable ignitor module"; "8 ignition events"; "any ECU that has the current rating required for two coils in parallel"; builder will "fire the plugs together for each cylinder". A snippet adds "twin dumb coils per cylinder, one per spark plug (Bosch 221 503 035)" (SN) |
| T9 | https://mbworld.org/?p=28018 | 2026-10-21 | F/S | "you'll see 'a' and 'b' markings which represent where each of the wires from the coil pack is supposed to go" |
| T10 | https://jalopnik.com/2016719/why-hemi-engines-have-16-spark-plugs/ | 2026-10-21 (art. 2025-11-05) | S | "the 5.7-liter, 6.2-liter, and 6.4-liter Hemi offerings" have two plugs per cylinder |
| T11 | https://www.enginelabs.com/?p=36499 (410 Gone); text from search snippet | 2026-10-21 | SN | pairs "1/6, 8/5, 4/7, and 3/2"; "Early 5.7 HEMIs from 2003-2005 have plug wires that fire across the motor in a wasted spark setup ... In 2006, they did away with the extra wires" |
| T12 | https://www.autoguide.com/auto/manufacturers/ram-manufacturers/2026-ram-1500-you-can-officially-have-a-hemi-v8-again-44620936 | 2026-10-21 (art. 2025-06-05) | S | "395 hp and 410 lb-ft of torque"; $1,200 option |
| T13 | https://moparinsiders.com/the-hemi-is-back-first-2026-ram-1500-v8-trucks-roll-out/ | 2026-10-21 (art. 2025-08-30) | S | "5.7-liter (345 cubic-inch) HEMI V8 with eTorque mild-hybrid system"; "we received 10,000 orders in the first 24 hours"; SHAP |
| T14 | https://www.guideautoweb.com/en/articles/80942/stellantis-aims-to-build-100-000-hemi-engines-in-2026 | 2026-10-21 (art. 2026-01-22) | S | "The goal for 2026 is to manufacture over 100,000 HEMI engines, more than tripling the 2025 output."; Saltillo; Dundee expected |
| T15 | https://kevinsautos.com/faq/how-much-does-a-2003-57-hemi-engine-weight.html | 2026-10-21 | S (low quality, uncited) | "dry weight ... approximately 520-550 pounds"; "A fully dressed 5.7L Hemi engine weighs approximately 560 lbs" |
| T16 | https://www.geneonline.com/2027-dodge-durango-r-t-392-marks-final-production-year-for-hemi-v-8-engine/ | 2026-10-21 (art. 2026-06-02) | S | "the last opportunity for consumers to purchase a new Durango equipped with the HEMI V-8 engine"; "475 horsepower and 470 lb.-ft." |
| T17 | https://global.honda/en/newsroom/worldnews/2001/4010518.html | 2026-10-21 | P | "two spark plugs in each of its newly designed, compact combustion chambers"; "intelligent, dual-point sequential ignition control"; "63kW (86PS) at 5700 rpm"; "119Nm (12.1kg-m) at 2800 rpm"; "8% lighter" |
| T18 | https://en.wikipedia.org/wiki/Honda_L_engine | 2026-10-21 | W | L12A i-DSI "8 spark plugs, 2 per cylinder", 78 PS@5700, 110 Nm@2800, 2002-2008; L13A i-DSI 83-95 PS |
| T19 | https://en.wikipedia.org/wiki/Ford_Pinto_engine | 2026-10-21 | W | "A version with two spark plugs per cylinder, distributor-less ignition, and reduced main bearing sizes was introduced in the 1989 Ford Ranger and 1991 Ford Mustang."; 105 hp / 135 lb-ft; through 2001 |
| T20 | https://therangerstation.com/tech_library/4cylinders.shtml | 2026-10-21 | S | "In 1989 the 2.3 was changed to a DIS ... utilizing a new 8-plug head (2-plugs per cylinder)"; 100 hp@4600, 133 ft-lb@2600; coil-pack description paraphrased by the tool |
| T21 | https://en.wikipedia.org/wiki/Alfa_Romeo_Twin_Spark_engine | 2026-10-21 | W | "two spark plugs per cylinder"; 16V: central plug plus smaller secondary; "a heavier cast-iron block engine, with an alloy head"; 2.0 150-155 PS@6400 |
| T22 | https://en.wikipedia.org/wiki/Nissan_Z_engine | 2026-10-21 | W | "NAPZ motors had dual spark-plugs (two per cylinder) except the pre-82 versions and latest versions of the Z24i" |
| T23 | https://en.wikipedia.org/wiki/Porsche_911_(964) | 2026-10-21 | W | "Twin-spark with knock regulation"; "250 PS (184 kW; 247 hp) at 6,100 rpm"; "310 N-m (229 lb-ft) at 4,800 rpm" |
| T24 | https://www.fvd.net/us-en/930602015AX3ATK/distributor-964-993-dual-ignition-remanufactured-complete-6-part-repair-send-in.html ; https://rennsportkc.com/964-distributor-rebuild/ | 2026-10-21 | SN/F | 964/993 twin distributors cover M64/01-03 and M64/05, /06, /20, /21, /22; "secondary distributor being driven by the first distributor via a small tooth belt" |
| T25 | https://www.motorbikestoday.com/news/Articles/BMW%20ignition.htm | 2026-10-21 | SN | "BMW Motorrad introduced dual ignition on its 2003 range"; "the plugs spark in parallel" |
| T26 | https://www.holley.com/products/fuel_systems/fuel_injection/terminator_x/parts/550-1225 | 2026-10-21 | SN | Terminator X for "GEN III HEMI engines from 2003-2013+, including the 5.7L, 6.1L and 6.4L" |
| T27 | https://en.wikipedia.org/wiki/Porsche_PFM_3200 | 2026-10-21 | W | "derived from the engine used in the Porsche 911"; N03 "162 kW (217 hp) at 5300 rpm"; about 80 delivered; TC surrendered 2007-09-17. A snippet adds "weighed 403 pounds" and "gained a dual ignition and two alternators" |
| T28 | https://planeandpilotmag.com/this-incredible-plane-mooney-porsche-m20l-pfm/ | 2026-10-21 | S | "dual electronic ignition"; "nearly 217 hp"; propeller at 2,300 rpm through a reduction gearbox |
| T29 | search "Mercedes M113 V8 aircraft conversion PSRU" / "M112 ... gyroplane OR airplane" | 2026-10-21 | - | no aviation hits (not found) |
| T30 | search "HEMI V8 aircraft engine conversion PSRU homebuilt" | 2026-10-21 | - | only Jeep swaps and XIV-2220 (not found) |
| T31 | https://autopsrus.com/?p=399 | 2026-10-21 | SN | PSRUs "can be adapted to just about anything between 150 HP to 550 HP" |
| T32 | https://www.ebay.de/p/16051843575 and others | 2026-10-21 | SN | M112947 EUR 1,046.90; M112941 EUR 400 + EUR 100 shipping; US$440; GBP 395 |
| T33 | https://www.forabodiesonly.com/mopar/threads/need-quick-rundown-5-7-hemi-apart.290113/post-1970571538 | 2026-10-21 | F/SN | 5.7 block "around $300" |
