# 43 — Docker Images: Package an Incomplete Workshop Safely

## Goal

Understand the supplied multi-stage Dockerfile, verify Python and dependency reproducibility, and distinguish the production and acceptance-test targets.

## 43.1 — Inspect the stages

File: `Dockerfile`

Identify:

1. the pinned `uv` tool image;
2. the Python slim runtime base;
3. the layer that installs only locked runtime dependencies;
4. the test target that adds development dependencies and tests;
5. the final production target.

Explain why copying `pyproject.toml` and `uv.lock` before application source improves layer reuse.

## 43.2 — Verify the image, not the host

```bash
docker compose build api
docker compose run --rm api python --version
docker compose run --rm api python -c "import fastapi, sqlalchemy"
```

The command must run inside the Compose-defined image. A successful host import proves nothing about the container.

## 43.3 — Examine runtime privilege

```bash
docker compose run --rm api id
```

The API must not run as root. Locate `USER`, `read_only`, `cap_drop`, and `no-new-privileges`. Explain which control belongs to the image and which belong to Compose.

## 43.4 — Preserve the teaching loop

The production image may contain incomplete functions; that is intentional. The image must still import the FastAPI course shell and serve tutorial routes. Do not replace `NotImplementedError` with fake return values merely to make a build green.

## Acceptance criteria

```bash
CHAPTER=43 make chapter-test
```

- Python runs from the pinned slim base.
- dependency installation honors `uv.lock`.
- the final user is non-root.
- solution files, caches, `.env`, and local databases are absent from the image.
