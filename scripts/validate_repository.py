#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import re
import sys
import urllib.parse
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.tex', '.bib', '.cff', '.yml', '.yaml', '.py', '.sh', '.txt'}
AUX_SUFFIXES = {
    '.aux', '.bbl', '.bcf', '.blg', '.fdb_latexmk', '.fls', '.log', '.out',
    '.run.xml', '.synctex.gz', '.toc'
}
FORBIDDEN_PUBLIC_TERMS = [
    'companion theory', 'companion work', 'companion manuscript',
    'private cross-paper dependency'
]


def fail(messages: list[str]) -> None:
    if messages:
        raise SystemExit('\n'.join(messages))


def text_files() -> list[Path]:
    return [
        p for p in ROOT.rglob('*') if p.is_file()
        and '.git' not in p.parts and '.build' not in p.parts
        and (p.suffix in TEXT_SUFFIXES or p.name in {'CITATION.cff', 'LICENSE'})
    ]


def check_structure() -> list[str]:
    required = [
        'README.md', 'LICENSE', 'CITATION.cff', 'CHANGELOG.md', 'CLAIMS.md',
        'VALIDATION.md', 'build.sh', 'paper/main.tex', 'paper/supplement.tex',
        'paper/preamble.tex', 'paper/references.bib',
        'paper/references_additions.bib',
        'releases/v1.0/Architecture_Before_the_Formula_v1.0.pdf',
        'releases/v1.0/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf',
        'releases/v1.0/Architecture_Before_the_Formula_v1.0_Source.zip',
        'releases/v1.0/SHA256SUMS.txt',
        '.github/workflows/validate-paper.yml',
    ]
    errors = [f'missing required path: {p}' for p in required if not (ROOT / p).exists()]
    legacy_dirs = [p for p in (ROOT / 'paper').iterdir() if p.is_dir() and re.fullmatch(r'v\d+_\d+(?:_\d+)?', p.name)]
    errors.extend(f'forbidden versioned source directory exists: {p.relative_to(ROOT)}' for p in legacy_dirs)
    if (ROOT / 'paper/source').exists():
        errors.append('forbidden legacy source directory exists: paper/source')
    return errors


def check_text() -> list[str]:
    errors: list[str] = []
    for path in text_files():
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(errors='replace')
        lower = text.lower()
        for term in FORBIDDEN_PUBLIC_TERMS:
            if term in lower:
                errors.append(f'{path.relative_to(ROOT)} contains development-only term: {term}')
        current_release_docs = {
            ROOT / 'CITATION.cff', ROOT / 'CLAIMS.md', ROOT / 'VALIDATION.md',
            ROOT / 'releases/v1.0/README.md'
        }
        if path.is_relative_to(ROOT / 'paper') or path in current_release_docs:
            if re.search(r'\bv0(?:[._]\d+)+\b', lower):
                errors.append(f'{path.relative_to(ROOT)} contains a stale pre-release token')
    return errors


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    pattern = re.compile(r'!?\[[^]]*\]\(([^)]+)\)')
    for path in ROOT.rglob('*.md'):
        if '.build' in path.parts:
            continue
        text = path.read_text(errors='replace')
        for target in pattern.findall(text):
            target = target.strip().split()[0]
            if target.startswith(('#', 'http://', 'https://', 'mailto:')):
                continue
            target = urllib.parse.unquote(target.split('#', 1)[0])
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)} has broken local link: {target}')
    return errors


def check_tex() -> list[str]:
    errors: list[str] = []
    tex_files = list((ROOT / 'paper').rglob('*.tex'))
    labels: list[str] = []
    refs: list[str] = []
    cites: list[str] = []
    for path in tex_files:
        text = path.read_text()
        labels.extend(re.findall(r'\\label\{([^}]+)\}', text))
        for group in re.findall(r'\\(?:Cref|cref|ref|eqref)\{([^}]+)\}', text):
            refs.extend(x.strip() for x in group.split(','))
        for group in re.findall(r'\\cite\w*\{([^}]+)\}', text):
            cites.extend(x.strip() for x in group.split(','))
    counts = collections.Counter(labels)
    duplicates = sorted(k for k, v in counts.items() if v > 1)
    missing_refs = sorted(set(refs) - set(labels))
    bib = (ROOT / 'paper/references.bib').read_text() + (ROOT / 'paper/references_additions.bib').read_text()
    keys = set(re.findall(r'@\w+\{([^,]+),', bib))
    missing_cites = sorted(set(cites) - keys)
    if duplicates:
        errors.append(f'duplicate labels: {duplicates}')
    if missing_refs:
        errors.append(f'missing references: {missing_refs}')
    if missing_cites:
        errors.append(f'missing citations: {missing_cites}')
    return errors


