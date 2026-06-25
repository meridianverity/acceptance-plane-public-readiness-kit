# Security and Boundary Reporting Policy

This repository does not contain production security software. It contains public readiness materials and an educational scenario-card linter.

Do not use the scenario-card linter to make real-world allow/deny decisions. It does not verify identity, authority, runtime posture, cryptographic evidence, revocation, freshness, target binding, policy state, conformance, certification status, or production readiness.

## What to report

Please report concerns involving:

- accidental implementation disclosure;
- accidental publication of exact API schemas, evidence object models, cryptographic binding methods, enforcement pipelines, hardware-specific adapters, private partner details, or unpublished patent claim language;
- unsafe wording that could encourage real-world deployment from public materials;
- false certification, compliance approval, procurement approval, or endorsement claims;
- misuse of Acceptance Plane™ or Meridian Verity Group marks as source-identifying marks;
- files that appear to be private, partner-specific, claim charts, production mechanisms, or certification materials.

## How to report

Preferred confidential path: use the repository's **GitHub Security Advisory** process for `meridianverity/acceptance-plane-public-readiness-kit` when the repository is public and advisories are enabled.

For public, non-sensitive wording issues, open a GitHub issue using the boundary-report template and do not include implementation details, claim charts, partner names, private file contents, credentials, secrets, or unpublished patent language.

If a report involves accidental implementation disclosure, keep the report confidential and provide only the minimum information needed for maintainers to locate and remove the material.

## Maintainer response target

Maintainers should triage boundary/security reports before routine content contributions. Reports involving private implementation detail, certification confusion, or mark misuse should be treated as release blockers until resolved.
