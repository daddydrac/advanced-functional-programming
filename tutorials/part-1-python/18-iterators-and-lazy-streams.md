# 18 — Iterators, Generators, and Lazy Evaluation

## Goal

Distinguish iterable from iterator, consume streams once, and control when computation happens.

An iterable can produce an iterator. An iterator supplies successive values and is stateful internally. `map`, `filter`, `zip`, and many `itertools` functions return lazy iterators.

```python
normalized = map(normalize_composition, incoming)
valid = map(validate_candidate, normalized)
result = collect_results(valid)
```

Nothing upstream is evaluated until the terminal fold consumes the stream. This supports bounded-memory pipelines: if each stage retains only its current element, auxiliary memory is $O(1)$.

Laziness also delays exceptions and effects. Document who owns consumption. Do not reuse an exhausted iterator; materialize a tuple when replay or stable identity matters.

## Lab

Insert a temporary pure counting wrapper around a `map` stage. Observe that construction performs no work and tuple conversion consumes it.

## Checkpoint

Build a lazy pipeline that parses numeric strings, removes invalid results through `Result`, and summarizes valid numbers with a terminal fold.

Reference coverage: iterators, generator expressions/functions, lazy evaluation, range, and collection traversal.

## Acceptance criteria

- transformation stages remain lazy until the terminal fold.
- invalid numeric strings remain typed failures.
- the iterator is not accidentally consumed twice.
