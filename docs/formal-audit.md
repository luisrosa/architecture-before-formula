# v1.0 formal and release audit

This audit records the mathematical, semantic, and release invariants checked for the v1.0 public source.

## Formal invariants

1. The receiver-factored architectural presentation remains the central typed object:
   `B_j = pi_j chi_Y F = G_j Q_j`.
2. Every load-bearing result is proved in the main article or technical supplement.
3. Bijective recoding of one receiver interface preserves its branch and fibers without introducing a general mechanism-equivalence theory.
4. `P_j`, `Agg_j P_j`, `Q_j`, and `G_j` remain distinct typed objects.
5. Exact and approximate interface barriers remain prior to the attention specialization.
6. Operator-valued pair contributions precede scalar relevance and transport.
7. Attention remains a conditional normal form rather than a universal axiom of receiver-organized computation.
8. Every attention commitment has a typed neighboring witness in the supplement.
9. Effective-potential language remains downstream of positive scalar routing.
10. The actual FFN activation vector is the hidden carrier; the second residual interface is named according to its actual role.
11. The deterministic variable-successor architecture remains in the main article; stochastic realizations remain in the supplement.
12. Routing weights alone do not establish intervention-relative mediation.

## Semantic-reference invariants

The LaTeX configuration uses `aliascnt` so shared numbering does not cause definitions, assumptions, lemmas, propositions, corollaries, examples, or remarks to render as the wrong statement type. CI audits the semantic type recorded in the `.aux` files for each label prefix.

## Source invariants

- The current manuscript source is contained entirely under `paper/`.
- The bibliography is version-local and does not depend on a legacy directory.
- Generated LaTeX products are excluded from the source tree and source package.
- The public source contains no development-only cross-paper dependency.
- Stable compiled PDFs are stored under `releases/v1.0/`.
- The source package is extracted and rebuilt during release validation.

## Release checks

The release pipeline verifies:

- duplicate labels, missing references, and missing bibliography keys;
- unresolved LaTeX or `natbib` warnings;
- semantic `cleveref` types;
- PDF structure, page count, metadata, extractable text, and embedded fonts;
- successful rasterization of every page;
- equality of normalized text between clean-source builds and committed PDFs;
- local README links;
- Citation File Format metadata;
- absence of generated files in the source package.
