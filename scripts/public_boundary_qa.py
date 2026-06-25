#!/usr/bin/env python3
"""Public boundary QA for the Acceptance Plane Public Readiness Kit.

This QA script checks public-release discipline. It is not a product test,
conformance suite, certification workflow, security review, legal review, or
production readiness test.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_BATCHES = [ROOT / "scenarios_batch_1", ROOT / "scenarios_batch_2"]
VALID_DECISIONS = {"ACCEPT", "HOLD", "REFUSE"}
REQUIRED_NOTICE = "Not a product implementation. Not a standard. No patent license. No certification right."
CANONICAL_DOI = "10.5281/zenodo.20645907"
EXPECTED_TOOL_PATH = "tools/scenario-card-lint/scenario_card_lint.py"
OLD_TOOL_TOKENS = ["ap-readiness-check", "ap_readiness_check.py", "ap_readiness_check"]
PUBLIC_HYPE_TOKENS = ["apex", "99.9", "99.99", "$100m", "kingdom port", "big tech can't", "big tech cannot"]
TEXT_SUFFIXES = {
    "", ".cff", ".csv", ".gitignore", ".gitattributes", ".editorconfig", ".json",
    ".md", ".py", ".sh", ".txt", ".yaml", ".yml"
}
TEXT_FILENAMES = {"LICENSE", "NOTICE", "VERSION", "Makefile"}
EXCLUDE_FROM_TEXT_SCAN = {"provenance/MANIFEST.sha256"}
EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".venv", "venv", "build", "dist", "htmlcov"
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}
EXCLUDED_FILENAMES = {".DS_Store", ".coverage"}

errors: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_excluded(path: Path) -> bool:
    relative = rel(path)
    if relative in EXCLUDE_FROM_TEXT_SCAN:
        return True
    if path.name in EXCLUDED_FILENAMES:
        return True
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    return any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)


def is_text_file(path: Path) -> bool:
    if is_excluded(path):
        return False
    return path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_scenarios() -> list[tuple[Path, dict]]:
    cards: list[tuple[Path, dict]] = []
    expected_ids = [f"AP-SCEN-{i:03d}" for i in range(1, 101)]

    old_cards_dir = ROOT / "scenarios" / "cards"
    if old_cards_dir.exists():
        errors.append("stale scenarios/cards directory remains; use scenarios_batch_1/ and scenarios_batch_2/")

    for batch_index, batch_dir in enumerate(SCENARIO_BATCHES, start=1):
        if not batch_dir.exists():
            errors.append(f"missing {batch_dir.relative_to(ROOT).as_posix()}")
            continue
        batch_cards = sorted(batch_dir.glob("AP-SCEN-*.json"))
        if len(batch_cards) != 50:
            errors.append(f"{batch_dir.relative_to(ROOT).as_posix()}: expected 50 scenario cards, found {len(batch_cards)}")
        for path in batch_cards:
            try:
                card = json.loads(read_text(path))
            except Exception as exc:  # noqa: BLE001 - public release QA should report all file errors.
                errors.append(f"{rel(path)}: invalid json: {exc}")
                continue
            cards.append((path, card))
            if card.get("expected_decision") not in VALID_DECISIONS:
                errors.append(f"{rel(path)}: invalid decision {card.get('expected_decision')}")
            if len(card.get("public_evidence_categories", [])) < 5:
                errors.append(f"{rel(path)}: too few evidence categories")
            if "rights_boundary" not in card:
                errors.append(f"{rel(path)}: missing rights_boundary")

    if len(cards) != 100:
        errors.append(f"expected 100 scenario cards, found {len(cards)}")

    ids = [card.get("id") for _, card in cards]
    if len(ids) != len(set(ids)):
        errors.append("duplicate scenario IDs")
    if sorted(ids) != expected_ids:
        errors.append("scenario IDs do not match AP-SCEN-001..AP-SCEN-100")

    card_paths_by_id = {card.get("id"): rel(path) for path, card in cards}
    index_path = ROOT / "scenarios" / "index.csv"
    if index_path.exists():
        with index_path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        index_ids = sorted(row.get("id") for row in rows)
        if index_ids != expected_ids:
            errors.append("scenarios/index.csv IDs do not match scenario cards")
        for row in rows:
            row_id = row.get("id")
            row_path = row.get("path")
            if row_id in card_paths_by_id and row_path != card_paths_by_id[row_id]:
                errors.append(f"scenarios/index.csv path mismatch for {row_id}: {row_path} != {card_paths_by_id[row_id]}")
            if row_path and not (ROOT / row_path).exists():
                errors.append(f"scenarios/index.csv points to missing file: {row_path}")
    else:
        errors.append("missing scenarios/index.csv")

    if not (ROOT / "scenarios" / "scenario_card.schema.json").exists():
        errors.append("missing public scenario-card JSON shape")

    return cards


def require_file(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        errors.append(f"{relative}: missing")
        return ""
    return read_text(path)


def check_core_boundary_docs() -> None:
    for relative in [
        "README.md", "README_ko.md", "NOTICE", "PATENT_AND_TRADEMARK_NOTICE.md", "ATTRIBUTION.md",
        "LICENSE", "docs/19-license-and-rights-boundary.md"
    ]:
        text = require_file(relative)
        if not text:
            continue
        if REQUIRED_NOTICE not in text and relative not in {"PATENT_AND_TRADEMARK_NOTICE.md", "ATTRIBUTION.md", "LICENSE", "docs/19-license-and-rights-boundary.md"}:
            errors.append(f"{relative}: missing required boundary notice")
        if "No patent license" not in text and "no patent" not in text.lower() and relative in {"NOTICE", "PATENT_AND_TRADEMARK_NOTICE.md", "ATTRIBUTION.md", "LICENSE", "docs/19-license-and-rights-boundary.md"}:
            errors.append(f"{relative}: missing no-patent-license language")

    for relative in [
        "LICENSES/MIT.txt", "LICENSES/CC-BY-4.0.txt", "DEPENDENCIES.md", "ROADMAP.md",
        "MAINTAINERS.md", "RELEASE_CHECKLIST.md", "QUICKSTART.md", "GITHUB_UPLOAD_GUIDE.md",
        "AAIF_FEEDBACK_INQUIRY.md", "docs/21-public-threat-model.md",
        "docs/22-one-hour-enterprise-evaluator-script.md", "docs/23-archive-and-license-boundary.md",
        "docs/24-release-integrity.md", "provenance/SBOM.spdx.json", "provenance/RELEASE_AUDIT.md",
        "launch/github_release_body_v0.1.4.md", "launch/upload_strategy_v0.1.4.md",
        "launch/git_publish_commands_v0.1.4.sh", ".editorconfig", ".gitattributes"
    ]:
        require_file(relative)

    if (ROOT / "playbooks" / "partner_licensing_readiness.md").exists():
        errors.append("stale sales-forward playbook remains: playbooks/partner_licensing_readiness.md")
    if not (ROOT / "playbooks" / "production_boundary_readiness.md").exists():
        errors.append("missing playbooks/production_boundary_readiness.md")

    citation = require_file("CITATION.cff")
    if citation:
        before_preferred = citation.split("preferred-citation:", 1)[0]
        if "\nidentifiers:" in before_preferred:
            errors.append("CITATION.cff appears to assign an identifier to the kit itself; use preferred-citation for canonical thesis DOI")
        if "preferred-citation:" not in citation or CANONICAL_DOI not in citation:
            errors.append("CITATION.cff missing preferred-citation canonical DOI")
        if "acceptance-plane-public-readiness-kit" not in citation:
            errors.append("CITATION.cff repository-code should point to the readiness-kit repo")
        if 'version: "0.1.4"' not in citation:
            errors.append("CITATION.cff version should be 0.1.4")

    zenodo_text = require_file(".zenodo.json")
    if zenodo_text:
        zenodo = json.loads(zenodo_text)
        related = zenodo.get("related_identifiers", [])
        if not any(r.get("scheme") == "doi" and r.get("identifier") == CANONICAL_DOI for r in related):
            errors.append(".zenodo.json related DOI should use raw DOI identifier with scheme doi")
        if zenodo.get("version") != "0.1.4":
            errors.append(".zenodo.json version should be 0.1.4")
        if "Software portions are under MIT" not in zenodo.get("notes", ""):
            errors.append(".zenodo.json notes should disclose split-license boundary")

    workflow = require_file(".github/workflows/qa.yml")
    if workflow:
        if "make qa" not in workflow and "make preflight" not in workflow:
            errors.append("GitHub Actions QA should call make qa or make preflight")
        if "PYTHONDONTWRITEBYTECODE" not in workflow:
            errors.append("GitHub Actions QA should avoid generated Python bytecode")

    makefile = require_file("Makefile")
    if makefile:
        for target in ["doctor:", "demo:", "demo-json:", "unit-test:", "qa-clean:", "preflight:", "package:"]:
            if target not in makefile:
                errors.append(f"Makefile missing {target}")
        if "PYTHONDONTWRITEBYTECODE" not in makefile:
            errors.append("Makefile missing PYTHONDONTWRITEBYTECODE")
        if "qa: unit-test full-check boundary-check manifest" not in makefile:
            errors.append("Makefile qa target should include standard-library unit tests")

    readme = require_file("README.md")
    if readme:
        if REQUIRED_NOTICE not in readme:
            errors.append("README missing rights-boundary tagline")
        if "5-minute educational scenario-card linter" not in readme:
            errors.append("README missing 5-minute developer utility positioning")
        if "docs/21-public-threat-model.md" not in readme:
            errors.append("README missing enterprise evaluator path to public threat model")
        try:
            citation_block = readme.split("Canonical public architecture thesis:", 1)[1].split("## Release principle", 1)[0]
            if "™" in citation_block:
                errors.append("README formal citation block should use clean academic title without ™")
        except IndexError:
            errors.append("README citation block not found")

    if (ROOT / "tools" / "ap-readiness-check").exists():
        errors.append("Old tool directory remains: tools/ap-readiness-check")
    if not (ROOT / EXPECTED_TOOL_PATH).exists():
        errors.append(f"Missing renamed linter: {EXPECTED_TOOL_PATH}")


def check_contribution_security_release_docs() -> None:
    contributing = require_file("CONTRIBUTING.md")
    if contributing:
        if "By submitting" not in contributing or "MIT License" not in contributing or "CC BY 4.0" not in contributing:
            errors.append("CONTRIBUTING.md missing inbound contribution licensing statement")
        if "must not include" not in contributing or "implementation-level" not in contributing:
            errors.append("CONTRIBUTING.md missing implementation-disclosure guardrail")

    security = require_file("SECURITY.md")
    if security:
        if "GitHub Security Advisory" not in security:
            errors.append("SECURITY.md missing GitHub Security Advisory reporting path")
        if "accidental implementation disclosure" not in security.lower():
            errors.append("SECURITY.md missing accidental implementation disclosure reporting scope")

    guide = require_file("GITHUB_UPLOAD_GUIDE.md")
    command = require_file("launch/git_publish_commands_v0.1.4.sh")
    release = require_file("launch/github_release_body_v0.1.4.md")
    for relative, text in [("GITHUB_UPLOAD_GUIDE.md", guide), ("launch/git_publish_commands_v0.1.4.sh", command)]:
        if text:
            if "--verify-tag" not in text:
                errors.append(f"{relative}: release command should use --verify-tag")
            if "v0.1.4" not in text:
                errors.append(f"{relative}: should reference v0.1.4")
    if release and REQUIRED_NOTICE not in release:
        errors.append("launch/github_release_body_v0.1.4.md missing exact boundary notice")


def full_repo_boundary_scan() -> tuple[int, int]:
    """Scan all text files for unsafe positive claims, stale references, and public hype terms."""
    text_files = [p for p in ROOT.rglob("*") if p.is_file() and is_text_file(p)]
    unsafe_patterns: list[tuple[str, re.Pattern[str]]] = [
        ("positive product implementation claim", re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(product implementation|reference implementation|production sdk|sdk|implementation package)\b", re.I)),
        ("positive formal standard claim", re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|defines|creates|establishes)\s+(a\s+)?(formal\s+)?standard\b", re.I)),
        ("positive patent/trademark/license grant", re.compile(r"\b(grants?|granting|provides|providing)\s+(a\s+)?(patent|trademark|service mark|implementation|certification)\s+(license|right)\b", re.I)),
        ("positive certification claim", re.compile(r"\b(certifies|certified by this kit|certification granted|officially certified|compliance approved|procurement approved)\b", re.I)),
        ("positive conformance program claim", re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(conformance suite|conformance test suite|certificate registry|certification program)\b", re.I)),
        ("positive production mechanism claim", re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(production verifier|permitreceipt engine|non-bypassable interceptor|cryptographic binding method|exact evidence schema|hardware adapter|patent claim chart)\b", re.I)),
    ]

    scanned = 0
    hits = 0
    allowed_literal_files = {"scripts/public_boundary_qa.py", "tools/scenario-card-lint/scenario_card_lint.py"}
    for path in text_files:
        relative = rel(path)
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        scanned += 1
        if relative not in allowed_literal_files:
            for token in OLD_TOOL_TOKENS:
                if token in text:
                    errors.append(f"{relative}: stale tool token remains: {token}")
                    hits += 1
            for token in PUBLIC_HYPE_TOKENS:
                if token in text.lower():
                    errors.append(f"{relative}: public hype/internal token remains: {token}")
                    hits += 1
            if "partner_licensing_readiness" in text or "Partner Licensing Readiness" in text:
                errors.append(f"{relative}: stale partner licensing playbook wording remains")
                hits += 1
            if "v0.1.3" in text and relative not in {"CHANGELOG.md"}:
                errors.append(f"{relative}: stale v0.1.3 reference remains")
                hits += 1
        for label, pattern in unsafe_patterns:
            for match in pattern.finditer(text):
                if relative in allowed_literal_files:
                    continue
                context = text[max(0, match.start() - 100): match.end() + 100].lower()
                if any(guard in context for guard in ["not ", "does not ", "do not ", "no ", "without ", "must not ", "avoid ", "is not ", "imply that ", "claim that ", "prohibited", "restricted", "doesn’t ", "don't "]):
                    continue
                errors.append(f"{relative}: {label}: {match.group(0)!r}")
                hits += 1
    return scanned, hits


def main() -> int:
    cards = check_scenarios()
    check_core_boundary_docs()
    check_contribution_security_release_docs()
    scanned, hits = full_repo_boundary_scan()

    if errors:
        print("QA FAILED")
        for error in errors:
            print("-", error)
        return 1

    print("QA PASSED")
    print("Scenario cards:", len(cards))
    print("Decision balance:", dict(Counter(card["expected_decision"] for _, card in cards)))
    print("Domain balance:", dict(Counter(card["domain"] for _, card in cards)))
    print(f"Full-repo text boundary scan: {scanned} files scanned, {hits} unsafe hits")
    print("Boundary notice: present")
    print("Citation metadata: preferred-citation boundary passed")
    print("Zenodo related DOI: raw DOI boundary passed")
    print("Developer quickstart: make demo present")
    print("License split: MIT software / CC BY 4.0 materials")
    print("CI manifest check: present")
    print("Tool naming: scenario-card-lint boundary passed")
    print("AAIF posture: feedback inquiry present; not hosted-project claim")
    print("Release integrity docs: present")
    print("Public hype/internal wording scan: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
