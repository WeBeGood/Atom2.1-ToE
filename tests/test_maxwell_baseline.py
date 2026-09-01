import importlib.util
import math
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
N000 = REPO / "nodes" / "N000_space_time_light_maxwell"


def load_sim():
    path = N000 / "code" / "sim.py"
    spec = importlib.util.spec_from_file_location("n000_sim", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_si_constants_and_plane_wave_identities():
    sim = load_sim()
    assert sim.C == 299_792_458.0
    assert math.isclose(sim.MU0, 1.256_637_061_27e-6, rel_tol=0.0, abs_tol=0.0)
    assert math.isclose(sim.EPS0, 8.854_187_8188e-12, rel_tol=2e-11)
    checks = sim.verify_baseline()
    assert checks
    assert all(checks.values()), [name for name, passed in checks.items() if not passed]


def test_n000_declares_scope_and_verification_boundary():
    node = yaml.safe_load((N000 / "node.yaml").read_text(encoding="utf-8"))
    assert node["scope"]["classification"] == "standard_electromagnetism"
    assert node["scope"]["excludes"]
    assert node["meta"]["maturity"] == "M3"

    claim_ids = {claim["id"] for claim in node["claims"]}
    assert claim_ids == {"N000-C1", "N000-C2", "N000-C3", "N000-C4", "N000-C5"}
    assert any("do not establish" in claim["statement"] for claim in node["claims"])

    validation = node["validation"]
    assert any("tests/test_maxwell_baseline.py" in check for check in validation["checks"])
    assert any("would not by itself validate Atom 2.1" in item for item in validation["falsifiers"])


def test_forms_node_uses_unit_aware_equations_and_correct_topology_condition():
    path = REPO / "nodes" / "N010_maxwell_differential_forms" / "node.yaml"
    node = yaml.safe_load(path.read_text(encoding="utf-8"))
    statements = " ".join(claim["statement"] for claim in node["claims"])
    exports = " ".join(node["interfaces"]["exports"])

    assert node["scope"]["classification"] == "standard_electromagnetism"
    assert "dHcal=Jcal" in exports
    assert "contractible" in statements
    assert "H^2_dR" in statements
    assert "simple connectedness alone is not" in statements


def test_polarization_node_fixes_helicity_convention_and_scope():
    path = REPO / "nodes" / "N011_polarization_helicity_chirality" / "node.yaml"
    node = yaml.safe_load(path.read_text(encoding="utf-8"))
    statements = " ".join(claim["statement"] for claim in node["claims"])

    assert node["scope"]["classification"] == "standard_electromagnetism"
    assert "i khat cross e_sigma=sigma e_sigma" in statements
    assert "do not by themselves establish" in statements


def test_paper_keeps_standard_and_hypothesis_sections_separate():
    path = REPO / "papers" / "P001_foundations" / "paper.yaml"
    paper = yaml.safe_load(path.read_text(encoding="utf-8"))
    sections = {section["id"]: section for section in paper["sections"]}

    assert sections["S2"]["nodes"] == ["N000", "N010", "N011"]
    assert "Standard" in sections["S2"]["title"]
    assert "Hypotheses" in sections["S3"]["title"]
    assert set(sections["S2"]["nodes"]).isdisjoint(sections["S3"]["nodes"])
