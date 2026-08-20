# Free Data Science Course: Learn Functional Programming by Screening Materials for a Fusion Reactor

*Intro Article on LinkedIn*: 

*Lambda calculus meets fusion physics—fold, compose, and rank reactor materials with FastAPI, PostgreSQL, and local AI ⚛️*

LambdaFlux is an intentionally incomplete, chapter-driven coding workshop. You build a REST-only fusion-materials screening system one functional abstraction at a time; the repository contains signatures, frozen data shapes, docstrings, Docker Compose infrastructure, staged tests, and scientific context—but not the completed solution.

You write the application. The Markdown chapters teach the ideas, walk through smaller examples, name the exact skeletons to edit, and define acceptance; they never hand you completed capstone function bodies.

The capstone screens research-inspired material candidates for plasma-facing and structural roles. It explores composition validation, thermophysical feature engineering, Pugh-ratio and thermal-stress proxies, hard constraints, Pareto ranking, uncertainty-aware experiment selection, PostgreSQL persistence, JWT/TOTP authentication, and a local Ollama experiment-planning assistant.

## What is intentionally provided

- 54 Markdown chapters plus an orientation chapter;
- frozen dataclasses and REST request/response schemas;
- function signatures with exact chapter item, tutorial path, and test command;
- a FastAPI course shell whose tutorial routes work immediately;
- Swagger-visible capstone routes that return HTTP 501 until you implement them;
- SQLAlchemy table shapes, Compose services, synthetic data, and staged acceptance tests;
- Python 3.14 slim, PostgreSQL, Ollama, and test tooling under one Compose file.

## What is intentionally missing

There are no completed folds, monads, lenses, statistics, screening algorithms, repositories, auth workflows, or Ollama automation. Search for `NotImplementedError` to see the curriculum backlog:

```bash
rg -n "NotImplementedError" app
```

Each docstring points to a numbered tutorial item such as:

```text
Chapter item: 28.3
Tutorial: tutorials/part-2-functional/28-foldl-and-foldr.md
Acceptance: CHAPTER=28 make chapter-test
```

## Start the course

```bash
make init
make up
```

Open `http://localhost:8000/docs`, call `GET /v1/tutorials`, and read `00-start-here`. Then implement one chapter at a time:

```bash
CHAPTER=26 make chapter-test
CHAPTER=28 make chapter-test
CHAPTER=29 make chapter-test
```

See [QUICKSTART.md](QUICKSTART.md), [docs/implementation-map.md](docs/implementation-map.md), and [docs/research-basis.md](docs/research-basis.md).

## Scientific scope

Fusion materials must be evaluated under coupled heat, plasma, neutron, mechanical, activation, and fuel-cycle constraints. LambdaFlux teaches the software and mathematical architecture of an early screening workflow; it does not predict reactor safety or qualify materials. Every bundled numerical property is synthetic and deliberately labeled as such. Real data must preserve source, method, units, uncertainty, conditions, and database version.

The curriculum structure is mapped to the [W3Schools Python tutorial](https://www.w3schools.com/python/python_getstarted.asp) and [Functional Python Programming, Third Edition](https://github.com/PacktPublishing/Functional-Python-Programming-3rd-Edition). All tutorial prose and skeleton code are original.
