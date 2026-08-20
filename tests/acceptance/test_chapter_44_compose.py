from pathlib import Path

import pytest
import yaml

pytestmark = pytest.mark.chapter(44)


def test_compose_models_the_complete_workshop() -> None:
    compose = yaml.safe_load(Path("compose.yaml").read_text(encoding="utf-8"))
    services = compose["services"]
    assert frozenset(services) == frozenset(
        ("api", "postgres", "ollama", "model-pull", "init", "test")
    )
    assert services["api"]["depends_on"]["postgres"]["condition"] == "service_healthy"
    assert services["api"]["depends_on"]["model-pull"]["condition"] == (
        "service_completed_successfully"
    )
    assert services["init"]["profiles"] == ["tools"]
    assert services["test"]["profiles"] == ["tools"]
