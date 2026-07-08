# v0.2.0 Upload Strategy

Boundary: public readiness release only. Not implementation, standard, certification, compliance approval, or patent license.

1. Run `make qa-full`.
2. Upload the ZIP and SHA sidecar from `dist/`.
3. Use `metadata/github_release_body_v0.2.0.md` as the release body.
4. After publishing, run GitHub artifact attestation if the repository is public and the workflow is enabled.
5. Do not upload private implementation materials, claim charts, customer mappings, or production evidence schemas.
