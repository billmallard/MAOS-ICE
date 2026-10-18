# Concept H crankshaft: catalog crank or one-off, and the H-301 drawing

Owner: PROPULSION. Issue: AER-3439 (raised by MANUFACTURING, AER-3384; costs from AER-3412). Date: 2026-10-18.
Status: **a recommendation and a Rev A quoting drawing. Nothing here has been made, measured or run.** This is an experimental engine design. Nothing in it is certified, certifiable or flight-ready. Bill declares any freeze.

Numbers come from [`analysis/engine_crank/crank_decision.py`](../../analysis/engine_crank/crank_decision.py) (tables in `crank_decision_tables.md`) and the crank model from [`cad/concept_h/h_crank.py`](../../cad/concept_h/h_crank.py). Both read one parameter file, [`cad/concept_h/h301_params.json`](../../cad/concept_h/h301_params.json). Tags: **[S]** sourced (URL and read date in [`sources/CRANK_SOURCES_2026-10-18.md`](sources/CRANK_SOURCES_2026-10-18.md), addendum), **[E]** PROPULSION estimate with its method in the script, **[A]** assumed, **[Q]** needs a quote or a vendor drawing. **None of these figures is a quote.**

![H-301 crankshaft: side view with cylinder 1 at TDC, end view from the rear with pin angles, shaded view, and the drawing notes](../../cad/concept_h/H-301_drawing.png)

*H-301 Rev A. Side view with cylinder 1 at TDC; end view from the rear with each pin's angle; shaded view; the notes block carries material, journals, fillets, nitriding, runout, oil, balance and inspection.*

## 1. The answer

1. **The adapted catalog billet does not fit concept H, and no adaptation can make it fit.** A 2JZ or RB26 billet is an inline-6 crank. Its throws come in mirror pairs (0 / 120 / 240 / 240 / 120 / 0 degrees), so it has three pin angles. H's opposed six needs six. On H's alternating banks, the inline-6 throws put the six TDCs 60 degrees apart, and **no even firing order exists**. Every one of the 20 three-and-three bank assignments was enumerated and none fires evenly (section 2). The catalog strokes are also wrong: 86, 94 or 96 mm [S] against 101.6. Pin spacing is one per bore, there are 7 mains, and the front end is a flywheel flange. Re-indexing a finished crank's pins is not a machining operation. Using that crank means building a different engine, an inline-6, not adapting H.
2. **A third candidate came out of AER-3412 and it does fit: the Continental O-470 / IO-520 crank.** It is an opposed six with 4 mains and H's exact 4.000 in stroke. It has an integral propeller flange and 4th-, 5th- and 6th-order pendulum dampers [S, Continental IO-520 overhaul manual]. **It is not cheaper.** A new O-470R crank is $11,924 (MSRP $17,626) [S], and a yellow-tagged used one is listed at $8,500 [S, snippet]. MANUFACTURING's $2k-7k band is not supported by any price found. It would also force H's case onto Continental's main spacing (not found), and its 2.250 in pins rule out catalog LS rods. It is the torsional reference here, not the pick.
3. **Recommendation: a one-off billet to drawing H-301, from a crank specialist.** **$6.6k-9.4k including balance [E, envelope 9.4], about 18-20 weeks [S, reseller figure].** Quote route 5 (general turn-mill shop, $7k-19k, 6-12 weeks [E, AER-3412]) to the same drawing as the lead-time alternate. If Bill takes the geared EZ36 variant on AER-3411, its $524 OE crank replaces this one, and H-301 becomes the fallback.
4. **Two changes to concept H come with the drawing, both found by drawing the crank.**
   - **Bank pitch 111.8 to 122.0 mm** (section 3). At 111.8 mm, two separate pins per bay leave 13.9 mm webs. On the same split-at-the-mains method, that is 1.7x the web bending stress of a cast LS crank, which leaves only the same fatigue margin as that crank (ratio 1.02). At 122 mm the webs are 17.3 mm and the margin is 1.45x the LS crank's. The case and crank grow by 31 mm.
   - **The LS7 rod-and-liner stack does not clear a staggered opposed crank** (section 6). At BDC the opposed rod's big end and the middle web reach into the other bank's piston. The overlap is 8-9 mm on a relieved-skirt model and up to 20 mm on a full-skirt one. The web ends and big ends also sweep 5-6 mm through the bottom of the Darton liner. **Neither is a crank feature.** The fix is a longer rod (6.360 in, a catalog length [S, snippet], raises the deck 7.4 mm and comes within about 1 mm), or relief cuts in the liner bottom and skirt, or both. It needs real rod and piston drawings [Q]. The counterweights are not the problem: at R62 they clear by 11 mm even on the full-skirt model.
