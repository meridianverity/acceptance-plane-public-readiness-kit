#!/usr/bin/env python3
"""Scenario uniqueness QA for the public readiness corpus."""
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict, Counter
ROOT = Path(__file__).resolve().parents[2]
EXPECTED_CARDS = 300

def load_cards():
    cards=[]
    for batch in sorted(ROOT.glob('scenarios_batch_*')):
        if batch.is_dir():
            for path in sorted(batch.glob('AP-SCEN-*.json')):
                cards.append((path, json.loads(path.read_text(encoding='utf-8'))))
    return cards

def stable_without_id(card):
    data={k:v for k,v in card.items() if k != 'id'}
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':'))

def main() -> int:
    cards=load_cards(); errors=[]
    if len(cards) != EXPECTED_CARDS:
        errors.append(f'expected {EXPECTED_CARDS} cards, found {len(cards)}')
    ids=[c.get('id') for _,c in cards]
    if len(ids) != len(set(ids)):
        errors.append('duplicate scenario ids: ' + ', '.join([k for k,v in Counter(ids).items() if v>1][:10]))
    checks=[('id-normalized duplicate cards', defaultdict(list)),('duplicate title/scenario pairs', defaultdict(list)),('repeated why text', defaultdict(list)),('repeated human_impact text', defaultdict(list)),('repeated learning_goal text', defaultdict(list)),('repeated acceptance_boundary text', defaultdict(list))]
    byname=dict(checks)
    for path,card in cards:
        byname['id-normalized duplicate cards'][stable_without_id(card)].append(path.as_posix())
        byname['duplicate title/scenario pairs'][(card.get('title','').strip().lower(), card.get('scenario','').strip().lower())].append(path.as_posix())
        byname['repeated why text'][card.get('why','').strip().lower()].append(path.as_posix())
        byname['repeated human_impact text'][card.get('human_impact','').strip().lower()].append(path.as_posix())
        byname['repeated learning_goal text'][card.get('learning_goal','').strip().lower()].append(path.as_posix())
        byname['repeated acceptance_boundary text'][card.get('acceptance_boundary','').strip().lower()].append(path.as_posix())
    for label,buckets in checks:
        groups=[v for k,v in buckets.items() if k and len(v)>1]
        if groups:
            errors.append(f'{label}: {len(groups)} groups')
    if errors:
        print('scenario uniqueness QA: FAIL')
        for e in errors: print('-',e)
        return 1
    print('scenario uniqueness QA: PASS')
    print(f'Cards: {len(cards)}')
    print('ID-normalized duplicate cards: 0')
    print('Duplicate title/scenario pairs: 0')
    print('Repeated why/human_impact/learning_goal/acceptance_boundary texts: 0')
    print('Boundary: educational corpus uniqueness only; not conformance, certification, compliance approval, production readiness, or an allow/deny decision.')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
