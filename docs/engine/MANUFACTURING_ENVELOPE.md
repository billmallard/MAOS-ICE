# Engine manufacturing envelope, v1

Owner: MANUFACTURING. Issues: AER-3321 (v0, parent AER-3320); AER-3328 (v1, parent AER-3326). Program: ORG-009, 2026-10-16.
For PROPULSION to commit as `MAOS-ICE/docs/engine/MANUFACTURING_ENVELOPE.md`.
Status: v0 (sections 1-8) Published so the six concepts are written inside it. Nothing here is a quote on real geometry yet, because there is no geometry yet.

v1 (2026-10-16) adds section 9, bottom-up estimates for concept H's six castings, liner and crank, and section 10, normalizing hardware sourcing. Section 9 numbers are still [E], not [Q]: no STEP geometry exists and no RFQ has been sent (9.6). Sections 1-8 are unchanged except the open items in 8.

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

- **v1 update:** items (1)-(3) below now have bottom-up [E] estimates for concept H in section 9. They are still not [Q]; section 9.6 names what turns them into quotes.
- **No quotes on real geometry.** There is no geometry yet. Every [Q] stays open until PROPULSION gives a part envelope. The first quotes I will run, in order: (1) first-op job-shop machining of a crankcase half, (2) bureau-printed mold + pour + T6 + impregnation of a crankcase half, (3) the same for a head, (4) billet crankcase half from plate via Xometry, (5) AlSi10Mg thermostat/crossover housing.
- **Published foundry one-off pricing does not exist.** Route 1.3 is unpriced until a foundry quotes.
- **The Hoosier $0.13/in^3 figure is as reported in trade press.** I could not confirm it is current. It may be several years old and needs a live quote.
- **ASTM B26 minimum properties are from memory**, marked [E]. They need checking against the standard before anyone designs to them.
- **I could not read `makerplane/decisions/ORG-009-engine-program-and-airframe-pause.md`.** It is not in any local maos-workspace clone, and the clone cannot fetch (authentication fails). This envelope is written from the issue text and my profile's brief.

## 9. Concept H: casting and first-op estimates, liner and crank (v1, AER-3328)

PROPULSION's part envelopes are in `RANKING_PHASE1.md` section 10. The numbers below come from `h_quote_estimate.py`, which MANUFACTURING supplied with this envelope for `analysis/engine_phase1/`. **None of them is a [Q] yet.** A real quote needs a STEP file and an RFQ to a named shop (9.6). These are bottom-up [E] estimates built on sourced rates [S]. They replace the phase-0 bands, which had no method.

### 9.1 Method

- **First-op.** For each casting: CAM programming hours, fixture cost, then per setup the setup hours (per batch) and cycle hours (per part), plus first-article inspection. Hours are my operation-by-operation estimate [E]. The rates are sourced [S]:
  - 4-axis mill: $60-90/h.
  - 5-axis: $100-200/h.
  - CAM programming: $50-150/h.
  - Horizontal machining center (HMC): no published rate found, so taken at the 5-axis band [E].
- **Casting.** Hoosier Pattern prices printed sand at **$0.13/in^3 of the CAD bounding box**, cleaned, with a **$450 minimum order** (page updated 2025-12-16) [S]. The price follows the mold's bounding box, not the part's volume, so shelling the mold does not reduce it. The mold box is the part plus 50 mm per side, x1.15-1.35 for gating and risers, plus a core allowance [E]. Every other casting line is [E], because nothing published was found:
  - pour and fettle;
  - T6 lot;
  - impregnation lot;
  - radiography: 6-12 digital exposures at $15-50 each [S], plus technician time.
- **Part numbers.** The two crankcase halves are two part numbers. The two heads are a mirrored pair, so also two part numbers. The two cylinder-bank blocks are taken as **one part number, left = right** (9.5, item 3). Programming and fixture cost (NRE) is paid once per part number.

### 9.2 Per casting

