"""OpenAPI-visible authentication exercises; all handlers start at HTTP 501."""

from typing import Never

from fastapi import APIRouter, HTTPException, Response, status

from app.api_models import (
    MessageResponse,
    MfaRequest,
    PasswordLoginRequest,
    RefreshRequest,
    RegisterRequest,
    RegistrationResponse,
    SetupTokenRequest,
    TokenPairResponse,
    UserResponse,
)
from app.dependencies import BearerCredentials

router = APIRouter(prefix="/v1/auth", tags=["1. Authentication exercises"])


def incomplete(item: str) -> Never:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail=f"Complete chapter item {item}; see tutorials/part-3-application/",
    )


@router.post("/register", response_model=RegistrationResponse)
def register(request: RegisterRequest) -> RegistrationResponse:
    """Wire AuthService.register in chapter 49 item 49.9."""
    del request
    incomplete("49.9")


@router.post(
    "/mfa/qr",
    response_class=Response,
    responses={200: {"content": {"image/svg+xml": {}}}},
)
def mfa_qr(request: SetupTokenRequest) -> Response:
    """Return a secret-bearing SVG only in memory; implement chapter item 49.5."""
    del request
    incomplete("49.5")


@router.post("/mfa/activate")
def activate_mfa(request: MfaRequest) -> None:
    """Wire MFA activation in chapter 49 item 49.10."""
    del request
    incomplete("49.10")


@router.post("/login/password")
def password_login(request: PasswordLoginRequest) -> None:
    """Wire the password challenge in chapter 48 item 48.13."""
    del request
    incomplete("48.13")


@router.post("/login/mfa", response_model=TokenPairResponse)
def mfa_login(request: MfaRequest) -> TokenPairResponse:
    """Wire MFA token issuance in chapter 49 item 49.11."""
    del request
    incomplete("49.11")


@router.post("/refresh", response_model=TokenPairResponse)
def refresh(request: RefreshRequest) -> TokenPairResponse:
    """Rotate a refresh token exactly once in chapter item 48.14."""
    del request
    incomplete("48.14")


@router.post("/logout", response_model=MessageResponse)
def logout(credentials: BearerCredentials) -> MessageResponse:
    """Revoke the current access token in chapter item 48.16."""
    del credentials
    incomplete("48.16")


@router.get("/me", response_model=UserResponse)
def me(credentials: BearerCredentials) -> UserResponse:
    """Resolve the authenticated user in chapter item 53.2."""
    del credentials
    incomplete("53.2")
