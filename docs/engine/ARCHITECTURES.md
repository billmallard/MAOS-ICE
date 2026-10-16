# Engine architectures, phase 0: the divergence pass

Owner: PROPULSION. Issue: AER-3320 (ORG-009, 2026-10-16). Status: **divergence pass.**

**These concepts are not ranked.** The order is the order they were written, and implies nothing. Ranking is phase 1, after Bill answers the phase-0 card.

None of this has been built, run or tested. Every mass, cost and power below is a physics floor or an extrapolation from analog engines, labeled as such. Nothing here is certified, certifiable or flight-ready.

## Method, once for all concepts

Every number in the concept tables comes from `analysis/engine_phase0/engine_floor.py` (physics) or `cost_floor.py` (cost), unless a source is named. Rerun commands are in `analysis/engine_phase0/README.md`.

**Power and size.**

- **BMEP**: P = BMEP x Vd x N / (60 k), with k = 2 for a 4-stroke and k = 1 for a 2-stroke or per rotor of a Wankel (Heywood ch. 2).
- **Mean piston speed**: Sp = 2 S N / 60.
- **Airflow check**: the implied sea-level volumetric efficiency (ηv) must land at or below about 0.97 for an unboosted engine. Every concept passes. Concept A, at 0.97, is at the edge.

**Fuel and the heat balance.**

- **Brake efficiency**: η_b = 3600 / (BSFC x LHV). Takeoff BSFC is 310 g/kWh for spark ignition (rich, E10 LHV 42.0 MJ/kg), 225 for a 4-stroke diesel, 215 for an opposed-piston 2-stroke and 340 for a Wankel. These are class values inside Heywood's ranges, **not** measured on these engines.
- **Heat split**: coolant and oil take fixed shares of fuel energy by cycle (Heywood ch. 12): spark ignition 24 % / 5 %, diesel 20 % / 6 %, opposed-piston 16 % / 7 %, Wankel 27 % / 8 %. The exhaust takes the remainder. The balance closes by construction, so the check is that the exhaust share lands at 34-45 % (Heywood). It lands at 0.37-0.43 for every concept.

**Normalizing.** Compressor work W = m_air cp T1 (PR^0.286 - 1) / η_c, ISA, at the proposed 12,000 ft critical altitude (REQUIREMENTS R-7). The spark-ignition manifold target is 1.08 bar, which includes losses. A turbocharger's work comes from the exhaust; a supercharger's comes off the crank.

**Mass.**

- **Analog scaling**: m = m_ref (hp / hp_ref)^x, using the closest real engine class (vendor dry masses, read 2026-10-16, `sources/COMPARABLE_ENGINES_2026-10-16.md`). The concept tables use these anchors:

  | Concept | Analog anchor (vendor dry mass) | Exponent x |
  |---|---|---|
  | A | Continental O-200-D 89.3 kg (100 hp) to Lycoming IO-540-K 212.7 kg (300 hp) | 0.79, fitted |
  | B | Rotax 912 ULS 56.6 kg | ASSUMED |
  | C | between the Rotax and Lycoming classes | ASSUMED |
  | D | Verner/Rotec radial class | ASSUMED |
  | E | Continental CD-135, 134 kg including turbo and FADEC | ASSUMED |
  | F, G | no close analog | ASSUMED |

- **Allowances**: x1.10 for thicker sand-cast walls (MANUFACTURING: 4-6 mm walls); 6/9/12 kg for turbo and intercooler; 4 kg for a two-lane FADEC.
- **Confidence**: **+/-25 %.** This is extrapolation, not design.

"Installed dry" follows REQUIREMENTS R-37: engine, drive, normalizer, FADEC, starter, alternator and exhaust, no fluids, no radiator. The cooling system is shown separately at the mid analog (8 kW per kg of rejected heat). Its full bound is 3.7-27 kW/kg.

**Cost.** First-article parts and services, labor excluded (REQUIREMENTS section 7). Line items are from MANUFACTURING's envelope v0 where sourced, otherwise estimates, and the job-shop first-op line is unquoted. The band is wide because the unquoted lines are wide. It is a floor for ranking, not a price.

