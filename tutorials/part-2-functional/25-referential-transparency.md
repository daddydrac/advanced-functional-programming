# 25 — Referential Transparency and Pure Functions

## Goal

Separate pure calculation from effects and understand why substitution makes code easier to test, parallelize, cache, and explain.

An expression $e$ is referentially transparent when replacing it with its value preserves program behavior. A pure function is deterministic and produces no observable side effects.

```python
def z_score(value: float, stats: RunningStats) -> float:
    deviation = standard_deviation(stats)
    return (value - stats.mean) / deviation if deviation > 0.0 else 0.0
```

Given equal immutable arguments, this returns equal results. It does not read a clock, call PostgreSQL, modify `stats`, or print.

Effects are not forbidden. They are pushed outward: the API receives JSON, repositories transact through SQLAlchemy, and the Ollama client performs HTTP. Each adapter converts effects into values for the core.

## Laws

Purity enables equational reasoning:

$$x=y \Rightarrow f(x)=f(y)$$

It also makes memoization correct when the cache key covers every argument.

## Lab

Classify every function in `app/domain` as pure or impure. Then classify repository and route functions.

## Checkpoint

Refactor a function that calls `datetime.now()` internally so a clock value or clock function becomes an explicit input.

Book mapping: understanding functional programming and pure-function design.

## Acceptance criteria

- clock/time is an explicit dependency.
- equal explicit inputs produce equal outputs.
- hidden global reads and writes are absent from the refactored function.
