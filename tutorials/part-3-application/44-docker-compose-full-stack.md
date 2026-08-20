# 44 — Docker Compose: One Command for the Entire Lab

## Goal

Operate the API, PostgreSQL, Ollama, model provisioning, secret bootstrap, and chapter-test tooling from one `compose.yaml`.

## 44.1 — Read the service graph

File: `compose.yaml`

The normal profile contains:

- `api`: the FastAPI workshop shell;
- `postgres`: durable relational state;
- `ollama`: local model server;
- `model-pull`: a one-shot model provisioning job.

The `tools` profile contains:

- `init`: create `.env` without host Python;
- `test`: run formatting, linting, typing, scaffold tests, or one chapter's acceptance tests.

Draw the dependency graph and label health versus completion conditions.

## 44.2 — Understand named volumes

PostgreSQL and Ollama use separate named volumes. `make down` preserves them; `make destroy` deletes them. State which command is destructive before running it.

## 44.3 — Generate secrets through Compose

File: `scripts/bootstrap_env.py`

```bash
make init
```

Inspect permissions with `ls -l .env`, but do not paste secret values into logs or commits. Explain why JWT signing and MFA encryption require independent keys.

## 44.4 — Start and observe

```bash
make up
docker compose ps
docker compose logs -f model-pull ollama api
```

The initial model download may be the slowest step. The API must wait for PostgreSQL health and model-pull completion rather than guessing with sleep.

## 44.5 — Activate a chapter test

`CHAPTER` enters only the test service:

```bash
CHAPTER=28 make chapter-test
```

Normal production services must not receive test-only secrets or SQLite URLs.

## Acceptance criteria

```bash
CHAPTER=44 make chapter-test
```

- all six services are defined in one Compose file;
- normal startup excludes `tools` services;
- health/completion dependencies are explicit;
- API and test containers use read-only filesystems and dropped capabilities where practical.
