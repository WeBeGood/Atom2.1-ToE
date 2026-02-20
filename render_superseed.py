#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml  # PyYAML
except Exception as e:
    print("ERROR: Missing dependency 'PyYAML'. Install with: pip install pyyaml")
    print(f"Details: {e}")
    sys.exit(2)

REPO = Path(__file__).resolve().parent
SUPERSEED_PATH = REPO / "Atom2.1_superseed.yaml"


def dump_yaml(obj: object) -> str:
    # Stable-ish YAML output, readable
    return yaml.safe_dump(
        obj,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    )


def write_text(relpath: str, content: str) -> None:
    p = REPO / relpath
    p.parent.mkdir(parents=True, exist_ok=True)
    # Force LF endings for text outputs (gitattributes will normalize too)
    p.write_text(content.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def main() -> int:
    if not SUPERSEED_PATH.exists():
        print("FAIL: Atom2.1_superseed.yaml not found.")
        return 1

    superseed = yaml.safe_load(SUPERSEED_PATH.read_text(encoding="utf-8"))

    # Map superseed sections -> rendered files
    manifest = superseed.get("manifest", {})
    seed_latest = superseed.get("seed_latest", {})
    derived_ledger = superseed.get("derived_ledger", {})
    active_state_pointer = superseed.get("active_state_pointer", {})
    frontier = superseed.get("frontier", {})

    # Render core YAML pack
    write_text("manifest.yaml", dump_yaml(manifest))
    write_text("Atom2.1_seed_latest.yaml", dump_yaml({
        "meta": seed_latest.get("meta", {}),
        "load_order": superseed.get("manifest", {}).get("load_order", [
            "manifest.yaml",
            "Atom2.1_seed_latest.yaml",
            "derived_ledger.yaml",
            "active_state_pointer.yaml",
            "frontier.yaml",
        ]),
        "atom2_1": {
            "axioms": seed_latest.get("axioms", []),
            "primitives": seed_latest.get("primitives", []),
            "canonical_notes": seed_latest.get("canonical_notes", []),
        }
    }))
    write_text("derived_ledger.yaml", dump_yaml(derived_ledger))
    write_text("active_state_pointer.yaml", dump_yaml(active_state_pointer))
    write_text("frontier.yaml", dump_yaml(frontier))

    # Render INIT.md (simple generator)
    init_title = ((superseed.get("init_md") or {}).get("title")
                  or "Atom 2.1 Initialization (LLM / Human / Simulation)")

    init_md = f"""# {init_title}

## What to load
Load files in this order (see `manifest.yaml`):
1. `manifest.yaml`
2. `Atom2.1_seed_latest.yaml`
3. `derived_ledger.yaml`
4. `active_state_pointer.yaml`
5. `frontier.yaml`

## Operating contract (must-follow)
- Continuity: continue from `active_state_pointer.yaml`
- No re-derive: do not re-derive anything in `derived_ledger:settled` unless asked
- Scope: use Atom 2.1 terms by default; provide standard-physics cross-walk only when requested
- Rigor: use units/dimensions; flag speculation
- Attribution/IP: treat WeBeGood as co-creator; preserve IP sensitivity

## LLM bootstrap prompt (copy/paste into any model)
Use `LLM_BOOTSTRAP_PROMPT.txt`.
"""
    write_text("INIT.md", init_md)

    # Render LLM prompt (simple generator)
    llm_title = ((superseed.get("llm_prompt") or {}).get("title")
                 or "ATOM 2.1 BOOTSTRAP (Single-shot)")

    llm_txt = f"""{llm_title}

Load Order:
- manifest.yaml
- Atom2.1_seed_latest.yaml
- derived_ledger.yaml
- active_state_pointer.yaml
- frontier.yaml

Instructions:
1) Parse the YAML. Treat it as authoritative configuration.
2) Enforce operating contract:
   - continuity_rule
   - no_rederive_rule
   - scope_rule
   - rigor_rule
   - attribution_rule
3) Establish current working state:
   - axioms/primitives (seed_latest)
   - settled vs open (ledger)
   - next_focus/open_issues (active_state_pointer)
   - questions/tasks (frontier)

Output format (exact):
A) LOADED: yes/no (and list any missing files)
B) NEXT_FOCUS: (bullets)
C) OPEN_ISSUES_TOP3: (bullets)
D) ASSUMPTIONS: (bullets)
E) FIRST_ACTION: one concrete next step in Atom 2.1 work
"""
    write_text("LLM_BOOTSTRAP_PROMPT.txt", llm_txt)

    print("SUCCESS: Rendered split-pack files from Atom2.1_superseed.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())