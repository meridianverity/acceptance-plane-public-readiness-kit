#!/usr/bin/env python3
"""Write provenance/MANIFEST.sha256 for repository release files.

Local VCS state and generated cache/build artifacts are intentionally excluded.
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


def main() -> int:
    entries: list[tuple[str, str]] = []
    for relative in sorted(discover_files()):
        entries.append((relative, sha256(ROOT / relative)))

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text("".join(f"{digest}  {relative}\n" for relative, digest in entries), encoding="utf-8")
    print(f"Wrote {MANIFEST.relative_to(ROOT).as_posix()} with {len(entries)} entries")
    print("Excluded local/generated paths: .git/, __pycache__/, *.pyc, build/, dist/, cache directories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