**The make/cast/machine/buy split is written inside MANUFACTURING's envelope v0** (AER-3321, `MANUFACTURING_ENVELOPE.md`). **Every row is pending MANUFACTURING's quote on real geometry**: there is no geometry yet. One change came straight from the envelope: every concept's bore is now **anchored to a catalog piston family** (envelope finding 4). Concepts F and G have no general catalog piston, and that is stated as a risk.

### The common part strategy (all four-stroke spark-ignition concepts: A, B, C, D)

Per-concept deltas follow in each concept section.

| Part | Path | Route (envelope section) | Skill |
|---|---|---|---|
| Crankcase, split at the crank centerline | **cast**: binder-jet bureau mold + foundry pour, A356/A357-T6, X-ray or pressure test, impregnate | 1.2 first article, 1.3 once stable; job-shop first-op [Q]; align hone at a machine shop | B0 + shop |
| Cylinder module / water jacket | **cast** (1.2: coolant cores print with the mold) + **buy** catalog dry or wet liner carrying the bore | 1.2 + section 4 liners | B0 + shop |
| Cylinder head | **cast** (1.2) + **buy** seat inserts and guides; seats cut and lapped by the builder (B1) or a machine shop | 1.2, 2.1 | B1 |
| Crankshaft | **buy custom billet 4340** (Crower/Bryant/Moldex, $3.4-6.3k, 3-4 months), balanced at a machine shop | section 6 | B0 + shop |
| Rods, pistons, rings, shells, valves, springs | **buy** catalog | section 4 | B1 (weigh-match) |
| Camshaft | **buy**: donor, regrind or custom billet from a cam grinder [Q] | section 6 | B0 |
| Covers, plenum, brackets, baffles, flanges | **cut** (laser/waterjet) or **print** (SLS/MJF); hobby-cast covers allowed | 3, 1.1 | B0-B2 |
| Coolant crossovers, thermostat housing | **print** AlSi10Mg (metal AM earns its price here) | 3 | B0 |
| Injectors, coils, sensors, pumps, starter, alternator | **buy** catalog (EV14 injectors $72-89, D585 coils $48-51, EWP115 $225) | 4 | B0 |
| Turbocharger, wastegate | **buy** catalog automotive turbo | (not in the envelope yet: ask) | B0 |
| FADEC (two lanes) | **buy** two open ECUs (Speeduino, rusEFI or SDS class) + open firmware and harness | `docs/ENGINE_MGMT_CANDIDATE_MATRIX_V1.md` | B1 |

What this strategy cannot avoid, per MANUFACTURING: a local job shop for the first-op machining of every casting, which is the largest unknown on the cost ledger. Also a billet crank or a donor crank.

---

## Concept A: flat, low-speed, big-bore, direct drive (liquid-cooled Lycoming geometry)

**Idea.** This is the Continental E-225 premise with water jackets. A horizontally opposed engine runs at propeller speed with no gearbox. The cylinder module uses the **Lycoming 540 cylinder's bore and stroke (130.2 x 111.1 mm)**, so the aviation piston, ring and valve catalog applies. Each cylinder makes about 50 hp.

**Family scaling.** Flat-2 for 100 hp, flat-4 for 200 hp, flat-6 for 300 hp, on one cylinder, head, piston and valvetrain module. The crankcase and crank are per-member. **The family holds on parts but breaks on smoothness at 100 hp**: a 100 hp flat-twin turning a propeller directly (REQUIREMENTS F-3).

| Member | Cyl | Vd | rpm | BMEP | Sp | Fuel at takeoff | Coolant / oil / exhaust heat | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 2 | 2.96 L | 2,750 | 11.0 bar | 10.2 m/s | 23.1 kg/h | 65 / 13 / 117 kW | 108 kg (+10) | $15k-39k |
| 200 hp | 4 | 5.92 L | 2,750 | 11.0 bar | 10.2 m/s | 46.2 kg/h | 129 / 27 / 234 kW | 183 kg (+20) | $20k-52k |
| 300 hp | 6 | 8.88 L | 2,750 | 11.0 bar | 10.2 m/s | 69.4 kg/h | 194 / 40 / 351 kW | 250 kg (+29) | $26k-65k |

