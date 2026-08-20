from dataclasses import replace

import pytest

from app.domain.models import MaterialScore
from app.domain.pipeline import (
    dominates,
    pareto_front,
    pugh_ratio,
    thermal_stress_proxy,
)
from app.domain.statistics import EMPTY_STATS, append_value, combine, summarize
from tests.factories import candidate

pytestmark = pytest.mark.chapter(50)


def score(identifier: str, utility: float, pugh: float, stress: float) -> MaterialScore:
    source = candidate(material_id=identifier, formula=identifier)
    return MaterialScore(
        candidate=source,
        feasible=True,
        pugh_ratio=pugh,
        thermal_stress_proxy_mpa=stress,
        utility=utility,
        uncertainty=0.2,
        reasons=("synthetic teaching score",),
    )


def test_welford_summary_and_partition_combine() -> None:
    values = (10.0, 12.0, 14.0)
    whole = summarize(values)
    partitioned = combine(summarize(values[:2]), summarize(values[2:]))
    assert whole.count == 3
    assert whole.mean == pytest.approx(12.0)
    assert partitioned.mean == pytest.approx(whole.mean)
    assert combine(EMPTY_STATS, whole) == whole
    assert append_value(EMPTY_STATS, 10.0).mean == 10.0


def test_physics_feature_unit_conversions() -> None:
    source = candidate(bulk_modulus_gpa=250.0, shear_modulus_gpa=125.0)
    assert pugh_ratio(source) == pytest.approx(2.0)
    expected_mpa = 300_000.0 * 5e-6 * (1200.0 - 293.15)
    assert thermal_stress_proxy(source, 1200.0) == pytest.approx(expected_mpa)


def test_pareto_dominance_requires_strict_improvement() -> None:
    better = score("better", utility=0.9, pugh=2.2, stress=900.0)
    worse = score("worse", utility=0.7, pugh=1.9, stress=1100.0)
    equal = replace(better, candidate=candidate(material_id="equal", formula="equal"))
    assert dominates(better, worse)
    assert not dominates(better, equal)
    assert pareto_front((better, worse)) == (better,)