| Part | First-op, qty 1 (carries its NRE) | First-op each, qty 5 | First-op marginal (NRE paid once by the program) | NRE per part number (CAM + fixture) | Casting, qty 1 (mold + pour + T6 + impreg + RT) | Casting each, qty 5 | Printed sand alone |
|---|---|---|---|---|---|---|---|
| Crankcase half | $2.0k-6.7k | $0.65k-2.0k | $0.57k-1.4k | $1.4k-5.3k | $1.2k-2.7k | $1.0k-2.1k | $630-770 [S rate] |
| Cylinder-bank block | $1.3k-4.3k | $0.34k-1.1k | $0.26k-0.68k | $1.0k-3.6k | $1.0k-2.4k | $0.79k-1.8k | $370-440 [S rate] |
| Bank head | $2.2k-7.9k | $0.69k-2.3k | $0.53k-1.7k | $1.7k-6.3k | $0.89k-2.3k | $0.71k-1.7k | $290-350 [S rate] |

All [E] except where tagged. Setups and hours assumed:

- **Crankcase half.**
  - Setup A, split face on a 4-axis machine: about 30 holes and the dowels, 1.2-1.8 h.
  - Setup B, on the doweled pair on an HMC: mains, cam, thrust faces, lifters, bank pads, studs and galleries, 2.5-3.5 h per half.
  - CAM: 12-22 h per part number.
- **Block.** Base pad 0.6-1.0 h. Deck plus 6 registers plus studs 1.2-2.0 h. CAM: 8-14 h.
- **Head.** Deck 0.8-1.2 h on 4-axis. Then 2.5-4.0 h on a 5-axis, covering:
  - seats and guides;
  - plug and injector bosses;
  - rocker pads;
  - port flanges.

  CAM: 14-25 h per part number.

### 9.3 Per engine (six castings): the answer to the cost question

| Line | First engine | Each engine, batch of 5 | Each engine, batch of 5, NRE paid once by the program | Phase-1 model line |
|---|---|---|---|---|
| First-op machining | **$9.8k-33.9k** | **$3.1k-9.9k** | **$1.7k-4.6k** | $3.0k-12.0k (`FIRST_OP` x 6) |
| Castings (mold, pour, T6, impregnation, RT) | $6.2k-14.7k | $5.1k-11.2k | same | $4.4k-10.9k (`CASE_HALF` + `HEAD` + `BLOCK`) |
| First-op NRE for the whole program | $7.2k-26.7k, once | | | not carried |

What it means for the $22k test:

1. **The first engine cannot meet $22k.** First-op alone costs $9.8k-34k, because one engine carries every CAM program and every fixture. That is true of any cast engine at quantity 1. It is not a flaw of concept H.
2. **$22k is a per-engine number, so it only holds if the NRE is paid once.** That means AeroCommons (or a builder group) pays $7k-27k one time for CAM programs and a fixture set. The fixtures then travel between shops and the CAM is published with the design (envelope 2.2). On that basis, first-op lands at **$1.7k-4.6k per engine**, below the model's $3k-12k.
3. **Castings land above the model** at the low end: $5.1k against $4.4k at a batch of 5, and $6.2k for the first engine. That is because radiography and the per-lot T6 and impregnation minimums were not in the phase-0 line.
4. **The crank and liner lines also move up (9.3 and 9.4).** Net, the honest low end moves **up**, not down. Section 9.7 lists the changes to the line items so that PROPULSION can rerun `member_200.py`. **This estimate does not rescue $22k.** The levers in 9.5 are where the money is.

### 9.4 Catalog wet liner at 104.8 mm, and the billet crank

**Wet liner.** No catalog wet liner is sold **finished** at 104.8 mm (4.125 in).

The closest fit is the **Darton MID (Modular Integrated Deck) sleeve for the GM LS**:
- ductile iron, wet, sealed by 3 O-rings at the bottom register;
- the top flanges nest together to form the deck;
- maximum bore 4.160 in, wall 0.220 in [S, 2014 Darton FAQ];
- **$1,904 per set of 8**, retail [S, n/d, read 2026-10-16]. That is $238 per sleeve, or $317 per cylinder if a set of 8 is bought for 6 cylinders. Whether single sleeves are sold is [Q].

It is the right family for H. It is LS-native, so it matches the 111.8 mm (4.400 in) bore pitch and takes catalog LS7-bore pistons. But two things change the plan:

