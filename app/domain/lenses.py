"""Typed lens exercises for immutable material records."""

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Lens[S, A]:
    """A lawful focus from source ``S`` to value ``A``.

    Chapter: 39
    Tutorial: ``tutorials/part-2-functional/39-lenses.md``
    """

    getter: Callable[[S], A]
    setter: Callable[[S, A], S]

    def get(self, source: S) -> A:
        """Read the focus.

        Chapter item: 39.2
        Tutorial: ``tutorials/part-2-functional/39-lenses.md``
        Acceptance: ``CHAPTER=39 make chapter-test``
        """
        raise NotImplementedError("Chapter 39 item 39.2: implement Lens.get")

    def set(self, value: A, source: S) -> S:
        """Return a new source with one focus replaced.

        Chapter item: 39.3
        Tutorial: ``tutorials/part-2-functional/39-lenses.md``
        Acceptance: ``CHAPTER=39 make chapter-test``
        """
        raise NotImplementedError("Chapter 39 item 39.3: implement Lens.set")

    def modify(self, function: Callable[[A], A], source: S) -> S:
        """Transform only the focus.

        Chapter item: 39.4
        Tutorial: ``tutorials/part-2-functional/39-lenses.md``
        Acceptance: ``CHAPTER=39 make chapter-test``
        """
        raise NotImplementedError("Chapter 39 item 39.4: implement Lens.modify")

    def compose[B](self, inner: Lens[A, B]) -> Lens[S, B]:
        """Compose two lenses.

        Chapter item: 39.5
        Tutorial: ``tutorials/part-2-functional/39-lenses.md``
        Acceptance: ``CHAPTER=39 make chapter-test``
        """
        raise NotImplementedError("Chapter 39 item 39.5: implement Lens.compose")


def dataclass_lens(attribute: str) -> Lens[object, object]:
    """Construct a lens with ``getattr`` and ``dataclasses.replace``.

    Chapter item: 39.6
    Tutorial: ``tutorials/part-2-functional/39-lenses.md``
    Acceptance: ``CHAPTER=39 make chapter-test``
    """
    raise NotImplementedError("Chapter 39 item 39.6: build a dataclass lens")


def law_get_put[S, A](lens: Lens[S, A], source: S) -> bool:
    """Check get-put.

    Chapter item: 40.2
    Tutorial: ``tutorials/part-2-functional/40-property-testing-functional-laws.md``
    Acceptance: ``CHAPTER=40 make chapter-test``
    """
    raise NotImplementedError("Chapter 40 item 40.2: encode get-put")


def law_put_get[S, A](lens: Lens[S, A], source: S, value: A) -> bool:
    """Check put-get.

    Chapter item: 40.3
    Tutorial: ``tutorials/part-2-functional/40-property-testing-functional-laws.md``
    Acceptance: ``CHAPTER=40 make chapter-test``
    """
    raise NotImplementedError("Chapter 40 item 40.3: encode put-get")


def law_put_put[S, A](lens: Lens[S, A], source: S, first: A, second: A) -> bool:
    """Check put-put.

    Chapter item: 40.4
    Tutorial: ``tutorials/part-2-functional/40-property-testing-functional-laws.md``
    Acceptance: ``CHAPTER=40 make chapter-test``
    """
    raise NotImplementedError("Chapter 40 item 40.4: encode put-put")
