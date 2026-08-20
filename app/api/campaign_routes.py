"""OpenAPI-visible material-screening exercises."""

from fastapi import APIRouter, HTTPException, status

from app.api_models import CampaignResponse, ScreeningRequest

router = APIRouter(prefix="/v1/campaigns", tags=["2. Fusion screening exercises"])


@router.post("/screen", response_model=CampaignResponse)
def screen(request: ScreeningRequest) -> CampaignResponse:
    """Wire the screening service in chapter 50 item 50.15.

    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    del request
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 50 item 50.15 is not implemented",
    )


@router.get("/{campaign_id}", response_model=CampaignResponse)
def get_campaign(campaign_id: str) -> CampaignResponse:
    """Wire owner-scoped retrieval in chapter 47 item 47.15."""
    del campaign_id
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 47 item 47.15 is not implemented",
    )
