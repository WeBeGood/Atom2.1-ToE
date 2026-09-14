# From an All-Direction Blackbody Field to Trinity and Beltrami Representations

**An Atom 2.1 derivation audit and research framework**

Originating model and project owner: **Craig Fink (WeBeGood)**. [Authors and final contribution statement to be confirmed by the human author.] [Affiliations to be supplied.] Working manuscript v0.1, 2026-09-14. AI-assisted mathematical drafting and checking; not journal peer reviewed, submitted, or empirically validated as a neutrino theory.

## Abstract

Atom 2.1 proposes that a Trinity transformation of the all-direction cosmic microwave background (CMB) field organizes a Beltrami Blackbody Radiation Vortex (BBRV) field whose NewWave structures are interpreted as neutrino seeds. We formulate this full-field proposal separately from a two-beam interference calculation. Opposite-direction Maxwell modes admit a standing-wave basis, and a rotation-invariant field admits an orthogonal decomposition into three cyclic-symmetry sectors. We construct an exact standing Beltrami-Maxwell solution with electric-magnetic exchange. These results establish representations and special solutions, while preserving the need to demonstrate localization, phase selection and neutrino observables. We correct proposed energy-helicity identities and derive a conditional elastic line-energy minimum. We also audit an independent-event tired-light model: three successive one-eighth losses remove 169/512 of initial energy, and the exact relative RMS spectral spread at half mean energy is 30.0845 percent. The distinction between established observations, conditional mathematics, and the project's physical hypotheses provides a reproducible basis for further development without fitting a purported prediction to its target.

## Keywords

Maxwell fields; blackbody radiation; standing waves; Trinity addition; cyclic symmetry; Beltrami fields; magnetic helicity; neutrino modes; spectral broadening; Atom 2.1.

## 1. Introduction and Research Question

The starting point is the full radiation field. Craig Fink's clarification is that the CMB supplies waves in every direction, and that Trinity addition is intended as a transformation within this field into the NewWave/BBRV description. A restriction to two isolated incident beams does not exhaust that proposal. The repository's earlier P002 explicitly studies only that restricted baseline; the present paper develops the additional all-direction and standing-field structure.

There are two questions. First, can ordinary Maxwell radiation be transformed into standing, cyclic and Beltrami representations? We show that it can under explicit conditions. Second, does that construction establish stable neutrino seeds with predicted masses and interactions? That is a separate physical identification, for which the supplied equations are incomplete.

The word "Mach 1" denotes the project's luminal constituent-wave regime. Constituent dispersion at $c$ does not imply that a standing interference pattern carries energy with speed $c$. We therefore distinguish constituent propagation, local energy flux, motion of a field pattern and motion of a particle. Natural units are permissible, but SI factors are restored for comparisons.

The purpose of this manuscript is to derive as much as possible without changing the owner's intended starting point or silently promoting interpretations into results. Numerical verification of an equation is not evidence that a proposed particle exists.

## 2. Background

**Established observation.** The CMB monopole has a nearly Planckian spectrum and is approximately isotropic after appropriate foreground and motion corrections. FIRAS strongly constrains departures from a blackbody spectrum [1,2]. These observations support the spectral input used below. They do not specify every relative microscopic electromagnetic phase.

**Standard result.** Maxwell's vacuum equations admit arbitrary linear superpositions of solutions. Standing-wave and helicity bases reorganize their degrees of freedom. Curl eigenfields provide helical spatial structure. Finite-energy time-dependent knotted Maxwell solutions also exist, including solutions with knotted zero-intensity lines [4]. These properties should not be conflated: a dark nodal line, a flux tube, a monochromatic eigenmode and a localized particle are distinct constructions.

**Project hypothesis.** Atom 2.1 identifies a special organization of the photonic CMB field with the BBRV/NewWave neutrino field. A coherent standing substrate and a physical seed interpretation are preserved as hypotheses to formalize. They are stronger statements than spectral isotropy alone.

