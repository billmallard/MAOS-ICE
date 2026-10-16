# Engine manufacturing envelope, v0

Owner: MANUFACTURING. Issue: AER-3321 (parent AER-3320). Program: ORG-009, 2026-10-16.
For PROPULSION to commit as `MAOS-ICE/docs/engine/MANUFACTURING_ENVELOPE.md`.
Status: v0. Published so the six concepts are written inside it. Nothing here is a quote on real geometry yet, because there is no geometry yet.

## How to read the numbers

Every number has a tag.

- **[S]**: sourced. The source is in the Sources list at the end. All sources were read on 2026-10-16. Where the page shows its own date, that date is given too. A retail price read off a shop page is a price on that day. It is not a contract.
- **[E]**: my engineering estimate. The method is named beside it. Treat it as a target with my name on it, not as a fact.
- **[Q]**: needs a real quote on real geometry. MANUFACTURING runs the quote once PROPULSION has an envelope sketch for the part.

Skill floors used throughout:

- **B0**: orders from files and assembles with hand tools and a torque wrench.
- **B1**: B0 plus careful measuring (micrometer, bore gauge, Plastigage, dial indicator) and hand-tool fitting (lapping valves, hand seat cutters, reaming).
- **B2**: B1 plus their own foundry, furnace or kiln work.
- **Shop**: a local automotive machine shop or a job shop. Named and priced wherever it appears.

## The four findings that should shape the concepts

1. **The online CNC services machine their own billet. They do not machine your casting.** SendCutSend's CNC service is 6061-T6 only, with a maximum part of 7 x 7 x 12 in [S]. Protolabs' 3-axis aluminum envelope is 22 x 14 x 3.75 in, with at most 2 in of milling depth per side [S]. Both are stock-material services. A crankcase or head casting needs a **job shop** that fixtures a rough casting to datums. That shop is local, priced by RFQ, and is the one step that is not "upload and wait" [Q]. Design consequence: either (a) accept one job-shop step per cast part and make it as cheap as possible (few datum faces, every critical bore set up together), or (b) make the part from billet or plate, which an online service *can* do [Q].
2. **Put the precision on catalog parts, not on castings.** A bought wet or dry liner carries the bore finish. Bought bearing shells carry the journal clearance. Bought seat inserts and guides carry the valve sealing. The casting then only has to hold the *housings* for those parts. Housing tolerance is roughly 0.01 to 0.02 mm class, and any machine shop does it. The casting never needs a honed running surface [E, standard practice in Darton-sleeved and Nikasil-liner engines].
3. **Hobbyist casting does not make a pressure-holding crankcase or cylinder head.** Section 1.1 gives the reasons. Hobbyist casting is real and useful for non-pressure parts and for prototypes. Any concept whose make/cast/machine/buy split says "builder casts the crankcase" or "builder casts the head" is outside this envelope.
4. **Choose bore, stroke, rod length and valve size from what the catalog already sells.** Pistons, rings, rods, valves, springs and gaskets are cheap when they exist and expensive or unobtainable when they do not (Section 4). PROPULSION should treat "a catalog piston, ring set and liner exist at this bore" as a constraint on bore, alongside BMEP and piston speed.

## 1. Aluminum sand casting

