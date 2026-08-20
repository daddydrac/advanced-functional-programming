# 29 — Derive `map`, `filter`, and `flatMap` from `foldr`

## Goal

Show that familiar collection operations are special folds, then use those operators to explore alloy composition spaces without mutation.

The constructor algebra is:

$$
\operatorname{map}(g)=\operatorname{foldr}(\lambda x,xs.\;g(x):xs,[])
$$

$$
\operatorname{filter}(p)=\operatorname{foldr}(\lambda x,xs.\;p(x)?x:xs,[]).
$$

`flatMap` maps one input to zero or more outputs and concatenates exactly one level. In Haskell this is `concatMap`; in many typed languages it is the collection monad's bind.

## Worked example: candidate labels

```python
families = ("W-Ta", "W-V")
fractions = (0.1, 0.2)

def variants(family: str) -> tuple[str, ...]:
    return tuple(map(lambda fraction: f"{family}@{fraction}", fractions))
```

`flatMap(variants, families)` should preserve family order and produce four labels. This example teaches cardinality without revealing capstone scoring.

## 29.1 — Predict cardinality

If there are $m$ base systems and $n$ fractions per system, write the output size of this regular expansion. Then explain why arbitrary `flatMap` has no fixed output-size formula.

## 29.2 — Derive `map_from_fold_right`

File: `app/domain/folds.py`

Add one transformed element to the front of the accumulator. Do not call built-in `map` inside the implementation.

## 29.3 — Derive `filter_from_fold_right`

Choose between adding the current element and returning the unchanged accumulator. Do not mutate a list.

## 29.4 — Derive `flat_map_from_fold_right`

Apply the function once per input and concatenate that finite result before the accumulated tail. Preserve order across both levels.

## 29.5 — Implement `concat`

File: `app/domain/folds.py`

Flatten one iterable level with a fold. Empty input must return the identity `()`.

## Acceptance criteria

```bash
CHAPTER=29 make chapter-test
```

- identity map returns an equal tuple;
- filter preserves relative input order;
- flatMap handles empty inner collections;
- implementations use `fold_right`, not built-in map/filter or loop syntax.
