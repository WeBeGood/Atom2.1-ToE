# N018 — Fine structure from charge, energy and action

Owner/co-creator: WeBeGood. Status: OPEN numerical prediction; completed conditional
reduction and restricted-baseline obstruction. No fitted 137 is a derived result.

## 1. Scope and units
The physical ontology proposes NewWave seed-lines in a BBRV/CMB medium and rest
mass from closure/twist. The ledger records accepted project premises; it does
not convert those premises into tested field dynamics. N017 supplies a closure
family, not a charged stable solution. We use the external electromagnetic
charge interface discussed in this session, with SI factors restored.

    alpha_fs = e_SI^2/(4pi eps0 hbar c)                  (SI)
             = e_G^2/(hbar c)                           (Gaussian)
             = e_HL^2/(4pi)                             (HL, hbar=c=1). (18.1)

The charge symbols have different unit conventions. The prior chat incorrectly
called the Gaussian expression Heaviside–Lorentz. Setting c=1 alone does not
set hbar=1 or remove the rationalization factor 4pi.
The target is the low-energy fine-structure constant, not a value at an arbitrary
renormalization scale. Comparison target verified against the NIST CODATA 2022 table on 2026-09-11:
alpha_fs^-1=137.035999177(21). The uncertainty is 0.000000021.
Reference: https://physics.nist.gov/cuu/Constants/Table/allascii.txt (CODATA tables).
The target is an external benchmark only, never an input to the field equations.

## 2. Source-free baseline obstruction
For smooth fields in a volume V satisfying N000/N015's source-free constraint,

    div E_i=0 => div(sum E_i)=0,
    Q(V)=eps0 integral_boundary(V) E dot dA=0.           (18.2)

This holds for any crossing angle, including 120 degrees, and independently of
local longitudinal electric components. An electric-dominated interference
region is not the same observable as a nonzero enclosed electric charge.
A localized charged object could in principle coexist with compensating charge
elsewhere; that still requires a locally nonzero effective source absent from
this smooth source-free baseline. The obstruction does not forbid all medium,
boundary, singular, or topologically nontrivial extensions. Each would require
explicit field equations and a careful definition of charge and of the enclosing
surface. In a material description, distinguish div D=rho_free from total charge
in div E=rho_total/eps0; do not import either relation without that interface.

N016's constant-kappa curl ansatz is homogeneous in A: if A solves it, so does sA.
Taking its divergence with kappa != 0 gives div A=0. It does not by itself fix the
scalar potential, produce electric charge, or select a quantum of action.

## 3. General conditional reduction
Assume a finite-energy candidate with isolated Coulomb far field and define
xi=r/L, E=E_* f(xi), B=(E_*/c) g(xi). Use a common instant, or consistent cycle
averages and a time-independent monopole, throughout the energy and flux.
Let

    C_Q = (1/4pi) lim_s->infinity integral_|xi|=s f dot dA_xi,
    C_U = (1/2) integral_R^3 (|f|^2+|g|^2) d^3xi > 0.   (18.3)

L is a declared characteristic size, not automatically arclength, Compton
length or torus radius. If far field is isotropic, E_r=E_* C_Q L^2/r^2+o(r^-2).
Gauss's law and Maxwell field energy give

    Q = 4pi eps0 E_* L^2 C_Q,
    U_EM = eps0 E_*^2 L^3 C_U,
    eta_EM = U_EM L/(hbar c).                           (18.4)

Eliminating E_* yields the central result, conditional on |Q|=e:

    alpha_fs = 4pi eps0 E_*^2 L^4 C_Q^2/(hbar c)
             = 4pi eta_EM C_Q^2/C_U.                   (18.5)

The dimensions cancel because eps0 E_*^2 L^4 is J m and hbar c is J m.
This is a derived identity for the stated interface, not a numerical prediction.
C_U must be finite; infinite plane waves cannot be substituted into (18.5).
If additional BBRV/core energy contributes to the particle, define
f_EM=U_EM/U_total (when both are well-defined positive energies). Then

    alpha_fs = 4pi f_EM eta_total C_Q^2/C_U,
    eta_total = U_total L/(hbar c).                      (18.6)

