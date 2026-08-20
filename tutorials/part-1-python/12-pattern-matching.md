# 12 — Structural Pattern Matching

## Goal

Use `match` to destructure immutable algebraic data instead of asking objects for mutable state.

`Result[T, E]` is a sum type: a value is either `Ok[T]` or `Err[E]`. Pattern matching makes both cases visible:

```python
def unwrap_or[T, E](default: T, result: Result[T, E]) -> T:
    match result:
        case Ok(value):
            return value
        case Err(_):
            return default
```

This resembles Haskell pattern matching. It is safer than returning `None` for every failure because the error branch can carry a reason.

A match can destructure tuples, mappings, dataclasses, literals, and guarded patterns. Include a fallback when external values are open-ended. For a closed sum such as `Ok | Err`, a type checker helps reveal missing variants.

## Lab

Read `map_result`, `bind_result`, and `collect_results` in `app/domain/result.py`. Trace what happens to the first error in a batch.

## Checkpoint

Create `Option[T] = Some[T] | Nothing` and implement `map_option` with `match`. Verify the functor identity law in lesson 40.

Reference coverage: Python `match`, cases, guards through conditions, and functional destructuring.

## Acceptance criteria

- both union branches are handled.
- identity mapping preserves every generated option.
- an unmatched branch cannot silently fall through.
