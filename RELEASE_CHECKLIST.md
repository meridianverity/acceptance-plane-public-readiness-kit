# Release Checklist — v0.2.0

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

## Local QA

- [ ] `make qa-clean`
- [ ] `make readiness-demo`
- [ ] `make crosswalk-check`
- [ ] `make coverage-check`
- [ ] `make workshop-demo`
- [ ] `make external-pointer-check`
- [ ] `make qa-full`

## Release assets

- [ ] Tag: `v0.2.0`
- [ ] Release title: `Acceptance Plane Public Readiness Kit v0.2.0 — Board-to-Builder Readiness for Action Acceptance Before Impact`
- [ ] Asset: `acceptance-plane-public-readiness-kit-v0.2.0.zip`
- [ ] Checksum asset: `acceptance-plane-public-readiness-kit-v0.2.0.zip.sha256.txt`
- [ ] Body: `metadata/github_release_body_v0.2.0.md`

## Boundary check

- [ ] Release body says it is public education/readiness material only.
- [ ] Release body does not claim implementation, standard, certification, compliance approval, production allow/deny, patent license, or deployment readiness.
- [ ] External conformance artifacts are referenced only as separate artifacts via pointer lock.
- [ ] No claim charts, customer mappings, private licensing maps, production evidence schemas, or implementation details are included.

## Hosted provenance after publish

- [ ] Attach ZIP and SHA sidecar.
- [ ] Run GitHub artifact attestation workflow.
- [ ] Enable OpenSSF Scorecard workflow if appropriate for the public repo.
- [ ] Record release URL and attestation verification command in a follow-up release note.
