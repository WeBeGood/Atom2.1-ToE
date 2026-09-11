# N017 — Electron closure and seed-line scaling (open)

Craig Fink (WeBeGood), Atom 2.1 ontology; formalization by ChatGPT at the user's request, 2026-09-11.
Status: open, M1. The conditional equations below do not establish an electron solution.

## Place in the progression

N000 space/time/light → N011 polarization → N015 two-parent-wave resultant → N016 candidate Beltrami seed-line → **N017 stable electron closure** → N018 alpha → H-SPEC.

N015's vector calculation is the animation baseline. The animations use x along the seed-line, and sample both parents and their sum at the same position/time. Their local cancellation views do not establish a confined knot. The accepted A120 NewWave rule and the N015 Maxwell calculation retain their distinct scopes.

## What can be established before choosing a closure law

Let L_nu > 0 be a specified seed-line length, L_e the closed centerline's arclength, and kappa the Beltrami inverse length. If these are the only dimensional length inputs, dimensional consistency requires

    L_e = L_nu F(kappa L_nu, eta_1, eta_2, ...),

where every eta is dimensionless and F is unknown. If kappa and all other independent scales are absent, this reduces to L_e = C L_nu, with dimensionless C undetermined. This is a dimensional constraint, not a computed closure law.

A CMB-derived wavelength would introduce another argument L_nu/lambda_CMB. Its choice must specify whether a frequency peak, wavelength peak, mean photon energy, or a derived resonance is used; these are not interchangeable. Choosing T_CMB does not supply the missing equation for F.

## Trefoil candidate: topology leaves continuous freedom

The trefoil mentioned in the ontology can be represented as a candidate centerline, without asserting it is the physical electron:

    r(u) = ((R+a cos(3u)) cos(2u),
            (R+a cos(3u)) sin(2u), a sin(3u)),  0 <= u < 2pi,
    R > a > 0.

Its arclength is

    L_e = integral_0^(2pi) sqrt(4(R+a cos(3u))^2 + 9a^2) du
        = a integral_0^(2pi) sqrt(4(R/a+cos(3u))^2 + 9) du.

Thus even this fixed knot type leaves both the overall scale a and the shape ratio R/a free. Knot labels or three crossings alone do not pick either number. A finite field-tube radius, its energy density and boundary conditions remain additional inputs. No trefoil simulation is added to the proven-field animations.

## Conditional phase closure

For a scalar mode with arclength phase gradient k_parallel, ordinary single-valued phase closure would require

    integral_loop k_parallel(s) ds = 2pi n,  n integer.

This is conditional on the scalar periodic boundary condition. Vector-frame rotation, polarization transport, gauge holonomy or other boundary rules would modify it and must be derived explicitly. k_parallel is not automatically N016's kappa. Setting k_parallel=kappa constant would imply kappa L_e=2pi n only after that extra identification. It still leaves n, the field normalization and stability unspecified.

## Required physical closure

Supply a field action/energy functional with the proposed medium coupling, a finite-energy solution, conserved quantities and boundary conditions. Show a stationary solution under the allowed variations and analyze its perturbations; a closed drawing or phase periodicity alone does not demonstrate stability. A constrained energy minimum is one possible sufficient route, not an assumed universal criterion for all driven structures.

Open alternatives from the pasted discussion are preserved: trefoil closure, nested 120-degree locks, or Beltrami modes constrained by a specified CMB resonance. They may be related proposals, not mutually exclusive established laws. None has been silently selected.

## Export and falsification

Export only the dimensional form and the unresolved closure requirements. A proposed F fails the predictive requirement if it remains arbitrary or is selected to fit alpha. A particular electron solution fails if it cannot satisfy its stated field equations/boundaries or is unstable on the claimed lifetime. These tests do not falsify every possible future closure law.
