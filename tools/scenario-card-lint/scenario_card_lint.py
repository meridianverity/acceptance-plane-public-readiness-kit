#!/usr/bin/env python3
"""
Educational Acceptance Plane scenario-card linter.

This tool is intentionally non-production. It checks whether public scenario
cards contain enough high-level fields for tabletop discussion. It does not
perform identity checks, policy evaluation, cryptographic verification,
revocation checking, freshness validation, permit issuance, conformance testing,
certification, compliance scoring, or enforcement.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = [
    "id", "title", "domain", "risk_tier", "action_type", "protected_system",
    "scenario", "acceptance_boundary", "public_evidence_categories",
    "expected_decision", "why", "human_impact", "learning_goal", "rights_boundary"
]

STRING_FIELDS = [field for field in REQUIRED_FIELDS if field != "public_evidence_categories"]
VALID_DECISIONS = {"ACCEPT", "HOLD", "REFUSE"}
VALID_RISK_TIERS = {"high-consequence", "context-dependent"}
MIN_EVIDENCE_CATEGORIES = 5

FORBIDDEN_CLAIM_WORDS = [
    "certified", "certification granted", "production verifier", "patent claim chart",
    "PermitReceipt schema", "non-bypassable implementation", "cryptographic protocol",
    "conformance suite", "certificate registry", "reference implementation"
]


def load_card(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: {path} is not valid JSON: {exc}")
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: {path} must contain a JSON object")
    return data


def check_card(card: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in card or card[field] in (None, "", []):
            issues.append(f"missing_required_field:{field}")

    for field in STRING_FIELDS:
        if field in card and card[field] not in (None, "") and not isinstance(card[field], str):
            issues.append(f"field_must_be_string:{field}")

    decision = str(card.get("expected_decision", "")).upper()
    if decision and decision not in VALID_DECISIONS:
        issues.append(f"invalid_expected_decision:{decision}")

    risk_tier = str(card.get("risk_tier", ""))
    if risk_tier and risk_tier not in VALID_RISK_TIERS:
        issues.append(f"unexpected_risk_tier:{risk_tier}")

    evidence = card.get("public_evidence_categories", [])
    if not isinstance(evidence, list):
        issues.append("public_evidence_categories_must_be_list")
    else:
        if len(evidence) < MIN_EVIDENCE_CATEGORIES:
            issues.append(f"too_few_public_evidence_categories:{len(evidence)}")
        if any(not isinstance(item, str) or not item.strip() for item in evidence):
            issues.append("public_evidence_categories_must_be_nonempty_strings")

    rights_boundary = str(card.get("rights_boundary", ""))
    if rights_boundary and "public educational scenario" not in rights_boundary.lower():
        issues.append("rights_boundary_should_say_public_educational_scenario")

    joined = json.dumps(card, ensure_ascii=False).lower()
    for phrase in FORBIDDEN_CLAIM_WORDS:
        if phrase.lower() in joined:
            issues.append(f"rights_boundary_warning:{phrase}")

    return issues


def report_for(path: Path) -> dict[str, Any]:
    card = load_card(path)
    issues = check_card(card)
    return {
        "path": path.as_posix(),
        "id": card.get("id", path.name),
        "title": card.get("title", "(untitled)"),
        "decision_label": card.get("expected_decision", "(missing)"),
        "status": "REVIEW_NEEDED" if issues else "DISCUSSION_READY",
        "issues": issues,
        "boundary": "educational scenario-card completeness lint only; not certification, compliance approval, production readiness, or an allow/deny decision",
    }


def print_text(reports: list[dict[str, Any]], include_summary: bool) -> None:
    for report in reports:
        print(f"\nScenario: {report['id']} — {report['title']}")
        print("Report type: educational scenario-card completeness lint only")
        print("Decision label:", report["decision_label"])
        print("Status:", report["status"])
        if report["issues"]:
            for issue in report["issues"]:
                print("-", issue)
        else:
            print("- The card has enough public structure for tabletop discussion.")
            print("- This is not certification, compliance approval, production readiness, or an allow/deny decision.")

    if include_summary:
        status_counts = Counter(report["status"] for report in reports)
        decision_counts = Counter(str(report["decision_label"]) for report in reports)
        print("\nSummary")
        print("Cards checked:", len(reports))
        print("Statuses:", dict(status_counts))
        print("Decision labels:", dict(decision_counts))
        print("Boundary: educational completeness lint only; no certification, compliance approval, production readiness, or allow/deny decision.")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Educational scenario-card linter for public Acceptance Plane scenario cards.")
    parser.add_argument("cards", nargs="+", help="Scenario-card JSON files to lint")
    parser.add_argument("--summary", action="store_true", help="Print aggregate counts after card reports")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format")
    parser.add_argument("--json-report", action="store_true", help="Alias for --format json")
    args = parser.parse_args(argv[1:])

    reports = [report_for(Path(card)) for card in args.cards]

    if args.json_report:
        args.format = "json"

    if args.format == "json":
        payload = {
            "tool": "scenario-card-lint",
            "tool_version": "0.3.4",
            "report_type": "educational scenario-card completeness lint only",
            "cards_checked": len(reports),
            "statuses": dict(Counter(report["status"] for report in reports)),
            "decision_labels": dict(Counter(str(report["decision_label"]) for report in reports)),
            "reports": reports,
            "boundary": "not certification, compliance approval, production readiness, or an allow/deny decision",
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print_text(reports, args.summary)

    return 1 if any(report["issues"] for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
