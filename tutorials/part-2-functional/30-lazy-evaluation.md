# 30 — Lazy Evaluation and Streaming Memory

## Goal

Build memory-efficient pipelines and understand when laziness changes evaluation timing.

`map` and `filter` are lazy in Python 3. Chaining them builds a recipe. A terminal consumer—tuple, list, sum, max, fold, or HTTP serializer—runs it.

For $n$ inputs, an eager pipeline with three intermediate arrays can require $O(n)$ memory at each stage. A lazy pipeline with a streaming left fold uses $O(1)$ auxiliary memory, excluding the final output.

```python
values = map(parse_value, lines)
valid = filter(is_ok, values)
stats = fold_left(append_result, EMPTY_STATS, valid)
```

Do not confuse lazy with pure. Reading a file lazily still performs I/O. Also avoid holding a database session open while a response consumes a lazy ORM result; materialize frozen domain values inside the repository boundary.

## Lab

Trace when `prepare_candidates` consumes its mapped validation results. Identify where replayability requires a tuple.

## Checkpoint

Design a million-candidate property summarizer whose memory is independent of input count. Explain where batching would enter the PostgreSQL adapter.

Book mapping: generator expressions/functions, lazy evaluation, memory efficiency, and data-stream processing.

## Acceptance criteria

- laziness is demonstrated before terminal consumption.
- memory use is independent of input count for the streaming summary.
- materialization points are justified.
