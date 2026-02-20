#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    import yaml  # PyYAML
except Exception as e:
    print("ERROR: Missing dependency 'PyYAML'.\n"
          "Install:  pip install pyyaml\n"
          f"Details: {e}")
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent

REQUIRED = [
    "manifest.yaml",
    "Atom2.1_seed_latest.yaml",
    "derived_ledger.yaml",
    "active_state_pointer.yaml",
    "frontier.yaml",
    "INIT.md",
    "LLM_BOOTSTRAP_PROMPT.txt",
    "Atom2.1_superseed.yaml",
]

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def fail(msg: str, code: int = 1) -> None:
    print(f"FAIL: {msg}")
    sys.exit(code)

def ok(msg: str) -> None:
    print(f"OK: {msg}")

def main() -> int:
    # 1) File existence
    missing = [p for p in REQUIRED if not (REPO_ROOT / p).exists()]
    if missing:
        fail("Missing required files:\n  - " + "\n  - ".join(missing))

    ok("All required files exist.")

    # 2) Parse YAMLs
    manifest = load_yaml(REPO_ROOT / "manifest.yaml")
    seed = load_yaml(REPO_ROOT / "Atom2.1_seed_latest.yaml")
    ledger = load_yaml(REPO_ROOT / "derived_ledger.yaml")
    state = load_yaml(REPO_ROOT / "active_state_pointer.yaml")
    frontier = load_yaml(REPO_ROOT / "frontier.yaml")
    superseed = load_yaml(REPO_ROOT / "Atom2.1_superseed.yaml")

    ok("All YAML files parse via safe_load().")

    # 3) Manifest consistency checks
    mf_files = manifest.get("files", [])
    mf_paths = [x.get("path") for x in mf_files if isinstance(x, dict)]
    load_order = manifest.get("load_order", [])

    if not load_order:
        fail("manifest.yaml has no load_order.")

    for p in load_order:
        if p not in mf_paths and p != "manifest.yaml":
            fail(f"manifest.yaml load_order includes '{p}' but it is not listed under manifest.files[].path")

    ok("manifest.yaml load_order is consistent with manifest.files[].path")

    # 4) SuperSeed output consistency (light check)
    outputs = (superseed.get("outputs") or {}).get("files") or []
    out_paths = [x.get("path") for x in outputs if isinstance(x, dict)]
    for p in ["manifest.yaml", "Atom2.1_seed_latest.yaml", "derived_ledger.yaml", "active_state_pointer.yaml", "frontier.yaml"]:
        if p not in out_paths:
            fail(f"Atom2.1_superseed.yaml outputs.files missing '{p}'")

    ok("Atom2.1_superseed.yaml outputs.files contains core pack outputs.")

    # 5) Quick schema presence (non-strict)
    for name, obj in [("seed", seed), ("ledger", ledger), ("state", state), ("frontier", frontier)]:
        meta = obj.get("meta", {})
        if "schema" not in meta:
            fail(f"{name} YAML missing meta.schema")

    ok("All core YAMLs include meta.schema.")

    print("\nSUCCESS: Atom 2.1 bootstrap pack validates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())