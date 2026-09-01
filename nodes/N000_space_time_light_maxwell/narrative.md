# N000 — Classical electromagnetism in vacuum (Maxwell baseline)

## Purpose
Establish an auditable standard-physics baseline that every later Atom 2.1 construction must recover in its claimed classical-vacuum limit. Nothing in this node proves an Atom 2.1 particle, medium, knot, or phase-lock hypothesis.

## Classification and assumptions

**Classification: standard classical electromagnetism.** Work in an inertial Cartesian chart of flat spacetime, use SI units and a right-handed spatial orientation, and take the fields to be smooth enough that the indicated derivatives commute. In the vacuum propagation region, charge density and current density vanish: ρ=0 and **J**=0.

The source equations, retained to make the vacuum restriction explicit, are

- ∇·**E** = ρ/ε₀,
- ∇·**B** = 0,
- ∇×**E** = −∂**B**/∂t,
- ∇×**B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t.

Setting ρ and **J** to zero gives the source-free system used below. The divergence equations are constraints on admissible initial/boundary data; the curl equations propagate those constraints when the sources obey charge conservation.

## SI constants

The speed of light is the exact SI defining constant

c = 299 792 458 m s⁻¹.

Since the 2019 SI revision, μ₀ is not defined to be exactly 4π×10⁻⁷ H m⁻¹. Current recommended values are experimentally adjusted, while the relation

μ₀ε₀ = 1/c²

remains exact. Numerical software in this node therefore stores exact c, a stated CODATA μ₀ value, and derives ε₀ from the identity.

## Wave-equation derivation

Taking the curl of Faraday’s law, substituting Ampère–Maxwell, and using

∇×(∇×**E**) = ∇(∇·**E**) − ∇²**E**

with ∇·**E**=0 gives

∇²**E** − (1/c²)∂²**E**/∂t² = 0.

Taking the curl of Ampère–Maxwell and using ∇·**B**=0 gives the corresponding result

∇²**B** − (1/c²)∂²**B**/∂t² = 0.

These are local field equations. A physical solution additionally needs initial data and boundary or radiation conditions appropriate to its domain.

## Monochromatic plane-wave audit

For phasors **E**=Re{**E₀** exp[i(**k**·**x**−ωt)]} and similarly for **B**, nonzero vacuum solutions obey

- **k**·**E₀** = **k**·**B₀** = 0,
- ω² = c²|**k**|²,
- **B₀** = (**k**×**E₀**)/ω,
- |**B₀**| = |**E₀**|/c and **E₀**×**B₀** points along **k**.

An infinite monochromatic plane wave is an idealized, non-localized solution with infinite total energy. It is useful as a local mode and limiting approximation, not as a literal finite-energy laboratory field.

## Energy and momentum

Maxwell’s equations imply Poynting’s theorem

∂u/∂t + ∇·**S** = −**J**·**E**,

where

u = (ε₀|**E**|² + |**B**|²/μ₀)/2,

**S** = (**E**×**B**)/μ₀.

In vacuum, electromagnetic momentum density is

**g** = **S**/c² = ε₀(**E**×**B**).

The Maxwell stress tensor is

Tᵢⱼ = ε₀(EᵢEⱼ − δᵢⱼ|**E**|²/2) + (BᵢBⱼ − δᵢⱼ|**B**|²/2)/μ₀.

Together, **g** and T describe field momentum and momentum transfer. For a vacuum plane wave the electric and magnetic contributions to u are equal and |**S**|=uc.

## Validity boundary

- Sources require the full ρ and **J** equations and the Lorentz force law.
- Matter requires constitutive relations and may introduce dispersion, loss, anisotropy, or nonlinearity.
- Curved spacetime requires a covariant formulation; N010 supplies the geometry-ready language, not a gravity theory.
- Quantum emission, absorption, vacuum polarization, and photon statistics are outside classical Maxwell theory.
- Agreement of a later model with a few plane-wave identities is necessary but not sufficient to recover electromagnetism; it must reproduce the equations, conservation laws, source coupling, and relevant boundary-value predictions.

## Empirical anchors

The BIPM SI definition fixes c exactly, while the NIST/CODATA adjustment reports mutually consistent electromagnetic constants. Precision null tests of Coulomb-law deviations, such as Williams, Faller, and Hill (1971), are representative direct probes of departures from the Maxwell baseline. These references anchor conventions and empirical scope; the deterministic checks in this repository test internal consistency only and are not themselves experimental validation.

## Atom 2.1 handoff
Any Atom 2.1 extension must identify its domain, recover this baseline in the appropriate limit, and state a discriminating, falsifiable departure. N010 and N011 may re-express standard electromagnetism geometrically, but no topology-to-particle inference is licensed by N000.
