# N000 simulation stub (Maxwell plane-wave sanity)
# Minimal dependencies; expand later with numpy/scipy/sympy as needed.

import math

# Constants (SI)
MU0 = 4.0e-7 * math.pi
EPS0 = 8.8541878128e-12
C = 1.0 / math.sqrt(MU0 * EPS0)


def info() -> None:
    print("N000 Maxwell baseline")
    print(f"mu0={MU0:.6e} H/m")
    print(f"eps0={EPS0:.6e} F/m")
    print(f"c={C:.6e} m/s")


if __name__ == "__main__":
    info()