**Open test.** Specify the Trinity map, its observables and any required dynamics; determine whether it describes an alternative representation of an existing electromagnetic solution or a physically distinct excitation. An invertible field redefinition is mathematically legitimate but leaves the number of independent degrees of freedom unchanged.

## 3. Methods and Reproducibility

We use source-free Maxwell theory in flat spacetime for the field constructions. Fields are either square-integrable on all space or explicitly labeled periodic/generalized modes. Rotational projectors require a rotation-invariant domain. Thermal calculations use a statistically homogeneous, isotropic, unpolarized ensemble as the baseline. Departures from that ensemble must be supplied as additional correlation information.

The real-field Riemann-Silberstein convention is $\mathbf F=\mathbf E+ic\mathbf B$. Here $\mathbf E$ and $\mathbf B$ are real physical fields, rather than independent complex peak phasors. Magnetic helicity is $H_B=\int\mathbf A\cdot\mathbf B\,dV$ with boundary and gauge conditions stated when used. We distinguish Planck's constant $h_P$, helicity $H_B$, total twist angle $\Theta$, line length $L$, and source-observer distance $D$.

The derivations reside in nodes N016, N019 and N020. Their standard-library Python programs perform independent quadrature, spatial/time finite differences, matrix operations and probability summation. The test suite checks representative counterexamples as well as positive identities. Representative floating-point residuals are reported with tolerances, not as exact symbolic proofs. No observed neutrino mass, fine-structure constant or Hubble constant is used to tune a prediction.

From the repository root:

```bash
python -m pip install -r requirements-dev.txt
python nodes/N016_cmb_seeded_beltrami_line/code/sim.py
python nodes/N019_energy_helicity_modes/code/sim.py
python nodes/N020_tired_light_statistics/code/sim.py
python render_superseed.py
python scripts/build_node_claims.py
python scripts/build_node_index.py
python scripts/build_paper_outline.py
python scripts/validate_nodes.py
python scripts/validate_papers.py
python -m pytest -q
```

## 4. Results

### 4.1 The blackbody provides a spectral scale, not a phase-lock rule

For frequency $\nu$ and temperature $T$,

$$
u_\nu(T)=\frac{8\pi h_P\nu^3}{c^3[\exp(h_P\nu/k_BT)-1]}.
$$

The left side is spectral energy density $u_\nu$, measured in J m$^{-3}$ Hz$^{-1}$. Integrating this expression and dividing its integrand by photon energy for the number density gives

$$
u(T)=\frac{8\pi^5 k_B^4T^4}{15h_P^3c^3},\qquad
n_\gamma(T)=\frac{16\pi\zeta(3)}{c^3}\left(\frac{k_BT}{h_P}\right)^3.
$$

At the illustrative input $T=2.725$ K, the implementation finds $u=4.17173825\times10^{-14}$ J m$^{-3}$ and $n_\gamma=4.10500843\times10^8$ m$^{-3}$. The temperature supplies scales such as $k_BT$ and $h_Pc/(k_BT)$. It does not select a particular particle mass or tube radius unless an additional dimensionless relation is derived.

In the ideal free thermal ensemble, different traveling modes have diagonal covariance, with equal occupation for equivalent directions and polarizations at a fixed frequency. Their mean complex amplitudes vanish. Local interference remains possible in each realization; ensemble diagonality is not a statement that electromagnetic fields never interfere. The distinction is that a fixed cross-mode phase is not supplied by the Planck power spectrum.

### 4.2 Standing waves provide a valid description of all-direction radiation

For opposite wavevectors, define

$$
f_c=\frac{e^{i\mathbf k\cdot\mathbf x}+e^{-i\mathbf k\cdot\mathbf x}}{\sqrt2},
\qquad
f_s=\frac{e^{i\mathbf k\cdot\mathbf x}-e^{-i\mathbf k\cdot\mathbf x}}{i\sqrt2}.
$$

