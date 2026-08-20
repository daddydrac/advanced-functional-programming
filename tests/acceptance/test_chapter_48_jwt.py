from datetime import timedelta

import pytest

from app.domain.result import Err, Ok
from app.infrastructure.security import TokenCodec, TokenKind

pytestmark = pytest.mark.chapter(48)


def test_jwt_kind_is_an_authorization_boundary() -> None:
    codec = TokenCodec(
        secret="chapter-48-secret-long-enough-for-the-test-boundary",
        issuer="lambdaflux.test",
        audience="lambdaflux-api",
    )
    token = codec.encode("user-1", TokenKind.ACCESS, timedelta(minutes=5))
    assert isinstance(codec.decode(token, TokenKind.ACCESS), Ok)
    assert isinstance(codec.decode(token, TokenKind.REFRESH), Err)
