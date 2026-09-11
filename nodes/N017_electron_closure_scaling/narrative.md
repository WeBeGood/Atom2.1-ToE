# N017 — Electron closure: geometry and scale selection

Owner/co-creator: WeBeGood. Status: open project hypothesis; conditional mathematics checked.

## Inherited state
Continue N016's candidate Beltrami seed-line and the accepted Mach-1 convention.
Do not promote a curve into a stable electron. Use x as the distinguished seed-line
axis; the torus below is oriented around x. Use theta for the crossing angle;
alpha_fs denotes the fine-structure constant, avoiding N015's angle symbol alpha.

## Explicit candidate geometry
For R > a > 0 and 0 <= t < 2 pi, choose the T(2,3) torus trefoil:

    x(t) = a sin(3t)
    y(t) = (R + a cos(3t)) cos(2t)
    z(t) = (R + a cos(3t)) sin(2t).                       (17.1)

This is a geometric ansatz, not a derived field configuration. Here a is the
minor radius of the supporting torus, NOT a field-core thickness. A finite
field tube would need another scale and nonintersection constraints.
With rho=a/R in (0,1), the exact arclength is

    L_e = R F(rho),
    F(rho) = integral_0^(2pi) sqrt(4(1+rho cos(3t))^2 + 9rho^2) dt. (17.2)

This follows by differentiating (17.1), using orthogonality of the radial,
azimuthal and x directions. R and a have units m; F is dimensionless.
There is no preferred rho or R in the knot type. Rescaling both radii by s>0
preserves the trefoil while multiplying L_e by s.

## Candidate seed-to-electron map
For constant nonzero kappa define a seed pitch convention L_nu=2pi/|kappa|.
N016 does not establish this as a neutrino wavelength or measured size.
Writing R=beta L_nu gives the explicit family

    L_e = beta F(rho) L_nu.                               (17.3)

This formalizes the missing scaling interface; beta and rho are not predictions.
IF an additional scalar phase transport law gives phase increment kappa ds
along this curved loop and requires single-valued closure, THEN

    |kappa| L_e = 2pi n,  n=1,2,...,
    L_e = n L_nu,  beta = n/F(rho).                       (17.4)

A curl eigenvalue is not automatically a phase wavenumber along a curved path.
Equation (17.4) is an additional hypothesis; polarization holonomy, curvature,
and torsion may change its phase law. It leaves rho and the choice of n free,
and does not establish an electromagnetic solution, charge, or stability.

## Scale stability
A closure shape must extremize a specified energy/action with specified conserved
quantities, and stability requires the appropriate positive second variation.
For illustration ONLY, if a future derivation yields U(L)=A/L+B L with A,B>0,
then L_*=sqrt(A/B) and U''(L_*)=2A/L_*^3>0 for the scale coordinate.
A has units J m and B J/m. Neither term is provided by the current nodes.
This one-coordinate minimum would not prove stability to other perturbations.
No use of this illustration is made in the alpha calculation.

## Decision on the proposed closure options
Trefoil geometry, nested Trinity phase constraints, and CMB/Beltrami forcing
are potentially complementary inputs, not mutually exclusive electron choices.
The trefoil is the repository's existing E-GEOM candidate. No new preferred
closure law has been silently selected. A real closure law must determine
shape, phase transport, boundary conditions and restoring dynamics together.

## Reproducibility and falsifiers
Run `python nodes/N017_electron_closure_scaling/code/sim.py`.
The code checks periodic closure and compares the analytic arclength integral
against an independently computed polygonal arclength. Tests cover scaling and
phase-family freedom. These check geometry only. A field solution failing its
stated boundary conditions or exhibiting an unstable allowed perturbation would
reject that particular electron candidate; it would not refute every possible
Atom 2.1 closure mechanism.