These are standing spatial sine and cosine functions. The change from traveling to standing modes is unitary and preserves the complete field and its energy when coefficients and magnetic partners are transformed consistently. Applying it to every opposite-direction pair gives a standing-wave representation of the all-direction radiation field.

This validates the representation part of the owner's clarification. It does not require assuming that the entire thermal field is one coherent standing oscillation. For a pair with covariance $C=P I$, a unitary transformation $Q$ gives $QCQ^\dagger=P I$. Merely changing the basis does not create correlated phases.

### 4.3 An explicit Trinity-compatible decomposition of the full field

Let $R$ rotate by $120^\circ$ about a chosen axis, and act on vector fields by

$$
(\mathcal R\mathbf F)(\mathbf x)=R\mathbf F(R^{-1}\mathbf x).
$$

Put $\omega=e^{2\pi i/3}$ and define

$$
\Pi_j=\frac13\sum_{r=0}^{2}\omega^{-jr}\mathcal R^r,
\qquad j=0,1,2.
$$

The cube-root identity proves

$$
\Pi_j\Pi_l=\delta_{jl}\Pi_j,\qquad
\sum_j\Pi_j=I,\qquad
\mathcal R\Pi_j=\omega^j\Pi_j.
$$

On a compatible domain these operators commute with curl and free Maxwell evolution. Thus a full Maxwell field decomposes into three cyclic sectors, each of which is itself a Maxwell solution. For finite-energy fields, orthogonality gives $U[\mathbf F]=\sum_jU[\Pi_j\mathbf F]$. Homogeneous radiation instead requires energy densities or a controlled volume limit.

This is a concrete possible mathematical meaning for a Trinity field transformation; it is not asserted to be the owner's unique intended operator. A selected sector is a projection. Its complementary sectors still account for the remaining energy. Retaining the original field and adding the projected field as extra energy would double count it.

On a three-mode frequency shell, the same algebra yields a unitary discrete Fourier matrix $Q_{jr}=\omega^{-jr}/\sqrt3$. An isotropic equal-occupation thermal covariance remains $P I$. Threefold coordinates therefore exist without implying the physical creation of three new species or a selective transfer into one of them.

### 4.4 An exact standing Beltrami-Maxwell field

Let a real spatial field $\mathbf e$ obey $\nabla\cdot\mathbf e=0$ and $\nabla\times\mathbf e=k\mathbf e$, where $k>0$ is constant. Then

$$
\mathbf E=\mathbf e\cos(ckt),\qquad
\mathbf B=-\mathbf e\sin(ckt)/c
$$

satisfy all four source-free Maxwell equations. In particular, $\nabla\times\mathbf E=k\mathbf e\cos(ckt)=-\partial_t\mathbf B$, and $c^2\nabla\times\mathbf B=-ck\mathbf e\sin(ckt)=\partial_t\mathbf E$. The complex field becomes

$$
\mathbf F=\mathbf e e^{-ickt},\qquad
\nabla\times\mathbf F=k\mathbf F.
$$

One example is $\mathbf e=E_0(\cos kz,-\sin kz,0)$. Rotated versions and their same-$k$ sums remain curl eigenfields; convergent angular superpositions can include all directions. Summing frequency shells gives a broadband Maxwell solution, although not generally a single constant curl eigenvalue.

For this real-spatial-field standing family,

$$
u=\frac{\epsilon_0|\mathbf e|^2}{2},\qquad
\mathbf S=0.
$$

Electric and magnetic energy exchange while their sum remains constant. At specific instants one field vanishes, but this is not a persistently electric-only or magnetic-only traveling mode. The field is generally non-null, and the example is not spatially localized. Its constituent plane waves have luminal dispersion; its local net energy flux is zero.

The general Maxwell identity

$$
c^2u^2-|\mathbf S|^2=\frac{\epsilon_0^2c^2}{4}
\left[(E^2-c^2B^2)^2+4c^2(\mathbf E\cdot\mathbf B)^2\right]
$$

shows precisely when a superposed field transports local energy at $c$: equality requires a nonzero null field. It cannot be inferred solely from the speeds of the constituents.

