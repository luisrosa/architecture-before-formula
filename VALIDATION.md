# v1.0 validation record

**Artifact:** *Architecture Before the Formula: Receiver-Wise Factorization and the Reconstruction of Transformer Blocks*  
**Version:** 1.0  
**Final pre-publication validation date:** 2026-08-09

## Status

The v1.0 repository is the maintained public source for the receiver-factorization manuscript. During the final pre-publication audit, the attention normal-form presentation was tightened so that the compositional positive-link assumption explicitly states the raw-weight relation used by its proof, the conventional additive-logit-bias convention was made explicit, the singleton-row anchoring proof was made fully literal, and two elementary omitted proof steps were supplied or clarified. The variable-successor extension was also written with an explicit restriction to each selected sector domain. These edits do not change the receiver-factorization primitive or the resulting Transformer normal form; they make the stated premises, typing, and proof dependencies explicit.

Repository-level provenance is carried by the immutable Git commit or tag being inspected, its associated GitHub Actions run, and the release hashes in `releases/v1.0/SHA256SUMS.txt`. Those identifiers are intentionally not duplicated as a commit hash inside this source file, which would make the recorded commit self-referential.

## Release evidence

| Item | Value |
|---|---|
| Main article | 30 pages; SHA-256 `8d9d8bc623f71e2f5b05b1c0fbe7605104f6d7beb4e84ee7a7dea254304f1805` pending refresh from the final validated build |
| Technical supplement | 14 pages; SHA-256 `e9b028b458984cec21ae6cca7454086dc7b0bb460e67972d74f78bb030028d2b` pending refresh from the final validated build |
| Build environment | GitHub Actions `xu-cheng/latex-action@v3`; exact runner/toolchain provenance is carried by the associated workflow run |
| Source layout | current source contained entirely in `paper/` |
| Bibliography | local `paper/references.bib` and `paper/references_additions.bib` |
| Font embedding | all fonts embedded in both PDFs |
| Rasterization | every page of both generated and committed release PDFs renders successfully |
| Source package | generated deterministically from the maintained repository tree and audited for generated/binary build products |

The clean source ZIP hash is recorded alongside the release artifacts rather than inside the archive, avoiding a self-referential package.

## Formal invariants

1. The receiver-factored architectural presentation remains the central typed object.
2. Every load-bearing result is proved in the main article or public supplement.
3. Bijective interface recoding is handled locally without importing a global mechanism-equivalence theory.
4. `P_j`, `Agg_j P_j`, `Q_j`, and `G_j` remain distinct.
5. Operator-valued pair contributions precede scalar relevance and transport.
6. The attention normal form explicitly links baseline and scalar evidence to raw weights before deriving the exponential row.
7. Attention remains a conditional normal form, with a typed neighboring witness for each commitment.
8. Effective-potential language remains downstream of positive scalar routing.
9. The actual FFN activation vector remains the hidden carrier.
10. The deterministic variable-successor architecture remains in the main article; stochastic realizations remain in the supplement.
11. Routing weights alone do not establish intervention-relative mediation.

## Repository checks completed

- no duplicate labels;
- no missing internal references;
- no missing bibliography keys;
- no unresolved citations or `natbib` warnings;
- no multiply defined labels or overfull boxes;
- correct semantic statement types under shared numbering;
- no stale pre-release paths or labels;
- no development-only cross-paper dependency in the public snapshot;
- no generated LaTeX products in `paper/`;
- stable compiled PDFs linked directly from the root README;
- deterministic clean-source packaging;
- source-package extraction and independent rebuild;
- PDF structure, text extraction, embedded fonts, and every-page rendering.

## Continuous validation

`.github/workflows/validate-paper.yml` validates the exact repository tree on every pull request and push to `main`. The workflow rebuilds the paper and supplement from the current source under its configured TeX environment, audits LaTeX diagnostics and semantic references, checks PDF structure with `qpdf`, verifies embedded fonts, renders every generated page, rebuilds the clean source package, and uploads the validated artifacts.

The committed files in `releases/v1.0/` are validated as immutable release artifacts. Their identity is checked against `releases/v1.0/SHA256SUMS.txt`, and the committed PDFs are independently checked for structure, text extraction, embedded fonts, and every-page rendering. Exact output equality across rebuilds is not asserted unless the build toolchain itself is pinned sufficiently to support that claim. Exact remote provenance is read from the commit or release tag together with its associated Actions run.
