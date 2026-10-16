# The engine program

**Status:** active since 2026-10-16. **Owner:** Bill Mallard.

This page is the program's brief: why the engine exists and what it must be. The
requirements, architectures and drive studies in this folder answer it. The earlier
documents in `docs/` (hybrid powertrain, genset and propulsion-reset studies) belong to
the paused MAOS airframe program and are kept as history and vendor evidence, not
direction.

## Why

Two costs price new aircraft out of reach: avionics, easily $50k-$100k, and engines,
now closing in on $100k for larger ones. The pyEfis avionics stack is the answer to the
first. This program is the answer to the second.

The premise is an old engine. The Continental E-225-8 in Bill's Bonanza is a simple
sand-cast engine, machined without CNC. Hobbyists now print molds and patterns and
sand-cast aluminum themselves, and on-demand services such as SendCutSend put precision
parts within an individual builder's reach. An aircraft engine made from files is more
within reach than it has ever been.

## The brief

- **A family at 100, 200 and 300 hp**, scaled by adding cylinders around common parts.
- **Normalized, not boosted.** A turbocharger or supercharger holds sea-level power
  against density altitude. It does not raise rated power.
- **Fuel.** Diesel is preferred but likely harder to execute. US auto gas in the 80-96
  octane range is acceptable, and **ethanol must be tolerated**.
- **Liquid cooled. Dual-lane electronic ignition. Computer engine management (FADEC).**
- **Made from files.** Every part is printed, cut, cast from a printed mold or pattern,
  machined by an off-the-shelf service, or bought off the shelf.
- **Ease of assembly and maintenance are primary concerns.** Fewer parts. Substantially
  lower cost.
- **The propeller is a named constraint.** A car changes gear; a fixed-pitch prop cannot
  change pitch to match engine speed. A transmission (CVT or otherwise) that lets an
  inexpensive fixed-pitch prop perform at higher airspeeds is to be evaluated, alongside
  every alternative, including self-adjusting props.
- **Not electric, for now.** Solid-state cells past 400 Wh/kg look likely within about
  two years, but that field still needs time and a great deal of money.

## What this is not

An experimental engine design. Nothing here is certified, certifiable or flight-ready,
and untested designs are labeled untested.
