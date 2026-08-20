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

## The problem: architecture before architectural identity

Neural architecture is routinely treated as a design variable before the identity criterion for that variable is made explicit. Module labels, computation graphs, represented intermediate states, and realized input-output functions can disagree about whether two descriptions should count as the same architecture.

The paper therefore asks a prior question:

> **What should count as the same neural architecture?**

The central move is to choose the architectural primitive before quotienting away the structure under study.

## The proposed architectural primitive

At a selected receiver cut, the theory keeps the represented process

$$
X \xrightarrow{Q_j} Z_j \xrightarrow{G_j} W_j,
\qquad
B_j = G_jQ_j,
$$

rather than immediately contracting it to the composite branch $B_j$.

$Q_j(x)$ is the intermediate state actually presented for further computation. Its distinction shadow

$$
\mathsf D(Q_j)=\ker Q_j
$$

records only which predecessor states remain distinguishable at the cut. The full represented process retains more: carrier presentation, declared architectural roles, and the continuation that actually receives and uses the retained state.

This separates three questions that are often conflated:

- **Which predecessor distinctions survive?**
- **How are those distinctions represented and organized?**
- **Which of them can the represented continuation actually access?**

The distinction shadow answers the first question only. The theory is built to keep the others visible.

## What follows from this choice of architectural primitive

### 1. An exact information-level equivalence

For two surjective factorizations of the same fixed branch, equality of distinction shadows is exactly the condition for unmarked factorization isomorphism through one unique carrier re-presentation.

So “these interfaces preserve the same predecessor distinctions” is not merely an informal resemblance claim. Under the stated conditions it defines an exact extensional quotient of represented factorizations.

### 2. Preserved information is not the same as represented accessibility

Equal distinction shadows guarantee recoverability up to the unique carrier re-presentation. They do **not** imply that the two represented processes have the same marked organization, nor that the recovering conversion is already available to a restricted continuation.

In short:

$$
\text{information preserved}
\;\neq\;
\text{represented organization}
\;\neq\;
\text{continuation accessibility}.
$$

An invertible conversion can preserve every predecessor distinction while still changing the coordinates that name receivers, sources, tokens, sites, heads, or other architecturally declared roles. Recovery is itself computation unless the comparison has already declared that conversion to be a passive re-presentation.

### 3. Architectural identity can depend on compositional context

A downstream schema does not act on an abstract input in isolation. It acts on the representation produced upstream. For

$$
\Omega \xrightarrow{A} X \xrightarrow{Q_{j,\theta}} Z_{j,\theta},
$$

the relevant effective interface is $Q_{j,\theta}A$, with

$$
\ker(Q_{j,\theta}A)=(A\times A)^{-1}\ker Q_{j,\theta}.
$$

This means that a downstream module label need not define a context-independent architectural degree of freedom. Whether two downstream choices remain distinct can depend on the upstream representation that supplies their inputs.

## The decisive construction: contextual collapse without information loss

The paper makes the compositional claim concrete with exact two-token local and attention schemas.

Two upstream maps are compared:

$$
A_{\mathrm{enc}}(u,v)=(2u+v,0),
\qquad
A_{\mathrm{id}}(u,v)=(u,v).
$$

Both are injective. After $A_{\mathrm{enc}}$, the local and attention schemas have the same effective distinction-class set. After the identity prefix, their effective distinction-class sets differ.

Because **both prefixes are injective**, the collapse after $A_{\mathrm{enc}}$ cannot be attributed to upstream predecessor-information loss.

The conclusion is not that “local and attention are the same architecture” in general. It is sharper and more contextual:

> **At the paper's stated distinction level, a nominal downstream architectural distinction can disappear under one injective upstream representation and reappear under another.**

So a module vocabulary can overcount genuinely independent architectural choices.

## Why this matters

### Architecture search: which nominal choices are genuinely independent?

A search problem over an architecture space already presupposes an individuation rule for that space. If downstream architectural identity depends on upstream representation, a Cartesian search parameterization can contain nominal choices that collapse after composition.

The theory therefore identifies a quotient problem that architecture search has to settle before treating every syntactic module choice as an independent coordinate.

It does **not** prove that computing or exploiting such a quotient is generically easier, faster, or polynomial-time. The contribution is prior: it specifies what a quotient-aware comparison would need to preserve and why that quotient can be context dependent.