5. **Torsion: fit a viscous damper on the rear snout.** With the geometry drawn, mode 1 is **255 Hz**. Its 6th-order crossing is at **2,549 rpm, in the cruise band** (FL-24 stands). Undamped, the worst nominal vibratory shear in the journal is **33 MPa**, against a 34 MPa yardstick (IACS M68 form, with an oil-hole factor [E]). It is **66 MPa if the crank's damping is half the assumed value**. A catalog-class viscous damper on the free (rear) end holds the worst case to **7 MPa** across every sensitivity case. Pendulums at the rear give 13 MPa. Pendulums at the propeller end do nothing, because that end is a node (section 4).

## 2. Deciding physics 1: what the crank can fire

`crank_decision.py` section 1. A cylinder reaches TDC when its pin points at its own bank. Even firing for a four-stroke six needs the TDCs, taken mod 360, to fall in three pairs 120 degrees apart. Each pair fires 360 degrees apart.

| Crank on H's L R L R L R banks | TDC mod 360, cylinders 1-6 | Even 120-degree orders |
|---|---|---|
| H-301 boxer throws: pairs 180 apart, bays at 0 / 240 / 120 | 0, 0, 240, 240, 120, 120 | 8. **1-6-3-2-5-4** chosen: it alternates banks, so each bank fires every 240 degrees |
| Inline-6 catalog throws (2JZ, RB26) | 0, 300, 240, 60, 120, 180 | **none** |
| Inline-6 throws, any 3 + 3 bank assignment | | **none of 20** |

The H-301 throws leave no free primary or secondary force or couple (machine zero, section 1 of the tables), as expected for an opposed six. **So the crank balances alone, with no bob weight**, provided rods are matched end for end and pistons by weight across each opposed pair.

## 3. Deciding physics 2: the webs at H's pitch

`crank_decision.py` section 3. Method: each bay is simply supported at its two mains, one rod fires at a design load of 70 bar [A] (60.4 kN), and the nominal bending stress is taken at the web next to the nearer main. The method over-predicts absolute stress, so it is used as a **ratio to a crank that runs**: a cast-iron GM LS crank at 80 bar [A] (155 MPa on the same method). Nitrided 4340 has 1.75x pearlitic ductile iron's fatigue strength (CRANK_AND_SCALING 3.3).

| Bank pitch (mm) | Webs (mm) | Longer by (mm) | Web stress (MPa) | Margin vs a cast LS crank |
|---|---|---|---|---|
| 111.8 (as drawn in H-101/102) | 13.9 | 0 | 266 | 1.02 |
| 118.0 | 15.9 | 19 | 212 | 1.28 |
| **122.0 (H-301)** | **17.3** | **31** | **187** | **1.45** |
| 128.0 | 19.3 | 49 | 158 | 1.72 |

At 111.8 mm H's crank would carry, continuously, the margin a car crank has only at full throttle. 122 mm is my pick: it buys 45 % more margin than the LS reference for 31 mm of length, about 2-3 kg of case and crank [E]. It also opens the gap between liners from 7.0 mm to about 17 mm, which helps the coolant jacket. The cycle model puts H's peak pressure at 51 bar, against the 70 bar design load, so the absolute margin is larger than the table shows. The table is not a stress analysis. FEA of a throw is open (section 8).

## 4. Deciding physics 3: torsion, H-301 at 122 mm

