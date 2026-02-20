# N015 Math Track — Seed Functional S(E,B) (placeholder)

## Goal
Define a concrete, **gauge-invariant** functional S(E,B) that measures the presence of a localized turning-region / boundary feature.

## Constraints
S(E,B) must be:
1) gauge-invariant (depends only on E,B or F,⋆F)
2) local or quasi-local (detects localized structure)
3) sensitive to phase-locking between two inputs

## Candidate families (to be refined)
### (A) Invariant scalars
Use Lorentz invariants:
- I1 = E^2 - c^2 B^2
- I2 = E·B

Potential seed-likeness measure:
- S = ∫_V (w1 |I1| + w2 |I2|) dV
with normalization choices stated.

### (B) Helicity / chirality measures
For suitable fields, define a helicity-like quantity (careful: gauge subtleties if using A):
- H ~ ∫ A·B dV (requires gauge handling)
Prefer using gauge-invariant proxies or explicitly fixed gauges.

### (C) Poynting flux turning-region indicator
Use energy flux S_vec = (1/μ0) E×B.
A turning-region could be associated with rapid spatial variation or local circulation of S_vec.

## Trinity scan
For a toy two-wave model, parameterize the second input with relative phase theta and scan:
- theta ∈ [0, 2π)
Compute S(theta) and look for an extremum near theta ≈ 2π/3.

If no plausible S yields an extremum near 120° under physically plausible inputs, the hypothesis fails as stated.
