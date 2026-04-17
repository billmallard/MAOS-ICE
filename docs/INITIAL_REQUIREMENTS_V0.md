# MAOS-ICE Initial Requirements v0

Status: Draft / Working notes. Intentionally early and incomplete.
Purpose: Seed ICE subsystem requirements for iterative refinement.

## Functional Requirements

- ICE-SYS-001: The ICE subsystem shall support continuous generator-duty operation in the 100-230 kW target class.
- ICE-SYS-002: The ICE subsystem shall publish commanded operating state and measured operating state each control cycle.
- ICE-SYS-003: The ICE controller shall support startup, run, derate, and shutdown states with deterministic transitions.
- ICE-SYS-004: The subsystem shall provide a configurable operating-point scheduler for efficiency-focused generator operation.

## Interface Requirements

- ICE-IF-001: Mechanical coupling interface shall define shaft speed range, torque limits, and alignment tolerances.
- ICE-IF-002: Electrical interface shall define starter/generator power budgets and grounding constraints.
- ICE-IF-003: Thermal interface shall define coolant flow, temperature limits, and alarm thresholds.
- ICE-IF-004: Fuel interface shall define pressure, flow, and contamination assumptions.
- ICE-IF-005: Telemetry interface shall define units, update rates, and fault flags for FCS and logging tools.

## Safety and Fault Requirements

- ICE-FLT-001: The controller shall detect overtemp, overspeed, low oil pressure, and sensor plausibility faults.
- ICE-FLT-002: Fault handling shall define degraded operation and commanded shutdown conditions.
- ICE-FLT-003: Fault transitions shall be logged with timestamp and reason code.
- ICE-FLT-004: Sensor loss shall not cause undefined controller outputs.

## Verification Requirements

- ICE-VER-001: Bench tests shall cover startup, steady-state load steps, and commanded shutdown.
- ICE-VER-002: Bench tests shall include injected sensor fault scenarios and expected responses.
- ICE-VER-003: At least one requirement-mapped simulation campaign shall validate operating-point logic.
- ICE-VER-004: Requirements shall be traceable to test artifacts or open gaps.
