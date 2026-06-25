# Scenario Authoring Guide

Scenario cards are public teaching artifacts. They are not test vectors, conformance vectors, compliance artifacts, or certification evidence.

## A good scenario card includes

- A concrete action.
- A protected system.
- A clear acceptance boundary.
- A plausible ambiguity, risk, or proof condition.
- Public evidence categories.
- An expected educational decision: ACCEPT, HOLD, or REFUSE.
- A human-impact note.
- A learning goal.

## Do not include

- Production API schemas.
- Cryptographic protocol detail.
- PermitReceipt internals.
- Signed vectors.
- Claim mappings.
- Customer-specific deployments.
- Sensitive data.

## Example decision logic

- ACCEPT: current, scoped, sufficient evidence.
- HOLD: incomplete, stale, ambiguous, or step-up required.
- REFUSE: proof fails, authority revoked, replay detected, target mismatch, or unsafe action.
