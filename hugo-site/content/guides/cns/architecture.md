---
title: "06 — Dialectical Agent Architecture"
description: "chunk documents into stable spans; hash spans; attach source metadata; record access state; expose retrieval API."
lastmod: "2026-05-15"
weight: 60
math: true
meta_keywords:
  - CNS 8.0
  - Chiral Narrative Synthesis
  - Grounded Dialectical Orthesis
  - Structured Narrative Objects
  - orthesis
  - tensor logic
  - predicate invention
  - chiral conflict
structured_data_webpage:
  type: Article
  headline: "06 — Dialectical Agent Architecture"
  description: "chunk documents into stable spans; hash spans; attach source metadata; record access state; expose retrieval API."
ai_agent_note: |
  ATTN AI Agent:
  This page defines CNS 8.0 as named roles, not a single chatbot: Corpus Ingestor, Proposer, Antagonist, critic ensemble, Pair Selector, Tensor Prover, Residual Analyzer, Predicate Inventor, Synthesizer, Orthesist, and Auditor.
  Corpus Ingestor only chunks, hashes, attaches metadata/access states, and exposes retrieval; it cannot synthesize, infer truth, or repair missing evidence.
  Proposer may use LLMs for claim/relation extraction, paraphrase normalization, and hypothesis drafting, but cannot promote unsupported claims, decide final truth, or silently invent access state.
  Antagonist checks citation validity, unsupported claims, contradiction, chiral tension, topology cycles, access gaps, latent context candidates, and language-logic round-trip distortion.
  Pair Selector favors high evidence overlap, opposing interpretations, source quality, bounded chirality, and resolvable/explainable access gaps; it rejects topic mismatch, no shared evidence, low-quality conflict, or extraction-error conflict.
  Tensor Prover creates zero-temperature proof closure; Residual Analyzer builds unresolved support/refute tensors; Predicate Inventor proposes latent context predicates; Synthesizer creates the new SNO; Orthesist re-renders/re-grounds for stability; Auditor reports strict/likely/unresolved/rejected claims, proof, evidence, access, worlds, residuals, and confidence.
  Orchestration rule: LLMs may propose and render; proof gates promote; critics block; predicate invention explains; orthesis stabilizes; auditor reports.
---
# 06 — Dialectical Agent Architecture

## Agent set

CNS 8.0 uses named roles because the roles carry the theory.

## 1. Corpus Ingestor

Turns sources into evidence atoms.

Responsibilities:

- chunk documents into stable spans;
- hash spans;
- attach source metadata;
- record access state;
- expose retrieval API.

Cannot:

- synthesize narratives;
- infer truth;
- repair missing evidence.

## 2. Proposer

Builds candidate SNOs.

Inputs:

- evidence packets;
- task frame;
- extraction schema.

Outputs:

- candidate SNOs with claims, relations, evidence refs, and initial provenance.

Allowed LLM use:

- claim extraction;
- relation extraction;
- paraphrase normalization;
- hypothesis drafting.

Forbidden:

- promoting claims without evidence;
- deciding final truth;
- silently inventing record access.

## 3. Antagonist

Finds reasons not to accept a candidate SNO.

Checks:

- citation validity;
- unsupported claims;
- contradictory evidence;
- chiral tension;
- topology cycles;
- access gaps;
- latent context candidates;
- language–logic round-trip distortion.

Output:

- Antagonist report;
- high-value synthesis pair candidates;
- failure modes.

## 4. Critic ensemble

Critics are specialized:

| Critic | Function |
|---|---|
| Grounding Critic | citation validity, entailment, evidence span checks |
| Logic Critic | graph consistency, proof closure, rule validity |
| Topology Critic | beta-1, persistence, circular support |
| Chirality Critic | graph/evidence/language-logic chirality |
| Novelty-Parsimony Critic | useful synthesis vs bloated predicates |
| Bias/Frame Critic | asymmetric source framing, protected attributes |
| Access Critic | missingness and record-access state discipline |
| Calibration Critic | confidence and posterior calibration |

## 5. Pair Selector

Ranks candidate SNO pairs by Productive Conflict Score.

It should favor:

- high evidence overlap;
- opposing interpretations;
- sufficient source quality;
- nontrivial but bounded chirality;
- resolvable or explainable access gaps.

It should reject:

- topic mismatch;
- conflict without shared evidence;
- low-source-quality conflict;
- conflict caused only by extraction errors.

## 6. Tensor Prover

Computes zero-temperature proof closure.

Outputs:

- strict derived atoms;
- proof traces;
- unsupported atom list;
- proof gaps.

## 7. Residual Analyzer

Constructs residual contradiction tensor after proof closure.

Outputs:

- unresolved support/refute mass;
- candidate tensor slices for factorization;
- contradiction heatmap.

## 8. Predicate Inventor

Proposes latent context predicates from residuals.

Candidate predicates may include:

- time period;
- subgroup;
- dose/threshold;
- jurisdiction;
- source frame;
- definition variant;
- measurement method;
- causal mechanism;
- access condition.

## 9. Synthesizer

Creates the new SNO.

The Synthesizer receives:

- input SNOs;
- Antagonist report;
- strict proof closure;
- residual tensor summary;
- accepted latent predicates;
- access-state constraints;
- possible-world summaries.

It emits:

- synthesized SNO;
- preserved contradictions;
- narrowed claims;
- latent predicates;
- proof/audit references.

## 10. Orthesist

Runs the stability loop.

Steps:

1. render synthesized logic state to language;
2. re-ground language to logic;
3. compute round-trip residual;
4. re-run critics;
5. accept as orthesis candidate or return to Synthesizer.

## 11. Auditor

Produces final report:

- strict claims;
- likely claims;
- unresolved claims;
- rejected claims;
- proof traces;
- evidence spans;
- access states;
- possible worlds;
- residual contradictions;
- confidence language.

## Orchestration principles

- LLMs may propose and render.
- Proof gates promote.
- Critics block.
- Predicate invention explains.
- Orthesis stabilizes.
- Auditor reports.
