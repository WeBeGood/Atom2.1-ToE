"""Catch failures that would strand a new worker or permit false completion."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cooperation_validator", ROOT / "scripts/validate_cooperation.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.mark.parametrize("records, message", [
    ([{"id": "A", "depends_on": ["B"]}], "unknown dependency"),
    ([{"id": "A", "depends_on": ["B"]}, {"id": "B", "depends_on": ["A"]}], "cycle"),
    ([{"id": "A"}, {"id": "A"}], "duplicate"),
])
def test_invalid_work_graph_rejected(records, message):
    with pytest.raises(ValueError, match=message):
        module.validate_dag(records, "tasks")


def test_incomplete_handoff_rejected(tmp_path):
    with pytest.raises(ValueError, match="missing"):
        module.validate_handoff({"schema_version": "1.0", "task_id": "A"}, {"A"}, tmp_path)


def test_artifacts_cannot_escape_repository(tmp_path):
    with pytest.raises(ValueError, match="outside repository"):
        module.artifact_exists(tmp_path, "../outside.txt")


def test_repository_cooperative_contract():
    module.validate(ROOT)


def test_completion_without_handoff_rejected(monkeypatch):
    original_load = module.load

    def load_with_false_completion(path):
        data = original_load(path)
        if path.name == "tasks.yaml":
            data["tasks"][0]["status"] = "completed"
        return data

    monkeypatch.setattr(module, "load", load_with_false_completion)
    with pytest.raises(ValueError, match="handoff required"):
        module.validate(ROOT)


def test_stale_generated_contract_rejected(monkeypatch):
    original_load = module.load

    def load_stale_contract(path):
        data = original_load(path)
        if path.name == "distributed_research.yaml":
            data["mission"]["objective"] = "outdated mission"
        return data

    monkeypatch.setattr(module, "load", load_stale_contract)
    with pytest.raises(ValueError, match="stale generated"):
        module.validate(ROOT)
