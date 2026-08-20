# 39 — Lenses: Update Nested Material Evidence without Mutation

## Goal

Implement a typed lens with `get`, `set`, `modify`, and composition, then use it to update one nested property in a frozen value.

A lens from source $S$ to focus $A$ contains:

$$get:S\to A$$

$$set:S\times A\to S.$$

## Worked example

```python
@dataclass(frozen=True)
class Trial:
    temperature_k: float
    label: str

temperature = Lens(
    getter=lambda trial: trial.temperature_k,
    setter=lambda trial, value: replace(trial, temperature_k=value),
)
```

Setting `1300.0` must return a new `Trial`; the original remains unchanged and `label` is preserved.

## 39.1 — Draw the types

For `Lens[MaterialCandidate, MaterialProperties]` composed with `Lens[MaterialProperties, float]`, write the resulting type.

## 39.2 — Implement `get`

File: `app/domain/lenses.py`

Delegate to the stored getter. Do not add caching or hidden state.

## 39.3 — Implement `set`

Use the stored setter and return its new source. The calling convention is value-first on the public method but source-first in the stored callable; trace both argument orders carefully.

## 39.4 — Implement `modify`

Express modify as get, transform, then set. The function must run exactly once.

## 39.5 — Implement composition

The composed getter reads outer then inner. The composed setter must rebuild the inner value and then rebuild the outer value. Do not mutate either object.

## 39.6 — Implement `dataclass_lens`

Use `getattr` and `dataclasses.replace`. A misspelled attribute may fail at runtime; explain why a field-specific constructor is safer in production.

## Acceptance criteria

```bash
CHAPTER=39 make chapter-test
```

- a composed lens changes only the requested nested field;
- original values remain equal to their pre-update snapshots;
- `modify` calls its function once;
- type checking accepts the typed composed lens.
