from dataclasses import dataclass, replace

import pytest
from hypothesis import given
from hypothesis import strategies as st

from app.domain.lenses import Lens, law_get_put, law_put_get, law_put_put

pytestmark = pytest.mark.chapter(40)


@dataclass(frozen=True, slots=True)
class Sample:
    value: int
    label: str = "fixed"


VALUE = Lens[Sample, int](
    getter=lambda sample: sample.value,
    setter=lambda sample, value: replace(sample, value=value),
)


@given(st.integers(), st.integers(), st.integers())
def test_lens_laws(source: int, first: int, second: int) -> None:
    sample = Sample(source)
    assert law_get_put(VALUE, sample)
    assert law_put_get(VALUE, sample, first)
    assert law_put_put(VALUE, sample, first, second)
