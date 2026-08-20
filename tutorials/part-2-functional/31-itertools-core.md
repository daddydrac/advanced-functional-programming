# 31 — `itertools` as a Lazy Algebra Toolkit

## Goal

Use standard-library iterator building blocks instead of hand-written iteration.

Key operators include `chain`, `islice`, `takewhile`, `dropwhile`, `accumulate`, `starmap`, `repeat`, `cycle`, `groupby`, `tee`, and `zip_longest`.

```python
from itertools import accumulate
from operator import add

prefix_sums = tuple(accumulate((1, 2, 3, 4), add))
```

`accumulate` produces every fold state; `reduce` returns only the final state. `chain.from_iterable` is a lazy flatten. `groupby` groups adjacent equal keys, so sort or otherwise establish adjacency first.

`tee` can buffer heavily when consumers advance at different speeds. Infinite iterators require a bounding consumer such as `islice` or `takewhile`.

## Lab

Replace a two-sequence concatenation pipeline with `chain`. Use `starmap` to apply a two-argument calibration to a sequence of pairs.

## Checkpoint

Use `accumulate` to produce a running candidate count and compare it with a final left fold.

Book mapping: the `itertools` module and lazy iterator composition.

## Acceptance criteria

- the running and final aggregations are compared.
- iterator exhaustion is tested.
- no unnecessary intermediate list is created.
