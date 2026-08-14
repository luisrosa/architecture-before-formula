#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, re, subprocess
from pathlib import Path
TITLE='Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map'
ARXIV='2601.11618'
EXPECTED_SECTIONS=['01_architecture_individuation.tex','02_related_objects.tex','03_receiver_access.tex','04_barriers.tex','05_composition.tex','05b_receiver_sufficient_prefix.tex','06_contextual_search.tex','07_transformer_realization.tex','08_scope_discussion.tex','09_conclusion.tex']
def fail(msg:str)->None: raise SystemExit(msg)
def sha256(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['prebuild','postbuild'],required=True); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); a=ap.parse_args(); root=a.root.resolve()
    required=[root/'README.md',root/'CLAIMS.md',root/'CITATION.cff',root/'CHANGELOG.md',root/'VALIDATION.md',root/'paper'/'main.tex',root/'paper'/'preamble_jmlr.tex',root/'releases'/'v1.6'/'SOURCE_SHA256SUMS.txt']
    for p in required:
        if not p.exists(): fail(f'missing required path: {p}')
    main_tex=(root/'paper'/'main.tex').read_text(); readme=(root/'README.md').read_text(); cff=(root/'CITATION.cff').read_text(); claims=(root/'CLAIMS.md').read_text()
    for text,label in [(main_tex,'paper/main.tex'),(readme,'README.md')]:
        if TITLE not in text: fail(f'current title missing from {label}')
    if 'version: "1.6"' not in cff or ARXIV not in cff: fail('CITATION.cff does not identify v1.6 and arXiv')
    if 'A_enc(u,v)=(2u+v,0)' not in claims: fail('claim ledger is missing injective contextual witness')
    found=sorted(p.name for p in (root/'paper'/'sections').glob('*.tex'))
    if found!=sorted(EXPECTED_SECTIONS): fail(f'unexpected current section surface: {found}')
    if (root/'paper'/'supplement.tex').exists() or (root/'paper'/'supplement').exists(): fail('stale v1.0 supplement remains in current paper surface')
    manifest=root/'releases'/'v1.6'/'SOURCE_SHA256SUMS.txt'
    for line in manifest.read_text().splitlines():
        if not line.strip(): continue
        expected,rel=line.split(None,1); p=root/'paper'/rel.strip()
        if not p.is_file(): fail(f'source manifest path missing: {p}')
        got=sha256(p)
        if got!=expected: fail(f'source hash mismatch for {rel}: {got}')
    if a.mode=='postbuild':
        candidates=[root/'paper'/'main.pdf',root/'.build'/'output'/'Architecture_Before_the_Formula_v1.6.pdf']; pdf=next((p for p in candidates if p.is_file()),None)
        if pdf is None: fail('no fresh-build PDF found')
        text=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True,errors='replace')
        if 'Architecture Before the Formula' not in text or 'Individuating Neural Architecture' not in text: fail('fresh-build PDF missing current title')
        info=subprocess.check_output(['pdfinfo',str(pdf)],text=True,errors='replace'); m=re.search(r'^Pages:\s+(\d+)',info,re.M)
        if not m or int(m.group(1))!=34: fail(f'expected 34-page fresh build; pdfinfo was:\n{info}')
    print(f'PUBLIC V1.6 REPOSITORY VALIDATION PASSED ({a.mode})')
if __name__=='__main__': main()
