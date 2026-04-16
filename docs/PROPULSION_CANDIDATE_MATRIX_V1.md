# MAOS Propulsion Candidate Matrix — V1

**Status:** Research / Preliminary — Experimental Amateur-Built Category  
**Date:** 2026-04-16  
**Source:** Trade study synthesis from public specifications, press sources, and first-principles range budgeting  
**Note:** All cost estimates are rough order of magnitude. Component pricing from startup vendors is volume- and relationship-dependent.

---

## 1. Design Requirements (Fuzzy Targets — Subject to Revision)

| Parameter | Minimum Target | Stretch Target | Notes |
|-----------|---------------|----------------|-------|
| Range | 700 NM | 1,000 NM | With 45-min reserve |
| Cruise speed | 160 KTAS | 220+ KTAS | At altitude |
| Cruise altitude | FL180 | FL250+ | Above-weather capable |
| Propulsion architecture | Series hybrid (ICE → gen → motor) | Single electric motor with battery buffer | Experimental category enables non-traditional configs |
| ICE power (continuous) | 100 kW / 134 hp | 230 kW / 310 hp | Generator duty cycle — not burst |
| Total propulsion mass | < 300 kg w/o fuel | < 200 kg w/o fuel | Including cooling, battery buffer |
| Propulsion cost (target) | < $100k | < $60k | Including integration hardware |
| Single-motor viability | Accepted | Preferred | Series hybrid provides fault buffer vs. piston single |

---

## 2. ICE Candidate Engines

### 2A. Motorcycle / Automotive Derived (No Aviation Type Certificate — Experimental Only)

| Engine | Disp. | Stock Power | Turbo Potential | Bare Mass* | Spec. Power (stock) | SFC (est., turbo cruise) | Avail. | Est. Bare Cost | Key Risks |
|--------|-------|-------------|----------------|------------|---------------------|--------------------------|--------|----------------|-----------|
| **Suzuki Hayabusa Gen3 (GSX-1300RR)** | 1,340 cc | 140 kW / 190 hp | 200–250 kW @ moderate boost | ~55 kg | 2.5 kW/kg | ~310 g/kWh | Now | $3–8k used | No TBO data for sustained duty; oil system needs inversion adaptation; high RPM band (7,000–10,000) needs reduction |
| **Kawasaki Ninja ZX-14R** | 1,441 cc | 147 kW / 200 hp | 200–270 kW | ~60 kg | 2.5 kW/kg | ~300 g/kWh | Now | $4–9k used | Same class as Hayabusa; slightly heavier |
| **Kawasaki H2 / H2R (supercharged)** | 998 cc | 147–158 kW | ~200 kW (SC already factory) | ~65 kg | 2.3–2.4 kW/kg | ~320 g/kWh | Now | $8–18k used | Supercharger parasitic at part load; complex |
| **BMW S1000RR** | 999 cc | 152 kW / 207 hp | 180–220 kW | ~65 kg | 2.3 kW/kg | ~310 g/kWh | Now | $4–10k used | Higher parts cost; excellent refinement |
| **Yamaha R1 (MT-10 CP4)** | 998 cc | 147 kW / 200 hp | 180–220 kW | ~58 kg | 2.5 kW/kg | ~300 g/kWh | Now | $3–8k used | Crossplane crank gives smooth low-RPM torque |

*Bare crankcase/head assembly, stripped of transmission/clutch/airbox/exhaust. Add ~10–15 kg for aviation cooling loop, intake, exhaust, and mounts.

**Notable Prior Art:**
- Twin Hayabusa engines powered the Bugatti 100P replica (fixed-wing racer project)
- Single Hayabusa engine used in Radical SR1, Westfield Megabusa, British Hillclimb Championship single-seaters
- Turbocharged Hayabusa achieves 600+ hp in drag racing; 300+ hp at reliable street boost levels is well-proven

