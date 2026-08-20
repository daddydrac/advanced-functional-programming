# 21 — Classes, Protocols, and Functional Polymorphism

## Goal

Learn object construction, properties, class methods, inheritance, and polymorphism while preferring immutable values and structural interfaces.

Classes are useful for values and effectful adapters. Frozen dataclasses model values. Service classes bundle injected dependencies. SQLAlchemy ORM classes live only in infrastructure because ORM objects have session identity and mutable persistence state.

Python polymorphism is often structural: if a value supplies the required operation, it can satisfy a `Protocol` without inheritance.

```python
from typing import Protocol

class Clock(Protocol):
    def __call__(self) -> datetime: ...
```

Class methods commonly construct from alternate representations. Properties expose computed attributes. Inheritance can share implementation but also couples state; composition of small functions is usually easier to test.

## Lab

Compare frozen `Observation` with SQLAlchemy `ObservationRow`. List which is a domain value and which is a persistence mechanism.

## Checkpoint

Define a `BriefGenerator` protocol and make the Ollama adapter satisfy it structurally. Replace it with a deterministic fake in a test.

Reference coverage: OOP, classes/objects, `__init__`, `self`, properties, class methods, inheritance, and polymorphism.

## Acceptance criteria

- the protocol is satisfied structurally.
- a deterministic fake replaces the external adapter in tests.
- domain code depends on behavior, not a concrete HTTP client.
