# 16 — Lambdas, Decorators, and Generator Functions

## Goal

Use concise anonymous transformations, behavior-preserving decorators, and lazy generator functions deliberately.

A lambda is a one-expression function. Name a function when the logic, type, or error deserves explanation. Lambdas shine as local arguments to `map`, `filter`, `sorted`, and folds.

A decorator maps functions to functions:

$$D : (A\to B) \to (A\to B)$$

It may add logging, timing, authorization, or caching, but should preserve the advertised contract. FastAPI route decorators register functions; they do not contain business logic.

Generator functions suspend and resume. They are lazy, but their internal control flow can obscure purity if they read files or mutate hidden state. Prefer generator expressions or iterator combinators for simple streams and isolate effectful producers.

```python
def traced[A, B](function: Callable[[A], B]) -> Callable[[A], B]:
    def wrapper(value: A) -> B:
        return function(value)
    return wrapper
```

## Lab

Find three lambdas in `pipeline.py` and replace one mentally with a named function. Decide which form communicates better.

## Checkpoint

Write a typed decorator that counts calls in the imperative shell, then explain why the wrapped computation is no longer referentially transparent.

Reference coverage: lambdas, decorators, generators, functions, and scope.

## Acceptance criteria

- decorator metadata is preserved.
- the effect introduced by call counting is documented.
- lazy generator consumption is demonstrated with a terminal operation.
