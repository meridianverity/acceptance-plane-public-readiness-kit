#!/usr/bin/env python3
"""Generate a public readiness report packet.

Educational report generator only. Not certification, compliance approval,
production readiness, procurement approval, or an allow/deny decision.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BOUNDARY='public readiness report only; not certification, compliance approval, procurement approval, production readiness, or an allow/deny decision'

def run_json(cmd):
    p=subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if p.returncode:
        raise SystemExit(p.stdout+p.stderr)
    return json.loads(p.stdout)

def main(argv):
    ap=argparse.ArgumentParser()
    ap.add_argument('--assessment', default='readiness/sample_readiness_assessment.json')
    ap.add_argument('--out', default='/tmp/acceptance-plane-public-readiness-report')
    args=ap.parse_args(argv[1:])
    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    readiness=run_json([sys.executable,'tools/readiness-index/readiness_index.py',args.assessment,'--format','json'])
    cov=json.loads((ROOT/'scenario_coverage/decision_balance_report.json').read_text(encoding='utf-8'))
    report={
        'tool':'acceptance-plane-public-report',
        'tool_version':'0.3.4',
        'readiness':readiness,
        'scenario_coverage':cov,
        'recommended_next_steps':[
            'run a board-to-builder workshop using the public packet',
            'document buyer questions without requesting private implementation details',
            'use the external pointer lock only when education must hand off to separate conformance evidence'
        ],
        'boundary':BOUNDARY,
    }
    (out/'public_readiness_report.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    md=[
        '# Acceptance Plane Public Readiness Report', '',
        f"Readiness posture: {readiness['readiness_posture']}",
        f"Discussion maturity: {readiness['discussion_maturity']} / 100", '',
        '## Scenario coverage',
        f"Cards: {cov['cards']}",
        f"Domains: {len(cov['domains'])}",
        f"Decision labels: {cov['decisions']}", '',
        '## Top gaps',
    ]
    for gap in readiness.get('top_gaps',[]):
        md.append(f"- {gap['gap']} ({gap['item_id']}, {gap['status']})")
    md += ['', f'Boundary: {BOUNDARY}', '']
    (out/'public_readiness_report.md').write_text('\n'.join(md), encoding='utf-8')
    print('public report generator: PASS')
    print('output:', out)
    print('files: public_readiness_report.md, public_readiness_report.json')
    print('boundary:', BOUNDARY)
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
