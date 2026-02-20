# N012 Math Track — Potentials, Gauge, and Wave Equations

## 1) Definitions imply homogeneous Maxwell automatically
Given:
- B = ∇×A
- E = −∇phi − ∂A/∂t

Then:
- ∇·B = ∇·(∇×A) = 0
- ∇×E = ∇×(−∇phi − ∂A/∂t) = −∂(∇×A)/∂t = −∂B/∂t

So Gauss(B) and Faraday are automatically satisfied.

## 2) Gauge freedom
Let Lambda(x,t) be any smooth function.
Define transformed potentials:
- A' = A + ∇Lambda
- phi' = phi − ∂Lambda/∂t

Compute fields:
- B' = ∇×A' = ∇×A + ∇×∇Lambda = B
- E' = −∇phi' − ∂A'/∂t = (−∇phi − ∂A/∂t) + (∇∂Lambda/∂t − ∂∇Lambda/∂t) = E

Thus E,B are invariant.

## 3) Lorenz gauge and wave equations (sketch)
Introduce the Lorenz gauge condition (to be written explicitly in 3+1 form):

(1/c^2) ∂phi/∂t + ∇·A = 0

Then the remaining Maxwell equations yield sourced wave equations for phi and A.
In vacuum (rho=0, J=0):
- (∇^2 − 1/c^2 ∂^2/∂t^2) phi = 0
- (∇^2 − 1/c^2 ∂^2/∂t^2) A = 0
