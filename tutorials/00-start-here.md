# 00 — Start Here: Build LambdaFlux, Do Not Merely Run It

## Outcome

You will build a REST-only fusion-materials screening workshop from intentionally incomplete Python. The final system accepts immutable material candidates, rejects invalid compositions, derives transparent physics features, finds a Pareto front, persists campaigns in PostgreSQL, protects researcher accounts with JWT and Google Authenticator-compatible TOTP, and asks local Ollama to propose the next experiment from deterministic evidence.

The repository is a workbook, not a solution. `GET /v1/tutorials` works immediately; capstone routes return HTTP 501 until you implement their chapter item.

## How a human completes this workshop

For every chapter, use the same learning loop:

1. Read the motivation and rewrite the relevant equation or type signature in your own words.
2. Predict the worked example before running it in the Compose test container.
3. Open only the named source skeleton; its docstring repeats the chapter item, tutorial path, and acceptance command.
4. Implement that item yourself. Hints specify laws, constraints, failure cases, and useful library functions without supplying the capstone body.
5. Run the chapter acceptance test, read the failure as feedback, and revise until it passes.
6. After the REST chapters, exercise the behavior through Swagger rather than calling services directly.

Do not search for a hidden completed application: none is included. The small code snippets teach transferable syntax or algebra; they are deliberately not drop-in answers to the capstone skeletons.

## Scientific question

No single material maximizes melting point, heat transport, ductility, irradiation tolerance, low activation, manufacturability, and low tritium retention. The software question is therefore:

> How do we transform incomplete, uncertain evidence into a reproducible shortlist without hiding tradeoffs or pretending that screening equals qualification?

## 00.1 — Verify the scaffold

```bash
make init
make up
curl http://localhost:8000/health/live
```

Open `http://localhost:8000/docs`. Call `GET /v1/tutorials/00-start-here`, then call `POST /v1/campaigns/screen`. HTTP 501 is the correct starting state.

## 00.2 — Understand the red-green loop

Choose one implementation chapter, run its acceptance test, implement only the named skeletons, and rerun:

```bash
CHAPTER=28 make chapter-test
```

Do not implement chapter 50 before chapters 26, 28, 29, 36, 37, 39, 40, and 46. The dependency order is part of the design lesson.

Chapters 01-24 use their visible lab/checkpoint criteria to build Python fluency. Starting at chapter 26, `CHAPTER=<number> make chapter-test` activates executable acceptance tests for the evolving application.

## 00.3 — Respect the scientific boundary

`data/sample-fusion-candidates.json` is synthetic. Its alloy families are research-inspired, but every numerical value was invented for exercises. A real record must state source, method, material condition, temperature, irradiation spectrum/fluence, uncertainty, units, and database version.

## Acceptance criteria

- The tutorial index loads through Swagger.
- You can explain why capstone routes initially return 501.
- You can find a skeleton's tutorial path and chapter item in its docstring.
- You agree not to interpret bundled scores as reactor qualification or safety evidence.
