# N015 — Two coherent vacuum plane waves at 120 degrees

## Purpose

Establish the vector-algebra baseline for two equal-frequency, equal-amplitude vacuum plane waves whose wavevectors meet at the proposed **Trinity angle** of 120°. The crossing angle and the controllable relative phase are treated as independent quantities.

This node contains two sharply separated layers:

1. **Standard result:** linear Maxwell superposition and its measurable interference observables.
2. **Atom 2.1 hypothesis:** the proposed name “neutrino seed” for a selected field region. That name is not a Maxwell result and no neutrino is derived here.

## Geometry

Let both wavevectors have magnitude k=ω/c and lie in the x-y plane, symmetric about +x:

**k₁** = k(½ **x̂** + √3/2 **ŷ**),

**k₂** = k(½ **x̂** − √3/2 **ŷ**).

Then **k₁**·**k₂**=−k²/2, so their crossing angle is 120°, while

**k₁**+**k₂**=k **x̂**,  **k₁**−**k₂**=√3 k **ŷ**.

These are geometric vector sums. The superposed field still contains both phase factors and is not a new plane wave with wavevector **k₁**+**k₂**.

## Fields and controllable phase

Choose the common polarization **ê**=**ẑ**, which is transverse to both wavevectors. With phase offset δ,

**E₁**=E₀ **ẑ** cos(**k₁**·**r**−ωt),

**E₂**=E₀ **ẑ** cos(**k₂**·**r**−ωt+δ),

**Bᵢ**=(**k̂ᵢ**×**Eᵢ**)/c.

Linearity gives **E**=**E₁**+**E₂** and **B**=**B₁**+**B₂**. The local relative phase is

Γ(**r**)=δ+(**k₂**−**k₁**)·**r**=δ−√3ky.

Thus δ translates the interference pattern; it does not change the fixed 120° crossing geometry. The transverse fringe spacing is λ/√3.

## Standard Maxwell observables

For peak phasor amplitude E₀ and single-wave intensity I₀=ε₀cE₀²/2, the cycle averages are

⟨u⟩ = ε₀E₀²[1+¼ cos Γ],

⟨**S**⟩ = I₀ **x̂**[1+cos Γ],

⟨**g**⟩ = ⟨**S**⟩/c².

The cycle-averaged field invariants for this polarization are

⟨E²−c²B²⟩ = (3/2)E₀² cos Γ,  ⟨**E**·**B**⟩=0.

At a point where Γ=120°, ⟨u⟩=(7/8)ε₀E₀² and ⟨**S**⟩=(I₀/2)**x̂**. Neither is stationary there: their phase derivatives are proportional to −sin Γ. The extrema occur at Γ=0 and Γ=π.

Averaging across one full fringe sets ⟨cos Γ⟩=0. The resulting energy and momentum flow equal the sums of the two input contributions. Interference redistributes local density and flux; it does not create net energy.

## Atom 2.1 interpretation boundary

Atom 2.1 may propose to call a selected interference region a “neutrino seed.” In the present calculation that phrase is only a project-specific interpretation. Linear vacuum Maxwell theory provides:

- no new independent photon or field mode,
- no localized finite-energy object,
- no self-binding or stability mechanism,
- no neutrino quantum numbers, mass, charge, or weak interaction,
- and no distinguished phase extremum at 120°.

Any future seed model must add explicit dynamics or boundary conditions, define a gauge-invariant and Lorentz-consistent localization/stability criterion, conserve energy-momentum, and predict an observation that differs from ordinary two-wave interference.

## Scope and limitations

This node assumes infinite monochromatic coherent plane waves in linear vacuum electromagnetism with one common linear polarization. It does not model wave packets, finite apertures, matter, nonlinear optics, gravity, a CMB photon field, quantum electrodynamics, or charge-only/magnetic-only propagation. “Photon plane wave” is used informally for a classical mode; photon-number claims require a separate quantum treatment.

## Paper handoff

The full human-readable derivation, journal-style scope statements, references, table, and reproducibility notes are in `papers/P002_trinity_vector_baseline/paper.md`.
