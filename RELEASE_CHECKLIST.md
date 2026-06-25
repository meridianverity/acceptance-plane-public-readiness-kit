# Release Checklist — v0.1.4

## Local gates

- [ ] `make doctor`
- [ ] `make demo`
- [ ] `make demo-json`
- [ ] `make manifest-refresh`
- [ ] `make qa-clean`
- [ ] Confirm `provenance/MANIFEST.sha256` is updated.
- [ ] Confirm `provenance/FILE_TREE.txt` is updated.
- [ ] Confirm ZIP checksum exists.

## Public boundary

- [ ] README says: “free public readiness kit with a 5-minute educational scenario-card linter for developers.”
- [ ] README says: “Not a product implementation. Not a standard. No patent license. No certification right.”
- [ ] No public file describes the kit as a free version, implementation, reference implementation, standard, conformance kit, certification kit, production verifier, or production deployment artifact.
- [ ] `playbooks/production_boundary_readiness.md` is present.
- [ ] The former sales-forward playbook filename is absent.

## GitHub release

- [ ] Repository: `meridianverity/acceptance-plane-public-readiness-kit`
- [ ] Tag: `v0.1.4`
- [ ] Release title: `Acceptance Plane™ Public Readiness Kit v0.1.4`
- [ ] Asset: `acceptance-plane-public-readiness-kit-v0.1.4.zip`
- [ ] Checksum asset: `acceptance-plane-public-readiness-kit-v0.1.4.zip.sha256`
- [ ] Body: `launch/github_release_body_v0.1.4.md`
- [ ] `gh release create` uses `--verify-tag`.

## AAIF posture

- [ ] Do not submit as an AAIF Hosted Project at this stage.
- [ ] Use `AAIF_FEEDBACK_INQUIRY.md` only as a feedback / working-group-fit inquiry.
- [ ] Do not claim donation, contribution, or official AAIF status unless AAIF approves through the required process.
