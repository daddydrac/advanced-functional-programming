import pytest

from app.domain.folds import (
    concat,
    filter_from_fold_right,
    flat_map_from_fold_right,
    map_from_fold_right,
)

pytestmark = pytest.mark.chapter(29)


def test_fold_derived_collection_operations() -> None:
    assert map_from_fold_right(lambda value: value * 2, (1, 2, 3)) == (2, 4, 6)
    assert filter_from_fold_right(lambda value: value % 2 == 1, (1, 2, 3)) == (1, 3)
    assert flat_map_from_fold_right(lambda value: (value, -value), (1, 2)) == (1, -1, 2, -2)
    assert concat(((1, 2), (), (3,))) == (1, 2, 3)
