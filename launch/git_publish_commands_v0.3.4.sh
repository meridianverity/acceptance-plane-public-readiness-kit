#!/usr/bin/env bash
set -euo pipefail

python3 scripts/build_release_zip.py
sha256sum -c dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt
python3 scripts/verify_release_artifact.py dist/acceptance-plane-public-readiness-kit-v0.3.4.zip --sha256-file dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt

git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.3.4"
git tag -a v0.3.4 -m "Acceptance Plane Public Readiness Kit v0.3.4"
git push origin main
git push origin v0.3.4

gh release create v0.3.4 \
  dist/acceptance-plane-public-readiness-kit-v0.3.4.zip \
  dist/acceptance-plane-public-readiness-kit-v0.3.4.zip.sha256.txt \
  --title "Acceptance Plane Public Readiness Kit v0.3.4 — Release-Surface Locked Public Readiness Corpus for Action Acceptance Before Impact" \
  --notes-file metadata/github_release_body_v0.3.4.md \
  --verify-tag
