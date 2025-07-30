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

Our `CriticPipeline` class directly implements this weighted summation. Look at the `evaluate_sno` method:

```python
# From CriticPipeline.evaluate_sno
total_weighted_score = 0.0
total_weight = 0.0

for critic_type, critic in self.critics.items():
    result = critic.evaluate(sno, context)
    total_weighted_score += result.score * critic.weight
    total_weight += critic.weight

trust_score = total_weighted_score / total_weight if total_weight > 0 else 0.0
```

Here's the breakdown:

- The `for` loop iterates through each critic, which represents the summation ($\sum$).
- `result.score` is the $\text{Score}_i(\mathcal{S})$ for a specific critic (Grounding, Logic, or Novelty).
- `critic.weight` is the $w_i$ for that critic.
- `total_weighted_score` accumulates the `result.score * critic.weight` product for each critic.
- Finally, we divide by `total_weight` to normalize the score, which becomes the SNO's final `trust_score` (`T`).

The `adjust_weights` method allows for the dynamic adjustment of $w_i$ values, just as described in the paper.

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
    score: float  # Normalized score [0, 1]
    confidence: float  # Confidence in the assessment [0, 1]
    explanation: str  # Human-readable explanation
    evidence: Dict[str, Any]  # Supporting evidence for the score
    sub_scores: Dict[str, float]  # Breakdown of component scores

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
        """Evaluate an SNO and return detailed results"""
        pass
    
    def update_weight(self, new_weight: float):
        """Dynamically adjust critic weight based on context"""
        self.weight = new_weight
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get performance statistics for this critic"""
        return {
            'type': self.critic_type.value,
            'weight': self.weight,
            'evaluations': self.evaluation_count,
            'avg_score': np.mean([r['score'] for r in self.performance_history]) if self.performance_history else 0.0,
            'avg_confidence': np.mean([r['confidence'] for r in self.performance_history]) if self.performance_history else 0.0
        }

class CriticPipeline:
    """Orchestrates multiple critics to produce comprehensive SNO evaluation"""
    
    def __init__(self):
        self.critics: Dict[CriticType, BaseCritic] = {}
        self.evaluation_history = []
    
    def add_critic(self, critic: BaseCritic):
        """Add a critic to the pipeline"""
        self.critics[critic.critic_type] = critic
    
    def evaluate_sno(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Evaluate an SNO using all available critics"""
        results = {}
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for critic_type, critic in self.critics.items():
            result = critic.evaluate(sno, context)
            results[critic_type.value] = result
            
            # Accumulate weighted score
            total_weighted_score += result.score * critic.weight
            total_weight += critic.weight
            
            # Update critic performance history
            critic.performance_history.append({
                'score': result.score,
                'confidence': result.confidence
            })
            critic.evaluation_count += 1
        
        # Compute final trust score
        trust_score = total_weighted_score / total_weight if total_weight > 0 else 0.0
        
        # Update SNO trust score
        sno.trust_score = trust_score
        
        evaluation_result = {
            'trust_score': trust_score,
            'critic_results': results,
            'weights_used': {ct.value: c.weight for ct, c in self.critics.items()},
            'evaluation_id': len(self.evaluation_history)
        }
        
        self.evaluation_history.append(evaluation_result)
        return evaluation_result
    
    def adjust_weights(self, weight_updates: Dict[CriticType, float]):
        """Dynamically adjust critic weights based on context"""
        for critic_type, new_weight in weight_updates.items():
            if critic_type in self.critics:
                self.critics[critic_type].update_weight(new_weight)

### 1. Grounding Critic Implementation

> **From Paper to Code: The Grounding Critic**
> The Grounding Critic evaluates how well a narrative's claims are supported by its evidence. Section 2.2 provides its formula:

$$
\text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e)
$$

> Here, $p(v|e)$ is the plausibility score of a claim `v` given a piece of evidence `e`. We will implement this using a pre-trained Natural Language Inference (NLI) model. An NLI model takes a premise (evidence) and a hypothesis (claim) and outputs probabilities for "entailment," "neutral," and "contradiction." We will use the "entailment" probability as our $p(v|e)$.

```python
class GroundingCritic(BaseCritic):
    def __init__(self, weight: float, nli_model=None, nli_tokenizer=None, nli_model_name: str = "microsoft/deberta-large-mnli"):
        super().__init__(CriticType.GROUNDING, weight)
        
        # Use pre-loaded models if provided (for efficiency), otherwise load on demand
        if nli_model is not None and nli_tokenizer is not None:
            self.nli_model = nli_model
            self.nli_tokenizer = nli_tokenizer
        elif HAS_TRANSFORMERS:
            import transformers
            self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(nli_model_name)
            self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(nli_model_name)
        else:
            raise ImportError("Transformers library is required for the GroundingCritic.")
        
        # Ensure we know the index for entailment
        self.entailment_id = self.nli_model.config.label2id.get('entailment', 2)  # Default to 2 if not found

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        claims = [data['claim'] for _, data in sno.reasoning_graph.nodes(data=True)]
        evidence_contents = [item.content for item in sno.evidence_set]
        
        if not claims or not evidence_contents:
            return CriticResult(0.0, 1.0, "No claims or evidence to ground.", {}, {})

        total_max_plausibility = 0.0
        sub_scores = {}

        for claim in claims:
            max_plausibility_for_claim = 0.0
            
            # Prepare NLI model inputs
            pairs = [(e, claim.content) for e in evidence_contents]
            inputs = self.nli_tokenizer(pairs, return_tensors='pt', padding=True, truncation=True)
            
            with torch.no_grad():
                logits = self.nli_model(**inputs).logits
                
            # Get probabilities for entailment
            # We use softmax to convert logits to probabilities
            probabilities = torch.softmax(logits, dim=1)
            entailment_probs = probabilities[:, self.entailment_id].tolist()
            
            if entailment_probs:
                max_plausibility_for_claim = max(entailment_probs)
            
            total_max_plausibility += max_plausibility_for_claim
            sub_scores[claim.claim_id] = max_plausibility_for_claim

        # Score is the average of the max plausibility scores for each claim
        final_score = total_max_plausibility / len(claims) if claims else 0.0
        
        return CriticResult(
            score=final_score,
            confidence=0.8, # Confidence can be improved with model-specific metrics
            explanation=f"Average max NLI entailment score across {len(claims)} claims is {final_score:.3f}.",
            evidence={'claim_scores': sub_scores},
            sub_scores=sub_scores
        )
```

