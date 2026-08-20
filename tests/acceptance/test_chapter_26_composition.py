import pytest

from app.domain.folds import compose, pipe

pytestmark = pytest.mark.chapter(26)


def test_composition_and_pipe_orders() -> None:
    def absolute(value: object) -> int:
        return abs(int(value))

    def stringify(value: object) -> str:
        return str(value)

    assert compose(stringify, absolute)(-3) == "3"
    assert pipe(-3, absolute, stringify) == "3"


def test_empty_composition_is_identity() -> None:
    marker = object()
    assert compose()(marker) is marker
