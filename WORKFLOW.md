# Atom 2.1 — Human Workflow Chart

This document is the stable reference for how changes should flow through the Atom 2.1 repository as it grows.

---

## Legend
- **Human** = you editing, deciding, reviewing
- **LLM** = ChatGPT/Claude/etc producing JSON patch bundles
- **Automation (local)** = `paste_patch.bat`, `regen_nodes.bat`
- **Automation (CI)** = GitHub Actions workflows

---

## A. Main “Change Flow”

```text
IDEA / PHYSICS CHANGE (Human)
        |
        v
LLM session initialized (LLM_WORKSPACE_INIT + SuperSeed/Nodes context)
        |
        v
LLM outputs JSON patch (ONLY) following PATCH_SPEC
        |
        v
Apply patch locally (paste_patch.bat)
        |       
        |--> agent_apply.py writes files, validates, commits, pushes
        |
        v
Generate deterministic artifacts locally (regen_nodes.bat)
        |
        v
Commit + push generated artifacts
        |
        v
CI runs (Nodes CI + Tests CI + Atom2.1 CI)
        |
        +--> GREEN: repo consistent + reproducible
        |
        +--> RED: fix mismatch (usually missing generated artifacts or schema rule)
```

---

## B. The “Two Push” Rule (why you sometimes see red)

CI enforces that **generated outputs are committed**. If you push a node change without regenerating locally first, CI will generate artifacts on Linux and fail on `git diff --exit-code`.

Avoid intermediate red by using a single clean cycle:

```text
Patch applied -> regen_nodes.bat -> commit -> push -> CI green
```

---

## C. Fast Path: Normal Daily Workflow (recommended)

### 1) Start an LLM session
1) Run `grab_superseed.bat` (or your preferred helper)
2) Paste `LLM_WORKSPACE_INIT.txt`
3) Paste SuperSeed / relevant node(s)

### 2) Make the change
Ask LLM for a patch bundle:
- “MAKE PATCH”

### 3) Apply change locally
- Double-click `paste_patch.bat`
- Paste JSON
- **Enter → Ctrl+Z → Enter**

### 4) Regenerate artifacts (ALWAYS after node changes)
- Run `regen_nodes.bat`

### 5) Commit + push
```cmd
git add -A
git commit -m "Regenerate artifacts"
git push
```

### 6) Confirm green
- GitHub → Actions → green checks

---

## D. Node Lifecycle (Maturity Model)

```text
Create node skeleton (TEMPLATE)   ---> M0 (outline)
        |
Add definitions + basic derivation ---> M1 (derivation)
        |
Add quantified claims + units      ---> M2 (quantified)
        |
Add code sim + checks              ---> M3 (simulated)
        |
Add falsifiers + validation logic  ---> M4 (falsifiable)
        |
Polish narrative + figures + refs  ---> M5 (publish-ready)
```

**Artifacts expected**
- M0–M1: node.yaml + narrative + math stubs
- M2: real claims + unit sanity + stable exports/imports
- M3: `code/sim.py` does something meaningful + (optional) a smoke test
- M5: figures + LaTeX quality + citations

---

## E. Figures Workflow

Figures are not fully automagic by default; two supported paths are encouraged.

### 1) Reproducible figures (preferred)
```text
code/sim.py -> generates figs/*.png or *.svg -> commit figs + document in figs/README.md
```

### 2) Concept diagrams (image model)
```text
Image model session -> export png/svg -> commit figs + store prompt in figs/README.md (or prompt.txt)
```

---

## F. Paper Assembly Workflow (P001 and future papers)

```text
nodes/ (truth)
   |
   +--> papers/P001_foundations/paper.yaml (node → section mapping)
   |
   +--> scripts/build_paper_outline.py -> papers/P001_foundations/outline.md
   |
   +--> main.tex may include node LaTeX slices when ready
```

This supports:
- assembling papers from nodes
- reordering without rewriting derivations
- creating publication-ready sections by selecting mature nodes

---

## G. “Why did CI go red?” quick triage

Most common causes:

1) **Generated artifacts not committed**
- Fix: run `regen_nodes.bat` → commit → push

2) **Cross-platform determinism mismatch**
- Fix: ensure generators write POSIX paths + LF (already handled by current tooling)

3) **Schema validation failure**
- Look for: `NODE VALIDATION FAILED: ...`
- Common fixes: missing `meta.maturity`, missing `interfaces.exports/imports`, missing narrative file path, missing `claims.md`

---

## H. Human pre-push checklist

- Did you change anything in `nodes/**`?
  - ✅ Run `regen_nodes.bat`
- Did you add a new node?
  - ✅ Ensure narrative exists and artifact paths are correct
- Did you add code?
  - ✅ Keep runtime short for CI
- Did you touch paper mappings?
  - ✅ `regen_nodes.bat` rebuilds paper outline

---

## Convenience Commands

### Apply a patch bundle
- Double-click `paste_patch.bat`
- Paste JSON
- Enter → Ctrl+Z → Enter

### Regenerate artifacts
- Run `regen_nodes.bat`
- Then commit + push
