# N011 Math Track — Polarization Bases

## Setup
Take a positive-frequency plane wave propagating along +z:

**E**(z,t)=Re{**E₀**e^{i(kz−ωt)}}.

Transversality requires **E₀**·**ẑ**=0, so **E₀** lies in the x-y plane.

## Linear basis

**E₀**=Eₓ**x̂**+Eᵧ**ŷ**.

## Circular basis

For σ=±1 define

**e**σ=(**x̂**+iσ**ŷ**)/√2.

The basis is orthonormal in the Hermitian inner product and satisfies

i**ẑ**×**e**σ=σ**e**σ.

The conversion formulas are

E₊=(Eₓ−iEᵧ)/√2,  E₋=(Eₓ+iEᵧ)/√2,

Eₓ=(E₊+E₋)/√2,  Eᵧ=i(E₊−E₋)/√2.

This is a unitary change of basis, so |Eₓ|²+|Eᵧ|²=|E₊|²+|E₋|².

## Real-field rotation

For a pure σ mode at z=0,

Re{**e**σe^{-iωt}}
= (**x̂**cosωt+σ**ŷ**sinωt)/√2.

Thus σ=+ rotates from +x toward +y as t increases, and σ=− rotates oppositely. The observed clockwise/counterclockwise word depends on which side of the wave the observer occupies.

## Magnetic field

N000 gives

**B₀**=(**k**×**E₀**)/ω=−iσ **E₀**/c

for a pure σ mode. This phase relation and |**B₀**|=|**E₀**|/c are direct Maxwell checks.

## Boundary

The two-mode decomposition is standard electromagnetism. It supplies no inference about localized particles or topological stability without additional dynamics.
