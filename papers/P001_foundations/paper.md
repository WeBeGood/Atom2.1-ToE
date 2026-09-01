# Atom 2.1 Foundations: A Standard Maxwell Reference Layer

**Authors:** [Author names to be supplied by the project owner before submission]
**Affiliations:** [Affiliations to be supplied; none inferred]
**Document status:** Working technical manuscript; not peer reviewed
**Version:** 0.2.0 (2026-09-01)

## Abstract

This manuscript records the standard classical-electromagnetic layer used as a recovery requirement by Atom 2.1. It states the vacuum Maxwell equations in SI units, derives the electric and magnetic wave equations, records plane-wave energy and momentum relations, and fixes geometric and polarization conventions. A differential-form representation is included as a coordinate-independent restatement. These established results constrain later Atom 2.1 hypotheses but do not support a particle, medium, knot, or phase-lock interpretation by themselves. No new experiment or empirical validation is reported.

## Keywords

Maxwell equations; electromagnetic waves; SI units; Poynting vector; differential forms; polarization; recovery limit

## 1. Introduction and Research Question

Atom 2.1 contains proposed extensions built from electromagnetic geometry. Before such proposals can be evaluated, the standard limit must be explicit and independently checkable.

**Research question:** What equations, conventions, conservation relations, and scope limits must any later Atom 2.1 model reproduce when it claims a classical source-free vacuum limit?

The answer in this manuscript is not a new theory. It is a compact reference layer assembled from nodes N000, N010, and N011.

## 2. Background

Maxwell’s equations provide the standard classical description of electric and magnetic fields. In a vacuum region with charge density ρ=0 and current density **J**=0, the equations are linear. Their plane-wave solutions, polarization structure, and conservation laws are standard textbook results [1–3].

**Standard result:** The equations and derivations in Sections 3–4 are established classical electromagnetism.

**Project boundary:** Atom 2.1 must recover these results where it claims ordinary vacuum electromagnetism. Agreement with selected identities is necessary but not sufficient to validate any project-specific ontology.

## 3. Methods and Reproducibility

### 3.1 Assumptions

- Flat Minkowski spacetime and one inertial Cartesian chart.
- SI units and right-handed spatial orientation.
- Fields are sufficiently differentiable for derivatives to commute.
- Vacuum is linear, homogeneous, isotropic, and source free in the analyzed region.
- Initial and boundary data satisfy the divergence constraints.
- Quantum, material, nonlinear, and curved-spacetime effects are excluded.

### 3.2 Vacuum field equations

The source-free Maxwell equations are

∇·**E**=0,  ∇·**B**=0,
∇×**E**=−∂**B**/∂t,  ∇×**B**=μ₀ε₀∂**E**/∂t.  **(1)**

Using ∇×(∇×**F**)=∇(∇·**F**)−∇²**F** gives

∇²**E**−(1/c²)∂²**E**/∂t²=0,
∇²**B**−(1/c²)∂²**B**/∂t²=0,  **(2)**

where c=1/√(μ₀ε₀). In the revised SI, c=299 792 458 m s⁻¹ exactly; μ₀ is experimentally adjusted and ε₀=1/(μ₀c²).

### 3.3 Plane waves and conservation observables

For phase exp[i(**k**·**r**−ωt)], a nonzero vacuum mode satisfies

ω=c|**k**|,  **k**·**E₀**=**k**·**B₀**=0,
**B₀**=(**k**×**E₀**)/ω.  **(3)**

Energy and momentum are described by

u=(ε₀E²+B²/μ₀)/2,  **S**=(**E**×**B**)/μ₀,  **g**=**S**/c².  **(4)**

Poynting’s theorem is

∂u/∂t+∇·**S**=−**J**·**E**.  **(5)**

### 3.4 Geometric and polarization formulation

With field-strength 2-form F, excitation 2-form ℋ, and current 3-form 𝒥, the unit-aware exterior equations are dF=0 and dℋ=𝒥. A metric-dependent constitutive relation connects ℋ and F. Locally, dF=0 implies F=dA on contractible patches; a global potential requires [F]=0 in H²_dR.

