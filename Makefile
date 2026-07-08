QA_PYTHON ?= python3
VERSION := 0.3.4
RELEASE_ZIP := dist/acceptance-plane-public-readiness-kit-v$(VERSION).zip
RELEASE_SHA := $(RELEASE_ZIP).sha256.txt
export PYTHONDONTWRITEBYTECODE=1

.NOTPARALLEL: qa-full release-zip verify-release reproducible-zip-check

.PHONY: doctor demo demo-json readiness-demo readiness-json readiness-check report-demo report-check browser-demo-check crosswalk-check crosswalk-coverage-check coverage-check scenario-uniqueness-check scenario-language-polish-check release-surface-polish-check coverage-refresh workshop-demo workshop-check facilitator-check external-pointer-check figure-check unit-test qa qa-clean qa-full clean sample-check full-check boundary-check manifest manifest-refresh file-tree preflight release-check release-zip verify-release reproducible-zip-check package

doctor:
	@echo "Acceptance Plane Public Readiness Kit v$(VERSION)"
	@echo "Python: $$($(QA_PYTHON) --version)"
	@echo "Repo boundary: not an implementation, standard, certification kit, or production allow/deny system."
	@echo "Runtime dependencies: Python standard library only."

demo:
	@echo "Acceptance Plane Public Readiness Kit — 5-minute educational demo"
	@echo "Boundary: not an implementation, standard, certification kit, or production allow/deny system."
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/AP-SCEN-001.json scenarios_batch_3/AP-SCEN-150.json scenarios_batch_6/AP-SCEN-300.json

demo-json:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --format json scenarios_batch_1/AP-SCEN-001.json scenarios_batch_3/AP-SCEN-150.json scenarios_batch_6/AP-SCEN-300.json

readiness-demo:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format markdown

readiness-json:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format json

readiness-check:
	$(QA_PYTHON) tools/readiness-index/readiness_index.py readiness/sample_readiness_assessment.json --format json > /tmp/action-acceptance-readiness-index.json

report-demo:
	$(QA_PYTHON) tools/public-report/public_report.py --out /tmp/acceptance-plane-public-readiness-report

report-check:
	$(QA_PYTHON) tools/public-report/public_report.py --out /tmp/acceptance-plane-public-readiness-report-check

browser-demo-check:
	$(QA_PYTHON) tools/static-readiness-demo/static_demo_check.py

crosswalk-check:
	$(QA_PYTHON) tools/crosswalk-lint/crosswalk_lint.py

crosswalk-coverage-check:
	$(QA_PYTHON) tools/crosswalk-coverage/crosswalk_coverage.py

coverage-check:
	$(QA_PYTHON) tools/scenario-coverage/scenario_coverage.py

scenario-uniqueness-check:
	$(QA_PYTHON) tools/scenario-uniqueness/scenario_uniqueness_qa.py

scenario-language-polish-check:
	$(QA_PYTHON) tools/scenario-language-polish/scenario_language_polish_qa.py

release-surface-polish-check:
	$(QA_PYTHON) tools/release-surface-polish/release_surface_polish_qa.py

coverage-refresh:
	$(QA_PYTHON) tools/scenario-coverage/scenario_coverage.py --write

workshop-demo:
	$(QA_PYTHON) tools/workshop-pack/workshop_pack.py --out /tmp/acceptance-plane-workshop-pack

workshop-check:
	$(QA_PYTHON) tools/workshop-pack/workshop_pack.py --out /tmp/acceptance-plane-workshop-pack-check

facilitator-check:
	$(QA_PYTHON) tools/facilitator-packet/facilitator_packet_check.py

external-pointer-check:
	$(QA_PYTHON) tools/external-pointer-check/external_pointer_check.py

figure-check:
	$(QA_PYTHON) scripts/verify_figure_assets.py

unit-test:
	$(QA_PYTHON) -m unittest discover -s tools/scenario-card-lint/tests -p "test_*.py"

sample-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py scenarios_batch_1/AP-SCEN-001.json

full-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_*/*.json > /tmp/scenario-card-lint.txt

boundary-check:
	$(QA_PYTHON) scripts/public_boundary_qa.py

manifest:
	$(QA_PYTHON) scripts/verify_manifest.py

file-tree:
	@find . -path './.git' -prune -o -path './dist' -prune -o -type f -print | sed 's#^./##' | sort > provenance/FILE_TREE.txt

manifest-refresh: clean coverage-refresh readiness-check file-tree
	$(QA_PYTHON) scripts/write_manifest.py

qa: unit-test full-check readiness-check report-check browser-demo-check crosswalk-check crosswalk-coverage-check coverage-check scenario-uniqueness-check scenario-language-polish-check release-surface-polish-check workshop-check facilitator-check external-pointer-check figure-check boundary-check manifest

qa-clean:
	$(MAKE) clean
	$(MAKE) qa
	$(MAKE) clean

release-zip: qa-clean
	$(QA_PYTHON) scripts/build_release_zip.py

verify-release: release-zip
	$(QA_PYTHON) scripts/verify_release_artifact.py $(RELEASE_ZIP) --sha256-file $(RELEASE_SHA)

reproducible-zip-check: release-zip
	$(QA_PYTHON) scripts/verify_reproducible_zip.py

qa-full:
	$(MAKE) release-zip
	$(QA_PYTHON) scripts/verify_release_artifact.py $(RELEASE_ZIP) --sha256-file $(RELEASE_SHA)
	$(QA_PYTHON) scripts/verify_reproducible_zip.py
	$(QA_PYTHON) scripts/verify_release_artifact.py $(RELEASE_ZIP) --sha256-file $(RELEASE_SHA)
	@echo "qa-full: PASS"

preflight: doctor demo readiness-demo report-demo qa-clean
	@echo "Preflight passed. Review RELEASE_CHECKLIST.md and GITHUB_UPLOAD_GUIDE.md before publishing."

release-check: qa-full
	@echo "Release gate passed for v$(VERSION)."

package: release-zip

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist
