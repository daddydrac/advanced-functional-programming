# 28 — `foldl` and `foldr`: The Algebra of Material Collections

## Goal

Implement strict left and right folds, understand association, and choose the correct fold for streaming statistics versus order-preserving construction.

For $[x_1,x_2,x_3]$:

$$
\operatorname{foldl}(f,z,xs)=f(f(f(z,x_1),x_2),x_3)
$$

$$
\operatorname{foldr}(f,z,xs)=f(x_1,f(x_2,f(x_3,z))).
$$

With subtraction and identity $0$, the first expression is $-6$ while the second is $2$. Fold direction disappears only for an associative operation with a compatible identity.

## Worked example: composition labels

```python
labels = ("W", "Ta", "V")
```

A right fold with `lambda symbol, tail: f"{symbol}({tail})"` and `"∅"` yields `W(Ta(V(∅)))`. This is useful for seeing the expression tree; it is not the final implementation.

## 28.1 — Identify the algebra

For each operation—sum, string concatenation, set union, subtraction, and `RunningStats.combine`—write its candidate identity and whether it is associative. Note that floating-point addition is only approximately associative.

## 28.2 — Implement `fold_left`

File: `app/domain/folds.py`

Skeleton: `fold_left`

Use `functools.reduce`. It must consume a generator once, preserve left-to-right evaluation, and use constant Python call-stack depth.

## 28.3 — Implement strict `fold_right`

File: `app/domain/folds.py`

Skeleton: `fold_right`

Requirements:

- support any finite iterable, not only a list;
- associate to the right;
- remain stack-safe for a large finite input;
- preserve original order when constructing tuples.

Hint: a finite Python iterator must become reversible somehow. Name the memory tradeoff in a comment.

## 28.4 — Compare with Haskell

Haskell's lazy `foldr` may produce a prefix of an infinite list when its combining function short-circuits. A strict Python implementation that materializes an iterator cannot. Explain this difference in the function docstring without claiming semantic equivalence.

## 28.5 — Prove direction with a non-associative operation

Add one test using subtraction and another using an expression string. A sum-only test cannot detect a swapped fold direction.

## Acceptance criteria

```bash
CHAPTER=28 make chapter-test
```

- subtraction proves the directions differ;
- the right fold preserves the order of a generator;
- a 10,000-element right fold does not recurse;
- no production loop/comprehension syntax is introduced.
