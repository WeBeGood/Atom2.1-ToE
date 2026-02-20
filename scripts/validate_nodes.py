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

REQUIRED_META = ["id", "title", "status"]


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
