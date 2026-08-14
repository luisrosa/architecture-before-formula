# Architecture Before the Formula

**Individuating Neural Architecture Beyond the Composite Map**  
Luis F. Rosario Freytes, University of Michigan, Ann Arbor

**Current public release:** v1.6, August 2026.  
**arXiv:** [2601.11618v3](https://arxiv.org/abs/2601.11618)  
**Submission status:** submitted to the *Journal of Machine Learning Research* (JMLR).  
**Peer-review status:** not yet peer reviewed.

## Read the paper

- [Current archival manuscript — arXiv](https://arxiv.org/abs/2601.11618)
- [Current LaTeX source](paper/)
- [v1.6 provenance record](releases/v1.6/)
- [Claim ledger](CLAIMS.md)
- [Formal/release audit](docs/formal-audit.md)

The earlier [v1.0 public release](releases/v1.0/) is retained as an immutable historical snapshot of the same research lineage. The current manuscript is a substantial reconstruction: architecture individuation and composition are now the primary problem; the earlier incorrect non-completability theorem and dependent claims are absent; and the decisive architecture-space witness uses injective prefixes.

## Question

Neural architectures are routinely compared, searched, compressed, or declared equivalent using module labels, computation graphs, or realized input-output functions. Those descriptions answer different identity questions. The paper asks a prior question:

> **What should count as the same neural architecture?**

At a selected receiver cut, the analysis keeps the represented process

```text
X --Q_j--> Z_j --G_j--> W_j
```

with `B_j = G_j Q_j`, rather than immediately contracting it to the composite branch `B_j`.

`Q_j(x)` is the intermediate state actually presented for further computation. `D(Q_j) = ker Q_j` is the extensional shadow recording which predecessor distinctions survive the cut. A represented receiver process keeps more structure than this shadow: carrier presentation, declared marks, and the continuations that can actually access the retained state matter. Under an upstream map `A`, the effective interface is `Q_{j,theta} A`; downstream architectural distinctions can therefore depend on upstream representation even when the prefix is injective.

## Main results

1. **Exact extensional classification at a fixed branch.** For surjective factorizations of the same branch, equality of distinction shadows is equivalent to unmarked factorization isomorphism through a unique carrier re-presentation.
2. **Marked identity is finer than preserved information.** Equal kernels guarantee recoverability up to re-presentation, but do not determine marked receiver organization or make the recovering conversion available to a restricted continuation.
3. **Composition changes the relevant architecture object.** Effective distinction classes are computed after precomposition through `Q_{j,theta} A`; family envelopes summarize common retained distinctions but are not complete architecture or capability objects.
4. **Injective contextual-collapse witness.** In the exact two-token construction, both `A_enc(u,v)=(2u+v,0)` and the identity prefix are injective. Local and attention schemas have the same effective distinction-class set after the former and different sets after the latter. The collapse therefore cannot be attributed to upstream information loss.
5. **Separate lossy prediction barrier.** A broadcast prefix supplies exact deterministic and Bayes squared-loss barriers (`1/2` and `1/4` in the stated witness) when the needed predecessor distinction is genuinely erased.
6. **Transformers as a worked realization.** Self-attention, pointwise feed-forward structure, residual composition, and PreNorm blocks instantiate the represented-process analysis; they are not the definition of architecture and are not presented as a separate novelty claim.

## Scope

The distinction shadow is not a complete architecture identity object. Marked receiver-process identity is still weaker than complete architecture identity, implementation identity, or causal-mechanism identity. The paper also does not claim that quotient-aware architecture search is automatically computationally easier or faster; it identifies what a comparison/search procedure would need to quotient only under the declared context and identity criterion.

## Build from source

Requirements are `latexmk`, `pdflatex`, `bibtex` or `bibtex8`, `curl`, and a standard scientific TeX installation.

```bash
bash ./build.sh
```

The generated PDF is written to `.build/output/Architecture_Before_the_Formula_v1.6.pdf`.

The maintained manuscript body is byte-identical to the frozen v1.6 scientific source. The official JMLR style file is retrieved from a pinned upstream commit during the build rather than vendored here. GitHub Actions validates and builds a fresh PDF. The frozen JMLR-submission binary is identified by hash in `releases/v1.6/README.md`; private submission-administration materials are not published in this repository.

## Repository organization

```text
paper/                 Current v1.6 manuscript source
releases/v1.6/         Current provenance record + source hashes
releases/v1.0/         Historical public v1.0 release
prior_versions/        Version-lineage note
CLAIMS.md               Current semantic/claim ledger
docs/formal-audit.md    Formal and release audit
scripts/                Build/release validation
```

## Citation

The archival identifier is [arXiv:2601.11618](https://arxiv.org/abs/2601.11618), DOI [10.48550/arXiv.2601.11618](https://doi.org/10.48550/arXiv.2601.11618). Citation metadata are also provided in [CITATION.cff](CITATION.cff).

```bibtex
@article{rosariofreytes2026architecture,
  title   = {Architecture Before the Formula: Individuating Neural Architecture Beyond the Composite Map},
  author  = {Rosario Freytes, Luis F.},
  year    = {2026},
  eprint  = {2601.11618},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi     = {10.48550/arXiv.2601.11618},
  note    = {Version 3; submitted to JMLR}
}
```

## License

The author's manuscript source and repository documentation are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE). Third-party build dependencies are identified in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
