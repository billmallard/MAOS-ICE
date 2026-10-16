# Engine phase 1b: concept H re-costed on MANUFACTURING's estimates, the $22k test, and the normalizer

Owner: PROPULSION. Issue: AER-3329 (follows AER-3326; inputs from AER-3328). Date: 2026-10-16.
Status: **analysis pass. Nothing here has been built, run or tested.** This is an experimental engine design. Nothing in it is certified, certifiable or flight-ready.

Every number comes from a script in `analysis/engine_phase1/` (rerun commands in its README) or from MANUFACTURING envelope v1 (`MANUFACTURING_ENVELOPE.md` sections 9 and 10), unless another source is named.

**Read this first: these are estimates, not quotes.** The issue asked for the [Q] lines to be replaced with quoted figures. MANUFACTURING delivered bottom-up estimates [E] built on sourced shop rates [S] instead, because there is no STEP geometry and no one holds a channel to send an RFQ (envelope 9.6; AER-3330). Every v1 line below is therefore [E]. The conclusions that survive that are stated as such. The ones that do not wait on the quote.

## 1. The answer

1. **The pick holds: concept H over concept A.** The ranking order did not change in any basis or variant (section 4). The matrix still calls it a tie. It now leans a little further toward A under ratio normalization, and H still leads under min-max.
2. **$22k is missed, on both readings of "first article".** H's low end rises from $23.2k to **$26.7k** if a builder pays and the program carries the tooling, and to **$35.8k** if the very first engine carries the tooling. With MANUFACTURING's two biggest DFM levers taken it is $25.8k and $34.5k. **No auto-gas candidate meets $22k even at the low end of its band**, and deleting the normalizer and the second ignition lane still leaves $23.5k. That miss does not depend on the quote: the quote would have to come in below MANUFACTURING's bottom-up low end on every line. F-5 goes to Bill as a card (section 5).
3. **The turbocharger stays.** On the sourced hardware a fixed-ratio supercharger loses its boost with crank rpm. With the ground-adjustable propeller, which does not hold rpm in a climb, it leaves **74 % of 200 hp in a 12,000 ft climb, against 94 % for the turbo** (section 6). It costs about the same and is 2-5 kg lighter.
4. **No envelope is outside MANUFACTURING's process envelope**, so item 4 of the issue (redraw what it flags) has nothing to redraw. Its seven DFM objections are design levers, not rejections. They are ruled on in AER-3331, with the coarse STEP. Here, items 1 and 4 are costed as a variant.
5. **Mass moved up.** The only catalog wet liner (Darton MID) adds 9-11 kg. The sourced normalizer runs 5-12 kg over the phase-0 allowance. Together they put H at **about 148-158 kg installed dry, against 134 kg in phase 1 and the proposed 150 kg** (section 7).

## 2. What changed in the inputs

| Line, 200 hp member | Phase 1 model | v1, builder basis | v1, first engine | Source |
|---|---|---|---|---|
| First-op machining, 6 castings | $3.0k-12.0k | $1.7k-4.6k | $9.8k-33.9k | envelope 9.3 [E on S rates] |
| Castings: mold, pour, T6, impregnation, RT | $4.4k-10.9k | $5.1k-11.2k | $6.2k-14.7k | envelope 9.3 [E on S sand rate] |
| Program tooling (CAM + fixtures), paid once | not carried | $7.2k-26.7k, outside the per-engine number | inside first-op above | envelope 9.3 [E] |
| Crank, one-off flat-6 billet + balance | $3.9k-7.2k | $6.6k-9.4k | same | envelope 9.4 [E on S anchors] |
| Liners, 6, incl. bore and hone | $0.9k-2.4k | $1.8k-2.7k | same | envelope 9.4 [E on S] |
| Normalizing: turbo, gate control, intercooler | $1.2k-3.0k | $2.0k-4.5k | same | envelope 10 [S prices, E install] |
| Machine shop | $1.0k-2.6k | less the two block decks, now in first-op | same | envelope 9.7 |

