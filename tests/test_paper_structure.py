import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]


def test_paper_validator_runs():
    script = REPO / "scripts" / "validate_papers.py"
    result = subprocess.run([sys.executable, str(script)], cwd=REPO, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "validated 2 paper(s)" in result.stdout


def test_all_paper_artifacts_exist_and_mapped_nodes_resolve():
    node_ids = {
        yaml.safe_load(path.read_text(encoding="utf-8"))["meta"]["id"]
        for path in (REPO / "nodes").glob("N*/node.yaml")
    }
    for paper_yaml in sorted((REPO / "papers").glob("P*/paper.yaml")):
        paper = yaml.safe_load(paper_yaml.read_text(encoding="utf-8"))
        for relative in paper["artifacts"].values():
            assert (REPO / relative).exists(), relative
        for section in paper["sections"]:
            assert set(section["nodes"]).issubset(node_ids)


def test_every_m3_or_higher_node_has_readable_paper_mapping():
    mature = set()
    for path in (REPO / "nodes").glob("N*/node.yaml"):
        node = yaml.safe_load(path.read_text(encoding="utf-8"))
        if node["meta"]["maturity"] in {"M3", "M4", "M5"}:
            mature.add(node["meta"]["id"])

    mapped = set()
    for path in (REPO / "papers").glob("P*/paper.yaml"):
        paper = yaml.safe_load(path.read_text(encoding="utf-8"))
        for section in paper["sections"]:
            mapped.update(section["nodes"])
    assert mature.issubset(mapped), sorted(mature - mapped)


def test_readable_paper_convention_is_documented():
    convention = (REPO / "papers" / "README.md").read_text(encoding="utf-8")
    assert "canonical human-readable manuscript" in convention
    assert "Standard result" in convention
    assert "Project hypothesis" in convention
    assert "Nodes at M3 or higher" in convention
