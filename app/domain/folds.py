"""Student exercises for folds and functional composition.

Every public function is intentionally incomplete. Follow the referenced
chapter item, implement it, then run that chapter's acceptance tests.
"""

from collections.abc import Callable, Iterable


def fold_left[A, B](function: Callable[[B, A], B], initial: B, values: Iterable[A]) -> B:
    """Reduce values from left to right.

    Chapter item: 28.2
    Tutorial: ``tutorials/part-2-functional/28-foldl-and-foldr.md``
    Acceptance: ``CHAPTER=28 make chapter-test``

    Required shape: ``f(...f(f(initial, x1), x2), xn)``. Production code may
    not use loop or comprehension syntax.
    """
    raise NotImplementedError("Chapter 28 item 28.2: implement fold_left")


def fold_right[A, B](function: Callable[[A, B], B], initial: B, values: Iterable[A]) -> B:
    """Reduce a finite iterable into a right-associated expression.

    Chapter items: 28.3-28.5
    Tutorial: ``tutorials/part-2-functional/28-foldl-and-foldr.md``
    Acceptance: ``CHAPTER=28 make chapter-test``

    Preserve input order and remain stack-safe. Explain why strict Python
    cannot reproduce Haskell's lazy ``foldr`` over an infinite list.
    """
    raise NotImplementedError("Chapter 28 item 28.3: implement fold_right")


def map_from_fold_right[A, B](function: Callable[[A], B], values: Iterable[A]) -> tuple[B, ...]:
    """Derive order-preserving ``map`` using only ``fold_right``.

    Chapter item: 29.2
    Tutorial: ``tutorials/part-2-functional/29-derive-map-filter-flatmap.md``
    Acceptance: ``CHAPTER=29 make chapter-test``
    """
    raise NotImplementedError("Chapter 29 item 29.2: derive map from fold_right")


def filter_from_fold_right[A](predicate: Callable[[A], bool], values: Iterable[A]) -> tuple[A, ...]:
    """Derive order-preserving ``filter`` using only ``fold_right``.

    Chapter item: 29.3
    Tutorial: ``tutorials/part-2-functional/29-derive-map-filter-flatmap.md``
    Acceptance: ``CHAPTER=29 make chapter-test``
    """
    raise NotImplementedError("Chapter 29 item 29.3: derive filter from fold_right")


def flat_map_from_fold_right[A, B](
    function: Callable[[A], Iterable[B]], values: Iterable[A]
) -> tuple[B, ...]:
    """Map each material to many features and flatten exactly once.

    Chapter item: 29.4
    Tutorial: ``tutorials/part-2-functional/29-derive-map-filter-flatmap.md``
    Acceptance: ``CHAPTER=29 make chapter-test``
    """
    raise NotImplementedError("Chapter 29 item 29.4: derive flatMap")


def compose(*functions: Callable[[object], object]) -> Callable[[object], object]:
    """Return the mathematical composition ``f(g(h(x)))``.

    Chapter items: 26.2-26.3
    Tutorial: ``tutorials/part-2-functional/26-composition-currying-and-partial.md``
    Acceptance: ``CHAPTER=26 make chapter-test``
    """
    raise NotImplementedError("Chapter 26 item 26.2: implement compose")


def pipe[A](value: A, *functions: Callable[[object], object]) -> object:
    """Apply functions left to right in data-flow order.

    Chapter item: 26.4
    Tutorial: ``tutorials/part-2-functional/26-composition-currying-and-partial.md``
    Acceptance: ``CHAPTER=26 make chapter-test``
    """
    raise NotImplementedError("Chapter 26 item 26.4: implement pipe")


def concat[A](values: Iterable[Iterable[A]]) -> tuple[A, ...]:
    """Flatten one level while preserving left-to-right order.

    Chapter item: 29.5
    Tutorial: ``tutorials/part-2-functional/29-derive-map-filter-flatmap.md``
    Acceptance: ``CHAPTER=29 make chapter-test``
    """
    raise NotImplementedError("Chapter 29 item 29.5: implement concat as a fold")
