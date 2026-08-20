"""Experiment-plan automation skeleton."""

from app.domain.models import ExperimentPlan
from app.domain.result import Result
from app.infrastructure.repositories import CampaignRepository, PlanRepository
from app.services.ollama import OllamaClient


class AutomationService:
    def __init__(
        self,
        campaigns: CampaignRepository,
        plans: PlanRepository,
        ollama: OllamaClient,
    ) -> None:
        self._campaigns = campaigns
        self._plans = plans
        self._ollama = ollama

    async def create_plan(self, owner_id: str, campaign_id: str) -> Result[ExperimentPlan, str]:
        """Load evidence, call Ollama, validate, and persist the plan.

        Chapter items: 51.7-51.9
        Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
        Acceptance: ``CHAPTER=51 make chapter-test``
        """
        raise NotImplementedError("Chapter 51 item 51.7: orchestrate experiment plan")
