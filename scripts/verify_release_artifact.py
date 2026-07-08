#!/usr/bin/env python3
"""Verify release ZIP shape, path safety, SHA sidecar, CRC, and in-archive manifest."""
from __future__ import annotations
import argparse, hashlib, zipfile, re
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'provenance/MANIFEST.sha256'}

def sha256_bytes(data:bytes)->str: return hashlib.sha256(data).hexdigest()

def parse_sidecar(path:Path):
    text=path.read_text(encoding='utf-8').strip()
    parts=text.split()
    if len(parts)<1 or not re.fullmatch(r'[0-9a-f]{64}', parts[0]):
        raise SystemExit('release artifact verification: FAIL\n- malformed SHA-256 sidecar')
    return parts[0]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('zip_path'); ap.add_argument('--sha256-file'); args=ap.parse_args()
    zip_path=Path(args.zip_path)
    errors=[]
    if args.sha256_file:
        expected=parse_sidecar(Path(args.sha256_file)); actual=hashlib.sha256(zip_path.read_bytes()).hexdigest()
        if expected!=actual: errors.append('archive sha256 sidecar mismatch')
    with zipfile.ZipFile(zip_path) as z:
        bad=z.testzip()
        if bad: errors.append(f'zip CRC failed: {bad}')
        names=z.namelist()
        if len(names)!=len(set(names)): errors.append('duplicate archive member')
        file_names=[n for n in names if not n.endswith('/')]
        roots={PurePosixPath(n).parts[0] for n in file_names if PurePosixPath(n).parts}
        if roots!={'acceptance-plane-public-readiness-kit'}: errors.append(f'archive must have single root acceptance-plane-public-readiness-kit, found {sorted(roots)}')
        for n in names:
            p=PurePosixPath(n)
            if p.is_absolute() or '..' in p.parts: errors.append(f'unsafe archive path: {n}')
        mname='acceptance-plane-public-readiness-kit/provenance/MANIFEST.sha256'
        if mname not in file_names: errors.append('missing in-archive MANIFEST.sha256')
        else:
            manifest=z.read(mname).decode('utf-8')
            entries={}
            for line in manifest.splitlines():
                if not line.strip(): continue
                digest, rel=line.split('  ',1)
                entries[rel]=digest
            actual_rels=[]
            for n in file_names:
                rel=str(PurePosixPath(n).relative_to('acceptance-plane-public-readiness-kit'))
                if rel in EXCLUDED: continue
                actual_rels.append(rel)
            extra=sorted(set(actual_rels)-set(entries)); missing=sorted(set(entries)-set(actual_rels))
            if extra: errors.append('unmanifested archive files: '+', '.join(extra[:8]))
            if missing: errors.append('manifest entries missing from archive: '+', '.join(missing[:8]))
            for rel,digest in entries.items():
                n='acceptance-plane-public-readiness-kit/'+rel
                if n in file_names:
                    actual=sha256_bytes(z.read(n))
                    if actual!=digest: errors.append(f'archive hash mismatch: {rel}')
    if errors:
        print('release artifact verification: FAIL')
        for e in errors: print('-',e)
        return 1
    print('release artifact verification: PASS')
    print('archive sha256 sidecar: OK' if args.sha256_file else 'archive sha256 sidecar: not requested')
    print('archive manifest: OK')
    print('archive path safety: OK')
    print('zip CRC: OK')
    return 0
if __name__=='__main__': raise SystemExit(main())