### 4.5 Phase persistence, selection and localization are separate

If two fields share a curl eigenvalue $\lambda$, then

$$
\nabla\times(\mathbf F_1+e^{i\theta}\mathbf F_2)
=\lambda(\mathbf F_1+e^{i\theta}\mathbf F_2)
$$

for every constant $\theta$. This disproves the proposed universal selection of $120^\circ$ by the curl condition alone. Equal-frequency free modes preserve their initially imposed relative phases; unequal frequencies slip. Constant phase is neutral persistence, not evidence of a restoring interaction. An attracting lock requires additional dynamics or a demonstrated constraint.

There is also a localization limitation. If a divergence-free field is square-integrable on all of $\mathbb R^3$ and obeys $\nabla\times\mathbf F=\lambda\mathbf F$ for a constant real nonzero $\lambda$, then its Fourier transform is supported on $|\mathbf k|=|\lambda|$. A square-integrable function supported on this measure-zero sphere vanishes almost everywhere. Consequently a nonzero globally finite-energy constant-$\lambda$ mode does not exist under those assumptions. Periodic modes, boundary-confined fields and broadband time-dependent knots are different cases; the result does not rule out the last of these [4].

### 4.6 Correct energy and helicity relations

With real physical fields, $U=\epsilon_0\int|\mathbf F|^2dV/2$. For a magnetic Beltrami field with compatible boundary/gauge conditions and nonzero constant $\lambda$, choose $\mathbf A=\mathbf B/\lambda$. Then

$$
U_B=\frac{1}{2\mu_0}\int B^2dV
=\frac{\lambda H_B}{2\mu_0}.
$$

This is magnetic energy, not automatically total electromagnetic energy. Woltjer's variational result also needs a specified domain and helicity constraint [3]. In general vacuum evolution, magnetic helicity alone changes as $dH_B/dt=-2\int\mathbf E\cdot\mathbf B\,dV$ when surface terms vanish. It must not be confused with a properly defined dual-symmetric electromagnetic helicity.

The proposed identity $H_B=c^{-1}\operatorname{Im}\int\mathbf F^*\cdot(\nabla\times\mathbf F)dV$ fails: for real $\lambda$, the integrand is $\lambda|\mathbf F|^2$, which is real. The right side is zero even when magnetic helicity is nonzero. Missing SI factors and this incorrect identity cannot be repaired by relabeling the field as a seed.

A further scaling check prevents an unsupported confinement claim. Under $\mathbf B_a(\mathbf x)=a^2\mathbf B(a\mathbf x)$ and $\mathbf A_a(\mathbf x)=a\mathbf A(a\mathbf x)$ on unbounded space, helicity is fixed and magnetic energy scales as $a$. If such dilation is allowed, helicity alone selects no finite-size energy minimum. Other constraints can change that result, but must be specified.

### 4.7 A conditional line-energy model can be derived honestly

A thin-tube reduction integrates the actual field energy across a cross-section, including a geometric Jacobian when necessary. It gives $U_{\rm tube}\simeq\int u_\ell(s)ds$. Mechanical tension is a separate stress/deformation quantity; it is not necessarily the same as $u_\ell$.

If an elastic model is explicitly postulated,

$$
U_{\rm eff}=\int_0^L\left[\tau+\frac C2(\partial_s\psi)^2\right]ds,
$$

then at fixed total twist $\Theta$, Cauchy-Schwarz gives $\int(\partial_s\psi)^2ds\ge\Theta^2/L$. Uniform twist attains the minimum:

$$
U_{\rm eff}=\tau L+\frac{C\Theta^2}{2L},\qquad
L_* = |\Theta|\sqrt{\frac{C}{2\tau}},\qquad
U_* = |\Theta|\sqrt{2\tau C}.
$$