**Normalizing: turbocharger.** Pressure ratio 1.68 at 12,000 ft; compressor work 6.4 % of rated power, supplied by the exhaust; compressor outlet 51 C at ISA. Big low-speed engines have the exhaust energy and the room for one turbo with a wastegate. A supercharger would take that 6.4 % off a direct-drive crank.

**Part strategy.** Common SI strategy above. Delta: the pistons, rings and valves come from the **aviation** catalog (Lycoming 540 class, priced like aviation parts, [Q]), not the cheap automotive one. Direct drive deletes the gearbox. The crank also carries propeller thrust and gyroscopic loads, so it is a full aviation crank in billet. **Pending MANUFACTURING.**

**Mass against R-37:** 108 / 183 / 250 kg against targets of 90 / 150 / 210 kg. It misses at every member, +/-25 %. Liquid cooling does not make a big-bore direct-drive engine lighter than its air-cooled parent.

**Most likely to kill it: knock.** A 130 mm bore at 11 bar BMEP on 91 AKI pump gas. The IO-540-K makes this BMEP (300 hp, 8.87 L, 2,700 rpm, about 11.2 bar) on 100-octane avgas. On 91 AKI with ethanol, a bore this size needs a lower compression ratio, a lower BMEP, or both. Liquid-cooled heads and FADEC knock control help, but by how much is unproven, and every point of compression costs about 3-4 % of fuel burn. Second: the 2-cylinder 100 hp member.

---

## Concept B: flat, high-speed, small-bore, geared (Rotax-scaled module)

**Idea.** The Rotax 912 recipe, made from files: small, fast, light cylinders and a reduction gearbox to the propeller. Module: **86 mm bore (Toyota/Subaru FA20 catalog family) x 64 mm stroke**, about 25 hp per cylinder, 5,800 rpm, about 2.4:1 to the prop.

**Family scaling.** Flat-4, flat-8, flat-12 on one module, with one head casting per cylinder pair (2/4/6 heads). **The family breaks at 300 hp**: a 12-cylinder flat engine has 48 valves (at 4 per cylinder), a long crank, and a firing frequency high enough to push torsional design hard. Realistically this is a 100/200 hp family, with 300 hp needing a larger module (REQUIREMENTS F-3).

| Member | Cyl | Vd | rpm | BMEP | Sp | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 4 | 1.49 L | 5,800 | 10.4 bar | 12.4 m/s | 23.1 kg/h | 65 / 13 / 117 kW | 72 kg (+10) | $18k-47k |
| 200 hp | 8 | 2.97 L | 5,800 | 10.4 bar | 12.4 m/s | 46.2 kg/h | 129 / 27 / 234 kW | 125 kg (+20) | $26k-67k |
| 300 hp | 12 | 4.46 L | 5,800 | 10.4 bar | 12.4 m/s | 69.4 kg/h | 194 / 40 / 351 kW | 174 kg (+29) | $34k-86k |

**Normalizing: turbocharger**, one per engine, with a wastegate. The same thermodynamics as A (PR 1.68, 6.4 %, 51 C at 12,000 ft). For reference, the Rotax 915/916 already does this with a turbo and intercooler.

**Part strategy.** Common SI strategy, plus:

- **Reduction gearbox [Q]**: catalog gears or a donor gearset in a cast or billet case, with a deliberately soft torsional coupling. See DRIVE_AND_PROP.md.
- **Overhead cams**: one cam pair per head (2/4/6 cams), so the cam drive is belt or chain on catalog sprockets.
- **Pistons**: automotive catalog (the cheap one).

**Pending MANUFACTURING.**

**Mass against R-37:** 72 / 125 / 174 kg against 90 / 150 / 210 kg. This is the only concept inside the mass targets at all three members, at +/-25 %.

**Most likely to kill it: the family breaks at 300 hp**, through 12 cylinders and part count. Close second, common to every geared concept: the reduction-drive torsional window. A plain steel quill shaft lands *inside* the forbidden band (DRIVE_AND_PROP.md, torsional section).

---

## Concept C: V-2/4/6, paired crankpins, mid-speed, geared

**Idea.** Large automotive cylinders in a V. Two rods share each crankpin, so the crank has half as many throws as there are cylinders: 1, 2 or 3. Module: **GM LS7 bore and stroke, 104.8 x 101.6 mm** (the deepest catalog of cheap performance pistons, rods, liners and gaskets anywhere), about 50 hp per cylinder, 4,700 rpm, about 2.0:1 to the prop.

