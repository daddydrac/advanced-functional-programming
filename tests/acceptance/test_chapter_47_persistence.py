import pytest

from app.infrastructure.database import Database
from app.infrastructure.repositories import candidate_to_payload, payload_to_candidate
from tests.factories import candidate

pytestmark = pytest.mark.chapter(47)


def test_candidate_payload_round_trip() -> None:
    source = candidate()
    assert payload_to_candidate(candidate_to_payload(source)) == source


def test_session_rolls_back_and_remains_usable(tmp_path) -> None:
    database = Database(f"sqlite+pysqlite:///{tmp_path / 'chapter47.sqlite3'}")
    database.initialize()
    with pytest.raises(RuntimeError), database.session() as session:
        session.execute(__import__("sqlalchemy").text("CREATE TABLE transient (id INTEGER)"))
        raise RuntimeError("force rollback")
    assert database.ready()
    database.dispose()
