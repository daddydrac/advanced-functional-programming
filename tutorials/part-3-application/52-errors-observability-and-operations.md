# 52 — Errors, Health, and Operations

## Goal

Make failures observable without exposing secrets or turning expected domain errors into unstructured 500 responses.

## 52.1 — Classify failure layers

| Failure | Representation |
|---|---|
| invalid composition | domain `Err`, HTTP 422 |
| unauthenticated request | HTTP 401 + `WWW-Authenticate` |
| unauthorized ownership | HTTP 404 or 403 by documented policy |
| PostgreSQL unavailable | readiness failure, HTTP 503 |
| Ollama unavailable | typed adapter error, HTTP 503 |
| programmer invariant violation | logged 500 with correlation ID |

## 52.2 — Preserve safe context

Log correlation ID, route, user ID hash or stable ID, campaign ID, duration, outcome, and error class. Never log passwords, JWTs, TOTP secrets/codes, QR URIs, or unpublished evidence bodies.

## 52.3 — Implement readiness

Files: `app/infrastructure/database.py`, `app/api/health_routes.py`

Database readiness executes `SELECT 1`. Ollama readiness should use its API with a bounded timeout. `/health/ready` succeeds only when dependencies required by the chosen readiness policy are available.

## 52.4 — Dispose resources

Add FastAPI lifespan initialization/disposal. Startup creates/validates schema for the workshop; shutdown disposes the SQLAlchemy engine and HTTP client.

## 52.5 — Measure the useful signals

Define counters/histograms for request latency, auth failures, TOTP replays, candidates per campaign, rejected records, Pareto-front size, Ollama latency/failure, and plan-validation rejection. Do not use high-cardinality material formula as a metric label.

## Acceptance criteria

```bash
CHAPTER=52 make chapter-test
```

- liveness succeeds without dependency checks;
- readiness fails closed when PostgreSQL is unavailable;
- secrets are absent from structured logs;
- shutdown disposes resources;
- adapter timeouts become 503 rather than hanging requests.
