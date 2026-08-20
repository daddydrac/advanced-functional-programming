# 36 — `Result`: Make Missing and Invalid Evidence Explicit

## Goal

Represent success and failure as values so a material record cannot silently flow through screening after validation fails.

The provided sum type is:

$$
\operatorname{Result}(T,E)=\operatorname{Ok}(T)+\operatorname{Err}(E).
$$

This is a tagged union: exactly one branch exists at a time.

## Worked example

```python
def positive(value: float) -> Result[float, str]:
    return Ok(value) if value > 0 else Err("must be positive")
```

Unlike an exception, the possibility of failure appears in the return type. The caller must pattern-match or use a combinator.

## 36.1 — Trace both channels

For `map_result(lambda x: x * 2, result)`, write the output for `Ok(3)` and `Err("missing")`. The function must never run on the error branch.

## 36.2 — Implement `map_result`

File: `app/domain/result.py`

Use pattern matching or `isinstance`. Preserve the exact error value and type.

## 36.3 — Implement `collect_results`

Turn `Iterable[Result[T,E]]` into `Result[tuple[T,...],E]`. Use a fold and return the first error in input order.

## 36.4 — Decide error policy explicitly

First-error behavior is not error accumulation. Write a note explaining when a validation applicative that collects every failure would be preferable.

## 36.5 — Implement `unwrap_or`

Return the success value or the caller's default. Do not treat falsey successes such as `0` as errors.

## Acceptance criteria

```bash
CHAPTER=36 make chapter-test
```

- mapping preserves `Err` unchanged;
- collection stops at the first ordered error;
- empty collection produces `Ok(())`;
- `unwrap_or(9, Ok(0))` returns `0`.
