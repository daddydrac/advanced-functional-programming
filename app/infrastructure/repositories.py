"""Repository skeletons separating mutable ORM rows from frozen domain data."""

from collections.abc import Iterable
from datetime import datetime

from app.domain.models import (
    ExperimentPlan,
    MaterialCandidate,
    ScreeningCampaign,
    User,
)
from app.infrastructure.database import Database, MaterialRow, UserRow


def row_to_user(row: UserRow) -> User:
    """Convert an ORM row to a frozen user.

    Chapter item: 47.6
    Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
    Acceptance: ``CHAPTER=47 make chapter-test``
    """
    raise NotImplementedError("Chapter 47 item 47.6: map UserRow to User")


def candidate_to_payload(candidate: MaterialCandidate) -> dict[str, object]:
    """Serialize a candidate without leaking dataclass internals.

    Chapter item: 47.7
    Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
    Acceptance: ``CHAPTER=47 make chapter-test``
    """
    raise NotImplementedError("Chapter 47 item 47.7: serialize candidate")


def payload_to_candidate(payload: dict[str, object]) -> MaterialCandidate:
    """Validate and rebuild a frozen candidate.

    Chapter item: 47.8
    Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
    Acceptance: ``CHAPTER=47 make chapter-test``
    """
    raise NotImplementedError("Chapter 47 item 47.8: deserialize candidate")


def row_to_candidate(row: MaterialRow) -> MaterialCandidate:
    """Convert a material ORM row.

    Chapter item: 47.9
    Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
    Acceptance: ``CHAPTER=47 make chapter-test``
    """
    raise NotImplementedError("Chapter 47 item 47.9: map MaterialRow")


class UserRepository:
    """User persistence exercises for chapters 47-49."""

    def __init__(self, database: Database) -> None:
        self._database = database

    def create(self, user: User) -> User:
        """Persist a user.

        Chapter item: 47.10
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.10: create user")

    def by_email(self, email: str) -> User | None:
        """Find normalized email without exposing enumeration.

        Chapter item: 48.5
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.5: query user by email")

    def by_id(self, user_id: str) -> User | None:
        """Find by stable ID.

        Chapter item: 47.11
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.11: query user by ID")

    def activate_mfa(self, user_id: str, totp_step: int) -> None:
        """Atomically activate MFA.

        Chapter item: 49.6
        Tutorial: ``tutorials/part-3-application/49-totp-mfa-google-authenticator.md``
        Acceptance: ``CHAPTER=49 make chapter-test``
        """
        raise NotImplementedError("Chapter 49 item 49.6: activate MFA")

    def accept_totp_step(self, user_id: str, previous_step: int, new_step: int) -> bool:
        """Compare-and-set the accepted TOTP step.

        Chapter item: 49.8
        Tutorial: ``tutorials/part-3-application/49-totp-mfa-google-authenticator.md``
        Acceptance: ``CHAPTER=49 make chapter-test``
        """
        raise NotImplementedError("Chapter 49 item 49.8: reject replay races")


class MaterialRepository:
    """Owner-scoped material storage."""

    def __init__(self, database: Database) -> None:
        self._database = database

    def add_many(self, owner_id: str, candidates: Iterable[MaterialCandidate]) -> None:
        """Persist immutable candidates.

        Chapter item: 47.12
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.12: persist candidates")

    def list_for_owner(self, owner_id: str, limit: int = 1_000) -> tuple[MaterialCandidate, ...]:
        """Return frozen candidates in deterministic order.

        Chapter item: 47.13
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.13: list owner candidates")


class CampaignRepository:
    def __init__(self, database: Database) -> None:
        self._database = database

    def create(self, campaign: ScreeningCampaign) -> ScreeningCampaign:
        """Persist a reproducible campaign snapshot.

        Chapter item: 47.14
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.14: persist campaign")

    def by_id(self, owner_id: str, campaign_id: str) -> ScreeningCampaign | None:
        """Enforce ownership in the query itself.

        Chapter item: 47.15
        Tutorial: ``tutorials/part-3-application/47-sqlalchemy-orm-and-postgresql.md``
        Acceptance: ``CHAPTER=47 make chapter-test``
        """
        raise NotImplementedError("Chapter 47 item 47.15: load owned campaign")


class PlanRepository:
    def __init__(self, database: Database) -> None:
        self._database = database

    def create(self, plan: ExperimentPlan) -> ExperimentPlan:
        """Persist the grounded plan and model identity.

        Chapter item: 51.8
        Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
        Acceptance: ``CHAPTER=51 make chapter-test``
        """
        raise NotImplementedError("Chapter 51 item 51.8: persist experiment plan")


class TokenRepository:
    def __init__(self, database: Database) -> None:
        self._database = database

    def revoke(self, jti: str, expires_at: datetime) -> None:
        """Persist token revocation.

        Chapter item: 48.8
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.8: revoke token")

    def is_revoked(self, jti: str) -> bool:
        """Check deny-list membership.

        Chapter item: 48.8
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.8: check revocation")


class AuthFailureRepository:
    def __init__(self, database: Database) -> None:
        self._database = database

    def record(self, subject: str, attempted_at: datetime) -> None:
        """Record a failed boundary attempt.

        Chapter item: 48.9
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.9: record auth failure")

    def count_since(self, subject: str, since: datetime) -> int:
        """Count failures in a fixed window.

        Chapter item: 48.9
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.9: count recent failures")

    def clear(self, subject: str) -> None:
        """Clear failures after success.

        Chapter item: 48.9
        Tutorial: ``tutorials/part-3-application/48-jwt-authentication.md``
        Acceptance: ``CHAPTER=48 make chapter-test``
        """
        raise NotImplementedError("Chapter 48 item 48.9: clear failures")
