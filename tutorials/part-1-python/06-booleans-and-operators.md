# 06 — Predicates, Boolean Algebra, and Operators

## Goal

Use arithmetic, comparison, logical, identity, membership, bitwise, conditional, and precedence rules to build explicit predicates.

A predicate has type $P : X \to \{\text{False},\text{True}\}$. Predicates compose through Boolean algebra:

$$\neg(P\land Q) = (\neg P)\lor(\neg Q)$$

```python
def crosses_threshold(score: float, threshold: float) -> bool:
    return abs(score) >= threshold
```

`==` compares values; `is` compares identity and is appropriate for singleton sentinels and enum members. `in` tests membership. `and`, `or`, and `not` short-circuit. Parentheses make precedence visible.

Assignment operators imply mutation and are rare in the pure core. Bitwise operators act on integer bit patterns and should not be confused with Boolean operators.

Conditional expressions are expressions, so they fit transformations:

```python
deviation = (value - mean) / scale if scale > 0.0 else 0.0
```

## Lab

Design a pure feasibility predicate for a plasma-facing material. Write its melting-point, conductivity, stability, and activation thresholds as mathematical intervals.

## Checkpoint

Define `all_pass` using `all(map(predicate, values))` and `any_fail` using a De Morgan equivalent. Property-test that the two descriptions agree.

Reference coverage: booleans; arithmetic, assignment, ternary, comparison, logical, identity, membership, and bitwise operators; operator precedence.

## Acceptance criteria

- De Morgan equivalents pass generated tests.
- boundary comparisons are explicit.
- predicates do not mutate or perform I/O.