### 2. Logic Critic Implementation

> **From Paper to Code: The Logic Critic**
> The Logic Critic assesses the structural coherence of the reasoning graph $G$. The paper specifies this as:

$$
\text{Score}_L = f_{\text{GNN}}(G; \theta)
$$

> Training a full Graph Neural Network (GNN) is a research project in itself. For our primitive, we will create a *functional proxy* for $f_{\text{GNN}}$ that uses graph-theoretic features to approximate logical coherence. This is a robust, explainable starting point for future GNN development. We'll check for orphaned claims, excessive branching (unfocused arguments), and graph density.

```python
class LogicCritic(BaseCritic):
    def __init__(self, weight: float):
        super().__init__(CriticType.LOGIC, weight)

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        G = sno.reasoning_graph
        num_nodes = G.number_of_nodes()
        if num_nodes <= 1:
            return CriticResult(1.0, 1.0, "Graph is too simple to assess logic.", {}, {})

        # 1. Orphaned claims score (we want 0 orphans)
        # Nodes with in-degree 0 (excluding the root) are orphans
        orphaned_nodes = [n for n, d in G.in_degree() if d == 0 and n != 'root']
        orphan_penalty = len(orphaned_nodes) / (num_nodes - 1)
        orphan_score = 1.0 - orphan_penalty
        
        # 2. Coherence score (low branching is better)
        # Average out-degree measures branching. Lower is more focused.
        avg_out_degree = sum(d for _, d in G.out_degree()) / num_nodes
        # Normalize: assume max reasonable branching is ~3
        coherence_score = max(0, 1.0 - (avg_out_degree / 3.0))

        # 3. Parsimony score (related to density)
        # We prefer simpler, less dense graphs.
        density = nx.density(G)
        parsimony_score = 1.0 - density

        # Combine scores
        final_score = 0.5 * orphan_score + 0.3 * coherence_score + 0.2 * parsimony_score
        
        sub_scores = {
            'orphan_score': orphan_score,
            'coherence_score': coherence_score,
            'parsimony_score': parsimony_score
        }

        return CriticResult(
            score=final_score,
            confidence=0.9, # High confidence as it's deterministic
            explanation=f"Logic score based on graph structure: {final_score:.3f}",
            evidence={'num_orphans': len(orphaned_nodes), 'avg_out_degree': avg_out_degree, 'density': density},
            sub_scores=sub_scores
        )
```

### 3. Novelty-Parsimony Critic Implementation

> **From Paper to Code: The Novelty-Parsimony Critic**
> This critic balances innovation against complexity. The formula from Section 2.2 is:
> $$
> \text{Score}_N = \alpha \cdot \min_i \|H - H_i\|_2 - \beta \cdot \frac{|E_G|}{|V|}
> $$
> The formula uses subtraction to create this balance. The first term rewards novelty (Euclidean distance to the nearest neighbor in the SNO population), and the second term, scaled by β, penalizes graph complexity (edge-to-node ratio). Since the result is not inherently bounded in [0, 1], our code calculates the raw score and then clamps the result to fit within our scoring framework.

```python
class NoveltyParsimonyCritic(BaseCritic):
    def __init__(self, weight: float, alpha: float, beta: float):
        super().__init__(CriticType.NOVELTY, weight)
        self.alpha = alpha
        self.beta = beta

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        sno_population = context.get('sno_population', [])
        
        # 1. Calculate Novelty Term: α * min_i ||H - H_i||
        population_embeddings = [s.hypothesis_embedding for s in sno_population if s.sno_id != sno.sno_id and s.hypothesis_embedding is not None]
        
        if not population_embeddings or sno.hypothesis_embedding is None:
            novelty_term = self.alpha * 1.0 # Max novelty if no population to compare to
            min_dist_str = "N/A (first SNO)"
        else:
            distances = [np.linalg.norm(sno.hypothesis_embedding - h) for h in population_embeddings]
            min_distance = min(distances)
            # Normalize distance (max L2 is 2.0) and multiply by alpha
            novelty_term = self.alpha * (min_distance / 2.0)
            min_dist_str = f"{min_distance:.3f}"

        # 2. Calculate Parsimony Penalty Term: β * (|E_G| / |V|)
        G = sno.reasoning_graph
        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        
        complexity_ratio = 0.0
        if num_nodes > 0:
            complexity_ratio = num_edges / num_nodes
        
        parsimony_penalty = self.beta * complexity_ratio

        # 3. Calculate Final Score according to the formula
        raw_score = novelty_term - parsimony_penalty
        
        # Clamp the score to be within the [0, 1] range
        final_score = np.clip(raw_score, 0, 1)

        explanation = f"Score({final_score:.3f}) = NoveltyTerm({novelty_term:.3f}) - ParsimonyPenalty({parsimony_penalty:.3f}). Min dist: {min_dist_str}."
        
        return CriticResult(
            score=final_score,
            confidence=0.9,
            explanation=explanation,
            evidence={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty, 'complexity_ratio': complexity_ratio},
            sub_scores={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty}
        )
```
