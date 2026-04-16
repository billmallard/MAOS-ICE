# MAOS-ICE

Open-source internal combustion engine subsystem development for MAOS hybrid-electric aircraft concepts.

## Status

Concept and architecture phase.

## Safety Notice

This repository is for research and experimental development only. It is not approved for manned flight and must not be used as-is in safety-critical operation without formal system safety assessment, verification, validation, and regulatory compliance.

This project targets the Experimental Amateur-Built category. FAA certification is not a current design constraint, but engineering decisions should still follow conservative aerospace and safety-critical best practices where practical.

## Role in MAOS Multi-Project Architecture

This repository owns the MAOS internal-combustion engine domain.

- Engine selection, integration assumptions, and operating envelope definitions.
- Generator-engine operating strategy support for series-hybrid architecture.
- Controls, sensing, health monitoring, and verification artifacts for the ICE subsystem.

Related repositories:

- MAOS-DESIGN owns aircraft-level geometry, packaging, and integration constraints.
- MAOS-FCS owns flight-control computation and flight-critical control paths.
- MAOS-ECS owns environmental control and pressurization subsystem development.
- aerocommons is the website and program-level communications hub.

## Mission

Develop a practical and robust internal combustion engine subsystem architecture that supports hybrid-electric power generation with deterministic controls, explicit fault behavior, and builder-realistic maintenance and integration pathways.

## Scope

In scope:

- Engine architecture trade studies and operating envelope definition.
- Generator coupling assumptions and operating-point control strategy.
- Fuel, ignition, cooling, lubrication, and sensing interface requirements.
- Engine control logic, monitoring, and fault-detection behavior.
- Subsystem simulation and bench-test verification artifacts.

Out of scope:

- Aircraft-level geometry governance and top-level configuration control (owned by MAOS-DESIGN).
- Primary flight-control laws and actuator command authority (owned by MAOS-FCS).
- Cabin ECS thermal/pressurization subsystem design ownership (owned by MAOS-ECS).

## Interface-First Rules

Before detailed implementation, freeze and version:

- Mechanical interfaces: mounts, shaft/coupling definitions, vibration assumptions.
- Electrical interfaces: starter/generator power budgets, sensor interfaces, grounding and shielding.
- Fuel and thermal interfaces: flow, pressure, temperature, and cooling-loop contracts.
- Control interfaces: command states, telemetry units/rates, fault flags, and timeout semantics.
- Timing budgets: control-loop and safety-monitoring cycle constraints.

Starter template: INTERFACE_CONTROL_DOCUMENT_TEMPLATE.md

## Suggested Repository Layout

- docs  Architecture, requirements, and verification plans
- firmware  Embedded controller software and diagnostics logic
- libs  Shared protocol and control-support libraries
- sim  Engine and hybrid-operating-point simulation tools
- tests  Unit, integration, bench, and fault-injection test suites
- tools  Calibration, logging, and analysis utilities
- configs  Engine profiles and operating-point presets
- data  Test captures, calibration data, and reference datasets

## Verification Strategy

- Requirements-to-test traceability for all ICE safety-relevant behaviors.
- Bench validation of controls, sensing, and fault-detection logic.
- Simulation campaigns for hybrid operating points and transient behavior.
- Fault-injection tests for sensor failures, misfire-like behavior, and over-temp/over-speed limits.
- Regression evidence for each interface-affecting change.

## Current Milestones (As of 2026-04-14)

Current repository maturity is bootstrap-level.

Near-term milestones:

1. Establish baseline repo structure (docs, firmware, libs, sim, tests, tools, configs, data).
2. Publish top-level ICE subsystem requirements and failure-mode assumptions.
3. Draft first ICD covering fuel, electrical, mechanical, and control interfaces.
4. Stand up minimal simulation scaffold for generator operating-point control experiments.
5. Define initial bench-test matrix for startup, steady-state, and fault-response behavior.

## Knowledge Migration

- Article-derived subsystem migration notes: `docs/ARTICLE_KNOWLEDGE_MIGRATION_2026Q2.md`
- Formal engine shortlist and downselect matrix: `docs/ENGINE_SELECTION_DOWNSELECT_V1.md`

## Licensing

This repository uses a dual-license model:

- Source code: PolyForm Noncommercial 1.0.0 (LICENSE-CODE)
- Documentation and non-code design content: CC BY-NC-SA 4.0 (LICENSE-DOCS)

Commercial use is not granted by default. For commercial licensing, contact contact@aerocommons.org.

Contribution and file classification guidance: CONTRIBUTING.md

## Program Context

MAOS is an open-source experimental aircraft development effort. The aircraft has not yet flown. All design and performance values are targets subject to revision as analysis and testing mature.
