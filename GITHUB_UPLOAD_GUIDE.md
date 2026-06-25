# GitHub Upload Guide

Recommended repository:

```text
meridianverity/acceptance-plane-public-readiness-kit
```

Recommended description:

```text
Free public readiness kit for discussing action acceptance before impact, with a 5-minute educational scenario-card linter. Not an implementation, standard, certification kit, or patent license.
```

## Pre-publish local gate

```bash
cd acceptance-plane-public-readiness-kit
make preflight
make manifest-refresh
make qa-clean
```

Do not publish if this fails.

## One-time repository creation with GitHub CLI

From inside this folder:

```bash
git init
git branch -M main
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.1.4"

gh repo create meridianverity/acceptance-plane-public-readiness-kit   --public   --description "Free public readiness kit for discussing action acceptance before impact, with a 5-minute educational scenario-card linter. Not an implementation, standard, certification kit, or patent license."   --homepage "https://meridianverity.com/"   --source=.   --remote=origin   --push

git tag -a v0.1.4 -m "Acceptance Plane Public Readiness Kit v0.1.4"
git push origin v0.1.4
```

## If the GitHub repository already exists

```bash
git init
git branch -M main
git remote add origin git@github.com:meridianverity/acceptance-plane-public-readiness-kit.git
git add .
git commit -m "Release Acceptance Plane Public Readiness Kit v0.1.4"
git push -u origin main

git tag -a v0.1.4 -m "Acceptance Plane Public Readiness Kit v0.1.4"
git push origin v0.1.4
```

## GitHub release

Use release title:

```text
Acceptance Plane™ Public Readiness Kit v0.1.4
```

Use body:

```text
launch/github_release_body_v0.1.4.md
```

Attach release assets:

```text
acceptance-plane-public-readiness-kit-v0.1.4.zip
acceptance-plane-public-readiness-kit-v0.1.4.zip.sha256
```

Command:

```bash
gh release create v0.1.4   ../acceptance-plane-public-readiness-kit-v0.1.4.zip   ../acceptance-plane-public-readiness-kit-v0.1.4.zip.sha256   --repo meridianverity/acceptance-plane-public-readiness-kit   --title "Acceptance Plane™ Public Readiness Kit v0.1.4"   --notes-file launch/github_release_body_v0.1.4.md   --verify-tag
```

## After publishing

Pin repositories in this order:

1. `acceptance-plane`
2. `acceptance-plane-public-readiness-kit`
3. `permit-receipt`

Keep `acceptance-plane` as the canonical thesis/provenance repo. Keep this repo as the developer-facing free public readiness kit.
## Manual web-upload order for the batch-scenario layout

If you use the GitHub web uploader instead of GitHub CLI, upload the extracted repository contents in this order and commit after each successful batch if the UI is unstable:

1. Root files plus `.github/`, `LICENSES/`, `docs/`, `figures/`, `launch/`, `metadata/`, `playbooks/`, `scripts/`, `templates/`, `tools/`, `adoption/`, and `demos/`.
2. `scenarios/` metadata directory.
3. `scenarios_batch_1/` containing `AP-SCEN-001.json` through `AP-SCEN-050.json`.
4. `scenarios_batch_2/` containing `AP-SCEN-051.json` through `AP-SCEN-100.json`.
5. `provenance/` last, because it contains the final manifest and audit materials.

Do not upload the ZIP file itself. If an older `scenarios/cards/` directory exists in the repo, delete it before final release because the final v0.1.4 batch layout uses `scenarios_batch_1/` and `scenarios_batch_2/`.

