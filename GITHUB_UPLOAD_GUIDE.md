# GitHub Upload Guide — v0.2.0

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

## Local release build

```bash
make qa-full
```

Expected assets:

```text
dist/acceptance-plane-public-readiness-kit-v0.2.0.zip
dist/acceptance-plane-public-readiness-kit-v0.2.0.zip.sha256.txt
```

## Tag and release

```bash
git status --short
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.2.0"
git tag -a v0.2.0 -m "Acceptance Plane Public Readiness Kit v0.2.0"
git push origin main
git push origin v0.2.0

gh release create v0.2.0   dist/acceptance-plane-public-readiness-kit-v0.2.0.zip   dist/acceptance-plane-public-readiness-kit-v0.2.0.zip.sha256.txt   --repo meridianverity/acceptance-plane-public-readiness-kit   --title "Acceptance Plane Public Readiness Kit v0.2.0 — Board-to-Builder Readiness for Action Acceptance Before Impact"   --notes-file metadata/github_release_body_v0.2.0.md   --verify-tag
```

## Optional hosted provenance

After release, run the artifact attestation workflow and record the verification command:

```bash
gh attestation verify acceptance-plane-public-readiness-kit-v0.2.0.zip   -R meridianverity/acceptance-plane-public-readiness-kit
```

Hosted attestation is public-release provenance. The local SLSA-shaped file in `provenance/SLSA.intoto.json` is a local release record only.
