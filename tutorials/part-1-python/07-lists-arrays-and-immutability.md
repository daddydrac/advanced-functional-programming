# 07 — Lists, Arrays, and Immutable Sequences

## Goal

Understand mutable lists and array-like data while choosing tuples at domain boundaries.

Lists support access, replacement, insertion, removal, sorting, copying, joining, and methods. Those operations are useful, but mutation makes behavior depend on history. LambdaFlux accepts REST arrays and converts them to tuples.

```python
values: tuple[float, ...] = (10.0, 10.2, 9.8)
scaled = tuple(map(lambda value: value * 1_000.0, values))
```

The output order is determined only by the input order. `sorted(values)` returns a list; wrap it in `tuple` when the result enters the immutable core. A Python “array” tutorial often means lists; numeric workloads may later use `array`, NumPy, or Arrow, but the algebra remains sequence transformation.

An array fold reduces $[x_1,\dots,x_n]$ to one value:

$$\operatorname{foldl}(\oplus,z,[x_1,\dots,x_n]) = (((z\oplus x_1)\oplus x_2)\dots\oplus x_n)$$

Lesson 28 gives both fold directions and derives other operators from `foldr`.

## Lab

Use `map_from_fold_right` to double a tuple. Confirm the source tuple is unchanged.

## Checkpoint

Model a candidate library as `tuple[MaterialCandidate, ...]`. Provide pure add, remove-by-ID, and sort-by-formula functions that return new tuples.

Reference coverage: lists, access/change/add/remove concepts, traversing without loop syntax, comprehension alternatives, sorting, copying, joining, list methods, and arrays.

## Acceptance criteria

- add, remove, and sort return tuples.
- the original candidate tuple remains unchanged.
- traversal uses higher-order functions rather than loop/comprehension syntax.
