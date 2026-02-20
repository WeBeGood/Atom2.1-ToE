# Atom 2.1 Initialization (LLM / Human / Simulation)

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
