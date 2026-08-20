# Curriculum Coverage Matrix

The lessons are original and use LambdaFlux examples. “Modeled after” means the topic sequence and skill coverage are mapped—not that source prose or code is copied.

## W3Schools core Python mapping

| Reference topic | LambdaFlux lesson(s) |
|---|---|
| Home, intro, get started, syntax/statements, output, comments | 01 |
| Variables, names, multiple values, output/global variables | 02 |
| Data types | 03 |
| Numbers, casting, math, module math/cmath concepts | 04 |
| Strings, slicing, methods, concatenation, formatting, escapes | 05 |
| Booleans and every operator family | 06 |
| Lists, comprehensions, arrays, sorting/copying/joining/methods | 07 |
| Tuples, access/update/unpack/join/methods | 08 |
| Sets, joins, frozenset, methods | 09 |
| Dictionaries, copying/nesting/methods, JSON | 10 |
| If, elif, else, shorthand, nesting, pass | 11 |
| Match | 12 |
| While loops, translated to state transitions/folds | 13 |
| For loops and range, translated to higher-order functions | 14 |
| Functions, arguments, args/kwargs, scope | 15 |
| Lambda, decorators, generators | 16 |
| Recursion | 17 |
| Iterators and generators | 18 |
| Modules, pip, virtual environments | 19 |
| Dates, None, input, try/except | 20 |
| OOP, classes, init, self, properties, class methods, inheritance, polymorphism | 21 |
| Encapsulation and inner classes | 22 |
| File handling/read/write/create/delete concepts | 23 |
| Regex | 05 |
| Integrated Python review | 24 |

The W3Schools navigation also links separate NumPy, Pandas, SciPy, Matplotlib, machine-learning, DSA, MySQL, and MongoDB curricula. This course adapts the database branch to the user's requested SQLAlchemy/PostgreSQL stack and focuses the numerical/data-science branch on functional statistics, folds, combinatorics, and a capstone rather than reproducing those separate product tutorials.

## Functional Python Programming, Third Edition mapping

| Book/repository chapter theme | LambdaFlux lesson(s) |
|---|---|
| Understanding Functional Programming | 25 |
| Essential Functional Concepts | 26–27 |
| Functions, Iterators, and Generators | 15–18, 30 |
| Working with Collections | 07–10, 29 |
| Higher-Order Functions | 14–16, 26, 29 |
| Recursions and Reductions | 17, 28 |
| Complex Stateless Objects | 03, 36, 39 |
| The Itertools Module | 31 |
| Combinatorics, Permutations, Combinations | 32 |
| The Functools Module | 33 |
| The Toolz Package | 34 |
| Decorator Design Techniques | 35 |
| The PyMonad Library | 36–38 |
| Multiprocessing, Threading, Concurrent Futures | 41 |
| Functional Web Services | 42, 45–47 |
| Optimization/bonus themes | 30, 41, 52, 54 |

## Added course-specific requirements

| Requirement | Coverage |
|---|---|
| Referential transparency | 01, 25 and domain tests |
| Composition $f(g(x))$ | 02, 26 |
| Heavy math/algebra | 04, 27–29, 32, 40–41, 50 |
| `foldr` and folding arrays | 07, 17, 28–29 |
| Monads | 36–38 |
| Lenses and laws | 39 plus property tests |
| No loops; map/filter/reduce/flatMap | all production `app` code plus AST test |
| Frozen dataclass type safety | 03 and all domain models |
| Docker/containerization | 43–44 |
| FastAPI/Swagger, REST only | 42, 45, 53 |
| SQLAlchemy ORM/PostgreSQL | 47 |
| JWT + Google Authenticator MFA | 48–49 |
| Local Ollama automation | 51 |
| Fusion-material roles and evidence provenance | 00, 03, 45, 50, 54 |
| Elastic/thermal feature engineering | 04, 27, 50 |
| Pareto partial orders and multi-objective screening | 06, 27, 40, 50 |
| Uncertainty-aware next-experiment acquisition | 40, 50-51 |
| OPTIMADE and Materials Project extensions | 54 |

## Workshop implementation policy

The repository intentionally supplies no completed capstone algorithms. Chapters 26-53 name exact skeleton functions and staged tests. Examples demonstrate the concept on smaller values, while acceptance criteria require the learner to construct the LambdaFlux implementation.
