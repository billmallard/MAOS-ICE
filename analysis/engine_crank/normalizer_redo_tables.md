## 1. Where the supercharger's ratio should be set

- Phase 1b set it at 3,300 rpm (12,000 ft ISA+20). With the 3b propeller in an 80 kt climb the engine never reaches 3,300.
- Set at the climb rpm it actually turns at 12,000 ft ISA+20, solved self-consistently: **3,084 rpm**.
- That is a pulley ratio 1.070x the phase 1b one (impeller 7 % faster at every crank rpm).

## 2. Full-throttle climb at 80 kt, ground-adjustable propeller (3b)

| Atmosphere | Altitude | turbo: rpm, net % | SC ratio at 3,300 (phase 1b): rpm, net % | SC ratio at climb rpm, bypass upper bound | SC ratio at climb rpm, bypass lower bound | no normalizer |
|---|---|---|---|---|---|---|
| ISA+0 | 0 ft | 2,570, 78% | 2,516, 73% (MAP 1.00, drive 4.7 kW) | 2,508, 72% (MAP 1.00, drive 5.4 kW) | 2,561, 77% (MAP 1.00, drive 0.8 kW) | 2,570, 78% |
| ISA+0 | 8,000 ft | 2,899, 88% | 2,822, 81% (MAP 1.00, drive 6.7 kW) | 2,811, 80% (MAP 1.00, drive 7.6 kW) | 2,831, 82% (MAP 1.00, drive 5.9 kW) | 2,523, 58% |
| ISA+0 | 12,000 ft | 3,087, 94% | 2,856, 74% (MAP 0.90, drive 6.3 kW) | 2,982, 84% (MAP 1.00, drive 9.0 kW) | 2,982, 84% (MAP 1.00, drive 9.0 kW) | 2,494, 49% |
| ISA+20 | 0 ft | 2,658, 81% | 2,598, 75% (MAP 1.00, drive 5.2 kW) | 2,590, 75% (MAP 1.00, drive 5.9 kW) | 2,647, 80% (MAP 1.00, drive 0.9 kW) | 2,558, 72% |
| ISA+20 | 8,000 ft | 3,003, 91% | 2,918, 83% (MAP 1.00, drive 7.4 kW) | 2,906, 82% (MAP 1.00, drive 8.4 kW) | 2,927, 84% (MAP 1.00, drive 6.6 kW) | 2,507, 53% |
| ISA+20 | 12,000 ft | 3,201, 97% | 2,952, 76% (MAP 0.90, drive 6.9 kW) | 3,084, 87% (MAP 1.00, drive 10.0 kW) | 3,084, 87% (MAP 1.00, drive 10.0 kW) | 2,474, 45% |

The rpm rises through the climb in every normalized column, as Bill said. The phase 1b supercharger loses because its ratio was set at an rpm the climb never reaches, not because the rpm decays.

## 3. The new ratio at cruise rpm (3,300) and at sea level

- 12,000 ft ISA+0, 3,300 rpm, bypass upper bound: compressor can make PR 1.88; manifold held 1.00 bar; drive 12.3 kW (8%); net 92%
- 12,000 ft ISA+0, 3,300 rpm, bypass lower bound: compressor can make PR 1.88; manifold held 1.00 bar; drive 9.9 kW (7%); net 93%
- 8,000 ft ISA+0, 3,300 rpm, bypass upper bound: compressor can make PR 1.85; manifold held 1.00 bar; drive 12.3 kW (8%); net 92%
- 8,000 ft ISA+0, 3,300 rpm, bypass lower bound: compressor can make PR 1.85; manifold held 1.00 bar; drive 6.9 kW (5%); net 95%
- 0 ft ISA+0, 3,300 rpm, bypass upper bound: compressor can make PR 1.79; manifold held 1.00 bar; drive 12.3 kW (8%); net 92%
- 0 ft ISA+0, 3,300 rpm, bypass lower bound: compressor can make PR 1.79; manifold held 1.00 bar; drive 1.1 kW (1%); net 99%
- 0 ft ISA+20, 3,300 rpm, bypass upper bound: compressor can make PR 1.73; manifold held 1.00 bar; drive 12.3 kW (8%); net 92%
- 0 ft ISA+20, 3,300 rpm, bypass lower bound: compressor can make PR 1.73; manifold held 1.00 bar; drive 1.2 kW (1%); net 99%
- Turbo at the same points: net 100 % to 12,000 ft, with a 1-2 kW pumping gain at altitude and 1-3 kW back-pressure at sea level (normalizer_h.py).

## 4. Holding the full 200 hp net with the supercharger

- 12,000 ft ISA+20: drive about 10.7 kW, so manifold about 1.07 bar to net 200 hp; H's knock-limited CR on MON 85 falls from 8.45 to 8.19
- 8,000 ft ISA+20: drive about 7.4 kW, so manifold about 1.05 bar to net 200 hp; H's knock-limited CR on MON 85 falls from 8.45 to 8.26

## 5. A geared engine

- rated 3,300 rpm: with a fixed-pitch propeller the climb rpm is the same fraction of rated (93% at 12,000 ft ISA+20), so every percentage above carries over; the belt step-up to the Rotrex is 1.00x the 3,300 rpm engine's.
- rated 4,800 rpm: with a fixed-pitch propeller the climb rpm is the same fraction of rated (93% at 12,000 ft ISA+20), so every percentage above carries over; the belt step-up to the Rotrex is 0.69x the 3,300 rpm engine's.
- rated 5,800 rpm: with a fixed-pitch propeller the climb rpm is the same fraction of rated (93% at 12,000 ft ISA+20), so every percentage above carries over; the belt step-up to the Rotrex is 0.57x the 3,300 rpm engine's.
- With a constant-speed propeller holding rated rpm in the climb, the supercharger's design point and cruise point coincide; the trade closes to drive power, mass and heat, as phase 1b said.