### Interpretability: what exactly is the internal object being interpreted?

Interpretability inherits the same individuation problem. Claims about heads, circuits, directions, layers, or other internal objects presuppose a criterion for when two represented computations count as the same object across changes of representation and compositional context.

The theory contributes two distinctions that matter directly to that question:

- **Recoverability is weaker than represented accessibility.** Information can be recoverable from an intermediate state without being available to the restricted continuation that actually follows.
- **Module labels need not define context-independent computational individuals.** The local/attention witness shows that the effective distinction represented by a downstream schema can change with an injective upstream representation.

This is not a complete theory of causal-mechanism identity and does not by itself solve mechanistic interpretability. Rather, it formalizes part of the prior individuation problem: which internal differences correspond to different represented computations in the first place.

## Two different phenomena the theory separates

The injective contextual-collapse result and the lossy prediction barrier are deliberately different results.

### Architectural redundancy without information loss

In the injective local/attention construction, all predecessor distinctions survive upstream, yet the downstream distinction classes can collapse in one representational context.

### Prediction barriers from genuine information loss

A separate broadcast prefix genuinely erases a predecessor distinction needed by the target. In that witness the theory yields exact prediction barriers: $1/2$ for the stated worst-case deterministic problem and $1/4$ for the stated Bayes squared-loss problem.

Keeping these examples separate distinguishes:

- **Contextual architectural redundancy:** two nominal architecture choices are redundant at the stated comparison level in a particular compositional context.
- **Information loss:** the representation has destroyed a predecessor distinction required for the task.

## Formal results

The manuscript proves the following theorem-level results underlying the narrative above:

1. **Exact extensional classification at a fixed branch.** For surjective factorizations of the same branch, equality of distinction shadows is equivalent to unmarked factorization isomorphism through a unique carrier re-presentation.
2. **Marked identity is finer than preserved information.** Equal kernels guarantee recoverability up to re-presentation, but do not determine marked receiver organization or make the recovering conversion available to a restricted continuation.
3. **Composition changes the relevant comparison object.** Effective distinction classes are computed after precomposition through $Q_{j,\theta}A$; family envelopes summarize common retained distinctions but are not complete architecture or capability objects.
4. **Injective contextual-collapse witness.** Local and attention schemas have the same effective distinction-class set after $A_{\mathrm{enc}}(u,v)=(2u+v,0)$ and different sets after the injective identity prefix. The collapse therefore cannot be attributed to upstream information loss.
5. **Separate lossy prediction barrier.** A broadcast prefix supplies exact deterministic and Bayes squared-loss barriers ($1/2$ and $1/4$ in the stated witness) when the needed predecessor distinction is genuinely erased.

## Transformers as an instance of the theory

Transformers make the represented-process analysis concrete because attention exposes a clear receiver/source organization. The paper shows how self-attention, pointwise feed-forward computation, residual composition, and PreNorm blocks instantiate the theory.

They are not the definition of architecture, and the Transformer reconstruction is not presented as a separate novelty claim.

## Scope

The distinction shadow is not a complete architecture identity object. Marked receiver-process identity is still weaker than complete architecture identity, implementation identity, or causal-mechanism identity.

The theory also does not claim that quotient-aware architecture search is automatically computationally easier or faster, and it does not identify recoverable or decodable information with information causally used by a represented continuation.

## Build from source

Requirements are `latexmk`, `pdflatex`, `bibtex` or `bibtex8`, `curl`, and a standard scientific TeX installation.

```bash
bash ./build.sh
```

The generated PDF is written to `.build/output/Architecture_Before_the_Formula_v1.6.pdf`.

The maintained manuscript body is byte-identical to the frozen v1.6 scientific source. The official JMLR style file is retrieved from a pinned upstream commit during the build rather than vendored here. GitHub Actions validates and builds a fresh PDF. The frozen JMLR-submission binary is identified by hash in `releases/v1.6/README.md`; private submission-administration materials are not published in this repository.

## Repository organization

- `paper/` — current v1.6 manuscript source
- `releases/v1.6/` — current provenance record and source hashes
- `releases/v1.0/` — historical public v1.0 release
- `prior_versions/` — version-lineage note
- `CLAIMS.md` — current semantic/claim ledger
- `docs/formal-audit.md` — formal and release audit
- `scripts/` — build/release validation

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
