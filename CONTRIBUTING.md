# Contributing

Thanks for contributing to MAOS-ICE.

## Licensing Classification Rules (Important)

This repository uses a dual-license model:

- Code files are licensed under PolyForm Noncommercial 1.0.0 (see LICENSE-CODE).
- Non-code design and documentation content is licensed under CC BY-NC-SA 4.0 (see LICENSE-DOCS).

Use these rules when adding files:

1. Treat executable or build-consumed files as code.
2. Treat narrative, diagrams, models, and design artifacts as non-code.
3. If a file is mixed-content or ambiguous, add a file-level license notice.
4. File-level notice overrides repository default for that file.

## Typical Classification Examples

Code (PolyForm NC):

- Controller and diagnostic software: .c, .cpp, .h, .hpp, .py, .rs
- Automation and test scripts: .ps1, .sh
- Build and CI logic used by tooling

Non-code (CC BY-NC-SA):

- Requirements, architecture notes, and design reports
- Interface specifications and test procedures
- Calibration datasets, engine test captures, and diagrams

## Pull Request Expectations

- Keep changes scoped and reviewable.
- Keep units, interfaces, and fault semantics explicit.
- Include evidence for behavior claims (bench logs, analysis outputs, test artifacts).
- Do not claim certification, compliance approval, or airworthiness status.

## Commercial Use

Commercial use is not granted by default.
For commercial licensing inquiries: contact@aerocommons.org
