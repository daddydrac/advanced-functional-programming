"""A small typed ``Result`` algebra for chapter-driven implementation."""

from collections.abc import Callable, Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Ok[T]:
    """The successful branch of ``Result[T, E]``."""

    value: T


@dataclass(frozen=True, slots=True)
class Err[E]:
    """The failure branch of ``Result[T, E]``."""

    error: E


type Result[T, E] = Ok[T] | Err[E]


def map_result[T, U, E](function: Callable[[T], U], result: Result[T, E]) -> Result[U, E]:
    """Map success and preserve failure.

    Chapter item: 36.2
    Tutorial: ``tutorials/part-2-functional/36-option-result-and-either.md``
    Acceptance: ``CHAPTER=36 make chapter-test``
    """
    raise NotImplementedError("Chapter 36 item 36.2: implement Result.map")


def bind_result[T, U, E](
    function: Callable[[T], Result[U, E]], result: Result[T, E]
) -> Result[U, E]:
    """Sequence a computation that can itself fail.

    Chapter items: 37.2-37.4
    Tutorial: ``tutorials/part-2-functional/37-monads-and-pymonad.md``
    Acceptance: ``CHAPTER=37 make chapter-test``
    """
    raise NotImplementedError("Chapter 37 item 37.2: implement monadic bind")


def collect_results[T, E](results: Iterable[Result[T, E]]) -> Result[tuple[T, ...], E]:
    """Collect successes or return the first error, using a fold.

    Chapter items: 36.3-36.4
    Tutorial: ``tutorials/part-2-functional/36-option-result-and-either.md``
    Acceptance: ``CHAPTER=36 make chapter-test``
    """
    raise NotImplementedError("Chapter 36 item 36.3: collect Results")


def unwrap_or[T, E](default: T, result: Result[T, E]) -> T:
    """Extract a success or return a caller-supplied default.

    Chapter item: 36.5
    Tutorial: ``tutorials/part-2-functional/36-option-result-and-either.md``
    Acceptance: ``CHAPTER=36 make chapter-test``
    """
    raise NotImplementedError("Chapter 36 item 36.5: implement unwrap_or")
