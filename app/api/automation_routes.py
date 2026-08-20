"""OpenAPI-visible local-AI experiment-planning exercise."""

from fastapi import APIRouter, HTTPException, status

from app.api_models import ExperimentPlanResponse, PlanRequest

router = APIRouter(prefix="/v1/automations", tags=["3. Local AI exercises"])


@router.post("/experiment-plan", response_model=ExperimentPlanResponse)
async def create_experiment_plan(request: PlanRequest) -> ExperimentPlanResponse:
    """Wire the grounded Ollama workflow in chapter 51 item 51.9.

    Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
    Acceptance: ``CHAPTER=51 make chapter-test``
    """
    del request
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 51 item 51.9 is not implemented",
    )
