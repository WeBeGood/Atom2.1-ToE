#!/usr/bin/env python3
"""Generate deterministic outlines for every papers/P*/paper.yaml manuscript."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

REPO = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO / "papers"
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


def build_outline(paper_yaml: Path, nodes: Dict[str, dict]) -> Path:
    paper = load_yaml(paper_yaml)
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

    configured = (paper.get("artifacts") or {}).get("outline")
    out_md = REPO / configured if configured else paper_yaml.parent / "outline.md"
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return out_md


def main() -> int:
    nodes = load_nodes()
    paper_files = sorted(PAPERS_DIR.glob("P*/paper.yaml"))
    if not paper_files:
        print("OK: no paper.yaml files")
        return 0

    for paper_yaml in paper_files:
        out_md = build_outline(paper_yaml, nodes)
        print(f"WROTE: {out_md.relative_to(REPO)}")

    print(f"WROTE: outlines for {len(paper_files)} paper(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
