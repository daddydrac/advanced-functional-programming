import pytest

from app.domain.result import Err, Ok, collect_results, map_result, unwrap_or

pytestmark = pytest.mark.chapter(36)


def test_result_functor_and_collection_behavior() -> None:
    assert map_result(lambda value: value * 2, Ok(3)) == Ok(6)
    assert map_result(lambda value: value * 2, Err("bad")) == Err("bad")
    assert collect_results((Ok(1), Ok(2))) == Ok((1, 2))
    assert collect_results((Ok(1), Err("first"), Err("second"))) == Err("first")
    assert collect_results(()) == Ok(())
    assert unwrap_or(9, Ok(0)) == 0
