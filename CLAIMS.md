# Claim ledger - v1.0

This ledger maps the manuscript's principal claims to their formal status and support in `paper/`.

| Claim | Status | Formal support |
|---|---|---|
| Architecture is a marked receiver-wise factorization of an already represented update. | Definition and organizing thesis | Definition `def:receiver-factored-architecture`; Eq. `eq:receiver-factorization` |
| Receiver labels alone do not impose restricted locality when every branch receives the full represented state. | Proposition | Proposition `prop:full-access-collapse` |
| The canonical answer quotient is the coarsest exact branch-sufficient quotient but does not identify the marked architecture. | Proposition and interpretive consequence | Proposition `prop:canonical-branch-quotient` |
| Bijective recodings of one receiver interface preserve its branch and its fibers. | Proposition and re-presentation convention | Proposition `prop:interface-representation` |
| Receiver interfaces form a refinement preorder, and coarser interfaces cannot recover distinctions removed by finer-to-coarser factorization. | Definition and proposition | Definition `def:interface-refinement`; Proposition `prop:refinement-preorder` |
| Global conjugacy can preserve the total update while destroying coordinate-local receiver interpretation. | Proposition | Proposition `prop:locality-conjugacy` |
| Retained local state, source-resolved contributions, aggregate exposure, complete receiver interface, and local continuation are distinct typed objects. | Definitions and central refinement diagram | Definitions `def:local-exposure-refinement`, `def:source-resolved-refinement`; Fig. `fig:interface-refinement` |
| Aggregation can erase source-resolved distinctions that remain relevant to a target, producing exact and approximate realization barriers. | Example, theorem, and lower bound | Example `ex:aggregation-collision`; Theorems `thm:aggregation-fiber`, `thm:deterministic-lower-bound`; Corollary `cor:exact-recoverability` |
| Unresolved variation at the interface and accessibility limits of a restricted local continuation are distinct error terms. | Exact squared-loss decomposition | Theorem `thm:squared-decomposition` |
| Provenance source types are marked, but actual state, parameter, instance, or schema dependence is derived by admissible counterfactual variation. | Definition and proposition | Definition `def:essential-dependence`; Proposition `prop:provenance-underdetermination` |
| Additive operator-valued pair contributions define a state-indexed operator family. Scalar relevance and transport form an additional marked factorization, not primitive data. | Definition and proposition | Definition `def:additive-routed-realization`; Proposition `prop:routed-operator-field` |
| Masked query-key softmax attention follows from pairwise scalar evidence, positive compositional linking, row anchoring, source-local payloads, additive aggregation, and shared finite separation rank. | Conditional normal-form theorem | Assumptions `ass:pairwise-scalar`–`ass:values-aggregation`; Definition `def:shared-separation-rank`; Proposition `prop:separable-bilinear`; Theorem `thm:attention-normal-form` |
| The attention commitments perform distinct architectural work and can be removed into typed neighboring regimes. | Constructive qualification ledger | Supplement `supp:commitment-witnesses` |
| Query-key coordinates are derived from shared finite separation rank rather than assumed as primitive. | Proposition | Proposition `prop:separable-bilinear` |
| Effective-potential and receiver free-energy representations are exact only in the positive scalar routing specialization. | Definition and theorem | Definition `def:effective-potential`; Theorem `thm:receiver-free-energy` |
| Exact source quotienting preserves the pushed-forward allocation and induces a log-sum-exp effective potential. | Theorem | Theorem `thm:potential-of-mean-force` |
| The FFN hidden-coordinate carrier is justified by the marked intermediate activation vector of the specified two-layer continuation, not by arbitrary algebraic refactorization. | Definition and proposition | Definition `def:local-continuation-refinement`; Proposition `prop:ffn-hidden-carrier` |
| A canonical PreNorm block admits a coarse factorization in which attention constructs the receiver interface and the FFN belongs to local continuation. | Theorem | Theorem `thm:block-receiver-factorization` |
| The familiar two-sublayer routed description is a finer marked presentation, while the actual FFN hidden carrier remains internal to the local branch. | Corollary and notation clarification | Corollary `cor:fine-two-stage-block` |
| Variable-cardinality successor architecture distinguishes selection of a receiver sector from successor content within that sector. | Definition and proposition | Definition `def:configurational-endogenization`; Proposition `prop:finite-slot-encoding`; Section `sec:variable-population` |
| Positive stochastic variable-successor laws admit effective sector potentials and a KL free-energy identity. | Supplementary proposition and theorem | Proposition `prop:supp-effective-sector-potential`; Theorem `thm:supp-joint-successor-free-energy` |
| Routing weights alone do not establish intervention-relative mediation. | Proposition and scope boundary | Proposition `prop:weights-not-mediation`; Section `sec:mechanism-boundary` |
| Implementation warrant, intervention licensing, identity across complete implementations, and tracking require additional evidence not supplied by an exact architectural factorization. | Explicit nonclaim | Section `sec:mechanism-boundary` |
