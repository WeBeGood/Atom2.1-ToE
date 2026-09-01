"""Deterministic SI checks for the N000 Maxwell vacuum baseline.

This is an algebraic audit, not an empirical validation or a field solver.
It intentionally uses only the Python standard library.
"""

import math
from typing import Dict, Tuple

Vector = Tuple[float, float, float]

# SI constants. c is exact; mu0 is the 2022 CODATA central value.
C = 299_792_458.0
MU0 = 1.256_637_061_27e-6
EPS0 = 1.0 / (MU0 * C * C)
Z0 = MU0 * C


def dot(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


def cross(a: Vector, b: Vector) -> Vector:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def scale(factor: float, vector: Vector) -> Vector:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def norm(vector: Vector) -> float:
    return math.sqrt(dot(vector, vector))


def verify_baseline() -> Dict[str, bool]:
    """Return deterministic checks of the documented plane-wave identities."""
    wavelength = 0.5  # m
    k_magnitude = 2.0 * math.pi / wavelength
    k: Vector = (0.0, 0.0, k_magnitude)
    omega = C * k_magnitude
    electric: Vector = (3.0, 4.0, 0.0)  # V/m
    magnetic = scale(1.0 / omega, cross(k, electric))

    electric_energy = 0.5 * EPS0 * norm(electric) ** 2
    magnetic_energy = 0.5 * norm(magnetic) ** 2 / MU0
    poynting = scale(1.0 / MU0, cross(electric, magnetic))
    total_energy = electric_energy + magnetic_energy
    momentum = scale(1.0 / (C * C), poynting)

    return {
        "si_identity": math.isclose(MU0 * EPS0 * C * C, 1.0, rel_tol=0.0, abs_tol=2e-15),
        "transverse_e": math.isclose(dot(k, electric), 0.0, abs_tol=1e-15),
        "transverse_b": math.isclose(dot(k, magnetic), 0.0, abs_tol=1e-15),
        "mutual_orthogonality": math.isclose(dot(electric, magnetic), 0.0, abs_tol=1e-15),
        "dispersion": math.isclose(omega, C * norm(k), rel_tol=2e-15),
        "amplitude": math.isclose(norm(magnetic), norm(electric) / C, rel_tol=2e-15),
        "equal_energy_parts": math.isclose(electric_energy, magnetic_energy, rel_tol=2e-15),
        "energy_flux": math.isclose(norm(poynting), total_energy * C, rel_tol=2e-15),
        "forward_flux": poynting[2] > 0.0 and math.isclose(poynting[0], 0.0, abs_tol=1e-15)
        and math.isclose(poynting[1], 0.0, abs_tol=1e-15),
        "momentum_density": math.isclose(norm(momentum), total_energy / C, rel_tol=2e-15),
    }


def info() -> int:
    print("N000 Maxwell baseline")
    print(f"c={C:.0f} m/s (exact SI)")
    print(f"mu0={MU0:.12e} H/m (2022 CODATA central value)")
    print(f"eps0={EPS0:.12e} F/m (derived from 1/(mu0*c^2))")
    print(f"Z0={Z0:.12f} ohm")

    checks = verify_baseline()
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(info())
