---
title: "Chapter 3: Multi-Component Critic Pipeline"
description: "Implementing transparent evaluation systems for grounding, logic, and novelty assessment"
weight: 3
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 3: Multi-Component Critic Pipeline

## The Problem with Black-Box Evaluation

Traditional knowledge synthesis systems often rely on opaque "oracle" critics that provide scores without explanation. CNS 2.0 takes a fundamentally different approach by decomposing evaluation into transparent, specialized components that each assess distinct aspects of narrative quality.

The Multi-Component Critic Pipeline consists of three specialized critics:

1. **Grounding Critic** - Evaluates evidential support
2. **Logic Critic** - Assesses structural coherence  
3. **Novelty-Parsimony Critic** - Balances innovation against complexity

### From Paper to Code: The Mathematical Foundation

The power of this pipeline comes from its transparent, component-based approach to calculating a final reward or trust score. The paper formalizes this in Section 2.2 with Equation (1).

> **From the Paper (Equation 1):**
> The final trust score $T$ and reward signal emerge from a weighted combination:

$$
\text{Reward}(\mathcal{S}) = \sum_{i \in \{G, L, N\}} w_i \cdot \text{Score}_i(\mathcal{S})
$$

> where $w_i$ are dynamically adjustable weights and the component scores are from the Grounding, Logic, and Novelty-Parsimony critics.

**From Paper to Code:**

Our `CriticPipeline` class directly implements this weighted summation. The `evaluate_sno` method iterates through each registered critic, calculates its score, multiplies it by the critic's weight, and sums the results. This weighted sum is then normalized to produce the final `trust_score`. The `adjust_weights` method allows for the dynamic adjustment of $w_i$ values, a crucial feature for contextual evaluation that we will discuss later in this chapter.

## Implementing the Specialized Critics

```python
"""
Multi-Component Critic Pipeline Implementation
============================================
Transparent, auditable evaluation of SNO quality
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Optional, Any
import numpy as np
from dataclasses import dataclass
from enum import Enum

@dataclass
class CriticResult:
    """Result from a critic evaluation with full transparency"""
    score: float
    confidence: float
    explanation: str
    evidence: Dict[str, Any]
    sub_scores: Dict[str, float]

class CriticType(Enum):
    GROUNDING = "grounding"
    LOGIC = "logic"
    NOVELTY = "novelty"

class BaseCritic(ABC):
    """Abstract base class for all CNS 2.0 critics"""
    
    def __init__(self, critic_type: CriticType, weight: float = 1.0):
        self.critic_type = critic_type
        self.weight = weight
        self.evaluation_count = 0
        self.performance_history = []
    
    @abstractmethod
    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        pass
    
    def update_weight(self, new_weight: float):
        self.weight = new_weight
    
    def get_statistics(self) -> Dict[str, Any]:
        return {
            'type': self.critic_type.value,
            'weight': self.weight,
            'evaluations': self.evaluation_count,
            'avg_score': np.mean([r['score'] for r in self.performance_history]) if self.performance_history else 0.0,
        }

class CriticPipeline:
    """Orchestrates multiple critics to produce comprehensive SNO evaluation"""
    
    def __init__(self):
        self.critics: Dict[CriticType, BaseCritic] = {}
        self.evaluation_history = []
    
    def add_critic(self, critic: BaseCritic):
        self.critics[critic.critic_type] = critic
    
    def evaluate_sno(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> Dict[str, Any]:
        results = {}
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for critic_type, critic in self.critics.items():
            result = critic.evaluate(sno, context)
            results[critic_type.value] = result
            total_weighted_score += result.score * critic.weight
            total_weight += critic.weight
            critic.performance_history.append({'score': result.score, 'confidence': result.confidence})
            critic.evaluation_count += 1
        
        trust_score = total_weighted_score / total_weight if total_weight > 0 else 0.0
        sno.trust_score = trust_score
        
        evaluation_result = {
            'trust_score': trust_score,
            'critic_results': results,
            'weights_used': {ct.value: c.weight for ct, c in self.critics.items()},
        }
        self.evaluation_history.append(evaluation_result)
        return evaluation_result
    
    def adjust_weights(self, weight_updates: Dict[CriticType, float]):
        for critic_type, new_weight in weight_updates.items():
            if critic_type in self.critics:
                self.critics[critic_type].update_weight(new_weight)

### 1. Grounding Critic Implementation

> **From Paper to Code: The Grounding Critic**
> The Grounding Critic evaluates how well a narrative's claims are supported by its evidence. The paper provides its formula:
> $$ \text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e) $$
> Here, $p(v|e)$ is the plausibility score of a claim `v` given evidence `e`. We implement this using a pre-trained Natural Language Inference (NLI) model, where the "entailment" probability serves as $p(v|e)$.

```python
class GroundingCritic(BaseCritic):
    def __init__(self, weight: float, nli_model=None, nli_tokenizer=None, nli_model_name: str = "microsoft/deberta-large-mnli"):
        super().__init__(CriticType.GROUNDING, weight)
        if nli_model and nli_tokenizer:
            self.nli_model, self.nli_tokenizer = nli_model, nli_tokenizer
        elif HAS_TRANSFORMERS:
            import transformers
            self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(nli_model_name)
            self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(nli_model_name)
        else:
            raise ImportError("Transformers library is required for the GroundingCritic.")
        self.entailment_id = self.nli_model.config.label2id.get('entailment', 2)

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        claims = [data['claim'] for _, data in sno.reasoning_graph.nodes(data=True)]
        evidence_contents = [item.content for item in sno.evidence_set]
        
        if not claims or not evidence_contents:
            return CriticResult(0.0, 1.0, "No claims or evidence to ground.", {}, {})

        total_max_plausibility, sub_scores = 0.0, {}
        for claim in claims:
            pairs = [(e, claim.content) for e in evidence_contents]
            inputs = self.nli_tokenizer(pairs, return_tensors='pt', padding=True, truncation=True)
            with torch.no_grad():
                logits = self.nli_model(**inputs).logits
            probabilities = torch.softmax(logits, dim=1)
            entailment_probs = probabilities[:, self.entailment_id].tolist()
            max_plausibility_for_claim = max(entailment_probs) if entailment_probs else 0.0
            total_max_plausibility += max_plausibility_for_claim
            sub_scores[claim.claim_id] = max_plausibility_for_claim

        final_score = total_max_plausibility / len(claims) if claims else 0.0
        return CriticResult(
            score=final_score, confidence=0.8,
            explanation=f"Average max NLI entailment score across {len(claims)} claims is {final_score:.3f}.",
            evidence={'claim_scores': sub_scores}, sub_scores=sub_scores
        )
