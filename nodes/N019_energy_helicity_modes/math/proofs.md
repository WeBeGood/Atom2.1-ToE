# Energy, helicity, line models and neutrino modes: audited derivations

SI throughout. These are mathematical results under named assumptions, not a neutrino derivation. Owner: Craig Fink / WeBeGood; AI-assisted audit, 2026-09-14.

## EH-01: energy and the magnetic Beltrami relation

For real E,B, F=E+icB gives U=epsilon_0 integral |F|^2 dV/2. This is instantaneous physical-field energy. Peak monochromatic E and B phasors instead give cycle-averaged U=epsilon_0 integral (|Etilde|^2+c^2|Btilde|^2) dV/4; do not blindly identify those phasors with the real-field RS convention.

If curl B=lambda B with real nonzero constant lambda, A=B/lambda is a vector potential. With periodic zero-mean fields or closed magnetic boundary B dot n=0 and compatible gauge conditions,

$$
H_B=\int A\cdot B\,dV=\lambda^{-1}\int B^2\,dV,
\qquad U_B=\frac{\lambda H_B}{2\mu_0}.
$$

H_B has units T^2 m^4, lambda has units m^-1, and U_B is energy. The electric energy has not disappeared. In N016's standing solution H_B oscillates as sin^2(ckt), whereas total Maxwell energy is constant. The magnetic-helicity balance for suitable vanishing surface terms is dH_B/dt=-2 integral E dot B dV. Vacuum magnetic helicity alone is not generally conserved. A dual-symmetric electromagnetic helicity needs its own properly normalized definition.

Woltjer's constrained variational argument: delta U_B=(1/mu_0) integral curl B dot delta A and delta H_B=2 integral B dot delta A (surface terms assumed zero). Stationarity of U_B-beta H_B gives curl B=2 mu_0 beta B. Domain, conserved constraints and accessible eigenvalues matter for the minimum. A stationary point is not proof of arbitrary dynamical relaxation or stability. Reference: https://doi.org/10.1073/pnas.44.6.489 .

Grok's expression Im integral F* dot curl F/c is not H_B: for curl F=lambda F its integrand is lambda |F|^2, real, and the proposed expression is zero. The dimensions also disagree with H_B. This is an explicit counterexample to the stated identity, not a convention change.

## EH-02: self-confinement does not come from the cited relation

For a smooth finite-energy magnetic field and decaying vector potential on R^3, define B_a(x)=a^2 B(ax), A_a(x)=a A(ax), a>0. Then curl A_a=B_a, H[B_a]=H[B], and U_B[B_a]=a U_B[B]. Under an unrestricted dilation preserving those constraints, a finite positive size is not an isolated energy minimum; energy can approach zero by spreading (a to zero). A fixed domain, other invariant, material stress or further interaction can forbid this dilation and must be specified. This scaling argument supplies no radius-eliminating virial law of the form used by Grok.

## EH-03: legitimate line reduction and conditional elastic model

For a thin tube around a centerline X(s), use transverse coordinates xi. Exactly, U_tube=integral ds integral d^2xi J(s,xi) u(x); for radius much smaller than curvature radius J approximately 1, so U_tube approximately integral u_l(s) ds with u_l=integral_A u dA. Include energy outside the tube and interference between overlapping decompositions. u_l has units J/m; mechanical tension follows a deformation derivative or Maxwell stress and need not equal u_l.

A separately postulated elastic energy is

$$
U_{\rm eff}=\int_0^L\left[\tau+\frac C2(\partial_s\psi)^2\right]ds.
$$

