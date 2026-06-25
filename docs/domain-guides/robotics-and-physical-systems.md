# Robotics and Physical Systems

This guide names public acceptance-boundary questions for robotics and physical systems. It is not a deployment guide or certification profile.

## Representative high-consequence actions

- motion command
- actuator trigger
- drug delivery suggestion
- warehouse robot reroute
- industrial fieldbus command

## Boundary question

Before the action becomes real, can the protected system explain why this exact action should be accepted now?

## Public evidence categories

- Action and consequence.
- Actor and delegation path.
- Scope and target.
- Runtime or environment evidence relevant to the action.
- Current policy state.
- Freshness, revocation, and replay posture.
- Human review or step-up condition where appropriate.
- Decision and reason category.

## Common HOLD conditions

- Earlier approval but uncertain current state.
- Missing target binding.
- Changed policy or revoked authority.
- High-risk consequence without sufficient review.
- Ambiguous tenant, patient, account, classroom, device, or jurisdiction context.

## Common REFUSE conditions

- Wrong target.
- Revoked delegation.
- Replay or duplicate request.
- Outside authority.
- Unverifiable evidence.
- Unsafe or prohibited action.
