import pytest

from app.domain.result import Err, Ok, Result, bind_result

pytestmark = pytest.mark.chapter(37)


def reciprocal(value: float) -> Result[float, str]:
    return Err("zero") if value == 0 else Ok(1 / value)


def test_bind_flattens_and_short_circuits() -> None:
    assert bind_result(reciprocal, Ok(2.0)) == Ok(0.5)
    assert bind_result(reciprocal, Err("earlier")) == Err("earlier")


def test_monad_identity_and_associativity() -> None:
    def add_one(value: int) -> Ok[int]:
        return Ok(value + 1)

    def double(value: int) -> Ok[int]:
        return Ok(value * 2)

    value = Ok(3)
    assert bind_result(add_one, Ok(3)) == add_one(3)
    assert bind_result(Ok, value) == value
    left = bind_result(double, bind_result(add_one, value))
    right = bind_result(lambda item: bind_result(double, add_one(item)), value)
    assert left == right
