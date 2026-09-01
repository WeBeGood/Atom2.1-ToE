import importlib.util
import math
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
N015 = REPO / "nodes" / "N015_trinity_phase_lock_seed_event"


def load_sim():
    path = N015 / "code" / "sim.py"
    spec = importlib.util.spec_from_file_location("n015_sim", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_trinity_geometry_and_phase_observables():
    sim = load_sim()
    checks = sim.verify_baseline()
    assert len(checks) == 14
    assert all(checks.values()), [name for name, passed in checks.items() if not passed]

    trinity = sim.observables(2.0 * math.pi / 3.0)
    assert math.isclose(trinity["energy_density"], 7.0 / 8.0, rel_tol=2e-15)
    assert math.isclose(sim.norm(trinity["poynting"]), 0.5, rel_tol=2e-15)
    assert math.isclose(trinity["invariant_1"], -3.0 / 4.0, rel_tol=2e-15)
    assert not math.isclose(sim.energy_phase_derivative(sim.TRINITY_PHASE), 0.0, abs_tol=1e-12)


def test_n015_sim_reports_standard_interference_boundary():
    sim = N015 / "code" / "sim.py"
    result = subprocess.run([sys.executable, str(sim)], cwd=REPO, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    output = result.stdout + result.stderr
    assert output.count("PASS:") == 14
    assert "FAIL:" not in output
    assert "relative phase delta is independent" in output
    assert "no new photon or neutrino is derived" in output


def test_n015_metadata_separates_standard_result_from_hypothesis():
    node = yaml.safe_load((N015 / "node.yaml").read_text(encoding="utf-8"))
    assert node["meta"]["maturity"] == "M3"
    assert node["scope"]["classification"] == "mixed_standard_result_and_project_hypothesis"
    assert "interference" in node["scope"]["standard_result"]
    assert "not derived" in node["scope"]["project_hypothesis"]
    assert any("CMB" in item for item in node["scope"]["excludes"])

    statements = " ".join(claim["statement"] for claim in node["claims"])
    assert "Gamma=120 degrees is not an extremum" in statements
    assert "not evidence for a new photon or neutrino" in statements


def test_readable_trinity_paper_reports_negative_maxwell_result():
    paper = (REPO / "papers" / "P002_trinity_vector_baseline" / "paper.md").read_text(encoding="utf-8")
    assert "crossing angle and a controllable relative phase are treated as independent" in paper
    assert "neither quantity has a phase extremum there" in paper
    assert "does not create a new independent photon" in paper
    assert "No CMB photon field" in paper
    assert "**Figure 1.**" in paper
    assert "**Table 1." in paper
