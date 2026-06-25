# RFP Questions for Action Acceptance Before Impact

Use these questions when evaluating AI agents, tool-calling platforms, cloud infrastructure, healthcare DSIs, financial agents, robotics systems, AR/VR overlay systems, sensor pipelines, and enterprise automation.

## Core buyer questions

1. Which autonomous or semi-autonomous actions can affect protected systems?
2. Where is the acceptance boundary for each high-consequence action?
3. What evidence is evaluated at the gate, rather than after impact?
4. How is the action bound to actor, delegation, scope, target, policy state, and freshness?
5. How does the system treat stale authority, revoked approval, target mismatch, replay, ambiguity, and partial evidence?
6. What actions result in ACCEPT, HOLD, or REFUSE?
7. Can the system produce a verifier-ready receipt or equivalent evidence package explaining why the action was accepted, held, or refused?
8. Does the system fail closed for high-consequence actions when required evidence is missing, stale, conflicting, or unverifiable?
9. Is post-hoc logging the only accountability mechanism, or does accountability begin at the point of action?
10. What parts of the acceptance process are independently verifiable by the customer, auditor, insurer, regulator, or affected institution?

## Red-flag answers

- “The agent has access, so the action is allowed.”
- “The runtime is attested, so all resulting actions are acceptable.”
- “We log everything afterwards.”
- “The model said it was safe.”
- “The approval existed earlier.”
- “The tool call succeeded.”
- “The vendor dashboard shows green.”
- “We cannot explain why this action was accepted.”

## Strong answers

- “We can name every high-consequence action class.”
- “We can show the acceptance boundary before production impact.”
- “We treat stale, ambiguous, or missing proof as HOLD or REFUSE.”
- “We can produce action-bound, scope-bound, time-bound evidence of the decision.”
- “We distinguish protected execution from accepted action.”
