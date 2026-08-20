# 41 — Concurrency, Multiprocessing, and Parallel Folds

## Goal

Choose threads, processes, or async IO based on workload and exploit monoids for deterministic parallel reduction.

Threads suit blocking IO but share memory. Processes suit CPU-bound Python and isolate memory, with serialization cost. `asyncio`/HTTPX suit many concurrent network waits. `concurrent.futures` gives `map`-oriented thread and process executors.

Pure functions are safer to parallelize because tasks do not race over mutable shared state.

For monoidal statistics:

1. partition material-property records;
2. summarize each partition independently;
3. combine summaries as a reduction tree.

Associativity makes partition placement irrelevant mathematically. Floating-point rounding can make bitwise results differ, so deterministic partitioning may still matter.

The FastAPI process handles IO concurrency. PostgreSQL provides transaction isolation. Ollama is an external service. Do not run CPU-heavy analysis directly on the event loop in a large deployment.

## Lab

Split a tuple into two parts, summarize each, combine them, and compare with one-pass Welford statistics.

## Checkpoint

Design a bounded process-pool adapter whose worker function accepts and returns only frozen, pickle-safe values.

Book mapping: multiprocessing, threading, `concurrent.futures`, performance, and web services.

## Acceptance criteria

- worker inputs/outputs are frozen and pickle-safe.
- parallel and serial reductions agree within documented tolerance.
- worker count and queue depth are bounded.
