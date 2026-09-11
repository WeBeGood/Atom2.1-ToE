# N018 — Fine-structure constant from Atom 2.1 (open)

Craig Fink (WeBeGood), Atom 2.1 ontology; formalization by ChatGPT at the user's request, 2026-09-11.
Status: open, M1. **No numerical Atom 2.1 prediction of alpha is obtained here.**

## Derivation interface

N017 must provide a stable normalized electron field, not merely a centerline. A proposed geometric ratio then needs an equation connecting it to electromagnetic coupling and an action scale. Let q be the predicted asymptotic electric charge and J_star the proposed fundamental action normalization. With vacuum impedance Z0 = 1/(epsilon0 c),

    g = q^2 Z0 / J_star,
    alpha_candidate = g / (4pi).

The second equation is an identification to justify by deriving the effective electromagnetic interaction; dimensional agreement alone does not prove it. Under q=e and J_star=hbar it reproduces the usual definition. In SI, q^2 Z0 has units C^2 ohm = J s, so g is dimensionless. This repackages the task: compute q and J_star (or their ratio) from independent Atom 2.1 dynamics. Inserting measured e, Z0 and hbar evaluates an empirical identity and is not the requested geometric derivation.

## Correct unit conventions

    SI:                 alpha = e_SI^2/(4pi epsilon0 hbar c)
    Gaussian:           alpha = e_G^2/(hbar c)
    Heaviside–Lorentz:  alpha = e_HL^2/(4pi hbar c)
    HL, hbar=c=1:       alpha = e_HL^2/(4pi)

The pasted conversation incorrectly named the Gaussian expression as Heaviside–Lorentz. Charge normalization changes between these conventions. Setting only c=1 does not also set hbar=1. Restore both factors when converting any Atom 2.1 action or energy comparison.

## A concrete missing charge equation

For smooth source-free Maxwell fields over a volume V with closed boundary,

    q_V = epsilon0 integral_boundary(V) E dot dA
        = epsilon0 integral_V div(E) dV = 0.

This includes the two parent fields used in the animations. Longitudinal E on the sampled x line is not, by itself, net electric charge. To obtain the electron's nonzero asymptotic q, specify sources, singularities with their boundary terms, nontrivial domain boundaries, or additional effective dynamics. This is a scoped obstruction for the smooth source-free baseline, not a claim that every Atom 2.1 extension is impossible.

Likewise, N016's curl A = kappa A is homogeneous: multiplying A by any constant preserves the equation while changing quadratic energy/helicity. A dimensionless ratio can cancel that amplitude, but the ansatz does not establish which such ratio is electromagnetic coupling. A selected eigenvalue or trefoil label alone does not fix charge/action normalization.

## Comparison protocol, after obtaining a prediction

The external low-energy reference is the 2022 CODATA adjustment:

    alpha_ref^(-1) = 137.035999177, standard uncertainty 0.000000021.
    Delta = alpha_candidate^(-1) - alpha_ref^(-1)
    residual_ppb = 1e9 Delta / alpha_ref^(-1).

Source: [NIST complete CODATA 2022 table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt), checked 2026-09-11. The reference is a comparison input only. Report theoretical uncertainty and the electromagnetic energy scale/convention. If independent Gaussian theoretical and reference uncertainties are appropriate, compare Delta to sqrt(u_theory^2+u_ref^2); do not treat correlated inputs as independent. Significant figures or proximity to 137 do not establish a derivation.

Every correction must follow from an identified term in the interaction or a controlled approximation; corrections chosen from the residual are a fit. The hydrogen relation a0 = reduced_lambda_C/alpha is an identity using alpha and supplies no independent prediction. H-SPEC remains downstream.

## Acceptance gates

1. N017 supplies field closure, finite energy and stability under explicit dynamics.
2. The solution predicts charge normalization and an action scale, or an equivalent effective coupling ratio.
3. The map from that ratio to alpha follows from the derived interaction.
4. No fitted alpha, Bohr radius or equivalent alpha-containing quantity enters upstream unnoticed.
5. A numerical prediction and independently justified corrections include an error budget and residual.
6. Hydrogen/spectral consequences supply additional tests beyond the single fitted quantity.

Until these gates are met, prediction and residual remain **not available**, rather than zero or a placeholder 137. A freely adjustable closure/coupling is underdetermined. A specific parameter-free candidate can be rejected by inconsistent units, violated conservation/boundary conditions or disagreement outside a justified error budget.
