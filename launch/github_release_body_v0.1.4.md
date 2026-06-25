# Acceptance Plane™ Public Readiness Kit v0.1.4

A free public readiness kit with a 5-minute educational scenario-card linter for developers.

**Made by Meridian Verity Group (MVG): https://meridianverity.com/**

Boundary: **Not a product implementation. Not a standard. No patent license. No certification right.**

## Why this release exists

Agentic AI systems increasingly propose actions that can affect protected systems before humans have time to inspect every step. This kit gives teams a public language and scenario-card corpus for discussing whether a specific autonomous action should be accepted before impact.

## 5-minute trial

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
```

No API keys, external services, package installs, model calls, or cloud accounts are required.

## What is new in v0.1.4

- Public-facing polish: removed hype wording and kept foundation/community language sober.
- `make doctor`, `make demo-json`, `make preflight`, and deterministic package/checksum support.
- Release upload guide with standard `v0.1.4` tag and `gh release create --verify-tag`.
- `playbooks/production_boundary_readiness.md` replacing first-impression licensing language.
- Public threat model, one-hour evaluator script, archive/license boundary guide, release-integrity guide.
- Demo transcript, JSON demo output, SPDX-style public SBOM, and release audit materials.
- Stronger public boundary QA for stale release artifacts, old playbook names, unsafe claims, and public hype terms.

## What this is not

This release is not a product implementation, formal standard, reference implementation, conformance suite, certification kit, patent license, production verifier, production deployment artifact, procurement approval, compliance approval, or allow/deny system.

Suggested release assets:

```text
acceptance-plane-public-readiness-kit-v0.1.4.zip
acceptance-plane-public-readiness-kit-v0.1.4.zip.sha256
```