**Motorcycle Engine Generator Coupling Challenge:**
Motorcycle engines operate in the 5,000–10,000 RPM power band. The HPDM-180R generator wants 3,000 RPM input (integral 6.7:1 gearbox reduces from ~20,000 RPM internal). A ~2:1 to 3.5:1 belt or chain reduction from engine output shaft to generator input is the typical solution — well-documented in motorsport applications. Toothed belt is preferred for low-noise, low-maintenance operation.

---

### 2B. Purpose-Built / Semi-Aviation Engines

| Engine | Power (cont.) | Power (TO) | Mass | Spec. Power | SFC (cruise) | TBO | Type Cert. | Cost | Notes |
|--------|--------------|-----------|------|-------------|--------------|-----|-----------|------|-------|
| **Rotax 912 iS** | 75 kW / 100 hp | 75 kW | 60 kg | 1.25 kW/kg | 285 g/kWh | 2,000 hr | FAA/EASA | $15–20k new | Underpowered alone; excellent as secondary/APU |
| **Rotax 915 iS** | 100 kW / 141 hp | 100 kW | 68 kg | 1.47 kW/kg | ~280 g/kWh | 1,800 hr | FAA/EASA | $28–35k new | Best certified SFC; turbocharged; established supply chain |
| **Rotax 916 iS** | 120 kW / 160 hp | 120 kW | ~72 kg | 1.67 kW/kg | ~280 g/kWh | ~2,000 hr | Pending | ~$35–45k new | Announced 2023; builds on 915 architecture |
| **Kawasaki Inline-4 Aero Turbo** | 110 kW / 148 hp | 149 kW / 200 hp | 85 kg | 1.74 kW/kg (cont) | ~320 g/kWh | TBD | TBD (cert target 2030) | $30–60k est. | Clean-sheet aviation; FADEC; liquid-cooled; mogas |
| **Kawasaki Inline-6 Aero Turbo** | 261 kW / 350 hp | 280 kW / 375 hp | 127 kg | 2.05 kW/kg | ~300 g/kWh | TBD | TBD (cert target 2030) | $50–90k est. | Same program; highest continuous power in class |
| **DeltaHawk DHK2H120** | 89.4 kW / 120 hp | 89.4 kW / 120 hp | 72.7 kg | 1.23 kW/kg | ~228 g/kWh max / ~191 g/kWh best econ | TBD | None (UAS/defense product) | Contact mfr | 2-stroke 2-cyl opposed diesel; 1.65L; Jet-A/JP8/SAF/#2 diesel; supercharged + CAC; liquid-cooled; -40°C cold start; max 2600 RPM. DHK2H80 and DHK2H100 also available (same 72.7 kg) |
| **DeltaHawk DHK180A4** | 134.2 kW / 180 hp | 134.2 kW / 180 hp | 151 kg | 0.88 kW/kg | ~245 g/kWh max / ~220 g/kWh best econ | TBD / contact mfr | **FAA TC (first clean-sheet certified piston in ~50 yrs)** | Contact mfr | 2-stroke inverted-Vee 4-cyl diesel; 3.3L; compound boosted (SC + TC + CAC); liquid-cooled; clockwise rotation (pilot view); Cirrus SR20 demo to 25,000 ft |
| **DeltaHawk DHK235A4** | 175.2 kW / 235 hp | 175.2 kW / 235 hp | 151 kg | 1.16 kW/kg | ~227 g/kWh max / ~221 g/kWh best econ | TBD / contact mfr | **FAA TC** | Contact mfr | Same DHK4 platform; best-economy SFC nearly flat from 180→235 hp variants; highest power in certified DHK family |

