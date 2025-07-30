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

The Grounding Critic evaluates how well a narrative's claims are supported by its evidence. It is the component responsible for ensuring that the knowledge generated by the system remains tethered to verifiable facts.

> **From the Paper (Section 2.2):**
> The formula for the Grounding Score is:
> $$ \text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e) $$
> Here, $p(v|e)$ is the plausibility score of a claim `v` given evidence `e`. We implement this using a pre-trained Natural Language Inference (NLI) model, where the "entailment" probability serves as $p(v|e)$.

#### Why Use Natural Language Inference?
Natural Language Inference is the task of determining whether a "hypothesis" sentence is true (entailment), false (contradiction), or undetermined (neutral) given a "premise" sentence. This maps perfectly to our use case:
-   **Premise**: A piece of evidence (`e`).
-   **Hypothesis**: A claim from the reasoning graph (`v`).

By feeding an (evidence, claim) pair to an NLI model, the model's predicted probability for the "entailment" class gives us a direct, well-calibrated measure of $p(v|e)$—how likely the evidence is to support the claim. This is a far more robust approach than simple keyword matching or vector similarity.

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
        # This loop corresponds to the Σ[v ∈ V] part of the formula
        for claim in claims:
            # Prepare (evidence, claim) pairs to calculate p(v|e) for all e ∈ E
            pairs = [(e, claim.content) for e in evidence_contents]
            inputs = self.nli_tokenizer(pairs, return_tensors='pt', padding=True, truncation=True)
            with torch.no_grad():
                logits = self.nli_model(**inputs).logits
            probabilities = torch.softmax(logits, dim=1)
            entailment_probs = probabilities[:, self.entailment_id].tolist()

            # This corresponds to the max[e ∈ E] p(v|e) part of the formula
            max_plausibility_for_claim = max(entailment_probs) if entailment_probs else 0.0
            total_max_plausibility += max_plausibility_for_claim
            sub_scores[claim.claim_id] = max_plausibility_for_claim

        # This corresponds to the (1/|V|) * Σ[...] part of the formula
        final_score = total_max_plausibility / len(claims) if claims else 0.0
        return CriticResult(
            score=final_score, confidence=0.8,
            explanation=f"Average max NLI entailment score across {len(claims)} claims is {final_score:.3f}.",
            evidence={'claim_scores': sub_scores}, sub_scores=sub_scores
        )
