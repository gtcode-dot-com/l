---
title: "Python Sketches"
description: "Reference Python sketches for CNS 8.0 computational components."
lastmod: "2026-05-15"
weight: 370
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
  headline: "Python Sketches"
  description: "Reference Python sketches for CNS 8.0 computational components."
ai_agent_note: |
  ATTN AI Agent:
  This page contains small test-oriented Python sketches for CNS 8.0 implementation planning, not production code.
  Sketch files listed are cns8_types.py, chirality.py, tensor_logic.py, predicate_invention.py, orthesis_loop.py, world_ranking.py, and synthetic_latent_context.py.
  cns8_types.py defines dataclasses for EvidenceAtom, Claim, Relation, ProofTrace, LatentPredicate, Residual, and SNO with claim statuses strict/likely/hypothesis/unresolved/rejected and relation types such as supports/refutes/conditions/latent_context_for.
  chirality.py sketches evidence_entanglement, evidence_polarity_chirality, graph_chirality, and productive_conflict_score with graph/polarity/entanglement/interaction weights.
  tensor_logic.py sketches zero-temperature supported-claim closure from citation and entailment matrices and computes ZTHR from strict claim IDs and proof edges.
  predicate_invention.py builds unresolved contradiction mass as min(support, refute)*(1-resolved), factorizes the context mode with SVD, and computes PIU.
  orthesis_loop.py sketches render -> ground -> distance -> update iteration with residual threshold and max iterations; world_ranking.py ranks possible worlds as auxiliary uncertainty; synthetic_latent_context.py generates toy contradictions with hidden contexts such as time_period, subgroup, dose, jurisdiction, measurement_method, or definition.
---
# Python Sketches

## sketches/README.md

````markdown
# Python Sketches

These files are minimal small examples for CNS 8.0 implementation planning.

- `cns8_types.py` — dataclasses for EvidenceAtom, Claim, Relation, ProofTrace, SNO.
- `chirality.py` — evidence entanglement and chirality proxies.
- `tensor_logic.py` — tiny zero-temperature proof closure sketch.
- `predicate_invention.py` — residual tensor and factorization sketch.
- `orthesis_loop.py` — render/re-ground fixed-point loop.
- `world_ranking.py` — possible-world posterior as reporting substrate.
- `synthetic_latent_context.py` — toy latent-context generator.

They are deliberately small and test-oriented.
````

## sketches/cns8_types.py

