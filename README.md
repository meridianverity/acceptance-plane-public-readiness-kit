# Acceptance Plane™ Public Readiness Kit v0.2.0

**Board-to-builder readiness for action acceptance before impact.**  
**Made by Meridian Verity Group (MVG): https://meridianverity.com/**  
**Not a product implementation. Not a standard. No patent license. No certification right.**

The Acceptance Plane™ is a public architecture category for discussing action-level trust in agentic AI infrastructure: the function that determines whether a specific autonomous AI action should be accepted by a protected system before impact, based on current, scope-bound, verifier-ready evidence at the acceptance boundary.

This kit helps boards, buyers, auditors, CISOs, platform teams, public-sector teams, nonprofits, researchers, and developers ask one practical pre-impact question:

> Should this exact autonomous action be accepted by this protected system right now?

## What changed in v0.2.0

The v0.1.x line was a clean public educational kit with a 5-minute scenario-card linter. v0.2.0 turns the same public boundary into a board-to-builder readiness gateway:

- **Action Acceptance Readiness Index**: a public discussion maturity score that produces a HOLD-style readiness report without claiming certification or production readiness.
- **Standards/security crosswalks**: public-safe prompts aligned to NIST AI RMF, OWASP agentic-AI security materials, Five Eyes/CISA agentic-AI guidance, and ISO/IEC 42001 vocabulary.
- **Public Evidence Ladder**: a non-implementation path from vocabulary, to scenario discussion, to readiness report, to RFP evidence request, to separate conformance handoff.
- **Readiness-to-conformance bridge**: external pointer lock for the separate Interop Gauntlet and Independent Verifier artifacts, without bundling implementation logic in this kit.
- **Scenario coverage reporting**: domain balance, decision balance, and public evidence-category heatmap for the 100-card corpus.
- **Board-to-builder workshop pack**: 30-minute board brief, 60-minute CISO/platform review, 90-minute procurement review, and 2-hour incident tabletop.
- **Procurement due-diligence pack**: vendor disclosure questions, RFP clause language, buyer checklist, non-certification language, and red flags.
- **Release provenance hardening**: release ZIP builder, archive verifier, manifest lock, SLSA-shaped local provenance, GitHub attestation workflow skeleton, and stronger boundary QA.

## 5-minute quickstart

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
make readiness-demo
make coverage-check
```

No API keys. No services. No package install. Python standard library only.

Expected readiness posture:

```text
Readiness posture: HOLD_FOR_IMPLEMENTATION_REVIEW
Discussion maturity: 72 / 100
Boundary: educational readiness signal only; not certification, compliance approval, procurement approval, production readiness, or an allow/deny decision
```

Run the full public QA gate:

```bash
make qa-clean
```

Build and verify a release ZIP:

```bash
make qa-full
```

## Board → Buyer → Builder → Conformance path

1. **Board**: use `workshops/30_min_board_briefing.md` and `docs/25-public-evidence-ladder.md` to frame why access, permission, execution, and acceptance are different questions.
2. **Buyer**: use `procurement/vendor_disclosure_questions.md` and `procurement/rfp_clause_library.md` to request action-level evidence without asking for private implementation details.
3. **Builder**: use `readiness/sample_readiness_assessment.json` and `tools/readiness-index/readiness_index.py` to identify public readiness gaps.
4. **Conformance handoff**: use `metadata/external_artifact_pointer_lock.json` and `docs/26-readiness-to-conformance-bridge.md` to point to separate conformance artifacts when education is no longer enough.

## What this release contains

- A developer-first **5-minute scenario-card linter**: `tools/scenario-card-lint/scenario_card_lint.py`.
- A **100-scenario public corpus** across ten domains for tabletop discussion, procurement, training, and public education.
- A public **Action Acceptance Readiness Index** and sample report.
- Public-safe standards/security crosswalks.
- Scenario coverage reports for the public corpus.
- Workshop materials and procurement due-diligence materials.
- A public-safe bridge to separate conformance artifacts.
- Strict release provenance: manifest verification, boundary QA, release ZIP verification, file tree, SBOM, SLSA-shaped local provenance, and release checklist.

## What this release intentionally does not contain

This package does **not** include production-grade enforcement, exact API schemas, full evidence object models, cryptographic binding methods, non-bypassable interceptor logic, PermitReceipt implementations, signed conformance vectors, certificate registry logic, runtime adapters, hardware-specific claim maps, partner deployments, unpublished patent claim language, patent claim charts, or implementation licenses.

Those omissions are intentional. This kit is for public category formation, literacy, readiness, procurement alignment, tabletop discussion, and human-centered stewardship. It is not a shortcut to deploy or certify an Acceptance Plane implementation.

## Suggested GitHub repo description

> Free public readiness kit for action acceptance before impact: scenario-card linting, readiness indexing, public evidence ladder, standards/security crosswalks, board-to-builder workshop materials, and a public-safe bridge to separate conformance artifacts.

## Suggested GitHub topics

`agentic-ai`, `ai-infrastructure`, `ai-security`, `ai-governance`, `action-acceptance`, `acceptance-plane`, `fail-closed-autonomy`, `public-readiness`, `scenario-cards`, `readiness-index`, `ai-risk-management`, `agentic-security`

## Start here

1. Run `make demo` and `make readiness-demo`.
2. Read `docs/00-executive-summary.md` and `docs/25-public-evidence-ladder.md`.
3. Review `docs/26-readiness-to-conformance-bridge.md` before discussing external conformance artifacts.
4. Use `workshops/facilitator_guide.md` for a team session.
5. Use `procurement/vendor_disclosure_questions.md` for buyer/vendor conversations.
6. Read `docs/09-publication-boundary.md`, `docs/16-public-release-boundary-checklist.md`, and `docs/17-pre-release-legal-ip-checklist.md` before publishing or adapting this package.

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
