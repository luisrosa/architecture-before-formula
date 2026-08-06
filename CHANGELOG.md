# Changelog

## v1.0 - 2026-08-06

First maintained public release of the receiver-factorization formulation.

- Defines architecture as a marked receiver-wise factorization of an already represented update.
- Separates receiver interface, source-resolved computation, retained aggregation, and receiver-local continuation.
- Derives masked query-key softmax attention under an explicit package of architectural commitments.
- Exhibits typed neighboring constructions showing the distinct work performed by those commitments.
- Reconstructs the FFN as a marked refinement of receiver-local continuation.
- Reconstructs the canonical PreNorm Transformer block at coarse and fine architectural grains.
- Includes a deterministic variable-successor extension and a separate stochastic supplement.
- States the additional evidence obligations required for stronger implementation-facing claims.
- Includes stable compiled PDFs, a clean source package, semantic theorem-reference audits, and reproducible release checks.

## Private development milestones

The retained development sequence begins at v0.9.0:

- v0.10.0 - receiver-factorization reorganization
- v0.9.1 - effective-potential and variable-successor extension
- v0.9.0 - receiver-interface and state-constructed-routing formulation

These developmental versions are not distributed in this public source repository.
