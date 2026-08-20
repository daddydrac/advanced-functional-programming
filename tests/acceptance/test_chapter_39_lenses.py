from dataclasses import dataclass, replace

import pytest

from app.domain.lenses import Lens

pytestmark = pytest.mark.chapter(39)


@dataclass(frozen=True, slots=True)
class Properties:
    melting_point_k: float
    label: str


@dataclass(frozen=True, slots=True)
class Candidate:
    properties: Properties
    candidate_id: str


PROPERTIES = Lens[Candidate, Properties](
    getter=lambda value: value.properties,
    setter=lambda value, focus: replace(value, properties=focus),
)
MELTING = Lens[Properties, float](
    getter=lambda value: value.melting_point_k,
    setter=lambda value, focus: replace(value, melting_point_k=focus),
)


def test_composed_lens_changes_only_focus() -> None:
    source = Candidate(Properties(3000.0, "synthetic"), "m-1")
    updated = PROPERTIES.compose(MELTING).set(3200.0, source)
    assert updated.properties.melting_point_k == 3200.0
    assert updated.properties.label == "synthetic"
    assert updated.candidate_id == "m-1"
    assert source.properties.melting_point_k == 3000.0
