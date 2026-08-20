"""Frozen sample values for acceptance tests; contains no solution algorithms."""

from app.domain.models import (
    ElementFraction,
    Evidence,
    MaterialCandidate,
    MaterialProperties,
    ReactorRole,
    ScreeningPolicy,
)


def candidate(
    material_id: str = "candidate-a",
    formula: str = "W70Ta30",
    bulk_modulus_gpa: float = 250.0,
    shear_modulus_gpa: float = 125.0,
    activation_proxy: float = 0.4,
) -> MaterialCandidate:
    return MaterialCandidate(
        material_id=material_id,
        formula=formula,
        role=ReactorRole.PLASMA_FACING,
        composition=(ElementFraction("W", 0.7), ElementFraction("Ta", 0.3)),
        properties=MaterialProperties(
            melting_point_k=3400.0,
            thermal_conductivity_w_mk=100.0,
            thermal_expansion_1e6_per_k=5.0,
            young_modulus_gpa=300.0,
            bulk_modulus_gpa=bulk_modulus_gpa,
            shear_modulus_gpa=shear_modulus_gpa,
            energy_above_hull_ev_atom=0.02,
            neutron_tolerance_proxy=0.8,
            tritium_retention_proxy=0.3,
            activation_proxy=activation_proxy,
        ),
        evidence=(Evidence("synthetic-test", "fixture", 0.2, "not scientific data"),),
    )


def policy() -> ScreeningPolicy:
    return ScreeningPolicy(
        minimum_melting_point_k=2900.0,
        minimum_thermal_conductivity_w_mk=40.0,
        maximum_energy_above_hull_ev_atom=0.05,
        maximum_activation_proxy=0.7,
        operating_temperature_k=1200.0,
        exploration_weight=0.35,
    )
