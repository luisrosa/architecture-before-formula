# Current manuscript source - v1.0

This directory contains the authoritative source for:

**Architecture Before the Formula: Receiver-Wise Factorization and the Reconstruction of Transformer Blocks**

## Conceptual spine

The paper is conditional on a represented update `F : X -> Y`. A marked successor presentation determines receiver branches `B_j`, and an architecture is defined by the marked receiver-wise factorizations

```text
B_j = G_j Q_j.
```

- `Q_j` is the receiver interface.
- `G_j` is the receiver-local continuation.
- Attention is a restricted refinement of `Q_j`.
- The FFN is a marked refinement of `G_j`.
- Stochastic variable-successor laws are retained only as a supplement extension.

## Files

- `main.tex` - main article
- `supplement.tex` - technical supplement
- `preamble.tex` - shared LaTeX configuration
- `references.bib` and `references_additions.bib` - complete bibliography
- `sections/` - main-article sections
- `supplement/` - proofs, variants, and stochastic extensions
- `build.sh` - direct in-directory build helper

From the repository root, prefer:

```bash
bash ./build.sh
```

That command compiles from a temporary copy and writes final PDFs to `.build/output/`, leaving this directory clean.
