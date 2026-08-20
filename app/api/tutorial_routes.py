"""Provided REST routes for reading the workshop itself."""

from fastapi import APIRouter, HTTPException, status

from app.api_models import TutorialResponse, TutorialSummaryResponse
from app.dependencies import TutorialDependency
from app.domain.result import Err

router = APIRouter(prefix="/v1/tutorials", tags=["0. Course tutorials"])


@router.get("", response_model=tuple[TutorialSummaryResponse, ...])
def list_tutorials(service: TutorialDependency) -> tuple[TutorialSummaryResponse, ...]:
    return tuple(map(TutorialSummaryResponse.from_domain, service.list()))


@router.get("/{slug}", response_model=TutorialResponse)
def get_tutorial(slug: str, service: TutorialDependency) -> TutorialResponse:
    result = service.get(slug)
    if isinstance(result, Err):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result.error)
    return TutorialResponse.from_tutorial(result.value)
