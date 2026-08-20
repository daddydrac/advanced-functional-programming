# 11 — Branching as Piecewise Functions

## Goal

Use `if`, `elif`, `else`, logical conditions, nesting, shorthand expressions, and `pass` while keeping decision functions total.

An `if` chain defines a piecewise function:

$$
f(x)=\begin{cases}
\text{critical} & |x|\ge 1.75t\\
\text{warning} & |x|\ge t\\
\text{watch} & |x|\ge 0.65t\\
\text{normal} & \text{otherwise}
\end{cases}
$$

Every input reaches a return, so the function is total over its declared domain. Nested conditionals often become clearer as small named predicates and early returns. A conditional expression is suitable for one small value choice; do not compress an entire decision tree.

`pass` is a syntactic placeholder, not an implementation. This repository avoids placeholders in operational paths.

## Lab

Read `feasibility_reasons` in `app/domain/pipeline.py`. Test property values exactly at every policy threshold and just to either side.

## Checkpoint

Write a total piecewise classifier for normalized evidence uncertainty. Express the same partition as mathematical intervals and prove no interval overlaps ambiguously.

Reference coverage: `if`, `elif`, `else`, shorthand conditions, logical operators, nested conditions, and the `pass` statement.

## Acceptance criteria

- intervals cover the full normalized uncertainty domain.
- no two branches ambiguously own the same boundary.
- out-of-domain input has an explicit result.
