# Atom 2.1 Initialization (LLM / Human / Simulation)

## What to load
Load files in this order (see `manifest.yaml`):
1. `manifest.yaml`
2. `Atom2.1_seed_latest.yaml`
3. `derived_ledger.yaml`
4. `active_state_pointer.yaml`
5. `frontier.yaml`
6. `distributed_research.yaml`
7. `research_map.yaml`

## Operating contract (must-follow)
- continuity_rule: Continue from active_state_pointer; do not restart from scratch.
- no_rederive_rule: Do not re-derive items listed in derived_ledger:settled unless explicitly requested.
- scope_rule: Stay inside Atom 2.1 vocabulary unless user asks for cross-walk to standard physics.
- rigor_rule: Use units, dimensions, and explicit assumptions; flag speculation.
- attribution_rule: Treat WeBeGood as co-creator; preserve IP sensitivity.
- regime_rule: Default Atom 2.1 discussions to the Mach-1 Luminal Realm with c=1 unless the user explicitly enters the Mach>1 Superluminal Realm.
- cooperation_rule: Load distributed_research.yaml; preserve auditable session handoffs and use reviewed task assignments.
- evidence_rule: New results remain derived_proposed until reviewed; distinguish project conventions, conditional proofs, and empirical support.
- authorization_rule: Use authorized compute and channels; preserve outputs, honor shutdown, and never obtain access by evading controls.

## Cooperative work
Read `CONTRIBUTING.md` and `cooperation/README.md`. Select a bounded task from
`cooperation/tasks.yaml`, load its dependencies and latest verified handoff,
and save reproducible evidence before ending the session. New sessions may
continue saved work; these files do not start background processes.

## LLM bootstrap prompt (copy/paste into any model)
Use `LLM_BOOTSTRAP_PROMPT.txt`.
