# V407 Dual-Gate Conformance Corpus Overlay v2 — Manual Upload Safe

This v2 overlay fixes the manual-upload problem caused by the exploded `assets2/corpus/...` tree in the prior V407 overlay.

## What changed in v2

- Removed the 100+ exploded `assets2/corpus/dual-gate-conformance/...` files from the overlay.
- Kept the full corpus as one downloadable dataset archive under `datasets/dual-gate-conformance-corpus/MVG-DGER-CORPUS-2026-001_v1.0.0_PUBLIC_SYNTHETIC.zip`.
- Added one compact browser fixture index at `assets2/fixtures/dual-gate-replay/v407/index.json` so the replay console still runs locally without individual corpus JSON files.
- Patched the replay console to use the compact index and route corpus vector / EvidencePack links to the dataset page or ZIP.
- Patched conformance pages to link to `/datasets/dual-gate-conformance-corpus/index.json` instead of the removed `assets2/corpus` path.
- Patched `assets2/ui/global-nav-premium.v406.js` in-place with the quiet Conformance Corpus link so no sitewide HTML nav-reference churn is needed.

## Manual upload counts

- Total overlay files: 22
- `assets2/` files in overlay: 7
- `assets2/corpus/` files in overlay: 0
- Corpus remains available as a single ZIP: `MVG-DGER-CORPUS-2026-001_v1.0.0_PUBLIC_SYNTHETIC.zip`

## Guardrails

- No public NVIDIA-specific corpus.
- No customer data.
- No secrets.
- No private vendor fields.
- No production credentials.
- No production authorization credential.
- No vendor certification / integration claim.
- No patent license or implementation right by publication.
- No `.well-known`, PGP/ASC, DSSE, state JSON, signatures, or trust artifacts included.