**DeltaHawk Key Notes:**
- **Best measured SFC in any candidate class.** DHK2H120 best-economy 191 g/kWh and DHK235A4 ~221 g/kWh are substantially below Rotax 915 (~280 g/kWh) and far below M250 at part power (550–700 g/kWh).
- **Diesel compression ignition** means Jet-A, JP-5, JP-8, SAF, and #2 diesel all work — widest fuel flexibility of any candidate. No avgas dependency.
- **DHK4 is FAA type certificated** — first clean-sheet certified piston engine in approximately 50 years. Meaningful for supply chain and long-term support confidence even in experimental operation.
- **Mass penalty:** DHK4 at 151 kg is heavier than Rotax 915 (68 kg) by ~83 kg for ~75 kW more power. Specific power is low (0.88–1.16 kW/kg) vs. motorcycle engines (2.5 kW/kg). For a series hybrid architecture where ICE weight drives less penalty than in direct-drive, this may be acceptable.
- **DHK2 is UAS/defense-focused** — no published TBO, no aviation type certificate. Lower risk for experimental but supply chain is defense-oriented.
- **Max RPM 2600** — favorable for direct generator coupling without heavy reduction gearing. H3X HPDM-180R at 3,000 RPM would require only modest ~1.15:1 ratio (or slightly overrunning the HPDM spec — contact H3X). Very clean integration compared to motorcycle engine at 7,000–10,000 RPM.
- **SFC figures derived from published spec sheet data.** DHK2H120: 45 lbs/hr at 89.4 kW = 228 g/kWh; best economy: 28.2 lbs/hr at 67.1 kW = 191 g/kWh. DHK235A4: 13.1 gal/hr × 6.7 lb/gal = 87.8 lbs/hr at 175.2 kW = 227 g/kWh; best economy: 10.2 gal/hr = 68.3 lbs/hr at 140.2 kW = 221 g/kWh. Source: DeltaHawk Engines operational performance spec sheets (April 2025).

---

### 2C. Turbine Engines (Shaft Output)

| Engine | Shaft Power | Mass | Spec. Power | SFC (cruise load) | SFC (part power) | TBO | Type Cert. | Used Cost | Notes |
|--------|-------------|------|-------------|-------------------|-----------------|-----|-----------|-----------|-------|
| **Rolls-Royce M250-C18 (Allison 250)** | 236 kW / 317 hp | 63 kg | 3.75 kW/kg | ~424 g/kWh @ design | ~600–700 g/kWh @ 50% | 3,500 hr | TC (large fleet) | $8–40k | Lighter, older variant; good availability |
| **M250-C20B** | 310 kW / 420 hp | 72 kg | 4.3 kW/kg | ~400 g/kWh @ design | ~550–700 g/kWh @ 50% | 3,500 hr | TC (large fleet) | $15–60k | Most common used variant; Bell 206, MD500 parts universe |
| **M250-C28** | 336 kW / 450 hp | ~75 kg | 4.5 kW/kg | ~390 g/kWh | ~540–680 g/kWh @ 50% | 3,500 hr | TC | $20–70k | Higher-power mid-tier |
| **M250-C47** | 533 kW / 715 hp | ~95 kg | 5.6 kW/kg | ~370 g/kWh | ~500–650 g/kWh @ 50% | 5,000 hr | TC | $40–100k | Latest variant; oversized for single-engine MAOS |

**Critical M250 Insight:** Turbine SFC is highly sensitive to throttle position. The M250 is designed for operation near full power (helicopter demand profile). In a fixed-wing cruise at modest power, part-power SFC can reach 600–700 g/kWh — roughly 2× a modern turbocharged piston. This is acceptable only if the aircraft is optimized for the M250's power band (i.e., designed to cruise at 220–260 KTAS at FL200–FL250 where the engine loads are appropriate). At those conditions, **the M250 becomes the heart of a 1,000+ NM, 220+ KTAS aircraft that rivals $1M+ pressurized singles** — at a fraction of the acquisition cost.

**M250 Part-Power Mitigation Options:**
- Recuperator/regenerative heat exchanger (Allison 250-E3 prototype demonstrated 280 hp / 84 kg with regeneration; not in production)
- Optimize airframe and prop pitch for higher cruise power fraction
- Higher cruise altitude (FL200–FL250) reduces drag, allows near-full-power cruise at true airspeed
- Pair with small battery buffer to absorb excess power on descent/approach