These last two results assume fixed positive $\tau,C$, nonzero $\Theta$ and validity of the model near the minimum. They prove a conditional elastic equilibrium. They do not derive $\tau$ or $C$ from Maxwell theory, vacuum impedance or the angle $120^\circ$. Fixing twist density instead of total twist changes the length scaling. Magnetic helicity further depends on magnetic flux, writhe and linking, not just local twist.

### 4.8 Three cyclic modes do not fix neutrino masses

For a cyclic permutation $P$, a Hermitian operator

$$
K=aI+bP+b^*P^\dagger
$$

has Fourier eigenvectors and eigenvalues $k_j=a+2\operatorname{Re}(b\omega^j)$. Changing $a,b$ changes the spectrum while preserving the cyclic basis. A real $b$ gives two equal eigenvalues. Therefore $C_3$ symmetry alone does not determine three distinct neutrino masses. Interpreting $K$ as a mass-squared operator requires a physical kinetic term, positivity and a derivation of its coefficients.

The exact democratic Fourier mixing matrix gives every squared entry $1/3$, whereas measured $|U_{e3}|^2$ is approximately $0.022$ [6,7]. The historical tri-maximal construction is useful group-theoretic context, not an already successful full neutrino model. Global phase multiples of a state are the same ray in projective Hilbert space; three complex component phases must not be mistaken for three automatically distinct physical states.

For any candidate localized system, compute total momentum as well as energy:

$$
M^2c^4=U^2-c^2|\mathbf P|^2.
$$

The standard ultrarelativistic relative oscillation phase, with SI masses, is

$$
\Delta\phi_{ij}\simeq\frac{\Delta m_{ij}^2c^3D}{2E\hbar}.
$$

A field-to-neutrino theory must also establish the appropriate spin, statistics, weak interactions and production/detection coherence. Naming three configurations and inserting their energies into the standard phase law leaves these tasks open.

### 4.9 What the tired-light arithmetic does establish

Under a separately assumed loss law $d\ln\nu/ds=-a(s)$, integration yields $1+z=\exp(\int a\,ds)$. If each event removes fraction $\kappa$ of the remaining energy, $E_N/E_0=(1-\kappa)^N$. Three events with $\kappa=1/8$ remove $169/512$, not $3/8$. The latter would apply to a different convention in which each allocation refers to the original energy.

For independent events with Poisson mean $\mu$, the exact probability-generating function gives

$$
\langle E\rangle=E_0e^{-\mu\kappa},\qquad
\frac{\sigma_E}{\langle E\rangle}=\sqrt{e^{\mu\kappa^2}-1}.
$$

At half surviving mean, $\mu=\ln2/\kappa$, and the relative RMS width at $\kappa=1/8$ is $0.30084503098$. This corrects Claude's approximate 29 percent. It is a standard deviation relative to the surviving mean, not a Gaussian FWHM; the idealized distribution has discrete energy steps.

The distinction between $\ln\langle E\rangle$ and $\langle\ln E\rangle$ matters. Their attenuation rates are $r\kappa$ and $-r\ln(1-\kappa)$ respectively, differing by 6.825 percent at one-eighth loss. Here $r=n\sigma$ is event rate per length.

For a specified mean redshift, an allowed RMS width $w$ gives the conditional bound

$$
\kappa\le\frac{\ln(1+w^2)}{\ln(1+z)}.
$$

At $z=1$ and an illustrative $w=10^{-3}$ this is $1.4427\times10^{-6}$. This is not a bound inferred from a particular observed source. Infinitely many sufficiently small events can approach a deterministic loss law with negligible event-count broadening; such a limit still requires a physical mechanism.

Using $H_0=70$ km s$^{-1}$ Mpc$^{-1}$ as a chosen calibration, $n=4.1\times10^8$ m$^{-3}$ and $\kappa=1/8$ yields $a=7.56705\times10^{-27}$ m$^{-1}$ and $\sigma=1.47650\times10^{-34}$ m$^2$. Claude's arithmetic is correct. However, photon wavelength squared is not an obligatory collision area. The cross-section must be derived from dynamics; its magnitude alone does not establish failure or success.

