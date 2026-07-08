#!/usr/bin/env python3
"""Scenario coverage reporter for the public readiness corpus."""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT=Path(__file__).resolve().parents[2]
BATCHES=sorted(p for p in ROOT.glob('scenarios_batch_*') if p.is_dir())
EXPECTED_CARDS=300
EXPECTED_DOMAINS=10
EXPECTED_PER_DOMAIN=30
MIN_DECISION_COVERAGE=90
OUT=ROOT/'scenario_coverage'
BOUNDARY='coverage for education only; not conformance coverage, certification coverage, compliance coverage, or implementation test coverage'

def cards():
    out=[]
    for b in BATCHES:
        for p in sorted(b.glob('AP-SCEN-*.json')):
            out.append((p,json.loads(p.read_text(encoding='utf-8'))))
    return out

def compute():
    cs=cards()
    domains=Counter(c['domain'] for _,c in cs)
    decisions=Counter(c['expected_decision'] for _,c in cs)
    risk=Counter(c.get('risk_tier','') for _,c in cs)
    evidence=Counter()
    by_domain_evidence=defaultdict(Counter)
    for _,c in cs:
        for e in c.get('public_evidence_categories',[]):
            evidence[e]+=1
            by_domain_evidence[c['domain']][e]+=1
    return cs,domains,decisions,risk,evidence,by_domain_evidence

def write_reports():
    cs,domains,decisions,risk,evidence,by_domain_evidence=compute()
    OUT.mkdir(exist_ok=True)
    with (OUT/'domain_coverage_matrix.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['domain','cards','accept','hold','refuse','high_consequence','context_dependent'])
        for domain,count in sorted(domains.items()):
            dc=[c for _,c in cs if c['domain']==domain]
            dd=Counter(c['expected_decision'] for c in dc); rr=Counter(c.get('risk_tier','') for c in dc)
            w.writerow([domain,count,dd.get('ACCEPT',0),dd.get('HOLD',0),dd.get('REFUSE',0),rr.get('high-consequence',0),rr.get('context-dependent',0)])
    (OUT/'decision_balance_report.json').write_text(json.dumps({
        'cards':len(cs), 'domains':dict(sorted(domains.items())), 'decisions':dict(decisions), 'risk_tiers':dict(risk), 'boundary':BOUNDARY
    }, indent=2), encoding='utf-8')
    (OUT/'evidence_category_heatmap.json').write_text(json.dumps({
        'evidence_categories':dict(sorted(evidence.items())),
        'by_domain':{d:dict(sorted(c.items())) for d,c in sorted(by_domain_evidence.items())},
        'boundary':BOUNDARY
    }, indent=2), encoding='utf-8')

def main(argv):
    p=argparse.ArgumentParser(); p.add_argument('--write',action='store_true'); args=p.parse_args(argv[1:])
    if args.write: write_reports()
    cs,domains,decisions,risk,evidence,_=compute()
    errors=[]
    if len(cs)!=EXPECTED_CARDS: errors.append(f'expected {EXPECTED_CARDS} cards, found {len(cs)}')
    if len(domains)!=EXPECTED_DOMAINS: errors.append(f'expected {EXPECTED_DOMAINS} domains, found {len(domains)}')
    if any(v!=EXPECTED_PER_DOMAIN for v in domains.values()): errors.append(f'domain imbalance: {dict(domains)}')
    for label in ['ACCEPT','HOLD','REFUSE']:
        if decisions.get(label,0)<MIN_DECISION_COVERAGE: errors.append(f'decision label under-covered: {label}={decisions.get(label,0)}')
    if len(evidence)<12: errors.append(f'expected at least 12 evidence categories, found {len(evidence)}')
    if errors:
        print('scenario coverage: FAIL')
        for e in errors: print('-',e)
        return 1
    print('scenario coverage: PASS')
    print(f'Cards: {len(cs)}')
    print(f'Domains: {len(domains)} / {EXPECTED_DOMAINS} balanced')
    print(f'Decision labels: {dict(decisions)}')
    print(f'Evidence categories: {len(evidence)} / 12 covered')
    print(f'High-consequence coverage: {round(risk.get("high-consequence",0)/len(cs)*100)}%')
    print('Coverage status: PUBLIC_READINESS_OPERATING_CORPUS_READY')
    print('Boundary:',BOUNDARY)
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
