from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[1]
NODES_DIR = REPO / "nodes"


def test_nodes_exist_and_parse():
    assert NODES_DIR.exists(), "nodes/ directory missing"
    node_files = sorted(NODES_DIR.glob("N*/node.yaml"))
    assert node_files, "No nodes found (N*/node.yaml)"

    for p in node_files:
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        meta = data.get("meta", {})
        assert meta.get("id"), f"{p}: meta.id missing"
        assert meta.get("title"), f"{p}: meta.title missing"
        assert meta.get("status"), f"{p}: meta.status missing"

        # claims.md should be present (generated)
        claims_md = p.parent / "claims.md"
        assert claims_md.exists(), f"{p}: claims.md missing"