```

#### Formula-to-Code Mapping: `GroundingCritic`
- **`for claim in claims:`**: This loop implements the summation over all vertices `v` in the set `V` ($\sum_{v \in V}$).
- **`pairs = [...]`**: For each claim `v`, we create pairs with every piece of evidence `e` in the evidence set `E`. This is the input needed to calculate $p(v|e)$ for all `e`.
- **`max_plausibility_for_claim = max(entailment_probs)`**: This line finds the single best piece of evidence for the current claim, implementing the maximization operation ($\max_{e \in \mathcal{E}}$).
- **`total_max_plausibility / len(claims)`**: Finally, we take the average of these maximum scores, implementing the normalization term ($\frac{1}{|V|}$).

### 2. Logic Critic Implementation

The Logic Critic assesses the structural coherence of the reasoning graph $G$. A narrative can have well-grounded claims but still be logically flawed if the claims don't connect in a coherent way.

> **From the Paper (Section 2.2):**
> The ideal Logic Score is produced by a Graph Neural Network (GNN):
> $$ \text{Score}_L = f_{\text{GNN}}(G; \theta) $$
> Training a full GNN is a major research project. For our implementation, we create a **functional proxy** for $f_{\text{GNN}}$ that uses graph-theoretic features to approximate logical coherence. This provides a robust, transparent, and computationally inexpensive starting point.

#### Interpreting the Logic Heuristics
Our heuristic-based `LogicCritic` uses a weighted average of three graph metrics to assess structural quality:

-   **Orphan Score**: This checks for "orphaned" claims—nodes that have no incoming links (i.e., they are not supported by any other claim). A good argument should have its premises well-supported. A high number of orphans suggests a collection of disconnected assertions rather than a coherent argument.
-   **Coherence Score**: This penalizes unfocused arguments by looking at the average "out-degree" (the number of outgoing links) of the nodes. A very high average suggests a single claim is being used to justify too many different points, potentially making the argument less focused.
-   **Parsimony Score**: This is based on graph `density`. A very dense graph can be a sign of a convoluted, "spaghetti-like" argument. This score rewards parsimony (simplicity), which is often a hallmark of strong reasoning (Occam's Razor).

```python
class LogicCritic(BaseCritic):
    def __init__(self, weight: float):
        super().__init__(CriticType.LOGIC, weight)

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        G = sno.reasoning_graph
        num_nodes = G.number_of_nodes()
        if num_nodes <= 1:
            return CriticResult(1.0, 1.0, "Graph is too simple to assess logic.", {}, {})

        # Heuristic 1: Penalize orphaned claims (unsupported assertions)
        orphaned_nodes = [n for n, d in G.in_degree() if d == 0 and n != 'root']
        orphan_penalty = len(orphaned_nodes) / (num_nodes - 1) if num_nodes > 1 else 0
        orphan_score = 1.0 - orphan_penalty
        
        # Heuristic 2: Penalize unfocused claims (a single claim supporting too many others)
        avg_out_degree = sum(d for _, d in G.out_degree()) / num_nodes
        coherence_score = max(0, 1.0 - (avg_out_degree / 3.0)) # Assumes avg out-degree > 3 is too much

        # Heuristic 3: Penalize complexity (convoluted, "spaghetti" arguments)
        density = nx.density(G)
        parsimony_score = 1.0 - density

        # Our functional proxy for f_GNN is a weighted average of these heuristics
        final_score = 0.5 * orphan_score + 0.3 * coherence_score + 0.2 * parsimony_score
        sub_scores = {'orphan_score': orphan_score, 'coherence_score': coherence_score, 'parsimony_score': parsimony_score}

        return CriticResult(
            score=final_score, confidence=0.9,
            explanation=f"Logic score based on graph structure: {final_score:.3f}",
            evidence={'num_orphans': len(orphaned_nodes), 'avg_out_degree': avg_out_degree, 'density': density},
            sub_scores=sub_scores
        )
