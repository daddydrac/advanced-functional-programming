# 54 — Extend LambdaFlux without Breaking Its Scientific Boundary

## Goal

Choose one production-style extension, write its laws and acceptance criteria first, and preserve the functional-core architecture.

## 54.1 — Import crystal data through OPTIMADE

Build an adapter for the OPTIMADE structures endpoint. Store provider base URL, provider ID, API version, structure ID, retrieval time, and raw field provenance. Map only properties actually supplied by that provider. Do not invent fusion-neutron fields from crystal data.

## 54.2 — Add a Materials Project adapter

Use the official client/API for thermodynamic, elasticity, or structure fields. Keep API credentials in environment secrets. Record database version because calculated values can change across releases.

## 54.3 — Add unit-safe quantities

Replace unit-bearing field names with a frozen quantity type or a vetted units library. Test dimensional compatibility so GPa cannot be added to kelvin.

## 54.4 — Upgrade uncertainty

Replace one normalized uncertainty with per-property distributions or intervals. Propagate uncertainty through feature calculations and Pareto membership. Distinguish aleatoric measurement uncertainty from epistemic model uncertainty.

## 54.5 — Add active-learning history

Persist experiment proposals, approvals, observations, and model versions. Compare acquisition against random selection with an offline replay benchmark. The LLM may explain a proposal but must not select or approve it invisibly.

## 54.6 — Add real migrations and audit events

Introduce Alembic, keyset pagination, PostgreSQL integration tests, structured audit events, and retention policies. Keep domain values frozen and repositories owner-scoped.

## 54.7 — Add stronger science models

Possible research directions include CALPHAD, DFT/ML potentials, displacement-cascade simulations, activation codes, tritium transport, thermal-mechanical finite elements, and microstructure-aware models. Each needs a separate validated adapter and provenance contract; none should be smuggled into the simple teaching proxy.

## Acceptance criteria

Write these before implementation:

- exact source/version provenance is round-trippable;
- missing scientific properties remain explicit `Err`/Option values;
- imported records cannot claim qualification;
- pure transformations remain deterministic;
- external adapters have recorded fixtures and bounded timeouts;
- a domain reviewer can reproduce every shortlist field from stored evidence.
