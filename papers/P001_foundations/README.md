# P001 — Foundations

This paper is assembled from Atom 2.1 derivation nodes.

## Files
- `paper.yaml` — section plan + node mapping
- `paper.md` — canonical human-readable Maxwell foundations manuscript
- `main.tex` — LaTeX counterpart
- `refs.bib` — manuscript bibliography
- `outline.md` — auto-generated outline from `paper.yaml` + node metadata

## Build (manual)
- Edit `paper.yaml` to map nodes to sections.
- Run: `python scripts/build_paper_outline.py`
- Compile LaTeX (optional): use your preferred LaTeX toolchain.

## Principle
Nodes remain the source of truth for derivations; papers are curated assemblies.
The repository-wide manuscript contract is documented in `papers/README.md`.
