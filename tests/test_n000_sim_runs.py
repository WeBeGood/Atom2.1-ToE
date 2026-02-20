import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_n000_sim_runs():
    sim = REPO / "nodes" / "N000_space_time_light_maxwell" / "code" / "sim.py"
    assert sim.exists(), "N000 sim.py missing"

    r = subprocess.run([sys.executable, str(sim)], cwd=REPO, text=True, capture_output=True)
    assert r.returncode == 0, f"sim.py failed: {r.stderr}"
    out = (r.stdout or "") + (r.stderr or "")
    assert "N000 Maxwell baseline" in out
    assert "c=" in out
