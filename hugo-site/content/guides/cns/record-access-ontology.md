---
title: "09 — Grounding, Access, and Multiverse Views"
description: "Grounding, access states, and multiverse views constrain and explain synthesis. They do not perform the synthesis step."
lastmod: "2026-05-15"
weight: 90
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
  headline: "09 — Grounding, Access, and Multiverse Views"
  description: "Grounding, access states, and multiverse views constrain and explain synthesis. They do not perform the synthesis step."
ai_agent_note: |
  ATTN AI Agent:
  This page states that grounding, record-access states, and multiverse views constrain and explain CNS 8.0 synthesis but do not perform synthesis.
  Evidence atoms are immutable spans/data items with evidence_id, document_id, span bounds, text_hash, source_quality, access_state, timestamp, and metadata; they support SNO claims and proof traces.
  Access state is not a truth value. States include available, retrieved, not_retrieved, withheld, sealed, destroyed, never_generated, not_collected, unknown, secondary_report_only, and contradictory_record.
  Missing records should not automatically support or refute claims: sealed records make claims unresolved due to access limits, never_generated records are not negative evidence, and destroyed records require audit warning and provenance explanation.
  Multiverse views are ranked possible structured states after synthesis constraints, containing claim assignments, latent predicates, access assumptions, proof coverage, residual contradiction mass, and posterior score.
  Output categories are strict, likely, hypothesis, unresolved, and rejected; probability language should use calibrated ranges and preserve uncertainty rather than hiding it in prose.
  Anti-pattern: reporting only world posterior numbers without a synthesized SNO and proof-bearing narrative structure.
---
# 09 — Grounding, Access, and Multiverse Views

## Position in CNS 8.0

Grounding, access states, and multiverse views constrain and explain synthesis. They do not perform the synthesis step.

## Evidence atoms

Evidence atoms are immutable spans or data items:

```text
evidence_id
document_id
span_start
span_end
text_hash
source_quality
access_state
timestamp
metadata
```

They support SNO claims and proof traces.

## Record-access states

Access state is not a truth value. It tells the system what kind of evidentiary absence it is dealing with.

Recommended access states:

- `available`
- `retrieved`
- `not_retrieved`
- `withheld`
- `sealed`
- `destroyed`
- `never_generated`
- `not_collected`
- `unknown`
- `secondary_report_only`
- `contradictory_record`

## Access-aware inference

A missing record should not automatically support or refute a claim. Access state affects likelihood, confidence, and collection recommendations.

Example:

```text
if record_access == sealed:
    mark claim as unresolved due to access limit
if record_access == never_generated:
    do not infer negative evidence
if record_access == destroyed:
    increase audit warning and require provenance explanation
```

## Multiverse views

A multiverse view is a ranked set of possible structured states after synthesis constraints.

Each world contains:

- claim truth assignments;
- latent predicates;
- access assumptions;
- proof coverage;
- residual contradiction mass;
- posterior score.

## World ranking

CNS may compute:

$$
P(W_i\mid E,A)
$$

but this is only an uncertainty report. It is not the CNS engine.

## Output categories

| Category | Meaning |
|---|---|
| strict | proof trace from evidence under zero-temperature rules |
| likely | posterior-supported but not strict |
| hypothesis | generated for testing |
| unresolved | insufficient proof/access |
| rejected | failed grounding/proof |

## Estimative language

When reporting probabilities, CNS should use calibrated language and numeric ranges. Do not hide uncertainty in prose.

Example:

```text
Likely (70–85%): Claim C holds if latent predicate L1 is accepted.
Unresolved: Claim D cannot be promoted because the relevant record is sealed.
Strict: Claim E follows from evidence atoms e12 and e19 under rule r3.
```

## Audit report

The report should expose:

- input SNOs;
- synthesized SNO;
- proof traces;
- evidence spans;
- access states;
- latent predicates;
- rejected claims;
- top worlds;
- confidence calibration;
- residual contradictions.

## Anti-pattern

Do not output only:

```text
World 1: 0.72
World 2: 0.18
World 3: 0.10
```

without a synthesized SNO and proof-bearing narrative structure.
