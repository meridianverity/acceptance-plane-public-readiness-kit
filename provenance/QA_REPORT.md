# QA Report — Acceptance Plane™ Public Readiness Kit v0.1.4

Release date: 2026-06-25  
Prepared by: Meridian Verity Group  
Repository: `acceptance-plane-public-readiness-kit`

## Scope

This report covers public-readiness QA only.

Scenario layout: `scenarios_batch_1/` + `scenarios_batch_2/` contain the 100 JSON cards; `scenarios/` contains shared metadata, index, schema, and format guide. The legacy `scenarios/cards/` path is not used in this release artifact. It is not a product implementation test, not a formal standard test, no patent license, and no certification right.

## Commands run

```bash
make doctor
make demo
make demo-json
make unit-test
make manifest-refresh
make qa-clean
make preflight
python3 -m pytest -q
git init
make qa-clean
```

## Results

```text
QA PASSED
Scenario cards: 100
Decision balance: {'HOLD': 35, 'REFUSE': 33, 'ACCEPT': 32}
Domain balance: {'cloud_deployment': 10, 'enterprise_data': 10, 'healthcare_dsi': 10, 'financial_actions': 10, 'public_sector': 10, 'education_minors': 10, 'ar_vr_overlays': 10, 'sensor_ingress': 10, 'robotics_physical': 10, 'agent_tool_use': 10}
Full-repo text boundary scan: 215 files scanned, 0 unsafe hits
Boundary notice: present
Citation metadata: preferred-citation boundary passed
Zenodo related DOI: raw DOI boundary passed
Developer quickstart: make demo present
License split: MIT software / CC BY 4.0 materials
CI manifest check: present
Tool naming: scenario-card-lint boundary passed
AAIF posture: feedback inquiry present; not hosted-project claim
Release integrity docs: present
Public hype/internal wording scan: passed
MANIFEST VERIFY PASSED
Strict manifest entries: 221
Excluded local/generated paths: .git/, __pycache__, *.pyc, build/, dist/, cache directories
Excluded self-reference: provenance/MANIFEST.sha256
```

## v0.1.4 public polish patches

- Scenario cards are organized into two 50-card upload-friendly batches while preserving the 100-card corpus, index, schema, QA, and manifest discipline.
- Public wording is sober and foundation-safe.
- Sales-forward first-impression playbook language was replaced with production-boundary readiness language.
- GitHub upload guide and shell command include `gh release create --verify-tag`.
- Added public threat model, one-hour evaluator script, archive/license boundary guide, release-integrity guide, demo transcript, JSON demo output, and SPDX-style public SBOM.
- Strengthened boundary QA to catch stale release artifacts, old playbook wording, public hype terms, unsafe positive claims, and release-command omissions.

## Release gate conclusion

The package is ready for public GitHub release as a free public readiness kit with a 5-minute educational scenario-card linter for developers.

It should not be represented as a product implementation, formal standard, reference implementation, conformance suite, certification kit, production verifier, patent license, production deployment artifact, procurement approval, compliance approval, or allow/deny system.
