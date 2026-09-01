# N000 Units + Dimensional Checks (SI)

## Core quantities

| Quantity | SI unit | Equivalent form |
|---|---|---|
| Electric field **E** | V m⁻¹ | N C⁻¹ |
| Magnetic flux density **B** | T | N A⁻¹ m⁻¹ |
| Charge density ρ | C m⁻³ | A s m⁻³ |
| Current density **J** | A m⁻² | C s⁻¹ m⁻² |
| Permittivity ε₀ | F m⁻¹ | C V⁻¹ m⁻¹ |
| Permeability μ₀ | H m⁻¹ | N A⁻² |
| Speed c | m s⁻¹ | exact SI value |
| Impedance Z₀ | Ω | μ₀c |

## Maxwell-equation checks

- ∇·**E** and ρ/ε₀ both have units V m⁻².
- ∇×**E** and −∂t**B** both have units V m⁻² because T s⁻¹ = V m⁻².
- ∇×**B**, μ₀**J**, and μ₀ε₀∂t**E** all have units T m⁻¹.

## Wave speed and impedance

[μ₀ε₀] = s² m⁻², so 1/√(μ₀ε₀) has units m s⁻¹.

For a plane wave, |**E**|/|**B**|=c has units (V m⁻¹)/T = m s⁻¹, and |**E**|/|**H**|=Z₀ has units Ω, where **H**=**B**/μ₀ in vacuum.

## Energy + momentum flow

- ε₀|**E**|² and |**B**|²/μ₀ both have units J m⁻³.
- **S**=(**E**×**B**)/μ₀ has units W m⁻².
- **J**·**E** has units W m⁻³, matching ∂tu and ∇·**S**.
- **g**=**S**/c² has units kg m⁻² s⁻¹ (momentum per volume).
- Each Maxwell-stress component has units J m⁻³ = Pa.

## Numerical constants used by the deterministic check

- c = 299 792 458 m s⁻¹ exactly.
- μ₀ = 1.256 637 061 27×10⁻⁶ H m⁻¹ (2022 CODATA central value).
- ε₀ is computed as 1/(μ₀c²); the published rounded CODATA value is 8.854 187 8188×10⁻¹² F m⁻¹.

The last digits of experimentally adjusted constants may change in future CODATA releases. Such an update is metadata maintenance, not a change to Maxwell’s equations.
