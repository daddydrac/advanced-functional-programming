# Skeleton-to-Chapter Implementation Map

Use this as the repository backlog. An item is complete only when its chapter test passes and the source contains no placeholder for that item.

| Chapter | Exact file | Skeletons/items |
|---:|---|---|
| 26 | `app/domain/folds.py` | 26.2 `compose`; 26.4 `pipe` |
| 28 | `app/domain/folds.py` | 28.2 `fold_left`; 28.3-28.5 `fold_right` |
| 29 | `app/domain/folds.py` | 29.2 `map_from_fold_right`; 29.3 `filter_from_fold_right`; 29.4 `flat_map_from_fold_right`; 29.5 `concat` |
| 36 | `app/domain/result.py` | 36.2 `map_result`; 36.3 `collect_results`; 36.5 `unwrap_or` |
| 37 | `app/domain/result.py` | 37.2 `bind_result` and monad-law reasoning |
| 39 | `app/domain/lenses.py` | 39.2-39.6 lens operations and `dataclass_lens` |
| 40 | `app/domain/lenses.py` | 40.2-40.4 executable lens laws |
| 45 | `app/api_models.py`, `app/api/*.py` | request-to-domain conversion and REST handlers |
| 46 | `app/domain/pipeline.py`, `app/dependencies.py` | normalization, validation, composition, dependency wiring |
| 47 | `app/infrastructure/database.py`, `repositories.py` | sessions, row/domain mapping, owner-scoped persistence |
| 48 | `app/infrastructure/security.py`, `app/services/auth.py`, `app/api/auth_routes.py` | JWT, passwords, refresh rotation, logout, throttling |
| 49 | same auth/security/API files | TOTP provisioning, in-memory SVG QR, encryption, replay protection, MFA state machine |
| 50 | `app/domain/statistics.py`, `pipeline.py`, `services/screening.py` | Welford stats, Pugh ratio, thermal proxy, feasibility, Pareto front, ranking |
| 51 | `app/domain/pipeline.py`, `services/ollama.py`, `automation.py` | acquisition, evidence packet, constrained prompt, local model call, persistence |
| 52 | `app/infrastructure/database.py`, `app/api/health_routes.py` | readiness, cleanup, operational errors |
| 53 | `app/dependencies.py`, `app/api/*.py`, `app/main.py` | Bearer/current-user dependencies and complete authenticated REST workflow |

Detailed acceptance statements and worked examples live in the named chapter Markdown files. Run `CHAPTER=<number> make chapter-test` from the repository root.
