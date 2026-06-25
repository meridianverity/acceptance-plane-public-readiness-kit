# Release Audit — Acceptance Plane™ Public Readiness Kit v0.1.4

Prepared by: Meridian Verity Group  
Date: 2026-06-25

## Public boundary

This release is a free public readiness kit with a 5-minute educational scenario-card linter for developers.

It is not a product implementation, formal standard, reference implementation, conformance suite, certification kit, patent license, production verifier, production deployment artifact, procurement approval, compliance approval, or allow/deny system.

## Gates run

```bash
make doctor
make demo
make demo-json
make unit-test
make manifest-refresh
make qa-clean
make preflight
```

## Scenario-card layout

- `scenarios_batch_1/`: AP-SCEN-001 through AP-SCEN-050.
- `scenarios_batch_2/`: AP-SCEN-051 through AP-SCEN-100.
- `scenarios/`: shared index, schema, format guide, and README.
- Legacy `scenarios/cards/` is intentionally absent.

## Integrity artifacts

- `provenance/MANIFEST.sha256`
- `provenance/FILE_TREE.txt`
- `provenance/SBOM.spdx.json`
- `provenance/QA_REPORT.md`
- `provenance/SHIP_DECISION.md`
- release ZIP `.sha256` checksum

## QA summary

```text
Scenario cards: 100
Decision balance: HOLD 35 / REFUSE 33 / ACCEPT 32
Domain balance: 10 domains × 10 cards
Full-repo text boundary scan: 215 files scanned, 0 unsafe hits
Strict manifest entries: 221
```

## Current release conclusion

Public release is appropriate after a clean checkout confirms `make qa-clean` passes.
