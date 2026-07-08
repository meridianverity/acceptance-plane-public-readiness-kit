# Release Checklist — v0.3.4

Before announcing this release:

- [ ] `make qa-full` passes from a clean checkout.
- [ ] `python3 scripts/verify_manifest.py` passes.
- [ ] `python3 tools/scenario-uniqueness/scenario_uniqueness_qa.py` passes.
- [ ] Release ZIP uses canonical dotted filename: `acceptance-plane-public-readiness-kit-v0.3.4.zip`.
- [ ] SHA sidecar line names the same dotted ZIP file.
- [ ] Git tag is `v0.3.4`.
- [ ] GitHub release title is exactly: `Acceptance Plane Public Readiness Kit v0.3.4 — Release-Surface Locked Public Readiness Corpus for Action Acceptance Before Impact`.
- [ ] Assets are uploaded and checksums match.
- [ ] Public page shows the v0.3.4 release before any announcement says it is publicly released.

Boundary: checklist only. Not certification, compliance approval, production readiness, or a patent license.


## v0.3.4 language-polish and learning-goal polish gate

Run `make scenario-language-polish-check` to verify that the 300-card public educational corpus does not contain visible wording scars such as a duplicated `before` token, incorrect article before `incident`, or incorrect article before `operator`. This is editorial QA only, not certification, conformance testing, production readiness, or an allow/deny decision.
