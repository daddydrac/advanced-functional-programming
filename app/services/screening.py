"""Use-case skeleton for a reproducible fusion-material screening campaign."""

from collections.abc import Iterable

from app.domain.models import MaterialCandidate, ScreeningCampaign, ScreeningPolicy
from app.domain.result import Result
from app.infrastructure.repositories import CampaignRepository, MaterialRepository


class ScreeningService:
    """Imperative shell around the pure screening pipeline."""

    def __init__(
        self,
        materials: MaterialRepository,
        campaigns: CampaignRepository,
    ) -> None:
        self._materials = materials
        self._campaigns = campaigns

    def run(
        self,
        owner_id: str,
        candidates: Iterable[MaterialCandidate],
        policy: ScreeningPolicy,
    ) -> Result[ScreeningCampaign, str]:
        """Validate, screen, persist, and return one immutable campaign.

        Chapter items: 46.6 and 50.15
        Tutorial:
          - ``tutorials/part-3-application/46-functional-core-imperative-shell.md``
          - ``tutorials/part-3-application/50-fusion-screening-math.md``
        Acceptance: ``CHAPTER=50 make chapter-test``

        Use ``uuid4`` and ``datetime.now(UTC)`` only here, never in the pure
        domain pipeline.
        """
        raise NotImplementedError("Chapter 50 item 50.15: run screening campaign")

    def get(self, owner_id: str, campaign_id: str) -> Result[ScreeningCampaign, str]:
        """Load an owner-scoped campaign.

        Chapter item: 47.15
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.15: get campaign")
