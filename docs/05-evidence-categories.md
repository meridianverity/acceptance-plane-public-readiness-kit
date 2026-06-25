# Public Evidence Categories

This file lists high-level public evidence categories for readiness discussions. It is not an evidence schema, API, protocol, or implementation design.

## Categories

| Category | Public question |
| --- | --- |
| Action | What exact action is being attempted? |
| Actor | What agent, workload, user, service, or tool chain initiated it? |
| Delegation | Who or what delegated authority, and is it still valid? |
| Scope | Is the action inside the current allowed scope? |
| Target | Is the target the intended protected system, record, interface, account, device, or environment? |
| Runtime | What relevant environment, integrity, or protection evidence exists? |
| Policy state | Which current policy state governs the action? |
| Freshness | Is the authority, approval, policy, or evidence still current? |
| Revocation | Has any required authority, credential, approval, or evidence been revoked or suspended? |
| Replay | Is the request a replay, duplicate, stale reuse, or unbound copy? |
| Consequence | What real-world state, data, person, workflow, account, record, device, or environment may be affected? |
| Step-up | Does the action require human review, quorum, escalation, or safer mode? |
| Decision | Was the action ACCEPTED, HELD, or REFUSED, and why? |

## Rule of thumb

A high-consequence action should not be accepted just because the agent has access. It should be accepted only when the action is sufficiently bound to current authority, scope, target, policy, runtime evidence, and consequence.