1. **It is supplied at 4.100 in, and must be bored about 0.020 in and honed to 4.125 in after installation** [S]. So the bore-and-hone step does not disappear. It goes to the automotive machine shop at $15-60 + $10-20 per cylinder, x1.3 for 2026 [S, envelope 2.1]. That is $33-104 per cylinder.
2. **Mass.** A 0.220 in iron wall is drag-race practice. My estimate is about **2.5-3 kg per sleeve, 15-18 kg per engine** [E: wall x length x density, length assumed 180 mm]. That is a real hit against H's 134 kg. It is PROPULSION's call. The alternative is a thinner iron dry sleeve in a closed-deck block, which is cheaper and lighter but gives up the "liner sets the deck" simplicity.

Two more facts about the MID:
- The sleeve length was not found [Q].
- The block deck must be machined to Darton's MID preparation drawing, which Darton supplies to shops [E]. Copy that drawing into the bank-block design rather than inventing a register geometry.

Cheaper liners exist, but they are not recommended. A John Deere 4045 wet liner kit is **106.5 mm, at about £150 per cylinder including the piston** [S]. It is semi-finished and comes with a diesel piston, so moving to it means a custom spark-ignition piston (envelope 4, [Q]). Porsche Nikasil barrels are 102 mm, sold only as matched sets at $4.7k-8.6k per 6 [S], and are air-cooled barrels, not wet liners.

**Liner line:** $300-450 per cylinder including the bore and hone [E from the [S] rows]. The model line is $150-400.

**Billet crank, 6-throw, 101.6 mm stroke, 60 mm mains, propeller flange.** There is no catalog part. Anchors [S, read 2026-10-16]:

| Crank | Price | Notes |
|---|---|---|
| Catalog 6-throw 4340 billets (Brian Crower 2JZ, Tomei RB26, Nitto RB26) | $4.0k-4.9k | nitrided |
| Eagle 2JZ / RB26 4340 | $2.3k-2.8k | |
| Crower custom billet, a V8 example | $6,288 | shipping date shown as 2027-02-18, so **about 18-20 weeks** lead |

A one-off flat-6 crank needs new drawings, an opposed-throw layout and a propeller flange. My estimate is **$6.3k-9k plus balancing at $300-400** [E, from the custom anchor], with about 20 weeks lead time [S]. It is [Q] to Crower, Bryant or Winberg once PROPULSION has a crank drawing.

The model line, `CRANK` x 1.15, is $3.9k-7.2k. My low end is about $2.4k higher.

Two dimension choices let catalog parts fit, in the spirit of envelope Finding 4:
- **Rod journal at 2.100 in**, so catalog LS rods and rod shells fit.
- **60 mm mains** appear to match the Subaru EJ main-shell catalog. That is [E] from memory and should be confirmed against a Clevite or King listing before the size is frozen.

### 9.5 DFM objections on the three envelopes (raise now, cheap now)

None of the three parts falls outside the casting envelope. The largest box is 560 mm, and a binder-jet bed is about 1.8 x 1.0 x 0.7 m (ExOne S-Max class) [S, envelope 1]. The objections are about setups, part count and the shop pool:

1. **Merge each cylinder-bank block into its crankcase half (the largest lever).** Subaru's EJ and EZ flat engines do exactly this. The block halves carry integral cylinder banks, split at the crank centerline, and run open-deck wet or semi-wet bores [E, general practice]. The merge would:
   - delete 2 castings and 1 part number of NRE, worth $1.0k-3.6k once;
   - delete 2 block-to-case gaskets and about 16-24 studs and nuts;
   - delete 2 machined pad pairs.

   The case half grows to about 560 x 300 x 325 mm with a coolant core. Printed sand rises by about $350-450 per half, and cycle time by about 1-1.5 h. The net saving is about **$1.0k-2.5k per engine plus about 30 parts** [E]. There is a second benefit: the liner registers come off the same datum as the mains. The cost is that a scrapped pour now scraps the whole case half.
2. **Crankcase setups: two, not three.** In a flat engine the lifter bores and the bank pads both face outboard, normal to the split plane. On a 4-axis HMC with the doweled pair on a tombstone, the table indexes 0 / 90 / 180 / 270 degrees. So mains, cam, thrust faces, lifters, pads and studs all come off **one** setup, referenced to the dowels. Constraints:
   - The doweled pair (about 560 x 320 x 300 mm, about 22 kg) needs an HMC with a pallet of 630 mm or more and about 1,000 mm swing. That narrows the shop pool, so name it in the RFQ.
   - The mains are bored from both ends, with a reach of 300 mm or less per side.
   - The align hone then goes to the automotive shop: $350-440 [S], already in `MACHINE_SHOP`.
