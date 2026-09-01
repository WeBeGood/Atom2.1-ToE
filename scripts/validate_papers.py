#!/usr/bin/env python3
"""Validate the durable human-readable paper convention."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Set

import yaml

REPO = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO / "papers"
NODES_DIR = REPO / "nodes"

REQUIRED_META = ("paper_id", "title", "status", "updated_utc")
REQUIRED_ARTIFACTS = ("readable", "latex", "bibliography", "outline")
REQUIRED_HEADINGS = (
    "## Abstract",
    "## Keywords",
    "## 1. Introduction and Research Question",
    "## 2. Background",
    "## 3. Methods and Reproducibility",
    "## 4. Results",
    "## 5. Discussion",
    "## 6. Limitations and Scope",
    "## 7. Conclusion",
    "## Data and Code Availability",
    "## Author Contributions",
    "## Acknowledgments",
    "## Declarations",
    "## References",
    "## Version and Provenance",
)


def fail(message: str) -> None:
    raise SystemExit(f"PAPER VALIDATION FAILED: {message}")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_nodes() -> Dict[str, dict]:
    nodes: Dict[str, dict] = {}
    for path in sorted(NODES_DIR.glob("N*/node.yaml")):
        data = load_yaml(path)
        node_id = str((data.get("meta") or {}).get("id", "")).strip()
        if node_id:
            nodes[node_id] = data
    return nodes


def validate_paper(path: Path, nodes: Dict[str, dict]) -> Set[str]:
    paper = load_yaml(path)
    meta = paper.get("meta")
    if not isinstance(meta, dict):
        fail(f"{path}: meta mapping required")
    for key in REQUIRED_META:
        if not str(meta.get(key, "")).strip():
            fail(f"{path}: meta.{key} is required")

    if not path.parent.name.startswith(str(meta["paper_id"])):
        fail(f"{path}: directory must begin with paper_id {meta['paper_id']}")

    artifacts = paper.get("artifacts")
    if not isinstance(artifacts, dict):
        fail(f"{path}: artifacts mapping required")
    for key in REQUIRED_ARTIFACTS:
        relative = str(artifacts.get(key, "")).strip()
        if not relative:
            fail(f"{path}: artifacts.{key} is required")
        artifact = REPO / relative
        if not artifact.exists():
            fail(f"{path}: missing artifacts.{key} file {relative}")

    readable = (REPO / str(artifacts["readable"])).read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        if heading not in readable:
            fail(f"{artifacts['readable']}: missing heading {heading!r}")
    if "[Author" not in readable or "[Affiliation" not in readable:
        fail(f"{artifacts['readable']}: transparent author/affiliation placeholders required")

    sections = paper.get("sections")
    if not isinstance(sections, list) or not sections:
        fail(f"{path}: non-empty sections list required")
    section_ids: Set[str] = set()
    mapped: Set[str] = set()
    for section in sections:
        if not isinstance(section, dict):
            fail(f"{path}: each section must be a mapping")
        section_id = str(section.get("id", "")).strip()
        title = str(section.get("title", "")).strip()
        node_ids = section.get("nodes")
        if not section_id or not title or not isinstance(node_ids, list):
            fail(f"{path}: each section requires id, title, and nodes list")
        if section_id in section_ids:
            fail(f"{path}: duplicate section id {section_id}")
        section_ids.add(section_id)
        for node_id in node_ids:
            if node_id not in nodes:
                fail(f"{path}: section {section_id} references unknown node {node_id}")
            mapped.add(str(node_id))
    return mapped


def main() -> int:
    nodes = load_nodes()
    paper_files = sorted(PAPERS_DIR.glob("P*/paper.yaml"))
    if not paper_files:
        fail("no papers/P*/paper.yaml files found")

    mapped: Set[str] = set()
    for path in paper_files:
        mapped.update(validate_paper(path, nodes))

    mature = {
        node_id
        for node_id, node in nodes.items()
        if str((node.get("meta") or {}).get("maturity", "")) in {"M3", "M4", "M5"}
    }
    missing = sorted(mature - mapped)
    if missing:
        fail("M3+ nodes missing from all paper mappings: " + ", ".join(missing))

    print(f"OK: validated {len(paper_files)} paper(s); mapped {len(mapped)} node(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
