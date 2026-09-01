# P002 — Trinity Vector Baseline

This directory contains the human-readable scientific paper for the first Atom 2.1 two-wave construction: two identical coherent vacuum plane-wave modes crossing at 120° with an independently controllable phase.

## Files

- `paper.yaml` — section-to-node mapping and artifact metadata.
- `paper.md` — canonical readable manuscript.
- `main.tex` — LaTeX counterpart.
- `refs.bib` — established references.
- `outline.md` — generated section map.

## Scope

The derivation is classical and vector based. It does not model a CMB field, QED, nonlinear interactions, or charge-only/magnetic-only propagating waves. “Neutrino seed” appears only as an explicitly unverified Atom 2.1 interpretation.

## Reproduce

```text
python nodes/N015_trinity_phase_lock_seed_event/code/sim.py
python scripts/build_paper_outline.py
python scripts/validate_papers.py
python -m pytest -q
```

The repository-wide readable-paper contract is in `papers/README.md`.
