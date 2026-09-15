#!/usr/bin/env python3
"""Validate cooperative records and planning DAGs; not a proof checker or scheduler."""
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"{path}: expected mapping")
    return value


def validate_dag(records, label):
    ids = [r["id"] for r in records]
    require(len(ids) == len(set(ids)), f"{label}: duplicate ID")
    graph = {r["id"]: r.get("depends_on", []) for r in records}
    active, done = set(), set()

    def visit(key):
        require(key in graph, f"{label}: unknown dependency {key}")
        require(key not in active, f"{label}: dependency cycle at {key}")
        if key in done:
            return
        active.add(key)
        for dep in graph[key]:
            visit(dep)
        active.remove(key)
        done.add(key)

    for key in graph:
        visit(key)


def artifact_exists(root, ref):
    require(isinstance(ref, str), "artifact reference must be a path string")
    path = (root / ref).resolve()
    require(path.is_relative_to(root.resolve()), f"artifact outside repository: {ref}")
    require(path.is_file(), f"missing artifact: {ref}")


def validate_handoff(record, task_ids, root):
    require(record.get("schema_version") == "1.0", "handoff: unsupported schema version")
    required = ["session_id", "worker_id", "operator_id", "task_id", "base_commit",
                "artifact_commit", "completed", "failed_attempts", "unresolved",
                "assumptions_changed", "artifact_refs", "verification_commands",
                "verification_results", "next_action", "stop_reason"]
    for key in required:
        require(key in record, f"handoff: missing {key}")
    require(record["task_id"] in task_ids, "handoff: unknown task")
    for key in ("session_id", "worker_id", "operator_id", "next_action"):
        require(isinstance(record[key], str) and record[key].strip()
                and "REQUIRED" not in record[key], f"handoff: unresolved {key}")
    for key in ("base_commit", "artifact_commit"):
        require(isinstance(record[key], str) and re.fullmatch(r"[0-9a-f]{40}", record[key]),
                f"handoff: {key} must be a full commit SHA")
    for key in ("completed", "failed_attempts", "unresolved", "assumptions_changed",
                "artifact_refs", "verification_commands", "verification_results"):
        require(isinstance(record[key], list), f"handoff: {key} must be a list")
    require(record["verification_results"], "handoff: record verification or explain why it was not performed")
    require(record["stop_reason"] in {"completed", "blocked", "context_checkpoint",
            "budget_limit", "operator_stop", "infrastructure_failure"}, "handoff: unknown stop reason")
    for ref in record["artifact_refs"]:
        artifact_exists(root, ref)


def validate(root=ROOT):
    source = load(root / "Atom2.1_superseed.yaml")
    for section in ("distributed_research", "research_map"):
        require(load(root / f"{section}.yaml") == source[section], f"stale generated {section}")
        require(f"{section}.yaml" in source["manifest"]["load_order"], f"{section}: missing load instruction")
    for filename in ("INIT.md", "LLM_BOOTSTRAP_PROMPT.txt"):
        text = (root / filename).read_text()
        for key in source["contract"]["rules"]:
            require(key in text, f"{filename}: missing contract rule {key}")

    nodes = {load(p)["meta"]["id"] for p in (root / "nodes").glob("N*/node.yaml")}
    branches = source["research_map"]["branches"]
    validate_dag(branches, "branches")
    branch_ids = {r["id"] for r in branches}
    task_doc = load(root / "cooperation/tasks.yaml")
    require(task_doc.get("schema_version") == "1.0", "unsupported task schema")
    tasks = task_doc["tasks"]
    validate_dag(tasks, "tasks")
    task_ids = {r["id"] for r in tasks}
    for record in branches + tasks:
        require(set(record["node_refs"]) <= nodes, f"{record['id']}: unknown node")
    for task in tasks:
        for key in ("title", "status", "branch_ref", "assignment", "latest_handoff",
                    "deliverable", "acceptance_criteria", "budget", "history"):
            require(key in task, f"{task['id']}: missing {key}")
        require(task["branch_ref"] in branch_ids, f"{task['id']}: unknown branch")
        require(task["status"] in {"queued", "active", "blocked", "review", "completed", "cancelled"},
                f"{task['id']}: invalid status")
        require(isinstance(task["acceptance_criteria"], list) and task["acceptance_criteria"],
                f"{task['id']}: missing acceptance criteria")
        assignment = task["assignment"]
        if task["status"] == "active":
            require(isinstance(assignment, dict), f"{task['id']}: active task needs assignment")
        if assignment is not None:
            require(isinstance(assignment, dict) and all(assignment.get(k) for k in
                    ("worker_id", "operator_id", "assigned_at")), f"{task['id']}: incomplete assignment")
        if task["status"] in {"review", "completed"}:
            require(task["latest_handoff"], f"{task['id']}: handoff required")
        if task["latest_handoff"]:
            artifact_exists(root, task["latest_handoff"])
            record = load(root / task["latest_handoff"])
            require(record["task_id"] == task["id"], "handoff belongs to another task")
            validate_handoff(record, task_ids, root)
    session_ids = set()
    for path in (root / "cooperation/sessions").glob("*.yaml"):
        record = load(path)
        validate_handoff(record, task_ids, root)
        require(record["session_id"] not in session_ids, "duplicate session ID")
        session_ids.add(record["session_id"])


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    print("SUCCESS: cooperative contract, research DAGs and handoff references validate.")
