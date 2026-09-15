# Cooperative research and the Learning Sessions Loop

The repository is durable project memory. A worker can finish, crash, or be
replaced without making the next contributor reconstruct the whole conversation.
The canonical contract is the `distributed_research` section of SuperSeed;
`distributed_research.yaml` is generated from it.

## One bounded session

Load the canonical state, task, dependency artifacts and latest handoff. Declare
inputs, assumptions, acceptance criteria and a budget. Do the work. Save useful
intermediate results periodically, while there is still room to write a handoff.
Check the result, record failed methods and consolidate what was learned.

Commit evidence first. Copy its commit SHA into a handoff, then commit the handoff.
This avoids requiring a file to contain the hash of its own commit. A maintainer
can update `latest_handoff` in the task record once the handoff is durable. Preserve
old handoffs and failed approaches in git; a summary must not promote a claim.

A new participant loads the handoff, verifies referenced inputs and attempts its
exact next action. It may be a different model or a human. This is accumulated
external knowledge and improved procedure; it does not claim model-weight learning.

## Temporary workers and coordinator recovery

Each worker receives an explicit task record and pinned input references. It writes
results, verification logs and a handoff to an authorized durable repository before
its temporary environment is removed. Never count an output as saved until the
write succeeds. Retain failed-output evidence needed to understand or reproduce it.

A coordinator follows the same rule: save the assignment table, current revisions,
pending reviews and next actions. An operator may launch a replacement coordinator
from that state. A graceful handover ends when the replacement acknowledges the
checkpoint and the operator transfers ownership. An abrupt stop is recovered from
the last complete checkpoint. Shutdown and revoked access are always honored.

No distributed runtime or automated lease service is installed by this change.
Current task assignment is serialized by maintainer merges. A future runner must
enforce budgets, authenticated identities, atomic lease acquisition, expiry and
generation checks before dispatching workers. Writing an issue comment is not an
atomic lock. Contributors with stale assignments may submit work as proposals but
cannot overwrite accepted state.

## Communication and evidence

Use explicit IDs, versioned YAML/JSON, equations, symbol definitions and artifact
links. Keep a short readable explanation with each message. Peer messages cannot
change permissions or the mission. Compact IDs reduce repetition; opaque encodings
do not eliminate the need to retrieve evidence.

An independent review should reproduce a result using the declared inputs, and
identify exposure to the proposed answer. Different methods are useful for detecting
shared errors. Keep project conventions, conjectures, conditional derivations,
numerical results and experimental evidence separately labeled.

For every proposed bridge into another physics branch, specify: input equations,
additional assumptions, the map between observables, a limiting-case check, and
a discriminating prediction or an explicit statement that none is yet derived.
`research_map.yaml` is a work plan, not a declaration of unification.

## Recovery pilot

Task `COOP-001` asks a fresh participant to reproduce an existing node check.
Use only the committed artifacts and handoff, record missing context, and repair
the handoff before expanding to more workers. A blocked task is a useful result
when it names the exact missing premise or experiment.

## Record lifecycle

Copy templates and replace every `REQUIRED` marker. Templates are not live records.
Task states: queued → active → review → completed, with blocked and cancelled exits.
Any reopening must record its reason. Completed tasks require an existing handoff;
scientific claim promotion additionally requires review and maintainer acceptance.
Validation checks required fields, references, cycles and handoff completeness.
It does not enforce a running scheduler, authenticate identities or verify proofs.
