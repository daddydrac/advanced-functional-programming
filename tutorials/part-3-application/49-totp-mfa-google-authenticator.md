# 49 — TOTP MFA: Google Authenticator-Compatible Enrollment

## Goal

Implement encrypted TOTP enrollment, QR provisioning, a two-stage login, and replay-resistant code acceptance.

TOTP derives a short code from a shared secret and integer time step:

$$T=\left\lfloor\frac{t-T_0}{X}\right\rfloor,$$

where $X$ is usually 30 seconds. Accepting a neighboring step tolerates clock skew but enlarges the replay surface.

## 49.1 — Draw the state machine

```text
registered, MFA off -> setup token -> valid TOTP -> MFA on
MFA on -> password -> challenge token -> fresh TOTP -> access + refresh
```

List which transitions are invalid and must fail closed.

## 49.2 — Generate the secret

File: `app/infrastructure/security.py`

Use PyOTP's cryptographically random base32 generator. Never derive a TOTP secret from email, password, or JWT secret.

## 49.3 — Encrypt at rest

Implement `SecretBox.encrypt/decrypt` with Fernet and a distinct environment key. Decryption failure becomes `Err`, not an uncaught cryptography exception.

## 49.4 — Build the provisioning URI

Use issuer and normalized email. Return the URI only during pending setup. Google Authenticator and other standard authenticator apps can scan this `otpauth://` URI.

## 49.5 — Render SVG QR

Files: `app/infrastructure/security.py`, `app/services/auth.py`, and `app/api/auth_routes.py`

Implement `qr_svg`, `AuthService.setup_uri`, and `POST /v1/auth/mfa/qr`. Generate SVG bytes in memory. Set the route media type to `image/svg+xml`; do not save the secret-bearing QR to disk.

## 49.6-49.7 — Verify a window functionally

File: `app/infrastructure/security.py`

Skeleton: `verify_totp`

Generate candidate steps with `range`, transform with `map`, retain matches with `filter`, and select the highest valid step. Compare codes with `hmac.compare_digest`.

## 49.8 — Reject replay races

Persist the last accepted step. Update it only when the stored old step still equals the value read and the new step is greater. That compare-and-set prevents two concurrent requests from accepting one code.

## 49.9-49.11 — Implement enrollment and MFA login

File: `app/services/auth.py`

Registration creates the disabled user, encrypted secret, and setup token. Activation consumes a code. MFA login consumes a later code and only then issues tokens. The activation code cannot be reused for login.

## Acceptance criteria

```bash
CHAPTER=49 make chapter-test
```

- a valid current code activates enrollment;
- the same time step is rejected on replay;
- a wrong setup/challenge token kind fails;
- encrypted database text does not contain the base32 secret;
- concurrent compare-and-set accepts at most one request.
