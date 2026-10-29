# Concept H, an open conversion on a production core, and buying an Aeromomentum

Owner: PROPULSION. Issue: AER-3632 (MANUFACTURING pricing: AER-3633). Date: 2026-10-21.
Status: **exploration, not a ruling.** Bill asked for it after the Hayabusa decision (AER-3525). Nothing here changes REQUIREMENTS section 12, R-1 or R-28. Nothing here has been built, weighed, run or flown. This is an experimental engine design; nothing in it is certified, certifiable or flight-ready.

Numbers come from [`analysis/engine_open_conversion/open_conversion.py`](../../analysis/engine_open_conversion/open_conversion.py) (tables in `open_conversion_tables.md`). It reuses the program's cost lines (`engine_phase0/cost_floor.py`) and concept H's model (`engine_crank/scaling_sweep.py`), so all three options are on one basis. Tags: **[S]** sourced, **[F]** forum or search snippet only, **[E]** PROPULSION estimate with its method in the script, **[MFG]** MANUFACTURING's estimate on AER-3633, **[A]** assumed. Source keys are in [`sources/OPEN_CONVERSION_SOURCES_2026-10-21.md`](sources/OPEN_CONVERSION_SOURCES_2026-10-21.md). **None of the costs is a quote.**

## 1. The answer

**Recommendation: a split.**
- **At 100 hp, B: an open conversion.** At 100 hp the program cannot beat Aeromomentum on price or mass, and concept H loses badly. What the program can add there is openness.
- **At 200 hp, A: keep concept H.** At 200 hp nobody sells a normalized conversion, and the open conversion costs a mass, ignition-redundancy and supply penalty H does not.
- **At 300 hp, neither yet.** Both miss on mass or are not designed.

Bill's read of the Aeromomentum line is right **at 100 hp, and only there.**

| | 100 hp | 200 hp | 300 hp |
|---|---|---|---|
| **A, concept H**, first engine | $26.8k / $40.9k / $62.4k, 110-111 kg (normalized). **Loses to everything** | $31.7k / $48.0k / $72.7k, 143-158 kg, two plugs per cylinder. **The only option that meets R-25 and R-37** | $34.0k / $51.1k / $76.9k, 174-177 kg, **extrapolated**: the second module is not designed |
| **B, open conversion**, first engine, normalized | Suzuki 1.5 L: $12.7k / $20.5k / $33.1k, 105-142 kg | Subaru EZ36: **$18.3k / $29.5k / $47.4k**, 166-216 kg | GM LS3: $22.7k / $33.3k / $49.0k, 227-289 kg |
| **Baseline, Aeromomentum as sold** (not normalized) | AM15 $14.7k-16.6k, 88-91 kg; AM13 $13.2k-15.1k, 81-84 kg | only the AM20T, **turbocharged to its rating** (breaks R-5): $30.5k-31.8k, 129 kg | none |

The cost figures are R-35's definition: parts and services, with the radiator, exhaust and FADEC, but without the mount, labor or propeller. Each band is low / mid / high. Masses are R-37 installed dry.

