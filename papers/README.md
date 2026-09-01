# Human-Readable Paper Convention

Every derivation that reaches a testable or paper-facing maturity should have a readable counterpart under `papers/P###_<slug>/`. Nodes remain the granular source of truth; papers explain connected derivations in ordinary scientific prose.

## Required files

Each paper directory contains:

- `paper.yaml` — paper identity, scope, artifact paths, and node-to-section mapping.
- `paper.md` — canonical human-readable manuscript.
- `main.tex` — LaTeX rendition or build-ready counterpart.
- `refs.bib` — bibliography for cited established work.
- `outline.md` — deterministic section map generated from `paper.yaml`.
- `README.md` — local build and scope notes.

## Required manuscript components

Where applicable, `paper.md` includes:

1. title, transparent author/affiliation placeholders, status, and version/provenance;
2. abstract and keywords;
3. introduction with a research question;
4. background separating established results from project hypotheses;
5. methods, assumptions, equations, and reproducibility details;
6. results, with numbered equations plus captioned tables/figures where useful;
7. discussion, limitations/scope, and conclusion;
8. data/code availability;
9. author-contribution and acknowledgment placeholders;
10. funding, conflicts, and ethics declarations as applicable;
11. references to established literature.

If a component does not apply, say so rather than inventing content. Never fabricate authorship, affiliations, funding, experimental data, empirical validation, or conflicts.

## Standard versus hypothesis labels

Each manuscript must identify which statements are:

- **Standard result** — follows from established mathematics or experimentally supported theory under stated assumptions.
- **Project hypothesis** — an Atom 2.1 interpretation, proposed mechanism, or unverified extrapolation.
- **Open test** — a calculation or observation that could support or falsify a hypothesis.

A standard derivation may constrain a project hypothesis, but it must not be presented as evidence for that hypothesis unless a discriminating test has actually been performed.

## Mapping and validation

- Map every paper section to its source nodes in `paper.yaml`.
- Add `artifacts.readable`, `artifacts.latex`, `artifacts.bibliography`, and `artifacts.outline`.
- Run `python scripts/build_paper_outline.py` after paper or node metadata changes.
- Run `python scripts/validate_papers.py` and the repository tests.
- Nodes at M3 or higher must be mapped into at least one paper, so tested derivations do not exist only as machine-facing YAML/code.

## Current papers

- `P001_foundations` — readable standard Maxwell foundation.
- `P002_trinity_vector_baseline` — vector-first 120° two-wave calculation and explicit Atom 2.1 interpretation boundary.

Later CMB, QED, particle, or nonlinear-field papers should be separate manuscripts rather than being folded into the vector-baseline paper.
