from datetime import UTC, datetime

import pyotp
import pytest

from app.domain.result import Err, Ok
from app.infrastructure.security import SecretBox, new_totp_secret, verify_totp

pytestmark = pytest.mark.chapter(49)


def test_totp_secret_is_encrypted_and_replay_is_rejected() -> None:
    key = "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA="
    secret = new_totp_secret()
    encrypted = SecretBox(key).encrypt(secret)
    assert secret not in encrypted
    assert SecretBox(key).decrypt(encrypted) == Ok(secret)

    now = datetime(2026, 8, 20, 12, 0, tzinfo=UTC)
    code = pyotp.TOTP(secret).at(now)
    first = verify_totp(secret, code, -1, now, valid_window=1)
    assert isinstance(first, Ok)
    assert isinstance(verify_totp(secret, code, first.value, now, valid_window=1), Err)
