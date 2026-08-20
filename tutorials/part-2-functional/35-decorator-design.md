# 35 — Functional Decorator Design

## Goal

Write typed decorators, preserve metadata, and distinguish pure wrappers from effectful cross-cutting behavior.

A decorator transforms one callable into another. A contract-preserving decorator keeps input and output types:

```python
from collections.abc import Callable
from functools import wraps

def validate_finite[A, B](fn: Callable[[A], B]) -> Callable[[A], B]:
    @wraps(fn)
    def wrapped(value: A) -> B:
        return fn(value)
    return wrapped
```

Timing, tracing, retries, authorization, transactions, and caching are decorators conceptually. They are effects or policies, so apply them at boundaries. Retrying a non-idempotent database write can duplicate work.

FastAPI's route decorators register the endpoint and its OpenAPI metadata. Domain functions remain framework-free.

## Lab

Inspect a route decorator and identify what OpenAPI contract it creates. Confirm the underlying service returns domain values.

## Checkpoint

Design an exponential-backoff decorator for the Ollama adapter. State why it must not wrap password verification or non-idempotent registration blindly.

Book mapping: decorator design techniques, metadata, typing, caching, and effect policies.

## Acceptance criteria

- retry applies only to idempotent adapter calls.
- backoff and maximum attempts are bounded.
- password and registration operations are explicitly excluded.