---

## 3. Generator / Electric Motor Candidates (H3X Product Line)

All H3X units are bidirectional (motor or generator mode), liquid-cooled, SiC inverter integrated, CAN interface, -40 to +60°C, rated to 45,000–70,000 ft.

| Product | Power | Mass | Specific Power | Output RPM | Bus Voltage | Fault Tolerance | Notes |
|---------|-------|------|----------------|-----------|-------------|----------------|-------|
| **HPDM-30** | 30 kW | ~3 kg | ~10 kW/kg | High | 300–800 VDC | Single | Small applications |
| **HPDM-180R** | 180 kW | **16 kg** | **11.25 kW/kg** | **3,000 RPM** | 850 VDC | Single | Integral 6.7:1 gearbox. **Best match for motorcycle engine generator or single prop motor** |
| **HPDM-350** | 350 kW | 50 kg | 7.0 kW/kg | 2,700 RPM | 900 VDC | **Dual (no single-point failure)** | Direct-drive capable; fault-tolerant; good for M250 generator or high-power prop motor |
| **HPDM-500** | 500 kW | 50 kg | 10 kW/kg | 10,000 RPM | 850 VDC | Dual | Stackable to 1 MW; 70,000 ft rated |
| **HPDG-30** | 30 kW | 32 kg | 0.94 kW/kg | — | 180–450 VDC | Single | Complete packaged genset (2-stroke ICE + HPDM-30 + electronics + cooling). TBO 500–1,000 hr |

**magniX for Propulsion Motor:**

| Product | Power | Mass | Specific Power | Avail. | Notes |
|---------|-------|------|----------------|--------|-------|
| **magniAIR** | 175 kW / 235 hp | 55 kg | 3.18 kW/kg | 2027 | Air-cooled. GA-optimized. RV-10 demo. FAA MOSAIC targeted |
| **magni350** | ~260 kW est. | ~70 kg est. | ~3.7 kW/kg | RFI only | Fixed-wing eCTOL; flight-tested |
| **magni650** | ~480 kW est. | ~120 kg est. | ~4 kW/kg | RFI only | Flew Dash 8 H2 demo, Eviation Alice |

**magniAIR is the strong choice for prop motor in the 120–175 kW power band.** It is air-cooled (eliminates second coolant loop), purpose-built for propeller applications at GA altitudes, and will be commercially available in 2027. Power electronics are integrated.

---

## 4. Battery Buffer

| Product | Energy Density | Key Features | Application |
|---------|---------------|-------------|-------------|
| **magniX Samson** | 300 Wh/kg | 1,000+ full cycles; modular; integrated BMS and distribution; aviation-grade cooling; certifiable | Buffer for hybrid bus; boost for takeoff/climb |

**Recommended buffer size:** 15–25 kWh (50–83 kg). Provides:
- 8–12 min full-power boost (takeoff + initial climb at 175 kW)
- ~20–30 min reduced-power glide margin if ICE/generator fails
- Load leveling on the generator (prevents ICE from chasing throttle transients)

---

## 5. Propulsion System Configurations — Assessed Combinations

### Config A: M250-C20B + HPDM-350 (gen) + HPDM-350 (motor) + 20 kWh battery
**"Go-Fast Single"**

| Parameter | Value |
|-----------|-------|
| ICE continuous | 310 kW / 420 hp |
| Prop power (after losses) | ~272 kW / 365 hp |
| Target cruise speed | 220–260 KTAS |
| Target cruise altitude | FL200–FL250 |
| Prop motor RPM | 2,700 (direct-drive or short gearbox) |
| Engine mass | 72 kg |
| Generator mass | 50 kg |
| Prop motor mass | 50 kg |
| Battery (20 kWh) | ~70 kg |
| Subtotal (excl. fuel, cooling, mounts) | **~242 kg** |
| Fuel burn (optimized cruise) | ~350–420 g/kWh × 272 kW = **~100–115 kg/hr Jet-A** at design point |
| Fuel burn (part power / poor throttle point) | ~160–200 kg/hr — must avoid this regime |
| 5-hr fuel @ design point (1,000 NM scenario) | **~500–575 kg Jet-A** |
| Total propulsion + fuel | **~740–820 kg** |
| ICE/gen cost | $15–110k (used M250) |
| Motor + electronics | ~$60–100k (HPDM-350 ×2) |
| Battery | ~$15–25k |
| **Total est. propulsion cost** | **~$90–235k depending on M250 condition** |
| Range at design cruise | 1,000 NM ✓ (altitude-optimized) |
| Performance comparison | Rivals TBM 700 / PC-12 class in speed and range |

