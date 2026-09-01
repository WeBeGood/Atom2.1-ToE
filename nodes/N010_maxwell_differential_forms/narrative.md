# N010 — Maxwell equations in differential forms (standard baseline)

## Purpose
Rewrite standard classical electromagnetism in a coordinate-independent language while preserving the SI source normalization and an explicit map back to N000. This mathematical reformulation does not make topology into matter and does not validate an Atom 2.1 particle model.

## Unit-aware core equations

Use the field-strength 2-form F, excitation 2-form ℋ, and electric charge-current 3-form 𝒥:

- dF = 0,
- dℋ = 𝒥.

These two equations are metric-independent. The metric and material response enter through a constitutive relation between ℋ and F. In vacuum that relation is equivalent, in the N000 inertial frame, to **D**=ε₀**E** and **H**=**B**/μ₀. A shorthand such as d⋆F=𝒥 is incomplete in SI unless the normalization of F, the Hodge star, and 𝒥 is stated.

## 3+1 audit

With the conventions in `math/forms_derivation.md`, write

F = B + E∧dt,  ℋ = D − H∧dt,  𝒥 = ρ vol₃ − dt∧j.

Then dF=0 gives Gauss’s magnetic law and Faraday’s law, while dℋ=𝒥 gives Gauss’s electric law and Ampère–Maxwell. Applying the vacuum constitutive relation reproduces N000.

## Local potentials and topology

Because d²=0, F=dA automatically implies dF=0. Conversely, the Poincaré lemma guarantees F=dA on each contractible patch. A single global A exists exactly when the de Rham class [F]∈H²_dR(M) vanishes. Simple connectedness by itself is not the general condition for a closed 2-form to be exact.

This is a precise standard-physics topology statement. It supplies vocabulary for later hypotheses but does not imply that an electromagnetic cohomology class is a particle, knot, or quantized Atom 2.1 state.

## Atom 2.1 handoff
Any project-specific use of topology must add a declared hypothesis, dynamics, boundary conditions, observables, and a recovery map to N000. N010 contributes only the standard geometric language and its verification criteria.
