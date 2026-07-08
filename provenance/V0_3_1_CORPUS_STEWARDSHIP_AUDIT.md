# v0.3.1 Corpus Stewardship Audit

Result: PASS. Verified by `make qa-full` for the v0.3.1 release artifact.

This patch addresses the final pre-release micro-HOLDs found in the v0.3.0 release candidate:

- Removes id-normalized duplicate cards from the 300-card public educational corpus.
- Removes repeated title/scenario pairs.
- Rewrites high-signal explanatory fields so `why`, `human_impact`, `learning_goal`, and `acceptance_boundary` are unique across all cards.
- Adds `tools/scenario-uniqueness/scenario_uniqueness_qa.py` and runs it in release QA.
- Updates Korean summary language from earlier 100-card wording to the v0.3.x 300-card public corpus.
- Uses canonical dotted release asset naming for the v0.3.1 release ZIP and SHA-256 sidecar.

Boundary: corpus stewardship and release integrity only. Not certification, compliance approval, production readiness, conformance testing, or an allow/deny decision.
