#!/usr/bin/env python3
"""Release-surface editorial QA for the public readiness kit.

This gate checks the files a reviewer is most likely to read first. It is a
narrow editorial release-quality check, not a semantic evaluator, certification
program, conformance test, compliance approval, or production allow/deny system.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
VERSION = "v0.3.4"
PREVIOUS_VERSION = "v0.3.3"
CANONICAL_ZIP = f"acceptance-plane-public-readiness-kit-{VERSION}.zip"
CANONICAL_SHA = f"{CANONICAL_ZIP}.sha256.txt"
CANONICAL_TITLE = "Acceptance Plane Public Readiness Kit v0.3.4 — Release-Surface Locked Public Readiness Corpus for Action Acceptance Before Impact"

PUBLIC_SURFACE_FILES = [
    "README.md",
    "README_ko.md",
    "QUICKSTART.md",
    "GITHUB_UPLOAD_GUIDE.md",
    "RELEASE_CHECKLIST.md",
    "CHANGELOG.md",
    "release_title.txt",
    "release_description.txt",
    "metadata/github_release_body_v0.3.4.md",
    "metadata/release_pointer_lock_v0.3.4.md",
    "metadata/public_release_state_note_v0.3.4.md",
    "metadata/repo_about.md",
    "launch/github_release_body_v0.3.4.md",
    "launch/upload_strategy_v0.3.4.md",
    "launch/git_publish_commands_v0.3.4.sh",
    "launch/linkedin_announcement.md",
    "launch/press_note.md",
    "docs/32-corpus-language-stewardship.md",
    "docs/33-learning-goal-polish.md",
    "docs/34-release-surface-polish.md",
    "provenance/QA_REPORT.md",
    "provenance/RELEASE_AUDIT.md",
    "provenance/SHIP_DECISION.md",
    "provenance/V0_3_4_RELEASE_SURFACE_POLISH_AUDIT.md",
]

ACTIVE_RELEASE_FILES = [
    "README.md",
    "README_ko.md",
    "QUICKSTART.md",
    "GITHUB_UPLOAD_GUIDE.md",
    "RELEASE_CHECKLIST.md",
    "release_title.txt",
    "release_description.txt",
    "metadata/github_release_body_v0.3.4.md",
    "metadata/release_pointer_lock_v0.3.4.md",
    "metadata/public_release_state_note_v0.3.4.md",
    "metadata/repo_about.md",
    "launch/github_release_body_v0.3.4.md",
    "launch/upload_strategy_v0.3.4.md",
    "launch/git_publish_commands_v0.3.4.sh",
    "launch/linkedin_announcement.md",
    "launch/press_note.md",
]

FORBIDDEN_VISIBLE_PHRASES = [
    "the final the final",
    "phrase family phrases",
    "phrase phrasing",
    "editorially locked public readiness corpus",
    "repeated repeated",
    "visible visible",
    "release release artifact",
    "public public",
]

FORBIDDEN_UNDERSCORE_ASSET_PATTERNS = [
    "acceptance-plane-public-readiness-kit-v0_3_4",
    "acceptance-plane-public-readiness-kit-v0_3_3",
]


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        raise FileNotFoundError(relative)
    return path.read_text(encoding="utf-8")


def check_changelog(errors: list[str]) -> None:
    text = read("CHANGELOG.md")
    headings = re.findall(r"^##\s+(v\d+\.\d+\.\d+)\s+—\s+\d{4}-\d{2}-\d{2}\s*$", text, flags=re.M)
    counts = Counter(headings)
    for version, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"CHANGELOG.md: duplicate heading for {version}: {count}")
    if not headings:
        errors.append("CHANGELOG.md: no version headings found")
    elif headings[0] != VERSION:
        errors.append(f"CHANGELOG.md: top heading is {headings[0]}, expected {VERSION}")
    if text.count(f"## {VERSION} — 2026-07-08") != 1:
        errors.append(f"CHANGELOG.md: expected exactly one {VERSION} heading")


def check_visible_phrases(errors: list[str]) -> None:
    for relative in PUBLIC_SURFACE_FILES:
        text = read(relative)
        lower = text.lower()
        for phrase in FORBIDDEN_VISIBLE_PHRASES:
            if phrase in lower:
                errors.append(f"{relative}: visible release-surface wording scar {phrase!r}")
        for pattern in FORBIDDEN_UNDERSCORE_ASSET_PATTERNS:
            if pattern in text:
                errors.append(f"{relative}: underscore release asset name remains: {pattern}")


def check_active_release_alignment(errors: list[str]) -> None:
    for relative in ACTIVE_RELEASE_FILES:
        text = read(relative)
        if VERSION not in text and relative not in {"metadata/repo_about.md", "release_description.txt"}:
            errors.append(f"{relative}: missing active version {VERSION}")
        if PREVIOUS_VERSION in text:
            errors.append(f"{relative}: stale active release pointer {PREVIOUS_VERSION}")
    title = read("release_title.txt").strip()
    if VERSION not in title:
        errors.append("release_title.txt: active version missing")
    if title != CANONICAL_TITLE:
        errors.append("release_title.txt: canonical title mismatch")
    for relative in ["GITHUB_UPLOAD_GUIDE.md", "RELEASE_CHECKLIST.md", "metadata/release_pointer_lock_v0.3.4.md", "launch/upload_strategy_v0.3.4.md", "launch/git_publish_commands_v0.3.4.sh"]:
        if CANONICAL_TITLE not in read(relative):
            errors.append(f"{relative}: canonical release title mismatch")
    body = read("metadata/github_release_body_v0.3.4.md")
    if CANONICAL_ZIP not in body or CANONICAL_SHA not in body:
        errors.append("metadata/github_release_body_v0.3.4.md: missing canonical ZIP/SHA names")


def check_no_stale_release_files(errors: list[str]) -> None:
    stale = [
        "metadata/github_release_body_v0.3.3.md",
        "metadata/release_pointer_lock_v0.3.3.md",
        "metadata/public_release_state_note_v0.3.3.md",
        "launch/github_release_body_v0.3.3.md",
        "launch/upload_strategy_v0.3.3.md",
        "launch/git_publish_commands_v0.3.3.sh",
    ]
    for relative in stale:
        if (ROOT / relative).exists():
            errors.append(f"stale release-facing file still bundled: {relative}")


def main() -> int:
    errors: list[str] = []
    try:
        check_changelog(errors)
        check_visible_phrases(errors)
        check_active_release_alignment(errors)
        check_no_stale_release_files(errors)
    except FileNotFoundError as exc:
        errors.append(f"missing release-surface file: {exc}")
    if errors:
        print("release-surface polish QA: FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("release-surface polish QA: PASS")
    print(f"Version: {VERSION}")
    print(f"Public surface files checked: {len(PUBLIC_SURFACE_FILES)}")
    print("Changelog duplicate headings: none")
    print("Visible release-surface wording scars: none")
    print("Active release pointers: canonical dotted v0.3.4 names")
    print("Boundary: editorial release-surface QA only; not certification, compliance approval, production readiness, conformance, or an allow/deny decision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
