# 24 — Python Foundations Integration Lab

## Goal

Combine the full Python foundation into one immutable material-candidate transformation and describe how it will later cross a REST boundary.

Build this pipeline:

$$\text{JSON}\xrightarrow{\text{Pydantic}}\text{ObservationInput}
\xrightarrow{\text{to\_domain}}\text{Observation}
\xrightarrow{\text{normalize}}\text{Observation}
\xrightarrow{\text{validate}}\text{Result}
$$

The code uses strings, numbers, booleans, tuples, frozensets, mappings, dates, functions, pattern matching, types, modules, errors, and effect boundaries. It avoids loop syntax and mutation.

## REST lab

1. Open Swagger at `/docs`.
2. Read this lesson through `GET /v1/tutorials/{slug}`.
3. Register and activate MFA.
4. Obtain an access token and use Swagger's **Authorize** control.
5. Validate a small candidate batch locally; the REST route remains intentionally incomplete until chapter 53.

Do not call the AI endpoint yet. First inspect the deterministic analysis and reproduce one z-score by hand.

## Checkpoint

Draw the data types at each arrow. For every function, name its domain, codomain, possible effects, and failure representation.

Reference coverage: integrated review of the complete core Python tutorial sequence before advanced functional programming.

## Acceptance criteria

- every arrow has named input/output types.
- every effect and failure channel is identified.
- the transformation preserves its frozen input.
