# v0.3.2 Language-Polish Audit

Result: PASS. Verified by `make qa-full` for the v0.3.2 release artifact.

## What changed

- Removed visible editorial scars from the 300-card public scenario corpus.
- Added `tools/scenario-language-polish/scenario_language_polish_qa.py`.
- Added `make scenario-language-polish-check` and included it in `make qa` / `make qa-full`.
- Updated legal/IP and provenance references to the 300-card public corpus.
- Kept canonical dotted release filenames for the release ZIP and SHA-256 sidecar.

## Language gate

The release gate rejects:

- a duplicated `before` token;
- incorrect incident-tabletop article phrasing;
- incorrect operator-handoff article phrasing;
- incorrect article usage before incident/operator nouns in high-signal scenario fields.

## Boundary

This is an editorial stewardship gate for public educational materials only. It is not certification, compliance approval, procurement approval, conformance testing, production readiness, a patent claim chart, a patent license, or an allow/deny decision.