### 4.10 Reproducible numerical results

| Check | Representative result | Meaning |
|---|---|---|
| Planck energy integral | Relative error below $10^{-9}$ | Spectral normalization verified |
| Standing-field Maxwell residual | Below $10^{-8}$ in normalized units | Analytic solution checked by finite differences |
| Cyclic projector algebra | Error below $10^{-12}$ | Full-field representation algebra verified on a modal example |
| Standing energy and flux | Constant energy, zero flux to numerical precision | Constituent speed and bulk flux distinguished |
| Proposed imaginary helicity | Zero for nonzero-helicity example | Counterexample to the supplied formula |
| Poisson moments | Direct sum agrees within $10^{-12}$ | Conditional linewidth calculation verified |

These tests are internal checks. They neither simulate the complete CMB nor detect neutrinos or establish cosmological redshift.

## 5. Discussion

The all-direction clarification matters. A complete field has a richer set of decompositions than a two-beam example, and the standing Beltrami solution demonstrates a real special case that can inform the model. The mathematical obstruction is not that field transformations are forbidden. It is that representations, prepared coherent patterns and physical conversion mechanisms make different claims.

The referenced knot paper supplies finite-energy null fields with knotted dark lines, not an energy-filled neutrino seed [4]. The cited three-wave-mixing paper uses nonlinear photonic crystals and four-spotted structures, so its stability cannot be transferred directly to empty-space Maxwell theory [5]. Kuramoto-inspired collective neutrino studies describe flavor ensembles rather than constituent photons [9]. Geometric phases and ternary plots likewise do not determine a neutrino mass operator.

Claude correctly identifies the absence of a derived energy-transfer interaction in the tired-light branch. Its cross-section size comparison and universal wording about scattering need qualification. The supernova evidence agrees with time dilation within errors: DES reports $b=1.003\pm0.005$ statistical $\pm0.010$ systematic for durations proportional to $(1+z)^b$ [8]. A constant propagation delay gives $t_{\rm arr}=t_{\rm emit}+T(D)$ and therefore does not stretch emission intervals. A different timing map needs a physical derivation.

FIRAS places stringent spectral-distortion constraints [1], but not every scattering process distorts an equilibrium spectrum. The proposed model needs a frequency-angle-time transfer kernel and a recipient energy-momentum budget. Interference itself conserves total Maxwell energy; it is not automatically an irreversible loss channel. N015's local $7/8$ energy density is not a universal $7:1$ intensity contrast or a transfer probability.

## 6. Limitations and Scope

No independently derived neutrino masses, mass-squared differences, weak couplings, fine-structure constant, Hubble constant or dark-sector predictions are claimed. The owner's BBRV interpretation remains the organizing research hypothesis. A complete proof cannot be manufactured by assigning physical names to otherwise unspecified coefficients.

The constant-curl localization theorem applies to nonzero constant real eigenvalues and square-integrable fields on unbounded flat space. It does not prohibit bounded-domain modes, broadband knots, or specified nonlinear theories. The no-attracting-lock argument applies to free linear evolution; neutral persistence is allowed. The thermal covariance argument applies to the stated equal-occupation ensemble, not every imaginable nonthermal correlated state. The stochastic linewidth constraint applies to independent finite-loss events, not automatically to deterministic or correlated processes.

This manuscript uses benchmark parameters and published observations for context, without performing a new observational fit. A journal target and its formatting, disclosure and data policies have not yet been selected. Final authorship, affiliations and declarations require the human author's completion.

## 7. Conclusion

An all-direction Maxwell field admits exact standing-wave and threefold cyclic representations, and an explicit standing Beltrami solution exhibits electric-magnetic exchange. These are established conditional results that preserve the intended CMB starting point. They do not, by themselves, identify a neutrino field or select its masses. Correctly scoped helicity, line-energy and stochastic-loss calculations sharpen the remaining work: define observable seed structure, derive its dynamics and conserved quantities, then compute predictions that distinguish it from ordinary electromagnetic interference and from target calibration.

