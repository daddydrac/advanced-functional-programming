# 42 — A Functional Approach to Web Services

## Goal

Design HTTP routes as thin translators around pure domain functions and explicit effect adapters.

Each route follows:

$$\text{HTTP input}\to\text{validated DTO}\to\text{use case}\to\text{domain Result}\to\text{HTTP output}$$

The route owns protocol concerns: status, headers, authentication dependency, and response schema. The service orchestrates. The domain calculates. The repository performs transactions.

Idempotence matters. `GET` should not mutate. `POST /v1/campaigns/screen` creates a stored result. Token refresh revokes the prior refresh token, so retry semantics must be understood.

Authorization is applied before owner-scoped repository lookups. An analysis ID alone is insufficient; queries require `(owner_id, analysis_id)`.

FastAPI derives OpenAPI from annotations and Pydantic models. Swagger is the only interactive client in this course, proving the backend is complete without a frontend.

## Lab

Trace the planned `POST /v1/campaigns/screen` flow and mark each pure/effect boundary before implementing it in chapter 53.

## Checkpoint

Design a `GET /v1/materials` route that returns only the authenticated owner's frozen candidates. Keep SQLAlchemy out of the response model.

Book mapping: a functional approach to web services, concurrency, typing, and effect isolation.

## Acceptance criteria

- the proposed route is owner-scoped.
- response models contain no ORM objects.
- HTTP status mapping occurs outside the domain layer.
