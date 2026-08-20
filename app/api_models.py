"""Provided immutable REST schemas and student-owned boundary converters."""

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from app.domain.models import MaterialCandidate, ScreeningPolicy
from app.services.tutorials import Tutorial, TutorialSummary


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class MessageResponse(FrozenModel):
    message: str


class RegisterRequest(FrozenModel):
    email: str = Field(min_length=3, max_length=320)
    password: str = Field(min_length=12, max_length=256)


class RegistrationResponse(FrozenModel):
    user_id: str
    setup_token: str
    provisioning_uri: str
    manual_key: str


class PasswordLoginRequest(FrozenModel):
    email: str
    password: str


class MfaRequest(FrozenModel):
    token: str = Field(min_length=20)
    code: str = Field(pattern=r"^\d{6}$")


class SetupTokenRequest(FrozenModel):
    setup_token: str = Field(min_length=20)


class RefreshRequest(FrozenModel):
    refresh_token: str = Field(min_length=20)


class TokenPairResponse(FrozenModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(FrozenModel):
    user_id: str
    email: str
    mfa_enabled: bool
    created_at: datetime


class ElementFractionInput(FrozenModel):
    symbol: str = Field(min_length=1, max_length=3)
    atomic_fraction: float = Field(gt=0.0, le=1.0)


class MaterialPropertiesInput(FrozenModel):
    melting_point_k: float = Field(gt=0.0)
    thermal_conductivity_w_mk: float = Field(gt=0.0)
    thermal_expansion_1e6_per_k: float = Field(gt=0.0)
    young_modulus_gpa: float = Field(gt=0.0)
    bulk_modulus_gpa: float = Field(gt=0.0)
    shear_modulus_gpa: float = Field(gt=0.0)
    energy_above_hull_ev_atom: float = Field(ge=0.0)
    neutron_tolerance_proxy: float = Field(ge=0.0, le=1.0)
    tritium_retention_proxy: float = Field(ge=0.0, le=1.0)
    activation_proxy: float = Field(ge=0.0, le=1.0)


class EvidenceInput(FrozenModel):
    source: str = Field(min_length=1)
    method: str = Field(min_length=1)
    uncertainty_fraction: float = Field(ge=0.0, le=1.0)
    notes: str = ""


class MaterialCandidateInput(FrozenModel):
    material_id: str = Field(min_length=1, max_length=64)
    formula: str = Field(min_length=1, max_length=128)
    role: str
    composition: Annotated[tuple[ElementFractionInput, ...], Field(min_length=1)]
    properties: MaterialPropertiesInput
    evidence: tuple[EvidenceInput, ...] = ()

    def to_domain(self) -> MaterialCandidate:
        """Convert and validate the REST shape at the domain boundary.

        Chapter item: 45.5
        Tutorial: ``tutorials/part-3-application/45-fastapi-swagger-rest-only.md``
        Acceptance: ``CHAPTER=45 make chapter-test``
        """
        raise NotImplementedError("Chapter 45 item 45.5: convert candidate input")


class ScreeningPolicyInput(FrozenModel):
    minimum_melting_point_k: float = Field(gt=0.0)
    minimum_thermal_conductivity_w_mk: float = Field(gt=0.0)
    maximum_energy_above_hull_ev_atom: float = Field(ge=0.0)
    maximum_activation_proxy: float = Field(ge=0.0, le=1.0)
    operating_temperature_k: float = Field(gt=0.0)
    exploration_weight: float = Field(ge=0.0)

    def to_domain(self) -> ScreeningPolicy:
        """Convert policy input.

        Chapter item: 45.6
        Tutorial: ``tutorials/part-3-application/45-fastapi-swagger-rest-only.md``
        Acceptance: ``CHAPTER=45 make chapter-test``
        """
        raise NotImplementedError("Chapter 45 item 45.6: convert screening policy")


class ScreeningRequest(FrozenModel):
    disclaimer: str = Field(min_length=20)
    candidates: Annotated[tuple[MaterialCandidateInput, ...], Field(min_length=2, max_length=5_000)]
    policy: ScreeningPolicyInput


class MaterialScoreResponse(FrozenModel):
    material_id: str
    formula: str
    feasible: bool
    pugh_ratio: float
    thermal_stress_proxy_mpa: float
    utility: float
    uncertainty: float
    reasons: tuple[str, ...]


class CampaignResponse(FrozenModel):
    campaign_id: str
    created_at: datetime
    candidate_count: int
    pareto_front: tuple[MaterialScoreResponse, ...]
    ranked: tuple[MaterialScoreResponse, ...]


class PlanRequest(FrozenModel):
    campaign_id: str = Field(min_length=1)


class ExperimentPlanResponse(FrozenModel):
    plan_id: str
    campaign_id: str
    model: str
    content: str
    created_at: datetime


class TutorialSummaryResponse(FrozenModel):
    slug: str
    title: str
    part: str

    @classmethod
    def from_domain(cls, tutorial: TutorialSummary) -> TutorialSummaryResponse:
        """Provided conversion used by the course browser."""
        return cls(slug=tutorial.slug, title=tutorial.title, part=tutorial.part)


class TutorialResponse(TutorialSummaryResponse):
    markdown: str

    @classmethod
    def from_tutorial(cls, tutorial: Tutorial) -> TutorialResponse:
        """Provided conversion used by the course browser."""
        return cls(
            slug=tutorial.slug,
            title=tutorial.title,
            part=tutorial.part,
            markdown=tutorial.markdown,
        )
