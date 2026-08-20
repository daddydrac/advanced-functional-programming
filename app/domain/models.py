"""Provided immutable data shapes for the LambdaFlux workshop.

These frozen dataclasses are scaffolding, not completed business logic. Extend
them only when a chapter explicitly asks you to do so.

Chapter items: 03.4-03.7
Tutorial: ``tutorials/part-1-python/03-types-and-frozen-data.md``
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class ReactorRole(StrEnum):
    """Simplified component roles used in the educational screening problem."""

    PLASMA_FACING = "plasma_facing"
    STRUCTURAL = "structural"
    BREEDER_BLANKET = "breeder_blanket"


@dataclass(frozen=True, slots=True)
class ElementFraction:
    symbol: str
    atomic_fraction: float


@dataclass(frozen=True, slots=True)
class MaterialProperties:
    """Research-inspired features; bundled values are synthetic, not qualified data."""

    melting_point_k: float
    thermal_conductivity_w_mk: float
    thermal_expansion_1e6_per_k: float
    young_modulus_gpa: float
    bulk_modulus_gpa: float
    shear_modulus_gpa: float
    energy_above_hull_ev_atom: float
    neutron_tolerance_proxy: float
    tritium_retention_proxy: float
    activation_proxy: float


@dataclass(frozen=True, slots=True)
class Evidence:
    source: str
    method: str
    uncertainty_fraction: float
    notes: str


@dataclass(frozen=True, slots=True)
class MaterialCandidate:
    material_id: str
    formula: str
    role: ReactorRole
    composition: tuple[ElementFraction, ...]
    properties: MaterialProperties
    evidence: tuple[Evidence, ...] = ()


@dataclass(frozen=True, slots=True)
class ScreeningPolicy:
    minimum_melting_point_k: float
    minimum_thermal_conductivity_w_mk: float
    maximum_energy_above_hull_ev_atom: float
    maximum_activation_proxy: float
    operating_temperature_k: float
    exploration_weight: float


@dataclass(frozen=True, slots=True)
class RunningStats:
    count: int
    mean: float
    m2: float
    minimum: float
    maximum: float


@dataclass(frozen=True, slots=True)
class MaterialScore:
    candidate: MaterialCandidate
    feasible: bool
    pugh_ratio: float
    thermal_stress_proxy_mpa: float
    utility: float
    uncertainty: float
    reasons: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ScreeningCampaign:
    campaign_id: str
    owner_id: str
    created_at: datetime
    policy: ScreeningPolicy
    candidate_count: int
    pareto_front: tuple[MaterialScore, ...]
    ranked: tuple[MaterialScore, ...]


@dataclass(frozen=True, slots=True)
class User:
    user_id: str
    email: str
    password_hash: str
    encrypted_mfa_secret: str
    mfa_enabled: bool
    last_totp_step: int
    created_at: datetime


@dataclass(frozen=True, slots=True)
class ExperimentPlan:
    plan_id: str
    campaign_id: str
    owner_id: str
    model: str
    content: str
    created_at: datetime
