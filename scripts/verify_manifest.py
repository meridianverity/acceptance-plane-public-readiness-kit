#!/usr/bin/env python3
"""Verify provenance/MANIFEST.sha256 for repository release files.

The manifest is strict for repository release files, while intentionally ignoring
local VCS state and generated cache/build artifacts such as .git/, __pycache__/,
.pyc files, build/, and dist/.
"""
from __future__ import annotations

from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "provenance" / "MANIFEST.sha256"
EXCLUDED_RELATIVE_PATHS = {"provenance/MANIFEST.sha256"}
EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".venv", "venv", "build", "dist", "htmlcov"
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}
EXCLUDED_FILENAMES = {".DS_Store", ".coverage"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_excluded(path: Path) -> bool:
    relative = rel(path)
    if relative in EXCLUDED_RELATIVE_PATHS:
        return True
    if path.name in EXCLUDED_FILENAMES:
        return True
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    return any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)


def discover_files() -> set[str]:
    found: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if is_excluded(path):
            continue
        found.add(rel(path))
    return found

import sys


def read_manifest() -> dict[str, str]:
    if not MANIFEST.exists():
        print("Missing provenance/MANIFEST.sha256", file=sys.stderr)
        sys.exit(2)

    entries: dict[str, str] = {}
    errors: list[str] = []
    for lineno, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError:
            errors.append(f"Malformed line {lineno}: {line}")
            continue
        if relative in entries:
            errors.append(f"Duplicate manifest entry: {relative}")
            continue
        candidate = ROOT / relative
        if relative in EXCLUDED_RELATIVE_PATHS or (candidate.exists() and is_excluded(candidate)):
            errors.append(f"Manifest must not include excluded file: {relative}")
            continue
        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            errors.append(f"Invalid SHA-256 digest for {relative}")
            continue
        entries[relative] = expected

    if errors:
        print("MANIFEST VERIFY FAILED")
        for error in errors:
            print("-", error)
        sys.exit(1)
    return entries


def main() -> int:
    entries = read_manifest()
    actual_files = discover_files()
    manifest_files = set(entries)

    errors: list[str] = []
    missing_from_manifest = sorted(actual_files - manifest_files)
    unexpected_entries = sorted(manifest_files - actual_files)

    for relative in missing_from_manifest:
        errors.append(f"Unmanifested file: {relative}")
    for relative in unexpected_entries:
        errors.append(f"Manifest entry for missing file: {relative}")

    for relative, expected in sorted(entries.items()):
        path = ROOT / relative
        if not path.exists():
            continue
        actual = sha256(path)
        if actual != expected:
            errors.append(f"Hash mismatch: {relative}")

    if errors:
        print("MANIFEST VERIFY FAILED")
        for error in errors:
            print("-", error)
        return 1

    print("MANIFEST VERIFY PASSED")
    print(f"Strict manifest entries: {len(entries)}")
    print("Excluded local/generated paths: .git/, __pycache__/, *.pyc, build/, dist/, cache directories")
    print("Excluded self-reference: provenance/MANIFEST.sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
