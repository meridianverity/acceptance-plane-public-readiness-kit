#!/usr/bin/env python3
"""Build a release ZIP with a single repository root and SHA-256 sidecar."""
from __future__ import annotations
import hashlib, zipfile, os, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
DIST=ROOT/'dist'
NAME=f'acceptance-plane-public-readiness-kit-v{VERSION}.zip'
EXCLUDED_DIRS={'.git','__pycache__','.pytest_cache','.mypy_cache','.ruff_cache','.venv','venv','build','dist','htmlcov'}
EXCLUDED_SUFFIXES={'.pyc','.pyo'}
EXCLUDED_FILENAMES={'.DS_Store','.coverage'}

def excluded(p:Path):
    parts=p.relative_to(ROOT).parts
    return any(x in EXCLUDED_DIRS for x in parts) or p.name in EXCLUDED_FILENAMES or p.suffix.lower() in EXCLUDED_SUFFIXES

def main():
    DIST.mkdir(exist_ok=True)
    zip_path=DIST/NAME
    sha_path=DIST/(NAME+'.sha256.txt')
    if zip_path.exists(): zip_path.unlink()
    if sha_path.exists(): sha_path.unlink()
    with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(ROOT.rglob('*')):
            if not path.is_file() or excluded(path): continue
            arc=Path('acceptance-plane-public-readiness-kit')/path.relative_to(ROOT)
            z.write(path, arc.as_posix())
    with zipfile.ZipFile(zip_path) as z:
        bad=z.testzip()
        if bad: raise SystemExit(f'ZIP CRC failed: {bad}')
    digest=hashlib.sha256(zip_path.read_bytes()).hexdigest()
    sha_path.write_text(f'{digest}  {zip_path.name}\n', encoding='utf-8')
    print('release zip:', zip_path)
    print('sha256:', digest)
    return 0
if __name__=='__main__': raise SystemExit(main())
