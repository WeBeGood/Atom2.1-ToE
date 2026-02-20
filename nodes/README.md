# Nodes

Each node is a self-contained unit of the Atom 2.1 derivation graph.

Recommended contents per node folder:
- node.yaml (metadata, claims, dependencies, artifacts)
- narrative.md (human-readable physics derivation)
- math/ (parallel math tracks)
- latex/ (paper-quality slice)
- code/ (reproducible sims/checks)

Nodes declare depends_on to form a derivation DAG.