```

#### Roadmap to a Production GNN-based Logic Critic
Our heuristic-based `LogicCritic` is a robust and transparent starting point. However, to capture more subtle and complex patterns of logical reasoning, implementing the GNN-based critic envisioned by the paper is a key enhancement. A GNN can learn from data to identify sophisticated patterns of coherence or fallacy that are difficult to define with hand-crafted rules. Here is a detailed roadmap for this research and engineering effort:

1.  **Data Collection and Labeling**: This is the most critical and labor-intensive step.
    *   **Source Material**: Gather a large corpus of arguments. These could be SNOs generated from scientific papers, legal documents, or philosophical texts.
    *   **Labeling Strategy**: You need to assign a "logical coherence" score to each reasoning graph. This is non-trivial. A good approach is to use multiple human raters (ideally experts in logic or the subject matter) to score each graph on a scale (e.g., 1-5). The average or consensus score becomes the label. You would also want them to flag specific logical fallacies, which could be used for more granular training tasks.
    *   **Dataset Size**: Aim for a dataset of at least a few thousand labeled graphs to train a robust GNN.

2.  **Feature Engineering for Graph Components**: The GNN needs numerical representations of the graph's nodes and edges.
    *   **Node Features**: Each node (`ClaimNode`) must be represented as a vector. The primary feature is the semantic embedding of the claim's text content. You can also add metadata features, like a one-hot encoding of the `claim_type`.
    *   **Edge Features**: Each edge (`ReasoningEdge`) can also have features. The most important would be a numerical representation of the `RelationType` (e.g., a one-hot vector) and the `strength` of the edge.

3.  **Model Architecture Selection**: The choice of GNN architecture is key.
    *   **Good Candidates**: Graph Convolutional Networks (GCNs), GraphSAGE, and Graph Attention Networks (GATs) are all strong choices.
    *   **Why GAT is a strong contender**: A Graph Attention Network (GAT) is particularly well-suited for this task. GATs learn to assign different "attention" weights to different neighbors when aggregating information. In our context, this means the model could learn that a `CONTRADICTS` edge from a highly trusted claim is more important than a `SUPPORTS` edge from a weak one. This ability to weigh the importance of relationships is central to logical analysis.

4.  **Training Task Definition**: The GNN will be trained on a **graph regression** task.
    *   **Input**: The entire reasoning graph, with its node and edge features.
    -   **Output**: A single continuous value, the predicted coherence score.
    -   **Loss Function**: A standard regression loss function like Mean Squared Error (MSE) would be used to minimize the difference between the GNN's predicted score and the average human-rated score from the dataset.

By completing this process, you replace the heuristic-based proxy with a powerful, data-driven model of logical coherence, significantly increasing the sophistication of the entire CNS 2.0 system.

### 3. Novelty-Parsimony Critic Implementation

This critic balances two competing virtues: the desire for new ideas (novelty) and the principle of simplicity (parsimony, or Occam's Razor). It ensures the system explores new territory without producing needlessly complex explanations.

> **From the Paper (Section 2.2):**
> This critic's score is calculated as:
> $$ \text{Score}_N = \alpha \cdot \min_i \|H - H_i\|_2 - \beta \cdot \frac{|E_G|}{|V|} $$
> The first term rewards novelty (distance to the nearest SNO), and the second penalizes graph complexity. Our implementation calculates this raw score and then clamps it to the [0, 1] range.

#### A Note on Normalization and Clamping
The raw score from this formula can be outside the standard `[0, 1]` range required by our system. We handle this in two ways:
1.  **Distance Normalization**: The raw Euclidean distance $\|H - H_i\|_2$ between embeddings doesn't have a fixed upper bound. We normalize it by dividing by `2.0` (the maximum possible distance between two normalized vectors) to bring the novelty term into a more predictable range.
2.  **Clamping**: After calculating the final `raw_score`, we use `np.clip(raw_score, 0, 1)`. This is a hard clamp that forces the final score into the `[0, 1]` interval, ensuring it's a valid input for the final weighted average.

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
            # Corresponds to the ||H - H_i||₂ part of the formula
            distances = [np.linalg.norm(sno.hypothesis_embedding - h) for h in population_embeddings]
            # Corresponds to the min_i part of the formula
            min_distance = min(distances)
            # Corresponds to the α * ... part, with normalization
            novelty_term = self.alpha * (min_distance / 2.0)
            min_dist_str = f"{min_distance:.3f}"

        G = sno.reasoning_graph
        # Corresponds to the |E_G|/|V| part of the formula
        complexity_ratio = G.number_of_edges() / G.number_of_nodes() if G.number_of_nodes() > 0 else 0
        # Corresponds to the β * ... part of the formula
        parsimony_penalty = self.beta * complexity_ratio

        raw_score = novelty_term - parsimony_penalty
        final_score = np.clip(raw_score, 0, 1) # Clamp to [0, 1]

        explanation = f"Score({final_score:.3f}) = Novelty({novelty_term:.3f}) - Parsimony({parsimony_penalty:.3f}). Min dist: {min_dist_str}."
        return CriticResult(
            score=final_score, confidence=0.9, explanation=explanation,
            evidence={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty},
            sub_scores={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty}
        )
```

## Contextual Evaluation: Dynamic Weight Adjustment

A key feature of the CNS 2.0 framework is its adaptability. The `adjust_weights` method in our `CriticPipeline` is the mechanism for this, allowing the system to change its "values" or priorities based on the current goal. Not all phases of knowledge discovery are the same; sometimes the goal is to explore wildly different ideas, while other times it is to rigorously verify a specific claim. Dynamic weights allow the CNS system to support both modes of operation.

