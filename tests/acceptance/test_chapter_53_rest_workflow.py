from pathlib import Path

import pytest

pytestmark = pytest.mark.chapter(53)


def test_capstone_routes_no_longer_contain_501_scaffolds() -> None:
    paths = (
        Path("app/api/auth_routes.py"),
        Path("app/api/campaign_routes.py"),
        Path("app/api/automation_routes.py"),
    )
    sources = tuple(map(lambda path: path.read_text(encoding="utf-8"), paths))
    assert all(map(lambda source: "HTTP_501_NOT_IMPLEMENTED" not in source, sources))
    assert all(map(lambda source: "ContainerDependency" in source, sources))
