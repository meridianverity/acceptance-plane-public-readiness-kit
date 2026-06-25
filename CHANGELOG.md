# Changelog

## v0.1.4 — 2026-06-25

Public polish and release-integrity hardening release.

Post-check polish before public push:

- Added the missing `rights_boundary` field to the linter sample fixture so the included CLI test passes cleanly.
- Converted the linter CLI test to standard-library `unittest` so test execution does not require external packages.
- Added `make unit-test` and included it in `make qa` / `make preflight` for stronger GitHub release discipline.
- Replaced licensing-forward public slogan language with protected-mechanism wording for a more foundation-safe first impression.

- Removed public-facing hype wording and kept release language sober, technical, and foundation-safe.
- Renamed the sales-forward production-readiness playbook to `playbooks/production_boundary_readiness.md` to keep the first public impression focused on readiness and boundary discipline.
- Added `make doctor`, `make demo-json`, `make preflight`, and deterministic packaging support.
- Added `launch/git_publish_commands_v0.1.4.sh` with `gh release create --verify-tag` and standard `v0.1.4` tag flow.
- Added release-integrity materials: `provenance/SBOM.spdx.json`, `provenance/RELEASE_AUDIT.md`, demo transcript, and JSON demo output.
- Added enterprise review aids: public threat model, one-hour evaluator script, archive/license boundary guide, `.editorconfig`, `.gitattributes`, and `.github/CODEOWNERS`.
- Strengthened public boundary QA to check for stale release artifacts, public hype terms, old playbook names, and release-command safety.
- Preserved the public/private boundary: no production verifier, exact evidence schema, cryptographic binding method, non-bypassable enforcement adapter, conformance vectors, certificate registry, hardware adapter, partner deployment, or patent claim chart.

## v0.1.3 — 2026-06-25

Public developer-readiness release.

- Repositioned the repository as a **free public readiness kit with a 5-minute educational scenario-card linter for developers**.
- Added developer-first `README.md` and `README_ko.md` quickstart paths.
- Added `make demo`, `make qa-clean`, and `make release-check`.
- Improved `scenario-card-lint` with `--summary`, `--format json`, stronger field/type checks, aggregate counts, and repeated rights-boundary language.
- Added `QUICKSTART.md`, `GITHUB_UPLOAD_GUIDE.md`, `AAIF_FEEDBACK_INQUIRY.md`, `DEPENDENCIES.md`, `MAINTAINERS.md`, `ROADMAP.md`, and `RELEASE_CHECKLIST.md`.
- Added a public educational scenario-card JSON shape at `scenarios/scenario_card.schema.json` without creating an evidence schema, API contract, conformance format, or implementation disclosure.
- Added a public license split: MIT for software files and CC BY 4.0 for non-software public readiness materials.
- Hardened manifest verification for real Git repositories by excluding `.git/`, Python cache files, and local build/cache artifacts while remaining strict for release files.
- Updated GitHub Actions to run `make demo` and `make qa` with `PYTHONDONTWRITEBYTECODE=1`.
- Added v0.1.3 launch and upload strategy materials.
- Preserved the public/private boundary: no production verifier, exact evidence schema, cryptographic binding, non-bypassable enforcement adapter, conformance vectors, certificate registry, hardware adapter, partner deployment, or patent claim chart.

## v0.1.2 — 2026-06-12

Flagship public-release hardening patch.

- Added full-repo text boundary QA for unsafe positive claims involving implementation, certification, conformance, standards, patent license, trademark license, or production mechanism language.
- Strengthened manifest verification so every repository file except `provenance/MANIFEST.sha256` itself must be listed exactly once and match SHA-256.
- Added `scripts/write_manifest.py` to regenerate the strict manifest.
- Renamed the educational utility to `scenario-card-lint` to reduce the risk that users treat it as a compliance, certification, or production readiness checker.
- Added inbound contribution licensing and implementation-disclosure guardrails to `CONTRIBUTING.md`.
- Added security/boundary reporting instructions and GitHub issue templates for public-safe boundary reports and scenario proposals.
- Added `ATTRIBUTION.md` for citation, mark use, allowed descriptive use, and prohibited certification/source-identifying use.
- Added `docs/17-pre-release-legal-ip-checklist.md` for counsel/IP/trademark/private-file sweep discipline before publication.
- Added `launch/upload_strategy_v0.1.2.md` to separate GitHub release, optional Zenodo archive, article companion, and scenario campaign roles.
- Updated README, Korean README, CFF, Zenodo metadata, Makefile, GitHub Actions, QA report, file tree, and provenance files for v0.1.2.
- Preserved the public/private boundary: no production verifier, exact evidence schema, cryptographic binding, non-bypassable enforcement adapter, conformance vectors, certificate registry, hardware adapter, partner deployment, or patent claim chart.

## v0.1.1 — 2026-06-12

Release-readiness hardening patch.

- Separated kit citation metadata from the canonical thesis DOI using `preferred-citation` in `CITATION.cff`.
- Normalized Zenodo `related_identifiers` DOI format to raw DOI under `scheme: doi`.
- Added manifest verification to GitHub Actions QA.
- Cleaned README formal citation title while preserving ™ in branding and framework-identifying use.
- Added public adoption materials: board one-pager, policy memo template, procurement scorecard, vendor email, launch copy, FAQ, maturity model, release-boundary checklist, and century-scale research agenda.
- Preserved the public/private boundary: no production verifier, exact evidence schema, cryptographic binding, non-bypassable enforcement adapter, conformance vectors, certificate registry, hardware adapter, partner deployment, or patent claim chart.

## v0.1.0 — Public Readiness Kit foundation release — 2026-06-12

Added:

- Open Profile for the Acceptance Plane category.
- 100 public scenario cards across ten domains.
- RFP and procurement templates.
- Public-interest covenant.
- Publication and licensing boundary guidance.
- Educational scenario-card linter.
- QA report, file tree, and SHA-256 manifest.

Intentionally not added:

- Production verifier.
- PermitReceipt implementation.
- Exact evidence schema.
- Cryptographic binding method.
- Non-bypassable enforcement adapter.
- Signed conformance vectors.
- Certificate registry.
- Certification program.
