# N010 — Maxwell in differential forms (topology-ready)

## Purpose
Rewrite Maxwell’s equations in a **coordinate-free geometric form** to make topology/geometry first-class citizens. This sets up later Atom 2.1 work where topology (knots/braids/chirality) becomes fundamental.

## Core idea
Instead of treating **E** and **B** as separate 3-vectors, package them into a single object on spacetime: the **field strength 2-form** F.

Maxwell becomes:
- **dF = 0**  (homogeneous equations)
- **d⋆F = J** (inhomogeneous equations; J=0 in vacuum)

## Topology hook
- dF=0 implies **local** existence of a potential 1-form A such that **F=dA**.
- Globally, topology can obstruct a single global A (nontrivial cohomology). This is the natural place to connect EM to topological structure.

## Atom 2.1 handoff
This node provides the clean bridge from Maxwell’s baseline (N000) to:
- topology-first descriptions (helicity, chirality, knot/link constraints)
- quantization-ready representations (A, gauge structure)