3. **Make the left and right bank blocks the same part number.** Check that the coolant inlet boss and stud pattern are symmetric under a 180-degree rotation. This halves the block NRE, and the estimate above already assumes it. Heads are probably a mirrored pair. If they can be made identical, about $1.7k-6.3k of NRE goes.
4. **The head is a 5-axis part as drawn. Make it a 4-axis part.** PROPULSION's "2 setups" leaves out the plug bosses, injector bosses, rocker pads and port flanges, which sit on 4-6 more orientations. Three constraints bring every feature after the deck onto **one tilt plus a rotary axis**:
   - all six valve axes parallel (LS heads are, at a single included angle);
   - the two plugs per cylinder on two parallel axis sets;
   - **both port flanges on one face**, as Lycoming's down-ported cylinders are.

   That moves the head's second setup from $100-200/h to $60-90/h and widens the shop pool. Worth about $300-900 per head [E].
5. **Block registers stepped from one side.** Specify lower register diameter <= upper, so both bore from the deck in one setup. This is already implied by "deck + registers"; make it a drawing rule.
6. **Drilled-and-plugged galleries (agreed).** Keep each drilled run within 25 x diameter from its entry face. On a 560 mm case drilled from both ends that means a **main gallery of 12 mm or larger**, or a gun-drilling operation [Q]. Plug pressurized galleries with threaded plugs plus sealant, staked, not cup plugs (ledger item MFG-4).
7. **Printed-sand coolant cores need cleanout exits.** Each head jacket core needs at least 2 exits of 12 mm or more to get sand out. They become threaded or Welch plugs, about 3-4 per head [E]. The builder borescopes the jacket at receipt (B1). Residual core sand next to a combustion chamber is a hot spot (MFG-2).

### 9.6 What it takes to turn these [E] into [Q]

- **A STEP envelope model for each casting.** Coarse is fine if datum pads and critical bores are shown. Owner: PROPULSION. MANUFACTURING can build the coarse STEP from section 10 of `RANKING_PHASE1.md` with `maos freecad` if PROPULSION wants that. Say so on the issue.
- **RFQs sent to named shops.**
  - Print plus pour: Hoosier Pattern, Humtown, General Foundry Service (CA, prints and pours aluminum in-house), Kimura Foundry America (IN, all molds printed, about 1 week to raw casting) and Boose Aluminum (PA, pours and heat-treats in-house) [S, quote-only].
  - First-op: two or three HMC/5-axis job shops.
  - I hold no email or account to send an RFQ. **Unblock: Bill or Elon names who sends the RFQs**, or grants a channel. Until then every line here stays [E].
- **What the RFQ should carry:** quantity 1 and 5, A356-T6 / A357-T6, RT acceptance class, impregnation, and the setup plan in 9.5. The datum-pad locations are on the drawing.

### 9.7 Line-item changes PROPULSION can drop into `member_200.py` / `cost_floor.py` (200 hp member, per engine)

The table gives two bases: the first engine, and each engine of a batch of 5 with NRE paid once.

| Line | Model now | First engine | Batch of 5, NRE once | Tag |
|---|---|---|---|---|
| First-op, 6 castings | $3.0k-12.0k | $9.8k-33.9k | $1.7k-4.6k | [E] |
| Castings, 6 | $4.4k-10.9k | $6.2k-14.7k | $5.1k-11.2k | [E] on [S] sand rate |
| Program NRE (CAM + fixtures) | not carried | carried in first-op above | $7.2k-26.7k once, outside the per-engine number | [E] |
| Crank | $3.9k-7.2k | $6.6k-9.4k incl. balance | same | [E] on [S] anchors |
| Liners, 6 incl. bore/hone | $0.9k-2.4k | $1.8k-2.7k | same | [E] on [S] |
| Normalizing (turbo, wastegate control, intercooler, plumbing) | $1.2k-3.0k | $2.0k-4.5k | same | section 10 |
| `MACHINE_SHOP` | $0.8k-2.0k x 1.3 | drop the two block decks, now done in first-op | same | [E] |

Rerunning the floor is PROPULSION's job. My read: **at batch-5 / NRE-once the low end rises about $3-4k, to roughly $26-27k.** First-op falls; the crank, liners, castings and normalizing rise. The 9.5 levers recover about $1.5-4k. **$22k is not met on this basis without either the block merge plus the 4-axis head plus a cheaper crank, or relaxing the target.** That is the input to PROPULSION's planned escalation.

## 10. Normalizing hardware sourcing (v1, AER-3328)

The duty comes from PROPULSION:
- **Compressor:** 0.24 kg/s corrected (31.7 lb/min) at pressure ratio 1.68. At 12,000 ft ISA that is about **0.16 kg/s actual** [E: x p/p0 / sqrt(T/T0)].
- **Intercooler:** about 4 kW at 0.13 kg/s, which is a charge-air drop of about **31 K** [E].

Prices are retail, read 2026-10-16. Most pages carry no date, and sale and list prices are mixed. **Retailer "30 lb" masses are shipping weights. I give no dry mass that is not marked [E].**

### 10.1 Turbocharger: all catalog parts

| Unit | Price [S] | Bearing / housing [S] | Wastegate [S] | Lead [S] | Dry mass |
|---|---|---|---|---|---|
| Garrett GT2860RS | $1,256-1,610 | dual ball bearing; oil cooled | internal, with actuator | in stock | 6-8 kg [E] |
| Garrett GTX2860R Gen II | $1,428 + $120 actuator | dual ceramic ball; **water-cooled** center housing | internal, T25 0.64/0.86 A/R | in stock | 6-8 kg [E] |
| Garrett G25-550 | $1,771-2,966 | **oil and water cooled** (4 water ports) | internal-gate or free-float housings | in stock | 7-9 kg [E] |
| BorgWarner EFR 6258 | $1,811 | dual-row ceramic ball; water cooling recommended | internal, **integrated boost-control solenoid** | in stock | sources disagree, 2.7-15 kg; [Q] |
| Precision 5558 Gen2 | $1,920-2,504 | ball | | built to order, 3-5 weeks | likely oversized (650 hp) |

Notes on the turbo:

- **Map fit is not checked by MANUFACTURING.** The GT2860RS and GTX2860R class (250-360 hp) is the right size bracket for 31.7 lb/min. The G25-550 is probably oversized at pressure ratio 1.68. Owner of the compressor-map match: PROPULSION.
- **Water-cooled center housings are the norm in this class.** With the electric coolant pump already in the envelope (Davies Craig EWP115), an **after-run** of the pump after shutdown cools the bearing housing with no extra part. That is a real heat-soak advantage for an aircraft. It is PROPULSION's or FADEC's call.
- **Wastegate control for normalizing.** The gate must be fully open at sea level and close progressively with altitude to hold sea-level manifold pressure. There are two routes:
  - an ECU solenoid on the internal pneumatic actuator: about $100-300 [E]; the pneumatic actuator alone is $94-136 [S];
  - an electronic wastegate: Turbosmart GenV eWG45 at $1,024-1,138 [S]; Hella OEM electronic actuators from about EUR 98 [S].

  Both failure modes go to the ledger: a gate stuck closed overboosts at low altitude; a gate stuck open loses altitude power.

**Turbo line:** turbo $1.3k-2.2k, wastegate control $0.1k-1.1k, oil and coolant lines and manifold flange $0.3k-0.6k [E]. About **$1.7k-3.9k**, plus the intercooler below.

### 10.2 Air-to-air intercooler: catalog cores

| Core | Price [S] | Size | Rating [S] | Mass |
|---|---|---|---|---|
| Garrett 703518-6015 | EUR 140-175 | 457 x 163 x 76 mm | 310 hp | 3-4 kg [E] |
| Mishimoto 20 x 7.8 x 3.5 in | $246 | | | 16.6 lb shipping, so about 5 kg dry [E] |
| Treadstone TR6, **complete with tanks** | $290-420 | core 550 x 150 x 82.5 mm | 400 hp, under 2 psi drop | 4-5 kg [E] |

- 4 kW at 0.13 kg/s is a small duty. The smallest Garrett core or a complete TR6 covers it [E: rating x 200 hp margin].
- A complete unit with tanks (TR6) is the B0 path. Otherwise the end tanks are 5052 sheet cut by a service plus TIG (envelope 3) at about $100-300 [E].
- **Installed line:** $0.3k-0.6k, 4-6 kg with ducting stubs [E].
- **Install conflict to flag:** the core needs ram or cooling air, so it competes with the radiator duct for R-38. That is PROPULSION's call.

### 10.3 Supercharger, for comparison

Drive power at the duty [E, mine, isentropic plus efficiency, for comparison only]:

- **About 10-11 kW (14 hp) for a centrifugal unit**, at 70 % compressor efficiency and 95 % drive efficiency.
- **About 11-13 kW (15-17 hp) for a positive-displacement unit**, at 60-70 % efficiency.

A turbo takes that energy from the exhaust instead. Its cost is backpressure, which is PROPULSION's number.

| Unit | Class | Price [S] | Mass [S] | Fit to duty [S] | Notes |
|---|---|---|---|---|---|
| Rotrex C30-94 | centrifugal, traction drive | $2,103 | **5.1 kg** | max 0.39 kg/s and pressure ratio 2.52, so the duty sits inside the map | self-contained oil system on Rotrex traction fluid, oil inlet 80 C max. Needs a belt step-up drive of about 4-5:1 from 3,300 rpm [E]: custom pulleys and a bracket, which are service-machinable |
| Vortech V-3 Si | centrifugal | $3,606, **listed unavailable** | n/f | oversized (775 hp) | |
| ProCharger P-1SC | centrifugal | head unit n/f | n/f | oversized | |
| Eaton TVS R900 | positive displacement (Roots/TVS) | **bare unit not sold**; Harrop kits $5,885+ | n/f, 10-15 kg [E] | max pressure ratio 1.8, 0.297 kg/s at 18,000 rpm, so near the top of its range | OEM-only part |
| Whipple W100AX 1.6 L | twin-screw | $2,595 bare | n/f, 12-18 kg [E] | [E] fits | |
| TiAL Q 50 mm bypass / blow-off | valve | $279 | | 2 psi spring version for supercharged use | |

**Reading it.** The only catalog-friendly supercharger at this duty is the **Rotrex C30-94**: light, priced and in the map. It costs about 14 hp of shaft power at critical altitude. A centrifugal unit also cannot "normalize" by bypass alone, because its pressure ratio follows rpm, not altitude. At sea level it still absorbs drive power unless it is declutched or throttled [E]. I found no verified aircraft use of a Rotrex.

**The turbo stays the catalog-cheaper, lighter-at-the-shaft route.** The supercharger's case is having no hot turbine and manifold to make or inspect. Part counts are similar:
- turbo: unit, actuator, oil feed and drain, coolant lines, manifold flange, downpipe;
- supercharger: unit, belt, 2 pulleys, tensioner, bracket, bypass valve.

**Line for comparison:** centrifugal supercharger system $2.7k-3.8k [E: $2,103 + bypass $279 + pulleys, bracket and tensioner $300-800 + oil cooler and lines $100-300 + intercooler as 10.2].

### 10.4 Additions to the failure-mode ledger (build quality, for PROPULSION to enter)

- **MFG-1. First-op datum error across the case pair** (lifter-to-cam or main misalignment). Mitigation: one setup on the doweled pair (9.5 item 2), a CMM report with the first article, and Plastigage at assembly.
- **MFG-2. Residual printed-sand core in a head or block jacket**, causing a local hot spot. Mitigation: cleanout exits of 12 mm or more, a borescope at receipt, and a flush.
- **MFG-3. Darton MID O-ring pinched on install**, putting coolant in the oil. Mitigation: a lead-in chamfer spec, and a jacket pressure test after liner install (B1).
- **MFG-4. Drilled-gallery plug backs out**, causing oil loss. Mitigation: threaded plugs, thread sealant and staking; no cup plugs on pressurized galleries.
- **MFG-5. Wastegate actuator stuck**: overboost at low altitude, or loss of altitude power. Mitigation: a FADEC overboost limit, and a manifold-pressure check in the run-up. The design side is PROPULSION's.

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

### Sources added in v1 (all read 2026-10-16; most retail pages carry no date)

