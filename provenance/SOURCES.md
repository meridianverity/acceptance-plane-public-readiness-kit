# Sources and Provenance

This public readiness kit is based on the Acceptance Plane public architecture thesis and related public release materials.

Canonical public architecture thesis DOI: 10.5281/zenodo.20645907

Key release boundary preserved in this kit:

- Public materials define the category, workflow, vocabulary, conceptual diagrams, scenario corpus, public-interest guidance, and procurement questions.
- Private/licensed materials retain implementation-level details such as exact API schemas, full evidence object models, cryptographic binding, enforcement pipelines, hardware-specific claim maps, partner deployments, conformance certification, certificate registries, signed test vectors, and unpublished patent language.

v0.1.2 provenance hardening:

- Full-repo text boundary QA scans public files for unsafe positive implementation/certification/conformance/standard/patent-license claims.
- Strict SHA-256 manifest verification fails on unmanifested files and stale manifest entries.
- `provenance/FILE_TREE.txt` and `provenance/QA_REPORT.md` are included in the manifest.
- The only file intentionally excluded from the manifest is `provenance/MANIFEST.sha256` itself.

No patent PDFs, claim charts, partner materials, private implementation files, production schemas, production verifier code, signed conformance vectors, or certificate-registry implementations are included in this package.


v0.1.4 public polish hardening:

- Public wording polish and release-command safety.
- Playbook rename to production-boundary-first language.
- Public threat model, evaluator script, archive/license boundary guide, release-integrity guide.
- Demo transcript, JSON demo output, and SPDX-style public SBOM.