**Why B at 100 hp.**
- **It is the only open option within reach of the AM15.** Its first engine is $10.7k / $17.5k / $28.6k unnormalized, against $14.7k-16.6k for an AM15 installed. Its mid is about $2k above the AM15's, and it is 3-29 kg heavier.
- **The cheapest version is a mix:** a used Suzuki core behind Aeromomentum's own gearbox, which Aeromomentum lists for $2,495 [S, re-checked on its parts page today], with the program's FADEC: $9.5k / $13.8k / $20.2k. That keeps the gearbox closed.
- **Concept H at 100 hp** (a flat-4 on H's module) costs about twice as much and is about 20 kg heavier than the AM15 as sold. **I recommend dropping it as the 100 hp member.**

**Why not B at 200 hp, even though it is the cheapest normalized 200 hp engine costed so far.**
- **Price and calendar.** Its low end, $18.3k, is the first figure in this program under R-35's $22k. That is only the low end, and the mid is $29.5k. It also reaches a first ground run in about 30-60 weeks, against H's 52-90.
- **Mass: it misses R-37 by 16-66 kg.**
- **R-25: it keeps one plug per cylinder.** One coil failure leaves about 81 % of MCP, against R-25's 90 %.
- **Supply: its core went out of production in 2019.**
- **Precedent: this is the same core family on which the last Subaru six conversion business failed.** Eggenfellner went bankrupt in 2009 after a series of gearbox generations that owners were asked to replace at their own expense [M6, M7, G47].
- **Its best use is the ground mule that HAYABUSA_PLATFORM role (d) already scored 7 of 10, if Bill takes H-EZ36 (AER-3411).**

**What "open" can mean for B, plainly.** The program can publish everything it adds:
- the gearbox, adapter and mount drawings;
- the FADEC hardware, firmware and calibration;
- the harness;
- the rebuild procedure and its measurement sheet;
- the installation data.

It cannot open the core's design, castings or supply: the builder buys a closed engine, new or used. It also cannot copy the factory service manual's text or figures. That is a real but bounded openness, and it is more than Aeromomentum offers only in the gearbox and the ECU. Aeromomentum already publishes its installation and internal-build manuals and sells every major part (section 6).

## 2. The three options

- **A, concept H.** The program's made-from-files engine: a flat-6 at 3,300 rpm, direct drive, LS7-class module, two plugs per cylinder (RANKING_PHASE1, CASTINGS_H, CRANK_H301). Here it is run through `scaling_sweep.py` at all three powers, so the family is on one model:
  - 100 hp: a flat-4 on the same module at 2,700 rpm (RANKING_PHASE1 section 5).
  - 300 hp: a second, larger flat-6 module, which is phase-2 work and not designed, so that column is **an extrapolation of the model**.
- **B, open conversion.** A production core, the program's gearbox (MANUFACTURING's AER-3633 build-up), the program's two-lane FADEC, open install documentation and a published rebuild sheet. The cores were chosen on four tests: port injection (the program FADEC has no direct-injection driver yet), aircraft BMEP below the car's own peak-torque BMEP, current or deep supply, and some aviation history. The pick per class:
  - **100 hp: Suzuki 1.5 L I4** (the K15B, in production since 2018; or the M15A or the Aeromomentum G15A). The K15B stays in the Suzuki Jimny, which mounts it **longitudinally** [S4]. A north-south bellhousing is the layout a propeller gearbox wants. Alternatives looked at and set aside: the Honda L15B is direct-injected and not supported by Haltech [G23]; the Toyota 1NZ and 2NR have no aviation history found [G30, G33]; the VW 1.4 TSI is direct-injected and turbocharged [G37].
  - **200 hp: Subaru EZ36 flat-6** (3.63 L, 2007-2019) [M1]. Alternatives set aside:
    - the FB25D is direct-injected [M10];
    - the K24 needs 7,000 rpm for 200 hp [M11];
    - the 2GR-FE is 163 kg bare [M21];
    - the 6G72 is old and was never flown in this form [M16];
    - the rotaries' last vendors are gone [M25, M30].
    - **The Mercedes M112 V6 (3.7 L) has two plugs per cylinder from the factory**, at about 160 kg [T5]. Section 7 covers it.
  - **300 hp: GM LS3 crate long block** (6.2 L, still sold new at $7.7k-9.7k) [L3]. Alternatives set aside:
    - the Coyote and the Gen V/VI V8s are direct-injected [L24, L21];
    - the 5.7 HEMI has two plugs per cylinder and is back in production for the 2026 Ram 1500, but it is iron-blocked and heavier still [T12, T15].
- **Baseline: buy an Aeromomentum** as sold. The AM13 (100 hp) or the AM15 (120 hp) at 100 hp. At 200 hp the line has only turbocharged engines: the AM15T at 160 hp and the AM20T at 260 hp [A5, A6].
- **B0, the bridge: an AM15 with the program's FADEC in place of its ECU.** This is the AER-3631 FADEC mule. It is in the tables because it is the cheapest way to get the open FADEC flying, not because it is a family member.

