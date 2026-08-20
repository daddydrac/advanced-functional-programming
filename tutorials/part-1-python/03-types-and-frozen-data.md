# 03 — Values, Types, and Frozen Dataclasses

## Goal

Recognize Python's built-in data types and model domain data with explicit, immutable types.

Python values include `int`, `float`, `complex`, `str`, `bool`, `None`, tuples, lists, sets, mappings, bytes, ranges, and callables. Type annotations let tools reject mismatched compositions before runtime.

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Measurement:
    metric: str
    value: float
    unit: str
```

`frozen=True` prevents attribute assignment. `slots=True` makes the layout explicit and usually smaller. The type is a product:

$$\text{Measurement} = \text{Metric} \times \mathbb{R} \times \text{Unit}$$

It contains one value from each component type. `Severity`, by contrast, is a sum-like enumeration: exactly one of normal, watch, warning, or critical.

Run the type checker:

```bash
uv run mypy app
```

Pydantic models guard the REST boundary and are frozen too. Domain dataclasses remain independent from FastAPI, which keeps the mathematical core portable.

## Lab

Inspect `app/domain/models.py` and `app/api_models.py`. Explain why the same concept has an API representation and a domain representation.

## Checkpoint

Create a frozen `Calibration(offset: float, scale: float)` and write a pure function from `(Calibration, Measurement)` to a new `Measurement`.

Reference coverage: data types, type inspection, classes/objects, `__init__`, `self`, and class properties through dataclass-generated behavior.

## Acceptance criteria

- `Calibration` and its nested values use `@dataclass(frozen=True, slots=True)`.
- Mutation raises rather than silently changing history.
- A transformation returns a new typed value and preserves the original.
