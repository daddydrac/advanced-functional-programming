from pathlib import Path

import pytest

pytestmark = pytest.mark.chapter(43)


def test_dockerfile_has_distinct_non_root_production_and_test_targets() -> None:
    dockerfile = Path("Dockerfile").read_text(encoding="utf-8")
    assert "FROM python:3.14.7-slim AS runtime" in dockerfile
    assert "uv sync --frozen --no-dev" in dockerfile
    assert "FROM runtime AS test" in dockerfile
    assert "FROM runtime AS production" in dockerfile
    assert "USER lambdaflux" in dockerfile