## 3. Cost (question 1)

`open_conversion.py` section 4. **Basis 1** is the program's first engine, carrying its NRE. **Basis 3** is a builder making one engine from the program's published files.

**MANUFACTURING's correction to how basis 3 is usually read (AER-3633).** Instant-quote CNC services price from the STEP with no visible NRE. A job shop that gets a STEP still writes its own toolpaths. So a builder's quantity-one price is close to the first engine's. Basis 3 drops sharply only for castings with proven, published gating and for gears whose drawing is settled.

| Member | Option | Basis 1 | Basis 3 | Basis 1, normalized |
|---|---|---|---|---|
| 100 hp | A, concept H (turbo included) | $26.8k / $40.9k / $62.4k | about $22.8k / $34.7k / $62.4k [E] | included |
| 100 hp | **B, used Suzuki core, program gearbox** | **$10.7k / $17.5k / $28.6k** | $9.8k / $16.1k / $26.4k | $12.7k / $20.5k / $33.1k |
| 100 hp | B, new Aeromomentum long block ($4,295 [S]), program gearbox | $12.9k / $18.9k / $27.6k | $12.0k / $17.5k / $25.4k | $14.9k / $21.9k / $32.1k |
| 100 hp | B, used Suzuki core, **Aeromomentum's gearbox** bought ($2,972 with plate [S]) | $9.5k / $13.8k / $20.2k | $9.5k / $13.8k / $20.0k | $11.5k / $16.8k / $24.7k |
| 100 hp | B0, AM15 with the program FADEC | $16.2k / $18.6k / $21.4k | same | $18.2k / $21.7k / $25.9k |
| 100 hp | Baseline AM13 | $13.2k-15.1k | same | $15.2k-19.6k |
| 100 hp | Baseline AM15 | $14.7k-16.6k | same | $16.7k-21.1k |
| 200 hp | A, concept H | $31.7k / $48.0k / $72.7k | about $27.0k / $40.8k / $72.7k [E] | included |
| 200 hp | **B, Subaru EZ36** | **$16.3k / $26.5k / $42.9k** | $15.0k / $24.5k / $39.9k | **$18.3k / $29.5k / $47.4k** |
| 200 hp | Baseline AM20T, turbocharged (breaks R-5) | $30.5k-31.8k | same | - |
| 300 hp | A, concept H, extrapolated | $34.0k / $51.1k / $76.9k | about $28.9k / $43.5k / $76.9k [E] | included |
| 300 hp | B, GM LS3 crate | $20.7k / $30.3k / $44.5k | $19.2k / $28.1k / $41.1k | $22.7k / $33.3k / $49.0k |

Engine mount, every option, builder TIG [MFG]: $1.4k-3.7k at 100 hp, $1.8k-4.5k at 200 hp, and $2.0k-5.0k at 300 hp.

**Where B's money goes** at 100 hp (basis 1):
- The gearbox ($3.3k-9.6k) and adapter ($1.1k-2.8k) are a third to two fifths of the bill.
- The core and its rebuild are only $2.1k-5.3k.
- **MANUFACTURING's finding is the key one: a program gearbox does not scale down with torque at quantity one.** Halving the torque saves about 20 %, because setup, heat-treat lots and grinding dominate. The 100 hp gearbox alone costs a quarter to three quarters of a complete AM15, whose own gearbox is rated to 225 hp [S, A2]. **That is the honest price of an open gearbox.**

**MANUFACTURING's unique-part lever, adopted as a proposal (AER-3633 section 1.3).** Design one gearbox for both the 100 hp and 200 hp cores: a fixed centre distance, the same case, bearings, slip clutch and output shaft, and a gear pair and adapter plate per core. A 22/55 pair gives 2.50:1 and a 25/52 pair gives 2.08:1 at module 3.
- **Cost:** about 10-25 % more gearbox and 2-4 kg on the 100 hp member.
- **Benefit:** it halves the design NRE and gives one build procedure and spares list.
- That is how Aeromomentum runs one 225 hp-rated gearbox across its line. It matters only if B is taken at both powers. With B at 100 hp only, as recommended, it does not apply.

