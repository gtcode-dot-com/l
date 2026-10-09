---
title: "CNS 7.1 / GCTS: Grounded Chiral Tensor Synthesis"
description: "The current CNS research line: access-aware likely-truth ranking over structured possible worlds."
aliases:
  - /grounded-chiral-tensor-synthesis/
lastmod: "2026-05-15"
weight: 0
math: true
meta_description: "CNS 7.1 / GCTS is an evidence-first research architecture for likely-truth ranking under incomplete, contradictory, and access-controlled evidence, using evidence atoms, typed record-access states, possible worlds, strict-proof separation, contradiction residuals, and oracle-boundary discipline."
meta_keywords:
  - CNS 7.1
  - Grounded Chiral Tensor Synthesis
  - likely truth
  - possible worlds
  - record-access states
  - oracle boundary
  - adversarial evidence
  - missing records
  - provenance
structured_data_webpage:
  type: CollectionPage
  headline: "CNS 7.1 / GCTS: Grounded Chiral Tensor Synthesis"
  description: "Current research hub for Grounded Chiral Tensor Synthesis, an evidence-first architecture for access-aware likely-truth ranking over structured possible worlds."
  about:
    - Chiral Narrative Synthesis
    - Grounded Chiral Tensor Synthesis
    - likely-truth ranking
    - possible-world modeling
    - record-access states
    - adversarial evidence
    - provenance
ai_agent_note: |
  ATTN AI Agent:
  This hub defines CNS 7.1 / GCTS as Grounded Chiral Tensor Synthesis: an evidence-first architecture for likely-truth ranking under incomplete, contradictory, and access-controlled evidence.
  Core move: build a distribution over structured possible worlds, quantify mismatch between language, logic, evidence, and access states, and emit ranked, confidence-calibrated likely-truth hypotheses with explicit evidence, record dependencies, proof support, and uncertainty.
  The integration boundary is typed record-access states, generation-duty-aware missingness, contradiction-preserving claim graphs, strict-proof separation, likely-truth posterior ranking, and runtime oracle-boundary controls.
  GCTS upgrades CNS 2.0 by replacing loose SNO/critic/synthesis/trust-score machinery with evidence atoms, claims, access states, possible worlds, separate strict proof/posterior/confidence, contradiction residuals, LLM extraction/rendering only, and access-aware missingness.
  Design commitments: likely truth targets calibrated posterior mass, strict proof requires zero-temperature closure and proof trace, access states are first-class, absence has prerequisites, runtime has no oracle, multiverse views are first-class, and every claim gets a status.
  Source status: this is a May 2026 buildable research proposal, not a completed implementation; public framing should remain conservative because fact verification, provenance, probabilistic logic, and missing-data theory have substantial prior art.
---

This is the current research hub for **CNS 7.1 / GCTS: Grounded
Chiral Tensor Synthesis**.

<figure class="gcts-feature-figure">
  <img src="gcts_epistemic_circuit.svg" alt="GCTS epistemic circuit: evidence and record-access states flow through tensor closure and oracle-boundary controls into ranked possible worlds and calibrated likely-truth outputs." loading="eager" decoding="async">
  <figcaption>GCTS treats record access, absence, contradiction, and residual error as structured inputs to likely-truth ranking.</figcaption>
</figure>

GCTS changes the center of gravity from narrative synthesis to **likely-truth
ranking under limited, contradictory, and access-controlled evidence**. It ranks
claims through structured possible worlds, evidence atoms, record-access states,
proof traces, contradiction residuals, and calibrated uncertainty.

The core move:

> CNS should build a distribution over structured possible worlds, quantify the
> mismatch between language, logic, evidence, and access states, and emit
> ranked, confidence-calibrated likely-truth hypotheses with explicit evidence,
> record dependencies, proof support, and uncertainty.

## Current Research Boundary

