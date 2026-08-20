# 05 — Strings as Immutable Sequences

## Goal

Use indexing, slicing, methods, concatenation, formatting, escapes, and regular expressions as pure text transformations.

Strings are immutable sequences. Operations return new strings:

```python
def canonical_label(value: str) -> str:
    return "_".join(filter(None, map(str.strip, value.casefold().split())))
```

This composes `casefold`, `split`, `map`, `filter`, and `join`. There is no index counter and no changing accumulator.

Slicing `text[start:stop:step]` returns a new string. Membership is a predicate. F-strings render values at the effect boundary:

```python
evidence = f"z={score:.3f}"
```

Use raw strings for regular-expression patterns. Treat a compiled pattern as an immutable parser:

```python
from re import compile

TOTP = compile(r"^\d{6}$")
```

Pydantic applies that same rule to MFA input. A regex recognizes a regular language; it is not a general parser for nested structures.

## Lab

Call `normalize_text(" Pulse   Height ")` and predict the output before running it. Test slicing and escaping in a scratch route response.

## Checkpoint

Create a pipeline that trims, validates, and formats a material identifier such as `synthetic-w53ta42v5`. Make every stage separately testable.

Reference coverage: strings, slicing, modification, concatenation, formatting, escape characters, string methods, string formatting, and regex.

## Acceptance criteria

- Each string stage is a separate pure function.
- valid and invalid material IDs have tests.
- formatting never changes the input string object or hidden state.
