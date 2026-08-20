"""Provided course-browser infrastructure.

Unlike the capstone functions, this small service is intentionally complete so
learners can read every Markdown chapter through Swagger before implementing
the project.
"""

from dataclasses import dataclass
from pathlib import Path

from app.domain.result import Err, Ok, Result


@dataclass(frozen=True, slots=True)
class TutorialSummary:
    slug: str
    title: str
    part: str


@dataclass(frozen=True, slots=True)
class Tutorial:
    slug: str
    title: str
    part: str
    markdown: str


def title_from_path(path: Path) -> str:
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    return first_line.removeprefix("# ").strip()


class TutorialService:
    """Read-only Markdown catalog used only by the course shell."""

    def __init__(self, course_dir: Path) -> None:
        self._course_dir = course_dir

    def _paths(self) -> tuple[Path, ...]:
        paths = filter(lambda path: path.name != "README.md", self._course_dir.rglob("*.md"))
        return tuple(sorted(paths))

    def list(self) -> tuple[TutorialSummary, ...]:
        return tuple(
            map(
                lambda path: TutorialSummary(
                    slug=path.stem,
                    title=title_from_path(path),
                    part=path.parent.name,
                ),
                self._paths(),
            )
        )

    def get(self, slug: str) -> Result[Tutorial, str]:
        matches = tuple(filter(lambda path: path.stem == slug, self._paths()))
        if len(matches) != 1:
            return Err("tutorial not found")
        path = matches[0]
        return Ok(
            Tutorial(
                slug=slug,
                title=title_from_path(path),
                part=path.parent.name,
                markdown=path.read_text(encoding="utf-8"),
            )
        )
