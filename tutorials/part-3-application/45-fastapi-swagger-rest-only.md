# 45 — FastAPI and Swagger: Design the Scientific Boundary

## Goal

Convert untrusted JSON into frozen domain values, expose the complete learning workflow in OpenAPI, and keep HTTP concerns outside the functional core.

## 45.1 — Inspect the provided schemas

File: `app/api_models.py`

Pydantic models validate syntax and broad bounds: required strings, positive moduli, normalized proxy ranges, and collection sizes. Domain validation still has work to do—Pydantic cannot know whether atomic fractions sum to one or whether a policy is scientifically coherent.

`ScreeningRequest` also requires the teaching-data disclaimer. Carrying it in the request makes it harder to paste synthetic values into a demo and later mistake them for sourced results.

## 45.2 — Separate transport from domain

`MaterialCandidateInput` is a REST shape. `MaterialCandidate` is a domain value. Write down three reasons they should not be the same class: versioned APIs, validation boundaries, and framework independence.

## 45.3 — Trace a request without implementing it

Target flow:

```text
JSON -> Pydantic input -> frozen domain value -> pure screening -> repository -> response model
```

Mark which arrows can fail and what HTTP status each boundary should use.

## 45.4 — Keep units in names

Fields such as `melting_point_k` and `young_modulus_gpa` encode units in the schema. This is less flexible than a full quantity type but safer than an unlabeled float. Chapter 54 proposes a unit-aware extension.

## 45.5 — Implement candidate conversion

File: `app/api_models.py`

Skeleton: `MaterialCandidateInput.to_domain`

Build nested tuples with `map`; convert the role string through `ReactorRole`; preserve evidence and uncertainty. Do not normalize composition here—that belongs to the pure pipeline so all adapters share one rule.

## 45.6 — Implement policy conversion

File: `app/api_models.py`

Skeleton: `ScreeningPolicyInput.to_domain`

The conversion must be a pure structural mapping.

## 45.7 — Preserve HTTP 501 until wiring exists

Files: `app/api/campaign_routes.py`, `auth_routes.py`, `automation_routes.py`

Do not return invented successful bodies. Replace each 501 only in its later chapter when the real service and auth dependency exist.

## Acceptance criteria

```bash
CHAPTER=45 make chapter-test
```

- valid JSON becomes the expected frozen candidate and policy;
- an invalid reactor role is rejected at the boundary;
- the OpenAPI schema includes tutorial, auth, screening, and experiment-plan routes;
- `app/domain` imports no FastAPI or Pydantic code.
