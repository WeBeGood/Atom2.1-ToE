# Conditional tired-light statistics and observational tests

Owner: Craig Fink / WeBeGood. AI-assisted audit of Grok and Claude, 2026-09-14. No physical coupling or redshift mechanism is asserted by these probability identities.

## TL-01: fixed count and continuous loss

If each event removes fraction kappa of the remaining energy, E_N/E0=(1-kappa)^N. At kappa=1/8, three events lose 1-(7/8)^3=169/512=0.330078125. The sum 3/8 is valid for three disjoint losses each defined relative to the original energy, not the sequential remaining-energy rule.

Assume d ln nu/ds=-a(s). Integration gives 1+z=exp(integral a ds), with a in m^-1. At constant a and small distance, z approximately a D. Setting a=H0/c matches the measured local slope but predicts neither H0 nor the entire cosmological distance relation. In stationary linear propagation, attenuation reduces amplitude/photon counts without automatically changing frequency. A redshift requires actual frequency conversion, with energy and momentum accounting for the recipient.

The repository N015 geometry gives normalized cycle-averaged energy 7/8 at one local phase for a specified polarization. This is not a universal 7:1 contrast and not a probability or an irreversible transferred fraction.

## TL-02: exact independent-event distribution

Assume N is Poisson with mean mu=integral r ds, r=n_target sigma, and fixed 0<kappa<1. Set q=1-kappa and E=E0 q^N. The generating function sum_N e^-mu mu^N t^N/N!=exp[mu(t-1)] yields

$$
\langle E\rangle=E_0e^{-\mu\kappa},\quad
\langle E^2\rangle=E_0^2e^{\mu(-2\kappa+\kappa^2)},\quad
\frac{\sigma_E}{\langle E\rangle}=\sqrt{e^{\mu\kappa^2}-1}.
$$

For mean E0/2, mu=ln2/kappa, hence relative RMS width sqrt(2^kappa-1)=0.30084503098 at kappa=1/8. Claude's 29 percent is an approximation, not the exact result. This is standard deviation relative to the surviving mean, not FWHM; relative to E0 it is 0.15042251549. The ideal line is a comb at E0 q^N before instrumental/intrinsic broadening, not a Gaussian.

The distribution of log energy has mean log E0+mu log q and variance mu(log q)^2. Thus -d ln <E>/ds=r kappa whereas -d <ln E>/ds=-r ln(1-kappa). The latter coefficient is 1.06825114 times the former at kappa=1/8. A common redshift for every photon cannot be inferred from the mean energy alone.

For a specified mean redshift defined by <E>/E0=1/(1+z),

$$
\mathrm{CV}^2=(1+z)^\kappa-1.
$$

An allowed fractional RMS width w therefore imposes kappa <= ln(1+w^2)/ln(1+z) in this model. At z=1 and an **illustrative**, not dataset-derived, w=10^-3, kappa must be no more than about 1.4427e-6. Taking kappa to zero and r to infinity at fixed r kappa produces a deterministic continuous-loss limit with vanishing event-count broadening. This removes this particular stochastic obstacle, not the requirements to derive a coupling and match other observables.

## TL-03: back-calculated cross-section

Using H0=70 km s^-1 Mpc^-1 as a chosen benchmark, c=299792458 m/s, 1 Mpc=3.085677581491367e22 m, n=4.1e8 m^-3 and kappa=1/8,

$$
a=7.56705327994\times10^{-27}\ {\rm m^{-1}},\quad
\sigma=a/(n\kappa)=1.47649820096\times10^{-34}\ {\rm m^2}.
$$

This is an inverse calibration for the mean-energy model. Claude's arithmetic is correct. Wavelength squared is not a photon collision area or a lower bound on cross-section; the Planck spectrum also has different peak positions in frequency and wavelength coordinates. Calling the inferred coupling absurd because lambda_peak^2 is larger is unjustified. A cross-section must follow from dynamics, incident/target energies, polarizations and relative directions. If target density is called the observed CMB, that identification and the recipient's heat/momentum budget must be justified.

## TL-04: conservation and measurements

Poynting's theorem is partial_t u+div S=-J dot E. In source-free linear vacuum the right side vanishes. Interference changes local transport, not an independent irreversible storage channel. A receiving field or medium requires an explicit coupled energy-momentum budget. A random-event loss law does not apply automatically to a coherent field-redefinition model.

The DES supernova study reports light-curve widths proportional to (1+z)^b with b=1.003 +/- 0.005 statistical +/- 0.010 systematic, not mathematically exact equality (https://arxiv.org/abs/2406.05050). In a static time-translation-invariant propagation model with t_arr=t_emit+T(D), dt_arr/dt_emit=1; a common delay alone does not stretch a source. A proposed alternative must derive a nontrivial timing map or transfer kernel and compare its distortion and stretch with data.

FIRAS bounds spectral deviations: RMS below 50 ppm of peak CMB intensity in the cited analysis, with constraints on y and mu distortions (https://arxiv.org/abs/astro-ph/9605054). This does not prohibit all scattering: elastic scattering or equilibrium processes can preserve a spectrum. Compute the frequency-angle collision kernel, energy deposition and relaxation instead of equating a generic scattering rate to distortion.

Independent fixed 1/8 losses predict very large line broadening; the precise exclusion for a particular source needs that source's spectrum, intrinsic width and selection function. Image blurring is a separate angle-kernel test and not automatically implied by pure forward energy loss. No observational dataset has been fitted here. Dark matter, gravity and dark energy do not follow from naming the receiving energy 'twist'; their stress-energy and observational predictions remain frontier tasks.