The builder basis is each engine of a batch of five, with the tooling bought once by the program and carried as its own line. The first-engine basis puts every CAM program and fixture on one engine. Which one R-35 means is Bill's question on AER-3330. This document reports both.

## 3. The 200 hp cost floor, v1

`cost_v1.py`. Low / mid / high; the mid is the geometric mean of the band, as in phase 1.

| Variant | Phase 1 | v1, builder basis | v1, first engine | Program tooling, once |
|---|---|---|---|---|
| **H as sent** (6 castings) | $23.2k / $36.8k / $58.4k | **$26.7k / $38.1k / $54.5k** | $35.8k / $55.9k / $87.3k | $7.2k-26.7k |
| **H with DFM items 1 + 4** (bank merged into the case half; 4-axis head; 4 castings) | | **$25.8k / $36.3k / $51.1k** | $34.5k / $53.5k / $82.7k | $7.2k-27.1k |
| A (8 castings; casting envelopes PROPOSED, scaled from H's) | $22.6k / $36.5k / $58.9k | $24.7k / $35.8k / $51.7k | $31.8k / $49.1k / $76.0k | $5.0k-17.9k |
| A with its Lycoming pistons priced | | $25.4k / $37.0k / $53.7k | $32.5k / $50.3k / $77.9k | $5.0k-17.9k |

How to read it:

- **The low end rises about $3.5k**, as MANUFACTURING said it would (envelope 9.7). First-op falls on the builder basis. The crank (+$2.7k), the liners (+$0.9k), the castings (+$0.7k) and the normalizer (+$0.8k) all rise.
- **The high end falls** on the builder basis, by $4k, because the first-op band narrowed from a guess to an operation-by-operation estimate.
- **The DFM levers are worth $0.9k at the low end and $1.8k at the mid.** That is the block merge (2 castings, 2 gaskets and 16-24 studs fewer) and a 4-axis head ($60-90/h instead of $100-200/h on its second setup). The full line items are in `cost_v1_tables.md`.
- **A's pistons, priced.** Phase 1 gave A the LS-class catalog price, which it named as flattering A. Aircraft Spruce lists 5.125 in Lycoming pistons at **$460-639 each** (read 2026-10-16), against **$155-280** for the Wiseco LS piston (envelope 4). That is a premium of $180-484 per cylinder, before rings. Lycoming rings are sold singly, at $60-184 each, so the premium shown is low.
- **Concept A's casting envelopes are mine, not MANUFACTURING's.** They are H's envelopes scaled to a flat-4 with a 130 mm bore: case half 480 x 330 x 180 mm, two 2-cylinder bank blocks, and four single-cylinder heads of one part number. They are good enough to compare against H, not to quote.

## 4. Does H over A still hold?

`rank_v1.py` reruns the phase-1 matrix: same weights, both normalizations, and the same Monte Carlo over weights. A and H are re-costed. H carries the Darton liner mass and, in the DFM variant, the block-merge part count. B, C, D and G were not re-estimated, so they are scaled by the mean v1 / phase-1 ratio of A and H (ASSUMED). Under ratio normalization a common factor changes nothing.

| Case (A's pistons priced) | Ratio-to-best order | First place, centred / flat draws | Min-max order | First place, centred / flat draws |
|---|---|---|---|---|
| Phase 1 (for reference) | A 9.01, H 8.82 | A 69 / 57 %; H 24 / 31 % | H 7.20, A 6.35 | H 67 / 51 %; A 9 / 15 % |
| Builder basis, H as sent | A 9.00, H 8.67 | A 81 / 65 %; H 9 / 19 % | H 6.81, A 6.33 | H 47 / 39 %; G 27 / 24 % |
| Builder basis, H with DFM 1 + 4 | A 8.94, H 8.74 | A 70 / 59 %; H 18 / 25 % | H 6.94, G 6.24, A 6.22 | H 58 / 44 % |
| First engine, H as sent | A 9.09, H 8.61 | | H 6.66, A 6.52 | |
| First engine, H with DFM 1 + 4 | A 9.04, H 8.67 | | H 6.78, A 6.42 | |

The full tables, including both cases with A's pistons at the LS price, are in `rank_v1_tables.md`.

**The order holds everywhere: A first under ratio, H first under min-max.** The matrix moved toward A under ratio normalization, because H's crank, liners and extra casting area all rose and its Darton liners added mass. Min-max moved the other way once the DFM levers were taken.

Phase 1 named three things that would flip the pick back to A (RANKING_PHASE1.md section 4). Against each:

1. **"The extra cylinder-bank casting area costs more than A's aviation pistons."** It does not. On the builder basis, with A's pistons priced, H as sent costs $1.1k more than A at the mid estimate, and H with the DFM levers costs **$0.7k less**. As sent it is within the band of the piston rings A's premium leaves out.
2. **"The 6th-order crossing cannot be moved or damped with a catalog-class part."** Not tested this pass. It is still the open risk on H (FL-24).
3. **"Bill weighs noise and part count above mass."** Not asked.

H keeps the four reasons phase 1 gave, outside the matrix: a flown analog (UL520iS), the mass (now about 153 kg against A's 183 kg plus the same normalizer growth), the LS piston catalog, and 3 points of knock margin.

## 5. The $22k test (R-35, F-5): a miss on both readings

| Variant | Builder basis, low / mid | First engine, low / mid |
|---|---|---|
| H as sent | $26.7k / $38.1k: **$4.7k over** at the low end | $35.8k / $55.9k: $13.8k over |
| H with DFM 1 + 4 | $25.8k / $36.3k: **$3.8k over** | $34.5k / $53.5k: $12.5k over |
| A, pistons priced | $25.4k / $37.0k: $3.4k over | $32.5k / $50.3k: $10.5k over |

**Why this is a miss now, not a wait for the quote.** To reach $22k, every line would have to come in $4k below MANUFACTURING's bottom-up low end, and that low end is built on the bottom of sourced shop-rate bands. A quote can confirm the low end. It is very unlikely to beat it by 15 %.

**What holding $22k would take** (H with the DFM levers, builder basis; `cost_v1.py`):

| Deletion | Low end | What it costs the brief |
|---|---|---|
| none | $25.8k | |
| delete the normalizer (turbo, gate, intercooler) | $23.8k | ruling 3 fails: about 65 % power at 12,000 ft, 76 % at 8,000 ft (Gagg-Ferrar) |
| and delete the second ignition lane | $23.5k | R-25 fails |

Even with both deletions the low end misses. **No cast-from-files engine meets $22k on this cost basis.** Holding $22k means giving up the premise, for example by moving to an automotive conversion, which the brief excludes.

**What relaxing $22k buys,** for the card:

- **Dollars.** A target of about **$30k per builder** passes H's low end ($25.8k) with $4k to spare. It needs the quotes to land in the lower part of the band, because the mid is $36.3k. A target that the mid passes would be about **$37k**.
- **Parts.** It keeps H as ranked: 6 cylinders, about 338 non-fastener parts and 86 part numbers (the merge takes 4 off 342), dual-lane ignition and a normalizer.
- **Mass.** It keeps H at about 148-158 kg installed dry, normalized to 12,000 ft. The cheapest way back toward $22k, deleting the normalizer, saves about 14-21 kg but gives up a third of the power at 12,000 ft.
- **The program tooling ($7.2k-27.1k) is a separate line** on the builder basis. If the first engine has to carry it, no target under about $35k is honest.

**The 300 hp target follows.** Ruling 2 set 300 hp at $30k. If 200 hp needs about $30k, a 300 hp member on a second, larger module will not fit under $30k. That is phase 2 work. It is stated here so the card does not imply 300 hp is unaffected.

## 6. Turbocharger or supercharger, on the sourced hardware

`normalizer_h.py`. Hardware from envelope 10: a Garrett GT2860RS / GTX2860R-class turbo with an internal wastegate, or a Rotrex C30-94 centrifugal supercharger on a fixed belt step-up. The Rotrex is the only catalog supercharger that fits the duty. Both feed the same intercooler.

### 6.1 The duty

| Case, 200 hp at 3,300 rpm | Pressure ratio | Compressor power, eta 0.72 / 0.60 | Compressor outlet, eta 0.72 / 0.60 | Corrected flow |
|---|---|---|---|---|
| Sea level, ISA | 1.06 | 1.0 / 1.2 kW | 21 / 23 C | 21.2 lb/min |
| 8,000 ft, ISA+20 | 1.43 | 7.1 / 8.5 kW | 63 / 72 C | 28.7 lb/min |
| 12,000 ft, ISA | 1.68 | 9.5 / 11.3 kW | 50 / 62 C | 31.9 lb/min |
| 12,000 ft, ISA+20 | 1.68 | 10.2 / 12.2 kW | 74 / 87 C | 33.1 lb/min |

This agrees with MANUFACTURING's 10-11 kW (envelope 10.3) and with phase 1's 76 C compressor outlet.

**The compressor map is not checked.** No digitized GT2860RS map was available. 33 lb/min at a pressure ratio of 1.68 sits at the high-flow, low-pressure-ratio corner of a GT28-class map. One forum report puts about 30 lb/min on a GT28-class compressor near choke, in the 60 % island (shoforum.com, unverified). The 0.60 column is that case. If the map confirms it, the next frame size up (GTX2867R or GT3071R class) is the match, at about the same price. **This is open. I own it, and it needs Garrett's published map overlaid on these four points.**

### 6.2 The trade

| | Turbocharger (GT2860RS class) | Supercharger (Rotrex C30-94) |
|---|---|---|
| **Holds sea-level manifold pressure to 12,000 ft at 3,300 rpm** | yes | yes, by design ratio |
| **At lower rpm** | yes. The wastegate sets turbine speed from exhaust energy, not from crank rpm. | **no.** Boost head scales with rpm squared: at 12,000 ft the manifold falls to 0.91 bar at 3,000 rpm and 0.81 bar at 2,570 rpm |
| **Full-throttle climb, 80 kt, ground-adjustable propeller (ISA)** | **88 % at 8,000 ft, 94 % at 12,000 ft** | 81 % at 8,000 ft, **74 % at 12,000 ft** |
| Same, with no normalizer | 58 % at 8,000 ft, 49 % at 12,000 ft | |
| **Power cost** | at altitude, a pumping **gain** of 1-2 kW: the turbine inlet (0.90-0.95 bar) sits below the normalized manifold (1.00 bar). At sea level, with the gate open, 1.4-2.9 kW of back-pressure (1-2 %) | 10.7-12.8 kW of crank drive at 12,000 ft (7-9 %). At low altitude it must be throttled or bypassed; its drive cost there is not modelled (the table charges an upper bound) |
| **Mass, without the shared intercooler** | 10-15.5 kg [E]: unit 6-8 kg (envelope 10.1), actuator 0.5-1, oil and coolant lines 1-1.5, turbine manifold and collector beyond a plain exhaust 2-4, heat shields 0.5-1 | 8.4-10.6 kg [E]: unit 5.1 kg [S], belt, two pulleys, tensioner and bracket 2-3.5, bypass valve 0.3-0.5, traction-fluid tank and cooler 1-1.5 |
| **Heat** | turbine housing at about 800-900 C in the cowl: 2-4 kW to cowl air [E]. Bearing housing to oil and coolant, 1-3 kW [E]. Needs an after-run of the electric coolant pump to stop coking (envelope 10.1) | no hot section. Its 7-9 % extra brake power at altitude adds about 7-9 kW to coolant and oil. The radiator has about 20 % margin at 12,000 ft (RANKING_PHASE1.md section 8) |
| **Control** | one closed loop: the FADEC schedules the wastegate on manifold pressure. The fail-safe direction must be designed in (FL-30) | bypass valve plus throttle. Boost cannot be scheduled independently of rpm. Needs a declutch, or variable drive, to stop absorbing power at sea level |
| **Cost** (envelope 10) | $1.7k-3.9k + intercooler $0.3k-0.6k | $2.7k-3.8k, including the intercooler |
| **Failures** | wastegate stuck closed: overboost at low altitude. Stuck open: unboosted power. Bearing or seal: oil into the intake or the exhaust. Exhaust leak upstream of the turbine: a hot jet in the cowl (FL-30 to FL-32) | belt or traction drive: unboosted power, with belt debris at the crank nose. A belt drive also adds a branch to the crank's torsional system |
| **Flown in this class** | yes: turbocharged Rotax 914/915/916, and turbo-normalized Continental and Lycoming installations | no verified aircraft use of a Rotrex found (envelope 10.3) |

**Ruling: turbocharger.** The decider is the propeller. The baseline propeller is ground-adjustable, so it does not hold rpm in a climb, and a supercharger on a fixed ratio gives back its boost as rpm falls. With a constant-speed propeller held at 3,300 rpm, the supercharger would hold 1.00 bar to 12,000 ft and the trade would close to mass and heat. Even then it pays 7-9 % of rated power to drive the compressor, where the turbo pays nothing at altitude. **The supercharger's real advantage is no hot section to make, inspect or contain.** That is worth recording, and it is not enough.

**What the turbo pick still owes:** the compressor-map overlay (6.1); the fail-safe direction of the wastegate actuator (FL-30); and the turbine-housing heat in the cowl, once there is a cowl.

## 7. Mass: the sourced parts push H to about the proposed limit

| Item | Phase 1 | v1 | Source |
|---|---|---|---|
| H installed dry, phase 1 | 134 kg | | `member_200.py` |
| Darton MID wet liners: 6 x 2.5-3 kg of iron, net of the aluminium they displace | in the jacket allowance | +9.4 to +11.2 kg | envelope 9.4 [E]; `cost_v1.py` |
| Normalizer: turbo system + intercooler | 9 kg allowance | 14-21.5 kg, so +5 to +12.5 kg | envelope 10 [E]; section 6 |
| **H installed dry, v1** | | **about 148-158 kg** (mid about 153 kg), +/-25 % | |

R-37's 150 kg is PROPOSED, not ruled, so this is a note, not a card. A's normalizer grows by the same amount, so the comparison with A (183 kg) holds. The lever back under 150 kg is the liner. A thin dry iron sleeve, about 2.5 mm wall, in a closed-deck block weighs about 1 kg per cylinder, not 2.5-3. It saves about 6-7 kg [E] for about the same installed cost, but it gives up the "liner sets the deck" simplicity. That choice is AER-3331's liner question.

## 8. Failure ledger

Added to `FAILURE_LEDGER.md`:

- **FL-30 to FL-32**, normalizer: the wastegate fail-safe direction, turbo bearing and seal failure, and an exhaust leak upstream of the turbine.
- **FL-33 to FL-37**, MANUFACTURING's build-quality items MFG-1 to MFG-5 (envelope 10.4).

## 9. What this pass did not do

- **No quotes.** Every v1 line is [E]. The quote decides how far into the band the cost lands. It does not decide the $22k miss (section 5).
- **No compressor-map overlay** (section 6.1).
- **Concept A's casting envelopes are PROPULSION's.** MANUFACTURING estimated only H's.
- **B, C, D and G were not re-costed.** They were scaled by a common factor, which does not change their ratio scores.
- **The DFM objections are costed, not ruled.** Items 1 and 4 are modelled as a variant. The rulings and the coarse STEP are AER-3331.
- **No torsional work.** FL-24 is unchanged.
- **The supercharger's sea-level unloading is not modelled.** It does not change the ruling, which rests on the altitude case.
