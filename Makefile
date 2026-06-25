QA_PYTHON ?= python3
VERSION := 0.1.4
export PYTHONDONTWRITEBYTECODE=1

.PHONY: doctor demo demo-json unit-test qa qa-clean clean sample-check full-check boundary-check manifest manifest-refresh file-tree preflight release-check package

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

unit-test:
	$(QA_PYTHON) -m unittest discover -s tools/scenario-card-lint/tests -p "test_*.py"

qa: unit-test full-check boundary-check manifest

qa-clean:
	$(MAKE) clean
	$(MAKE) qa
	$(MAKE) clean

sample-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py scenarios_batch_1/AP-SCEN-001.json

full-check:
	$(QA_PYTHON) tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/*.json scenarios_batch_2/*.json > /tmp/scenario-card-lint.txt

boundary-check:
	$(QA_PYTHON) scripts/public_boundary_qa.py

manifest:
	$(QA_PYTHON) scripts/verify_manifest.py

file-tree:
	@find . -path './.git' -prune -o -type f -print | sed 's#^./##' | sort > provenance/FILE_TREE.txt

manifest-refresh: clean file-tree
	$(QA_PYTHON) scripts/write_manifest.py

preflight: doctor demo qa-clean
	@echo "Preflight passed. Review RELEASE_CHECKLIST.md and GITHUB_UPLOAD_GUIDE.md before pushing."

release-check: preflight
	@echo "Release gate passed for v$(VERSION)."

package: qa-clean
	@cd .. && rm -f acceptance-plane-public-readiness-kit-v$(VERSION).zip acceptance-plane-public-readiness-kit-v$(VERSION).zip.sha256
	@cd .. && zip -qr acceptance-plane-public-readiness-kit-v$(VERSION).zip acceptance-plane-public-readiness-kit -x '*/.git/*' '*/__pycache__/*' '*/.pytest_cache/*' '*/.mypy_cache/*' '*/.ruff_cache/*' '*/.DS_Store'
	@cd .. && python3 -c "from pathlib import Path; import hashlib, zipfile; p=Path('acceptance-plane-public-readiness-kit-v$(VERSION).zip'); h=hashlib.sha256(p.read_bytes()).hexdigest(); Path(str(p)+'.sha256').write_text(h+'  '+p.name+'\n', encoding='utf-8'); z=zipfile.ZipFile(p); bad=z.testzip(); z.close(); assert bad is None, bad; print('ZIP OK:', p); print('SHA256:', h)"

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist
