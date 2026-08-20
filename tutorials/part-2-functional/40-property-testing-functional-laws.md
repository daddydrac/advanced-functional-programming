# 40 — Property Tests: Prove the Lens and Fold Laws

## Goal

Turn algebraic laws into executable Hypothesis properties so implementations are checked across many generated values rather than a few handpicked examples.

## Lens laws

For lens $L$, source $s$, and values $a,b$:

1. Get-put: $set(get(s),s)=s$.
2. Put-get: $get(set(a,s))=a$.
3. Put-put: $set(b,set(a,s))=set(b,s)$.

## 40.1 — Explain what the laws prevent

Give one broken setter for each law: a setter that changes unrelated fields, a setter that clamps the value, and a setter that combines new and old state.

## 40.2 — Implement `law_get_put`

File: `app/domain/lenses.py`

Return a Boolean equality; do not raise inside the law function.

## 40.3 — Implement `law_put_get`

Set the supplied focus and immediately read it back.

## 40.4 — Implement `law_put_put`

Compare two successive sets with only the final set.

## 40.5 — Add fold laws

For tuple concatenation, test identity and associativity. For `map_from_fold_right`, test the identity law and composition law:

$$map(id,xs)=xs$$

$$map(f\circ g,xs)=map(f,map(g,xs)).$$

## 40.6 — Treat floating point honestly

`RunningStats.combine` is associative only up to floating-point rounding. Use `math.isclose` with a justified tolerance. Never weaken equality for exact tuple or lens laws.

## Acceptance criteria

```bash
CHAPTER=40 make chapter-test
```

- all three lens laws pass for generated nested dataclasses;
- tuple-monoid laws pass exactly;
- statistical laws use documented tolerances;
- Hypothesis can shrink a deliberately broken lens to a minimal counterexample.
