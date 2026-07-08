# Release-surface polish — v0.3.4

v0.3.4 treats the first screen of a public release as part of release integrity. A package can pass manifest, scenario, boundary, and reproducibility checks while still losing reviewer trust if the public release surface contains duplicate headings, repeated words, awkward phrase-family wording, or stale active release pointers.

This release adds a dedicated release-surface polish gate for files that a reviewer is likely to read first: README, changelog, release body, release title and description, upload guide, release checklist, launch notes, and the corpus-language stewardship documents.

The gate checks for:

- duplicate version headings in `CHANGELOG.md`;
- repeated-word scars such as duplicate-adjective wording;
- awkward phrase-family wording in release notes;
- stale active release pointers to the immediately previous release in active release files;
- underscore release asset names in active release-facing files.

Boundary: this is editorial release-surface QA for a public education and readiness kit. It is not certification, compliance approval, production readiness, conformance, or an allow/deny decision.
