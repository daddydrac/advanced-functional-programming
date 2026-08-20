import pytest

from app.api_models import (
    ElementFractionInput,
    EvidenceInput,
    MaterialCandidateInput,
    MaterialPropertiesInput,
    ScreeningPolicyInput,
)
from app.domain.models import ReactorRole

pytestmark = pytest.mark.chapter(45)


def test_rest_inputs_convert_to_frozen_domain_values() -> None:
    request = MaterialCandidateInput(
        material_id="m-1",
        formula="W70Ta30",
        role="plasma_facing",
        composition=(
            ElementFractionInput(symbol="W", atomic_fraction=0.7),
            ElementFractionInput(symbol="Ta", atomic_fraction=0.3),
        ),
        properties=MaterialPropertiesInput(
            melting_point_k=3400.0,
            thermal_conductivity_w_mk=100.0,
            thermal_expansion_1e6_per_k=5.0,
            young_modulus_gpa=300.0,
            bulk_modulus_gpa=250.0,
            shear_modulus_gpa=125.0,
            energy_above_hull_ev_atom=0.02,
            neutron_tolerance_proxy=0.8,
            tritium_retention_proxy=0.3,
            activation_proxy=0.4,
        ),
        evidence=(
            EvidenceInput(
                source="synthetic",
                method="fixture",
                uncertainty_fraction=0.2,
                notes="not scientific data",
            ),
        ),
    )
    candidate = request.to_domain()
    assert candidate.role is ReactorRole.PLASMA_FACING
    assert candidate.composition[1].symbol == "Ta"
    assert candidate.evidence[0].uncertainty_fraction == 0.2


def test_policy_conversion() -> None:
    policy = ScreeningPolicyInput(
        minimum_melting_point_k=2900.0,
        minimum_thermal_conductivity_w_mk=40.0,
        maximum_energy_above_hull_ev_atom=0.05,
        maximum_activation_proxy=0.7,
        operating_temperature_k=1200.0,
        exploration_weight=0.35,
    ).to_domain()
    assert policy.operating_temperature_k == 1200.0
