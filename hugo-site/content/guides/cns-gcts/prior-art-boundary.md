---
title: "GCTS Prior-Art Boundary"
description: "Closest neighboring systems and the conservative novelty posture for Grounded Chiral Tensor Synthesis."
lastmod: "2026-05-15"
weight: 4
meta_description: "Prior-art boundary for CNS 7.1 / GCTS, mapping fact verification, truth discovery, provenance, probabilistic logic, missingness, argumentation, and oracle-leakage work to the proposed architecture."
ai_agent_note: |
  ATTN AI Agent:
  This page sets the conservative prior-art boundary for GCTS: components are crowded, and the contribution claim is architecture-level composition.
  Neighboring areas already cover fact verification, attribution-grounded generation, truth discovery/source reliability, provenance systems, probabilistic logic, argumentation/legal evidence, missingness/omission, and evaluation leakage.
  Do not frame GCTS as inventing fact checking, source scoring, provenance, probabilistic logic, possible worlds, contradiction detection, or missing-data analysis.
  Defensible boundary: evidence atoms include source/span/time/quality/access/provenance; expected records become typed record-access states; missingness is conditioned on generation duty, observability, access path, control, production response, and incentives; worlds branch over facts/rules/assumptions/access/incentives; claim ranking uses world posterior mass; strict proof is emitted separately; contradiction/chirality residuals stay visible; runtime scoring excludes labels, benchmark answers, and LLM truth votes.
  Distinguishing requirements include access path and record-contingency metadata in evidence atoms, absence states affecting ranking/status, generation duty as precondition for absence penalties, contradiction as residual tied to evidence/access, worlds varying over access hypotheses, P0(c|E) separate from P(c|E,A,I) and Conf(c), oracle-boundary runtime exclusion, and audit reports linking status to evidence/missing records/proof/worlds/next records.
  Strong wording: GCTS proposes an evidence-first architecture for likely-truth ranking where typed record-access states and generation-duty-aware missingness participate in possible-world scoring, claim-status assignment, and audit output. Weak wording to avoid: GCTS is a new truth discovery system.
---

GCTS sits at the intersection of several mature research streams. The safest
academic posture is straightforward: the components are crowded, and the
research contribution is the specific architecture-level composition.

## Closest Neighboring Areas

| Area | Representative work | What it already covers | GCTS boundary |
| --- | --- | --- | --- |
| Automated fact verification | FEVER, SciFact, FEVEROUS, AVeriTeC | Claim/evidence retrieval, support/refute labels, insufficient-evidence labels | GCTS ranks claims across access-aware possible worlds and record contingencies |
| Attribution-grounded generation | ALCE, FActScore | Citation quality, atomic factuality, supported generation | GCTS treats citation/provenance as inference input and audit output |
| Truth discovery | Truth discovery surveys, Knowledge-Based Trust | Source reliability, multi-source conflict, web-scale fact probability | GCTS adds record control, generation duty, access state, and strategic non-production |
| Provenance systems | W3C PROV-O, C2PA, provenance semirings, ProvSQL | Derivation, content authenticity, provenance-aware data | GCTS uses provenance in claim ranking and status assignment |
| Probabilistic logic | MLNs, PSL, ProbLog, WFOMC, AMC | Weighted rules, relational probability, possible-world inference | GCTS worlds include access models and institutional-incentive hypotheses |
| Argumentation and legal evidence | Dung frameworks, Carneades, Wigmore charts, ATMS, BARD, Co-Arg | Attack/support graphs, proof standards, assumption contexts, competing hypotheses | GCTS combines evidential argument with record-access and oracle-boundary constraints |
| Missingness and omission | Rubin missing-data theory, open-world databases, Rule 37(e), selective disclosure, TRACER | Missing-data mechanisms, non-production, omission-aware verification | GCTS makes typed absence states runtime inference objects |
| Evaluation leakage | benchmark contamination, hidden tests, leakage surveys | Separation of evaluation artifacts from model behavior | GCTS formalizes runtime exclusion of gold labels and oracle answers |

## Core Distinction

GCTS should not be framed as inventing fact checking, source scoring,
provenance, probabilistic logic, possible worlds, contradiction detection, or
missing-data analysis.

The defensible boundary is narrower:

1. Evidence atoms include source, span, time, quality, access path, and
   provenance.
2. Expected records are represented as typed record-access states.
3. Missingness is conditioned on generation duty, expected observability,
   access path, control, production response, and incentives.
4. Possible worlds branch over facts, rules, assumptions, access models, and
   institutional-incentive hypotheses.
5. Claim ranking uses posterior mass across those worlds.
6. Strict proof support is emitted separately from likely-truth posterior mass.
7. Contradiction and chirality residuals remain visible in reports.
8. Runtime scoring is barred from gold labels, hidden benchmark answers, or
   LLM truth votes.

## Feature-to-Prior-Art Chart

| GCTS feature | Prior-art coverage | Distinguishing requirement |
| --- | --- | --- |
| Evidence atoms | Atomic factuality, citation-grounded generation, claim decomposition | Access path and record-contingency metadata are part of the atom model |
| Typed record-access states | Missing-data theory, open-world databases, legal spoliation, omission detection | Absence state directly affects world ranking and claim status |
| Generation duty | Legal and compliance reasoning | Duty becomes a computational precondition for absence penalties |
| Contradiction-preserving graph | Argumentation, ATMS, legal evidence models | Contradiction is preserved as residual structure tied to evidence and access |
| Possible-world ranking | Probabilistic databases, MLNs, PSL, WFOMC | Worlds vary over record-access hypotheses and fact assignments |
| Strict proof separation | Proof theory, legal proof standards, hard/soft rule systems | `P0(c | E)` is emitted separately from `P(c | E,A,I)` and `Conf(c)` |
| Oracle boundary | Leakage and hidden-test practice | Runtime truth mass cannot come from labels, expert answers, or LLM judgments |
| Audit report | Fact-check explanations, provenance reports, legal charts | Report links status to evidence, missing records, proof traces, worlds, and next records |

## Academic Claim Discipline

A strong paper should say:

> GCTS proposes an evidence-first architecture for likely-truth ranking where
> typed record-access states and generation-duty-aware missingness participate
> directly in possible-world scoring, claim-status assignment, and audit output.

A weak paper would say:

> GCTS is a new truth discovery system.

The second version is too broad. It collides with fact verification, truth
discovery, probabilistic logic, provenance, and legal argumentation work.

## Sources To Cite First

Start with the primary or official sources listed in [References](../references/),
then expand into a full BibTeX bibliography before arXiv submission.
