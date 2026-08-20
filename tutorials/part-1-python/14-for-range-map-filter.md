# 14 — Replacing `for` with `map`, `filter`, and `range`

## Goal

Recognize iteration intent and select the higher-order operator that states it directly.

Use:

- `map(f, xs)` for one output per input;
- `filter(p, xs)` to retain matching inputs;
- `flat_map(f, xs)` for zero or many outputs per input;
- `fold` to summarize;
- `zip` to align sequences;
- `enumerate` when position is data;
- `range` to represent an arithmetic progression.

```python
scaled = tuple(map(lambda x: x * 1_000.0, voltages))
large = tuple(filter(lambda x: abs(x) >= threshold, scaled))
```

The structure exposes cardinality. `map` preserves length; `filter` cannot increase it; `flatMap` may do either. These facts help reason about memory and API payload limits.

`range(start, stop, step)` is lazy and does not allocate every integer. It is useful as a finite index domain even though most domain transformations should not need indexes.

## Lab

Read the `rank_candidates` skeleton: scoring will be `map`, infeasible removal will be `filter`, and presentation order will be `sorted`.

## Checkpoint

Turn a candidate library into `(formula, melting_point_k)` pairs, retain values above a toy threshold, and average them. Express the full pipeline without loop or comprehension syntax.

Reference coverage: `for`, `range`, traversal, break/continue intent through higher-order operators, and loop-free collection processing.

## Acceptance criteria

- mapping, filtering, and terminal reduction are visibly separate stages.
- empty retained input has defined behavior.
- no loop or comprehension syntax is used.
