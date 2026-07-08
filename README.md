# Acceptance Plane™ Public Readiness Kit v0.3.4

**Public readiness operating system for action acceptance before impact.**  
**Made by Meridian Verity Group (MVG): https://meridianverity.com/**  
**Not a product implementation. Not a standard. No patent license. No certification right.**

The Acceptance Plane™ is a public architecture category for discussing action-level trust in agentic AI infrastructure: the function that determines whether a specific autonomous AI action should be accepted by a protected system before impact, based on current, scope-bound, verifier-ready evidence at the acceptance boundary.

This kit helps boards, buyers, auditors, CISOs, platform teams, public-sector teams, nonprofits, researchers, developers, and facilitators ask one practical pre-impact question:

> Should this exact autonomous action be accepted by this protected system right now?

## What changed in v0.3.4

v0.3.4 is an editorial-lock and corpus-stewardship release. It keeps the v0.3.x public readiness operating system intact while removing the final visible scenario-card and learning-goal wording scars and adding a release gate so they cannot return:

- **300 public scenario cards** across 10 domains for board, buyer, builder, incident, and facilitator discussion.
- **Scenario uniqueness QA**: no id-normalized duplicates, no duplicate title/scenario pairs, and no repeated high-signal explanatory fields.
- **Scenario language-polish QA**: rejects visible wording scars such as a duplicated `before` token, incorrect article before `incident`, and incorrect article before `operator`.
- **Browser-only readiness demo** in `browser_readiness_demo/` with no network dependency.
- **Markdown/JSON public readiness report generator** via `make report-demo`.
- **Crosswalk coverage heatmap** via `make crosswalk-coverage-check`.
- **Third-party facilitator reproduction packet** in `third_party_facilitator/`.
- **Public adoption evidence template** in `adoption/public_adoption_evidence_template.md`.
- **Deterministic release integrity** carried forward from v0.2.1: manifest lock, reproducible ZIP, figure integrity, boundary QA, and hosted-attestation guidance.

## 5-minute quickstart

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
make readiness-demo
make report-demo
make browser-demo-check
```

No API keys. No services. No package install. Python standard library only.

Run the full public QA gate:

```bash
make qa-full
```

## Board → Buyer → Builder → Conformance path

1. **Board**: use `workshops/30_min_board_briefing.md` and `docs/25-public-evidence-ladder.md` to frame why access, permission, execution, and acceptance are different questions.
2. **Buyer**: use `procurement/vendor_disclosure_questions.md` and `procurement/rfp_clause_library.md` to request action-level evidence without asking for private implementation details.
3. **Builder**: use `readiness/sample_readiness_assessment.json` and `tools/readiness-index/readiness_index.py` to identify public readiness gaps.
4. **Facilitator**: use `third_party_facilitator/REPRODUCTION_PACKET.md` to reproduce the public education workflow.
5. **Conformance handoff**: use `metadata/external_artifact_pointer_lock.json` and `docs/26-readiness-to-conformance-bridge.md` to point to separate conformance artifacts when education is no longer enough.

## What this release contains

- A developer-first **5-minute scenario-card linter**.
- A **300-scenario public corpus** across ten domains for tabletop discussion, procurement, training, and public education.
- A public **Action Acceptance Readiness Index** and sample report.
- A browser-only public readiness demo.
- Markdown/JSON public readiness report generation.
- Public-safe standards/security crosswalks and crosswalk coverage heatmap.
- Scenario coverage reports for the public corpus.
- Workshop materials and procurement due-diligence materials.
- A facilitator reproduction packet and public adoption evidence template.
- A public-safe bridge to separate conformance artifacts.
- Strict release provenance: manifest verification, boundary QA, deterministic release ZIP verification, reproducibility check, file tree, SBOM, hosted-attestation guidance, and release checklist.

## What this release intentionally does not contain

This package does **not** include production-grade enforcement, exact API schemas, full evidence object models, cryptographic binding methods, non-bypassable interceptor logic, PermitReceipt implementations, signed conformance vectors, certificate registry logic, runtime adapters, hardware-specific claim maps, partner deployments, unpublished patent claim language, patent claim charts, or implementation licenses.

Those omissions are intentional. This kit is for public category formation, literacy, readiness, procurement alignment, tabletop discussion, facilitator reproducibility, and human-centered stewardship. It is not a shortcut to deploy or certify an Acceptance Plane implementation.

## Suggested GitHub repo description

> Free public readiness operating system for action acceptance before impact: 300 scenario cards, scenario-card linting, readiness indexing, browser demo, public report generator, evidence ladder, crosswalks, workshops, procurement materials, facilitator packet, and a public-safe bridge to separate conformance artifacts.

## Suggested GitHub topics

`agentic-ai`, `ai-infrastructure`, `ai-security`, `ai-governance`, `action-acceptance`, `acceptance-plane`, `fail-closed-autonomy`, `public-readiness`, `scenario-cards`, `readiness-index`, `ai-risk-management`, `agentic-security`

## Start here

1. Run `make demo`, `make readiness-demo`, and `make report-demo`.
2. Open `browser_readiness_demo/index.html` locally.
3. Read `docs/00-executive-summary.md`, `docs/25-public-evidence-ladder.md`, and `docs/29-public-readiness-operating-system.md`.
4. Use `workshops/facilitator_guide.md` for a team session.
5. Use `procurement/vendor_disclosure_questions.md` for buyer/vendor conversations.
6. Read `PUBLIC_BOUNDARY.md` before publishing or adapting this package.

## License and rights boundary

This repository uses a public license split:

- **Software files** under `tools/`, `scripts/`, `.github/workflows/`, and the root `Makefile` are provided under the MIT License unless a file states otherwise.
- **Text, documentation, figures, templates, scenario cards, launch materials, and adoption materials** are provided under Creative Commons Attribution 4.0 International (CC BY 4.0) unless a file states otherwise.

This public kit does **not** grant any patent license, trademark license, service mark license, product implementation license, certification right, compliance approval, endorsement, or right to use Meridian Verity Group names, logos, marks, or framework identifiers as source-identifying marks. See `PATENT_AND_TRADEMARK_NOTICE.md`, `ATTRIBUTION.md`, and `docs/19-license-and-rights-boundary.md`.

## Citation

Current canonical public architecture record:

Lee, Scott. Meridian Verity Group. (2026). *The Acceptance Plane: A Public Trust Architecture for Agentic AI Action Acceptance and Verifier-Ready Receipts* (MVG-AP-TR-2026-06-v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.20683834

This readiness kit is a public educational supplement to that record. Earlier v1.0.0 thesis language may appear in historical changelog notes only.

## Release principle

> Open the question. Protect the mechanism. Help the world refuse unsafe autonomous action before impact.
