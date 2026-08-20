"""Test configuration for scaffold checks and opt-in chapter acceptance tests."""

import os
from base64 import urlsafe_b64encode

import pytest

os.environ.setdefault("JWT_SECRET", "test-secret-that-is-long-enough-for-workshop-tests-only")
os.environ.setdefault("MFA_ENCRYPTION_KEY", urlsafe_b64encode(b"0" * 32).decode())
os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:////tmp/lambdaflux-tests.sqlite3")
os.environ.setdefault("COURSE_DIR", "tutorials")


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Skip acceptance tests except those selected through ``CHAPTER``."""
    active = os.getenv("CHAPTER", "").lstrip("0")
    skip = pytest.mark.skip(reason="set CHAPTER=<number> to activate this milestone")

    def configure(item: pytest.Item) -> None:
        marker = item.get_closest_marker("chapter")
        expected = "" if marker is None else str(marker.args[0]).lstrip("0")
        if marker is not None and active != expected:
            item.add_marker(skip)

    tuple(map(configure, items))
