#!/usr/bin/env bash
set -euo pipefail

# Run from inside the unzipped acceptance-plane-public-readiness-kit directory.
# Requires: git and GitHub CLI (`gh`) authenticated to an account with access to meridianverity.

REPO="meridianverity/acceptance-plane-public-readiness-kit"
VERSION="v0.1.4"
ZIP_ASSET="../acceptance-plane-public-readiness-kit-v0.1.4.zip"
SHA_ASSET="../acceptance-plane-public-readiness-kit-v0.1.4.zip.sha256"
DESCRIPTION="Free public readiness kit for discussing action acceptance before impact, with a 5-minute educational scenario-card linter. Not an implementation, standard, certification kit, or patent license."

make preflight
make manifest-refresh
make qa-clean

git init
git branch -M main
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.1.4"

gh repo create "$REPO"   --public   --description "$DESCRIPTION"   --homepage "https://meridianverity.com/"   --source=.   --remote=origin   --push

git tag -a "$VERSION" -m "Acceptance Plane Public Readiness Kit v0.1.4"
git push origin "$VERSION"

gh release create "$VERSION" "$ZIP_ASSET" "$SHA_ASSET"   --repo "$REPO"   --title "Acceptance Plane™ Public Readiness Kit v0.1.4"   --notes-file launch/github_release_body_v0.1.4.md   --verify-tag

cat <<'NEXT'
Next manual checks:
1. Confirm Issues and Security reporting are enabled.
2. Add repository topics from metadata/topics.txt.
3. Pin profile repos: acceptance-plane, acceptance-plane-public-readiness-kit, permit-receipt.
4. Use AAIF_FEEDBACK_INQUIRY.md only for feedback / working-group-fit inquiry.
5. Do not represent this repository as an AAIF hosted project unless AAIF accepts it through the formal process.
NEXT