**Verdict:** Spectacular performance potential. The economics depend entirely on finding a mid-time M250-C20B in the $20–40k range and keeping H3X costs in check. The aircraft must be optimized for high-altitude cruise to avoid the part-power SFC trap. If you're going to build this aircraft, build it to use the turbine.

---

### Config B: Twin Turbo Hayabusa + 2× HPDM-180R (gen) + 1× HPDM-180R (motor) + 20 kWh battery
**"Affordable Hybrid — Twin Redundancy"**

| Parameter | Value |
|-----------|-------|
| ICE continuous (both) | 2 × ~180 kW = 360 kW total |
| Cruise mode | One engine at ~136 kW; second on standby or load-sharing |
| Prop power at cruise | ~120 kW (160–180 KTAS) / ~190 kW pushed (200 KTAS) |
| Engines (2× stripped, turboed) | 2 × ~70 kg = 140 kg |
| Generators (2× HPDM-180R) | 2 × 16 kg = 32 kg |
| Prop motor (1× HPDM-180R) | 16 kg |
| Battery (20 kWh) | ~70 kg |
| Subtotal (excl. fuel, cooling, mounts) | **~258 kg** |
| SFC (turbo gasoline, cruise load) | ~310 g/kWh |
| Fuel burn at 136 kW ICE load | **~42 kg/hr (~14 gal/hr)** |
| 6.25-hr block + reserve fuel | **~300 kg (~100 gal) mogas/avgas** |
| Total propulsion + fuel | **~560 kg** |
| ICE cost (2× used + turbo kits) | ~$30–50k |
| HPDM-180R ×3 | ~$60–120k |
| Battery | ~$15–25k |
| **Total est. propulsion cost** | **~$105–195k** |
| Range (160 KTAS, FL180) | 1,000 NM ✓ |
| Range (200 KTAS, both engines) | 700–800 NM ✓ |

**Verdict:** Best balance of cost, redundancy, and fuel efficiency. Motorcycle engines are available now. Primary risk is sustained-duty TBO — this is the biggest unvalidated assumption for the motorcycle engine path. Continuous-duty test program at generator load is required before flight.

---

### Config C: Single Turbo Hayabusa + HPDM-180R (gen) + HPDM-180R (motor) + 25 kWh battery
**"Minimum Cost Hybrid Single"**

| Parameter | Value |
|-----------|-------|
| ICE continuous | ~150–180 kW turbo |
| Prop power at cruise | ~110 kW (sustained) |
| Engine mass | ~70 kg |
| Generator + motor (HPDM-180R ×2) | 32 kg |
| Battery (25 kWh) | ~85 kg |
| Subtotal | **~187 kg** |
| Fuel burn | ~42–46 kg/hr |
| 6.25-hr fuel | ~285 kg |
| Total w/ fuel | **~470 kg** |
| ICE + turbo | ~$15–25k |
| HPDM-180R ×2 | ~$40–80k |
| Battery | ~$18–28k |
| **Total est. cost** | **~$73–133k** |
| Range (150 KTAS, FL180) | 1,000 NM ✓ |
| Cruise speed | Conservative — 150–170 KTAS |

**Verdict:** Lowest cost and mass. Single ICE is the risk point — but battery buffer provides meaningful fault margin (far better than piston single). Viable if cruise speed target is 150–170 KTAS.

