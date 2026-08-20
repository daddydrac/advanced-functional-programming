# 34 — Toolz Pipelines and Curried Functions

## Goal

Use `toolz` when its vocabulary makes a transformation clearer than custom helpers.

Toolz offers `pipe`, `compose`, curried functions, `curry`, `partition`, `groupby`, `frequencies`, `merge`, and iterator variants.

```python
from toolz import compose, curry, pipe

@curry
def scale(factor: float, value: float) -> float:
    return factor * value

millivolts = scale(1_000.0)
result = pipe(2.3, millivolts, abs)
```

Third-party abstractions create dependency cost. Prefer them when the team shares the vocabulary and the operation is well tested. This course implements small folds directly so their mechanics remain visible, then compares Toolz equivalents.

## Lab

Recreate `normalize_text` with `toolz.pipe`. Compare readability and type-checker precision.

## Checkpoint

Use curried Toolz functions to create reusable threshold-specific analysis stages. Ensure no mutable partial state is captured.

Book mapping: the Toolz package, currying, composition, iterator utilities, and collection transformations.

## Acceptance criteria

- curried stages can be reused with two thresholds.
- no mutable partial state is captured.
- Toolz behavior is compared with the local fold utilities.
