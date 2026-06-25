# Acceptance Plane™ Public Readiness Kit v0.1.4

**A free public readiness kit with a 5-minute educational scenario-card linter for developers.**  
**Made by Meridian Verity Group (MVG): https://meridianverity.com/**  
**Not a product implementation. Not a standard. No patent license. No certification right.**

The Acceptance Plane™ is a public architecture category for discussing action-level trust in agentic AI infrastructure: the function that determines whether a specific autonomous AI action should be accepted by a protected system before impact, based on current, scope-bound, verifier-ready evidence at the acceptance boundary.

This kit helps developers, buyers, auditors, researchers, public-sector teams, nonprofits, and public-interest organizations ask one practical pre-impact question:

> Should this exact autonomous action be accepted by this protected system right now?

## 5-minute developer quickstart

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
```

No API keys. No services. No package install. Python standard library only.

Expected result:

```text
Status: DISCUSSION_READY
- The card has enough public structure for tabletop discussion.
- This is not certification, compliance approval, production readiness, or an allow/deny decision.
```

Run the full public QA gate, including the standard-library unit test:

```bash
make qa
```

For a clean local check that removes generated Python cache files before and after QA:

```bash
make qa-clean
```

## What this release contains

- A developer-first **5-minute scenario-card linter**: `tools/scenario-card-lint/scenario_card_lint.py`.
- A **100-scenario public corpus** across ten domains for tabletop discussion, procurement, training, and public education.
- Scenario cards are organized into two upload-friendly batches: `scenarios_batch_1/` and `scenarios_batch_2/`; shared index/schema material is in `scenarios/`.
- A public **Open Profile** for vocabulary: compute plane, control plane, data plane, acceptance plane, acceptance boundary, gate-time evidence, ACCEPT / HOLD / REFUSE.
- Readiness material for enterprise, public-sector, healthcare, finance, cloud, education, AR/VR, sensor, robotics, and personal-agent contexts.
- Adoption templates for boards, policy teams, public-sector buyers, nonprofits, vendors, and standards-adjacent conversations.
- Strict public-release provenance: full-repo boundary QA, manifest verification, file tree, QA report, and release checklist.
- A public **AAIF feedback-inquiry path** that explicitly avoids premature hosted-project claims.

## What this release intentionally does not contain

This package does **not** include production-grade enforcement, exact API schemas, full evidence object models, cryptographic binding methods, non-bypassable interceptor logic, PermitReceipt implementations, signed conformance vectors, certificate registry logic, runtime adapters, hardware-specific claim maps, partner deployments, or unpublished patent claim language.

Those omissions are intentional. This kit is for public category formation, literacy, readiness, procurement alignment, tabletop discussion, and human-centered stewardship. It is not a shortcut to deploy or certify an Acceptance Plane implementation.

## Start here

1. Run [`make demo`](Makefile) or read [`QUICKSTART.md`](QUICKSTART.md).
2. Read [`docs/00-executive-summary.md`](docs/00-executive-summary.md).
3. Review [`docs/01-open-profile.md`](docs/01-open-profile.md).
4. Explore the scenario corpus at [`scenarios/index.csv`](scenarios/index.csv).
5. Run the linter directly:

```bash
python3 tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/AP-SCEN-001.json scenarios_batch_1/AP-SCEN-050.json scenarios_batch_2/AP-SCEN-100.json
```

6. Use [`templates/rfp_questionnaire.md`](templates/rfp_questionnaire.md) and [`adoption/procurement_scorecard.md`](adoption/procurement_scorecard.md) for public readiness discussions.
7. Read [`AAIF_FEEDBACK_INQUIRY.md`](AAIF_FEEDBACK_INQUIRY.md) before any standards/foundation outreach.
8. Read [`GITHUB_UPLOAD_GUIDE.md`](GITHUB_UPLOAD_GUIDE.md) before publishing the repository.


## Enterprise evaluator path

For reviewers who want a fast but disciplined evaluation flow:

1. Run [`make demo`](Makefile).
2. Read [`docs/21-public-threat-model.md`](docs/21-public-threat-model.md).
3. Follow [`docs/22-one-hour-enterprise-evaluator-script.md`](docs/22-one-hour-enterprise-evaluator-script.md).
4. Review [`docs/23-archive-and-license-boundary.md`](docs/23-archive-and-license-boundary.md) before any archive deposit.
5. Verify release integrity with [`docs/24-release-integrity.md`](docs/24-release-integrity.md).

## Suggested GitHub repo description

> Free public readiness kit for discussing action acceptance before impact, with a 5-minute educational scenario-card linter. Not an implementation, standard, certification kit, or patent license.

## Suggested GitHub topics

`agentic-ai`, `ai-infrastructure`, `ai-security`, `ai-governance`, `action-acceptance`, `acceptance-plane`, `fail-closed-autonomy`, `public-readiness`, `scenario-cards`, `verifier-ready-evidence`

## License and rights boundary

This repository uses a public license split:

- **Software files** under `tools/`, `scripts/`, `.github/workflows/`, and the root `Makefile` are provided under the MIT License unless a file states otherwise.
- **Text, documentation, figures, templates, scenario cards, launch materials, and adoption materials** are provided under Creative Commons Attribution 4.0 International (CC BY 4.0) unless a file states otherwise.

This public kit does **not** grant any patent license, trademark license, service mark license, product implementation license, certification right, compliance approval, endorsement, or right to use Meridian Verity Group names, logos, marks, or framework identifiers as source-identifying marks. See [`PATENT_AND_TRADEMARK_NOTICE.md`](PATENT_AND_TRADEMARK_NOTICE.md), [`ATTRIBUTION.md`](ATTRIBUTION.md), and [`docs/19-license-and-rights-boundary.md`](docs/19-license-and-rights-boundary.md).

## Citation

Canonical public architecture thesis:

Lee, Scott. Meridian Verity Group. (2026). *The Acceptance Plane: The Missing Trust Layer for Agentic AI Infrastructure* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20645907

## Release principle

> Open the question. Protect the mechanism. Help the world refuse unsafe autonomous action before impact.