`crank_decision.py` section 4. A 9-mass chain: propeller, nose, six throws, and the rear (cam gear and accessory drive). **Stiffness comes from Carter's equivalent length** (Ker Wilson) on the drawn journals, pins and webs, split into a term per feature. Phase 1 assumed its stiffnesses. **Excitation** is the gas plus reciprocating inertia torque of one cylinder from a single-zone Wiebe cycle scaled to H's IMEP (12.1 bar, peak 51 bar, indicated torque 507 N m against 508 needed). It is phased by firing order and swept at full throttle along the fixed-pitch propeller curve. **Damping:** crank loss factor 0.04 [A], plus the propeller's aerodynamic damping.

- **Modes 255 / 705 / 1,147 Hz.** Phase 1's assumed chain gave 261 / 768 / 1,274, so the drawn geometry confirms it. The mode-1 shape runs -0.05 at the propeller to 1.00 at the rear: **the propeller is a near-node and the rear end swings most.**
- **Mode-1 crossings between 1,000 rpm and 120 % of rated:** order 6 (major) at **2,549 rpm**, order 9 (major) at 1,700, order 7.5 at 2,040, and order 4.5 at 3,399.

| Option | Worst nominal shear, 1,000-3,465 rpm | At |
|---|---|---|
| no damper | **33.2 MPa** | 2,550 rpm (6th order) |
| **viscous damper on the rear snout** (ring 0.035 kg m^2 [A], damping tuned by sweep) | **7.3 MPa** | 3,300 rpm, off-resonance |
| two 6th-order pendulums on bay 3 (rear) | 13.2 MPa | 1,325 rpm |
| two 6th-order pendulums on bay 1 (propeller end) | 32.0 MPa | 2,275 rpm |

| Sensitivity | Mode 1 | No damper | Viscous damper |
|---|---|---|---|
| baseline | 255 Hz | 33.2 MPa | 7.3 MPa |
| crank stiffness x0.8 / x1.2 | 233 / 274 Hz | 28.1 / 37.7 | 7.7 / 7.3 |
| loss factor 0.02 | 255 Hz | **65.7** | 7.4 |
| propeller 0.6 / 2.5 kg m^2 | 260 / 250 Hz | 32.0 / 34.3 | 7.0 / 7.6 |

**The TV case for H-301, stated:** without a damper the 6th-order resonance sits in cruise, at the yardstick, and doubles if damping is lower than assumed. That is FL-24 with geometry behind it. **A rear viscous damper takes the worst case to about a fifth of the yardstick and makes it insensitive to every uncertainty swept.** It treats all orders and modes at once. It is one bought, bolt-on part instead of pendulums, pins and bushings machined into the crank. The rear is where the mode swings, and where H has room. The yardstick is a shaft rule used as a guide, not a crank rule, and the stresses are nominal: fillet and oil-hole concentrations sit on top of them.

**Why not Continental's pendulums?** They work. The model's 6th-order pendulum needs an effective length of 2.0 mm, and Continental's 6th-order pin in its bushing bore gives 1.7-1.8 mm [S], a match that suggests the model is sound. But a pendulum treats one order. At the rear it holds 13 MPa, not 7. It also adds machined blades, bushings, pins and an inspection item (FL-25). The drawing reserves no pendulum blades, so choosing them later would mean a Rev B.

**What would prove it:** a dynamometer torsional survey (angular velocity at the free end, order-tracked), run with and without the damper, before flight. It is the only test that turns these numbers into evidence.

## 5. The H-301 specification, against the 10 rfq-package-v1 items

