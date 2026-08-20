# 47 — SQLAlchemy and PostgreSQL: Persist without Domain Leakage

## Goal

Implement transaction boundaries and owner-scoped repositories while ensuring mutable SQLAlchemy rows never escape into the frozen domain.

## 47.1 — Inspect the supplied schema

File: `app/infrastructure/database.py`

Tables store users, material candidates, screening campaigns, experiment plans, revoked tokens, and auth failures. JSON columns preserve nested educational records, but query-heavy production properties may deserve normalized tables.

## 47.2 — State the impedance mismatch

ORM rows participate in a mutable session identity map. Domain dataclasses are frozen values. A repository converts between them so pure code cannot lazy-load, accidentally update a row, or depend on session lifetime.

## 47.3 — Implement `Database.__init__`

Create an engine with `pool_pre_ping=True` and a session factory with `expire_on_commit=False`. Add SQLite's thread option only when the URL begins with SQLite; chapter tests use SQLite while Compose uses PostgreSQL.

## 47.4 — Implement the session context manager

Required state machine:

1. create session;
2. yield it;
3. commit on success;
4. roll back and re-raise on failure;
5. close in every path.

Catch `BaseException` at this cleanup boundary so cancellation also rolls back, but never swallow it.

## 47.5 — Initialize metadata

Use the provided `Base.metadata`. In a production extension, replace create-all with Alembic migrations.

## 47.6-47.9 — Implement boundary mappings

File: `app/infrastructure/repositories.py`

Map datetimes to aware UTC values, reconstruct enums explicitly, preserve tuple order, and validate JSON rather than blindly casting. Round-trip tests must compare frozen domain values.

## 47.10-47.14 — Implement writes and queries

Every method gets a short session. Batch candidate inserts. Use deterministic ordering. Convert after the query but before returning.

## 47.15 — Enforce ownership in SQL

`CampaignRepository.by_id(owner_id, campaign_id)` must include both predicates. Do not load by campaign ID and check ownership later; that creates an avoidable authorization gap.

## Acceptance criteria

```bash
CHAPTER=47 make chapter-test
```

- a candidate round-trips through SQLite into an equal frozen value;
- a forced exception rolls back and closes the session;
- a second owner cannot load the first owner's campaign;
- no SQLAlchemy type appears in a domain function signature.
