#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent

def run(cmd: list[str]) -> None:
    r = subprocess.run(cmd, cwd=REPO, text=True)
    if r.returncode != 0:
        raise SystemExit(r.returncode)

def write_file(relpath: str, content: str) -> None:
    path = REPO / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python agent_apply.py <patch.json>")
        print("  python agent_apply.py --stdin")
        return 2

    if sys.argv[1] == "--stdin":
        patch = json.loads(sys.stdin.read())
        patch_path = None
    else:
        patch_path = (REPO / sys.argv[1]).resolve()
        patch = json.loads(patch_path.read_text(encoding="utf-8"))
    message = patch.get("commit_message")
    files = patch.get("files", [])
    if not message or not files:
        print("Patch must include: commit_message, files[]")
        return 2

    for f in files:
        rel = f["path"]
        content = f["content"]
        write_file(rel, content)
        print(f"WROTE: {rel}")

    # Validate
    print("RUN: python validate_atom2_1.py")
    run([sys.executable, "validate_atom2_1.py"])

    # Commit + push
    run(["git", "add", "-A"])
    if patch_path is not None:
        run(["git", "reset", "--", str(patch_path.relative_to(REPO))])
    run(["git", "commit", "-m", message])
    run(["git", "push"])

    print("DONE: applied patch, validated, committed, pushed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())