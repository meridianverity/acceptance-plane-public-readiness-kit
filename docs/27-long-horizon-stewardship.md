# Long-Horizon Stewardship

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

This note describes how the public readiness kit should remain understandable, verifiable, and safe to reuse over a long horizon. It is a stewardship posture, not a guarantee of maintenance, support, compliance, certification, or implementation completeness.

## Stewardship question

Could a future reviewer understand what this artifact was, what it was not, how it was verified, and why the public/private boundary mattered without relying on private context?

## Principles

1. **Receipts over promises.** Preserve verifiable artifacts: manifest, checksum sidecar, release tag, release body, public-state note, and hosted artifact attestation.
2. **Boundary before expansion.** New educational material must not drift into production verifier logic, exact evidence schemas, cryptographic binding methods, non-bypassable enforcement mechanisms, conformance vectors, certificate registries, claim charts, or private licensing maps.
3. **Plain-language survivability.** Keep the core question visible: should this exact autonomous action be accepted by this protected system right now?
4. **Deterministic packaging.** Release ZIPs should be reproducible from the same source bytes, independent of source-file modification times.
5. **Citation continuity.** Keep the canonical DOI and CFF metadata aligned with the current public architecture record.
6. **Public-safe evidence ladder.** Keep readiness, procurement, workshop, and conformance-handoff material separated so readers do not mistake readiness discussion for certification or production approval.
7. **Human consequence.** Preserve the reason the boundary exists: downstream people should not absorb avoidable harm from missing, stale, mismatched, or unreplayable proof.

## Review cadence

Before each public release, run the technical QA gates and also ask:

- Does the first page still state the boundary clearly?
- Are release assets deterministic and hash-verifiable?
- Are visual assets regenerated from their current sources and hash-locked?
- Does the release avoid private mechanisms, customer material, and claim-level disclosures?
- Does the public language match the current Meridian Verity public surface without copying transient marketing text into technical claims?
- Is any external artifact referenced only by pointer lock and separated from this public kit?

## Non-goals

This note does not promise long-term support, legal sufficiency, standards status, conformance coverage, certification coverage, procurement acceptance, production readiness, patent coverage, or commercial availability. Those questions require separate written scope and review.
