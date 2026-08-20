# 53 — Complete the Authenticated REST Workflow

## Goal

Replace the remaining HTTP 501 scaffolds with real service calls and exercise the entire backend through Swagger—no frontend and no direct Python shell shortcuts.

## 53.1 — Wire dependency injection

Use `ContainerDependency` in capstone routes. Add a bearer-token dependency that decodes an access token, checks revocation, resolves the user, and emits `WWW-Authenticate: Bearer` on 401.

## 53.2 — Complete auth routes

Implement registration, QR retrieval, activation, password challenge, MFA token issuance, refresh, logout, and `/me`. Keep public errors uniform.

## 53.3 — Complete screening routes

`POST /v1/campaigns/screen` must:

1. require an access token;
2. convert REST inputs to domain values;
3. run `ScreeningService`;
4. map typed failures to documented status codes;
5. return the immutable stored campaign.

`GET /v1/campaigns/{id}` must enforce ownership in its repository query.

## 53.4 — Complete experiment-plan route

Require auth, load the owned campaign, call local Ollama, validate, persist, and return the plan. A unavailable model is 503; missing owned campaign is 404.

## 53.5 — Run the Swagger sequence

1. `GET /v1/tutorials`.
2. `POST /v1/auth/register`.
3. retrieve/scan the QR and activate MFA.
4. wait for the next 30-second code.
5. password login, then MFA login.
6. use Swagger **Authorize** with the access JWT.
7. `POST /v1/campaigns/screen` with the sample request body.
8. `GET /v1/campaigns/{campaign_id}`.
9. `POST /v1/automations/experiment-plan`.
10. logout and prove the access token no longer works.

## 53.6 — Check cross-owner isolation

Register a second user. The second user must not retrieve the first campaign or create a plan for it.

## Acceptance criteria

```bash
CHAPTER=53 make chapter-test
```

- the full flow succeeds with mocked Ollama;
- no capstone route returns 501;
- every protected route rejects missing, wrong-kind, expired, and revoked tokens;
- owner isolation is proven through REST tests;
- OpenAPI documents request/response/error schemas.
