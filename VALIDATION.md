# Validation record — public v1.6

**Artifact:** *Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map*  
**Repository version:** 1.6  
**Scientific freeze date:** 2026-08-12

## Authoritative public state

The maintained `paper/` manuscript body is byte-identical to the frozen v1.6 scientific source. `releases/v1.6/SOURCE_SHA256SUMS.txt` fixes those public source bytes.

Submission-provenance hashes are retained as identity records without publishing private submission packages:

- frozen 34-page JMLR-submission manuscript PDF: `4fddb69c4ce94d4b45923724fcf0f0b61a01b4c5b76c2e5341c450f13e7e212e`
- validated clean arXiv v3 source ZIP: `76f9eebeda84e4c9e45bce66d4ab6178708ebae27ae2f8a10e35e3590e398b6f`

The public archival paper is arXiv:2601.11618v3. A fresh repository build is validated structurally and uploaded by CI; byte equality across TeX/PDF environments is not asserted.

## Scientific invariants

Validation is constrained by `CLAIMS.md`: the represented receiver process is not contracted when architecture identity is under analysis; `D(Q)=ker Q` is an extensional shadow rather than a complete architecture object; fixed-branch kernel equality classifies only the declared unmarked surjective factorizations; marked equivalence and restricted continuation accessibility are finer questions; composition acts on `Q_{j,theta}A`; the main local/attention witness uses injective prefixes; the lossy broadcast witness is separate; Transformer material is an instance; and no generic architecture-search speedup is claimed.

## Repository checks

CI validates Citation File Format metadata, the v1.6 source surface and SHA-256 manifest, compilation with the official JMLR style retrieved from a pinned upstream commit, absence of undefined citations/references, 34-page PDF structure, extractable text, embedded fonts, every-page rasterization, integrity of the historical v1.0 release manifest, and deterministic public source packaging. Layout warnings and the already-submitted duplicate-label warning are surfaced by the TeX log but are not promoted to false manuscript failures.

Fresh TeX output is validated as a build product. The frozen submission PDF is tracked by its provenance hash; exact byte equality between a fresh build and the frozen submission PDF is not asserted because TeX/PDF metadata can vary across toolchains.
