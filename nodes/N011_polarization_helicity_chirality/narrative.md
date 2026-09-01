# N011 — Polarization, helicity, chirality baseline (plane waves)

## Purpose
Fix a reproducible standard-physics convention for polarization and helicity before any later project-specific use of chirality language.

## Plane-wave recap (from N000)
For a plane wave propagating along **k̂**:

- **E** ⟂ **k̂**,
- **B** ⟂ **k̂**,
- **E** ⟂ **B**.

## Two degrees of freedom
For nonzero **k**, the constraint **k**·**E₀**=0 leaves a two-dimensional complex transverse space. Linear and circular polarizations are alternative bases of the same space, not extra modes.

For propagation along +z and phase exp[i(kz−ωt)], define

**e**σ = (**x̂** + iσ **ŷ**)/√2,  σ∈{+1,−1}.

This basis is fixed by the eigenvalue equation

i **k̂**×**e**σ = σ **e**σ.

## Circular polarization and handedness
At fixed z=0, the real field associated with **e**+ is proportional to

**x̂** cos(ωt) + **ŷ** sin(ωt),

so it rotates from +x toward +y as time increases. This appears counterclockwise to an observer on the −z side looking along +z, and clockwise to an observer on the +z side looking back toward the source. The σ=− mode rotates oppositely.

Different optics and particle-physics sources attach “left” and “right” to different viewing directions and Fourier signs. This node therefore treats σ and the eigenvalue equation as normative; verbal labels are secondary and must include a viewing convention.

## Scope boundary

Polarization describes field-mode geometry. Helicity labels a rotation-generator eigenstate for a plane wave. Neither fact alone produces localization, knot stability, charge, mass, or a particle spectrum. Any Atom 2.1 identification of these structures must be declared and tested as an additional hypothesis.

## Atom 2.1 handoff
Later nodes may build on the fixed σ convention. They must keep standard polarization results separate from proposed topology-to-particle dynamics.
