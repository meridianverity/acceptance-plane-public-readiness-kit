# Release Integrity

This repository treats the ZIP, manifest, checksum, and Git tag as separate integrity signals.

## Local gates

```bash
make demo
make qa-clean
make manifest-refresh
make qa-clean
```

## Manifest

`provenance/MANIFEST.sha256` lists repository files and SHA-256 digests. It intentionally excludes itself and local/generated runtime artifacts such as `.git/`, Python bytecode, cache directories, virtual environments, `build/`, and `dist/`.

## ZIP checksum

Every shared release ZIP should be accompanied by a `.sha256` file.

## Git release tag

Use a standard release tag such as `v0.1.4`. Create the tag locally, push it, then create the GitHub release with `--verify-tag` so the release command aborts if the tag is missing.

## Boundary

Passing these integrity checks means the public artifact is internally consistent. It does not mean certification, conformance, compliance approval, production readiness, or implementation completeness.
