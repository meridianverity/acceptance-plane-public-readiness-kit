# Attestation and Provenance Note — v0.3.4

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

This repository intentionally does **not** bundle a completed local `SLSA.intoto.json` statement for the release ZIP.

Reason: the final ZIP digest is only known after every in-archive byte is fixed. If a completed statement inside the ZIP names the ZIP digest, changing the statement changes the ZIP digest again. That creates circular provenance and invites placeholder fields.

The v0.3.4 release path uses three non-circular integrity signals instead:

1. `provenance/MANIFEST.sha256` locks every repository release file except the manifest itself.
2. `dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt` records the final release ZIP digest after deterministic build.
3. GitHub artifact attestation is generated after `make qa-full` for the built ZIP and verified against the released asset.

Local files in this repository are public release records and verification aids only. Completed hosted attestation is created outside the ZIP by the release workflow after the artifact exists.
