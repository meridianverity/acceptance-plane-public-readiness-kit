#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
required=['third_party_facilitator/REPRODUCTION_PACKET.md','third_party_facilitator/result-template.json','third_party_facilitator/facilitator-signoff-template.md']
errors=[]
for r in required:
    p=ROOT/r
    if not p.exists(): errors.append(f'missing {r}')
    elif 'not certification' not in p.read_text(encoding='utf-8').lower(): errors.append(f'{r}: missing boundary phrase')
if errors:
    print('facilitator packet: FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('facilitator packet: PASS')
print('boundary: public reproducibility only; no certification or production approval')
