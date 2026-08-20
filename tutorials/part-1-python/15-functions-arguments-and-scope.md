# 15 — Functions, Arguments, and Signatures

## Goal

Design functions with positional, keyword, default, variadic, and typed arguments while keeping dependencies explicit.

Functions are values: they can be passed, returned, stored, and composed. Prefer a small signature that says exactly what the computation needs.

```python
from collections.abc import Callable

type Predicate[T] = Callable[[T], bool]

def keep[T](predicate: Predicate[T], values: tuple[T, ...]) -> tuple[T, ...]:
    return tuple(filter(predicate, values))
```

`*args` collects positional arguments; `**kwargs` collects named arguments. They are useful at adapters but can hide a domain contract. Keyword-only parameters make policy choices visible. Defaults should be immutable values.

Closures capture enclosing bindings. Dependency injection passes effectful collaborators—clock, repository, HTTP client—as values rather than importing globals.

## Algebra view

Currying transforms a multi-argument function:

$$f : A\times B\to C \quad\Longleftrightarrow\quad f : A\to(B\to C)$$

Python usually uses `functools.partial` instead of native curried syntax.

## Lab

Inspect the injected `clock` in `AuthService`. Explain how it makes time-dependent code testable.

## Checkpoint

Define a typed `Predicate[T]`, a `Transformer[A, B]`, and a partially applied threshold predicate.

Reference coverage: functions, arguments, positional/keyword arguments, `*args`, `**kwargs`, defaults, scope, and first-class functions.

## Acceptance criteria

- generic callable aliases type-check.
- partial application captures only immutable configuration.
- function inputs and outputs are explicit.
