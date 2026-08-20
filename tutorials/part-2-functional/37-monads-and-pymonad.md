# 37 — Monadic Bind: Sequence Calculations that May Fail

## Goal

Implement `bind_result`, understand why `map` is insufficient for a function returning `Result`, and test the monad laws.

If $f:A\to Result[B,E]$, ordinary mapping over `Result[A,E]` produces a nested `Result[Result[B,E],E]`. Bind removes that extra layer:

$$
\operatorname{bind}:Result[A,E]\to(A\to Result[B,E])\to Result[B,E].
$$

## Worked example

```python
def reciprocal(value: float) -> Result[float, str]:
    return Err("division by zero") if value == 0 else Ok(1 / value)
```

Binding `reciprocal` after a parsed numeric result propagates either parsing failure or zero failure without nested conditionals.

## 37.1 — Compare map and bind types

Write the static type of mapping `reciprocal` over `Ok(2.0)`. Then write the type produced by binding it.

## 37.2 — Implement `bind_result`

File: `app/domain/result.py`

Run the provided function only for `Ok`. Return `Err` unchanged.

## 37.3 — Test left and right identity

For `pure = Ok`:

$$
pure(a) >>= f = f(a)
$$

$$
m >>= pure = m.
$$

Use both success and failure examples.

## 37.4 — Test associativity

$$
(m >>= f) >>= g = m >>= (\lambda x. f(x) >>= g).
$$

The equality is about observable `Result` values, not evaluation timing of impure functions. Keep test functions pure.

## 37.5 — Compare PyMonad

Recreate the reciprocal example with PyMonad's `Either`. Record what becomes shorter and what becomes less explicit for a Python learner. LambdaFlux keeps the small local algebra so every branch remains inspectable.

## Acceptance criteria

```bash
CHAPTER=37 make chapter-test
```

- `Err` short-circuits without calling the next function;
- nested results are flattened;
- left identity, right identity, and associativity pass.