**Family scaling.** V-twin for 100 hp, V4 for 200 hp, V6 for 300 hp, with one cylinder, head and piston module. The crank and case are per-member. The V6 needs a split-pin or 60-degree layout for even firing, so the crankcase differs by member. The 100 hp V-twin has the same smoothness problem as A's flat-twin (F-3), made worse by uneven firing at a 90-degree V angle.

| Member | Cyl | Vd | rpm | BMEP | Sp | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 2 | 1.75 L | 4,700 | 10.9 bar | 15.9 m/s | 23.1 kg/h | 65 / 13 / 117 kW | 92 kg (+10) | $16k-42k |
| 200 hp | 4 | 3.51 L | 4,700 | 10.9 bar | 15.9 m/s | 46.2 kg/h | 129 / 27 / 234 kW | 157 kg (+20) | $21k-54k |
| 300 hp | 6 | 5.26 L | 4,700 | 10.9 bar | 15.9 m/s | 69.4 kg/h | 194 / 40 / 351 kW | 215 kg (+29) | $26k-67k |

**Normalizing: turbocharger**, as A and B.

**Part strategy.** Common SI strategy, with two deltas:

- **Pushrod valvetrain** from a single cam in the V, using catalog LS-class lifters, pushrods and rockers. One cam per engine is a part-count win.
- **Reduction gearbox [Q]**, as B.

**Pending MANUFACTURING.**

**Mass against R-37:** 92 / 157 / 215 kg against 90 / 150 / 210 kg. That is at the line, +/-25 %.

**Most likely to kill it: the geared drive behind 2 or 4 large cylinders.** Big, infrequent torque pulses at a low firing order put the gearbox's first torsional mode where it is hardest to tune away. At 200 hp, the soft coupling would have to be below about 5,800 N m/rad (crank-referred). Second: mean piston speed of 15.9 m/s, the highest of the set and on the high side for continuous aviation duty, where Rotax runs 11.8 m/s.

---

## Concept D: liquid-cooled radial, single-throw crank

**Idea.** The Rotec/Verner modular-radial recipe with water jackets. All cylinders work on **one crank throw** through a master rod and link rods. That is the simplest crankshaft of any concept: built-up, short, and with no long torsional length. Direct drive. Module: **114.3 mm bore (4.5 in big-block Chevy catalog piston) x 106 mm stroke**, about 33 hp per cylinder.

**Family scaling.** 3, 7 and 9 cylinders, all odd as single-row four-stroke firing requires. Each extra cylinder adds one head-and-cylinder module and a larger crankcase ring. **The 200 hp member is a 7-cylinder run at 2,400 rpm** (28.6 hp per cylinder), because no odd count gives exactly 200 hp at 33 hp per cylinder. The 3-cylinder 100 hp member is rough (1.5-order excitation).

| Member | Cyl | Vd | rpm | BMEP | Sp | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 3 | 3.26 L | 2,600 | 10.5 bar | 9.2 m/s | 23.1 kg/h | 65 / 13 / 117 kW | 104 kg (+10) | $18k-46k |
| 200 hp | 7 | 7.61 L | 2,400 | 9.8 bar | 8.5 m/s | 46.2 kg/h | 129 / 27 / 234 kW | 170 kg (+20) | $27k-68k |
| 300 hp | 9 | 9.79 L | 2,600 | 10.5 bar | 9.2 m/s | 69.4 kg/h | 194 / 40 / 351 kW | 229 kg (+29) | $31k-80k |

**Normalizing: a geared centrifugal supercharger in the rear case.** This is classic radial practice: one impeller also distributes mixture to every cylinder evenly, which a radial needs. Cost: 6.9 % of rated power off the crank at 12,000 ft (compressor efficiency 0.65, 56 C outlet), and at sea level the fixed gear ratio over-boosts, so a throttle or a bypass must waste it. A turbo is the alternative, at A's numbers.

**Part strategy.** Common SI strategy with these deltas:

- **Crank**: built-up single-throw crank [Q], cheaper than a multi-throw billet.
- **Master rod and link rods: custom, with no catalog equivalent [Q].**
- **Coolant**: a manifold ring for 3-9 jacketed heads.
- **Oil**: a scavenge design that keeps the lower cylinders from hydraulic lock.

