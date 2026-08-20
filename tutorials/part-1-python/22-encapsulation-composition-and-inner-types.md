# 22 — Encapsulation without Mutable Secrets

## Goal

Use module boundaries, private conventions, closures, and composition to encapsulate behavior.

Python uses naming conventions rather than absolute privacy. A leading underscore marks an implementation detail. Encapsulation is strongest when an invariant is enforced by constructors and every update returns a new valid value.

`AuthService` encapsulates token, hashing, secret-box, clock, and repository collaborators. Its callers do not touch encrypted TOTP storage.

Nested or inner classes are occasionally useful for tightly scoped types, but module-level frozen types are easier to import, type-check, test, and serialize. Prefer composition:

$$\text{Automation} = \text{AnalysisRepository} + \text{BriefRepository} + \text{OllamaClient}$$

Stateful ORM objects are encapsulated in repositories. They are converted immediately to frozen domain values before crossing the boundary.

## Lab

Trace `UserRow → User` through `row_to_user`. Identify the point where mutable ORM state stops leaking.

## Checkpoint

Design a module that hides a unit conversion table and exports only a pure `convert` function returning `Result`.

Reference coverage: encapsulation, inner classes, composition, private naming conventions, and class boundaries.

## Acceptance criteria

- unit-table mutation is impossible through the public API.
- incompatible units return `Err`.
- tests exercise only exported behavior.
