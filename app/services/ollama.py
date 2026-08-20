"""Local Ollama adapter skeleton for grounded experiment planning."""

from app.domain.models import ScreeningCampaign
from app.domain.result import Result


def evidence_packet(campaign: ScreeningCampaign) -> tuple[str, ...]:
    """Create deterministic, provenance-aware lines before any LLM call.

    Chapter item: 51.3
    Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
    Acceptance: ``CHAPTER=51 make chapter-test``
    """
    raise NotImplementedError("Chapter 51 item 51.3: build evidence packet")


def experiment_prompt(campaign: ScreeningCampaign) -> str:
    """Constrain the model to supplied evidence, hypotheses, and next tests.

    Chapter items: 51.4-51.5
    Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
    Acceptance: ``CHAPTER=51 make chapter-test``

    The prompt must forbid claims of reactor qualification, invented values,
    and safety conclusions. It must request citations to material IDs.
    """
    raise NotImplementedError("Chapter 51 item 51.4: create grounded prompt")


class OllamaClient:
    def __init__(self, base_url: str, model: str, timeout_seconds: float) -> None:
        self._base_url = base_url
        self._model = model
        self._timeout_seconds = timeout_seconds

    async def propose(self, campaign: ScreeningCampaign) -> Result[str, str]:
        """POST a non-streaming chat request to local Ollama.

        Chapter item: 51.6
        Tutorial: ``tutorials/part-3-application/51-ollama-experiment-planner.md``
        Acceptance: ``CHAPTER=51 make chapter-test``
        """
        raise NotImplementedError("Chapter 51 item 51.6: call Ollama")
