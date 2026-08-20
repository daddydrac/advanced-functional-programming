# 26 — Composition: Build Scientific Pipelines from Small Functions

## Goal

Implement mathematical composition and left-to-right piping, then use their type boundaries to reason about a materials-data pipeline.

For $g:A\to B$ and $f:B\to C$:

$$
(f\circ g)(x)=f(g(x)).
$$

Composition is valid only when the output type of the inner function matches the input type of the outer function.

## Worked example

These functions are deliberately smaller than the capstone implementation:

```python
def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15

def physically_possible(kelvin: float) -> bool:
    return kelvin >= 0.0
```

`compose(physically_possible, celsius_to_kelvin)(25.0)` should be `True`. `pipe(25.0, celsius_to_kelvin, physically_possible)` computes the same value but reads in data-flow order.

## 26.1 — Trace the order before coding

On paper, expand `compose(f, g, h)(x)` into nested calls. Then expand `pipe(x, f, g, h)`. Mark which fold direction matches each expression.

## 26.2 — Implement `compose`

File: `app/domain/folds.py`

Skeleton: `compose`

Requirements:

- return a new function;
- apply functions from right to left;
- make zero functions behave as identity;
- use a fold, not a loop or comprehension.

Hint: the accumulator is the current value, and each function consumes that value.

## 26.3 — Check referential transparency

Call the composed function twice with the same input. The values must compare equal, and no external state may change. Composition cannot make an impure function pure; document that limit.

## 26.4 — Implement `pipe`

File: `app/domain/folds.py`

Skeleton: `pipe`

Apply functions left to right. Do not implement `pipe` by reversing twice. Choose the fold whose evaluation order already matches the requirement.

## Acceptance criteria

```bash
CHAPTER=26 make chapter-test
```

- `compose(str, abs)(-3)` returns `"3"`.
- `pipe(-3, abs, str)` returns the same value.
- zero-function composition is identity.
- the production AST contains no loop or comprehension nodes.
