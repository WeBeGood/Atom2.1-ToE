# Contributing to Atom 2.1

Humans and AI agents operated with their owners' authorization are welcome to
contribute derivations, counterexamples, calculations, literature mappings and
independent reviews. WeBeGood / Craig Fink is the theory originator. Preserve
authorship and the distinction between his definitions and a contributor's inferences.

1. Load `INIT.md` and the manifest's files. Read the cooperative contract.
2. Select a bounded task from `cooperation/tasks.yaml`, or propose a new one.
   The maintainer records assignments by merging task-record changes. Until
   then, work is a proposal and may overlap another contributor's work.
3. Use a branch or fork. Record the starting commit, task ID, operator, model
   (if applicable), method and resource budget. No credentials belong in records.
4. Read the relevant node and its dependency closure. Reuse settled results
   within their assumptions. Flag contradictions without silently replacing them.
5. Save derivations and reproducible checks in the relevant node; save a session
   handoff in `cooperation/sessions/`. Use the templates in `cooperation/templates/`.
6. Open a pull request identifying the problem, changed claims, assumptions,
   validation, remaining gaps and next action. New results are `derived_proposed`.
7. An independent reviewer checks the evidence. Owner or authorized maintainer
   acceptance controls promotion into the canonical ledger. Contributor consensus
   alone does not establish a physical result.

Project definitions describe Atom 2.1 faithfully. Mathematical proofs establish
only their stated conclusions under their assumptions. Comparing proposed bridges
to modern physics is in scope when the task requests it; it does not silently
replace Atom 2.1 vocabulary. Record unresolved differences in wording explicitly.

Edit canonical sections in `Atom2.1_superseed.yaml`, then run:

```bash
python render_superseed.py
python validate_atom2_1.py
python scripts/validate_cooperation.py
pytest -q
```

Run the relevant node's numerical checks when changing its mathematics or code.
Generated-file synchronization is checked by CI. YAML validation checks structure
and references; it is not mathematical peer review.

See `cooperation/README.md` for the Learning Sessions Loop and `research_map.yaml`
for the open branch map. Participation instructions do not provide compute,
accounts, scheduled execution, or permission to access someone else's systems.
