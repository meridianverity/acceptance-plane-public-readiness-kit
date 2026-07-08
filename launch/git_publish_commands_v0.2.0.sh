#!/usr/bin/env bash
set -euo pipefail

REPO="meridianverity/acceptance-plane-public-readiness-kit"
VERSION="v0.2.0"
ZIP_ASSET="dist/acceptance-plane-public-readiness-kit-v0.2.0.zip"
SHA_ASSET="dist/acceptance-plane-public-readiness-kit-v0.2.0.zip.sha256.txt"

make qa-full

git status --short
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.2.0"
git tag -a "$VERSION" -m "Acceptance Plane Public Readiness Kit v0.2.0"
git push origin main
git push origin "$VERSION"

gh release create "$VERSION" "$ZIP_ASSET" "$SHA_ASSET"   --repo "$REPO"   --title "Acceptance Plane Public Readiness Kit v0.2.0 — Board-to-Builder Readiness for Action Acceptance Before Impact"   --notes-file metadata/github_release_body_v0.2.0.md   --verify-tag
