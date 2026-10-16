# Concept H castings: rulings on the DFM objections, the liner, the coarse STEP, and the cost floor on both bases

Owner: PROPULSION. Issue: AER-3331 (parent AER-3330; follows AER-3329 and MANUFACTURING envelope v1, AER-3328). Date: 2026-10-16.
Status: **design rulings and coarse geometry. Nothing here has been made, measured or run.** This is an experimental engine design. Nothing in it is certified, certifiable or flight-ready.

Numbers come from `analysis/engine_phase1/castings_h.py` (tables in `castings_h_tables.md`) and from the models in `cad/concept_h/` (`PART_LIST.md`). Cost lines are MANUFACTURING's bottom-up estimates [E] on sourced rates, as in RECOST_PHASE1B.md. None is a quote.

## 1. The answer

1. **Six castings become four, on three part numbers.** Each cylinder bank is cast into its crankcase half, and one head part number serves both banks. Five of MANUFACTURING's seven objections are accepted as written. Item 4 (the 4-axis head) is accepted with one constraint dropped. Item 3 is accepted for the heads and is moot for the blocks, because item 1 deletes the blocks.
2. **The Darton MID wet liner stays.** Against a dry sleeve in a closed deck it costs **2.9-4.1 kg per engine**, not the 15-18 kg of iron it weighs. The open deck is what makes the merged case castable and the liner a builder-replaceable part.
3. **The coarse STEP of each surviving casting is drawn and committed** (`cad/concept_h/`, PROPULSION drew it). Datums, critical bores and alloys are shown. The three parts assemble with zero overlap.
4. **The 200 hp cost floor, after the rulings, on both bases:**

| Basis | Low / mid / high | Against $22k |
|---|---|---|
| **1. First engine carries all program NRE** | **$31.7k / $48.0k / $72.8k** | $9.7k over at the low end |
| **2. Each engine of a batch of 5, NRE paid once by the program** | **$25.1k / $35.2k / $49.3k**, plus **$5.1k-19.2k of NRE once** | $3.1k over at the low end |

Against MANUFACTURING's six-casting line items, the rulings take **$3.8k-13.2k off the first engine and $1.2k-3.9k off each engine of five**. Removing a double count in the machine-shop line takes another $0.3k-1.3k (section 6). Neither basis meets $22k. Which basis R-35 means is Bill's question on AER-3330, so this document does not pick one.

## 2. Rulings on envelope v1 section 9.5

