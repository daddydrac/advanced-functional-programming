# 01 — Python, but Function-First

## Goal

Run Python 3.14 without installing Python on the host, understand expressions and statements, and make your first pure transformation.

Python supports procedural, object-oriented, and functional styles. This course deliberately puts a functional core inside an imperative shell. The shell performs unavoidable effects—HTTP, time, randomness, files, and PostgreSQL. The core receives values and returns new values.

```python
def kinetic_energy(mass_kg: float, velocity_m_s: float) -> float:
    return 0.5 * mass_kg * velocity_m_s**2
```

For fixed inputs, the result is fixed. Replacing `kinetic_energy(2.0, 3.0)` with `9.0` cannot change the program. That property is **referential transparency**.

## Container lab

```bash
make init
make up
curl http://localhost:8000/health/live
```

The `Dockerfile` starts from `python:3.14.7-slim`; the host needs Docker, not Python. Open `http://localhost:8000/docs`. Execute `GET /v1/tutorials`, then fetch this lesson by slug.

## Think mathematically

A pure function is a mapping $f : X \to Y$. The signature tells you the domain and codomain; the body tells you the mapping rule.

## Checkpoint

Add a pure `momentum(mass, velocity)` function to a scratch module and verify that two calls with equal arguments are equal. Do not print from inside it; printing is an effect.

Reference coverage: Python introduction, getting started, syntax, output, and comments.

## Acceptance criteria

- The worked example runs in the Compose test container.
- Two equal inputs produce equal outputs with no printing inside the pure function.
- You can identify the input type, output type, and effect boundary.
