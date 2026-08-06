# Architecture Before the Formula

**Receiver-Wise Factorization and the Reconstruction of Transformer Blocks**  
Luis F. Rosario Freytes, University of Michigan, Ann Arbor

**Current release:** v1.0, August 2026. This working preprint has not yet been peer reviewed.

## Read the paper

- [Main paper - PDF](releases/v1.0/Architecture_Before_the_Formula_v1.0.pdf)
- [Technical supplement - PDF](releases/v1.0/Architecture_Before_the_Formula_v1.0_Technical_Supplement.pdf)
- [Current LaTeX source](paper/)
- [Claim ledger](CLAIMS.md)
- [Formal and release audit](docs/formal-audit.md)

## Overview

A represented update does not by itself determine which successor obligations are separately addressed, what information reaches each receiver, or how each receiver constructs its successor value. The paper defines architecture, conditional on a represented update `F : X -> Y`, as a **marked receiver-wise factorization**

```text
B_j = pi_j chi_Y F = G_j Q_j.
```

- `Q_j` is the receiver interface: the information made available to receiver `j`.
- `G_j` is the receiver-local continuation.
- Attention is derived as a restricted construction of `Q_j`.
- The pointwise FFN is derived as a marked refinement of `G_j`.

## Main results

- A complete, typed definition of receiver-factored architectural presentation.
- Full-access collapse, canonical branch quotient, interface re-presentation, and an interface-refinement preorder.
- Exact and approximate barriers induced by receiver-interface and aggregation fibers.
- A separation between source-resolved computation, retained aggregate exposure, and complete receiver state.
- State-indexed additive operator families from operator-valued pair contributions.
- Masked query-key softmax attention from explicit architectural commitments.
- Typed neighboring constructions showing the distinct work performed by those commitments.
- Effective-potential and receiver free-energy representations only in the positive scalar specialization.
- The FFN as a marked hidden-coordinate refinement of receiver-local continuation.
- A canonical PreNorm block as an attention-constructed receiver interface followed by structured local continuation.
- A deterministic extension to state-conditioned successor presentations, with stochastic realizations isolated in the supplement.
- An explicit boundary between exact architectural presentation and stronger implementation-facing claims.

## Build from source

Requirements:

- `latexmk`
- `pdflatex`
- `bibtex` or `bibtex8`
- a standard TeX Live scientific installation

Build both documents without writing generated files into `paper/`:

```bash
bash ./build.sh
```

The PDFs are written to `.build/output/`. GitHub Actions repeats the build from the repository source package and validates references, statement types, PDF structure, embedded fonts, every rendered page, release links, citation metadata, and source-package cleanliness.

## Repository organization

```text
paper/                 Current v1.0 LaTeX source
releases/v1.0/         Stable compiled PDFs and checksums
prior_versions/        Public version-history note
CLAIMS.md               Claim-to-proof ledger
docs/formal-audit.md    Formal and release audit
```

The retained development sequence begins at v0.9.0. Those earlier milestones were private developmental versions and are not distributed in this public source repository.

## Citation

Citation metadata are provided in [CITATION.cff](CITATION.cff). Until a DOI or archival identifier is available, cite:

```bibtex
@article{rosariofreytes2026architecture,
  title   = {Architecture Before the Formula: Receiver-Wise Factorization and the Reconstruction of Transformer Blocks},
  author  = {Rosario Freytes, Luis F.},
  year    = {2026},
  month   = aug,
  note    = {Working preprint, version 1.0}
}
```

## License

The manuscript PDFs, original LaTeX source, bibliography, and repository documentation are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE), unless a file states otherwise.
