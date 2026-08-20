# 46 — Functional Core, Imperative Shell

## Goal

Keep normalization, validation, feature calculation, and ranking pure while isolating UUIDs, time, SQL, HTTP, encryption, and model calls in adapters.

## 46.1 — Classify every operation

| Operation | Pure core or shell? | Reason |
|---|---|---|
| normalize atomic fractions | core | deterministic value transformation |
| calculate Pugh ratio | core | mathematical function |
| create campaign UUID | shell | randomness |
| choose current timestamp | shell | clock dependency |
| insert SQL row | shell | external state |
| call Ollama | shell | network/model effect |

If a pure function needs the current time, pass it as an argument; do not call the clock inside it.

## 46.2 — Implement composition normalization

File: `app/domain/pipeline.py`

Skeleton: `normalize_composition`

Compute the fraction sum with a fold and use frozen copies. Reject or preserve zero-sum input for validation rather than dividing by zero. Do not mutate the supplied tuple.

## 46.3 — Test idempotence

For valid positive fractions:

$$normalize(normalize(x))=normalize(x).$$

Use a tolerance for floating-point fractions and exact equality for unchanged metadata.

## 46.4 — Implement candidate validation

Skeleton: `validate_candidate`

Return `Result`, not an exception. Check nonempty identity/formula/composition, finite positive physical quantities, fractions, evidence uncertainty, and role-specific assumptions. Error messages must identify the failed invariant without claiming scientific qualification.

## 46.5 — Implement `prepare_candidates`

Compose `map(normalize_composition)`, `map(validate_candidate)`, and `collect_results`. Require at least two candidates so a ranking comparison is meaningful.

## 46.6 — Implement the service boundary

File: `app/services/screening.py`

The service may create IDs/timestamps, call pure ranking functions, persist values, and convert exceptions to typed failures. It may not reimplement the formulas.

## 46.7-46.9 — Wire the dependency container

File: `app/dependencies.py`

Construct one `Database`, repository adapters, security primitives, and services from `Settings`. Initialize/dispose the database in FastAPI lifespan during chapter 52. Keep the container explicit so tests can replace dependencies.

## Acceptance criteria

```bash
CHAPTER=46 make chapter-test
```

- normalization is pure and idempotent;
- validation returns `Err` rather than throwing for domain-invalid input;
- input candidates remain unchanged;
- an AST import test proves the domain layer has no infrastructure dependencies.