---

### Config D: Kawasaki I4 Aero + HPDM-180R (gen) + magniAIR (motor) + 20 kWh battery
**"Clean-Sheet Aviation — 2030+"**

| Parameter | Value |
|-----------|-------|
| ICE continuous | 110 kW |
| Prop power | ~97 kW sustained |
| Engine mass | 85 kg |
| Generator + motor | 16 + 55 = 71 kg |
| Battery | ~70 kg |
| Subtotal | **~242 kg** |
| Cruise speed (sustainable) | 150–165 KTAS |
| Fuel | ~200 kg / ~66 gal |
| Total w/ fuel | **~440 kg** |
| Estimated cost (2030) | ~$80–140k |
| Range | 1,000 NM ✓ at 150 KTAS |

**Verdict:** Aviation-pedigreed ICE with FADEC. Lowest integration risk. But does not deliver the speed targets without I6 upgrade. Constrained by 2030 availability. Ideal if the project timeline permits.

---

### Config E: Kawasaki I6 Aero + HPDM-350 (gen) + HPDM-350 (motor) + 20 kWh battery
**"Purpose-Built Performance — 2030+"**

| Parameter | Value |
|-----------|-------|
| ICE continuous | 261 kW |
| Prop power (after losses) | ~230 kW |
| Engine mass | 127 kg |
| Generator + motor (HPDM-350 ×2) | 100 kg |
| Battery | ~70 kg |
| Subtotal | **~297 kg** |
| Cruise speed | 200–220 KTAS at FL180 |
| Fuel burn | ~80 kg/hr |
| 5-hr fuel | ~430 kg |
| Total w/ fuel | **~730 kg** |
| Est. cost (2030) | ~$150–230k |
| Range | 1,000 NM ✓ |

**Verdict:** Closest to ideal aviation solution at the performance target — if you can wait until 2030 and accept the cost. Competitive with certified light turboprop operating costs at a fraction of acquisition price.

---

## 6. Configuration Comparison Summary

| Config | Label | Cruise Speed | Range | Propulsion Mass (w/o fuel) | Est. Total Fuel | Est. Prop. Cost | Avail. | Primary Risk |
|--------|-------|-------------|-------|--------------------------|-----------------|----------------|--------|-------------|
| **A** | M250 Go-Fast | 220–260 KTAS | 1,000 NM | ~242 kg | ~550 kg Jet-A | $90–235k | Now | Part-power SFC; must be altitude-optimized |
| **B** | Twin Hayabusa | 160–200 KTAS | 700–1,000 NM | ~258 kg | ~300 kg mogas | $105–195k | Now | Motorcycle engine sustained-duty TBO unknown |
| **C** | Single Hayabusa | 150–170 KTAS | 1,000 NM | ~187 kg | ~285 kg mogas | $73–133k | Now | Same TBO concern; lowest cost |
| **D** | Kawasaki I4 | 150–165 KTAS | 1,000 NM | ~242 kg | ~200 kg mogas | $80–140k | 2030 | Modest speed; 4-year wait |
| **E** | Kawasaki I6 | 200–220 KTAS | 1,000 NM | ~297 kg | ~430 kg mogas | $150–230k | 2030 | Cost; 4-year wait |

---

## 6A. Bifurcated Development Paths (Execute In Parallel)

### Path T: M250 Turbine-Forward (Go-Fast Family Machine)

Mission intent:
- Maximize high-altitude cruise speed and weather-penetrating family travel capability.
- Accept higher fuel burn in exchange for turboprop-like performance and simple single-ICE architecture.

Current best-price pairings (now):

