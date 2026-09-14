# CMB, standing waves, and the Trinity transformation: explicit proofs

Owner and originating interpretation: Craig Fink / WeBeGood. Mathematical audit: AI-assisted, 2026-09-14. Results below are conditional theorems, not observational demonstrations of neutrinos. Use SI except where c=epsilon_0=mu_0=1 is explicitly used for numerical checks.

## CMB-01: what the observed blackbody fixes

The isotropic blackbody spectral energy density is

$$
u_\nu(T)=\frac{8\pi h_P\nu^3}{c^3[\exp(h_P\nu/k_BT)-1]}.
$$

Here the symbol on the left is **u_nu**, not frequency: u_nu is measured in J m^-3 Hz^-1, h_P is Planck's constant, and nu is frequency. With x=h_P nu/(k_B T), integrating gives

$$
u(T)=\frac{8\pi^5 k_B^4}{15h_P^3c^3}T^4,\qquad
n_\gamma(T)=\frac{16\pi\zeta(3)}{c^3}\left(\frac{k_BT}{h_P}\right)^3.
$$

The standard integral identities are integral x^3/(exp x-1) dx=pi^4/15 and integral x^2/(exp x-1) dx=2 zeta(3). The code checks these by independent numerical quadrature. The temperature supplies an energy scale k_B T and a length scale h_P c/(k_B T); it does not select a knot radius or a particle mass without an additional rule.

Observed near-isotropy and the nearly Planckian spectrum support this spectral input [R1,R2]. They do not measure all relative microscopic phases. An ideal statistically homogeneous, isotropic, unpolarized free thermal field has a modal covariance

$$
\langle a_s(\mathbf k) a_{s'}^*(\mathbf k')\rangle
=P(k)\delta_{ss'}\delta^3(\mathbf k-\mathbf k'),\qquad
\langle a_s(\mathbf k)\rangle=0.
$$

This is a stated thermal ensemble model; an individual realization can interfere locally. Independent modes do not have a fixed relative phase. A coherent special configuration with the same frequency powers is mathematically possible, but its higher-order correlations must be separately supplied and tested. CMB temperature anisotropy/acoustic-perturbation coherence is not by itself phase coherence of microwave electromagnetic oscillations.

For a statistically isotropic angular intensity I_nu, integration over directions gives zero mean flux because integral n_hat dOmega=0, and the radiation pressure tensor is u delta_ij/3. Zero mean flux is not a zero field and not a luminal bulk velocity.

## CMB-02: the standing-wave representation is legitimate

For each pair of opposite wavevectors, write complex spatial basis functions

$$
f_c=\frac{e^{i\mathbf k\cdot\mathbf x}+e^{-i\mathbf k\cdot\mathbf x}}{\sqrt2},
\quad f_s=\frac{e^{i\mathbf k\cdot\mathbf x}-e^{-i\mathbf k\cdot\mathbf x}}{i\sqrt2}.
$$

They are sqrt(2) cos(k dot x) and sqrt(2) sin(k dot x). This is a unitary change of basis, so the coefficient norm/energy is preserved. Vector polarizations and their Maxwell-related magnetic partners transform with the basis. A radiation field in every direction can therefore be represented by standing spatial modes. This is the valid part of the owner's clarification; it is not restricted to two isolated incident beams.

A field can be written in this basis without its random modal coefficients being phase locked. For an equal-occupation pair with covariance P I, a unitary basis change Q gives Q(P I)Q^dagger=P I. Re-expression alone cannot introduce thermal modal coherence.

## CMB-03: a precise C3 transformation of the whole field

Let R rotate space by 120 degrees about a chosen axis, and let its action on a vector field be

$$
(\mathcal R\mathbf F)(\mathbf x)=R\mathbf F(R^{-1}\mathbf x).
$$

On all space (or a rotation-invariant domain with compatible boundary conditions), R^3=I, curl commutes with this action, and its action is unitary in the field energy inner product. Define omega=exp(2 pi i/3) and

$$
\Pi_j=\frac13\sum_{r=0}^2\omega^{-jr}\mathcal R^r,\qquad j=0,1,2.
$$

The root-of-unity identity sum_r omega^{mr}=3 if m=0 mod 3 and zero otherwise proves

$$
\Pi_j\Pi_l=\delta_{jl}\Pi_j,\quad
\sum_j\Pi_j=I,\quad \mathcal R\Pi_j=\omega^j\Pi_j.
$$

Because rotations commute with the free Maxwell evolution, these projections commute with it too. Thus **a Maxwell field, including an all-direction field, has an exact decomposition into three C3 sectors, and each sector evolves as a Maxwell solution**. For finite total energy, orthogonality gives U[F]=sum_j U[Pi_j F]. For infinite homogeneous radiation, use spectral densities or finite-volume regulators and take a controlled limit rather than assigning a finite total energy.

This is one mathematically explicit candidate for a Trinity *representation*. The author has not specified that this projector is the unique physical Trinity map. Keeping all sectors is a decomposition; keeping just one is a projection with discarded complementary energy; adding their energies to the original field would double count. The axis itself is a choice in an isotropic state.

