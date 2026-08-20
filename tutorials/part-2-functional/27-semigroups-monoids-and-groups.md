# 27 — Algebra: Semigroups, Monoids, and Groups

## Goal

Use algebraic laws to choose safe reductions and parallel combinations.

A semigroup is a set $S$ with an associative binary operation:

$$ (a\oplus b)\oplus c = a\oplus(b\oplus c) $$

A monoid adds an identity $e$:

$$e\oplus a=a=a\oplus e$$

Examples: integers under addition with 0; integers under multiplication with 1; strings or tuples under concatenation with empty; sets under union with empty set.

A group additionally gives every element an inverse. Integers under addition form a group; natural numbers under addition do not.

LambdaFlux's `RunningStats` has `EMPTY_STATS` and an associative `combine` up to floating-point rounding. That permits chunk-local summaries followed by a tree reduction.

## Parallel implication

For a monoid, partitions can be folded independently:

$$\operatorname{fold}(A\mathbin{+\!+}B)=\operatorname{fold}(A)\oplus\operatorname{fold}(B)$$

## Lab

Run `test_parallel_combine_matches_one_pass_fold` and the identity property test.

## Checkpoint

Identify the algebra for “all checks pass,” “any check fails,” evidence concatenation, and maximum utility.

Book mapping: reductions, mathematical/statistical algorithms, monoids, and parallel-safe aggregation.

## Acceptance criteria

- each operation has a stated set, closure rule, and identity when one exists.
- associativity is tested, with floating-point caveats where required.
- invalid “group” claims identify the missing inverse or closure property.
