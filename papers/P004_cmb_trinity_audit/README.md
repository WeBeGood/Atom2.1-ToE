# P004 - All-direction CMB/Trinity manuscript

Canonical human-readable source: [paper.md](paper.md). Complete LaTeX counterpart: [main.tex](main.tex). Printable draft: [paper.pdf](paper.pdf). Claims and proofs are mapped in paper.yaml; full derivations are in N016, N019 and N020.

Author/model attribution: Craig Fink / WeBeGood. Final author list, affiliation and declarations remain for the human author. This is an AI-assisted working manuscript, not journal peer review or an empirical neutrino derivation.

Regenerate LaTeX with `python scripts/build_cmb_paper.py` (requires Pandoc). Build PDF from this directory with `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice and copy main.pdf to paper.pdf. The numbered references are included directly in the complete manuscript; refs.bib supplies reusable citation records. No BibTeX pass is required for this rendering.

Run the N016/N019/N020 simulations and `python -m pytest -q` from the repository root. The mathematical results have explicit assumptions; open physics is not hidden behind completed code.
