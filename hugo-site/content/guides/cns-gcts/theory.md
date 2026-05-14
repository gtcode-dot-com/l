---
title: "GCTS Theory"
description: "The formal object model for Grounded Chiral Tensor Synthesis: evidence, access states, claims, worlds, chirality, and confidence."
lastmod: "2026-05-13"
weight: 1
math: true
meta_description: "Formal theory for CNS 7.1 / GCTS, including evidence atoms, record-access states, institutional incentives, possible worlds, chirality metrics, and likely-truth confidence."
---

GCTS separates three questions that are often collapsed:

1. What is strictly proven?
2. What is likely true across admissible worlds?
3. What uncertainty remains because of evidence quality, missing records,
   access conditions, source incentives, or contradiction structure?

## Evidence Atoms

An evidence atom is:

$$
e_i = (u_i, s_i, t_i, q_i, a_i, m_i)
$$

where `u_i` is a stable source identifier, `s_i` is a span, observation,
record, or structured datum, `t_i` is temporal scope, `q_i` is source/evidence
quality, `a_i` is access path, and `m_i` is metadata.

The available evidence set is:

$$
E = \{e_1,\dots,e_n\}
$$

## Record-Access States

GCTS models missing evidence as structured information. A record-access state is:

$$
r_k = (id_k, type_k, owner_k, duty_k, expected_k, access_k, production_k, q_k)
$$

The `access_k` value is one of `available`, `inaccessible`, `sealed`,
`withheld`, `destroyed`, `not_generated`, or `unknown`.

This lets the system distinguish:

- absence of evidence;
- evidence of absence;
- inaccessible evidence;
- withheld evidence;
- not-generated evidence.

Absence can penalize a claim only when record-generation duty, expected
observability, collection path, and access path justify that penalty.

## Claims And Statuses

A claim is:

$$
c_j = (p_j, a_j, \rho_j, \kappa_j, \sigma_j)
$$

where `p_j` is a proposition, `a_j` is an argument frame, `rho_j` is a reference
set, `kappa_j` is a record-contingency set, and `sigma_j` is one of `proven`,
`probable`, `plausible`, `record_contingent`, `conflicted`, `unsupported`, or
`rejected`.

Relations among claims are typed through a relation set `R`, including
`supports`, `refutes`, `implies`, `specializes`, `generalizes`, `qualifies`,
`depends_on`, and `independent`.

## Language, Logic, And Access

Let `L` be the language/concept manifold, `T` the logic/proof space, and `A`
the access/missingness space. A grounding map extracts proof and access
structure:

$$
G: L \rightarrow \mathcal{T} \times \mathcal{A}
$$

A rendering map turns structured worlds back into language:

$$
S: \mathcal{T} \times \mathcal{A} \rightarrow L
$$

The orthesis is the stable structured state:

$$
(\mathcal{T}^{\ast},\mathcal{A}^{\ast}) =
G(S(\mathcal{T}^{\ast},\mathcal{A}^{\ast}))
$$

The orthesis is the structured state that survives language rendering without
losing proof support, likely-truth support, access-state coherence, or
uncertainty.

## Chirality

Round-trip chirality measures whether a structured state survives rendering and
re-grounding:

$$
\delta(X) = d_{\mathcal{T},\mathcal{A}}(X, G(S(X)))
$$

A fluent narrative can still have high chirality if its logical or access
structure falls apart under grounding.

GCTS also measures:

- graph chirality, based on edge-incidence differences between claim graphs;
- residual tensor chirality, based on unresolved support/refutation mass;
- access chirality, when structured modeling breaks narrative access
  assumptions.

## Possible Worlds

A world view is:

$$
W_k = (F_k, R_k, Z_k, \Pi_k, A_k, M_k, H_k)
$$

where `F_k` contains accepted facts and likely-truth claims, `R_k` is a rule
subset, `Z_k` are latent context predicates, `Pi_k` are proof traces, `A_k` are
assumptions, `M_k` is a record-access model, and `H_k` is an
institutional-incentive hypothesis set.

Worlds are scored by energy:

$$
Q(W_k \mid E,A,I) =
\frac{\exp(-\mathcal{E}(W_k;E,A,I))}
{\sum_\ell \exp(-\mathcal{E}(W_\ell;E,A,I))}
$$

Lower energy worlds are better supported. Contradictions, unsupported
complexity, access mismatch, and weak grounding raise energy; evidence support
lowers it.

## Likely-Truth Ranking

For a claim `c`:

$$
P(c \mid E,A,I)=
\sum_k Q(W_k\mid E,A,I)\,\mathbf{1}[c \in Cl(W_k)]
$$

The score reports posterior mass across structured worlds rather than direct
LLM confidence.

Strict proof support is emitted separately:

$$
P_0(c \mid E)=
\sum_k Q(W_k\mid E,A,I)\,\mathbf{1}[c \in Cl_0(W_k)]
$$

The system must emit `P(c | E,A,I)`, `P_0(c | E)`, and `Conf(c)` separately.
A claim can be likely but low-confidence, strictly proven but narrow, or
plausible but record-contingent.
