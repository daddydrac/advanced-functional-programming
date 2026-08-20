# 32 — Combinatorics with `itertools`

## Goal

Generate Cartesian products, permutations, and combinations while predicting cardinality before allocation.

For $n$ distinct items:

$$P(n,r)=\frac{n!}{(n-r)!},\qquad C(n,r)=\frac{n!}{r!(n-r)!}$$

`product(A, B)` has $|A||B|$ pairs. `permutations(xs, r)` respects order; `combinations(xs, r)` does not. `combinations_with_replacement` permits repeated choices.

This matters when comparing alloy-element pairs. Ten elements yield $C(10,2)=45$ unordered pairs; a 10,000-candidate library yields almost 50 million candidate pairs. Laziness delays memory allocation but not total computational work.

## Lab

Generate all unordered element pairs for four symbols. Map an interaction-score function over them and retain only strong relationships.

## Checkpoint

Before executing, calculate the count for a three-parameter grid. Add a maximum-cardinality guard that returns `Err` when the request is unsafe.

Book mapping: `itertools` permutations, combinations, products, and combinatorial complexity.

## Acceptance criteria

- cardinality is calculated before enumeration.
- unsafe grids return `Err` before allocation.
- combinations, permutations, and Cartesian products are distinguished.
