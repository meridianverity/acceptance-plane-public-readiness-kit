# Pre-Release Legal / IP / Public-Disclosure Checklist

This checklist is a release hygiene tool, not legal advice. Use appropriate counsel for patent, trademark, licensing, standards, public-disclosure, export, regulatory, and contractual questions.

## Release identity

- [ ] Release title uses “Public Readiness Kit,” “public reference materials,” “scenario corpus,” or equivalent safe public wording.
- [ ] Release does not describe itself as an open-source implementation, reference implementation, SDK, formal standard, certification kit, conformance suite, or production verifier.
- [ ] Version number, tag, changelog, README, CFF, and Zenodo metadata agree.

## Counsel / IP / mark review

- [ ] Counsel or authorized IP reviewer has reviewed the public disclosure boundary.
- [ ] Trademark or source-identifying mark strategy has been reviewed.
- [ ] Patent-publication strategy has been reviewed for relevant jurisdictions.
- [ ] No statement creates or implies patent license, trademark license, implementation license, certification right, endorsement, compliance approval, or procurement approval.

## Private-file sweep

- [ ] No private partner material.
- [ ] No claim charts or claim mappings.
- [ ] No unpublished patent claim language.
- [ ] No exact API schemas.
- [ ] No full evidence object models.
- [ ] No cryptographic binding methods or protocols.
- [ ] No production verifier, PermitReceipt engine, non-bypassable interceptor, runtime adapter, certificate registry, or signed conformance vector corpus.
- [ ] No hardware-specific adapter, driver path, enforcement pipeline, or domain-specific runtime implementation.
- [ ] No credentials, keys, secrets, private URLs, partner names, deployment artifacts, or commercial negotiation materials.

## Public-good alignment

- [ ] Release leads with stewardship, public literacy, and safer questions before impact.
- [ ] Public materials help hospitals, schools, small cities, nonprofits, auditors, public-sector buyers, and civil-society teams ask practical acceptance questions.
- [ ] Release does not frame the work as anti-vendor, anti-model, anti-cloud, anti-autonomy, or patent-enforcement-first.
- [ ] Release separates public education from private/licensed production mechanism conversations.

## Provenance and QA

- [ ] Full-repo boundary QA passes.
- [ ] Scenario-card linter passes across the 100-card corpus.
- [ ] Strict manifest verification passes and fails on unmanifested files.
- [ ] `provenance/FILE_TREE.txt`, `provenance/QA_REPORT.md`, and `provenance/SOURCES.md` are current and included in the manifest.
- [ ] ZIP integrity test passes.

## Launch gate

- [ ] GitHub release asset is the primary public distribution point.
- [ ] Optional Zenodo archive is used for citable preservation, not as the canonical thesis replacement.
- [ ] Release notes repeat the boundary notice.
- [ ] LinkedIn/article copy says: “We are opening the readiness layer, not the mechanism.”
