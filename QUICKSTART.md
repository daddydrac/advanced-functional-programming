# Quickstart: Learn by Making the Tests Pass

## 1. Prerequisite

Install Docker Desktop with Docker Compose. No host Python, PostgreSQL, or Ollama installation is required.

## 2. Generate local secrets

```bash
make init
```

The Compose `init` service creates `.env` with unique database, JWT, and MFA-encryption secrets and refuses to overwrite it.

## 3. Start the workshop shell

```bash
make up
docker compose ps
```

Open `http://localhost:8000/docs`. These routes work before any exercise is implemented:

- `GET /`
- `GET /health/live`
- `GET /v1/tutorials`
- `GET /v1/tutorials/{slug}`

Capstone routes appear in Swagger but return HTTP 501. That is expected: the response points to the chapter item you must complete.

## 4. Work in dependency order

| Milestone | Chapters | Outcome |
|---|---:|---|
| Functional vocabulary | 01-25 | Python, immutability, pure functions |
| Composition and folds | 26-29 | `compose`, `foldl`, `foldr`, map/filter/flatMap |
| Effects and optics | 30-40 | laziness, `Result`, monadic bind, lenses, laws |
| Service foundations | 41-46 | Docker, REST schemas, pure core/imperative shell |
| Durable and secure API | 47-49 | SQLAlchemy/PostgreSQL, JWT, Google Authenticator MFA |
| Scientific workflow | 50-51 | Pareto screening and local Ollama experiment planning |
| Operations and integration | 52-54 | health, end-to-end REST flow, extensions |

Run the test for only the active chapter:

```bash
CHAPTER=28 make chapter-test
```

The first run should fail. Implement only the referenced skeletons, rerun until green, then commit before moving forward.

## 5. Use the teaching dataset

`data/sample-fusion-candidates.json` contains research-inspired but entirely synthetic properties. After chapter 50, submit the whole document to `POST /v1/campaigns/screen`; the required top-level disclaimer keeps the teaching-data boundary visible in every request.

## 6. Stop or destroy

```bash
make down
```

To permanently delete the PostgreSQL and Ollama volumes:

```bash
make destroy
```
