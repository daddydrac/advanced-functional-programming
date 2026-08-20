"""Tests that must pass before the learner implements any chapter."""

import ast
from pathlib import Path

import yaml
from fastapi.testclient import TestClient

from app.main import app

FORBIDDEN = (
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.ListComp,
    ast.SetComp,
    ast.DictComp,
    ast.GeneratorExp,
)


def test_course_has_55_chapter_documents_with_acceptance_criteria() -> None:
    paths = tuple(filter(lambda path: path.name != "README.md", Path("tutorials").rglob("*.md")))
    documents = tuple(map(lambda path: path.read_text(encoding="utf-8"), paths))
    assert len(paths) == 55
    assert all(map(lambda text: text.startswith("# "), documents))
    assert all(map(lambda text: "## Acceptance criteria" in text, documents))
    assert all(map(lambda text: text.count("```") % 2 == 0, documents))


def test_course_browser_works_and_capstone_starts_incomplete() -> None:
    with TestClient(app) as client:
        index = client.get("/v1/tutorials")
        chapter = client.get("/v1/tutorials/50-fusion-screening-math")
        incomplete = client.post("/v1/campaigns/screen", json={})
    assert index.status_code == 200
    assert len(index.json()) == 55
    assert chapter.status_code == 200
    assert "Pareto" in chapter.json()["markdown"]
    assert incomplete.status_code in (422, 501)


def test_compose_contains_runtime_and_tooling_services() -> None:
    compose = yaml.safe_load(Path("compose.yaml").read_text(encoding="utf-8"))
    assert frozenset(compose["services"]) == frozenset(
        ("api", "postgres", "ollama", "model-pull", "init", "test")
    )
    assert compose["services"]["api"]["build"]["target"] == "production"
    assert compose["services"]["test"]["build"]["target"] == "test"
    assert compose["services"]["test"]["profiles"] == ["tools"]
    assert compose["services"]["test"]["environment"]["CHAPTER"] == "${CHAPTER:-}"


def test_production_source_contains_no_loop_or_comprehension_syntax() -> None:
    paths = Path("app").rglob("*.py")
    nodes = map(
        lambda path: ast.walk(ast.parse(path.read_text(encoding="utf-8"), filename=str(path))),
        paths,
    )
    forbidden = tuple(filter(lambda node: isinstance(node, FORBIDDEN), map_from_walks(nodes)))
    assert forbidden == ()


def map_from_walks(walks: object) -> tuple[ast.AST, ...]:
    """Flatten AST walks without adding forbidden syntax to the test itself."""
    from itertools import chain

    return tuple(chain.from_iterable(walks))  # type: ignore[arg-type]


def test_every_placeholder_points_to_a_numbered_chapter() -> None:
    paths = tuple(Path("app").rglob("*.py"))
    trees = map(
        lambda path: ast.parse(path.read_text(encoding="utf-8"), filename=str(path)),
        paths,
    )
    nodes = map_from_walks(map(ast.walk, trees))
    functions = filter(
        lambda node: isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)), nodes
    )
    placeholders = tuple(filter(is_placeholder_function, functions))
    docstrings = tuple(map(lambda node: ast.get_docstring(node) or "", placeholders))
    assert placeholders
    assert all(map(lambda text: "Chapter item" in text, docstrings))
    assert all(map(lambda text: "Tutorial:" in text, docstrings))
    assert all(map(lambda text: "Acceptance:" in text, docstrings))


def is_placeholder_function(node: ast.AST) -> bool:
    """Identify student-owned functions without implementing forbidden syntax."""
    calls = filter(lambda part: isinstance(part, ast.Call), ast.walk(node))
    names = map(lambda call: call.func, calls)
    return any(
        map(
            lambda name: isinstance(name, ast.Name) and name.id == "NotImplementedError",
            names,
        )
    )