```

### 2. Logic Critic Implementation

> **From Paper to Code: The Logic Critic**
> The Logic Critic assesses the structural coherence of the reasoning graph $G$. The paper specifies this as:
> $$ \text{Score}_L = f_{\text{GNN}}(G; \theta) $$
> Training a full Graph Neural Network (GNN) is a research project. For our implementation, we create a *functional proxy* for $f_{\text{GNN}}$ that uses graph-theoretic features to approximate logical coherence. This is a robust, explainable starting point.

```python
class LogicCritic(BaseCritic):
    def __init__(self, weight: float):
        super().__init__(CriticType.LOGIC, weight)

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        G = sno.reasoning_graph
        num_nodes = G.number_of_nodes()
        if num_nodes <= 1:
            return CriticResult(1.0, 1.0, "Graph is too simple to assess logic.", {}, {})

        orphaned_nodes = [n for n, d in G.in_degree() if d == 0 and n != 'root']
        orphan_penalty = len(orphaned_nodes) / (num_nodes - 1) if num_nodes > 1 else 0
        orphan_score = 1.0 - orphan_penalty
        
        avg_out_degree = sum(d for _, d in G.out_degree()) / num_nodes
        coherence_score = max(0, 1.0 - (avg_out_degree / 3.0))

        density = nx.density(G)
        parsimony_score = 1.0 - density

        final_score = 0.5 * orphan_score + 0.3 * coherence_score + 0.2 * parsimony_score
        sub_scores = {'orphan_score': orphan_score, 'coherence_score': coherence_score, 'parsimony_score': parsimony_score}

        return CriticResult(
            score=final_score, confidence=0.9,
            explanation=f"Logic score based on graph structure: {final_score:.3f}",
            evidence={'num_orphans': len(orphaned_nodes), 'avg_out_degree': avg_out_degree, 'density': density},
            sub_scores=sub_scores
        )
