# 17 — Recursion versus Reduction

## Goal

Understand base cases, recursive cases, stack limits, and why folds are usually the production choice in Python.

A recursive list sum follows the inductive definition:

$$\operatorname{sum}([])=0,\qquad \operatorname{sum}(x:xs)=x+\operatorname{sum}(xs)$$

Python does not optimize tail calls, so deep recursion can exhaust the call stack. `functools.reduce` performs a strict left fold in constant Python stack space. LambdaFlux implements `fold_right` by reversing a finite tuple and reducing, also avoiding recursive stack growth.

Structural recursion is still useful for trees when depth is bounded. Divide-and-conquer algorithms can recurse logarithmically. The key is to know the maximum depth and memory behavior.

## Lab

Compare the equations for factorial and list sum with `fold_left`. Determine the identity and binary operation for each.

## Checkpoint

Implement factorial with a fold over `range(1, n + 1)`. State why multiplication with identity 1 forms a monoid over nonnegative integers.

Reference coverage: recursion, ranges, reductions, base cases, and Python stack behavior.

## Acceptance criteria

- factorial handles zero through identity `1`.
- fold and recursive results agree on safe small inputs.
- stack-depth limitations are stated.
