# Readiness-to-Conformance Bridge

Boundary: public education and handoff only. This kit does not bundle conformance vectors, verifier logic, production mechanisms, certification rights, implementation licenses, or patent claim charts.

The Acceptance Plane Public Readiness Kit is the public front door for action acceptance readiness. It helps teams decide whether they have enough shared language, scenario coverage, buyer questions, and organizational ownership to move toward separate evidence.

When readiness discussion is no longer enough, the kit points outward to separate artifacts:

- **Acceptance Plane Interop Gauntlet v0.4.0** — public conformance target.
- **Acceptance Plane Independent Verifier v0.2.0** — second executable verification path.

Those artifacts are not bundled here. The pointer lock in `metadata/external_artifact_pointer_lock.json` records their names, roles, versions, SHA-256 digests, and boundaries so a reviewer can see the ecosystem path without confusing this public kit with an implementation or conformance package.

## Handoff rule

Move from this readiness kit to separate conformance evidence only after the team can answer:

1. What exact action creates impact?
2. What protected system receives that impact?
3. What evidence categories must be current at the acceptance boundary?
4. What should trigger HOLD rather than ACCEPT?
5. What should trigger REFUSE?
6. Who owns human escalation?
7. What buyer questions can be asked without requesting private implementation mechanisms?

## Public-safe phrasing

Use:

> The readiness kit helps a team decide when action-level evidence should be requested before autonomous action becomes impact.

Avoid:

> The readiness kit performs verification, approval, production deployment, or implementation of action acceptance.
