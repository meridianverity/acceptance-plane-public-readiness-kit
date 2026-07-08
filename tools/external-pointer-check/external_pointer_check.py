#!/usr/bin/env python3
"""Validate public-safe external artifact pointer lock."""
from __future__ import annotations
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
LOCK=ROOT/'metadata/external_artifact_pointer_lock.json'
SHA_RE=re.compile(r'^[0-9a-f]{64}$')

def main():
    errors=[]
    if not LOCK.exists():
        print('external pointer check: FAIL\n- missing lock'); return 1
    doc=json.loads(LOCK.read_text(encoding='utf-8'))
    if 'not bundled' not in json.dumps(doc).lower(): errors.append('boundary should state separate artifacts are not bundled')
    arts=doc.get('artifacts',{})
    for key in ['acceptance_plane_interop_gauntlet','acceptance_plane_independent_verifier']:
        art=arts.get(key)
        if not art: errors.append(f'missing {key}'); continue
        if not SHA_RE.match(art.get('sha256','')): errors.append(f'{key} invalid sha256')
        if 'Separate artifact' not in art.get('boundary',''): errors.append(f'{key} missing separate-artifact boundary')
    if errors:
        print('external pointer check: FAIL')
        for e in errors: print('-',e)
        return 1
    print('external pointer check: PASS')
    print('gauntlet:', arts['acceptance_plane_interop_gauntlet']['version'], arts['acceptance_plane_interop_gauntlet']['sha256'])
    print('independent verifier:', arts['acceptance_plane_independent_verifier']['version'], arts['acceptance_plane_independent_verifier']['sha256'])
    print('boundary: pointer lock only; separate artifacts not bundled')
    return 0
if __name__=='__main__': raise SystemExit(main())