**Concept H's basis 3 is a reading, not a build-up.** At 0.85-1.0 x basis 1 it follows MANUFACTURING's point above. H's basis 2 (five engines, NRE paid once) is $24.4k / $34.1k at 200 hp.

## 4. Installed mass and power (question 2)

**Power at the flange** (`open_conversion.py` section 1). Each core is asked for the family number at the flange through a 0.97 gearbox. The check is BMEP against the car's own peak-torque BMEP: the highest the core reaches anywhere on its car curve.

| Core | Takeoff | MCP | BMEP, takeoff / MCP | Piston speed, takeoff | Margin to the car's peak-torque BMEP |
|---|---|---|---|---|---|
| Suzuki K15B, 1.46 L | 100 hp at 5,800 rpm | 90 hp at 5,500 | 10.9 / 10.3 bar | 16.4 m/s | 8 % / 13 % |
| Subaru EZ36, 3.63 L | 200 hp at 5,000 | 180 hp at 4,700 | 10.2 / 9.7 bar | 15.2 m/s | 12 % / 16 % |
| GM LS3, 6.2 L | 300 hp at 4,400 | 270 hp at 4,100 | 10.1 / 9.8 bar | 13.5 m/s | 13 % / 16 % |
| Concept H (for scale) | 200 hp at 3,300 | 180 hp at 3,300 | 10.3 / 9.3 bar | 11.2 m/s | - |

- **All three cores make their member's rating at or below concept H's BMEP,** at a piston speed near the Aeromomentum and Viking class (about 16 m/s).
- **The K15B is the tightest.** 100 hp at the flange is the car's own peak power (77 kW). So the 100 hp member has no takeoff margin on that core, and the 1.5 L Suzuki is a 95-100 hp engine, not a 120 hp one.
- **Aeromomentum's own ratings, read the same way, are higher.**
  - The AM15's 120 hp at 5,800 rpm is **12.4 bar** if it is crank power.
  - The AM13's 100 hp is 11.9 bar.
  - Both sit above the Rotax 912's 11.2 bar.
  - The AM20T is 20.1 bar, a boosted figure.
  - Aeromomentum does not say whether its ratings are at the crank or at the flange, and it publishes no continuous rating. Its manual asks for cruise at 65 % or less [A9, A10].