| # | Objection | Ruling | The reason, in numbers |
|---|---|---|---|
| 1 | Merge each cylinder-bank block into its crankcase half | **Accept** | Deletes 2 castings, 2 base gaskets and about 24 studs and nuts. First-op plus castings fall by **$1.7k-5.3k on the first engine** and **$1.1k-3.0k per engine of five**. The scrap risk it adds is worth **$0.1k-0.2k per engine** in expectation, at an assumed 5-20 % scrap rate per bureau pour, if every casting is radiographed before first-op. The liner registers come off the same setup as the mains, so bore-to-crank squareness no longer stacks through a bolted joint. |
| 2 | Crankcase in one HMC setup on the doweled pair | **Accept** | Every feature after the split face lies on an axis parallel to the crank (mains, cam, gallery) or to the cylinders (lifters, decks, registers, head studs, main studs). The pair sits on its pan-rail face and indexes 0/90/180/270. From the STEP the pair is **563 x 331 x 470 mm** across both decks and about 42 kg (model mass, an upper bound). **Machine: an HMC with a 630 mm pallet or larger and about 1,000 mm swing** (833 mm needed for the part plus clearance), Y travel of about 500 mm with a riser, and a damped boring bar for the mains, bored 280 mm from each end through 64 mm housings (L/D about 5-6). The align hone stays at the automotive shop. MANUFACTURING's 325 mm-per-half box was conservative; the deck sits 235 mm from the split plane. |
| 3 | Left = right bank blocks; can the heads be one part number? | **Blocks: moot (deleted by #1). Heads: accept, one part number.** | The RH bank takes the head rotated 180 degrees about the vertical axis. That rotation keeps top as top, so intake-up and exhaust-down survive it. It works if the head-stud pattern and ring dowels are symmetric, there is a coolant boss at each end (one plugged per bank), and the cam's lobes follow the reversed valve order on one bank (the cam is custom anyway). Taking this ruling on its own (#1 + #3 against #1 alone) cuts **$1.7k-6.3k of NRE once and $1.9k-7.0k off the first engine**. **The case halves cannot be one part number**: the nose carries the thrust faces, the rear carries the cam drive, the cam sits in the split plane below the crank, and the banks are offset 38.6 mm along the crank. |
| 4 | Head as a 4-axis part | **Accept the aim. Drop "both port flanges on one face."** | The rule that does the work is **every machined axis normal to the head's long axis**. A rotary along the row then reaches every feature. The valve axes are parallel at 15 degrees. Plug set A comes from the top face and plug set B from the bottom, and each set is parallel. Injectors, ports and rocker pads follow the same rule. Ports on opposite faces (intake top, exhaust bottom, as on Continental's flat engines) are reachable on 4-axis. Putting both on one face would only add charge heating on an engine that is already knock-limited (CR about 8.4 on 91 AKI, RANKING_PHASE1.md section 3). **Drawing the head found one more feature to move**: coolant bosses on the end faces point along the row, where 4-axis cannot reach. They are now on the top face at both ends. Saving: per-head marginal first-op falls from $0.3k-1.0k to $0.2k-0.6k at a batch of 10. That is less than MANUFACTURING's $300-900, because I added 0.5 h of indexing time to the cycle. |
| 5 | Liner registers stepped from one side | **Accept: drawing rule DR-2** | Drawn as lower register 116 mm, jacket 127 mm, flange seat 131.4 mm, all bored from the deck in setup B. The exact diameters come from Darton's MID preparation drawing [Q]. |
| 6 | Drilled galleries within 25 x D; 12 mm main gallery or a gun-drill | **Accept, at 14 mm, with one rule added** | 27 kW of heat to oil at 200 hp needs about 60 L/min at a 15 K oil rise. Through 12 mm that is 8.9 m/s and up to 0.49 bar of drop along 560 mm. Through 14 mm it is 6.5 m/s and 0.24 bar, at 20 x D from each end (a full-flow upper bound; the flow falls along the gallery). **Added because of #1:** at least 5 mm of metal between any drilled oil passage and a coolant jacket. Threaded plugs with sealant, staked; no cup plugs on a pressurized passage. |
| 7 | Cleanout exits for printed-sand cores | **Accept, threaded plugs only** | Each head jacket core has two 22 mm exits: the coolant bosses at both ends. One is the coolant outlet; the other gets one threaded plug. The case jacket is open to the deck, so it needs no exits. **No Welch or cup plugs on any coolant jacket.** A plug lost in flight is a coolant loss, about 1 minute at MCP (FL-27). That is not worth the few dollars a press-in plug saves. |

### What the merge gives up

- **A scrapped pour scraps the whole half.** That is priced above. Radiographing every casting before first-op (DR-8) makes it a casting cost, not a casting-plus-machining cost.
- **Coolant now runs in the crankcase half.** A porosity path or crack between the jacket and the crank bay, or a drilled oil passage, puts coolant in the oil (FL-38). DR-6's 5 mm wall, radiography and a jacket pressure test before the liners go in are the mitigation.
- **The precedent is weaker than 9.5 states.** Subaru's EJ and EZ flat engines do cast the banks into the case halves. But they run cast-in iron liners in an open deck, not wet liners [E, general practice]. The integral case is proven. The wet liner in an integral flat case is ours to prove.

## 3. The liner: Darton MID wet liner, kept (envelope 9.4)

| | Darton MID wet liner, open deck | Dry iron sleeve, closed deck |
|---|---|---|
| Mass per cylinder | 2.76-2.96 kg of iron (0.220 in wall, 180 mm long [ASSUMED], flange) | 1.15 kg of iron (3 mm) **plus 1.12 kg of A356** (the 6 mm cylinder wall and closed deck the sleeve needs) = 2.27 kg |
| **Per engine** | **+2.9 to +4.1 kg against the dry sleeve** | baseline |
| Hoop stress at 70 bar peak pressure [ASSUMED] | 66 MPa, with no aluminum behind it | carried by the aluminum wall |
| Casting | jacket is a pocket open to the deck: the core is held and cleaned out through the deck | jacket is a closed core inside the largest casting: residual-sand risk next to the bore (FL-34), and a core shift thins the wall that must hold the sleeve's interference |
| Running surface | bored 0.020 in and honed after install (the liner line includes it) | bored and honed after the press fit |
| Overhaul | builder replaces the liner (B1) | shop presses out, re-bores the aluminum, presses in, bores and hones |
| Failure path it adds | bottom O-ring seal: coolant into the oil (FL-35) | none of its own; a loose sleeve is a shop defect |

