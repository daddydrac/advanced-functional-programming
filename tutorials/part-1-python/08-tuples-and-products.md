# 08 — Tuples, Products, and Unpacking

## Goal

Use tuples for immutable ordered data, unpack them safely, and recognize product types.

A tuple fixes order but not necessarily length at runtime. Its type can describe either a record-like product or a homogeneous sequence:

```python
coordinate: tuple[float, float, float] = (1.0, 2.0, 3.0)
values: tuple[float, ...] = (1.0, 2.0, 3.0, 4.0)
```

Access and unpacking do not mutate. “Updating” means constructing a new tuple. Joining means concatenation. `count` and `index` query the value.

Cartesian products explain tuple structure. If $A$ has $m$ possible values and $B$ has $n$, then $A\times B$ has $mn$ pairs. The LambdaFlux tags type `tuple[tuple[str, str], ...]` is an immutable sequence of key/value products.

```python
tags = tuple(sorted({"run": "42", "beam": "on"}.items()))
```

Sorting produces a canonical representation, which helps equality, hashing, caching, and reproducible tests.

## Lab

Inspect where REST dictionaries become sorted tuples in `ObservationInput.to_domain` and where repositories reconstruct them.

## Checkpoint

Write `swap(pair)` and `first(pair)` as pure functions. State their types using type parameters.

Reference coverage: tuples, access, conceptual update by replacement, unpacking, traversal through higher-order functions, joining, and tuple methods.

## Acceptance criteria

- generic `swap` and `first` signatures type-check.
- product cardinality is calculated correctly.
- no tuple is treated as if it were mutable.
