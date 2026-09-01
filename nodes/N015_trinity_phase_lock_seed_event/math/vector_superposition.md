# N015 Math Track — 120° Two-Wave Vector Superposition

## 1. Geometry

For α=2π/3, choose

**n₁**=(1/2,√3/2,0),  **n₂**=(1/2,−√3/2,0),  **kᵢ**=k**nᵢ**.

Then **n₁**·**n₂**=−1/2, |**n₁**+**n₂**|=1, and |**n₁**−**n₂**|=√3. The local phase difference is

Γ=δ+(**k₂**−**k₁**)·**r**=δ−√3ky.

Adjacent equal-phase planes are separated by

d=2π/|**k₂**−**k₁**|=λ/√3.

## 2. Phasor fields

Use peak phasors and common polarization **ẑ**:

**Ẽ**=E₀**ẑ**(e^{i**k₁**·**r**}+e^{i(**k₂**·**r**+δ)}),

**B̃**=(E₀/c)[(**n₁**×**ẑ**)e^{i**k₁**·**r**}+(**n₂**×**ẑ**)e^{i(**k₂**·**r**+δ)}].

Because (**n₁**×**ẑ**)·(**n₂**×**ẑ**)=**n₁**·**n₂**=−1/2,

|**Ẽ**|²=2E₀²(1+cosΓ),

c²|**B̃**|²=E₀²(2−cosΓ).

## 3. Energy density

For peak phasors,

⟨u⟩=(1/4)[ε₀|**Ẽ**|²+|**B̃**|²/μ₀].

Using 1/(μ₀c²)=ε₀ gives

⟨u⟩=ε₀E₀²[1+¼cosΓ].

## 4. Energy flux and momentum

The cycle-averaged Poynting vector is

⟨**S**⟩=(1/2μ₀)Re(**Ẽ**×**B̃***).

The common-polarization geometry reduces this to

⟨**S**⟩=I₀(**n₁**+**n₂**)(1+cosΓ)
=I₀**x̂**(1+cosΓ),

where I₀=ε₀cE₀²/2. Vacuum momentum density is ⟨**g**⟩=⟨**S**⟩/c².

## 5. Field invariants

The time-averaged invariants are

⟨E²−c²B²⟩=(3/2)E₀²cosΓ,

⟨**E**·**B**⟩=0.

The first invariant is generally nonzero because the sum of two null plane-wave fields need not itself be null. This remains a standard interference result.

## 6. Phase values

| Γ | |**Ẽ**|/E₀ | ⟨u⟩/(ε₀E₀²) | ⟨Sₓ⟩/I₀ |
|---:|---:|---:|---:|
| 0 | 2 | 5/4 | 2 |
| 2π/3 | 1 | 7/8 | 1/2 |
| π | 0 | 3/4 | 0 |

At Γ=π the electric phasor cancels at that plane, but the magnetic field and energy density do not vanish. None of these local patterns constitutes a new independent propagating mode.

## 7. Fringe average

Over a full transverse fringe, the average of cosΓ is zero. Therefore

overline{⟨u⟩}=ε₀E₀²,

overline{⟨**S**⟩}=I₀**x̂**,

which are exactly the sums of the two individual energy densities and vector fluxes.
