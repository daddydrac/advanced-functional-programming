# 19 — Modules, Packages, `pip`, `uv`, and Virtual Environments

## Goal

Understand imports, package boundaries, dependency resolution, pinned environments, and why Docker does not replace a lockfile.

Every `app` directory containing `__init__.py` is a package. Imports express dependencies. The dependency direction is intentional:

```text
api/services → infrastructure/domain
infrastructure → domain
domain → standard library only
```

The pure domain never imports FastAPI, SQLAlchemy, PostgreSQL, or Ollama.

`pip` installs distributions. A virtual environment isolates their import paths. This project uses `uv` to resolve `pyproject.toml` into `uv.lock`. The Docker build runs `uv sync --frozen`, so a changed dependency declaration without a matching lock fails.

Containers isolate operating-system files; virtual environments isolate Python packages. Use both for reproducibility.

```bash
uv sync --dev --frozen
uv run pytest
```

## Lab

Inspect `pyproject.toml`, `uv.lock`, and the two Docker stages. Find the exact Python, FastAPI, SQLAlchemy, and psycopg versions.

## Checkpoint

Explain why `latest` is acceptable for a learning-only Ollama image but exact database and Python tags reduce surprise. Propose a digest-pinning production policy.

Reference coverage: modules, imports, packages, pip, virtual environments, and dependency management.

## Acceptance criteria

- runtime dependencies are locked.
- image-tag and digest tradeoffs are explained.
- all required commands have Compose equivalents.