For propagation direction **k̂**, two independent transverse polarization modes remain. N011 fixes the helicity basis through i**k̂**×**e**σ=σ**e**σ and states the phase/viewing convention explicitly.

### 3.5 Reproducibility

The deterministic checks require only the repository’s documented Python environment:

```text
python nodes/N000_space_time_light_maxwell/code/sim.py
python scripts/validate_nodes.py
python scripts/validate_papers.py
python -m pytest -q
```

No external dataset is used.

## 4. Results

The analytical derivation produces the wave equations, dispersion relation, transverse constraints, Poynting balance, vacuum momentum density, and form/vector crosswalk summarized above.

**Table 1. Traceability of standard results to repository nodes.**

| Result | Source node | Deterministic status |
|---|---|---|
| Vacuum Maxwell equations and wave operator | N000 | Algebraic and numerical checks |
| Energy, flux, momentum, and stress | N000 | Dimensional and plane-wave checks |
| Unit-aware differential-form equations | N010 | Explicit 3+1 derivation |
| Polarization and helicity convention | N011 | Basis and sign checks |

No original experimental result is claimed. No figure is necessary for the baseline equations; later manuscripts may reuse node figures with numbered captions.

## 5. Discussion

The baseline makes later claims auditable. A proposed extension cannot be supported merely by reproducing c, transversality, or a familiar interference pattern. It must also identify its domain, source coupling, conservation laws, initial/boundary formulation, and a discriminating prediction.

The differential-form language introduces legitimate topology through local and global properties of F. It does not imply that a cohomology class is a particle. Likewise, polarization helicity is a standard mode property and does not by itself imply localization or matter.

## 6. Limitations and Scope

This paper is limited to classical electromagnetism in flat spacetime, with source-free vacuum emphasized. It does not cover quantum electrodynamics, photon statistics, matter response, nonlinear optics, gravity, neutrino physics, or any Atom 2.1 particle mechanism. Infinite plane waves are mathematical idealizations; physical beams require finite apertures and boundary data.

The references establish accepted theoretical background. Repository checks validate internal algebra and implementation consistency, not nature itself.

## 7. Conclusion

Equations (1)–(5), their unit conventions, and their scope form the standard Maxwell recovery layer for Atom 2.1. Later hypotheses must remain visibly separate, recover this layer in the appropriate limit, and supply falsifiable predictions beyond it.

## Data and Code Availability

No empirical data were generated or analyzed. Source text and deterministic checks are stored in nodes N000, N010, and N011 of this repository. Generated claims and outlines are reproducible through the repository scripts.

## Author Contributions

[Placeholder: contributions must be supplied by the actual authors before dissemination. No contribution roles are inferred.]

## Acknowledgments

[Placeholder: none declared in this repository version.]

## Declarations

- **Funding:** [Not declared; do not infer.]
- **Conflicts of interest:** [Not declared; authors must provide a statement.]
- **Ethics approval:** Not applicable to this theoretical manuscript; no human participants, animals, or personal data are involved.
- **Consent to participate/publication:** Not applicable in the present repository version.

## References

1. J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley (1999), ISBN 978-0-471-30932-1.
2. D. J. Griffiths, *Introduction to Electrodynamics*, 4th ed., Cambridge University Press (2017), ISBN 978-1-108-42041-9.
3. M. Born and E. Wolf, *Principles of Optics*, 7th ed., Cambridge University Press (1999), [doi:10.1017/CBO9781139644181](https://doi.org/10.1017/CBO9781139644181).

## Version and Provenance

Version 0.2.0, dated 2026-09-01. This readable manuscript was assembled from repository nodes N000, N010, and N011 after the Maxwell-baseline formalization in commit `d70f2d2`. Nodes remain the detailed source of truth. The manuscript is a working document and has not been peer reviewed.
