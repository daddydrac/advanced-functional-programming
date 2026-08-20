# Workshop Security Threat Model

Authentication protects research campaigns even though the bundled data is synthetic.

| Threat | Chapter mitigation |
|---|---|
| Password database theft | Argon2 hashing; chapter 48.10 |
| User enumeration | uniform registration/login errors; chapter 48.11-48.13 |
| JWT confusion | fixed algorithm plus explicit token kind; chapter 48.2-48.7 |
| Stolen refresh token | one-time rotation and revocation; chapter 48.8/48.14 |
| Brute force | persisted failure window and throttling; chapter 48.9 |
| MFA database disclosure | Fernet-encrypted TOTP secret; chapter 49.3 |
| TOTP replay | accepted-step compare-and-set; chapter 49.6-49.8 |
| Cross-user data access | owner predicates inside repository queries; chapter 47.15 |
| Prompt injection in evidence | deterministic structured packet; chapter 51.3-51.5 |
| Invented scientific claims | output validation, ID citations, explicit non-qualification boundary; chapter 51.7 |

JWTs are signed, not encrypted. Do not place passwords, TOTP secrets, material data, or unpublished findings in token claims.