| Path T Pairing | ICE | Generator | Propulsion Motor | Combined Electric Hardware Cost (est.) | Notes |
|---|---|---|---|---:|---|
| T1 (Premium) | M250-C20B | HPDM-350 | HPDM-350 | $40k-$80k+ | Best technical fit, highest cost |
| T2 (Budget Hybrid) | M250-C20B | Hyper9 HV AC-X144 | Tesla Model 3 rear DU | **~$15.5k** | Strong budget fit; mass and integration complexity increase |
| T3 (Go-Fast Budget) | M250-C20B | Hyper9 HV AC-X144 | Tesla Model S LDU | **~$17.5k** | Highest budget power headroom; strong mass penalty |
| T4 (Balanced) | M250-C20B | Tesla Model 3 rear DU (gen mode) | Tesla Model 3 rear DU | **~$19.8k** | Symmetric hardware, high controls complexity |

Path T critical gates:
1. Validate turbine part-power SFC at intended cruise altitude and speed.
2. Prove generator-mode thermal and bus stability for selected low-cost generator hardware.
3. Quantify total installed mass delta from low-cost EV components versus aerospace machines.

### Path H: Hayabusa-Forward (Cost-Efficient Hybrid)

Mission intent:
- Maximize price-performance and fuel efficiency in 160-200 KTAS mission space.
- Use motorcycle-engine supply/cost advantage, with battery buffer for climb and fault margin.

Current best-price pairings (now):

| Path H Pairing | ICE | Generator | Propulsion Motor | Combined Electric Hardware Cost (est.) | Notes |
|---|---|---|---|---:|---|
| H1 (Best Budget Baseline) | Single turbo Hayabusa | Hyper9 HV AC-X144 | Hyper9 AC-X1 | **~$11.0k** | Closest to target economics; lower power ceiling |
| H2 (Twin Redundant Budget) | Twin turbo Hayabusa | 2x Hyper9 HV AC-X144 | Tesla Model 3 rear DU | **~$21.1k** | Strong redundancy and cruise headroom |
| H3 (High-Speed Cost Compromise) | Twin turbo Hayabusa | Hyper9 HV AC-X144 | Tesla Model 3 rear DU | **~$15.5k** | Better speed potential than H1, manageable cost |
| H4 (Premium Technical) | Twin turbo Hayabusa | 2x HPDM-180R | HPDM-180R | $60k-$120k | Performance benchmark, outside budget intent |

Path H critical gates:
1. Continuous-duty engine endurance at generator load (primary technical risk).
2. Reduction-drive durability and torsional behavior for generator coupling.
3. Generator-mode inverter control validation for selected low-cost machine.

---

### Path D: DeltaHawk-Forward (Certified Diesel, Fuel-Efficient Mid-Range)

