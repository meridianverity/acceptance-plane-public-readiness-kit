# Copy/paste contents for 9 hidden GitHub files

Use GitHub **Add file → Create new file**. For each file, type the target path exactly, paste the matching block, and commit.

## .editorconfig

```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[*.{json,yml,yaml,py,txt,csv}]
indent_style = space
indent_size = 2

[*.py]
indent_size = 4
```

## .gitattributes

```
* text=auto eol=lf
*.png binary
*.zip binary
*.sha256 text eol=lf
```

## .gitignore

```
__pycache__/
*.pyc
.DS_Store
.env
.venv/
venv/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/
*.log
dist/
build/
*.zip
*.zip.sha256
```

## .zenodo.json

```
{
  "title": "Acceptance Plane™ Public Readiness Kit",
  "upload_type": "other",
  "description": "A free public readiness kit with a 5-minute educational scenario-card linter for developers. Not a product implementation. Not a standard. No patent license. No certification right.",
  "creators": [
    {
      "name": "Lee, Scott",
      "affiliation": "Meridian Verity Group"
    }
  ],
  "license": "cc-by-4.0",
  "version": "0.1.4",
  "keywords": [
    "Acceptance Plane",
    "Agentic AI",
    "AI Infrastructure",
    "Action Acceptance",
    "Acceptance Boundary",
    "Verifier-Ready Evidence",
    "Fail-Closed Autonomy",
    "AI Security",
    "AI Governance",
    "Public Readiness",
    "Scenario Corpus",
    "Scenario Card Linter"
  ],
  "related_identifiers": [
    {
      "identifier": "10.5281/zenodo.20645907",
      "relation": "isSupplementTo",
      "scheme": "doi"
    }
  ],
  "notes": "Software portions are under MIT; non-software public readiness materials are under CC BY 4.0 unless a file states otherwise. This metadata is for optional archival use only and must be reviewed before enabling automated archive deposits. No patent license, trademark license, certification right, compliance approval, or implementation right is granted."
}
```

## .github/CODEOWNERS

```
# Optional CODEOWNERS file.
# After the GitHub organization/team is created, uncomment and replace the team below.
# * @meridianverity/maintainers
```

## .github/ISSUE_TEMPLATE/boundary_report.yml

```
name: Boundary report
description: Report public wording that may blur implementation, certification, patent, trademark, or private-mechanism boundaries.
title: "Boundary report: "
labels: ["boundary-review"]
body:
  - type: markdown
    attributes:
      value: |
        Use this only for public, non-sensitive wording issues. Do not include confidential implementation details, private partner material, claim charts, credentials, unpublished patent language, or secrets.
  - type: input
    id: file_path
    attributes:
      label: File or section
      description: Where did you see the issue?
    validations:
      required: true
  - type: textarea
    id: concern
    attributes:
      label: Concern
      description: Describe why the wording may imply implementation, certification, patent/trademark permission, or a private mechanism.
    validations:
      required: true
  - type: textarea
    id: suggested_fix
    attributes:
      label: Suggested public-safe wording
      description: Optional replacement wording.
    validations:
      required: false
```

## .github/ISSUE_TEMPLATE/config.yml

```
blank_issues_enabled: false
contact_links:
  - name: Confidential boundary or security report
    url: https://github.com/meridianverity/acceptance-plane-public-readiness-kit/security/advisories/new
    about: Use GitHub Security Advisories for accidental implementation disclosure, private material, or false certification claims.
```

## .github/ISSUE_TEMPLATE/scenario_card.yml

```
name: Scenario card proposal
description: Propose a public scenario card for tabletop discussion.
title: "Scenario proposal: "
labels: ["scenario", "public-readiness"]
body:
  - type: markdown
    attributes:
      value: |
        Scenario cards must remain high-level public discussion materials. Do not submit exact schemas, cryptographic methods, production mechanisms, partner deployments, claim charts, or private data.
  - type: input
    id: domain
    attributes:
      label: Domain
      placeholder: healthcare_dsi, public_sector, robotics_physical, etc.
    validations:
      required: true
  - type: input
    id: expected_decision
    attributes:
      label: Expected discussion decision
      placeholder: ACCEPT / HOLD / REFUSE
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Scenario
      description: Public, high-level description only.
    validations:
      required: true
  - type: textarea
    id: human_impact
    attributes:
      label: Human impact
      description: Who could be helped or harmed if the action is accepted without enough proof?
    validations:
      required: true
```

## .github/workflows/qa.yml

```
name: Public Readiness Kit QA

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  qa:
    runs-on: ubuntu-latest
    env:
      PYTHONDONTWRITEBYTECODE: "1"
    steps:
      - uses: actions/checkout@v4
      - name: Show Python version
        run: python3 --version
      - name: Run public preflight
        run: make preflight
```

