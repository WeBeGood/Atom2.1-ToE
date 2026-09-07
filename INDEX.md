# Atom 2.1 Workspace Index

## Canonical source of truth
- **Atom2.1_superseed.yaml** is the single source of truth.
- CI enforces that rendered outputs match SuperSeed (render + `git diff --exit-code`).
- **Regime convention:** unless a section explicitly says Superluminal Realm, treat Atom 2.1 math as **Mach-1 Luminal Realm** math with `c=1`.

## Core workspace files
- `manifest.yaml` — file list + load order
- `Atom2.1_seed_latest.yaml` — axioms/primitives snapshot (rendered)
- `derived_ledger.yaml` — settled vs open items (rendered)
- `active_state_pointer.yaml` — next_focus + open issues (rendered)
- `frontier.yaml` — questions/tasks queue (rendered)

## Canonical regime split
- **Luminal Realm:** developed core of Atom 2.1; `c=1`, Mach 1, waves following waves in the BBRV photon/CMB sea; `E=mc^2` is handled as `E=m` in natural units.
- **Superluminal Realm:** open future branch; Mach>1 to Mach infinity, incidence angles 120° to 180°, superluminal-looking geometric/phase-channel artifacts, not ordinary energy traveling faster than `c`.
- **120° Trinity Addition:** retained as the first Mach-1 Luminal threshold; older 120°-only wording should be read as Luminal-Realm shorthand, not as a complete tired-light or Superluminal-Realm derivation.

## Node graph (derivation DAG)
- `nodes/` — derivation nodes (each has `node.yaml`, narrative, math tracks, LaTeX slices, and code)
  - `nodes/N000_space_time_light_maxwell/` — **Classical electromagnetism in vacuum (Maxwell baseline)**

## Human-readable papers
- `papers/README.md` — durable manuscript convention and required scientific-paper sections
- `papers/P001_foundations/paper.md` — readable standard Maxwell foundation
- `papers/P002_trinity_vector_baseline/paper.md` — 120° two-wave vector derivation and hypothesis boundary
- `papers/P*/paper.yaml` — node-to-section mappings used to generate each `outline.md`

## What to run
- Validate: `python validate_atom2_1.py`
- Validate nodes: `python scripts/validate_nodes.py`
- Validate readable papers: `python scripts/validate_papers.py`
- Regenerate node and paper artifacts: `regen_nodes.bat` (Windows) or `regen_nodes.sh`
- Render from SuperSeed: `python render_superseed.py`

## Clipboard helpers (Windows)
- `grab_bootstrap.bat` — copies INIT + SuperSeed + PATCH_SPEC + reminders
- `grab_superseed.bat` — copies SuperSeed only
- `grab_patch_spec.bat` — copies PATCH_SPEC.md

## Apply an LLM patch bundle
- Double-click `paste_patch.bat`
- Paste JSON patch bundle
- Press **Enter**, then **Ctrl+Z**, then **Enter**

## Notes
- Prefer edits to **Atom2.1_superseed.yaml**; the agent auto-renders when SuperSeed changes.
- Nodes should declare `depends_on` so we can generate an ordered tree/graph.