**Pending MANUFACTURING.**

**Mass against R-37:** 104 / 170 / 229 kg against 90 / 150 / 210 kg. It misses, +/-25 %.

**Most likely to kill it: the master-and-link-rod system.** It moves the "made from files" break from the crank to the rods. That is a precision, fatigue-critical forging or billet set with no catalog source, and one more custom part than every other concept. Second: the liquid-cooling plumbing for a radial and its frontal packaging.

---

## Concept E: four-stroke diesel, common rail, turbocharged, geared (I3 / I6 / V8)

**Idea.** The Continental CD-135 / Austro recipe, made from files. A compression-ignition 4-stroke with common-rail injection, a turbocharger as part of the combustion system, and a reduction gear to the propeller. Module: **Mercedes OM640 bore and stroke, 83 x 92 mm** (the OE engine behind the CD-135/155 and AE300; catalog OE pistons). About 25 hp per cylinder at 15-17 bar BMEP.

**Family scaling.** I3 for 100 hp and I6 for 200 hp, on one 3-cylinder head module (one head for the I3, two for the I6). **300 hp breaks the inline family**: an I9 is impractical, so it needs a V8, which means a different crankcase and crank, and heads that are not the I3 module.

| Member | Cyl | Vd | rpm | BMEP | Sp | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 3 | 1.49 L | 3,900 | 15.4 bar | 12.0 m/s | 16.8 kg/h | 40 / 12 / 73 kW | 116 kg (+6) | $18k-45k |
| 200 hp | 6 | 2.99 L | 3,900 | 15.4 bar | 12.0 m/s | 33.6 kg/h | 80 / 24 / 146 kW | 197 kg (+13) | $25k-60k |
| 300 hp | 8 (V) | 3.98 L | 3,900 | 17.3 bar | 12.0 m/s | 50.3 kg/h | 120 / 36 / 219 kW | 271 kg (+19) | $28k-68k |

The diesel's fuel burn is **27 % lower** than spark ignition at takeoff (225 against 310 g/kWh, class values), and its heat to coolant is about **38 % lower**, which shrinks the radiator. Holding 2.2 bar manifold to 12,000 ft needs a pressure ratio of 3.41, with about 20 % of rated power as turbine work (from the exhaust) and a **150 C compressor outlet**. An intercooler is mandatory.

**Normalizing: turbocharger**, integral to the cycle. **This does not satisfy REQUIREMENTS R-5 as written.** See E-NA below and finding F-1.

**Part strategy.** Common strategy plus:

- **High-pressure fuel pump, common rail and injectors**: buy (Bosch-class, [Q]).
- **Glow plugs**: buy.
- **DOHC heads**: two cams per head module.
- **Head and case**: designed for peak cylinder pressure of about 160-180 bar ([E], modern passenger-car diesel class, not sourced this pass), against about 60-80 bar for spark ignition ([E]).

**Pending MANUFACTURING**, and the first concept that needs MANUFACTURING to say whether **an A356-T6 sand-cast head and case can carry diesel peak pressure** at all.

**Mass against R-37:** 116 / 197 / 271 kg against 90 / 150 / 210 kg. It misses at every member, +/-25 %. That is consistent with the real diesels: CD-135 134 kg, AE300 185 kg, SMA 195 kg.

**Most likely to kill it: diesel peak cylinder pressure in a sand-cast aluminum head and crankcase.** Head-bolt clamp load, deck fatigue and main-web fatigue at about twice the spark-ignition pressure. Every production aircraft diesel found started from an automotive block, or from a purpose-built case not made in sand. Second: F-1.

### Variant E-NA: the same diesel held literally to 1 bar manifold

This variant is not a seventh concept. It is E under REQUIREMENTS R-5 as written, kept to show what the requirement costs.

| Member | Cyl | Vd | rpm | BMEP | Installed dry |
|---|---|---|---|---|---|
| 100 hp | 6 | 2.99 L | 4,000 | 7.5 bar | 194 kg |
| 200 hp | 12 | 5.97 L | 4,000 | 7.5 bar | 334 kg |
| 300 hp | 18 | 8.96 L | 4,000 | 7.5 bar | 504 kg |

