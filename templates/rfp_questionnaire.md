# Acceptance Plane RFP Questionnaire

## Vendor

- Vendor name:
- Product / service:
- Version:
- Deployment context:
- High-consequence actions:

## Questions

1. List all autonomous or semi-autonomous actions that can affect protected systems.
2. For each action, identify the acceptance boundary.
3. Describe what evidence is evaluated before impact.
4. Explain how actor, delegation, scope, target, runtime, policy state, freshness, revocation, and consequence are considered.
5. Explain ACCEPT / HOLD / REFUSE behavior.
6. Explain fail-closed behavior for high-consequence actions.
7. Describe what verifier-ready evidence or receipt-like record is produced.
8. Explain how stale authority, revoked approval, target mismatch, replay, and ambiguity are handled.
9. Explain how the system prevents post-hoc-only accountability.
10. State whether any claims of certification, compliance, or conformance are independently auditable and legally authorized.

## Buyer note

Do not accept “we have access control” or “we log it later” as a complete answer for high-consequence autonomous actions.
