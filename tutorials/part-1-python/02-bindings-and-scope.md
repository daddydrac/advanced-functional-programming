# 02 — Bindings, Names, and Scope

## Goal

Learn variables, legal names, multiple assignment, output values, and scope without treating a name as a box that must be mutated.

In functional code, prefer a sequence of meaningful bindings:

```python
raw_voltage = 2.75
gain = 4.0
calibrated_voltage = raw_voltage * gain
```

The names form a tiny proof: given the two inputs, the output follows. Reassigning `raw_voltage` later would weaken that reasoning. Python does not enforce single assignment, so we enforce it by design.

Multiple unpacking is useful when it reveals structure:

```python
formula, property_name, value = ("W70Ta30", "melting_point_k", 3480.0)
```

Avoid global mutable state. Pass configuration as an argument or capture immutable configuration in a closure. A local name has lexical scope: Python resolves it in the current function, then enclosing functions, then the module, then built-ins.

## Algebra view

Substitution is safe when bindings do not change:

$$y = f(x),\quad z = g(y) \Rightarrow z = g(f(x))$$

That is the bridge from ordinary variables to composition.

## Lab

Read `app/domain/pipeline.py`. Identify the future bindings required by `normalize_composition`. Each one should name a value; the original candidate must never be overwritten.

## Checkpoint

Rewrite a three-step calibration as three immutable bindings, then collapse it into a composition in lesson 26.

Reference coverage: variables, names, assigning multiple values, output variables, global variables, and function scope.

## Acceptance criteria

- The calibration uses immutable local bindings and no global state.
- Rebinding a name is distinguished from mutating a value.
- The material example produces the same result on repeated calls.
