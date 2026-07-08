# Changelog

## v0.3.4 — 2026-07-08

- Removes the duplicate v0.3.3 changelog heading and visible release-surface wording issues found after v0.3.3.
- Adds release-surface polish QA so duplicate release headings, repeated-word scars, awkward phrase-family wording, stale active release pointers, and underscore release filenames cannot pass future release gates.
- Simplifies `make qa-full` so full release QA builds once, verifies directly, and still performs reproducible ZIP checks without recursive release rebuild loops.
- Publishes canonical dotted v0.3.4 release asset names and metadata while preserving strict public boundaries.
- Keeps the 300-card public readiness operating system intact: 10 domains, 100 ACCEPT / 100 HOLD / 100 REFUSE, uniqueness QA, language-polish QA, release-surface QA, readiness index, browser demo, report generator, workshop pack, procurement pack, facilitator packet, external conformance bridge, deterministic release verification, and reproducible ZIP check.

## v0.3.3 — 2026-07-08

- Polishes the final ACCEPT-card learning-goal wording issue in the 300-card public readiness corpus.
- Adds release-gate checks for repeated reaches-before learning-goal phrasing so the issue cannot return.
- Publishes canonical dotted v0.3.3 release asset names and metadata while preserving strict public boundaries.

## v0.3.2 — 2026-07-08

- Removes final editorial scars from the 300-card public educational corpus, including duplicated-before wording and incorrect incident/operator article usage.
- Adds scenario language-polish QA to release gates so visible generator scars cannot pass future release QA.
- Aligns remaining 300-card public corpus language in legal/IP and provenance files.
- Publishes canonical dotted v0.3.2 release asset names and release metadata while preserving strict public boundaries.

## v0.3.1 — 2026-07-08

- Re-curates the 300-card public educational scenario corpus so every scenario has unique title/scenario, why, human-impact, learning-goal, and acceptance-boundary text.
- Adds scenario uniqueness QA and wires it into `make qa` / `make qa-full`.
- Aligns Korean summary language with the v0.3.x 300-card corpus.
- Canonicalizes release-facing commands, metadata, ZIP asset names, and sidecar names around dotted `v0.3.1` filenames.
- Retains deterministic ZIP packaging, manifest verification, release artifact verification, reproducible ZIP checks, figure DOI checks, and public boundary QA.


## v0.3.0 — 2026-07-08

- Promotes the kit from an integrity-and-stewardship release into a public readiness operating system.
- Expands the public educational scenario corpus from 100 to 300 cards across ten domains while preserving public-only boundaries.
- Adds a browser-only static readiness demo with no network dependency.
- Adds a Markdown/JSON public readiness report generator.
- Adds crosswalk coverage heatmap output.
- Adds a third-party facilitator reproduction packet and public adoption evidence template.
- Updates release metadata, manifest, file tree, QA report, boundary QA, and deterministic packaging for v0.3.0.
- Preserves the public/private boundary: no production verifier, exact evidence schema, cryptographic binding, non-bypassable enforcement adapter, conformance vectors, certificate registry, partner deployment, or patent claim chart.

## v0.2.1 — 2026-07-08

- Fixes stale DOI text in the rendered PNG figures by regenerating them from the current SVG sources.
- Removes the misleading local SLSA placeholder and clarifies that hosted artifact attestation is generated after build.
- Makes release ZIP construction deterministic by fixing ZIP member timestamps, Unix permissions, ordering, compression inputs, and sidecar output.
- Adds a reproducible ZIP check to the release QA path so mtime-only changes do not alter the release artifact digest.
- Updates release metadata, CFF dates, workflows, release guides, SBOM labels, and public-state guard files for v0.2.1.
- Adds long-horizon stewardship guidance and a figure rendering provenance note while preserving the public/private boundary.

## v0.2.0 — 2026-07-07

- Promotes the public readiness kit from a scenario-card-only educational package into a board-to-builder adoption gateway.
- Adds the Action Acceptance Readiness Index with sample assessment and report output.
- Adds public-safe crosswalks for NIST AI RMF, OWASP agentic-AI materials, Five Eyes/CISA agentic-AI guidance, and ISO/IEC 42001 language.
- Adds the Public Evidence Ladder and a readiness-to-conformance handoff bridge to separate external artifacts.
- Adds scenario coverage reports for the initial public corpus, later expanded and curated to the 300-card v0.3.x public corpus.
- Adds board, CISO/platform, procurement, and incident-tabletop workshop materials.
- Adds procurement due-diligence questions, RFP clauses, red flags, and non-certification language.
- Adds release ZIP build/verification tools, release pointer metadata, provenance workflow skeletons, SPDX metadata and hosted-attestation guidance, and stronger boundary QA.

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