**Installed dry mass** (R-37's definition; section 3 of the script; line items in the tables):

| Member | Option | Naturally aspirated | Normalized | R-37 (proposed) |
|---|---|---|---|---|
| 100 hp | A, concept H | - | 110-111 kg | 90 kg |
| 100 hp | B, Suzuki 1.5 L, program gearbox | 91-120 kg | 105-142 kg | 90 kg |
| 100 hp | B0, AM15 with the program FADEC | 91-97 kg | 105-119 kg | 90 kg |
| 100 hp | Baseline AM15 / AM13, with exhaust | 88-91 / 81-84 kg | 102-112 / 95-106 kg | 90 kg |
| 200 hp | A, concept H | - | 143-145 kg (sweep); 148-158 kg (phase 1b) | 150 kg |
| 200 hp | B, Subaru EZ36 | 152-194 kg | 166-216 kg | 150 kg |
| 200 hp | Baseline AM20T, turbocharged | 129 kg [S] | - | 150 kg |
| 300 hp | A, concept H, extrapolated | - | 174-177 kg | 210 kg |
| 300 hp | B, GM LS3 | 213-268 kg | 227-289 kg | 210 kg |

- **At 100 hp nothing normalized meets 90 kg, not even the AM13.** R-37's 100 hp line was proposed against unnormalized engines (Rotax 912, UL260iS). On a like-for-like normalized basis the AM15 is 102-112 kg, and B is 105-142 kg.
- **The weakest numbers are B's core masses.**
  - No OEM figure was found for the EZ36. The 125-145 kg band is anchored on Eggenfellner's 159 kg EZ30 package, which included its gearbox [M5].
  - The LS3's 175-197 kg comes from conflicting forum figures [L5].
  - The Suzuki's 72-85 kg is AM15's 83.9 kg less its gearbox, against a secondary 85 kg for the K15B [G14].
  - Weighing one core settles each.
- **Cross-check at 300 hp:** Auto PSRU's LS3 firewall-forward package is 570-590 lb wet, 259-268 kg [L7]. B's 227-289 kg normalized dry brackets it.

## 5. Time and effort to a first ground run and a first flight (question 3)

`open_conversion.py` section 5: weeks from a go decision, as the longest chain through each option's task list. Every duration is [E] unless tagged. **The airframe is assumed ready when the engine is; it is not (MAOS is paused), and that holds for every option.**

| Option | First ground run | First flight | What sets the first run | Builder hours to a ready engine |
|---|---|---|---|---|
| A, concept H, 200 hp | 52-90 weeks | 76-136 weeks | the crank: finish the design, an RFQ path (AER-3330, open since 2026-10-16), then 18-20 weeks of lead [S] | 300-630 |
| B, Suzuki, 100 hp | 30-60 weeks | 50-100 weeks | the two-lane FADEC (26-52 weeks), shared with A | 195-410 |
| B, EZ36, 200 hp | 30-60 weeks | 50-100 weeks | the FADEC; the gearbox is 16-34 weeks beside it | 240-475 |
| B0, AM15 with the program FADEC (AER-3631) | 28-56 weeks | 42-84 weeks | the FADEC | - |
| Baseline, AM15 as sold | 5-14 weeks | 13-30 weeks | delivery (no lead time published; Aeromomentum quotes about 8 weeks for the AM15T [S, A5]) | 40-160 |

- **B's calendar is set by the FADEC, which every option except the baseline needs.** With the FADEC taken out of the race, B runs as soon as its gearbox is designed and made (12-24 weeks at 100 hp) and H as soon as its crank is (46-78 weeks, then assembly).
- **The baseline flies soonest, and teaches the program nothing it owns.**
- **The airframe is the real long pole for every flying option.** No option above has one.

## 6. Openness (question 4)

What a builder can inspect, repair, modify and rebuild from published material:

| | A, concept H | B, open conversion | B0, AM15 + program FADEC | Baseline, Aeromomentum |
|---|---|---|---|---|
| Engine design: castings, crank, geometry | **open**: the program's STEP and drawings | **closed**: the car maker's. The program can publish measurements, limits and procedures it writes itself, not the factory manual's text or figures (US copyright excludes procedures and methods [P44]) | closed | closed; Aeromomentum publishes an internal build manual [A8] |
| Parts supply for the engine | catalog parts (pistons, rods, liners, bearings, valves), multi-source | OEM and aftermarket car parts, multi-source while the car is supported | Aeromomentum sells long block, short block, head, crank, block [A12] | the same |
| Rebuild | to the program's sheet | **to the program's measurement sheet** (MANUFACTURING proposes it as the core open deliverable) | Aeromomentum's manual | Aeromomentum's manual |
| Gearbox | direct drive (none) | **open drawings**, catalog bearings, couplings and clutch | closed; Aeromomentum sells the box and its parts [A12] | closed design, parts sold |
| ECU hardware and firmware | **open**, the program FADEC | **open** | **open** | a single MicroSquirt ECU, which the manual calls an "open source port fuel injection system" [A9]; Kitplanes 2025 says Bosch [K2]. The calibration is Aeromomentum's |
| Installation design and data | open | open | open | manuals public as PDFs [A8]; the design data behind them not published |
| What stays proprietary | nothing designed by the program; catalog parts are bought | the core: castings, metallurgy, the maker's supply decisions | the core and the gearbox | the gearbox design, the calibration, core sourcing |

**What "open" cannot mean for B.**
- A builder cannot make the core, and cannot rely on a given core existing in ten years (section 8).
- A program cannot certify that a used core is good. It can only publish the inspection that finds out, which is why MANUFACTURING recommends a mandatory rebuild to the sheet ($1.5k-7.2k).
- **The open ECU firmware cannot be a rusEFI fork as licensed today.** rusEFI is GPLv3 with added terms, one of which is "rusEFI is not approved for manned aircraft applications" [P34]. Its fork FOME carries the same file [P38]. Speeduino (GPL-2.0, hardware CERN-OHL-S) carries no such term [P39]. That bears on the FADEC work in AER-3631, and it needs a licence read, not my reading.
- **No open aircraft reduction drive was found anywhere** [P22, P24]. The program's gearbox would be the first, which is a contribution and also means no field record to borrow.

**Precedent for "open-ish" on a dead core: the Corvair.** The car was built 1960-1969 [O5]. About 500 aircraft were flying by 2014 [O3]. The conversion is taught at hands-on Colleges where builders assemble and run their own engines [O3]. It survives on documentation, aftermarket cranks and a shrinking pool of good cases ("GM's not making any more of these" [O6]). It also had to learn, by in-flight crank failures, to add a fifth bearing at the propeller end [O5, O8]. That is what B would look like after 50 years, documentation included. The manual is sold, not open [O2].

## 7. Requirements fit (question 5)

| Requirement | A, concept H | B, open conversion | Baseline, Aeromomentum |
|---|---|---|---|
| **R-25** two lanes, any single failure leaves 90 % of MCP | **meets by design** (two plugs per cylinder) | **reduced-redundancy exception** on any single-plug core: ECUs, crank sensors, power feeds and injector drivers can be dual; the plug and its coil cannot. One cylinder dead leaves **71 % of MCP (Suzuki I4), 81 % (EZ36 flat-6), 85 % (LS3 V8)** (section 2 of the script) | **fails**: one ECU, one plug per cylinder [A9, A10]; 71 % after a cylinder |
| R-25 with a twin-plug core | - | possible at 200 hp on a **Mercedes M112** (twin plug, out of production, about 160 kg [T1, T5]; the stock coil feeds both plugs of a cylinder, so lane separation needs a coil change, unverified [T7, T8]), and at 300 hp on the **5.7 HEMI** (twin plug, in production for the 2026 Ram, iron block, heavier than the LS3 [T10, T12, T15]) | - |
| **R-37** installed dry 90 / 150 / 210 kg | 100 hp misses (110-111 kg); **200 hp meets (143-158 kg)**; 300 hp meets on an extrapolation | misses at every power, normalized: 105-142 / 166-216 / 227-289 kg | 100 hp misses once normalized (AM15 102-112 kg); unnormalized the AM13 is 81-84 kg |
| **R-40** 2,000 h TBO | zero hours; R-41's provisional interval and teardowns apply | zero aviation hours on these cores in this duty. Aeromomentum claims 2,000 h on its Suzuki cores [S, A2 A3], a vendor claim with no published fleet hours | vendor claim of 2,000 h (AM13, AM15), 1,500 h (turbos), 1,800 h (AM20T) [A2-A6]; warranty void on "extended high power use" [A11] |
| R-5, R-7 normalized to 12,000 ft | carried (turbo in the costs) | add the program's normalizer: +$2.0k-4.5k, +14-21.5 kg | **fails**: the AM13/AM15 are unnormalized, and the 150-300 hp models are boosted to their ratings |
| R-12, R-15 91 AKI on MON 85, E0-E15 | designed for it (CR 8.4) | the car cores run on regular; E15 needs the program's fuel parts. EPA's E15 approval covers 2001+ US road vehicles; the K15B was never sold in the US | 90 AKI, 93 AKI for high power; **up to E10** [A9]: E15 outside the vendor's approval |
| **R-1** family on common parts | meets at 100 and 200 hp on one module; 300 hp needs the second module | **breaks**: three cores share nothing but the FADEC, the gearbox approach and the documentation | not a family in R-1's sense |
| **R-28** made from files | meets | **read literally, meets**: a car engine is "bought off the shelf". It breaks the premise behind R-28 (a builder makes the engine, as on the E-225) and leaves R-29 to R-31 with nothing to govern | meets literally; nothing is made |
| R-32 assembly and maintenance, fewer parts | a new engine to learn | a car engine with car parts, plus a gearbox | the simplest for the builder |
| R-33 a cylinder module replaced in 4 h | designed for it | no: car heads, head gaskets, timing chains | no |
| R-35 $15k / $22k / $30k | misses at every power | **100 hp:** misses at the mid. **200 hp:** the low end ($18.3k normalized) is under $22k for the first time; the mid ($29.5k) is not. **300 hp:** low end under $30k, mid over | AM15 meets $15k only unnormalized |

**So B needs, at minimum, an R-25 exception (or a twin-plug core), an R-37 relaxation, and an explicit reading of R-1 and R-28.** R-28 is not the obvious break. Read as written, a bought core satisfies it. **R-1 and R-25 are what B actually breaks.**

## 8. Supply risk (question 6)

| Core | Status 2026 | New supply | Used supply | When it ends |
|---|---|---|---|---|
| Suzuki G13BB / G15A (Aeromomentum's) | **out of production**: the last G13BB civil vehicle ended March 2019, with an army re-run after [S1, S2]; no G15A end date found | Aeromomentum sells "new" long blocks at $3,295 / $4,295 [A12] and says it never uses used parts [A2]; where those blocks come from is not published | thin in the US | Aeromomentum must move its line to another core, and its product changes under its customers |
| Suzuki K15B | **in production** (Jimny, Ertiga, Brezza; India, Japan, Africa, Indonesia) [G13, S4]; India moved most models to the direct-injected K15C | not sold as a crate engine in the US; import | **thin in the US**: Suzuki left the US car market in 2012, and the Jimny was never sold there [E] | the K15C is direct-injected; the program FADEC would need a DI driver |
| Suzuki M15A | out of production; last application to 2022 [W2] | none found | thin in the US | - |
| Subaru EZ36 | **out of production since 2019** [M1] | no new long block found | deep: Outback and Legacy 2010-2019 sold in volume [E]; $1.5k-4.6k delivered [MFG] | the used pool shrinks over decades; the split aluminum case cannot be repaired if a main bore is damaged [MFG] |
| GM LS3 | out of vehicles since 2017, **still sold new as a crate engine** [L3, L4] | yes, $7.7k-9.7k | deep | GM's successors are direct-injected (Gen V, and Gen VI from 2027) [L21] |
| Concept H's catalog parts (LS7-class pistons and rods, Darton liners, valves, bearings) | aftermarket, multi-source | yes | - | a single catalog part can be superseded; the files let the program redraw around a replacement |

**The vendor is a supply risk of its own.** The automotive-conversion vendors this program has met have mostly stopped:
- Eggenfellner went bankrupt in 2009 [M6];
- Stratus closed about 2008 [G43];
- Raven closed in 2017 [G6];
- EPI stopped all manufacturing in 2018 [P8];
- NSI and Maxwell folded [G47];
- Mistral was liquidated [M25].

**A closed product dies with its maker; an open one does not.** The Corvair is still flown 57 years after its core ended, on documentation [O5]. That is the strongest argument for B over the baseline. It does not depend on B being cheaper.

**New against used.** Every B core except the LS3 is used in practice. MANUFACTURING's line makes the rebuild part of the price, not an option ($1.5k-3.8k for the Suzuki, $3.2k-7.2k for the EZ36). The program's deliverable is the measurement sheet that turns a used core into a documented zero-time baseline.

**Model-year churn** is the slow risk. The industry is moving to direct injection: Suzuki K15C, Honda L15B, Subaru FB25D, GM Gen V and Gen VI, Ford Coyote Gen 3 and later. **The program FADEC needs a direct-injection driver within one model generation, or B is confined to dying port-injected cores.** That is a FADEC requirement B creates and A does not (A is port-injected by design).

## 9. Which of 100 / 200 / 300 hp each covers (question 7)

| | 100 hp | 200 hp | 300 hp |
|---|---|---|---|
| **A, concept H** | **feasible, uncompetitive**: costs twice an AM15 and is 20 kg over R-37 | **the design point; the only option meeting R-25 and R-37** | only with the second module, not designed |
| **B, open conversion** | **yes**: the best open route. Suzuki 1.5 L, near the AM15's price, heavier, with an R-25 exception | **possible**: EZ36, the cheapest normalized 200 hp found, but heavy, single-plug and out of production. Better as H-EZ36's ground mule | **possible on paper**: LS3, misses R-37 by 17-79 kg; EPI quit LS conversions over crank stiffness at continuous load [L22] |
| **Baseline, Aeromomentum** | **yes**, the market answer (AM13 / AM15), unnormalized, single lane | only boosted (AM20T, breaks R-5) | none normalized |

## 10. Failure ledger

Added to `FAILURE_LEDGER.md`, each conditional on a B route being taken. FL-61 to FL-69 are left for AER-3631, running in parallel.
- **FL-70:** a single-plug cylinder on any converted core: one coil or plug lost.
- **FL-71:** a used core's unknown history.
- **FL-72:** reduction-drive input spline and drive-flange fatigue on a conversion: Eggenfellner, the Viking 110 and the Glasair LS1 cases.
- **FL-73:** gearbox bearing-retainer screws backing out under vibration (Aeromomentum's own 2019 bulletin).
- **FL-74:** a fuel-rail bracket cracking on a vibrating car engine (AM15, 2022).
- **FL-75:** a car wet sump in aircraft attitudes on any converted core.

## 11. What this pass did not do

- **No core was weighed.** The EZ36 mass has no OEM figure, and the LS3 figures conflict. Weighing one core of each settles them.
- **No quotes.** Every cost is [E] or [MFG]. Aeromomentum's prices are list prices read today, not quotes.
- **It is not known whether Aeromomentum sells its gearbox for engines other than its own.** The parts page lists it [A12]. MANUFACTURING and the drives research both read it as sold only with their engines [MFG, P16]. One email settles it.
- **Not checked:** the Aeromomentum gearbox's fit to a K15B or M15A bellhousing, and the EZ36's manual flywheel and bellhousing pattern (MANUFACTURING flags it: most US EZ36 cars were automatics).
- **The calendar is a task list with [E] durations,** not a plan. The FADEC's 26-52 weeks is the number that sets three of the five rows, and it is AER-3631's to firm up.
- **No torsional model of any B drive.** HAYABUSA_PLATFORM's two-inertia method applies to an I4 and would be the first step on a B-100 drive. EPI's warnings on drive resonance apply [L35].
- **R-40 has no evidence for any option.** Aeromomentum's 2,000 h is a vendor claim. The auto-conversion accident base rates are [O24-O27]:
  - auto conversions were 15 % of the 2011 amateur-built accident fleet and 23 % of its powerplant failures (NTSB SS-12/01);
  - about 0.08 % per year failed, against 0.03 % for Lycoming and Continental (Wanttaja 2023).
  - These are the rates a B engine starts from, and H's starting point is worse: a new design with no fleet.
- **The licence question on rusEFI's aircraft term** was not read by anyone qualified.
- **The Mercedes M112 and 5.7 HEMI twin-plug routes are noted, not costed.**

## 12. Bill's call

**Make the 100 hp member an open conversion, and keep concept H for 200 hp?** I recommend yes, for three reasons:
- At 100 hp an open Suzuki conversion comes within about $2k of an AM15 at the mid, while concept H costs twice as much.
- At 200 hp nobody sells a normalized engine, and H is the only option that meets both two-lane ignition and the mass target.
- The FADEC work on the bought AM15 (AER-3631) is the first step for both.

If Bill says no, H stays the family at all three powers, and the 100 hp member stays a $27k-62k derivative. The question is on AER-3632 as a card.