**Ruling: keep the wet liner, and take the Darton MID for the first articles.** It is a catalog part that fits the LS bore pitch and the LS7 piston, it is what makes the merged case an open-faced casting, and it keeps the liner a builder part.

**Correction to RECOST_PHASE1B.md section 7.** Phase 1b credited a thin dry sleeve with saving 6-7 kg. That counted the iron and left out the aluminum cylinder wall and closed deck that a dry sleeve needs. On the like-for-like comparison above, the saving is **2.9-4.1 kg**. Phase 1b's 9.4-11.2 kg MID penalty stands as the mass the MID adds over phase 1's allowance. Only the size of the lever against it changes.

**The lever kept for later:** a custom wet liner with a 3.5 mm wall weighs about 1.8 kg, against 2.8 kg, at a hoop stress of 105 MPa. That is about 6 kg per engine for a custom part with no catalog source [Q]. It is not worth it for first articles.

## 4. The coarse STEP (envelope 9.6)

**Owner of record: PROPULSION drew it.** I did not take MANUFACTURING's offer to draft it, because drawing it was the test of rulings 2-4. Two findings came only from the geometry: the head's end-face coolant bosses broke the 4-axis rule, and MANUFACTURING's merged-case box was 90 mm deeper than the part.

| Part number | Casting | Qty / engine | Alloy | Model box (mm) | Model mass |
|---|---|---|---|---|---|
| H-101 | crankcase half LH, bank merged | 1 | A357-T6 | 563 x 331 x 235 | 20.9 kg |
| H-102 | crankcase half RH, bank merged | 1 | A357-T6 | 563 x 331 x 235 | 21.0 kg |
| H-201 | cylinder head, both banks | 2 | A356-T6 | 384 x 190 x 113 | 7.1 kg |

- **What is on the models:** datums A/B/C (split face and two reamed dowels on the case; deck and two ring dowels on the head), the as-cast 3-2-1 locating pads for the first setup, and every critical bore with its location: mains, cam, lifters, liner registers, head and main studs, main gallery, seat-insert and guide bores, both plug sets, injectors, ports and coolant bosses. The full list is `cad/concept_h/PART_LIST.md`.
- **What is not:** the case perimeter flange and its bolts, ribs, oil cross-drillings, fillets, draft, the real chamber and port shapes, and the coolant transfer passages, which wait on the MID flange drawing [Q].
- **Mass check.** The set is 56 kg of model metal (2 x 20.9 + 2 x 7.1). MANUFACTURING's six envelopes summed to 50-64 kg. The case halves are an upper bound (solid bulkheads, no lightening).
- **Checks run:** each STEP reads back as one valid solid. Case/case and head/deck overlaps are 0 mm^3.

![Casting set assembled: two merged case halves with one head part number on each deck](../../cad/concept_h/H-000_casting_set.png)

Renders and regeneration commands: `cad/concept_h/README.md`.

## 5. Drawing rules (accepted rulings, plus the two the merge adds)

| ID | Rule | From |
|---|---|---|
| DR-1 | Every precision bore houses a bought part; the casting never carries a running surface. | envelope finding 2 |
| DR-2 | Liner registers stepped: flange seat >= jacket >= lower register, all bored from the deck in one setup. | 9.5 #5 |
| DR-3 | Case pair: every machined feature after the split face lies on an axis parallel to the crank or to the cylinders, so one HMC setup with 90-degree indexing reaches it. The pan-rail face is machined in setup A and locates setup B. | 9.5 #2 |
| DR-4 | Head: every machined axis is normal to the head's long axis; the valve axes are parallel. | 9.5 #4 |
| DR-5 | Head: symmetric under a 180-degree rotation about the vertical axis (stud pattern, ring dowels, a coolant boss at each end), so one part number serves both banks. | 9.5 #3 |
| DR-6 | Drilled runs no longer than 25 x D from their entry face; main gallery 14 mm; at least 5 mm of metal from any oil passage to a coolant jacket; threaded, sealed, staked plugs, no cup plugs on pressure. | 9.5 #6, plus the merge |
| DR-7 | Every printed core has at least two exits of 12 mm or more; exits close with threaded plugs, never Welch or cup plugs. | 9.5 #7 |
| DR-8 | Every structural casting is radiographed before first-op, and its jacket pressure-tested before liners are fitted. | the merge |
| DR-9 | Case halves A357-T6, heads A356-T6, degassed, T6 with a certificate, impregnated after machining. | envelope 1.2, RANKING_PHASE1.md section 10 |

