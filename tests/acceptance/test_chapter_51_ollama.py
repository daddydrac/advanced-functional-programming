from datetime import UTC, datetime

import pytest

from app.domain.models import MaterialScore, ScreeningCampaign
from app.domain.pipeline import acquisition_score
from app.services.ollama import evidence_packet, experiment_prompt
from tests.factories import candidate, policy

pytestmark = pytest.mark.chapter(51)


def campaign() -> ScreeningCampaign:
    item = MaterialScore(
        candidate=candidate(),
        feasible=True,
        pugh_ratio=2.0,
        thermal_stress_proxy_mpa=1300.0,
        utility=0.8,
        uncertainty=0.3,
        reasons=("synthetic teaching score",),
    )
    return ScreeningCampaign(
        campaign_id="campaign-1",
        owner_id="user-1",
        created_at=datetime(2026, 8, 20, tzinfo=UTC),
        policy=policy(),
        candidate_count=1,
        pareto_front=(item,),
        ranked=(item,),
    )


def test_acquisition_and_prompt_are_grounded() -> None:
    item = campaign().ranked[0]
    assert acquisition_score(item, policy()) == pytest.approx(0.8 + 0.35 * 0.3)
    packet = evidence_packet(campaign())
    prompt = experiment_prompt(campaign())
    assert packet
    assert "candidate-a" in prompt
    assert "qualification" in prompt.casefold()
    assert all(map(lambda line: "candidate-a" in line, packet))
