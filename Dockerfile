# syntax=docker/dockerfile:1.7
FROM ghcr.io/astral-sh/uv:0.12.3 AS uv

FROM python:3.14.7-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/srv/.venv/bin:${PATH}"

WORKDIR /srv

COPY --from=uv /uv /uvx /bin/
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app ./app
COPY tutorials /course

RUN groupadd --system lambdaflux \
    && useradd --system --gid lambdaflux --home-dir /nonexistent lambdaflux

USER lambdaflux
EXPOSE 8000

HEALTHCHECK --interval=20s --timeout=3s --start-period=15s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health/live', timeout=2)"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--no-server-header"]

FROM runtime AS test

USER root
RUN uv sync --frozen --no-install-project
COPY tests ./tests
COPY scripts ./scripts
USER lambdaflux

CMD ["sh", "-c", "ruff format --check app tests scripts && ruff check app tests scripts && mypy app && pytest"]

FROM runtime AS production
