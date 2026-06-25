# ACCEPT / HOLD / REFUSE Playbook

## ACCEPT

Use ACCEPT when the evidence is current, scoped, consistent, sufficient, and bound to the intended action and target.

Public examples:

- Production change matches current approval and target.
- Delegation is current and action is inside scope.
- Runtime posture is relevant and sufficient for the action class.
- Revocation and freshness checks are not ambiguous.
- The action consequence is understood and within permitted bounds.

## HOLD

Use HOLD when evidence is incomplete, stale, ambiguous, high-risk, inconsistent, or requires step-up review.

Public examples:

- Approval existed earlier but may have expired.
- Target appears similar but not identical.
- Runtime evidence is unavailable or outdated.
- Policy state changed after the action was proposed.
- The action may affect vulnerable users, regulated records, money, physical devices, or safety-critical workflows.

## REFUSE

Use REFUSE when proof fails.

Public examples:

- The action is outside authority.
- The target is wrong or mismatched.
- Delegation is revoked.
- The request appears replayed.
- Required evidence is unverifiable.
- The action is unsafe or not bound to the intended protected system.

## Default posture

For high-consequence actions: proof sufficient → ACCEPT; proof incomplete → HOLD; proof failed → REFUSE.
