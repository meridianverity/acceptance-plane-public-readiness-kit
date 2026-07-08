# Micro-HOLD Fix Audit — Acceptance Plane Public Readiness Kit v0.2.0

This note records the final public-release polish pass applied before sharing the v0.2.0 release artifact.

Boundary: public readiness material only. Not implementation, standard, certification kit, compliance approval, patent license, or production allow/deny system.

## Fixed items

1. **Public GitHub release state guard**
   - Added `metadata/public_release_state_note_v0.2.0.md`.
   - Release docs now state that v0.2.0 should not be announced as publicly released until the GitHub tag/release page and uploaded SHA sidecar are live.

2. **Canonical DOI / title alignment**
   - Updated `CITATION.cff`, `.zenodo.json`, README citation text, SVG figure labels, attribution text, and boundary QA constants to the current public architecture record:
     `The Acceptance Plane: A Public Trust Architecture for Agentic AI Action Acceptance and Verifier-Ready Receipts`, MVG-AP-TR-2026-06-v2.0.2, DOI `10.5281/zenodo.20683834`.

3. **Stale v0.1.4 release references**
   - Updated the release-integrity tag example to `v0.2.0`.
   - Updated `provenance/GIT_CHECKOUT_TEST.txt` to v0.2.0 and current QA scope.
   - Updated `demos/sample_json_report.json` tool version to `0.2.0`.
   - Historical v0.1.4 references remain only in changelog/upgrade/deleted-file notes where they are intentionally historical.

4. **Broken root boundary reference**
   - Added root `PUBLIC_BOUNDARY.md` so docs that instruct reviewers to inspect the boundary have an obvious top-level target.

5. **Tiny grammar fix**
   - Changed `a educational scenario-card linter` to `an educational scenario-card linter`.

6. **Release audit wording**
   - Replaced unfinished `Result: filled after QA.` with `Result: PASS. Verified by make qa-full for the v0.2.0 release artifact.`

## Final expected gates

```text
make qa-full                                      PASS
scripts/verify_manifest.py                       PASS
scripts/public_boundary_qa.py                    PASS, 0 unsafe hits
scripts/verify_release_artifact.py <zip> --sha   PASS
v0.1.4 + v0.2.0 overlay + deleted-file cleanup   PASS
```
