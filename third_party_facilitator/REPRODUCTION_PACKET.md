# Third-party facilitator reproduction packet

This packet lets an outside facilitator reproduce the public readiness workflow without becoming an implementation verifier or certification body.

Suggested reproduction path:

1. Verify the release ZIP SHA-256 sidecar.
2. Run `make qa-full` from a fresh checkout or fresh ZIP.
3. Run a public workshop using `workshops/facilitator_guide.md`.
4. Generate a public readiness report with `make report-demo`.
5. Fill `result-template.json` with the observed public outputs.

Boundary: this packet records public educational reproducibility only. It is not certification, compliance approval, production readiness, procurement approval, conformance approval, implementation validation, or a patent license.
