# N010 Math Track — Maxwell in Differential Forms (3+1 split)

## Goal
Show that the unit-aware form equations reproduce N000’s vector Maxwell equations under fixed signs and orientation.

## Decomposition

On a right-handed spatial slice let E,H be spatial 1-forms and B,D,j spatial 2-forms. With d=d₃+dt∧∂t, define

F = B + E∧dt,

ℋ = D − H∧dt,

𝒥 = ρ vol₃ − dt∧j.

Maxwell’s equations are

dF=0,  dℋ=𝒥.

## Homogeneous pair

Direct expansion gives

dF = d₃B + dt∧(∂tB+d₃E).

The spatial and dt-containing parts vanish independently:

d₃B=0,  ∂tB+d₃E=0.

Under the standard spatial vector/form identification these are

∇·**B**=0,  ∇×**E**=−∂t**B**.

## Inhomogeneous pair

Similarly,

dℋ = d₃D + dt∧(∂tD−d₃H).

Equating this with 𝒥 yields

d₃D=ρ vol₃,  d₃H=j+∂tD,

or in vector notation

∇·**D**=ρ,  ∇×**H**=**J**+∂t**D**.

For vacuum in the N000 inertial frame,

**D**=ε₀**E**,  **H**=**B**/μ₀,

so the inhomogeneous equations become

∇·**E**=ρ/ε₀,

∇×**B**=μ₀**J**+μ₀ε₀∂t**E**.

This completes the explicit 3+1 recovery check.

## Metric and topology

The exterior equations are independent of a metric. The vacuum constitutive relation can be written with a Hodge star only after fixing metric signature, orientation, time-coordinate normalization, and the physical normalization of F and ℋ.

If dF=0, the Poincaré lemma gives F=dA on a contractible patch. Globally, a potential exists iff [F]=0 in H²_dR(M). This cohomological fact is standard geometry; no particle interpretation follows without additional, independently testable assumptions.
