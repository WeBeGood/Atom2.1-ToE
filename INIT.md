\# Atom 2.1 Initialization (LLM / Human / Simulation)



\## What to load

Load files in this order (see `manifest.yaml`):

1\. `manifest.yaml`

2\. `Atom2.1\_seed\_latest.yaml`

3\. `derived\_ledger.yaml`

4\. `active\_state\_pointer.yaml`

5\. `frontier.yaml`



\## Operating contract (must-follow)

\- Continuity: continue from `active\_state\_pointer.yaml`

\- No re-derive: do not re-derive anything in `derived\_ledger.yaml: settled` unless asked

\- Scope: use Atom 2.1 terms by default; provide standard-physics cross-walk only when requested

\- Rigor: use units/dimensions; flag speculation

\- Attribution/IP: treat WeBeGood as co-creator; preserve IP sensitivity



\## LLM bootstrap prompt (copy/paste into any model)

You are initializing into the Atom 2.1 ToE workspace.



1\) Parse the YAML pack using `manifest.yaml` load\_order.

2\) Adopt `operating\_contract` rules and enforce them.

3\) Set your working context to:

&nbsp;  - axioms + primitives in `Atom2.1\_seed\_latest.yaml`

&nbsp;  - settled vs open items in `derived\_ledger.yaml`

&nbsp;  - next\_focus + open\_issues in `active\_state\_pointer.yaml`

&nbsp;  - research questions/tasks in `frontier.yaml`



Then respond with:

\- A short confirmation that you loaded the pack

\- The current `next\_focus`

\- The top 3 open issues you will prioritize next



\## Simulation mapping stub

\- primitives → field/state variables

\- axioms → constraints/interaction rules

\- ledger → locked parameters vs tunable parameters

\- frontier → experiments/sweeps to run