````python
"""CNS 8.0 type sketches.

Not production code. These classes define the minimal shape for the MVP.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal, Any

ClaimStatus = Literal["strict", "likely", "hypothesis", "unresolved", "rejected"]
RelationType = Literal[
    "supports", "refutes", "implies", "conditions", "narrows", "explains",
    "reframes", "in_tension_with", "equivalent_under_context", "latent_context_for"
]

@dataclass(frozen=True)
class EvidenceAtom:
    evidence_id: str
    document_id: str
    text: str
    start: int
    end: int
    text_hash: str
    source_quality: float = 1.0
    access_state: str = "available"
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class Claim:
    claim_id: str
    text: str
    status: ClaimStatus = "hypothesis"
    evidence_refs: list[str] = field(default_factory=list)
    proof_refs: list[str] = field(default_factory=list)
    confidence: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class Relation:
    source: str
    target: str
    type: RelationType
    evidence_refs: list[str] = field(default_factory=list)
    weight: float = 1.0

@dataclass
class ProofTrace:
    proof_id: str
    claim_id: str
    root_evidence: list[str]
    rules: list[str]
    intermediate_atoms: list[str] = field(default_factory=list)
    temperature: float = 0.0
    status: str = "valid"

@dataclass
class LatentPredicate:
    predicate_id: str
    label: str
    source: str
    grounding_status: str = "candidate"
    evidence_refs: list[str] = field(default_factory=list)
    piu: float = 0.0

@dataclass
class Residual:
    subject: str
    predicate: str
    object: str
    context: str
    support_mass: float
    refute_mass: float
    unresolved_mass: float

@dataclass
class SNO:
    sno_id: str
    hypothesis: str
    claims: list[Claim] = field(default_factory=list)
    relations: list[Relation] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    proof_traces: list[ProofTrace] = field(default_factory=list)
    residuals: list[Residual] = field(default_factory=list)
    latent_predicates: list[LatentPredicate] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    lineage: dict[str, Any] = field(default_factory=dict)
````

## sketches/chirality.py

````python
"""Chirality and Evidential Entanglement sketches."""
from __future__ import annotations
from collections import defaultdict
from math import exp
from cns8_types import SNO

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def evidence_entanglement(a: SNO, b: SNO, weights: dict[str, float] | None = None) -> float:
    weights = weights or {}
    ea, eb = set(a.evidence), set(b.evidence)
    union = ea | eb
    if not union:
        return 0.0
    inter = ea & eb
    return sum(weights.get(e, 1.0) for e in inter) / sum(weights.get(e, 1.0) for e in union)

def evidence_polarity_map(sno: SNO) -> dict[tuple[str, str], float]:
    """Map (evidence_id, claim_id) to signed stance support=+1 refute=-1."""
    out: dict[tuple[str, str], float] = defaultdict(float)
    for rel in sno.relations:
        if rel.type not in ("supports", "refutes"):
            continue
        sign = 1.0 if rel.type == "supports" else -1.0
        for e in rel.evidence_refs:
            out[(e, rel.target)] += sign * rel.weight
    return out

def evidence_polarity_chirality(a: SNO, b: SNO) -> float:
    pa, pb = evidence_polarity_map(a), evidence_polarity_map(b)
    keys = set(pa) | set(pb)
    if not keys:
        return 0.0
    return sum(abs(pa.get(k, 0.0) - pb.get(k, 0.0)) for k in keys) / len(keys)

def graph_chirality(a: SNO, b: SNO) -> float:
    """Simple edge-set disagreement proxy.

    Production implementation should use aligned signed incidence matrices.
    """
    ea = {(r.source, r.target, r.type) for r in a.relations}
    eb = {(r.source, r.target, r.type) for r in b.relations}
    union = ea | eb
    if not union:
        return 0.0
    return len(ea ^ eb) / len(union)

def productive_conflict_score(a: SNO, b: SNO, weights: dict[str, float] | None = None) -> float:
    weights = weights or {"graph": 0.30, "polarity": 0.30, "ent": 0.20, "interaction": 0.20}
    g = graph_chirality(a, b)
    p = evidence_polarity_chirality(a, b)
    ent = evidence_entanglement(a, b)
    raw = weights["graph"] * g + weights["polarity"] * p + weights["ent"] * ent + weights["interaction"] * p * ent
    return sigmoid(4.0 * (raw - 0.5))
````

## sketches/tensor_logic.py

````python
"""Tiny zero-temperature tensor-logic closure sketch.

This is deliberately small: boolean matrices plus explicit proof traces.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass
class ClosureResult:
    supported: np.ndarray
    proof_edges: list[tuple[int, int, str]]

def zero_temp_supported(cites: np.ndarray, entails: np.ndarray) -> ClosureResult:
    """Derive Supported[c] = step(sum_e Cites[c,e] * Entails[e,c]).

    cites: shape [claims, evidence]
    entails: shape [evidence, claims]
    """
    scores = (cites.astype(int) * entails.T.astype(int)).sum(axis=1)
    supported = scores > 0
    proofs: list[tuple[int, int, str]] = []
    for c in range(cites.shape[0]):
        for e in range(cites.shape[1]):
            if cites[c, e] and entails[e, c]:
                proofs.append((c, e, "supported_claim(c) <- cites(c,e) AND entails(e,c)"))
    return ClosureResult(supported=supported, proof_edges=proofs)

def zthr(strict_claim_ids: list[int], proof_edges: list[tuple[int, int, str]]) -> float:
    strict = set(strict_claim_ids)
    if not strict:
        return 0.0
    proved = {c for (c, _e, _rule) in proof_edges}
    missing = strict - proved
    return len(missing) / len(strict)

if __name__ == "__main__":
    cites = np.array([[1,0], [0,1], [0,0]], dtype=bool)
    entails = np.array([[1,0,0], [0,1,0]], dtype=bool)
    result = zero_temp_supported(cites, entails)
    print(result.supported.tolist())
    print(result.proof_edges)
    print("ZTHR", zthr([0,1], result.proof_edges))
````

## sketches/predicate_invention.py

