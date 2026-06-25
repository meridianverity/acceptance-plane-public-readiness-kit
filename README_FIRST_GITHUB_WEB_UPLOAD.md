# GitHub web paste pack for v0.1.4 hidden files

Do **not** upload these visible `.txt` helper files into the repository.
They are only copy/paste helpers because GitHub web upload may reject hidden dotfiles with “This file is hidden.”

Use **Add file → Create new file** in GitHub for each target path below.
Paste the contents from the matching helper file, then commit.

## Create these 9 files exactly

1. Target path: `.editorconfig`  
   Paste from: `files_to_copy/01_PASTE_AS_.editorconfig.txt`

2. Target path: `.gitattributes`  
   Paste from: `files_to_copy/02_PASTE_AS_.gitattributes.txt`

3. Target path: `.gitignore`  
   Paste from: `files_to_copy/03_PASTE_AS_.gitignore.txt`

4. Target path: `.zenodo.json`  
   Paste from: `files_to_copy/04_PASTE_AS_.zenodo.json.txt`

5. Target path: `.github/CODEOWNERS`  
   Paste from: `files_to_copy/05_PASTE_AS_.github_CODEOWNERS.txt`

6. Target path: `.github/ISSUE_TEMPLATE/boundary_report.yml`  
   Paste from: `files_to_copy/06_PASTE_AS_.github_ISSUE_TEMPLATE_boundary_report.yml.txt`

7. Target path: `.github/ISSUE_TEMPLATE/config.yml`  
   Paste from: `files_to_copy/07_PASTE_AS_.github_ISSUE_TEMPLATE_config.yml.txt`

8. Target path: `.github/ISSUE_TEMPLATE/scenario_card.yml`  
   Paste from: `files_to_copy/08_PASTE_AS_.github_ISSUE_TEMPLATE_scenario_card.yml.txt`

9. Target path: `.github/workflows/qa.yml`  
   Paste from: `files_to_copy/09_PASTE_AS_.github_workflows_qa.yml.txt`

## Recommended commit message

`Add release gate dotfiles and GitHub QA workflow`

## After commit

Refresh the repository page. You should see:

- `.github/` folder at repo root
- `.gitignore`
- `.gitattributes`
- `.editorconfig`
- `.zenodo.json`
- Actions tab showing the `Public Readiness Kit QA` workflow

Then create GitHub Release `v0.1.4` with Release label `None`.
