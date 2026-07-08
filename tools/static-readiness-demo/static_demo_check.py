#!/usr/bin/env python3
"""Check the browser-only public readiness demo boundary."""
from __future__ import annotations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
files=[ROOT/'browser_readiness_demo/index.html', ROOT/'browser_readiness_demo/app.js', ROOT/'browser_readiness_demo/README.md']
errors=[]
for p in files:
    if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}')
text='\n'.join(p.read_text(encoding='utf-8') for p in files if p.exists()).lower()
for bad in ['fetch(', 'xmlhttprequest', 'http://', 'https://', 'certification' + ' granted', 'production' + '-ready']:
    if bad in text: errors.append(f'forbidden browser demo token: {bad}')
for need in ['network used: no','not certification','allow/deny decision']:
    if need not in text: errors.append(f'missing browser demo boundary phrase: {need}')
if errors:
    print('browser demo check: FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('browser demo check: PASS')
print('network used: no')
print('boundary: educational browser readiness discussion only')
