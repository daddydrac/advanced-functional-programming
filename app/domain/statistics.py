"""Immutable streaming-statistics exercises for feature normalization."""

from collections.abc import Iterable
from math import inf

from app.domain.models import RunningStats

EMPTY_STATS = RunningStats(count=0, mean=0.0, m2=0.0, minimum=inf, maximum=-inf)


def append_value(stats: RunningStats, value: float) -> RunningStats:
    """Add one value with Welford's numerically stable recurrence.

    Chapter items: 50.2-50.3
    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.2: implement Welford append")


def summarize(values: Iterable[float]) -> RunningStats:
    """Fold values into ``RunningStats``.

    Chapter item: 50.4
    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.4: summarize with fold_left")


def combine(left: RunningStats, right: RunningStats) -> RunningStats:
    """Combine summaries as a monoid operation.

    Chapter items: 27.5 and 50.5
    Tutorial:
      - ``tutorials/part-2-functional/27-semigroups-monoids-and-groups.md``
      - ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.5: implement parallel combine")


def sample_variance(stats: RunningStats) -> float:
    """Return Bessel-corrected variance.

    Chapter item: 50.6
    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.6: implement sample variance")


def standard_deviation(stats: RunningStats) -> float:
    """Return non-negative standard deviation.

    Chapter item: 50.6
    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.6: implement standard deviation")


def z_score(value: float, stats: RunningStats) -> float:
    """Standardize a feature and define zero-variance behavior.

    Chapter item: 50.7
    Tutorial: ``tutorials/part-3-application/50-fusion-screening-math.md``
    Acceptance: ``CHAPTER=50 make chapter-test``
    """
    raise NotImplementedError("Chapter 50 item 50.7: implement z_score")