C has units J m, psi is dimensionless angle, and tau has units J/m. At fixed total twist Theta=psi(L)-psi(0), Cauchy-Schwarz implies integral (psi')^2 ds >= Theta^2/L, with equality for uniform twist. Thus

$$
U_{\rm eff,min\ twist}=\tau L+\frac{C\Theta^2}{2L}.
$$

If tau,C>0 and Theta nonzero are fixed and this effective theory applies over the relevant lengths, minimizing over L gives L*=|Theta| sqrt(C/(2tau)) and U*=|Theta| sqrt(2tau C), with positive second derivative. These are **conditional elastic-model results**, not Maxwell predictions for a particle size or mass. If twist density q rather than total twist is fixed, the twist energy is C q^2 L/2. Grok called h a density but used total-twist scaling, and did not derive tau or C.

For isolated thin magnetic tubes with specified framing, H_B approximately Phi^2(Tw+Wr) plus mutual-linking terms for other tubes. Consequently helicity also depends on flux and writhe/linking, not solely on a local twist angle. Gauge-sensitive A dot B cannot be assigned unique local material meaning without a gauge/boundary prescription.

## EH-04: C3 selects a basis, not a mass spectrum

Let P be a cyclic 3 by 3 permutation matrix and omega=exp(2 pi i/3). The Hermitian circulant K=a I+bP+b*P^dagger, a real, has Fourier eigenvectors and eigenvalues k_j=a+2 Re(b omega^j). Different a,b give different spectra with the same C3 eigenvectors. If b is real two eigenvalues are equal. Interpreting K as a mass-squared operator also requires positivity and a physical kinetic term. Three cyclic copies of a configuration can be symmetry-related, not distinct energy eigenstates.

The exact democratic DFT mixing matrix has |U_alpha i|^2=1/3. It does not match the observed reactor mixing |U_e3|^2 approximately 0.022. The older tri-maximal hypothesis is a historical ansatz, not a derivation of mass values. References: https://arxiv.org/abs/hep-ph/9909431 ; https://pdg.lbl.gov/2024/reviews/rpp2024-rev-neutrino-mixing.pdf .

## EH-05: invariant mass and oscillation phase

Total field energy U and momentum P=integral S/c^2 dV obey M^2 c^4=U^2-c^2|P|^2. Only in a rest frame is U=Mc^2. A strictly luminal object has no rest frame/proper length; a standing field can have zero net momentum without being confined. For two photons of energies E1,E2 meeting at spatial angle theta, M^2 c^4=2 E1 E2(1-cos theta); at equal E0 and theta=120 degrees, Mc^2=sqrt(3) E0. This is the two-photon system invariant, not a new bound particle. The background must be included if it receives momentum or energy.

Under standard relativistic ultrarelativistic propagation, expanding E_i=sqrt(p^2c^2+m_i^2 c^4) gives relative phase

$$
\Delta\phi_{ij}\simeq\frac{\Delta m_{ij}^2 c^3D}{2E\hbar}.
$$

If masses are reported as rest energies epsilon_i=m_i c^2, the same expression is Delta(epsilon^2) D/(2 E hbar c). Flavor mixing and interference then require coherent production and detection; the probability's usual sin-squared argument is half this relative phase. Setting c=1 is consistent only with the chosen unit convention. Rewriting E=m in those units does not prove photon rest mass. Spin-1/2, fermionic statistics, weak chirality/coupling and a compatible dispersion remain unaddressed by the seed model.

## EH-06: geometry and literature boundaries

Spatial crossing angle, polarization angle, phase and spatial rotational symmetry are independent specifications. In projective Hilbert space psi, omega psi and omega^2 psi are the same ray. The component vector (1,omega,omega^2) is a distinct matter only relative to a defined basis; it is not three projective states. A sum of doubled mixing angles equal to pi would define a triangle, not an equilateral triangle. A ternary chart is a probability-coordinate convention, not proof of a physical lock.

De Klerk et al. construct finite-energy null Maxwell fields with knotted zero-intensity lines using Bateman variables and complex polynomials (https://doi.org/10.1103/PhysRevA.95.053820). A zero-intensity nodal line is not an energy-filled tube. Kong et al. (https://arxiv.org/abs/2408.09086) use nonlinear photonic crystals with a checkerboard and four-spotted structures; their material coupling cannot be silently imported into source-free vacuum. Trefoil topology admits symmetric embeddings but does not determine a phase-lock force. Kuramoto-inspired neutrino ensemble descriptions concern collective flavor dynamics, not constituent photons (example https://arxiv.org/abs/2609.04441). Unidentified anyon/braid and doubled-angle papers in the supplied text remain unverified references, not evidence.
