# 38 — Reader, State, and IO Effects

## Goal

Recognize three common effect patterns and use ordinary Python dependency injection without pretending effects disappear.

Reader represents a computation that needs an environment:

$$\operatorname{Reader}[R,A]\cong R\to A$$

Passing `Settings`, a clock, or repositories into a service is a pragmatic Reader pattern.

State represents a transition:

$$\operatorname{State}[S,A]\cong S\to(A,S)$$

Welford's `append_value(stats, value)` is a pure state transition returning new `RunningStats`.

IO represents an action whose result depends on the world. Python does not enforce an IO type. LambdaFlux makes IO visible through module placement and adapter classes: SQLAlchemy sessions, HTTPX calls, randomness, encryption, and time live outside `app/domain`.

## Lab

Categorize `normalize_composition`, `Database.session`, `TokenCodec.encode`, and `OllamaClient.propose` as pure, Reader-like, State-like, or IO.

## Checkpoint

Refactor a hidden environment lookup into an explicit Reader-style argument. Refactor an in-place accumulator into a State-style return value.

Book mapping: monadic stateful simulations, web-service effects, and controlled procedural exceptions.

## Acceptance criteria

- configuration is passed explicitly Reader-style.
- state transitions return new state plus value.
- IO remains at the module boundary.
