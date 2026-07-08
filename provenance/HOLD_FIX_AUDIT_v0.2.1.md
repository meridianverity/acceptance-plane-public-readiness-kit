# HOLD Fix Audit — Acceptance Plane Public Readiness Kit v0.2.1

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

This audit records the v0.2.1 pass that converted the v0.2.0 HOLD findings into release-gated checks.

## Fixes

1. **Rendered PNG DOI drift fixed**
   - Regenerated `figures/acceptance-plane-stack.png` from `figures/acceptance-plane-stack.svg`.
   - Regenerated `figures/acceptance-plane-workflow.png` from `figures/acceptance-plane-workflow.svg`.
   - Added `provenance/FIGURE_ASSET_LOCK.json` and `scripts/verify_figure_assets.py` so figure hashes, dimensions, and SVG DOI text are checked by QA.

2. **Local SLSA placeholder removed**
   - Removed completed-looking local SLSA/in-toto JSON from the release package.
   - Added `provenance/ATTESTATION_PROVENANCE_NOTE.md` explaining why completed provenance for the ZIP must be generated after the ZIP exists.
   - Kept GitHub artifact attestation in the release workflow.

3. **Deterministic ZIP construction fixed**
   - `scripts/build_release_zip.py` now writes fixed ZIP member timestamps, deterministic Unix modes, sorted paths, and a single archive root.
   - Added `scripts/verify_reproducible_zip.py` and `make reproducible-zip-check`.
   - `make qa-full` runs release verification, reproducibility verification, and a final release verification pass.

4. **Citation metadata fixed**
   - `CITATION.cff` uses full `YYYY-MM-DD` dates for the kit and preferred public architecture record.

5. **Long-horizon stewardship added**
   - Added `docs/27-long-horizon-stewardship.md`.
   - Added `docs/28-public-surface-alignment.md` for Meridian Verity public-surface language discipline.

## Result

The release gate is now stricter than the v0.2.0 gate: the original blockers are fixed and the checks that would have caught them are part of the public QA path.