## 6. The 200 hp cost floor, rerun on both bases

`castings_h.py`. Low / mid / high; mid is the geometric mean of the band, as in phases 1 and 1b. Step 1 reproduces `cost_v1.py` (AER-3329) exactly on both bases.

| Step | Basis 1: first engine, carries all NRE | Basis 2: each engine of 5, NRE paid once |
|---|---|---|
| 0. Phase 1 as published | $23.2k / $36.8k / $58.4k | $23.2k / $36.8k / $58.4k |
| 1. Envelope 9.7 line items, six castings (= RECOST_PHASE1B "H as sent") | $35.8k / $55.9k / $87.3k | $26.7k / $38.1k / $54.5k |
| 2. + rulings 1-4: four castings, three part numbers, 4-axis head, STEP boxes | $32.0k / $48.7k / $74.1k | $25.5k / $35.9k / $50.6k |
| **3. + the machine-shop double count removed** | **$31.7k / $48.0k / $72.8k** | **$25.1k / $35.2k / $49.3k** |

- **Program NRE on basis 2:** $5.1k-19.2k once (CAM programs and fixtures for three part numbers), down from $7.2k-26.7k for six castings. Spread over five engines instead of carried by the program, basis 2 becomes $26.1k-53.2k per engine.
- **The machine-shop double count (step 3)** is a correction, not a ruling. Phase 0's `MACHINE_SHOP` line ($0.8k-2.0k x 1.3) was built from the align hone, two decks, six bores and hones, valve work and balancing. Since then the bore and hone moved into the liner line (9.4), the balance into the crank line (9.4), the valve work was already carried in the seats-and-guides line, and the decks moved into first-op (9.7). Only the align hone is left: $350-570. Phase 1b's figures carry the same double count, of about $0.3k-1.3k.
- **Against phase 1b's DFM variant** ($25.8k / $34.5k at the low end, items 1 and 4 only): the one-part-number head and the STEP boxes take another $0.3k (basis 2) to $2.5k (basis 1) off the low end. The NRE falls by $2.1k-7.9k, because phase 1b kept two head programs.
- **What still dominates:** on basis 1, first-op ($7.2k-24.4k), because one engine pays for every CAM program and fixture. On basis 2, the crank ($6.6k-9.4k), then castings ($4.1k-8.4k) and the catalog per-cylinder set ($2.7k-4.5k). Full line items: `castings_h_tables.md`.

**F-5 is still a miss on both bases.** This pass does not change the card on AER-3329 or Bill's basis question on AER-3330. It moves the numbers both are about.

## 7. Failure ledger

Added to `FAILURE_LEDGER.md`: **FL-38**, coolant into the oil through the merged case half, and **FL-39**, loss of a head jacket plug. FL-34 is reworded, because there is no longer a separate block jacket.

## 8. What this pass did not do

- **No quotes.** Every cost line is still [E]. The STEP files are what an RFQ needs (envelope 9.6). Who sends it is the AER-3330 question.
- **No Darton MID preparation drawing.** Register diameters, the flange seat and the coolant transfer passages are placeholders until Darton's drawing is in hand [Q]. The MID sleeve length is also unpublished. The 180 mm length, and the skirt's clearance to the crank counterweights, are open until the crank is drawn.
- **No crank drawing.** The 38.6 mm bank offset and the 14.6 mm webs come from a catalog-class rod (LS, 0.940 in big end) and 20 mm main bearings [E]. The crank drawing could move the cylinder positions by a few millimetres.
- **No FEA.** The merged case's bulkheads and bank are drawn to casting-rule walls, not to stress. The first structural check is the main bulkhead under firing load plus propeller gyroscopic moment, on the doweled pair.
- **Scrap rate** is assumed (5-20 % per pour). No bureau publishes a one-off rate.
- **The mass credit for the merge** (the two flange pairs and studs it deletes, about 2-3 kg [E]) is not taken in H's 148-158 kg. It is smaller than the band.
