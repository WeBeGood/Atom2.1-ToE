#!/usr/bin/env python3
"""Generate a readable paper outline from paper.yaml and node metadata.

Outputs:
- papers/P001_foundations/outline.md (for now: one paper)

Later: generalize for multiple papers.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

REPO = Path(__file__).resolve().parents[1]
PAPER_DIR = REPO / "papers" / "P001_foundations"
PAPER_YAML = PAPER_DIR / "paper.yaml"
OUT_MD = PAPER_DIR / "outline.md"

NODES_DIR = REPO / "nodes"


def load_yaml(p: Path) -> dict:
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_nodes() -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    for node_yaml in sorted(NODES_DIR.glob("N*/node.yaml")):
        data = load_yaml(node_yaml)
        meta = data.get("meta", {})
        nid = str(meta.get("id", "")).strip()
        if nid:
            out[nid] = data
    return out


def main() -> int:
    paper = load_yaml(PAPER_YAML)
    nodes = load_nodes()

    title = paper.get("meta", {}).get("title", "(untitled)")
    updated = paper.get("meta", {}).get("updated_utc", "")

    lines = []
    lines.append(f"# {title}")
    if updated:
        lines.append(f"\n_Last updated (UTC): {updated}_")
    lines.append("\n## Section map")

    for sec in paper.get("sections", []) or []:
        sid = sec.get("id", "")
        stitle = sec.get("title", "")
        lines.append(f"\n### {sid}: {stitle}")
        nlist = sec.get("nodes", []) or []
        if not nlist:
            lines.append("- Nodes: (none)")
            continue
        lines.append("- Nodes:")
        for nid in nlist:
            meta = nodes.get(nid, {}).get("meta", {})
            ntitle = meta.get("title", "(missing)")
            status = meta.get("status", "(unknown)")
            lines.append(f"  - {nid} — {ntitle} (status: {status})")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"WROTE: {OUT_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