| | 1.1 Hobbyist (printed pattern or lost-PLA, backyard furnace) | 1.2 Binder-jet printed mold + foundry pour | 1.3 Conventional foundry pours the builder's printed pattern |
|---|---|---|---|
| Who | the builder (B2) | print bureau (Hoosier Pattern, Humtown, the ExOne network) [S], then a foundry pours | no-bake or green-sand jobbing foundry |
| Pattern / tooling | PLA or PETG pattern with draft and shrink; or lost-PLA in plaster-sand investment [S] | none: mold and cores are printed straight from CAD [S] | builder prints the pattern and core boxes (1-2 deg draft, about 1.3% Al shrink [E, standard A356 pattern allowance]) |
| Alloy actually poured | scrap, typically wheels (A356-type) [S]; chemistry unknown and unverified | foundry ingot to spec: A356 or A357 | foundry ingot to spec: A356 or A357 |
| Melt quality control | flux at best; no rotary degassing, no filtration, no density or reduced-pressure test [E] | degassed and filtered; sample bar on request [E] | same as 1.2 |
| Gas and shrink porosity | high and variable; hydrogen pickup from long exposure and superheat is the usual failure [S] | low to moderate; feeding and chills are designed into the printed mold | low to moderate; depends on the foundry's gating design for your pattern |
| Minimum wall | 4-5 mm green sand; about 3 mm plaster/lost-PLA on small parts [E, hobby practice] | about 3-4 mm [E, published sand-print practice] | about 4-5 mm no-bake [E] |
| Cored coolant and oil passages | sodium-silicate/CO2 cores rammed in printed core boxes are possible; locating, venting and removing them is hard [E] | **its strength**: cores print with the mold, so coolant jackets that are impossible conventionally become routine (race heads are made this way) [S] | printed core boxes; the foundry makes and sets the cores [E] |
| As-cast tolerance and finish | +/-1-2 mm, rough [E] | about +/-0.5-1 mm over 300 mm, Ra about 12-25 um [E] | about +/-0.8-1.5 mm [E] |
| T6 | home kiln solution (about 540 C) plus water quench plus about 155 C age is possible but unverified; quench delay and +/-5 C uniformity decide the result [E] | a commercial heat treater, priced by batch or by lb-hour [S, structure only] | same as 1.2 |
| Pressure-tightness | impregnation seals micro-porosity [S]; it does **not** fix shrink cavities or cold shuts | X-ray or a pressure test, then impregnation as standard practice [E] | same as 1.2 |
| Price basis | about the cost of propane, sand and scrap: tens of dollars per pour [E] | **$0.13 per in^3 of printed sand** (Hoosier Pattern, as reported) [S]; plus pour, T6, impregnation [Q] | pattern is builder-printed (about $50-300 of filament [E]); foundry one-off setup plus per-lb [Q, nothing published] |
| Worked example | n/a | crankcase half about 400 x 250 x 150 mm in a shelled mold of about 1,200-2,000 in^3: **about $160-260 of printed sand** [E from the [S] rate], so roughly **$1,000-2,500 first article** poured, T6 and impregnated [E, to be replaced by [Q]] | [Q] |
| Lead time | weekend per attempt, many attempts | print 3-5 days [S]; pour plus HT plus impregnation 2-4 weeks [E] | 2-6 weeks [E] |
| Skill floor | B2 | B0 (sends files, receives a casting) | B0 plus a careful pattern print and finish |

### 1.1 The blunt answer: can a hobbyist cast a crankcase or head that holds oil and coolant pressure?

**No. Not as a flight part.** Four reasons, each independent of the others:

1. **No porosity control and no inspection.** Without degassing and a density or X-ray check, the builder cannot know whether a given casting has gas or shrink porosity behind a machined oil gallery or bearing web. Impregnation seals leaks [S]. It does not restore strength lost to a shrink cavity.
2. **Unknown alloy.** Wheel scrap is A356-type, but nobody has measured that melt. The property basis (ASTM B26 A356-T6 minimums, about 30 ksi UTS, 20 ksi yield, 3% elongation [E, from the standard as recalled; verify against B26]) does not apply to an unverified melt.
3. **Unverified T6.** Solution temperature uniformity and quench delay decide whether you have T6 or something softer. A builder has no hardness tester and no tensile bar to check.
4. **Cores.** A head's coolant jacket around the chamber and seats is the hardest core in the engine. In printed sand (1.2) it is routine. In a backyard it is the place a core shifts or a vent fails and leaves a thin wall next to a combustion chamber.

The Hackaday-covered lost-PLA cylinder (2026-08-28) produced a usable casting "with only a few imperfections". The article says nothing about pressure-tightness or running [S]. That is the honest state of the art.

**What hobbyist casting is good for:** non-pressurized covers (valve, timing, accessory), intake plenum, thermostat and coolant necks, brackets, and **fit-check prototypes** of the crankcase and head before paying for 1.2 or 1.3. That is a real saving, because a wrong first article from a bureau costs about a thousand dollars and weeks [E].

