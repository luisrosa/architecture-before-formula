#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import stat
import textwrap
import zipfile
from pathlib import Path

FIXED_TIME = (2026, 8, 6, 0, 0, 0)
EXCLUDED_SUFFIXES = {
    '.aux', '.bbl', '.bcf', '.blg', '.fdb_latexmk', '.fls', '.log', '.out',
    '.run.xml', '.synctex.gz', '.toc', '.pdf', '.zip', '.pyc'
}
ROOT_FILES = [
    'LICENSE', 'CITATION.cff', 'CHANGELOG.md', 'CLAIMS.md', 'VALIDATION.md',
    'build.sh'
]

PACKAGE_README = textwrap.dedent('''\
# Architecture Before the Formula v1.0 - source package

This archive contains the complete LaTeX source for:

**Architecture Before the Formula: Receiver-Wise Factorization and the Reconstruction of Transformer Blocks**

It excludes compiled PDFs, generated LaTeX products, release artifacts, Git history, and CI-only files.

## Build

Requirements:

- `latexmk`
- `pdflatex`
- `bibtex` or `bibtex8`
- a standard TeX Live scientific installation

From the package root:

```bash
bash ./build.sh
```

The compiled article and supplement are written to `.build/output/`.

The compiled v1.0 PDFs and release checksums are distributed separately with the GitHub release.
''')


def excluded(path: Path) -> bool:
    return any(path.name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES)


def zip_info(name: str, executable: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_TIME)
    mode = 0o755 if executable else 0o644
    info.external_attr = (stat.S_IFREG | mode) << 16
    return info


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    prefix = 'architecture-before-formula-v1.0-source'

    files: list[Path] = []
    for rel in ROOT_FILES:
        path = root / rel
        if not path.is_file():
            raise SystemExit(f'missing source-package file: {rel}')
        files.append(path)
    for directory in ['paper', 'docs']:
        for path in sorted((root / directory).rglob('*')):
            if path.is_file() and not excluded(path):
                files.append(path)

    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.writestr(zip_info(f'{prefix}/README.md'), PACKAGE_README.encode())
        for path in sorted(set(files)):
            rel = path.relative_to(root).as_posix()
            executable = os.access(path, os.X_OK)
            zf.writestr(zip_info(f'{prefix}/{rel}', executable), path.read_bytes())

    print(output)


if __name__ == '__main__':
    main()
