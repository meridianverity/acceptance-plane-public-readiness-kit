#!/usr/bin/env python3
"""Editorial-polish QA for the public readiness scenario corpus.

This gate is intentionally narrow: it catches visible generator/editorial scars
that can make an otherwise valid educational corpus look mass-produced.
It is not a semantic evaluator, certification gate, conformance test, or
production allow/deny system.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_CARDS = 300
FORBIDDEN_PHRASES = [
    "before " + "before",
    "before the team reaches " + "before",
    "the team reaches " + "before",
    "reaches " + "before",
    "During a " + "incident tabletop",
    "During a " + "operator handoff",
    " a " + "incident ",
    " a " + "operator ",
]
CHECK_FIELDS = [
    "title",
    "scenario",
    "why",
    "human_impact",
    "learning_goal",
    "acceptance_boundary",
]


def load_cards() -> list[tuple[Path, dict]]:
    cards: list[tuple[Path, dict]] = []
    for batch in sorted(ROOT.glob("scenarios_batch_*")):
        if not batch.is_dir():
            continue
        for path in sorted(batch.glob("AP-SCEN-*.json")):
            cards.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return cards


def main() -> int:
    cards = load_cards()
    errors: list[str] = []
    if len(cards) != EXPECTED_CARDS:
        errors.append(f"expected {EXPECTED_CARDS} cards, found {len(cards)}")
    for path, card in cards:
        for field in CHECK_FIELDS:
            value = card.get(field, "")
            if not isinstance(value, str):
                errors.append(f"{path.relative_to(ROOT).as_posix()}: {field} is not text")
                continue
            for phrase in FORBIDDEN_PHRASES:
                if phrase in value:
                    errors.append(f"{path.relative_to(ROOT).as_posix()}: {field} contains editorial scar {phrase!r}")
    if errors:
        print("scenario language-polish QA: FAIL")
        for error in errors[:60]:
            print("-", error)
        if len(errors) > 60:
            print(f"- ... {len(errors) - 60} additional findings")
        return 1
    print("scenario language-polish QA: PASS")
    print(f"Cards: {len(cards)}")
    print("Editorial scars rejected: duplicated-before wording, repeated reaches-before phrasing, and incorrect article usage before incident/operator")
    print("Boundary: educational corpus language QA only; not certification, compliance approval, production readiness, conformance, or an allow/deny decision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