Replacing U_EM with the total rest energy without this accounting is invalid.
Background subtraction and medium energy require a specified stress-energy law.

If a future quantization law independently establishes U_total/omega=hbar and
chi=omega L/c, then eta_total=chi. Neither chi, f_EM nor C_Q^2/C_U is selected
by the current seed/closure equations. Calling U/omega an action does not prove
it is the canonical action variable of a nonlinear knot.

## 4. Why the missing normalization matters
With unchanged dimensionless shape and L, a homogeneous field amplitude change
E_* -> s E_* gives Q -> sQ, U_EM -> s^2 U_EM and alpha_fs -> s^2 alpha_fs.
The accepted angle and topology remain unchanged. Thus these constraints alone
cannot choose an elementary charge coupling. On a strictly source-free smooth
branch C_Q=0, so it is not an electron candidate at all.

L conventions cannot create a prediction: under L'=bL with E_* fixed for the
same physical field, C_Q'=C_Q/b^2, C_U'=C_U/b^3 and eta_EM'=b eta_EM. Equation
(18.5) is invariant. Arbitrarily renaming a length as L_e cannot tune alpha.
Likewise f->a f, g->a g, E_*->E_*/a leaves the physical fields and (18.5) unchanged.

## 5. Analytic diagnostic with an explicit source (NOT an electron)
Choose g=0 and f(xi)=xi/(1+|xi|^2)^(3/2). This is a smooth electrostatic test
profile with

    C_Q=1,
    rho_charge(r)=3 eps0 E_*/L (1+r^2/L^2)^(-5/2),
    C_U=2pi integral_0^infinity s^4/(1+s^2)^3 ds=3pi^2/8,
    alpha_fs=32 eta_EM/(3pi).                           (18.7)

Substitution s=tan(t) turns the energy integral into integral_0^(pi/2) sin^4(t) dt.
The nonzero source is supplied, not generated from two waves. This example
checks the far-field/energy calculation and shows that arbitrarily many
couplings are compatible with a shape unless action/amplitude is selected.
It is not a trefoil, stable matter solution, simulation of two photons becoming
one particle, or prediction of alpha. Matching eta to the benchmark is an
inverse calibration and is explicitly rejected as a derivation.

## 6. Corrections and falsifiable completion criteria
For a nonzero baseline and fixed length convention, small perturbations obey

    delta alpha/alpha = delta eta_EM/eta_EM
                       +2 delta C_Q/C_Q - delta C_U/C_U + O(delta^2). (18.8)

If using total energy, also include delta f_EM/f_EM. This is sensitivity
bookkeeping, not calculated radiative or geometric correction coefficients.
A corrected numerical prediction needs independently derived coefficients,
controlled truncation/numerical errors, and a specified low-energy observable.

To close ALPHA, provide (1) NewWave/BBRV dynamics and boundary conditions,
(2) a nonzero elementary charge solution, with conservation/source accounting,
(3) finite field and medium energy, (4) stable closure and independently selected
shape/phase mode, (5) a derived action normalization and length convention,
(6) a parameter-free evaluated coupling with uncertainty and correction budget.
If these equations leave a continuous coupling or require experimental alpha,
e, a0 or electron radius to select the solution, the numerical derivation is
still open. The identities a0=lambda_bar_C/alpha and r_e=alpha lambda_bar_C use
alpha; they do not derive it. A number near 137 assembled from pi and knot
integers is not a substitute for these steps.

Run `python nodes/N018_alpha_charge_action/code/sim.py` to produce deterministic
JSON. `--candidate-inverse VALUE` reports residual and benchmark-uncertainty
units for an externally supplied candidate, labelled supplied_not_derived.
No candidate means null prediction and null residual, rather than false success.