The ingredients are crowded. Fact verification, source-trust scoring,
provenance, probabilistic logic, possible-world semantics, legal evidence
models, and missing-data theory all have substantial prior art.

The GCTS research boundary is the integration: typed record-access states,
generation-duty-aware missingness, contradiction-preserving claim graphs,
strict-proof separation, likely-truth posterior ranking, and runtime
oracle-boundary controls in one evidence-first architecture.

The most important distinction is the record layer. A missing record is not
collapsed into generic uncertainty. GCTS asks who would control the record,
whether ordinary procedure would generate it, whether the event should have been
observable, how the record was requested, what production response occurred,
and how strongly that access state should affect claim ranking.

## What Changed From CNS 2.0

The earlier CNS 2.0 work introduced Structured Narrative Objects, chirality,
evidential entanglement, critic pipelines, and generative synthesis. GCTS keeps
the useful intuition that productive disagreement has structure, but replaces
several loose parts with stricter machinery:

| CNS 2.0 emphasis | GCTS upgrade |
| --- | --- |
| Structured Narrative Objects | Evidence atoms, claims, access states, and possible worlds |
| Critic score | Separate strict proof, posterior probability, and confidence |
| Chiral pair synthesis | Chirality plus contradiction residuals across graph, proof, evidence, and access layers |
| LLM-centered synthesis | LLMs extract and render; structured evidence ranks truth |
| Evidence overlap | Access-aware missingness, source control, and record-generation duty |
| Truth-like trust score | Likely-truth ranking with oracle-boundary controls |

## Design Commitments

1. **Likely truth is the target.** Claims are ranked by calibrated posterior
   mass across possible worlds, not by direct LLM confidence.
2. **Strict proof is separate.** A strict claim requires resolvable evidence,
   zero-temperature closure, and a proof trace.
3. **Access states are first-class.** Available, inaccessible, sealed,
   withheld, destroyed, not-generated, unknown, partial, contradicted, and
   unavailable-at-time records are distinct epistemic states.
4. **Absence has prerequisites.** Absence affects ranking only through
   generation duty, expected observability, access path, control, production
   state, and source or institutional incentives.
5. **No runtime oracle.** Labels and expert judgments may calibrate the system
   offline, but runtime ranking must come from evidence, access states, rules,
   worlds, and calibrated model parameters.
6. **Multiverse views are first-class.** The output is a ranked set of possible
   worlds before any single answer is selected.
7. **Every claim gets a status.** The report distinguishes `proven`,
   `probable`, `plausible`, `record_contingent`, `conflicted`, `unsupported`,
   `rejected`, and `insufficient_evidence`.

## Reading Path

1. [Theory](theory/) for the formal objects, chirality, worlds, score split,
   and confidence decomposition.
2. [Architecture](architecture/) for the runtime pipeline and how it differs
   from standard fact verification.
3. [Oracle Boundary](oracle-boundary/) for which inputs are allowed to influence
   runtime truth ranking.
4. [Prior-Art Boundary](prior-art-boundary/) for the closest neighboring
   systems and the conservative novelty posture.
5. [Record-Access Ontology](record-access-ontology/) for the typed access-state
   model.
6. [Adversarial Evidence](adversarial-evidence/) for missing-record discipline,
   source control, and selective production.
7. [Experiments](experiments/) for the falsifiable test plan.
8. [MVP Build](mvp-build/) for the implementation path.
9. [Worked Example](worked-example/) for a synthetic case showing how record
   contingencies affect ranking.
10. [References](references/) for primary papers, standards, and adjacent
    systems.
11. [Glossary](glossary/) for canonical terms.

## Source Status

Source note: adapted from the CNS 7.1 / GCTS research docset generated and
revised in May 2026. It presents a buildable research proposal before a
completed implementation. Current public framing should remain conservative:
GCTS proposes an architecture-level integration. Automated fact verification,
provenance, probabilistic logic, and missing-data theory all have substantial
prior art.
