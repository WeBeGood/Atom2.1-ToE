# Atom 2.1 Workspace Index

## Canonical source of truth
- **Atom2.1_superseed.yaml** is the single source of truth.
- CI enforces that rendered outputs match SuperSeed (render + `git diff --exit-code`).

## Core workspace files
- `manifest.yaml` — file list + load order
- `Atom2.1_seed_latest.yaml` — axioms/primitives snapshot (rendered)
- `derived_ledger.yaml` — settled vs open items (rendered)
- `active_state_pointer.yaml` — next_focus + open issues (rendered)
- `frontier.yaml` — questions/tasks queue (rendered)

## What to run
- Validate: `python validate_atom2_1.py`
- Render from SuperSeed: `python render_superseed.py`

## Clipboard helpers (Windows)
- `grab_bootstrap.bat` — copies INIT + SuperSeed + confirm-loaded + end-of-session steps
- `grab_superseed.bat` — copies SuperSeed only
- `grab_patch_spec.bat` — copies PATCH_SPEC.md

## Apply an LLM patch bundle
- Double-click `paste_patch.bat`
- Paste JSON patch bundle
- Press **Enter**, then **Ctrl+Z**, then **Enter**

## Notes
- Prefer LLM edits to **Atom2.1_superseed.yaml**; the agent auto-renders when SuperSeed changes.
- Keep derivations as separate docs (e.g., `derivations/`) and reference them from the ledger when ready.
