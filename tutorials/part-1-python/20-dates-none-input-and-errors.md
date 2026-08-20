# 20 — Dates, `None`, Input Boundaries, and Exceptions

## Goal

Handle time zones, optional values, external input, and failures without contaminating the pure core.

Use timezone-aware datetimes. JWT code uses UTC; API models require `AwareDatetime`. A naive datetime has no offset and is ambiguous at daylight-saving boundaries.

`None` is a singleton representing absence, but it carries no explanation. Use `T | None` for ordinary optional lookup and `Result[T, E]` for an operation that can fail meaningfully.

Exceptions are appropriate for unrecoverable adapter failures and framework translation. Expected domain failures are values. FastAPI routes convert `Err` into explicit HTTP status codes.

```python
result = service.get(owner_id, analysis_id)
if isinstance(result, Err):
    raise HTTPException(status_code=404, detail=result.error)
```

Interactive `input()` belongs to a terminal program, not this REST-only system. JSON requests are the input boundary; Pydantic validates them before domain conversion.

## Lab

Create a timezone-naive campaign timestamp in a small Pydantic exercise and inspect the validation failure. Then add UTC information and compare the accepted value.

## Checkpoint

Model a lookup with `Option` and a validation with `Result`. Explain why the types communicate different semantics.

Reference coverage: dates, `None`, user input, try/except, errors, and boundary validation.

## Acceptance criteria

- all stored timestamps are timezone-aware UTC.
- Option and Result use cases are distinguished.
- boundary exceptions become typed/application errors without swallowing defects.
