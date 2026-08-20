import pytest
from fastapi.testclient import TestClient

from app.infrastructure.database import Database
from app.main import app

pytestmark = pytest.mark.chapter(52)


def test_liveness_and_database_readiness(tmp_path) -> None:
    with TestClient(app) as client:
        assert client.get("/health/live").status_code == 200
    database = Database(f"sqlite+pysqlite:///{tmp_path / 'ready.sqlite3'}")
    database.initialize()
    assert database.ready()
    database.dispose()
