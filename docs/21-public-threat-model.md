# Public Threat Model

This document describes threats to the public readiness kit itself. It is not a security design for a production Acceptance Plane implementation.

## Protected public assets

- The public/private boundary: users must not confuse this kit with an implementation, standard, certification kit, or production allow/deny system.
- Scenario-card integrity: public cards should remain educational and should not reveal partner deployments, exact evidence schemas, cryptographic mechanisms, or patent claim language.
- Release provenance: published files should match the manifest and checksum.
- Community trust: issues, pull requests, and forks should preserve attribution and avoid certification or endorsement claims.

## Main public risks

1. **Boundary confusion** — a reader treats `DISCUSSION_READY`, `ACCEPT`, `HOLD`, or `REFUSE` as a production decision.
2. **Implementation leakage** — a contribution includes exact evidence objects, verifier logic, cryptographic bindings, adapter code, partner deployment details, or claim charts.
3. **Certification implication** — a vendor suggests that passing the linter means conformance, compliance approval, certification, procurement approval, or production readiness.
4. **Supply-chain drift** — generated files, local caches, or unreviewed files enter a release ZIP.
5. **Trademark misuse** — names or marks are used as source-identifying marks or endorsements without permission.

## Controls in this repository

- Repeated boundary notice in README, NOTICE, license boundary, tool output, issue templates, and release notes.
- Full-repo public boundary QA scan.
- Strict SHA-256 manifest verification with generated-file exclusions.
- Split license notice: MIT for software files, CC BY 4.0 for public materials unless a file states otherwise.
- Security and accidental implementation-disclosure reporting path.
- AAIF feedback-inquiry posture instead of premature hosted-project submission.

## Non-goals

This public threat model does not describe production verifier architecture, evidence binding, runtime enforcement, certificate registry design, hardware adapters, policy engines, partner deployments, or patent claim coverage.
