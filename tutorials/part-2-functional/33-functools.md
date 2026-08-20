# 33 — `functools`: Reduce, Partial, Cache, and Dispatch

## Goal

Use the standard functional helpers with explicit correctness conditions.

`reduce` implements strict left folding. `partial` fixes arguments. `lru_cache` memoizes by hashable arguments. `singledispatch` selects by the first argument's runtime type. `wraps` preserves decorator metadata.

```python
from functools import lru_cache, partial, reduce

product = reduce(lambda acc, x: acc * x, values, 1)
warns = partial(crosses_threshold, threshold=2.5)
```

Cache only referentially transparent results unless you explicitly accept staleness. A cached function that reads PostgreSQL or time can return obsolete state. Frozen dataclasses and tuples make strong cache keys.

The app uses `lru_cache` to construct settings and the dependency container once. That is lifecycle management in the imperative shell, not a pure calculation.

## Lab

Find both cached constructors. Explain what would break if their environment variables changed during process lifetime.

## Checkpoint

Memoize a pure factorial or calibration lookup, then property-test equality with the uncached version.

Book mapping: the `functools` module, reduction, partial application, decorators, caching, and dispatch.

## Acceptance criteria

- cached and uncached pure results are equal.
- cache keys contain only stable hashable inputs.
- effects are not hidden behind memoization.
