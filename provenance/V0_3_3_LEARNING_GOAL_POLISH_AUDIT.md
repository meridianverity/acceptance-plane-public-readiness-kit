# v0.3.3 Learning-goal Polish Audit

Result: PASS. Verified by `make qa-full` for the v0.3.3 release artifact.

What changed:

- Rewrote 100 ACCEPT-card `learning_goal` fields to remove the remaining the repeated before/reaches-before learning-goal phrase wording scar.
- Added the repeated before/reaches-before phrase, the team/reaches-before phrase, and the reaches-before phrase to the scenario language-polish QA blocker list.
- Preserved 300-card count, 10-domain balance, and 100 / 100 / 100 ACCEPT / HOLD / REFUSE discussion-label balance.
- Preserved public boundaries: educational readiness only; not implementation, conformance, certification, compliance approval, patent license, production verifier, or production allow/deny behavior.

Why this matters:

A public readiness corpus can pass structural QA while still losing trust if a human reviewer sees generator-like phrasing. v0.3.3 treats editorial polish as a release-integrity requirement and makes the specific scar a recurring gate failure.
