# N010 Notation + Conventions

## Spacetime

- M is an oriented smooth four-dimensional spacetime.
- The N000 cross-check uses coordinates (t,x,y,z) and spatial orientation vol₃=dx∧dy∧dz.
- d=d₃+dt∧∂t, where d₃ is the exterior derivative on a constant-t spatial slice.
- The flat metric has signature (−,+,+,+). It is needed for the Hodge star and vacuum constitutive law, not for dF=0 or dℋ=𝒥.

## Differential forms

- d: exterior derivative
- ∧: wedge product
- ⋆: Hodge star operator (metric-dependent)

## EM objects

- A: 1-form (potential)
- F: field-strength 2-form
- ℋ: excitation 2-form
- 𝒥: electric charge-current 3-form
- E and H: spatial 1-forms corresponding to electric and magnetic field intensity
- B and D: spatial 2-forms corresponding to magnetic and electric flux density
- j: spatial current-density 2-form

## Fixed 3+1 decomposition

- F = B + E∧dt
- ℋ = D − H∧dt
- 𝒥 = ρ vol₃ − dt∧j

These signs are part of the convention. Changing metric signature, orientation, phasor sign, or the placement of dt requires a corresponding translation.

## Potential statement

F=dA locally on contractible patches when dF=0. Global exactness requires [F]=0 in H²_dR(M); simple connectedness alone is not sufficient in general.