Twice the cylinders and about 1.7x the mass. At 200 hp it is heavier than a 300 hp IO-540-K (212.7 kg). **A literally normalized diesel family is not a real option**; that is finding F-1.

---

## Concept F: opposed-piston two-stroke diesel, no cylinder head

**Idea.** Two pistons share one cylinder and meet in the middle (the Junkers Jumo 205 layout, revived in modern truck research). **There is no cylinder head and no valvetrain.** The hardest casting in every other concept, the head with its coolant cores, seats and guides, simply does not exist. Ports in the liner wall are uncovered by the pistons. Two crankshafts, one at each end, are geared together, and the gear train is also the propeller reduction. Module: 82 mm bore x 2 x 78 mm strokes, about 50 hp per cylinder (two pistons) at 3,000 rpm.

**Family scaling.** 2, 4 and 6 cylinders with one liner, piston and port module. The two cranks and the gear train lengthen per member. Six cylinders is still a short crank pair.

| Member | Cyl (pistons) | Vd | rpm | BMEP (2-stroke) | Sp | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|---|
| 100 hp | 2 (4) | 1.65 L | 3,000 | 9.1 bar | 7.8 m/s | 16.0 kg/h | 30 / 13 / 72 kW | 109 kg (+5) | $19k-43k |
| 200 hp | 4 (8) | 3.30 L | 3,000 | 9.1 bar | 7.8 m/s | 32.1 kg/h | 61 / 27 / 144 kW | 185 kg (+11) | $23k-52k |
| 300 hp | 6 (12) | 4.94 L | 3,000 | 9.1 bar | 7.8 m/s | 48.1 kg/h | 91 / 40 / 217 kW | 254 kg (+16) | $27k-60k |

Fuel burn is the lowest of the set (215 g/kWh, class value), as is heat to coolant (no head). The cycle needs scavenge air at every operating point. A Roots-type blower at a pressure ratio of about 1.4 takes **about 7 kW of shaft power at 100 hp** (9-10 %). That is a hand calculation from the model's airflow at a blower efficiency of 0.55, [E]. The turbo then holds the scavenge manifold (2.0 bar) to altitude, at PR 3.10 and a 136 C outlet. **Normalizing: scavenge blower + turbo, integral.** F-1 applies to F as it does to E.

**Part strategy, and how it differs most:**

- **No head, no cams, no valves, no springs, no seats, no guides.**
- **Liners with machined port belts**: custom, [Q].
- **Pistons**: custom, because a port-controlling piston skirt and crown have **no general catalog part** [Q]. Envelope finding 4 says off-catalog pistons become custom orders.
- **Cranks**: two billet cranks.
- **Gear train**: a phasing gear train, catalog gears where possible, [Q].
- **Crankcase**: two simple cast end-housings plus a cylinder block.

**Pending MANUFACTURING.**

**Mass against R-37:** 109 / 185 / 254 kg against 90 / 150 / 210 kg. It misses, and the confidence is lower than for the others: there is no modern small aviation opposed-piston analog.

**Most likely to kill it: development maturity.** Scavenging, port timing and piston-crown and port-bridge heat are a combustion research program, not a build-from-files program, and no small opposed-piston aircraft diesel is in service to learn from. Second: custom pistons and two cranks.

---

## Concept G: Wankel rotary, rotor-module family

**Idea.** The family is literally built by adding modules. Each rotor, with its housing and intermediate plate, is a stack slice. Module: the **Mazda 13B rotor (0.654 L chamber)**, with an aftermarket rotor, housing and seal supply. About 50 hp per rotor at 4,600 eccentric-shaft rpm, gently stressed against the 13B's road-car speeds. About 2.0:1 reduction to the prop. Few parts and smooth: no valvetrain, no reciprocating mass.

**Family scaling.** 2, 4 and 6 rotors, one rotor and housing module. The eccentric shaft is per-member and must be multi-piece above 2 rotors, as on Mazda's 4-rotor R26B race engine.

