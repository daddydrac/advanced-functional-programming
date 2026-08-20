# 13 — Replacing `while` with State Transitions

## Goal

Understand what a `while` loop represents, then model repetition with recursion, folds, iterators, or explicit state transitions.

A `while` loop repeatedly mutates state while a predicate is true. Functional design separates the transition from the repetition mechanism:

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Decay:
    time: int
    particles: float

def step(state: Decay) -> Decay:
    return replace(state, time=state.time + 1, particles=state.particles * 0.5)
```

Now `step` is testable without a clock or loop. A finite simulation can apply it with a left fold over `range(steps)`. An unbounded stream belongs in an iterator abstraction with a termination consumer.

The important distinction is between **what changes mathematically** and **how Python schedules repeated application**. Keep the first pure.

## Lab

Use `fold_left(lambda state, _: step(state), initial, range(10))`. Predict the particle count using $N_t=N_0(1/2)^t$.

## Checkpoint

Model Newton iteration as a pure `step(guess)` and apply exactly $n$ steps with a fold. Do not use loop syntax.

Reference coverage: while-loop purpose, termination, and the functional state-transition alternative.

## Acceptance criteria

- iteration count is explicit input data.
- Newton steps use a fold and terminate predictably.
- production-style example code contains no `while`.
