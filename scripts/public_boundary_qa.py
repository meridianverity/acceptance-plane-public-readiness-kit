#!/usr/bin/env python3
"""Public boundary QA for the Acceptance Plane Public Readiness Kit."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import csv, json, re

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"
SCENARIO_BATCHES = [ROOT / "scenarios_batch_1", ROOT / "scenarios_batch_2"]
VALID_DECISIONS = {"ACCEPT", "HOLD", "REFUSE"}
REQUIRED_NOTICE = "Not a product implementation. Not a standard. No patent license. No certification right."
CANONICAL_DOI = "10.5281/zenodo.20645907"
TEXT_SUFFIXES = {"", ".cff", ".csv", ".gitignore", ".gitattributes", ".editorconfig", ".json", ".md", ".py", ".sh", ".txt", ".yaml", ".yml"}
TEXT_FILENAMES = {"LICENSE", "NOTICE", "VERSION", "Makefile"}
EXCLUDE_FROM_TEXT_SCAN = {"provenance/MANIFEST.sha256"}
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv", "build", "dist", "htmlcov"}
PUBLIC_HYPE_TOKENS = ["apex", "99.9", "99.99", "$100m", "world #1", "nobel", "kingdom port", "big tech can't", "big tech cannot"]
ALLOWED_LITERAL_FILES = {"scripts/public_boundary_qa.py", "tools/scenario-card-lint/scenario_card_lint.py"}
errors: list[str] = []

def rel(path: Path) -> str: return path.relative_to(ROOT).as_posix()
def is_excluded(path: Path) -> bool:
    r = rel(path)
    return r in EXCLUDE_FROM_TEXT_SCAN or path.name in {".DS_Store", ".coverage"} or path.suffix.lower() in {".pyc", ".pyo"} or any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)
def is_text_file(path: Path) -> bool: return not is_excluded(path) and (path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_SUFFIXES)
def read(path: Path) -> str: return path.read_text(encoding="utf-8")
def require(relative: str) -> str:
    p=ROOT/relative
    if not p.exists(): errors.append(f"{relative}: missing"); return ""
    return read(p)

def check_scenarios():
    cards=[]; expected=[f"AP-SCEN-{i:03d}" for i in range(1,101)]
    for b in SCENARIO_BATCHES:
        files=sorted(b.glob('AP-SCEN-*.json'))
        if len(files)!=50: errors.append(f"{rel(b)}: expected 50 scenario cards, found {len(files)}")
        for p in files:
            try: c=json.loads(read(p))
            except Exception as exc: errors.append(f"{rel(p)} invalid json: {exc}"); continue
            cards.append((p,c))
            if c.get('expected_decision') not in VALID_DECISIONS: errors.append(f"{rel(p)} invalid decision")
            if len(c.get('public_evidence_categories',[]))<5: errors.append(f"{rel(p)} too few evidence categories")
            if 'rights_boundary' not in c: errors.append(f"{rel(p)} missing rights boundary")
    ids=[c.get('id') for _,c in cards]
    if len(cards)!=100: errors.append(f"expected 100 cards, found {len(cards)}")
    if sorted(ids)!=expected: errors.append('scenario IDs do not match AP-SCEN-001..100')
    idx=ROOT/'scenarios/index.csv'
    if not idx.exists(): errors.append('missing scenarios/index.csv')
    else:
        rows=list(csv.DictReader(idx.open(newline='',encoding='utf-8')))
        if sorted(row.get('id') for row in rows)!=expected: errors.append('scenarios/index.csv IDs mismatch')
    return cards

def check_versions_and_core():
    for f in ['README.md','README_ko.md','NOTICE','QUICKSTART.md','GITHUB_UPLOAD_GUIDE.md','RELEASE_CHECKLIST.md','PATENT_AND_TRADEMARK_NOTICE.md','ATTRIBUTION.md','LICENSE','docs/19-license-and-rights-boundary.md']:
        text=require(f)
        if f in {'README.md','README_ko.md','NOTICE','QUICKSTART.md'} and REQUIRED_NOTICE not in text:
            errors.append(f'{f}: missing exact boundary notice')
    if require('VERSION').strip()!=VERSION: errors.append('VERSION mismatch')
    cff=require('CITATION.cff')
    if f'version: "{VERSION}"' not in cff: errors.append('CITATION.cff version mismatch')
    if CANONICAL_DOI not in cff or 'preferred-citation:' not in cff: errors.append('CITATION.cff missing preferred DOI')
    zen=json.loads(require('.zenodo.json') or '{}')
    if zen.get('version')!=VERSION: errors.append('.zenodo.json version mismatch')
    if not any(r.get('identifier')==CANONICAL_DOI for r in zen.get('related_identifiers',[])): errors.append('.zenodo.json missing canonical DOI')
    make=require('Makefile')
    for target in ['readiness-demo:', 'crosswalk-check:', 'coverage-check:', 'workshop-demo:', 'external-pointer-check:', 'release-zip:', 'verify-release:', 'qa-full:']:
        if target not in make: errors.append(f'Makefile missing {target}')

def check_required_new_files():
    required=[
        'readiness/action_acceptance_readiness_index.schema.json','readiness/index_items.json','readiness/scoring_model.md','readiness/sample_readiness_assessment.json','readiness/sample_readiness_report.md',
        'crosswalks/README.md','crosswalks/crosswalk.schema.json','crosswalks/nist_ai_rmf_crosswalk.json','crosswalks/owasp_agentic_ai_crosswalk.json','crosswalks/five_eyes_agentic_ai_crosswalk.json','crosswalks/iso_iec_42001_crosswalk.json',
        'docs/25-public-evidence-ladder.md','docs/26-readiness-to-conformance-bridge.md',
        'metadata/external_artifact_pointer_lock.json','metadata/external_artifact_pointer_lock.schema.json','metadata/github_release_body_v0.2.0.md','metadata/release_pointer_lock_v0.2.0.md',
        'scenario_coverage/domain_coverage_matrix.csv','scenario_coverage/decision_balance_report.json','scenario_coverage/evidence_category_heatmap.json','scenario_coverage/scenario_taxonomy.md',
        'workshops/30_min_board_briefing.md','workshops/60_min_ciso_platform_review.md','workshops/90_min_procurement_vendor_review.md','workshops/2_hour_incident_tabletop.md','workshops/facilitator_guide.md','workshops/participant_worksheet.md',
        'procurement/vendor_disclosure_questions.md','procurement/buyer_due_diligence_checklist.md','procurement/non_certification_language.md','procurement/rfp_clause_library.md','procurement/vendor_response_red_flags.md',
        'tools/readiness-index/readiness_index.py','tools/crosswalk-lint/crosswalk_lint.py','tools/scenario-coverage/scenario_coverage.py','tools/workshop-pack/workshop_pack.py','tools/external-pointer-check/external_pointer_check.py',
        'scripts/build_release_zip.py','scripts/verify_release_artifact.py','provenance/SLSA.intoto.json','.github/workflows/release-artifacts.yml','.github/workflows/scorecard.yml','.github/workflows/attest-release.yml'
    ]
    for r in required: require(r)

def check_external_pointer():
    doc=json.loads(require('metadata/external_artifact_pointer_lock.json') or '{}')
    text=json.dumps(doc).lower()
    if 'not bundled' not in text or 'separate artifact' not in text: errors.append('external pointer lock missing separation boundary')
    for name in ['acceptance_plane_interop_gauntlet','acceptance_plane_independent_verifier']:
        art=doc.get('artifacts',{}).get(name,{})
        if not re.fullmatch(r'[0-9a-f]{64}', art.get('sha256','')): errors.append(f'{name}: invalid sha256')

def full_scan():
    files=[p for p in ROOT.rglob('*') if p.is_file() and is_text_file(p)]
    unsafe_patterns=[
        ('positive product implementation claim', re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(product implementation|reference implementation|production sdk|sdk|implementation package)\b", re.I)),
        ('positive formal standard claim', re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|defines|creates|establishes)\s+(a\s+)?(formal\s+)?standard\b", re.I)),
        ('positive rights grant', re.compile(r"\b(grants?|granting|provides|providing)\s+(a\s+)?(patent|trademark|service mark|implementation|certification)\s+(license|right)\b", re.I)),
        ('positive approval claim', re.compile(r"\b(certifies|certification granted|officially certified|compliance approved|procurement approved|production-ready)\b", re.I)),
        ('positive conformance program claim', re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(conformance suite|conformance test suite|certificate registry|certification program)\b", re.I)),
        ('positive production mechanism claim', re.compile(r"\b(this|the)\s+(kit|repository|release|package)\s+(is|provides|contains|includes)\s+(a\s+)?(production verifier|permitreceipt engine|non-bypassable interceptor|cryptographic binding method|exact evidence schema|hardware adapter|patent claim chart)\b", re.I)),
    ]
    scanned=hits=0
    for p in files:
        r=rel(p); text=read(p); scanned+=1; lower=text.lower()
        if r not in ALLOWED_LITERAL_FILES:
            for token in PUBLIC_HYPE_TOKENS:
                if token in lower:
                    errors.append(f'{r}: public hype/internal token remains: {token}'); hits+=1
        for label,pat in unsafe_patterns:
            for m in pat.finditer(text):
                if r in ALLOWED_LITERAL_FILES: continue
                ctx=text[max(0,m.start()-120):m.end()+120].lower()
                if any(g in ctx for g in ['not ', 'does not ', 'do not ', 'no ', 'without ', 'must not ', 'avoid ', 'is not ', 'not a ', 'not an ', 'doesn’t ', "don't "]):
                    continue
                errors.append(f"{r}: {label}: {m.group(0)!r}"); hits+=1
    return scanned,hits

def main():
    cards=check_scenarios(); check_versions_and_core(); check_required_new_files(); check_external_pointer(); scanned,hits=full_scan()
    if errors:
        print('QA FAILED')
        for e in errors: print('-',e)
        return 1
    print('QA PASSED')
    print('Scenario cards:', len(cards))
    print('Decision balance:', dict(Counter(c['expected_decision'] for _,c in cards)))
    print('Domain balance:', dict(Counter(c['domain'] for _,c in cards)))
    print(f'Full-repo text boundary scan: {scanned} files scanned, {hits} unsafe hits')
    print('Boundary notice: present')
    print('Readiness index: present')
    print('Crosswalks: present')
    print('Evidence ladder: present')
    print('Workshop/procurement pack: present')
    print('External pointer lock: present')
    print('Release artifact tools: present')
    print('Public hype/internal wording scan: passed')
    return 0
if __name__=='__main__': raise SystemExit(main())
