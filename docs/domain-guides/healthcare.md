# Healthcare and Clinical Decision Support

This guide names public acceptance-boundary questions for healthcare and clinical decision support. It is not a deployment guide or certification profile.

## Representative high-consequence actions

- chart write-back
- order suggestion finalization
- triage prioritization
- patient message send
- clinical workflow trigger

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
