"""Deterministic audit of two coherent vacuum plane waves crossing at 120°.

This standard-library calculation verifies the algebra documented by N015. It is
not a field solver and does not model or detect a neutrino.
"""

from __future__ import annotations

import math
from typing import Dict, Tuple

Vector = Tuple[float, float, float]
TRINITY_ANGLE = 2.0 * math.pi / 3.0
TRINITY_PHASE = 2.0 * math.pi / 3.0


def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: Vector) -> float:
    return math.sqrt(dot(a, a))


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def subtract(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def cross(a: Vector, b: Vector) -> Vector:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def scale(factor: float, a: Vector) -> Vector:
    return tuple(factor * x for x in a)  # type: ignore[return-value]


def directions(alpha: float = TRINITY_ANGLE) -> Tuple[Vector, Vector]:
    """Return unit directions symmetric about +x with crossing angle alpha."""
    half = alpha / 2.0
    return (math.cos(half), math.sin(half), 0.0), (
        math.cos(half),
        -math.sin(half),
        0.0,
    )


def observables(gamma: float, alpha: float = TRINITY_ANGLE) -> Dict[str, object]:
    """Return dimensionless phasor and cycle-averaged observables."""
    n1, n2 = directions(alpha)
    phase_cos = math.cos(gamma)
    direction_sum = add(n1, n2)
    electric_phasor_sq = 2.0 * (1.0 + phase_cos)
    magnetic_phasor_sq_c2 = 2.0 + 2.0 * math.cos(alpha) * phase_cos
    energy_density = 0.25 * (electric_phasor_sq + magnetic_phasor_sq_c2)
    poynting = scale(1.0 + phase_cos, direction_sum)
    invariant_1 = 0.5 * (electric_phasor_sq - magnetic_phasor_sq_c2)
    return {
        "electric_phasor_sq": electric_phasor_sq,
        "magnetic_phasor_sq_c2": magnetic_phasor_sq_c2,
        "energy_density": energy_density,
        "poynting": poynting,
        "momentum_density_scaled": poynting,
        "invariant_1": invariant_1,
        "invariant_2": 0.0,
    }


def energy_phase_derivative(gamma: float, alpha: float = TRINITY_ANGLE) -> float:
    return -0.5 * (1.0 + math.cos(alpha)) * math.sin(gamma)


def flux_phase_derivative(gamma: float, alpha: float = TRINITY_ANGLE) -> float:
    n1, n2 = directions(alpha)
    return -norm(add(n1, n2)) * math.sin(gamma)


def direct_cycle_average(
    gamma: float, alpha: float = TRINITY_ANGLE, samples: int = 1440
) -> Dict[str, object]:
    """Independently average the real E/B fields with E0=c=eps0=mu0=1."""
    n1, n2 = directions(alpha)
    polarization: Vector = (0.0, 0.0, 1.0)
    b1_direction = cross(n1, polarization)
    b2_direction = cross(n2, polarization)
    energy_sum = 0.0
    flux_sum: Vector = (0.0, 0.0, 0.0)
    invariant_sum = 0.0
    for index in range(samples):
        optical_phase = 2.0 * math.pi * index / samples
        e1 = scale(math.cos(optical_phase), polarization)
        e2 = scale(math.cos(optical_phase - gamma), polarization)
        b1 = scale(math.cos(optical_phase), b1_direction)
        b2 = scale(math.cos(optical_phase - gamma), b2_direction)
        electric = add(e1, e2)
        magnetic = add(b1, b2)
        energy_sum += 0.5 * (dot(electric, electric) + dot(magnetic, magnetic))
        flux_sum = add(flux_sum, cross(electric, magnetic))
        invariant_sum += dot(electric, electric) - dot(magnetic, magnetic)
    return {
        "energy_density": energy_sum / samples,
        "poynting": scale(2.0 / samples, flux_sum),  # divide by I0=1/2
        "invariant_1": invariant_sum / samples,
    }


def verify_baseline() -> Dict[str, bool]:
    n1, n2 = directions()
    nsum = add(n1, n2)
    ndifference = subtract(n1, n2)
    polarization: Vector = (0.0, 0.0, 1.0)
    at_zero = observables(0.0)
    at_trinity = observables(TRINITY_PHASE)
    at_pi = observables(math.pi)
    direct_trinity = direct_cycle_average(TRINITY_PHASE)
    general_cases = (
        (math.pi / 3.0, 0.4),
        (math.pi / 2.0, 1.2),
        (TRINITY_ANGLE, 2.3),
    )

    general_angle_direct_average = True
    for alpha, gamma in general_cases:
        analytic = observables(gamma, alpha)
        direct = direct_cycle_average(gamma, alpha)
        general_angle_direct_average = general_angle_direct_average and math.isclose(
            float(direct["energy_density"]), float(analytic["energy_density"]), abs_tol=4e-15
        )
        general_angle_direct_average = general_angle_direct_average and all(
            math.isclose(direct["poynting"][axis], analytic["poynting"][axis], abs_tol=4e-15)  # type: ignore[index]
            for axis in range(3)
        )
        general_angle_direct_average = general_angle_direct_average and math.isclose(
            float(direct["invariant_1"]), float(analytic["invariant_1"]), abs_tol=4e-15
        )

    samples = [observables(2.0 * math.pi * index / 720.0) for index in range(720)]
    mean_energy = sum(float(item["energy_density"]) for item in samples) / len(samples)
    mean_flux = tuple(
        sum(item["poynting"][axis] for item in samples) / len(samples)  # type: ignore[index]
        for axis in range(3)
    )

    return {
        "crossing_angle_120": math.isclose(dot(n1, n2), -0.5, abs_tol=2e-15),
        "wavevector_sum": math.isclose(norm(nsum), 1.0, rel_tol=2e-15),
        "wavevector_difference": math.isclose(norm(ndifference), math.sqrt(3.0), rel_tol=2e-15),
        "common_transverse_polarization": math.isclose(dot(n1, polarization), 0.0, abs_tol=1e-15)
        and math.isclose(dot(n2, polarization), 0.0, abs_tol=1e-15),
        "fringe_spacing": math.isclose(1.0 / norm(ndifference), 1.0 / math.sqrt(3.0), rel_tol=2e-15),
        "trinity_electric_amplitude": math.isclose(
            math.sqrt(float(at_trinity["electric_phasor_sq"])), 1.0, rel_tol=2e-15
        ),
        "trinity_energy": math.isclose(float(at_trinity["energy_density"]), 7.0 / 8.0, rel_tol=2e-15),
        "trinity_flux": math.isclose(norm(at_trinity["poynting"]), 0.5, rel_tol=2e-15),  # type: ignore[arg-type]
        "trinity_not_extremum": not math.isclose(energy_phase_derivative(TRINITY_PHASE), 0.0, abs_tol=1e-12)
        and not math.isclose(flux_phase_derivative(TRINITY_PHASE), 0.0, abs_tol=1e-12),
        "phase_endpoints": math.isclose(float(at_zero["energy_density"]), 5.0 / 4.0, rel_tol=2e-15)
        and math.isclose(float(at_pi["energy_density"]), 3.0 / 4.0, rel_tol=2e-15)
        and math.isclose(norm(at_pi["poynting"]), 0.0, abs_tol=1e-15),  # type: ignore[arg-type]
        "trinity_invariant": math.isclose(float(at_trinity["invariant_1"]), -3.0 / 4.0, rel_tol=2e-15),
        "direct_field_average": math.isclose(
            float(direct_trinity["energy_density"]), float(at_trinity["energy_density"]), abs_tol=3e-15
        )
        and all(
            math.isclose(direct_trinity["poynting"][axis], at_trinity["poynting"][axis], abs_tol=3e-15)  # type: ignore[index]
            for axis in range(3)
        )
        and math.isclose(
            float(direct_trinity["invariant_1"]), float(at_trinity["invariant_1"]), abs_tol=3e-15
        ),
        "general_angle_direct_average": general_angle_direct_average,
        "fringe_average": math.isclose(mean_energy, 1.0, abs_tol=2e-15)
        and math.isclose(mean_flux[0], 1.0, abs_tol=2e-15)
        and math.isclose(mean_flux[1], 0.0, abs_tol=2e-15)
        and math.isclose(mean_flux[2], 0.0, abs_tol=2e-15),
    }


def main() -> int:
    print("N015 120-degree two-wave Maxwell baseline")
    print("crossing angle alpha=120 deg; relative phase delta is independent")
    print("at local Gamma=120 deg: u/(eps0*E0^2)=0.875, Sx/I0=0.5")
    checks = verify_baseline()
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print("INTERPRETATION: interference only; no new photon or neutrino is derived")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