## Data and Code Availability

All derivations, Python programs, diagnostic JSON, test cases and source references are in the public WeBeGood/Atom2.1-ToE repository. This paper maps to N016, N019 and N020, with N000/N015 providing baseline definitions. The complete claim-by-claim audit is [the dated review record](../../notes/2026-09-14_grok_claude_peer_review.md). No new empirical dataset was collected. Diagnostic files may vary in their final floating-point digits across platforms; the mathematical checks use explicit tolerances.

## Author Contributions

Craig Fink / WeBeGood originated the Atom 2.1 model and supplied the CMB/Trinity clarification and source discussions. AI assistance supplied literature checks, mathematical auditing, code, tests and draft text. Grok's proposed construction and Claude's critique are attributed as supplied discussion contributions, not journal authors or independent peer reviewers. [Author approval, final authorship and contributions to be completed by the human author.]

## Acknowledgments

The review distinguishes the owner's scientific proposal from AI-generated derivations and corrections. No endorsement by cited authors, journals or institutions is implied.

## Declarations

Funding and conflicts of interest have not been supplied and require author declarations. Institutional affiliation has not been supplied. Ethics approval and participant consent are not applicable to this theoretical/computational work. Generative AI use is disclosed above; journal-specific wording must be checked before submission. No empirical validation, external peer-review acceptance or publication is claimed.

## References

1. Fixsen, D. J., et al. (1996). The Cosmic Microwave Background Spectrum from the Full COBE/FIRAS Data Set. *Astrophysical Journal*, 473, 576. <https://doi.org/10.1086/178173> . <https://arxiv.org/abs/astro-ph/9605054> .
2. NASA LAMBDA. FIRAS overview. <https://lambda.gsfc.nasa.gov/product/cobe/firas_overview.html> . Observational spectrum context, accessed 2026-09-14.
3. Woltjer, L. (1958). A Theorem on Force-Free Magnetic Fields. *PNAS*, 44, 489-491. <https://doi.org/10.1073/pnas.44.6.489> .
4. de Klerk, A. J. J. M., van der Veen, R. I., Dalhuisen, J. W., and Bouwmeester, D. (2017). Knotted optical vortices in exact solutions to Maxwell's equations. *Physical Review A*, 95, 053820. <https://doi.org/10.1103/PhysRevA.95.053820> .
5. Kong, C., et al. (2024). Composite solitary vortices of three-wave mixing in quasi-phase-matched photonic crystals. *Chaos, Solitons & Fractals*, 187, 115358. <https://doi.org/10.1016/j.chaos.2024.115358> . <https://arxiv.org/abs/2408.09086> .
6. Scott, W. G. (1999). Tri-Maximal vs Bi-Maximal Neutrino Mixing. <https://arxiv.org/abs/hep-ph/9909431> .
7. Particle Data Group (2024). Neutrino Masses, Mixing, and Oscillations. <https://pdg.lbl.gov/2024/reviews/rpp2024-rev-neutrino-mixing.pdf> .
8. White, R. M. T., et al. (2024). The Dark Energy Survey Supernova Program: Slow supernovae show cosmological time dilation out to z approximately 1. <https://arxiv.org/abs/2406.05050> .
9. Majumder, R., Mukherjee, D., Gupta, S., and Dasgupta, B. (2026). Stability of Collective Neutrino Oscillations -- A Distributional Approach. Preprint, not treated here as an established empirical result. <https://arxiv.org/abs/2609.04441> .

## Version and Provenance

P004 v0.1, 2026-09-14. Based on the owner-supplied Grok/Claude text, the subsequent CMB clarification, current repository base c988bd6402298e26d40565b1e4cf6c05c20f50aa, and the cited sources. The prior P001-P003 manuscripts and their scientific scope are preserved. The new proofs are conditional statements, and the C3 operator is an explicit candidate representation rather than an inferred unique owner definition. This is a working research manuscript prepared for human revision, not a claim of journal readiness or acceptance.
