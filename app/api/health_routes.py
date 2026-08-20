"""Health-route milestones."""

from fastapi import APIRouter, HTTPException, status

from app.api_models import MessageResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/live", response_model=MessageResponse)
def live() -> MessageResponse:
    """Provided process-liveness route."""
    return MessageResponse(message="alive: workshop scaffold")


@router.get("/ready", response_model=MessageResponse)
def ready() -> MessageResponse:
    """Add PostgreSQL and Ollama checks in chapter 52 item 52.3.

    Tutorial: ``tutorials/part-3-application/52-errors-observability-and-operations.md``
    Acceptance: ``CHAPTER=52 make chapter-test``
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 52 item 52.3 is not implemented",
    )
