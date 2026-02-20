# N000 Units + Dimensional Checks (SI)

## Core quantities
- Electric field E: V/m = N/C
- Magnetic field B: tesla (T) = N/(A·m)
- Permittivity ε0: F/m = C/(V·m)
- Permeability μ0: H/m = N/A^2
- Speed of light c: m/s

## Key relations
### Wave speed
From Maxwell (vacuum):

c = 1 / sqrt(μ0 ε0)

Dimensional check:
- [μ0] = N/A^2
- [ε0] = C/(V·m)
- [μ0 ε0] has units of s^2/m^2
- therefore 1/sqrt(μ0 ε0) has units m/s

## Energy + momentum flow
- Poynting vector S = (1/μ0) E×B has units W/m^2
- Energy density u = (ε0/2)|E|^2 + (1/(2μ0))|B|^2 has units J/m^3