| Member | Rotors | Vd | rpm | BMEP (per rotor-rev) | Fuel | Coolant / oil / exhaust | Installed dry (+ cooling) | Cost floor |
|---|---|---|---|---|---|---|---|---|
| 100 hp | 2 | 1.31 L | 4,600 | 7.4 bar | 25.4 kg/h | 80 / 24 / 118 kW | 87 kg (+13) | $16k-37k |
| 200 hp | 4 | 2.62 L | 4,600 | 7.4 bar | 50.7 kg/h | 160 / 47 / 235 kW | 142 kg (+26) | $21k-48k |
| 300 hp | 6 | 3.92 L | 4,600 | 7.4 bar | 76.1 kg/h | 240 / 71 / 353 kW | 192 kg (+39) | $27k-58k |

The rotary burns **about 10 % more fuel** than the piston spark-ignition concepts at takeoff (340 against 310 g/kWh, class values; the cruise gap is commonly larger, not sourced this pass). Its heat to coolant and oil is the highest of the set: about 1.4x shaft power, so the largest radiator. **Normalizing: turbocharger** (PR 1.68, 7.1 %, 51 C at 12,000 ft). The rotary's hot, high-energy exhaust suits a turbo, and the 13B has turbo heritage.

**Part strategy.**

- **Rotors, rotor housings, apex and side seals: buy aftermarket** (13B, out of OE production) [Q].
- **Intermediate and end plates**: cast or billet [Q].
- **Eccentric shaft**: custom, multi-piece [Q].
- **No heads, cams or valves.**

**Pending MANUFACTURING.**

**Mass against R-37:** 87 / 142 / 192 kg against 90 / 150 / 210 kg. Inside the targets, +/-25 %, with a heavier cooling line than any piston concept.

**Most likely to kill it: the rotor housing's trochoid running surface and the seal supply.** A coated (chrome or Nikasil-class), ground trochoid is outside every file-based route in the envelope. The aftermarket supply exists for an engine Mazda stopped building in 2012, so it is a supply that can end. Second: fuel burn.

---

## Reference, not a concept: buy an automotive core

The Viking and Aeromomentum route (an automotive engine plus a reduction drive, about $13-28k, sources file) violates "made from files" for its core. It stays here as **the cost yardstick every concept is measured against**, especially at 100 hp (REQUIREMENTS F-2).

## Summary of the physics floor (unranked, same order as above)

| Concept | Fuel | Family | Installed dry, 100 / 200 / 300 hp | Cost floor, 200 hp | Most likely to kill it |
|---|---|---|---|---|---|
| A flat direct big-bore | auto gas | 2/4/6, one module | 108 / 183 / 250 kg | $20k-52k | knock in a 130 mm bore on pump gas |
| B flat geared small-bore | auto gas | 4/8/12, breaks at 300 | 72 / 125 / 174 kg | $26k-67k | 12 cylinders at 300 hp |
| C V paired-pin geared | auto gas | 2/4/6, one module | 92 / 157 / 215 kg | $21k-54k | gearbox torsional window behind big cylinders |
| D radial single-throw | auto gas | 3/7/9, one module | 104 / 170 / 229 kg | $27k-68k | master/link rods with no catalog source |
| E 4-stroke diesel | Jet-A / diesel | I3/I6, breaks to V8 | 116 / 197 / 271 kg | $25k-60k | diesel peak pressure in sand-cast aluminum |
| F opposed-piston diesel | Jet-A / diesel | 2/4/6, one module | 109 / 185 / 254 kg | $23k-52k | development maturity |
| G Wankel | auto gas | 2/4/6 rotors, one module | 87 / 142 / 192 kg | $21k-48k | trochoid surface and seal supply |

All masses are +/-25 % extrapolations. All costs are first-article floors with unquoted lines. Nothing is ranked.

## What this pass did not do

- **No quotes.** Every make/cast/machine/buy row is pending MANUFACTURING's quotes on real geometry, and there is no geometry yet. MANUFACTURING's first quotes are queued in its envelope section 8.
- **Turbochargers are not in the envelope yet.** Their cost line here is PROPULSION's estimate.
- **No knock model.** Concept A's killer is argued from the IO-540-K precedent and Heywood's trends, not computed.
- **No crank or case FEA**, and no peak-pressure structural check for E. That is phase 1.
- **The torsional analysis is a two-inertia window** (DRIVE_AND_PROP.md), not a multi-mass model with real stiffnesses.