**Concept:** Use a DHK235A4 (175 kW, FAA TC'd, Jet-A) as generator source. Best SFC of any piston candidate (~221–227 g/kWh), widest fuel compatibility, and max 2600 RPM output enabling simple direct or near-direct coupling to H3X HPDM-180R (3000 RPM — ~1.15:1 step-up, or operated within spec contact H3X). Path D occupies the middle ground: better efficiency than Path H, far better part-power SFC than Path T, and FAA pedigree for long-term support.

**Primary tradeoff:** Mass. DHK235A4 is 151 kg — 83 kg heavier than Rotax 915 for roughly the same generator output class. In a series hybrid, generator mass is carried everywhere. This requires a clean airframe mass budget review before committing.

| Path D Pairing | ICE | Generator | Propulsion Motor | Combined Electric Hardware Cost (est.) | Notes |
|---|---|---|---|---|---|
| **D1 (Premium)** | DHK235A4 | HPDM-180R | HPDM-350 | ~$60–120k | Best integration at max RPM match; dual fault-redundant prop motor |
| **D2 (Budget)** | DHK235A4 | Hyper9 HV AC-X144 | Tesla Model 3 rear DU | ~$15.5k | Near-direct RPM coupling possible; EV-sourced hardware; low acquisition cost |
| **D3 (Rotax fallback)** | DHK235A4 | Hyper9 HV AC-X144 | Hyper9 HV motor | ~$11.2k | Full budget track; generator and motor both sub-$6k |

Path D critical gates:
1. Mass budget: confirm airframe can absorb 151 kg generator ICE vs. 68 kg Rotax-class without exceeding MTOW.
2. DHK4 TBO and pricing: contact DeltaHawk for actual TBO figure and purchase price.
3. RPM coupling: confirm H3X HPDM-180R at 3,000 RPM can accept DHK4 max 2,600 RPM direct (or confirm need for ~1.15:1 step-up gear).
4. Supply chain: DeltaHawk is a startup (Racine, WI); verify production availability and lead time.

---

## 6B. ICE-to-Electric Dependency Map

Question resolved: electric motor search is partially independent from ICE, but not fully independent.

| Domain | Independent of ICE? | Dependency Detail |
|---|---|---|
| Propulsion motor peak power sizing | Partial | Depends on aircraft performance target more than ICE type |
| Propulsion motor voltage class | Partial | Must match bus architecture selected by generator and battery |
| Generator machine selection | **Dependent** | Strongly depends on ICE shaft speed, torque ripple, and coupling strategy |
| Cooling architecture | **Dependent** | Turbine and motorcycle paths drive different thermal rejection patterns |
| Controls and fault management | **Dependent** | State machine and failure handling differ by ICE transient behavior |
| Cost optimization | Partial | Hardware market is mostly ICE-agnostic, but adapters and controls are not |

Practical rule:
- Run electric motor procurement and bench characterization in parallel across both paths.
- Keep generator/coupling design path-specific (T vs H) from day one.

---

## 7. Open Questions / Next Steps

### High Priority
- [ ] Sustained-duty TBO test data for Hayabusa/ZX-14R at generator load (5,000+ RPM, continuous, 500+ hours) — **this is the critical gate for Configs B and C**
- [ ] H3X HPDM-180R actual pricing and lead time for non-defense customers
- [ ] M250 airframe design optimization: what cruise altitude / airspeed puts the engine on its efficiency knee?
- [ ] magniAIR pricing (expected 2027 commercial availability)

### Medium Priority
- [ ] Reduction drive design (belt/chain/gear) for motorcycle engine → HPDM-180R coupling
- [ ] Thermal management architecture for series-hybrid bus (shared coolant loop vs. separate loops)
- [ ] Battery buffer BMS integration with H3X CAN control interface
- [ ] SFC test data for M250-C20B at FL200–FL250 cruise — does the altitude profile change the SFC calculus?

### Long Term
- [ ] Kawasaki aero engine program status check (2027–2028 as they approach cert)
- [ ] Hydrogen-compatible variant timing (Kawasaki roadmap: post-2030)
- [ ] Revisit if any Kawasaki-generator package spec sheet becomes available

---

## 8. Evidence Confidence Levels

| Claim | Confidence | Source |
|-------|-----------|--------|
| M250-C20B: 310 kW, 72 kg, ~$15–60k used | High | Wikipedia / public specs; active market |
| HPDM-180R: 180 kW, 16 kg, 3,000 RPM, 45,000 ft | High | H3X product page (confirmed specs) |
| HPDM-350: 350 kW, 50 kg, dual-redundant | High | H3X product page (target specs from testing) |
| magniAIR: 175 kW, 55 kg, air-cooled, 2027 | High | Official magniX press release + multiple press sources |
| Samson battery: 300 Wh/kg | High | magniX official |
| Hayabusa bare mass ~55 kg stripped | Medium | Derived from 215 kg dry whole-bike, minus documented major subassemblies |
| Hayabusa turbo ~200–250 kW reliable | Medium | Drag racing heritage + Bugatti 100P replica program; not aviation-validated |
| M250 part-power SFC ~600–700 g/kWh | Medium | Gas turbine thermodynamic principle; specific M250 curve not obtained |
| Kawasaki I4/I6 continuous power ratings | High | Confirmed via multiple aviation press sources + brochure |
| H3X pricing estimates | Low | Startup — no published list pricing; contact required |

---

*Document status: Research — for design exploration and trade study purposes only.*  
*All specifications should be verified against current vendor datasheets before design commitment.*