**What would move the line** (PROPULSION's lever, not mine to decide): a design with **no pressurized oil gallery cast into the case**, using external or drilled-and-plugged steel lines, and a dry-sump scavenge-only case. That lowers the case to "structural, oil-wetted, not pressurized". It is still structural fatigue on an unverified casting, so it is still 1.2/1.3 for flight. It does make an inspected hobby casting a plausible ground-test article.

### 1.2 / 1.3 Recommendation for the engine's structural castings

Crankcase, block or cylinder module, and head: **binder-jet bureau + foundry (1.2) for first articles and any part with coolant cores. Conventional foundry with a printed pattern (1.3) for open-faced, simple-cored parts once the design is stable.** Specify A356-T6 (or A357-T6 where fatigue margin is thin), degassed, X-rayed or pressure-tested, and impregnated. Leave 1.5-3 mm machining stock on every machined face [E].

Design rules PROPULSION should design to now:

- Split the crankcase at the crank centerline so both halves pour open-faced, with no core for the crank bay.
- Uniform walls of 4-6 mm, with radiused junctions and no isolated heavy bosses (Campbell's feeding rules).
- Bring coolant and oil passages to an open face wherever possible so cores are supported and can be removed.
- Every precision bore is a housing for a bought part (Finding 2).

## 2. Machining

### 2.1 What each kind of shop actually does

| Operation | Online CNC service (SendCutSend, Protolabs, Xometry) | Local automotive machine shop | Builder with a fixture |
|---|---|---|---|
| Billet or plate parts within envelope (brackets, covers, pump bodies, caps, flanges) | **yes**: SendCutSend 6061 up to 7x7x12 in, +/-0.005 in, 2-5 days [S]; Protolabs Al up to 22x14x3.75 in 3-axis, +/-0.005 in [S]; Xometry quotes larger parts and ISO 2768-f/m and ISO 286 grades [S] | yes | no |
| First-op machining of a rough casting (datums, decks, faces, bolt holes) | **no** through the instant-quote path (stock-material services) [S]; Xometry custom RFQ possible [Q] | job shop, not an engine shop [Q] | no |
| Line-bore or align-hone mains and cam bores | no | **yes**: align hone $75-150, align bore up to about $410 [S] | no (needs a boring bar or hone) |
| Cylinder bore and hone (iron liner) | no | **yes**: bore $15-60 per cyl, hone $10-20 per cyl [S] | deglaze only (ball hone); cannot size a bore |
| Deck flatness | yes on billet; on a casting, see first-op | **yes**: $125-285 [S] | check only (straightedge and feelers) |
| Valve seats and guides | no | **yes**: seat/guide install plus valve job; valve job from about $20 each on small engines, $375-490 per head with porting [S] | **lap valves: yes (B1). Cut seats with hand carbide cutters: yes (B1)** [E]. Ream new guides: yes (B1) [E] |
| Crank journals (grind, polish) | no | **yes**: $85-200 [S] | measure only |
| Balance the rotating assembly | no | **yes**: $300-400 [S] | weigh-match pistons and rods on a scale: yes (B1) |
| Cam journals and lobes | no | cam grinder (specialist) [Q] | no |

Machine-shop rates above come from a published US shop price guide and forum price reports [S]. They are 2020s-era retail and vary by region; plan +30% for 2026 [E].

### 2.2 What this means for the build-cost ledger

Per engine, the machine-shop bill for a cast case-and-head engine is about **$800-2,000** [E, from the [S] line items: align hone, deck x2, bore/hone x4-6, valve work, balance]. On top of that is **first-op job-shop machining of each casting** [Q, the largest unknown on the ledger; likely several hundred to a few thousand dollars per casting for one-offs]. Repeat engines get cheaper only if the builder group or AeroCommons owns a **shared fixture set** that travels between shops. That is a document-and-fixture deliverable this program can supply [E].

## 3. Cutting, sheet and additive

| Route | Use on this engine | What it holds | Price basis | Skill floor |
|---|---|---|---|---|
| Laser / waterjet (SendCutSend, OSH Cut) | baffles, brackets, mounting plates, exhaust and intake flanges, oil-pan sides, gasket blanks (fiber sheet via waterjet), cooling ducts | +/-0.005 in cutting tolerance class [S, SCS]; minimum feature scales with thickness; bending only in the alloys on the bendable list | priced by bounding box, pierce count and job quantity [S, see MANUFACTURING tradecraft note] | B0 |
| Service bending | oil pan, shrouds, brackets that replace a fastened pair | flange, relief and radius rules per alloy; 5052 and steel bend, high-strength tempers do not at tight radii | as above | B0 |
| Sheet + weld (TIG) | fabricated oil sump, coolant manifold, exhaust | welder-dependent | materials plus a welder's time [Q] | builder TIG or a local welding shop |
| Metal AM: AlSi10Mg (SLM/DMLS) via Craftcloud, JLC3DP, Sculpteo [S] | where it earns its price: **small, complex, internally-ported, low-load parts**, such as coolant crossover and thermostat housings with internal passages, oil-jet manifolds, sensor bosses, a one-piece intake runner pack | dense, about 0.1-0.2 mm accuracy as built; needs stress relief and machining on sealing faces [E] | JLC3DP 316L was $0.21/g (Aug 2025) [S]; AlSi10Mg pricing changed July 2026 and needs a live quote [S, Q] | B0 |
| Metal AM: steel or Inconel | turbo manifold or collector, if normalizing by turbo | expensive per kg; fatigue at weld-free joints is good | [Q] | B0 |
| Polymer: SLS/MJF PA12, PA-CF | intake plenum and runners (check temperature), ducting, connector housings, fit-check prototypes of everything | about +/-0.3 mm [E] | cheap, tens of dollars per part [E] | B0 |

Where metal printing does **not** earn its price: crankcase, head, rods, crank. These are too big (the price scales with volume), fatigue-critical (porosity and surface finish), or both. Revisit only if a part count collapses by printing (for example, a whole accessory case that replaces 10+ parts) [E].

## 4. Buy from catalogs

Design rule: the dimension set (bore, compression height, pin diameter, rod length, big-end width, valve stem diameter and length, spring installed height, head-gasket bore) should **pick an existing catalog family**. A custom version of any of these turns a $50-300 part into a lead-time and a minimum order.

| Part | Buy | Representative price (2026-10-16) | Note |
|---|---|---|---|
| Pistons | forged, from a performance catalog (Wiseco, JE) or OE cast | Wiseco forged: about **$155-280 each** [S] | custom bore or compression height: [Q] for Wiseco/JE custom programs |
| Rings | ring set matched to piston | included in many piston kits [S] | |
| Rods | H-beam forged steel (Eagle, Manley) | Eagle set of 4: **$400-417**; Manley set of 4: **$525-544**; Manley single **$153** [S] | rod length and big-end width chosen from catalog |
| Main and rod bearings | Clevite/MAHLE, King, ACL shells | main set **$58-147** depending on application [S] | journal diameters chosen from a catalog shell |
| Liners | ductile-iron dry sleeves (Darton) or plated wet liners | Darton set **about $600, install $1,000-1,500** at a shop [S] | a wet liner with a finished bore removes the bore/hone step entirely; [Q] for a catalog wet liner at the chosen bore |
| Bore re-plating (if Nikasil liners) | US Chrome, Millennium Technologies | **about $200 per cyl**; LN Engineering $409-449 per cyl reconditioning [S] | |
| Valves | stainless, motorcycle or auto catalog (Ferrea etc.) | **$35-53 each** [S] | choose head diameter, stem and length from catalog |
| Springs, retainers, keepers, seats, guides | catalog | [Q] | |
| Head gasket | MLS (Cometic) | **$85-236** [S] for catalog bores; custom needs tooling [S] | choose bore and bolt pattern to match a catalog gasket, or plan O-ring + liner-flange seal |
| Injectors | Bosch EV14 | **$72-89 each** [S] | |
| Coils | GM D585 coil-near-plug | **$48-51 each** [S] | dual-lane: two per cylinder or a dual-output coil, a PROPULSION/FADEC choice |
| Coolant pump | electric, Davies Craig EWP115 | **$225** [S] | deletes a belt and pump drive (part-count win); failure mode goes on the ledger |
| Oil pump | gerotor from a donor engine or dry-sump section | [Q] | |
| Sensors (MAP, IAT, CLT, oil P/T, crank/cam) | automotive | [Q] (typically tens of dollars each [E]) | |
| Fasteners | ARP head and main studs; metric catalog bolts | [Q] | specify catalog stud lengths |
| Seals, O-rings, gaskets | catalog sizes only | [E] small | every groove sized to an AS568 or ISO 3601 O-ring |

**Catalog parts per cylinder, as a sanity check:** piston + rings + rod + 2 rod-bearing shells + 2-4 valves + springs + 1 injector + 1-2 coils comes to **about $450-750 per cylinder** at the prices above [E, sum of [S] rows]. At four cylinders that is $1,800-3,000 before liners, bearings, gaskets, pumps and sensors.

## 5. Finishing and treatment

| Treatment | Who, for one-off quantities | Price basis | Note |
|---|---|---|---|
| T6 heat treat of castings | commercial heat treater, or the foundry's own furnace | batch minimum, or cents per lb-hour [S, structure]; [Q] for the lot minimum | ask the foundry to deliver T6; it removes a shipping leg |
| Vacuum impregnation | Godfrey & Wing, Sharretts and peers [S] | production cost is about $2 for a 10 kg casting [S]; one-off lot minimum [Q] | do it after machining; seals micro-porosity only |
| Nikasil/NSC bore plating | US Chrome, Millennium, LN Engineering [S] | $200-449 per cyl [S] | only if the liner is aluminum |
| Anodizing | SendCutSend (type II on its own parts) [S]; local anodizer for others | [Q] | high-silicon castings (A356) anodize grey and uneven; anodize billet parts, not castings [E] |
| Piston crown / skirt coatings | offered by piston makers at order | [Q] | |
| Thermal barrier / exhaust coating | local coater | [Q] | |

## 6. The parts most likely to break "made from files", and the cheapest honest path for each

| Part | Why it breaks the premise | Cheapest honest path |
|---|---|---|
| **Crankshaft** | Forged or billet steel, nitrided, ground, balanced. None of the file routes does it. | (a) **Reuse an OE automotive or motorcycle crank** and design the bottom end around it. Cheapest, but it locks bore spacing, stroke and journal sizes, and an OE crank was never designed for prop gyroscopic and thrust loads, so it pushes toward a PSRU (PROPULSION's call). (b) **Custom billet 4340 from Crower, Bryant or Moldex: about $3,400-6,300, 3-4 months** [S]. Then a machine shop balances it ($300-400 [S]). (c) Nothing cheaper is honest. |
| **Cylinder head** | Coolant cores around chamber and seats; seat and guide work. | Binder-jet bureau + foundry, A356/A357-T6, impregnated (1.2), then job-shop first-op and machine-shop seats and guides. Or **reuse a catalog head** from a donor engine, if PROPULSION's concept allows it. Builder can lap and hand-cut seats (B1). |
| **Crankcase / block** | Line-bore and first-op machining of a casting. | Split at the crank centerline; 1.2 or 1.3 casting; one job-shop setup that machines all mains together; machine-shop align hone. Alternative for low volumes: **machined from plate by an online service** [Q]. That removes casting risk and is likely to cost more per unit. |
| **Camshaft** | Lobe grinding is a specialist trade. | Donor-engine cam, or a regrind or custom billet from a cam grinder [Q]. Belt or chain drive with catalog sprockets avoids cutting gears. |
| **Gears (PSRU, cam drive, accessory)** | Gear cutting and hardening are not file services. | Catalog gears (KHK, Boston Gear) or a donor gearset; belt or chain drives where torque allows [Q]. |
| **Custom pistons** (only if bore or compression height is off-catalog) | Forging dies. | Pick the bore from the catalog (Finding 4); custom programs exist at [Q] cost and lead time. |

## 7. Build-quality risks for the failure-mode ledger (SAFETY is paused; PROPULSION holds the ledger)

1. Casting porosity behind an oil gallery or bearing web leads to oil loss or web cracking. Mitigation: route 1.2/1.3 only, X-ray or pressure test, impregnation, no pressurized cast galleries where avoidable.
2. Unverified T6 leads to low fatigue strength in the case or head. Mitigation: a heat treater with a certificate; hardness check on a coupon.
3. Main-bore misalignment across case halves leads to bearing distress. Mitigation: halves machined together; align hone; Plastigage at assembly.
4. Liner fit (dry-sleeve interference, wet-liner protrusion) leads to a head-gasket leak or coolant in the oil. Mitigation: a protrusion spec plus a builder measurement step (B1).
5. Builder-cut valve seats with a wrong width or concentricity lead to a burnt valve. Mitigation: a seat-width spec, a vacuum or leak-down test as a builder check.

## 8. Open items and what I could not prove

- **No quotes on real geometry.** There is no geometry yet. Every [Q] stays open until PROPULSION gives a part envelope. The first quotes I will run, in order: (1) first-op job-shop machining of a crankcase half, (2) bureau-printed mold + pour + T6 + impregnation of a crankcase half, (3) the same for a head, (4) billet crankcase half from plate via Xometry, (5) AlSi10Mg thermostat/crossover housing.
- **Published foundry one-off pricing does not exist.** Route 1.3 is unpriced until a foundry quotes.
- **The Hoosier $0.13/in^3 figure is as reported in trade press.** I could not confirm it is current. It may be several years old and needs a live quote.
- **ASTM B26 minimum properties are from memory**, marked [E]. They need checking against the standard before anyone designs to them.
- **I could not read `makerplane/decisions/ORG-009-engine-program-and-airframe-pause.md`.** It is not in any local maos-workspace clone, and the clone cannot fetch (authentication fails). This envelope is written from the issue text and my profile's brief.

## Sources (all read 2026-10-16)

- SendCutSend CNC machining specifications: https://sendcutsend.com/services/cnc-machining/
- Protolabs CNC milling design guidelines: https://www.protolabs.com/services/cnc-machining/cnc-milling/design-guidelines/
- Xometry tolerance standards (ISO 2768, ISO 286): https://xometry.pro/en/?p=16868
- ExOne sand printing network, 3-5 day molds: https://www.nasdaq.com/press-release/exone-launches-new-sand-3d-printing-network-powered-by-more-than-40-industrial-binder
- Hoosier Pattern $0.13/in^3 printed sand: https://www.additivemanufacturing.media/articles/commercializing-sand-3d-printing-in-the-new-tech-belt
- 3D sand printing for race engine castings: https://www.raceenginetechnology.com/News/3d-sand-printing-vs-traditional-tooling
- Lost-PLA engine cylinder (Hackaday, 2026-08-28): https://hackaday.com/2026/08/28/casting-engine-parts-from-3d-prints/
- Hobby casting porosity mechanisms: https://homemodelenginemachinist.com/threads/metal-casting-at-home.34377
- Vacuum impregnation cost: https://www.godfreywing.com/blog/cost-of-vacuum-impregnation/ ; https://www.sharrettsplating.com/blog/solving-porosity-with-vacuum-impregnation/
- Heat-treat pricing structure: https://www.iforgeiron.com/topic/26378-how-to-price-a-heat-treatment/
- Machine shop operations and prices: https://bullnosegarage.com/common-engine-machine-work-definitions-and-costs/
- Custom billet crank prices and lead time: https://www.summitracing.com/parts/cro-95185c ; https://turbobuick.com/threads/which-steel-crank.441714/page-2
- Nikasil re-plating: https://lnengineering.com/nikasil-cylinder-nsc-plating-reconditioning-for-porsche-engines.html ; https://pilotsofamerica.com/community/threads/so-would-you-pay-extra-for-nikasil-cylinders.106574/post-2387988
- Darton sleeves: https://grassrootsmotorsports.com/forum/grm/learn-me-block-sleeving-d16a6/23904/page1
- Wiseco pistons: https://shop.revzone.com.au/products/wiseco-forged-piston-single-fits-sbc-ls1-vortec-5-1239032
- Eagle and Manley rods: https://www.manleyperformance.com/?p=233904 ; https://www.velocityshop.com/products/manley-dodge-neon-srt-4-2-4l-i4-dohc-h-beam-connecting-rod-set-set-of-4
- Clevite bearings: https://modbargains.com/clevite-subaru-ej-series-5-thrust-main-bearing-set
- Ferrea valves: https://www.orientexpressracing.com/product/10680/ferrea-stainless-steel-valve
- Cometic MLS gaskets: https://www.summitracing.com/parts/cgt-c5118-030/make/ford ; https://modbargains.com/cometic-ford-2-3l-ohc-97mm-bore-018-inch-mls-head-gasket
- Bosch EV14 injectors: https://www.highflowfuel.com/bosch-ev14-fuel-injectors-280158230-choose-qty/
- GM D585 coils: https://ictbillet.com/collections/ignition-coils
- Davies Craig EWP115: https://www.americanmuscle.com/challenger-ewp115-alloy-remote-electric-water-pump-12-volt-dc-8140.html
- JLC3DP metal pricing: https://jlc3dp.com/news/materials-finishing-pricing-update-july2026 ; https://jlc3dp.com/blog/drastic-material-price-cuts-and-adjusted-post-processing-service-fees
