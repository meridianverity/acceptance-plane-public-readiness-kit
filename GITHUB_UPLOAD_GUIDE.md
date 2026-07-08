# GitHub Upload Guide — v0.3.4

Run locally before publication:

```bash
make qa-full
sha256sum -c dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt
```

Expected assets:

```text
dist/acceptance-plane-public-readiness-kit-v0.3.4.zip
dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt
```

Publish:

```bash
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.3.4"
git tag -a v0.3.4 -m "Acceptance Plane Public Readiness Kit v0.3.4"
git push origin main
git push origin v0.3.4

gh release create v0.3.4   dist/acceptance-plane-public-readiness-kit-v0.3.4.zip   dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt   --repo meridianverity/acceptance-plane-public-readiness-kit   --title "Acceptance Plane Public Readiness Kit v0.3.4 — Release-Surface Locked Public Readiness Corpus for Action Acceptance Before Impact"   --notes-file metadata/github_release_body_v0.3.4.md   --verify-tag
```

Hosted attestation should be attached by GitHub Actions after public build. Local JSON is not a substitute for hosted provenance.