````python
"""Residual tensor factorization sketch for predicate invention.

Uses matricized SVD as a placeholder for Tucker/CP decomposition.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

@dataclass
class PredicateCandidate:
    axis: str
    index: int
    score: float
    label_hint: str

def build_residual_tensor(support: np.ndarray, refute: np.ndarray, resolved: np.ndarray | None = None) -> np.ndarray:
    """Unresolved contradiction mass: min(support, refute) * (1-resolved)."""
    if resolved is None:
        resolved = np.zeros_like(support)
    return np.minimum(support, refute) * (1.0 - resolved)

def factorize_context_mode(residual: np.ndarray, top_k: int = 3) -> list[PredicateCandidate]:
    """Find high-energy context factors by matricizing all but last axis."""
    if residual.ndim < 2:
        raise ValueError("residual tensor must have at least 2 axes")
    context_dim = residual.shape[-1]
    mat = residual.reshape((-1, context_dim))
    if mat.size == 0:
        return []
    _u, s, vt = np.linalg.svd(mat, full_matrices=False)
    candidates: list[PredicateCandidate] = []
    for k in range(min(top_k, len(s))):
        context_idx = int(np.argmax(np.abs(vt[k])))
        score = float(s[k] * abs(vt[k, context_idx]))
        candidates.append(PredicateCandidate("context", context_idx, score, f"latent_context_{context_idx}"))
    return candidates

def predicate_invention_utility(before_energy: float, after_energy: float, complexity: float) -> float:
    return max(0.0, before_energy - after_energy) / (1.0 + complexity)

if __name__ == "__main__":
    rng = np.random.default_rng(7)
    support = rng.random((4,3,4,2))
    refute = rng.random((4,3,4,2))
    residual = build_residual_tensor(support, refute)
    print(factorize_context_mode(residual))
````

## sketches/orthesis_loop.py

````python
"""Orthesis loop sketch."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class OrthesisStep:
    iteration: int
    residual: float
    accepted: bool
    notes: str

@dataclass
class OrthesisResult:
    accepted: bool
    final_state: Any
    steps: list[OrthesisStep]

def orthesis_loop(
    logic_state: Any,
    render: Callable[[Any], str],
    ground: Callable[[str], Any],
    distance: Callable[[Any, Any], float],
    update: Callable[[Any, Any], Any],
    threshold: float = 0.10,
    max_iters: int = 3,
) -> OrthesisResult:
    """Render -> ground -> compare -> update loop.

    Production code should preserve proof traces and compare proof-critical atoms.
    """
    state = logic_state
    steps: list[OrthesisStep] = []
    for i in range(max_iters):
        text = render(state)
        regrounded = ground(text)
        residual = distance(state, regrounded)
        accepted = residual <= threshold
        steps.append(OrthesisStep(i, residual, accepted, "round-trip residual"))
        if accepted:
            return OrthesisResult(True, state, steps)
        state = update(state, regrounded)
    return OrthesisResult(False, state, steps)
````

## sketches/synthetic_latent_context.py

````python
"""Synthetic latent-context generator sketch."""
from __future__ import annotations
from dataclasses import dataclass
import random

@dataclass
class SyntheticCase:
    evidence: list[str]
    claim_a: str
    claim_b: str
    hidden_context: str
    expected_synthesis: str

CONTEXTS = ["time_period", "subgroup", "dose", "jurisdiction", "measurement_method", "definition"]

def generate_case(seed: int | None = None) -> SyntheticCase:
    rng = random.Random(seed)
    context = rng.choice(CONTEXTS)
    value_a, value_b = "A", "B"
    evidence = [
        f"Evidence E1 says predicate P holds under {context}={value_a}.",
        f"Evidence E2 says predicate P does not hold under {context}={value_b}.",
    ]
    return SyntheticCase(
        evidence=evidence,
        claim_a="P holds.",
        claim_b="P does not hold.",
        hidden_context=context,
        expected_synthesis=f"P is conditional on {context}; it holds for {value_a} and does not hold for {value_b}.",
    )

if __name__ == "__main__":
    for i in range(3):
        print(generate_case(i))
````

## sketches/world_ranking.py

````python
"""Possible-world ranking as auxiliary uncertainty reporting."""
from __future__ import annotations
from dataclasses import dataclass
from math import exp

@dataclass
class World:
    world_id: str
    log_likelihood: float
    log_prior: float
    residual_energy: float
    chirality_residual: float
    access_penalty: float = 0.0

def rank_worlds(worlds: list[World], alpha: float = 1.0, beta: float = 1.0) -> list[tuple[World, float]]:
    scores = []
    for w in worlds:
        score = w.log_likelihood + w.log_prior - alpha * w.residual_energy - beta * w.chirality_residual - w.access_penalty
        scores.append(score)
    if not scores:
        return []
    m = max(scores)
    probs = [exp(s - m) for s in scores]
    z = sum(probs)
    return sorted(zip(worlds, [p / z for p in probs]), key=lambda x: x[1], reverse=True)
````
