# Acceptance Plane Public Readiness Kit v0.3.4 — Release-Surface Locked Public Readiness Corpus for Action Acceptance Before Impact

Free public readiness operating system for discussing action acceptance before impact: 300 curated public scenario cards with uniqueness QA, language-polish QA, release-surface polish QA, scenario-card linting, Action Acceptance Readiness Index, browser-only readiness demo, Markdown/JSON public report generator, scenario and crosswalk coverage reports, public evidence ladder, board-to-builder workshop materials, procurement question pack, facilitator reproduction packet, adoption evidence template, and a public-safe bridge to separate conformance artifacts. Not an implementation, standard, certification kit, compliance approval, patent license, or production allow/deny system.

## What changed in v0.3.4

v0.3.4 is a release-surface polish patch for the v0.3.x public readiness operating system. It preserves the curated 300-card public educational corpus and closes the last visible release-facing editorial issues found after the previous patch.

- Removes the duplicate previous-version changelog heading.
- Polishes visible release-surface wording in changelog and corpus stewardship docs.
- Adds `tools/release-surface-polish/release_surface_polish_qa.py`.
- Wires `release-surface-polish-check` into `make qa` and `make qa-full`.
- Keeps scenario-card linting, scenario uniqueness QA, scenario language-polish QA, readiness index, browser demo, public report generator, crosswalks, workshop pack, procurement pack, facilitator packet, external pointer lock, deterministic ZIP, reproducible ZIP check, figure lock, and public boundary QA.

## Boundary

This is a public education and readiness discussion kit. It is not an implementation, standard, certification kit, compliance approval, patent license, production verifier, conformance suite, or production allow/deny system.

## Suggested verification

```bash
sha256sum -c acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt
unzip acceptance-plane-public-readiness-kit-v0.3.4.zip
cd acceptance-plane-public-readiness-kit
make qa-full
```

Do not describe v0.3.4 as publicly released until the GitHub tag, release page, ZIP asset, SHA-256 sidecar, and checksum match are visible on the public repository.
