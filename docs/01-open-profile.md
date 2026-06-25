# Acceptance Plane Open Profile

This Open Profile defines public vocabulary for discussing action acceptance before impact. It is not a standard, product specification, API contract, evidence schema, implementation guide, or certification profile.

## Canonical category definition

The Acceptance Plane™ is the architectural function that determines whether a specific autonomous AI action should be accepted by a protected system before impact, based on current, scope-bound, verifier-ready evidence at the acceptance boundary.

## Planes

| Plane | Public description |
| --- | --- |
| Compute Plane | Runs models, agents, workloads, tools, and execution environments. |
| Control Plane | Configures identity, policy, orchestration, permissions, and governance. |
| Data Plane | Moves prompts, context, memory, retrieval results, tool outputs, and state. |
| Acceptance Plane | Determines whether autonomous action should be accepted before impact. |

## Acceptance boundary

The acceptance boundary is where AI intention may become system consequence. It can appear at an agent runtime, gateway, policy layer, application boundary, data layer, device boundary, operating-system path, or deeper infrastructure boundary. The exact placement can vary. The function should not.

## Public evidence categories

For public discussion, gate-time evidence may include:

- The action being attempted.
- The actor, agent, workload, user delegation, tool, or service chain initiating it.
- The runtime or environment evidence relevant to the action.
- The approved scope and intended target.
- The current policy state.
- Freshness, revocation, replay, and ambiguity indicators.
- Required approval, step-up, hold, or refusal condition.
- The final decision and public reason category.

This is a high-level category list, not an evidence schema.

## Decision vocabulary

| Decision | Meaning |
| --- | --- |
| ACCEPT | Evidence is current, scoped, consistent, and sufficient. |
| HOLD | Evidence is incomplete, stale, ambiguous, high-risk, or requires step-up review. |
| REFUSE | The action is outside authority, mismatched, revoked, replayed, unverifiable, unsafe, or not bound to the intended target. |

## Operating principle

Fail-closed autonomy: accept when proof is sufficient, hold when proof is incomplete, and refuse when proof fails.