A same-frequency triplet also admits the unitary DFT Q_jr=omega^{-jr}/sqrt(3). For an isotropic thermal triplet, C=P I and Q C Q^dagger=P I. Consequently a passive three-mode transformation preserves its thermal covariance; it does not populate a new species. This restricted statement does not exclude a separately specified interaction, nonthermal state, or nonunitary physical process with an energy reservoir.

## CMB-04: exact standing Beltrami-Maxwell solution

Let e(x) be real, divergence free, and satisfy curl e=k e for constant k>0. Set

$$
\mathbf E(\mathbf x,t)=\mathbf e(\mathbf x)\cos(ckt),\qquad
\mathbf B(\mathbf x,t)=-\mathbf e(\mathbf x)\sin(ckt)/c.
$$

Then curl E=k e cos(ckt)=-partial_t B, and c^2 curl B=-ck e sin(ckt)=partial_t E; both divergences vanish. Hence this is an exact source-free Maxwell solution. Its Riemann-Silberstein field is

$$
\mathbf F=\mathbf E+ic\mathbf B=\mathbf e\,e^{-ickt},\qquad
\nabla\times\mathbf F=k\mathbf F.
$$

An elementary choice is e=E0(cos kz,-sin kz,0). Rotating that field and taking arbitrary linear combinations at the same k gives more curl eigenfields, including angular superpositions over all directions with convergent amplitudes. Different frequency shells can be combined into a broadband Maxwell solution. A generic broadband sum does not have one constant curl eigenvalue.

For this real-e standing family,

$$
u=\epsilon_0|\mathbf e|^2/2,\quad \mathbf S=\mathbf E\times\mathbf B/\mu_0=0,
\quad E^2-c^2B^2=|\mathbf e|^2\cos(2ckt),
\quad \mathbf E\cdot\mathbf B=-|\mathbf e|^2\sin(2ckt)/(2c).
$$

This proves electric/magnetic exchange in an exact standing Beltrami field. At some instants B=0 everywhere and at others E=0 everywhere; neither is a persistently electric-only or magnetic-only traveling vacuum wave. Local energy stays stationary in this example, although its traveling-wave constituents have dispersion omega=ck. It is generally non-null and is not a localized neutrino solution. This distinction must be retained when the owner calls all constituent waves Mach 1.

More generally Maxwell gives the local inequality

$$
c^2u^2-|\mathbf S|^2=\frac{\epsilon_0^2c^2}{4}
\left[(E^2-c^2B^2)^2+4c^2(\mathbf E\cdot\mathbf B)^2\right]\ge0.
$$

Only a nonzero null field saturates |S|=cu. Constituent propagation at c does not force a standing superposition's energy flux to have magnitude cu.

## CMB-05: no special relative phase is selected by linear curl

If curl F1=lambda F1 and curl F2=lambda F2, then for every constant theta,

$$
\nabla\times(F_1+e^{i\theta}F_2)=\lambda(F_1+e^{i\theta}F_2).
$$

Having fields in every direction does not change this identity. For free modal amplitudes a_l(t)=a_l(0) exp(-i omega_l t), populations |a_l|^2 stay constant. Equal frequencies preserve every initial relative phase; unequal frequencies slip. There is no preferred attracting 120-degree phase under this evolution. Perturbations between two free finite-energy solutions retain their energy norm, so an attracting phase lock is not generated by free dynamics. This does not deny neutral persistence of a deliberately prepared coherent configuration.

## CMB-06: localization limitation of constant-lambda fields

Suppose F is square integrable on R^3, divergence free, and curl F=lambda F with real constant nonzero lambda. Curling again gives -laplacian F=lambda^2 F. Fourier transformation gives (|k|^2-lambda^2) Fhat(k)=0. Its Fourier support lies on a sphere of measure zero. A square-integrable function supported only there is zero almost everywhere. Thus no nonzero globally square-integrable constant-lambda curl eigenfield exists on unbounded R^3. Periodic/cavity modes and generalized monochromatic fields evade the finite-energy assumption; localized wave packets require a spectral spread. This does **not** exclude finite-energy time-dependent Maxwell knots constructed from broadband fields [R4].

## Remaining physical step

The representation theorem is established. Identifying a sector or special coherent configuration as a neutrino still requires a definition of the observable NewWave field, appropriate energy accounting, localization and stability criteria, its dispersion, and its coupling to neutrino production/detection. An invertible field redefinition can reveal structure but cannot by itself add independently observable degrees of freedom. The proposed coherent BBRV substrate is preserved as a project hypothesis rather than discarded because a two-beam calculation was incomplete.

References: R1 Fixsen et al. https://arxiv.org/abs/astro-ph/9605054 ; R2 NASA FIRAS https://lambda.gsfc.nasa.gov/product/cobe/firas_overview.html ; R4 de Klerk et al. https://doi.org/10.1103/PhysRevA.95.053820 . The projection, covariance, standing-field and localization proofs are supplied above, not attributed to those observational papers.