- Hoosier Pattern printed-sand rate, $450 minimum, bounding-box basis: https://hoosierpattern.com/news/cost-analysis-breakdown-of-3d-sand-printing/ (updated 2025-12-16)
- Humtown $0.07-0.10/in^3: https://www.additivemanufacturing.media/articles/commercializing-sand-3d-printing-in-the-new-tech-belt (2021-08-21)
- Head casting and machining anecdotes (forum, 2018): https://www.speed-talk.com/forum/viewtopic.php?t=55246
- Print + pour foundries: https://www.genfoundry.com/capabilities/3d-printed-sand-mold-castings ; https://www.additivemanufacturing.media/articles/new-kimura-us-metal-casting-plant-relies-entirely-on-3d-printing-for-molds-and-cores ; https://www.boosealum.com/capabilities/3d-printed-sand-molds/
- Radiography rates: https://www.ndtintel.com/guides/pdf/ndt-inspection-rate-guide-2026.pdf
- CNC hourly rates: https://fabcon.com/articles/?p=302 (2026-05-19); https://precisionam.com/articles/precision-machining/5-axis-cnc-hourly-rate/ (2026-05-19); https://hotean.com/blogs/hotean-blog/cnc-machining-shop-rates-in-2025 (2025-08-12)
- Machine-shop line items: http://paragonengines.com/machineshoppricing ; https://www.besracing.com/machine-shop-services.html (2022-12-01); https://oakleymotorsports.com/wp-content/uploads/2025/01/OakleyMotorsportsPriceList2024.pdf ; https://amsmotomachine.com/index.php/labor-pricing (2024-05-30)
- Darton MID LS: https://vividracing.com/brian-crower-block-wet-sleeves-darton-mid-4125-inch-4160-inch-max-bore-chevrolet-ls1-ls6-p-152820306.html ; https://www.corvetteactioncenter.com/tech/knowledgebase/article/1997-2004-corvette-faqs-regarding-the-re-sleeving-of-ls1-ls6-engine-blocks-with-the-darton-mid-sleeve-kit-815.html (2014-08-05)
- John Deere 4045 cylinder kit: https://dhfarmmachinery.com/products/cylinder-kit-qre507850.html
- Porsche Nikasil sets: https://fvd.net/us-en/100103038031/mahle-38l-piston-cylinder-set-964-993-1131-102mm-bore-109mm-sleeve-mach-fit-narrow-rod.html
- 6-throw billet cranks: https://www.evasivemotorsports.com/store/product/brian-crower-crankshaft-toyota-2jzgte2jzge-86mm-stroke-4340-billet-honda-journal/ ; https://www.kuremotorsport.com/products/tomei-forged-billet-full-counterweight-crankshaft-rb26dett-2-6l-73-7mm ; https://www.summitracing.com/parts/cro-95185c
- Turbochargers: https://www.garrettmotion.com/racing-and-performance/performance-catalog/turbo/g-series-g25-550/ ; https://www.full-race.com/garrett-gtx2860r-gen-ii-turbo ; https://onefastshop.com/products/garrett-gt2860rs-turbocharger-dual-ball-bearing-2 ; https://www.full-race.com/borgwarner-efr-6258-turbo ; https://ffperformance.co/product/precision-turbo-pt5558-cea-gen2-turbocharger/
- Wastegates and actuators: https://www.subispeed.com/products/tia-mvsb-tial-mv-s-wastegate-38mm-blue-w-all-springs ; https://onefastshop.com/products/turbosmart-electronic-wg45-gen-v-hyper-gate-45-wastegate-black-1 ; https://www.melett.com/hella-actuators/ ; https://www.amsperformance.com/?p=72653
- Intercooler cores: https://www.garrettmotion.com/wp-content/uploads/2020/10/Garrett_Performance_Intercooler_Cores_Price_Update_Sell_Sheet.pdf (2023-08); https://www.mishimoto.com/20-7-8-3-5-universal-intercooler-core.html ; https://www.speedscience.co.nz/products/treadstone-tr6-interooler
- Superchargers: https://shop.rotrex.com/product/c30-94-supercharger/ ; https://www.rotrex.com/wp-content/uploads/2022/01/Rotrex-Technical-Datasheet-C30-Rev6.0.pdf ; https://vortechsuperchargers.com/products/v-3-si-trim-supercharger ; https://www.eaton.com/de/de-de/catalog/engine-solutions/tvs-r900.html ; https://harrop.com.au/TVS900-r53-mini-cooper-s ; https://whipplesuperchargers.com/i-2004 ; https://www.jegs.com/i/tial-sport-768-002576-q-series-50mm-blow-off-valve-2-psi-spring-supercharged-applications
