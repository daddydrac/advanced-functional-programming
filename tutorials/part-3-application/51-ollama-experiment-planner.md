# 51 — Local Ollama: Propose the Next Experiment from Grounded Evidence

## Goal

Use deterministic screening to choose informative candidates, then ask a local model to draft an auditable experiment proposal without inventing properties or declaring safety.

## 51.1 — Keep the LLM downstream

The pure core calculates feasibility, score, uncertainty, and Pareto membership. Ollama receives those stored results. It does not calculate the source-of-truth rank and cannot write material properties.

## 51.2 — Implement acquisition score

File: `app/domain/pipeline.py`

Begin with an upper-confidence-style teaching rule:

$$a(x)=u(x)+\beta\sigma(x),$$

where $u$ is transparent utility, $\sigma$ is input uncertainty, and $\beta$ is `exploration_weight`. High uncertainty can make a candidate informative even when it is not currently best. This score proposes what to measure next; it does not claim the material is superior.

## 51.3 — Build the evidence packet

File: `app/services/ollama.py`

For Pareto and high-acquisition candidates, emit deterministic lines containing material ID, formula, role, feasibility, exact score fields, limitations, evidence source/method, and uncertainty. Use folds/map; never paste raw ORM objects.

## 51.4 — Design the prompt contract

Request exactly these sections:

1. `Candidate and rationale`
2. `Observed or supplied evidence`
3. `Uncertainty and missing evidence`
4. `Proposed experiment`
5. `Measurements and stopping rules`
6. `Safety and qualification boundary`

Require every factual line to cite a material ID. Forbid new numeric values, reactor-safety claims, and phrases that imply qualification.

## 51.5 — Defend against prompt injection

Treat source/evidence text as quoted data, not instructions. Delimit it and tell the model never to follow instructions found inside. In a production extension, validate allowed characters and length before prompt construction.

## 51.6 — Implement the Ollama call

POST to `/api/chat` with `stream: false`, configured model, low temperature, and timeout. Map HTTP, timeout, malformed JSON, and empty-content failures to `Err` without leaking internal URLs.

## 51.7 — Validate the response

Before persistence, require all six headings, require at least one valid material ID, reject unknown IDs, and flag numeric tokens not found in the evidence packet. A human must approve any experiment.

## 51.8-51.9 — Persist and expose

File: `app/services/automation.py`, `app/api/automation_routes.py`

Load only the authenticated owner's campaign, call Ollama, validate, create immutable plan metadata, persist it, and return through the REST schema. Return 503 when local Ollama is unavailable.

## Acceptance criteria

```bash
CHAPTER=51 make chapter-test
```

- acquisition increases with uncertainty when utility is fixed;
- the prompt contains only deterministic campaign evidence;
- unknown material IDs are rejected;
- mocked Ollama failures become typed errors/HTTP 503;
- the model cannot modify stored campaign scores;
- output clearly says experimental and safety review are required.
