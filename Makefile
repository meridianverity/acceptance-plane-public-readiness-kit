QA_PYTHON ?= python3
VERSION := 0.2.0
RELEASE_ZIP := dist/acceptance-plane-public-readiness-kit-v$(VERSION).zip
RELEASE_SHA := $(RELEASE_ZIP).sha256.txt
export PYTHONDONTWRITEBYTECODE=1

.PHONY: doctor demo demo-json readiness-demo readiness-json readiness-check crosswalk-check coverage-check coverage-refresh workshop-demo workshop-check external-pointer-check unit-test qa qa-clean qa-full clean sample-check full-check boundary-check manifest manifest-refresh file-tree preflight release-check release-zip verify-release package

doctor:
	@echo "Acceptance Plane Public Readiness Kit v$(VERSION)"
	@echo "Python: $$($(QA_PYTHON) --version)"
	@echo "Repo boundary: not an implementation, standard, certification kit, or production allow/deny system."
	@echo "Runtime dependencies: Python standard library only."

demo:
	@echo "Acceptance Plane Public Readiness Kit — 5-minute educational demo"
	@echo "Boundary: not an implementation, standard, certification kit, or production allow/deny system."
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/AP-SCEN-001.json scenarios_batch_1/AP-SCEN-050.json scenarios_batch_2/AP-SCEN-100.json

demo-json:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --format json scenarios_batch_1/AP-SCEN-001.json scenarios_batch_1/AP-SCEN-050.json scenarios_batch_2/AP-SCEN-100.json

readiness-demo:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format markdown

readiness-json:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format json

readiness-check:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format json > /tmp/action-acceptance-readiness-index.json

crosswalk-check:
	$(QA_PYTHON) tools/crosswalk-lint/crosswalk_lint.py

coverage-check:
	$(QA_PYTHON) tools/scenario-coverage/scenario_coverage.py

coverage-refresh:
	$(QA_PYTHON) tools/scenario-coverage/scenario_coverage.py --write

workshop-demo:
	$(QA_PYTHON) tools/workshop-pack/workshop_pack.py --out /tmp/acceptance-plane-workshop-pack

workshop-check:
	$(QA_PYTHON) tools/workshop-pack/workshop_pack.py --out /tmp/acceptance-plane-workshop-pack-check

external-pointer-check:
	$(QA_PYTHON) tools/external-pointer-check/external_pointer_check.py

unit-test:
	$(QA_PYTHON) -m unittest discover -s tools/scenario-card-lint/tests -p "test_*.py"

sample-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py scenarios_batch_1/AP-SCEN-001.json

full-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/*.json scenarios_batch_2/*.json > /tmp/scenario-card-lint.txt

boundary-check:
	$(QA_PYTHON) scripts/public_boundary_qa.py

manifest:
	$(QA_PYTHON) scripts/verify_manifest.py

file-tree:
	@find . -path './.git' -prune -o -path './dist' -prune -o -type f -print | sed 's#^./##' | sort > provenance/FILE_TREE.txt

manifest-refresh: clean coverage-refresh readiness-check file-tree
	$(QA_PYTHON) scripts/write_manifest.py

qa: unit-test full-check readiness-check crosswalk-check coverage-check workshop-check external-pointer-check boundary-check manifest

qa-clean:
	$(MAKE) clean
	$(MAKE) qa
	$(MAKE) clean

release-zip: qa-clean
	$(QA_PYTHON) scripts/build_release_zip.py

verify-release:
	$(QA_PYTHON) scripts/verify_release_artifact.py $(RELEASE_ZIP) --sha256-file $(RELEASE_SHA)

qa-full: release-zip verify-release
	@echo "qa-full: PASS"

preflight: doctor demo readiness-demo qa-clean
	@echo "Preflight passed. Review RELEASE_CHECKLIST.md and GITHUB_UPLOAD_GUIDE.md before publishing."

release-check: qa-full
	@echo "Release gate passed for v$(VERSION)."

package: release-zip

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist
