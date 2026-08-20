import pytest

from app.domain.folds import fold_left, fold_right

pytestmark = pytest.mark.chapter(28)


def test_fold_directions_are_not_swapped() -> None:
    assert fold_left(lambda state, value: state - value, 0, (1, 2, 3)) == -6
    assert fold_right(lambda value, state: value - state, 0, (1, 2, 3)) == 2


def test_fold_right_preserves_generator_order_and_stack_safety() -> None:
    assert fold_right(lambda value, state: (value, *state), (), (x for x in range(5))) == tuple(
        range(5)
    )
    assert fold_right(lambda _value, count: count + 1, 0, range(10_000)) == 10_000
