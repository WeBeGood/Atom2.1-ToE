#!/usr/bin/env python3
"""Generate claims.md for each node from node.yaml.

Writes:
- nodes/<node>/claims.md

Deterministic output for CI.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

import yaml

REPO = Path(__file__).resolve().parents[1]
NODES_DIR = REPO / "nodes"


def load_yaml(p: Path) -> dict:
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def make_claims_md(node_id: str, title: str, claims: List[dict]) -> str:
    lines: List[str] = []
    lines.append(f"# {node_id} Claims — {title}")
    lines.append("")
    lines.append("Generated from `node.yaml` by `scripts/build_node_claims.py`. Commit this file.")
    lines.append("")

    if not claims:
        lines.append("(No claims listed.)")
        lines.append("")
        return "\n".join(lines) + "\n"

    lines.append("| Claim ID | Statement | Units |")
    lines.append("|---|---|---|")
    for c in claims:
        cid = str(c.get("id", "")).strip()
        stmt = str(c.get("statement", "")).strip().replace("\n", " ")
        units = str(c.get("units", "")).strip().replace("\n", " ")
        # Escape pipes for markdown table
        stmt = stmt.replace("|", "\\|")
        units = units.replace("|", "\\|")
        lines.append(f"| {cid} | {stmt} | {units} |")

    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    if not NODES_DIR.exists():
        print("OK: no nodes/")
        return 0

    count = 0
    for node_yaml in sorted(NODES_DIR.glob("N*/node.yaml")):
        data = load_yaml(node_yaml)
        meta = data.get("meta", {})
        node_id = str(meta.get("id", "")).strip()
        title = str(meta.get("title", "")).strip()
        claims = data.get("claims", []) or []

        out = node_yaml.parent / "claims.md"
        out.write_text(make_claims_md(node_id, title, claims), encoding="utf-8", newline="\n")
        count += 1

    print(f"WROTE: claims.md for {count} node(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