### Scenario: Shifting from Exploration to Verification

Let's demonstrate this with a concrete example. We will create a sample SNO that is highly novel but has mediocre logic and grounding. We will then evaluate it under two different weighting schemes: one that prioritizes novelty (Exploration Mode) and one that prioritizes rigor (Verification Mode).

```python
# --- Setup: Create a sample SNO and a pipeline ---
# This code assumes the classes from previous chapters are available.

# 1. Create a mock SNO. Let's imagine this is a very new, slightly underdeveloped idea.
#    We will manually set the scores each critic *would* produce for demonstration.
class MockCritic(BaseCritic):
    def __init__(self, critic_type, weight, mock_score):
        super().__init__(critic_type, weight)
        self.mock_score = mock_score
    def evaluate(self, sno, context=None):
        return CriticResult(score=self.mock_score, confidence=1.0, explanation="Mocked result", evidence={}, sub_scores={})

# Our SNO is very novel (0.9) but has weak logic (0.4) and grounding (0.5)
mock_novelty_critic = MockCritic(CriticType.NOVELTY, 1.0, 0.9)
mock_logic_critic = MockCritic(CriticType.LOGIC, 1.0, 0.4)
mock_grounding_critic = MockCritic(CriticType.GROUNDING, 1.0, 0.5)

# Create the pipeline
pipeline = CriticPipeline()
pipeline.add_critic(mock_novelty_critic)
pipeline.add_critic(mock_logic_critic)
pipeline.add_critic(mock_grounding_critic)

# A dummy SNO object to pass to the pipeline
sample_sno = StructuredNarrativeObject(central_hypothesis="A sample SNO for testing.")

# --- Phase 1: Exploration Mode ---
# We want to find new ideas, so we heavily weight novelty.
print("--- EVALUATING IN EXPLORATION MODE ---")
pipeline.adjust_weights({
    CriticType.NOVELTY: 0.8,   # High weight for new ideas
    CriticType.LOGIC: 0.1,
    CriticType.GROUNDING: 0.1
})
exploration_result = pipeline.evaluate_sno(sample_sno, {})
print(f"Weights: {exploration_result['weights_used']}")
print(f"Novelty Score: {mock_novelty_critic.mock_score}, Logic Score: {mock_logic_critic.mock_score}, Grounding Score: {mock_grounding_critic.mock_score}")
print(f"Final Trust Score (Exploration): {exploration_result['trust_score']:.4f}\n")
# Expected: (0.9*0.8 + 0.4*0.1 + 0.5*0.1) / (0.8+0.1+0.1) = 0.81

# --- Phase 2: Verification Mode ---
# Now, we shift to rigorously checking our ideas.
print("--- EVALUATING IN VERIFICATION MODE ---")
pipeline.adjust_weights({
    CriticType.NOVELTY: 0.1,    # Low weight for novelty
    CriticType.LOGIC: 0.45,     # High weight for logical soundness
    CriticType.GROUNDING: 0.45  # High weight for evidential support
})
verification_result = pipeline.evaluate_sno(sample_sno, {})
print(f"Weights: {verification_result['weights_used']}")
print(f"Novelty Score: {mock_novelty_critic.mock_score}, Logic Score: {mock_logic_critic.mock_score}, Grounding Score: {mock_grounding_critic.mock_score}")
print(f"Final Trust Score (Verification): {verification_result['trust_score']:.4f}\n")
# Expected: (0.9*0.1 + 0.4*0.45 + 0.5*0.45) / (0.1+0.45+0.45) = 0.495
```

As the output clearly shows, the **same SNO** is considered high-trust (`0.81`) in exploration mode but fails to meet the quality bar (`0.495`) in verification mode. This ability to programmatically shift the system's "values" is not just a theoretical feature but a practical tool for guiding the knowledge discovery process, making CNS 2.0 a powerful and flexible framework.
