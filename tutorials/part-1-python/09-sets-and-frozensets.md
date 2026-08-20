# 09 — Sets, Frozensets, and Set Algebra

## Goal

Use uniqueness, membership, union, intersection, difference, and symmetric difference without mutable set updates.

`set` is mutable; `frozenset` is immutable and hashable. Sets are unordered, so never rely on display order.

```python
required = frozenset(("sub", "jti", "exp"))
present = frozenset(payload)
missing = required - present
```

For sets $A$ and $B$:

- union $A\cup B$ contains either;
- intersection $A\cap B$ contains both;
- difference $A\setminus B$ contains only $A$;
- symmetric difference $A\triangle B$ contains exactly one side.

Membership is usually average $O(1)$ for hashable values. A frozen dataclass is hashable when all fields are hashable, which makes value-oriented modeling work naturally with sets.

## Lab

In `group_stats`, a `frozenset` extracts unique metric names before each metric is summarized.

## Checkpoint

Given supplied chemical symbols and an allowed-element inventory, compute unknown, missing, and valid symbols as three pure set expressions.

Reference coverage: sets, access through membership, add/remove concepts via new-set construction, traversal through higher-order functions, joins, frozenset, and set methods.

## Acceptance criteria

- unknown, missing, and valid symbols are correct disjoint/set expressions.
- inputs are `frozenset` values.
- membership behavior is covered by tests.