The Rev A print is `cad/concept_h/H-301_drawing.png`. The solid is `cad/concept_h/H-301.step` (one valid solid, model mass **24.6 kg**, 531 mm overall; CRANK_AND_SCALING's independent estimate was about 24 kg). Engine frame: x from the case front face toward the rear, +z the LH bank, cylinder 1 at TDC.

| # | rfq item | H-301 Rev A | Basis |
|---|---|---|---|
| 1 | Throw layout and phasing | 6 throws, 3 bays, LH rod forward in each bay. Pins at 0 / 180 / 240 / 60 / 120 / 300 degrees against rotation from P1 (P1-P6). Rotation clockwise seen from the rear. Firing **1-6-3-2-5-4**. **Bank offset 41.4 mm** (was 38.6) | section 2 |
| 2 | Main journals | **4 x 60.00 mm** (-0.013 / -0.025 [E]; final to the shell maker's table [Q]). Width 22; M1 26 with the thrust faces. **Spacing 122.0** (M1-M4 at x 60, 182, 304, 426) | section 3. A 60 mm main shell is still unconfirmed (envelope 9.4). Continental's 2.375 in (60.3 mm) mains are a fallback size |
| 3 | Rod journal | **53.34 mm (2.100 in) x 24.1 mm wide**, one LS rod per pin. Rod **154.1 mm (6.067 in) as drawn; 6.360 in proposed** (section 6). Pin 0.927 in [S] | catalog LS rods [S] |
| 4 | Counterweights against the liner skirt | Counterweights on the six outer webs, **R62 over +/-55 degrees**. **Envelope R70** (3 mm on a full-skirt model), R80 on a relieved one. The interference found is rod, web and piston against the stack, not counterweight (section 6) | swept clearance, Darton sleeve 147.3 mm [S] |
| 5 | Thrust | Thrust faces on both sides of M1, ground; end float 0.10-0.25 mm [E] on flanged thrust shells [Q]. Load: tractor thrust about 2.3 kN static [E, DRIVE_AND_PROP] | |
| 6 | Propeller flange | **Lycoming Type 2 pattern: 6 bushings on 4.750 in (120.65 mm)** [S, SI 1098Q]. Bores 19.82 mm for **72060-S bushings** (OD 0.7818-0.7823 in, 0.0005-0.0020 in tight [S]). Flange 0.44 in (11.11 mm) thick [S, the O-540 class]. OD 146 [E]. Pilot 60 x 12 **[Q, from the propeller vendor's hub drawing]**. Face runout 0.05 mm FIR [E] (Continental's service limit is 0.005 in [S]). Solid nose: no oil to the propeller (option 3b is ground-adjustable; an electric pitch hub needs none) | |
| 7 | Rear snout | Cam-gear seat 50 x 30, the gear shrunk on and driven by a dowel (Continental's practice [S]). Reluctor seat 46 x 12, one wheel read by both FADEC lanes' sensors. **Damper flange 110 OD, 6 x M10 on 90, pilot 60** | section 4 |
| 8 | Oil drilling | One straight 6 mm drilling per pin from its nearer main: P1/P3/P5 from the bay's front main, P2/P4/P6 from its rear main. Enters the main 90 degrees behind the pin, exits the pin 60 degrees ahead of its outermost point [E]. Ends broken and polished, **no plugs**. Exit angle checked against the bearing load polar at Rev B | |
| 9 | Fillets, treatment, material, balance | **R3 fillets** on every journal, ground in form, no undercut; journals Ra 0.2 um, fillets Ra 0.4 um. **4340 VAR, AMS 6414**, quench and temper to 28-32 HRC core; **quote AMS 6415 air-melt as an alternate** (MANUFACTURING: it moves the bar line by $2k-4k). Gas nitride after finish grind: case 0.30-0.50 mm, compound layer 5 um or less on journals, micropolish. MPI (ASTM E1444) after roughing and after nitriding. **Balance the crank alone, no bob weight**, ISO 21940-11 G2.5 at 3,300 rpm [E] | sections 2, 4; envelope 9.4 |
| 10 | Torsional check and damper | Done (section 4). **Viscous damper on the rear flange**; the propeller end needs no damper snout. Damper itself: a catalog automotive viscous damper class, 0.035 kg m^2 ring [A], **$0.4k-0.9k [E, needs-quote]**, 3-5 kg [E], machined to the 60 mm pilot | section 4 |

**What a crank shop still needs that is not on this sheet:** a dimensioned 2-D release print. Rev A is a quoting print, as Bryant's form and MANUFACTURING's checklist ask. It is not a production drawing. Shops quote custom cranks from "prints and/or specifications" [S, rfq-package-v1], and this sheet plus the STEP is that specification.

## 6. Finding: the LS7 stack against a staggered opposed crank

`crank_decision.py` section 6 sweeps the crank, both rods' big ends (42 mm radius about the pin [A]), the webs and the counterweights through 720 degrees. It checks them against every piston and liner bottom. The liner bottom is 87.7 mm from the axis: the deck at 235 mm, less Darton's 147.3 mm sleeve. Two piston models are used, because no catalog piston drawing is in hand. The **disc** model is the full bore down to 30 mm below the gudgeon pin [A]. The **relieved** model has skirt panels on the thrust sides only, and pin bosses [A].

| Feature | Against | Disc (mm) | Relieved (mm) |
|---|---|---|---|
| middle web | other bank's piston at BDC | -20.0 | -9.0 |
| opposed rod big end | other bank's piston at BDC | -19.5 | -8.6 |
| web ends | liner bottom | -5.6 | -5.6 |
| opposed rod big end | liner bottom | -5.1 | -5.1 |
| counterweights (R62) | piston | +11.3 | +23.3 |

**Why it happens:** in each bay the two pins are 180 degrees apart, so when one cylinder is at BDC its opposed partner's pin, middle web and big end swing toward it. The bank offset (41.4 mm) is inside the bore radius (52.4 mm), and the LS7's 6.067 in rod puts the BDC gudgeon pin only 103 mm from the axis. Continental's pistons carry "cylindrical relief cuts at the bottom to clear the crankshaft counterweights" [S, IO-520 manual], so the problem is a known one in this layout.

| Rod (in) | Deck rise (mm) | Piston gap, relieved (mm) | Liner gap (mm) | Catalog, 2.100 in journal |
|---|---|---|---|---|
| 6.067 | 0 | -8.4 | -5.6 | LS7 |
| 6.200 | 3.4 | -5.0 | -2.2 | Eagle ESP [S] |
| **6.360** | **7.4** | **-0.9** | **+1.8** | Speedmaster [S, snippet] |
| 6.460 | 10.0 | +1.6 | +4.4 | not found |

**Proposed:** a 6.360 in rod and a deck 7.4 mm higher, with skirt and liner-bottom relief taken from the real piston and rod drawings to reach 3 mm. A longer rod also lowers the side thrust. The cost is 7.4 mm per side of case height and a piston chosen for the new deck. **This changes H-101, H-102 and the cylinder module, not the crank**, so it goes to a castings revision (section 8), not to H-301.

## 7. Failure ledger

Added **FL-50**: the rear viscous damper loses its fluid or degrades. FL-24's 6th-order resonance then returns at about 2,550 rpm, 33-66 MPa nominal, with no cockpit cue. Mitigation: a damper inspection and replacement interval, and a dynamometer survey with and without the damper so the undamped margin is known. Section 6 is a design finding, not a service failure. An engine assembled without the fix would lock on its first hand rotation.

## 8. What this pass did not do, and what is open

- **No quotes.** The crank RFQ (rfq-package-v1 section 4) can now be written against H-301 Rev A. Sending it waits on AER-3330/AER-3333 (Bill: who sends RFQs).
- **The castings do not yet match H-301.** H-101/H-102/H-201 are at the 111.8 mm pitch and the 235 mm deck. They need regenerating at 122 mm, and at a deck set by the rod-and-piston pick. Those STEP files are what rfq-package-v1 is pinned to (MAOS-ICE `e062428`), so **MANUFACTURING's casting and first-op RFQ drafts are superseded on pitch and deck** until that revision lands. Follow-up: AER-3442. *Done on AER-3442: the castings are at 122 mm and a 246 mm deck, with a 6.560 in rod (CASTINGS_H.md section 9, `analysis/engine_crank/stack_h.py`).*
- **No FEA, no main-bearing load polar, no oil-film check.** The web check is a comparative sanity check. The 22 mm main width and the oil-hole exits are [E] until the bearing load polar is run.
- **Assumed and not found:** the LS7 rod's big-end envelope and piston skirt profile; a catalog 60 mm main shell; the propeller pilot diameter; the viscous damper's real inertia and price; Continental's main spacing.
- **The Continental crank prices are two listings and a snippet.** A survey of real used-crank prices (MANUFACTURING's item 4 on AER-3412) would settle the fallback. A $250 as-is core [S, snippet] is the cheapest way to measure one.
