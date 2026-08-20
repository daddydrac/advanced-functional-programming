# 48 — JWT Authentication: Typed Tokens and Rotating Sessions

## Goal

Implement password authentication and distinct setup, challenge, access, and refresh JWT capabilities without confusing their authority.

## 48.1 — Model token authority

| Token kind | Permitted use |
|---|---|
| `mfa_setup` | activate one pending enrollment |
| `mfa_challenge` | submit a TOTP after password success |
| `access` | call protected API routes briefly |
| `refresh` | rotate into a new token pair once |

A signed JWT is readable by its holder. Put only subject, token ID, kind, issuer, audience, and times in claims.

## 48.2-48.4 — Implement encoding

File: `app/infrastructure/security.py`

Skeleton: `TokenCodec.encode`

Use a fixed HS256 algorithm, UTC timestamps, `nbf`, `iat`, `exp`, a unique `jti`, and explicit `type`. The secret comes from environment settings.

## 48.5-48.7 — Implement fail-closed decoding

Allow only the chosen algorithm. Require all claims. Verify signature, issuer, audience, and time. Convert the type string through `TokenKind` and compare it with the expected kind. Return `Err` for every malformed/expired/wrong-kind token without leaking decoder internals.

## 48.8 — Implement revocation and rotation

Persist the refresh token's `jti` before issuing its replacement. A second use must fail. Delete expired deny-list entries in an operational extension.

## 48.9 — Persist throttling state

Count failures in a time window by normalized email before password success and by user ID after a challenge exists. Do not rely on per-process memory because Compose may restart or scale the API.

## 48.10 — Configure Argon2

Use `pwdlib.PasswordHash.recommended()`. For an unknown email, verify against a dummy hash to reduce timing differences.

## 48.11-48.12 — Normalize identity and validate passwords

Implement `normalized_email` and `validate_password` in `app/services/auth.py` with map/filter rather than loops. Return a typed failure listing requirements.

## 48.13-48.16 — Build the password/session workflow

Password success yields only an MFA challenge. Implement access validation, one-time refresh rotation, and logout revocation. Do not issue access before MFA.

## Acceptance criteria

```bash
CHAPTER=48 make chapter-test
```

- wrong token kinds and algorithms fail;
- expired tokens fail;
- refresh rotation rejects replay;
- password hashes never equal plaintext;
- an unknown email follows the same public failure path.
