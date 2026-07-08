#!/usr/bin/env python3
"""Validate public-safe crosswalk files."""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
FILES=[
    ROOT/'crosswalks/nist_ai_rmf_crosswalk.json',
    ROOT/'crosswalks/owasp_agentic_ai_crosswalk.json',
    ROOT/'crosswalks/five_eyes_agentic_ai_crosswalk.json',
    ROOT/'crosswalks/iso_iec_42001_crosswalk.json',
]
REQUIRED={"source","source_url","scope_boundary","mappings"}
MAP_REQUIRED={"source_area","acceptance_plane_question","public_readiness_prompt","scope_boundary"}
FORBIDDEN=["compliance mapping", "certification claim", "formal standards alignment"]

def main() -> int:
    errors=[]
    total=0
    for path in FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        try:
            doc=json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)} invalid JSON: {exc}"); continue
        missing=REQUIRED-set(doc)
        if missing: errors.append(f"{path.relative_to(ROOT)} missing {sorted(missing)}")
        boundary=doc.get('scope_boundary','').lower()
        if not all(word in boundary for word in ['educational','not']):
            errors.append(f"{path.relative_to(ROOT)} boundary must be educational and non-claiming")
        maps=doc.get('mappings',[])
        if not isinstance(maps,list) or len(maps)<5:
            errors.append(f"{path.relative_to(ROOT)} must have at least five mappings")
            maps=[]
        for i,m in enumerate(maps, start=1):
            total += 1
            miss=MAP_REQUIRED-set(m)
            if miss: errors.append(f"{path.relative_to(ROOT)} mapping {i} missing {sorted(miss)}")
            text=json.dumps(m, ensure_ascii=False).lower()
            # These phrases are allowed only inside the explicit boundary sentence with a negation.
            for phrase in FORBIDDEN:
                if phrase in text and f"not a {phrase}" not in text and f"not {phrase}" not in text:
                    errors.append(f"{path.relative_to(ROOT)} mapping {i} unsafe phrase: {phrase}")
    if errors:
        print('crosswalk lint: FAIL')
        for e in errors: print('-',e)
        return 1
    print('crosswalk lint: PASS')
    print(f'crosswalks: {len(FILES)}')
    print(f'mappings: {total}')
    print('boundary: educational crosswalks only; not compliance mapping or certification claim')
    return 0

if __name__=='__main__': raise SystemExit(main())
