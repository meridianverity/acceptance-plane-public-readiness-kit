#!/usr/bin/env python3
"""Generate/check public crosswalk coverage heatmap."""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'crosswalk_coverage'
BOUNDARY='public crosswalk coverage only; not compliance mapping, certification, legal opinion, or standards approval'
files=sorted((ROOT/'crosswalks').glob('*_crosswalk.json'))
errors=[]; heatmap={}; total=0
for p in files:
    doc=json.loads(p.read_text(encoding='utf-8'))
    mappings=doc.get('mappings',[])
    if len(mappings)<4: errors.append(f'{p.name}: too few mappings')
    areas=Counter(m.get('source_area','(missing)') for m in mappings)
    heatmap[doc.get('source',p.stem)]={'mappings':len(mappings),'source_areas':dict(sorted(areas.items()))}
    total += len(mappings)
if len(files)!=4: errors.append(f'expected 4 crosswalk files, found {len(files)}')
if total<24: errors.append(f'expected at least 24 mappings, found {total}')
OUT.mkdir(exist_ok=True)
(OUT/'crosswalk_coverage_heatmap.json').write_text(json.dumps({'sources':heatmap,'total_mappings':total,'boundary':BOUNDARY},indent=2)+'\n',encoding='utf-8')
if errors:
    print('crosswalk coverage: FAIL')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('crosswalk coverage: PASS')
print(f'sources: {len(files)}')
print(f'mappings: {total}')
print('output: crosswalk_coverage/crosswalk_coverage_heatmap.json')
print('boundary:',BOUNDARY)
