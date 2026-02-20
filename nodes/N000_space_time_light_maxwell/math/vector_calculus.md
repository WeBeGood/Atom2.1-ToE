# N000 Math Track — Vector Calculus Derivation (Vacuum)

## Operators (Cartesian)
Let ∇ = (∂/∂x, ∂/∂y, ∂/∂z).
- Divergence: ∇·F
- Curl: ∇×F
- Laplacian: ∇²F = ∇(∇·F) − ∇×(∇×F)

Vector identity used:

∇×(∇×E) = ∇(∇·E) − ∇²E

## Maxwell (vacuum)
∇·E = 0
∇·B = 0
∇×E = −∂B/∂t
∇×B = μ0 ε0 ∂E/∂t

## Wave equation for E
Start with Faraday:

∇×E = −∂B/∂t

Take curl of both sides:

∇×(∇×E) = −∂/∂t (∇×B)

Substitute Ampère–Maxwell:

∇×(∇×E) = −∂/∂t (μ0 ε0 ∂E/∂t) = −μ0 ε0 ∂²E/∂t²

Use identity and Gauss (∇·E=0):

∇(∇·E) − ∇²E = −μ0 ε0 ∂²E/∂t²

0 − ∇²E = −μ0 ε0 ∂²E/∂t²

∇²E = μ0 ε0 ∂²E/∂t²

Similarly for B:

∇²B = μ0 ε0 ∂²B/∂t²

## Speed
Compare with ∇²E = (1/c²) ∂²E/∂t², hence

c = 1/√(μ0 ε0)
