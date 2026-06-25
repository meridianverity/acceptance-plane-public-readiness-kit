# Archive and License Boundary

The recommended first public release path is GitHub repository plus GitHub release asset. Archive deposits such as Zenodo can be added later after reviewing license metadata.

## Why this matters

The repository uses a split license model:

- Software files under `tools/`, `scripts/`, `.github/workflows/`, and the root `Makefile` are under MIT unless a file states otherwise.
- Documentation, scenario cards, templates, figures, adoption materials, launch materials, and other non-software public readiness materials are under CC BY 4.0 unless a file states otherwise.

Some archive systems emphasize a single top-level license field. That can make a split-license repository look simpler than it is. Public release notes should repeat the split-license boundary.

## Recommended order

1. Publish the GitHub repository.
2. Publish the GitHub release ZIP and `.sha256` checksum.
3. Confirm the release page shows the split-license boundary.
4. Only then consider an archive deposit, with counsel/stewardship review if needed.

## Non-grants

The archive, repository, release ZIP, and metadata do not grant any patent license, trademark license, certification right, conformance status, compliance approval, implementation right, production deployment right, or endorsement.