def check_cff() -> list[str]:
    errors: list[str] = []
    data = yaml.safe_load((ROOT / 'CITATION.cff').read_text())
    expected = {
        'cff-version': '1.2.0',
        'type': 'software',
        'version': '1.0',
        'license': 'CC-BY-4.0',
    }
    for key, value in expected.items():
        if str(data.get(key)) != value:
            errors.append(f'CITATION.cff: {key} must be {value!r}')
    preferred = data.get('preferred-citation') or {}
    if preferred.get('type') != 'article':
        errors.append('CITATION.cff: preferred-citation.type must be article')
    if str(preferred.get('version')) != '1.0':
        errors.append('CITATION.cff: preferred-citation.version must be 1.0')
    return errors


def check_source_zip() -> list[str]:
    errors: list[str] = []
    path = ROOT / 'releases/v1.0/Architecture_Before_the_Formula_v1.0_Source.zip'
    if not path.exists():
        return [f'missing source ZIP: {path.relative_to(ROOT)}']
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        for name in names:
            base = Path(name).name
            if any(base.endswith(suffix) for suffix in AUX_SUFFIXES):
                errors.append(f'source ZIP contains generated file: {name}')
            if base.endswith(('.pdf', '.zip')):
                errors.append(f'source ZIP contains binary release artifact: {name}')
        required = ['README.md', 'LICENSE', 'CITATION.cff', 'paper/main.tex', 'paper/references.bib']
        for req in required:
            if not any(name.endswith('/' + req) for name in names):
                errors.append(f'source ZIP missing: {req}')
    return errors


def check_prebuild_cleanliness() -> list[str]:
    errors: list[str] = []
    for path in (ROOT / 'paper').iterdir():
        if path.is_file() and any(path.name.endswith(s) for s in AUX_SUFFIXES | {'.pdf'}):
            errors.append(f'generated file committed in paper/: {path.name}')
    workflows = list((ROOT / '.github/workflows').glob('*.yml'))
    if [p.name for p in workflows] != ['validate-paper.yml']:
        errors.append(f'expected exactly validate-paper.yml, found {[p.name for p in workflows]}')
    return errors


def check_cref_types() -> list[str]:
    errors: list[str] = []
    expected = {
        'def': 'definition', 'lem': 'lemma', 'prop': 'proposition',
        'ass': 'assumption', 'cor': 'corollary', 'thm': 'theorem',
        'ex': 'example', 'rem': 'remark',
    }
    for aux_path in [ROOT / 'paper/main.aux', ROOT / 'paper/supplement.aux']:
        if not aux_path.exists():
            errors.append(f'missing post-build aux file: {aux_path.relative_to(ROOT)}')
            continue
        text = aux_path.read_text(errors='replace')
        for label, actual in re.findall(
            r'\\newlabel\{((?:def|lem|prop|ass|cor|thm|ex|rem):[^}]+)@cref\}\{\{\[([^]]+)\]', text
        ):
            prefix = label.split(':', 1)[0]
            if actual != expected[prefix]:
                errors.append(f'{label} recorded as {actual}, expected {expected[prefix]}')
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['prebuild', 'postbuild'], default='prebuild')
    args = parser.parse_args()
    errors: list[str] = []
    errors += check_structure()
    errors += check_text()
    errors += check_markdown_links()
    errors += check_tex()
    errors += check_cff()
    errors += check_source_zip()
    if args.mode == 'prebuild':
        errors += check_prebuild_cleanliness()
    else:
        errors += check_cref_types()
    fail(errors)
    print(f'repository validation passed ({args.mode})')


if __name__ == '__main__':
    main()
