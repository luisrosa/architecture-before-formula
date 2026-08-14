#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, stat, textwrap, zipfile
from pathlib import Path
FIXED_TIME=(2026,8,14,0,0,0)
EXCLUDED_SUFFIXES={'.aux','.bbl','.bcf','.blg','.fdb_latexmk','.fls','.log','.out','.run.xml','.synctex.gz','.toc','.pdf','.zip','.pyc'}
ROOT_FILES=['LICENSE','CITATION.cff','CHANGELOG.md','CLAIMS.md','VALIDATION.md','THIRD_PARTY_NOTICES.md','build.sh']
PACKAGE_README=textwrap.dedent('''\
# Architecture Before the Formula v1.6 — public source package

Maintained public LaTeX source and audit metadata for *Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map*. The archival public record is arXiv:2601.11618v3. Build from the package root with `bash ./build.sh`.
''')
def excluded(path: Path)->bool:
    if path.name=='jmlr2e.sty': return True
    return any(path.name.endswith(s) for s in EXCLUDED_SUFFIXES)
def zinfo(name:str, executable:bool=False)->zipfile.ZipInfo:
    i=zipfile.ZipInfo(name,FIXED_TIME); mode=0o755 if executable else 0o644; i.external_attr=(stat.S_IFREG|mode)<<16; return i
def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    root=a.root.resolve(); out=a.output.resolve(); out.parent.mkdir(parents=True,exist_ok=True); prefix='architecture-before-formula-v1.6-source'
    files=[]
    for rel in ROOT_FILES:
        p=root/rel
        if not p.is_file(): raise SystemExit(f'missing source-package file: {rel}')
        files.append(p)
    for d in ['paper','docs']:
        for p in sorted((root/d).rglob('*')):
            if p.is_file() and not excluded(p): files.append(p)
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        z.writestr(zinfo(f'{prefix}/README.md'),PACKAGE_README.encode())
        for p in sorted(set(files)):
            rel=p.relative_to(root).as_posix(); z.writestr(zinfo(f'{prefix}/{rel}',os.access(p,os.X_OK)),p.read_bytes())
    print(out)
if __name__=='__main__': main()
