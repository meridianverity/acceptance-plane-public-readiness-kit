#!/usr/bin/env python3
"""Generate a public-safe workshop packet from scenario cards."""
from __future__ import annotations
import argparse, json, shutil, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
DEFAULT_IDS=['AP-SCEN-001','AP-SCEN-010','AP-SCEN-035','AP-SCEN-064','AP-SCEN-099']
BOUNDARY='public workshop packet only; not certification, compliance approval, production readiness, or an allow/deny decision'

def find_card(card_id):
    for folder in ['scenarios_batch_1','scenarios_batch_2']:
        p=ROOT/folder/f'{card_id}.json'
        if p.exists(): return p, json.loads(p.read_text(encoding='utf-8'))
    raise SystemExit(f'missing scenario card {card_id}')

def main(argv):
    p=argparse.ArgumentParser(); p.add_argument('--out',default='/tmp/acceptance-plane-workshop-pack'); p.add_argument('--cards',nargs='*',default=DEFAULT_IDS); args=p.parse_args(argv[1:])
    out=Path(args.out); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True, exist_ok=True)
    cards=[find_card(cid) for cid in args.cards]
    (out/'agenda.md').write_text('# Workshop Agenda\n\n1. Boundary framing\n2. Scenario review\n3. Readiness index questions\n4. Decision log\n5. Action items\n\nBoundary: '+BOUNDARY+'\n', encoding='utf-8')
    lines=['# Selected Scenario Cards\n']
    for _,c in cards:
        lines.append(f"\n## {c['id']} — {c['title']}\n\n- Domain: {c['domain']}\n- Discussion label: {c['expected_decision']}\n- Boundary: {c['acceptance_boundary']}\n- Learning goal: {c['learning_goal']}\n")
    lines.append('\nBoundary: scenario labels are for tabletop discussion only.\n')
    (out/'selected_scenario_cards.md').write_text('\n'.join(lines), encoding='utf-8')
    (out/'readiness_questions.md').write_text((ROOT/'workshops/participant_worksheet.md').read_text(encoding='utf-8'), encoding='utf-8')
    (out/'decision_log_template.md').write_text('# Decision Log Template\n\n| Scenario | ACCEPT/HOLD/REFUSE discussion label | Evidence gap | Owner | Next step |\n|---|---|---|---|---|\n', encoding='utf-8')
    (out/'action_items.md').write_text('# Action Items\n\n- [ ] Name acceptance boundary owner.\n- [ ] Record top readiness gaps.\n- [ ] Decide whether separate conformance evidence is needed.\n\nBoundary: '+BOUNDARY+'\n', encoding='utf-8')
    required=['agenda.md','selected_scenario_cards.md','readiness_questions.md','decision_log_template.md','action_items.md']
    missing=[name for name in required if not (out/name).exists()]
    if missing:
        print('workshop pack: FAIL', missing); return 1
    print('workshop pack: PASS')
    print('output:', out)
    print('files:', ', '.join(required))
    print('boundary:', BOUNDARY)
    return 0
if __name__=='__main__': raise SystemExit(main(sys.argv))
