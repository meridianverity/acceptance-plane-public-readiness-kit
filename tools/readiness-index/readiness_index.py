#!/usr/bin/env python3
"""Action Acceptance Readiness Index.

Educational readiness signal only. Not certification, compliance approval,
procurement approval, production readiness, or an allow/deny decision.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
ITEMS_PATH = ROOT / "readiness" / "index_items.json"
VALID = {"YES", "PARTIAL", "NO", "UNKNOWN"}
POINTS = {"YES": 2, "PARTIAL": 1, "NO": 0, "UNKNOWN": 0}
BOUNDARY = "educational readiness signal only; not certification, compliance approval, procurement approval, production readiness, or an allow/deny decision"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: missing file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def compute(assessment: dict[str, Any]) -> dict[str, Any]:
    item_doc = load_json(ITEMS_PATH)
    items = item_doc.get("items", [])
    if not isinstance(items, list) or len(items) < 40:
        raise SystemExit("ERROR: readiness/index_items.json must contain at least 40 items")
    by_id = {item["id"]: item for item in items}
    responses = assessment.get("responses", [])
    if not isinstance(responses, list):
        raise SystemExit("ERROR: assessment responses must be a list")

    response_by_id = {}
    issues = []
    for resp in responses:
        if not isinstance(resp, dict):
            issues.append("response_not_object")
            continue
        iid = resp.get("item_id")
        status = str(resp.get("status", "")).upper()
        if iid not in by_id:
            issues.append(f"unknown_item:{iid}")
            continue
        if status not in VALID:
            issues.append(f"invalid_status:{iid}:{status}")
            continue
        response_by_id[iid] = status

    missing = sorted(set(by_id) - set(response_by_id))
    for iid in missing:
        response_by_id[iid] = "UNKNOWN"

    earned = sum(POINTS[response_by_id[iid]] for iid in by_id)
    maximum = len(by_id) * 2
    maturity = round(earned / maximum * 100)
    if maturity >= 80:
        posture = "DISCUSSION_READY_FOR_CONFORMANCE_HANDOFF"
    elif maturity >= 60:
        posture = "HOLD_FOR_IMPLEMENTATION_REVIEW"
    else:
        posture = "FOUNDATIONAL_DISCUSSION_NEEDED"

    category_scores: dict[str, dict[str, int]] = defaultdict(lambda: {"earned": 0, "maximum": 0})
    gaps = []
    for iid, item in by_id.items():
        status = response_by_id[iid]
        cat = item.get("category", "uncategorized")
        category_scores[cat]["earned"] += POINTS[status]
        category_scores[cat]["maximum"] += 2
        if status in {"NO", "UNKNOWN", "PARTIAL"}:
            gaps.append({"item_id": iid, "status": status, "gap": item.get("gap_if_missing", item.get("prompt", "gap"))})

    top_gaps = gaps[:8]
    return {
        "assessment_id": assessment.get("assessment_id", "(missing)"),
        "readiness_posture": posture,
        "discussion_maturity": maturity,
        "earned_points": earned,
        "maximum_points": maximum,
        "items": len(by_id),
        "issues": issues,
        "missing_responses": missing,
        "category_scores": {k: {**v, "score": round(v["earned"] / v["maximum"] * 100) if v["maximum"] else 0} for k, v in sorted(category_scores.items())},
        "top_gaps": top_gaps,
        "boundary": BOUNDARY,
    }


def print_markdown(result: dict[str, Any]) -> None:
    print(f"Readiness posture: {result['readiness_posture']}")
    print(f"Discussion maturity: {result['discussion_maturity']} / 100")
    print(f"Items: {result['items']}")
    print("Top gaps:")
    for gap in result["top_gaps"]:
        print(f"  - {gap['gap']} ({gap['item_id']}, {gap['status']})")
    if not result["top_gaps"]:
        print("  - no gaps recorded in this educational sample")
    print(f"Boundary: {result['boundary']}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Educational Action Acceptance Readiness Index")
    parser.add_argument("assessment", help="assessment JSON file")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv[1:])
    result = compute(load_json(Path(args.assessment)))
    if result["issues"]:
        print(json.dumps(result, indent=2), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_markdown(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
