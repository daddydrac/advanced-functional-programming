# 50 — Fusion-Materials Screening Math: Constraints, Proxies, and Pareto Fronts

## Goal

Build the pure scientific core that transforms candidate records into transparent, non-dominated shortlists. The result is a research triage artifact—not a reactor qualification decision.

## 50.1 — Separate measurements from teaching proxies

The input includes familiar thermophysical/elastic features plus normalized neutron, tritium, and activation proxies. In a real program, the latter depend on spectrum, fluence, temperature, microstructure, isotope inventory, time, and measurement/simulation method. Never present a proxy as a material constant.

## 50.2-50.3 — Implement Welford update

File: `app/domain/statistics.py`

For old count $n$, mean $\mu_n$, and new value $x$:

$$
n'=n+1,
\qquad \delta=x-\mu_n,
$$

$$
\mu_{n'}=\mu_n+\frac{\delta}{n'},
\qquad M_{2,n'}=M_{2,n}+\delta(x-\mu_{n'}).
$$

Return a new `RunningStats`; do not mutate the old value.

## 50.4 — Fold a feature stream

Implement `summarize` with `fold_left(append_value, EMPTY_STATS, values)`. Empty input returns the identity summary.

## 50.5 — Combine partitions

Implement the parallel Welford combination formula. `EMPTY_STATS` must be a left and right identity. This lets independent batches combine as a tree reduction.

## 50.6-50.7 — Variance and standardization

Use Bessel's correction for sample variance:

$$s^2=\frac{M_2}{n-1}.$$

Then $z=(x-\mu)/s$. Define variance as zero for $n<2$ and z-score as zero when deviation is zero.

## 50.8 — Compute the Pugh ratio

File: `app/domain/pipeline.py`

Use the explicit convention:

$$P=\frac{K}{G},$$

where $K$ is bulk modulus and $G$ is shear modulus. Literature sometimes uses the reciprocal, so the evidence string must name the convention. Treat it as a ductility-related screening descriptor, not a proof.

## 50.9 — Compute a thermal-stress proxy

For an intentionally simplified constrained-heating proxy:

$$\sigma_{proxy}=E\alpha\Delta T,$$

with $E$ converted from GPa to MPa, $\alpha$ converted from $10^{-6}/K$, and $\Delta T=\max(0,T_{op}-293.15)$. Document omitted geometry, Poisson effects, temperature dependence, plasticity, irradiation, and interfaces.

## 50.10 — Compose hard constraints

Implement `is_feasible` from predicates for melting point, thermal conductivity, energy above hull, and activation proxy. Use `all(map(...))`. A hard constraint is a policy choice, not a discovered truth.

## 50.11 — Build a transparent utility

Implement `score_candidate`. Normalize terms to compatible directions, keep coefficients visible, and create a `reasons` tuple naming every pass/failure and formula convention. Do not hide values in an opaque model.

## 50.12 — Define Pareto dominance

Candidate $a$ dominates $b$ when it is no worse in every chosen objective and strictly better in at least one:

$$
a\prec b \iff \left(\forall_i\;a_i\succeq_i b_i\right)
\land\left(\exists_j\;a_j\succ_j b_j\right).
$$

Maximize utility and Pugh ratio; minimize thermal stress, activation, tritium retention, and uncertainty. Compare only feasible scores.

## 50.13 — Compute the Pareto front

For each score, retain it only when no other score dominates it. Express the nested quantifiers with `filter`, `any`, and generator-free higher-order calls. Preserve a deterministic order.

## 50.14 — Rank for presentation

Implement `rank_candidates` as composition: score, retain feasible, sort by transparent utility with a stable material-ID tie breaker. Keep the Pareto front separate; a total ranking and a partial order answer different questions.

## 50.15 — Create a campaign

File: `app/services/screening.py`

Prepare candidates, rank them, calculate the front, create ID/time in the shell, persist candidates and campaign, and return `Result`. Do not call Ollama here.

## Acceptance criteria

```bash
CHAPTER=50 make chapter-test
```

- Welford summary matches a trusted small hand calculation;
- partitioned and single-pass summaries agree within tolerance;
- unit conversions in thermal stress are tested explicitly;
- dominance requires at least one strict improvement;
- dominated candidates are absent from the front;
- original candidates and policy remain unchanged;
- every score includes reasons and the synthetic-data warning remains visible.