```

#### Path to a Production GNN-based Logic Critic
Our heuristic-based `LogicCritic` is a great starting point, but for a production system, implementing the GNN-based critic envisioned by the paper is a key enhancement. Here’s a roadmap for that process:

1.  **Data Collection:** A GNN needs labeled data. You would need to create a dataset of SNO reasoning graphs, each labeled with a "coherence score" (e.g., from 0 to 1). This dataset could be bootstrapped by human experts rating the logical soundness of various argument structures.
2.  **Feature Engineering:** Each node (claim) in the graph would need features. The most important feature would be the semantic embedding of the claim's text content. Edge features could include a one-hot encoding of the `RelationType` (e.g., `SUPPORTS`, `CONTRADICTS`).
3.  **Model Architecture:** A Graph Attention Network (GAT) or GraphSAGE would be excellent choices. These architectures can learn to weigh the importance of different neighboring claims and relationships when evaluating the logic of a central claim.
4.  **Training Task:** The GNN would be trained on a "graph classification" task. It would take the entire reasoning graph as input and output a single value—the predicted coherence score. The loss function would aim to minimize the difference between the GNN's prediction and the human-provided label from the dataset.

This GNN would be able to learn much more nuanced patterns of logical fallacies or strengths than our heuristic model, moving the critic from a proxy to a powerful, learned component.

### 3. Novelty-Parsimony Critic Implementation

> **From Paper to Code: The Novelty-Parsimony Critic**
> This critic balances innovation against complexity using the formula:
> $$ \text{Score}_N = \alpha \cdot \min_i \|H - H_i\|_2 - \beta \cdot \frac{|E_G|}{|V|} $$
> The first term rewards novelty (distance to the nearest SNO), and the second penalizes graph complexity. Our implementation calculates this raw score and then clamps it to the [0, 1] range.

```python
class NoveltyParsimonyCritic(BaseCritic):
    def __init__(self, weight: float, alpha: float, beta: float):
        super().__init__(CriticType.NOVELTY, weight)
        self.alpha = alpha
        self.beta = beta

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        sno_population = context.get('sno_population', [])
        population_embeddings = [s.hypothesis_embedding for s in sno_population if s.sno_id != sno.sno_id and s.hypothesis_embedding is not None]
        
        if not population_embeddings or sno.hypothesis_embedding is None:
            novelty_term, min_dist_str = self.alpha * 1.0, "N/A (first SNO)"
        else:
            distances = [np.linalg.norm(sno.hypothesis_embedding - h) for h in population_embeddings]
            min_distance = min(distances)
            novelty_term = self.alpha * (min_distance / 2.0) # Normalize L2 distance
            min_dist_str = f"{min_distance:.3f}"

        G = sno.reasoning_graph
        complexity_ratio = G.number_of_edges() / G.number_of_nodes() if G.number_of_nodes() > 0 else 0
        parsimony_penalty = self.beta * complexity_ratio

        raw_score = novelty_term - parsimony_penalty
        final_score = np.clip(raw_score, 0, 1)

        explanation = f"Score({final_score:.3f}) = Novelty({novelty_term:.3f}) - Parsimony({parsimony_penalty:.3f}). Min dist: {min_dist_str}."
        return CriticResult(
            score=final_score, confidence=0.9, explanation=explanation,
            evidence={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty},
            sub_scores={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty}
        )
```

## Contextual Evaluation: Dynamic Weight Adjustment

A key feature of the CNS 2.0 framework is its adaptability. The `adjust_weights` method in our `CriticPipeline` is the mechanism for this, allowing the system to change its evaluation priorities based on the current context or goal.

Why is this important? Because not all phases of knowledge discovery are the same. Sometimes you need to explore wildly different ideas; other times, you need to rigorously verify a specific claim. Dynamic weights allow the CNS system to support both.

### Scenario: Shifting from Exploration to Verification

Let's consider a common workflow:
1.  **Exploration Phase:** When starting in a new domain, the system's goal is to generate a diverse set of novel hypotheses. We want to reward new ideas, even if they are not yet perfectly logical or well-grounded.
2.  **Verification Phase:** Once a set of promising, high-novelty SNOs has been identified, the goal shifts. We now need to rigorously test these ideas, prioritizing their logical consistency and evidential support.

Here’s how we would use dynamic weights to manage this shift:

```python
# Assume 'critic_pipeline' is an instance of our CriticPipeline

# --- Phase 1: Exploration ---
# We want to find new ideas, so we boost the weight of the Novelty critic.
print("Setting weights for EXPLORATION phase...")
critic_pipeline.adjust_weights({
    CriticType.NOVELTY: 0.7,   # High weight for new ideas
    CriticType.LOGIC: 0.15,
    CriticType.GROUNDING: 0.15
})
# Now, when evaluate_sno is called, it will heavily favor novel SNOs.
print(f"Current weights: {critic_pipeline.critics[CriticType.NOVELTY].weight=}, {critic_pipeline.critics[CriticType.GROUNDING].weight=}")


# --- Phase 2: Verification ---
# We have some promising ideas. Now we need to check if they hold up.
# We boost the Grounding and Logic critics.
print("\nSetting weights for VERIFICATION phase...")
critic_pipeline.adjust_weights({
    CriticType.NOVELTY: 0.1,    # Low weight for novelty
    CriticType.LOGIC: 0.45,     # High weight for logical soundness
    CriticType.GROUNDING: 0.45  # High weight for evidential support
})
# Now, the same SNOs will be re-evaluated with a focus on their rigor.
print(f"Current weights: {critic_pipeline.critics[CriticType.NOVELTY].weight=}, {critic_pipeline.critics[CriticType.GROUNDING].weight=}")
```

This ability to programmatically shift the system's "values" makes CNS 2.0 a powerful and flexible tool for knowledge work, capable of adapting its strategy to the task at hand.
