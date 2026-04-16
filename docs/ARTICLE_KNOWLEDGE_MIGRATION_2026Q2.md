# MAOS-ICE Article Knowledge Migration (2026 Q2)

Purpose: Capture ICE/generator architecture knowledge from aerocommons articles and define immediate MAOS-ICE actions.

Scope note: This is R&D guidance for Experimental Amateur-Built development. It is not a certification claim.

## Source Articles

- 2026-04-05-maos-engine-comparison-matrix.md
- 2026-04-05-maos-generator-selection.md
- 2026-04-05-maos-1g1b2m-architecture-decision.md
- 2026-03-25-single-vs-twin-engine-architecture.md
- 2026-04-05-maos-propulsion-redundancy-battery.md

## Imported Decisions and Working Baseline

- Current architecture baseline from program trade studies is 1G+1B+2M for Phase 1, with explicit documentation of residual single-generator risk and battery reserve assumptions.
- Engine selection remains driven by reliability, supportability, integration mass, fuel efficiency, and generator coupling practicality.
- Generator selection and engine selection are coupled decisions; MAOS-ICE owns this coupling definition for integration handoff.

## ICE-Focused Guidance to Carry Into This Repo

- Maintain a clear distinction between engine-as-prime-mover and motor-as-thrust source in safety/failure analysis.
- Publish generator operating bands that minimize fuel burn while respecting thermal and mechanical limits.
- Define restart, degraded-operation, and emergency dispatch behavior with unambiguous state transitions.

## Open Decisions Assigned to MAOS-ICE

- Finalize Phase 1 engine shortlist and selection rationale.
- Lock generator pairing strategy and interface constraints (electrical, control, cooling, mounting).
- Define fault-state behavior for generator-offline events and restart windows.
- Confirm fuel and thermal operating envelopes for altitude mission profile.

## Immediate Work Items

1. Create docs/ENGINE_SELECTION_DOWNSELECT_V1.md with weighted scoring and rationale.
	(Done)
2. Create docs/GENERATOR_PAIRING_AND_CONTROL_MODES.md for integration contracts.
3. Create docs/ICE_FAILSAFE_AND_RESTART_LOGIC.md with explicit state machine.
4. Provide an initial interface payload for MAOS-MOTOR and MAOS-FCS consumption.

## Suggested Deliverables to Add Next

- docs/ENGINE_SELECTION_DOWNSELECT_V1.md
	(Completed)
- docs/GENERATOR_PAIRING_AND_CONTROL_MODES.md
- docs/ICE_FAILSAFE_AND_RESTART_LOGIC.md
