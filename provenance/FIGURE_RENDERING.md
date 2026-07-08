# Figure Rendering Note — v0.3.4

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

The public PNG figures in `figures/` were regenerated from the current SVG sources during the v0.2.1 HOLD-fix pass and re-verified during v0.3.4 packaging.

Locked figures:

- `figures/acceptance-plane-stack.svg` → `figures/acceptance-plane-stack.png`
- `figures/acceptance-plane-workflow.svg` → `figures/acceptance-plane-workflow.png`

The SVG sources contain the canonical DOI `10.5281/zenodo.20683834`. The rendered PNG files are checked by `scripts/verify_figure_assets.py` against `provenance/FIGURE_ASSET_LOCK.json` for hash and dimensions. This is a release-integrity check only; it is not certification, conformance evidence, production readiness, or implementation evidence.
