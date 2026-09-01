# N000 Math Track — Vector Calculus Derivation (Vacuum)

## Preconditions

Let **E**,**B**∈C² on an open source-free region of an inertial Cartesian chart. Assume μ₀ and ε₀ are constant, spatial and time derivatives commute, and the divergence constraints hold. These conditions are what permit the following local manipulations.

Use the identity

∇×(∇×**F**) = ∇(∇·**F**) − ∇²**F**.

## Wave equation for E

Start from Faraday’s law and take a curl:

∇×(∇×**E**) = −∂t(∇×**B**).

Substitute the source-free Ampère–Maxwell law:

∇×(∇×**E**) = −μ₀ε₀∂t²**E**.

The curl-curl identity and ∇·**E**=0 give

−∇²**E** = −μ₀ε₀∂t²**E**,

hence

∇²**E** − μ₀ε₀∂t²**E** = 0.

## Wave equation for B

Take a curl of source-free Ampère–Maxwell:

∇×(∇×**B**) = μ₀ε₀∂t(∇×**E**)
= −μ₀ε₀∂t²**B**.

Using ∇·**B**=0 gives

∇²**B** − μ₀ε₀∂t²**B** = 0.

## Speed

Comparison with the standard wave operator yields

c = 1/√(μ₀ε₀).

This is a characteristic speed of the differential equations. Existence and uniqueness of a particular field require compatible initial and boundary data.

## Plane-wave constraints

Insert **E**=Re{**E₀**e^{i(**k**·**x**−ωt)}} and the analogous **B** into Maxwell’s equations. Replacing ∇ by i**k** and ∂t by −iω gives

- **k**·**E₀**=0 and **k**·**B₀**=0,
- **k**×**E₀**=ω**B₀**,
- **k**×**B₀**=−(ω/c²)**E₀**.

Cross the first curl relation with **k** and use transversality:

**k**×(**k**×**E₀**) = −|**k**|²**E₀**
= ω **k**×**B₀** = −(ω²/c²)**E₀**.

For a nonzero field, ω²=c²|**k**|². The positive-frequency branch has ω=c|**k**|, and

**B₀**=(**k**×**E₀**)/ω,  |**B₀**|=|**E₀**|/c.

## Poynting theorem

Dot **E** into Ampère–Maxwell and **B**/μ₀ into Faraday’s law, then use

∇·(**E**×**B**) = **B**·(∇×**E**) − **E**·(∇×**B**).

After collecting time derivatives,

∂t[(ε₀|**E**|²+|**B**|²/μ₀)/2]
+ ∇·[(**E**×**B**)/μ₀] = −**J**·**E**.

In the source-free region the right-hand side is zero. Integrating over a fixed volume and applying the divergence theorem gives the energy change as the negative outward Poynting flux, provided the fields are regular enough and the boundary flux is defined.
