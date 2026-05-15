---
title: "JSON Schemas"
description: "Source JSON schemas for SNO-8, evidence atoms, proof traces, and orthesis reports."
lastmod: "2026-05-15"
weight: 360
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
  headline: "JSON Schemas"
  description: "Source JSON schemas for SNO-8, evidence atoms, proof traces, and orthesis reports."
ai_agent_note: |
  ATTN AI Agent:
  This page provides source JSON schemas for CNS 8.0 SNO-8 objects, EvidenceAtom objects, ProofTrace objects, and OrthesisReport objects.
  SNO-8 requires sno_id, version=8.0, hypothesis, claims, relations, evidence, metrics, and lineage; optional arrays include record_access, proof_traces, residuals, latent_predicates, and world_support.
  SNO claim objects require claim_id, text, status, and evidence_refs; status enum is strict, likely, hypothesis, unresolved, rejected; confidence must be between 0 and 1.
  SNO relation type enum is supports, refutes, implies, conditions, narrows, explains, reframes, in_tension_with, equivalent_under_context, and latent_context_for.
  EvidenceAtom requires evidence_id, document_id, span start/end, text_hash, and access_state; access_state enum includes available, retrieved, not_retrieved, withheld, sealed, destroyed, never_generated, not_collected, unknown, secondary_report_only, and contradictory_record.
  ProofTrace requires proof_id, claim_id, root_evidence, rules, and status; status enum is valid, invalid, partial, with optional temperature, intermediate_atoms, and checksum.
  OrthesisReport requires sno_id, accepted, metrics, strict_claims, likely_claims, unresolved_claims, and rejected_claims, with optional hypotheses, proof_traces, access_gaps, and worlds.
---
# JSON Schemas

## schemas/sno8.schema.json

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SNO-8",
  "type": "object",
  "required": [
    "sno_id",
    "version",
    "hypothesis",
    "claims",
    "relations",
    "evidence",
    "metrics",
    "lineage"
  ],
  "properties": {
    "sno_id": {
      "type": "string"
    },
    "version": {
      "const": "8.0"
    },
    "hypothesis": {
      "type": "object"
    },
    "claims": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/claim"
      }
    },
    "relations": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relation"
      }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "record_access": {
      "type": "array"
    },
    "proof_traces": {
      "type": "array"
    },
    "residuals": {
      "type": "array"
    },
    "latent_predicates": {
      "type": "array"
    },
    "world_support": {
      "type": "array"
    },
    "metrics": {
      "type": "object"
    },
    "lineage": {
      "type": "object"
    }
  },
  "$defs": {
    "claim": {
      "type": "object",
      "required": [
        "claim_id",
        "text",
        "status",
        "evidence_refs"
      ],
      "properties": {
        "claim_id": {
          "type": "string"
        },
        "text": {
          "type": "string"
        },
        "status": {
          "enum": [
            "strict",
            "likely",
            "hypothesis",
            "unresolved",
            "rejected"
          ]
        },
        "evidence_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "proof_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "confidence": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      }
    },
    "relation": {
      "type": "object",
      "required": [
        "source",
        "target",
        "type"
      ],
      "properties": {
        "source": {
          "type": "string"
        },
        "target": {
          "type": "string"
        },
        "type": {
          "enum": [
            "supports",
            "refutes",
            "implies",
            "conditions",
            "narrows",
            "explains",
            "reframes",
            "in_tension_with",
            "equivalent_under_context",
            "latent_context_for"
          ]
        },
        "evidence_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    }
  }
}
````

## schemas/evidence_atom.schema.json

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "EvidenceAtom",
  "type": "object",
  "required": [
    "evidence_id",
    "document_id",
    "span",
    "text_hash",
    "access_state"
  ],
  "properties": {
    "evidence_id": {
      "type": "string"
    },
    "document_id": {
      "type": "string"
    },
    "span": {
      "type": "object",
      "required": [
        "start",
        "end"
      ],
      "properties": {
        "start": {
          "type": "integer"
        },
        "end": {
          "type": "integer"
        }
      }
    },
    "text": {
      "type": "string"
    },
    "text_hash": {
      "type": "string"
    },
    "source_quality": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "access_state": {
      "enum": [
        "available",
        "retrieved",
        "not_retrieved",
        "withheld",
        "sealed",
        "destroyed",
        "never_generated",
        "not_collected",
        "unknown",
        "secondary_report_only",
        "contradictory_record"
      ]
    },
    "timestamp": {
      "type": "string"
    },
    "metadata": {
      "type": "object"
    }
  }
}
````

## schemas/proof_trace.schema.json

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProofTrace",
  "type": "object",
  "required": [
    "proof_id",
    "claim_id",
    "root_evidence",
    "rules",
    "status"
  ],
  "properties": {
    "proof_id": {
      "type": "string"
    },
    "claim_id": {
      "type": "string"
    },
    "root_evidence": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "rules": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "temperature": {
      "type": "number"
    },
    "intermediate_atoms": {
      "type": "array"
    },
    "status": {
      "enum": [
        "valid",
        "invalid",
        "partial"
      ]
    },
    "checksum": {
      "type": "string"
    }
  }
}
````

## schemas/orthesis_report.schema.json

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OrthesisReport",
  "type": "object",
  "required": [
    "sno_id",
    "accepted",
    "metrics",
    "strict_claims",
    "likely_claims",
    "unresolved_claims",
    "rejected_claims"
  ],
  "properties": {
    "sno_id": {
      "type": "string"
    },
    "accepted": {
      "type": "boolean"
    },
    "metrics": {
      "type": "object"
    },
    "strict_claims": {
      "type": "array"
    },
    "likely_claims": {
      "type": "array"
    },
    "hypotheses": {
      "type": "array"
    },
    "unresolved_claims": {
      "type": "array"
    },
    "rejected_claims": {
      "type": "array"
    },
    "proof_traces": {
      "type": "array"
    },
    "access_gaps": {
      "type": "array"
    },
    "worlds": {
      "type": "array"
    }
  }
}
````
