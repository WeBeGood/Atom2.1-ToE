#!/usr/bin/env python3
"""Validate node.yaml structure for all nodes.

Goal: keep nodes consistent and CI-enforced.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

import yaml

REPO = Path(__file__).resolve().parents[1]
NODES_DIR = REPO / "nodes"

REQUIRED_META = ["id", "title", "status", "maturity"]


def fail(msg: str) -> None:
    raise SystemExit(f"NODE VALIDATION FAILED: {msg}")


def load_yaml(p: Path) -> dict:
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def validate_node(node_yaml: Path) -> None:
    data = load_yaml(node_yaml)
    meta = data.get("meta")
    if not isinstance(meta, dict):
        fail(f"{node_yaml}: missing meta mapping")

    for k in REQUIRED_META:
        if not str(meta.get(k, "")).strip():
            fail(f"{node_yaml}: meta.{k} is required")

    dep = data.get("depends_on", [])
    if dep is None:
        dep = []
    if not isinstance(dep, list):
        fail(f"{node_yaml}: depends_on must be a list")

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict):
        fail(f"{node_yaml}: artifacts mapping required")

    narrative = artifacts.get("narrative")
    if not str(narrative or "").strip():
        fail(f"{node_yaml}: artifacts.narrative is required")

    # Check referenced narrative exists
    npath = (REPO / str(narrative)).resolve()
    if not npath.exists():
        fail(f"{node_yaml}: missing narrative file {narrative}")

    # Interfaces: exports/imports are required
    interfaces = data.get("interfaces")
    if not isinstance(interfaces, dict):
        fail(f"{node_yaml}: interfaces mapping required")

    exports = interfaces.get("exports")
    imports = interfaces.get("imports")
    if exports is None or not isinstance(exports, list):
        fail(f"{node_yaml}: interfaces.exports must be a list")
    if imports is None or not isinstance(imports, list):
        fail(f"{node_yaml}: interfaces.imports must be a list")

    # Claims required to be list (can be empty)
    claims = data.get("claims", [])
    if claims is None:
        claims = []
    if not isinstance(claims, list):
        fail(f"{node_yaml}: claims must be a list")

    # If claims exist, each must have id/statement/units
    for c in claims:
        if not isinstance(c, dict):
            fail(f"{node_yaml}: each claim must be a mapping")
        if not str(c.get("id", "")).strip():
            fail(f"{node_yaml}: claim missing id")
        if not str(c.get("statement", "")).strip():
            fail(f"{node_yaml}: claim {c.get('id')} missing statement")
        if c.get("units") is None:
            fail(f"{node_yaml}: claim {c.get('id')} missing units")

    # claims.md must exist (generated)
    claims_md = node_yaml.parent / "claims.md"
    if not claims_md.exists():
        fail(f"{node_yaml}: missing generated {claims_md.relative_to(REPO)}")


def main() -> int:
    if not NODES_DIR.exists():
        print("OK: no nodes/ directory")
        return 0

    node_files: List[Path] = sorted(NODES_DIR.glob("N*/node.yaml"))
    if not node_files:
        print("OK: no node.yaml files")
        return 0

    for p in node_files:
        validate_node(p)

    print(f"OK: validated {len(node_files)} node(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
