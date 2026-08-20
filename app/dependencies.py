"""Dependency-injection skeleton plus the provided tutorial dependency."""

from dataclasses import dataclass
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import Settings, get_settings
from app.domain.models import User
from app.infrastructure.database import Database
from app.infrastructure.security import TokenClaims
from app.services.auth import AuthService
from app.services.automation import AutomationService
from app.services.screening import ScreeningService
from app.services.tutorials import TutorialService

bearer_scheme = HTTPBearer(auto_error=False)
BearerCredentials = Annotated[
    HTTPAuthorizationCredentials | None,
    Security(bearer_scheme),
]


@dataclass(frozen=True, slots=True)
class Container:
    """Explicit application wiring created in chapter 46."""

    settings: Settings
    database: Database
    auth: AuthService
    screening: ScreeningService
    automation: AutomationService


@lru_cache(maxsize=1)
def get_container() -> Container:
    """Wire infrastructure adapters to use-case services.

    Chapter items: 46.7-46.9
    Tutorial: ``tutorials/part-3-application/46-functional-core-imperative-shell.md``
    Acceptance: ``CHAPTER=46 make chapter-test``
    """
    raise NotImplementedError("Chapter 46 item 46.7: wire dependency container")


@lru_cache(maxsize=1)
def get_tutorial_service() -> TutorialService:
    """Provided course infrastructure so Markdown is available through REST."""
    return TutorialService(get_settings().course_dir)


ContainerDependency = Annotated[Container, Depends(get_container)]
TutorialDependency = Annotated[TutorialService, Depends(get_tutorial_service)]


def access_claims(
    credentials: BearerCredentials,
    container: ContainerDependency,
) -> TokenClaims:
    """Authenticate a Bearer access token with a uniform 401 response.

    Chapter item: 53.1
    Tutorial: ``tutorials/part-3-application/53-complete-rest-walkthrough.md``
    Acceptance: ``CHAPTER=53 make chapter-test``
    """
    del credentials, container
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 53 item 53.1: implement Bearer access dependency",
    )


AccessClaimsDependency = Annotated[TokenClaims, Depends(access_claims)]


def current_user(
    claims: AccessClaimsDependency,
    container: ContainerDependency,
) -> User:
    """Resolve the authenticated frozen user or emit uniform HTTP 401.

    Chapter item: 53.1
    Tutorial: ``tutorials/part-3-application/53-complete-rest-walkthrough.md``
    Acceptance: ``CHAPTER=53 make chapter-test``
    """
    del claims, container
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Chapter 53 item 53.1: resolve the authenticated user",
    )


CurrentUserDependency = Annotated[User, Depends(current_user)]
