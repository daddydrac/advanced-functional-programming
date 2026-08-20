from dataclasses import replace

import pytest

from app.domain.models import ElementFraction
from app.domain.pipeline import normalize_composition, prepare_candidates, validate_candidate
from app.domain.result import Err, Ok
from tests.factories import candidate

pytestmark = pytest.mark.chapter(46)


def test_normalization_is_pure_and_idempotent() -> None:
    source = replace(
        candidate(),
        composition=(ElementFraction("W", 7.0), ElementFraction("Ta", 3.0)),
    )
    first = normalize_composition(source)
    second = normalize_composition(first)
    assert first == second
    assert source.composition[0].atomic_fraction == 7.0
    assert sum(map(lambda item: item.atomic_fraction, first.composition)) == pytest.approx(1.0)


def test_validation_and_preparation_use_result() -> None:
    valid = candidate()
    invalid = replace(valid, formula="")
    assert isinstance(validate_candidate(valid), Ok)
    assert isinstance(validate_candidate(invalid), Err)
    assert isinstance(prepare_candidates((valid, replace(valid, material_id="m-2"))), Ok)
