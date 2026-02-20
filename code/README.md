# Code Conventions (Atom 2.1)

## Goals
- Reproducible simulations and checks per node
- Minimal dependencies by default
- Expand to heavier physics stacks only when needed

## Recommended Python stack
Baseline (common, LLM-friendly):
- numpy, scipy
- sympy (symbolic derivations / simplification)
- matplotlib (plots)

Optional PDE / field simulation stacks:
- FEniCS / FEniCSx (finite element PDE)
- MEEP (FDTD electromagnetics)
- FiPy (finite volume PDE)

## Structure
For a node with computation:
- `nodes/<node>/code/sim.py` — CLI runnable, deterministic output
- `nodes/<node>/code/notebooks/` — exploratory notebooks (optional)
- `nodes/<node>/figs/` — generated plots (commit only key figures)

## Rules
- Scripts should run from repo root using relative paths.
- Prefer writing files with UTF-8 and LF newlines.
- Keep runtime under ~10s for CI smoke tests.
- Add a small pytest-based smoke test when a new sim is introduced.
