---
title: "Chapter 3: The Multi-Component Critic Pipeline"
description: "Implementing transparent evaluation systems for grounding, logic, and novelty assessment"
weight: 3
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 3: The Multi-Component Critic Pipeline

## The Problem with Black-Box Evaluation

Many AI systems use opaque "oracle" critics that provide scores without explanation. CNS 2.0 rejects this approach, instead decomposing evaluation into a transparent, auditable pipeline of specialized components. Each critic assesses a distinct aspect of narrative quality, making the final `Trust Score` understandable and debuggable.

The Multi-Component Critic Pipeline consists of three specialized critics:

1.  **Grounding Critic**: How well is the narrative supported by evidence?
2.  **Logic Critic**: Is the argument structurally and logically coherent?
3.  **Novelty-Parsimony Critic**: Does the narrative offer a new, simple explanation?

### The Mathematical Foundation: Weighted Averaging

The final `Trust Score` emerges from a weighted combination of the individual critic scores, as defined by Equation (1) in Section 2.2 of the paper.

> **From the Paper (Equation 1):**

$$
\text{Reward}(\mathcal{S}) = \sum_{i \in \{G, L, N\}} w_i \cdot \text{Score}_i(\mathcal{S})
$$

> where $w_i$ are dynamically adjustable weights for the Grounding, Logic, and Novelty-Parsimony critics.

Our `CriticPipeline` class directly implements this formula. It iterates through each critic, calculates its score, applies the corresponding weight $w_i$, and normalizes the result to produce the final `Trust Score`.

## Implementing the Critic Infrastructure

First, we define the basic infrastructure: a `BaseCritic` abstract class, `CriticResult` dataclasses for structured output, and the `CriticPipeline` orchestrator.

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
# Assume StructuredNarrativeObject is available from Chapter 2

@dataclass
class CriticResult:
    """A structured result from a single critic evaluation, ensuring transparency."""
    score: float
    confidence: float
    explanation: str
    # evidence can store any data that supports the explanation, e.g., claim-level scores
    evidence: Dict[str, Any] = field(default_factory=dict)
    sub_scores: Dict[str, float] = field(default_factory=dict)

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
```

## 1. Grounding Critic

The Grounding Critic ensures that narratives remain tethered to verifiable facts by evaluating how well claims are supported by evidence.

> **From the Paper (Section 2.2):**

$$ \text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e) $$

> where $p(v|e)$ is the plausibility of a claim $v$ given evidence $e$.

#### Formula Breakdown: `Score_G`
This formula calculates the average "best possible support" for all claims in a narrative. Let's break it down from inside out:
-   **`p(v|e)`**: This is the core judgment: "Given this piece of evidence `e`, how plausible is claim `v`?" We use a Natural Language Inference (NLI) model to calculate this, where `p(v|e)` is the model's confidence in the "entailment" relationship.
-   **`max_{e \in E}`**: For each individual claim `v`, we loop through *all* available evidence in the set `E` and find the *single best piece of evidence* that supports it. A claim only needs one strong piece of evidence to be considered well-supported.
-   **`∑_{v \in V}`**: We sum up these "maximum plausibility" scores for every claim `v` in the reasoning graph's vertex set `V`.
-   **`1/|V|`**: Finally, we average the total score by dividing by the number of claims. This ensures that SNOs with many claims aren't unfairly advantaged or disadvantaged.

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

## 2. Logic Critic

The Logic Critic assesses the structural coherence of the reasoning graph $G$. A narrative can have well-grounded claims but still be logically flawed.

> **From the Paper (Section 2.2):**
> The ideal Logic Score is produced by a Graph Neural Network (GNN):
> $$ \text{Score}_L = f_{\text{GNN}}(G; \theta) $$
> Training a full GNN is a major research project. For our implementation, we create a **functional proxy** for $f_{\text{GNN}}$ that uses graph-theoretic heuristics to approximate logical coherence.

#### Formula Breakdown: `Score_L` (Heuristic Proxy)
Our heuristic-based `LogicCritic` uses a weighted average of three metrics to approximate what a trained GNN would learn:
-   **Orphan Score (Penalty for unsupported claims)**: Checks for claims that are not supported by any other claim. A high number of orphans suggests a collection of disconnected assertions, not a coherent argument.
-   **Coherence Score (Penalty for unfocused claims)**: Penalizes claims that are used to support too many other, potentially unrelated, points.
-   **Parsimony Score (Penalty for complexity)**: Rewards simplicity (Occam's Razor) by penalizing overly dense, "spaghetti-like" argument graphs.

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

#### Roadmap to a GNN-based Logic Critic
While our heuristic is a robust start, a GNN-based critic is the ultimate goal. Here is a more concrete roadmap, including a conceptual code skeleton.

**1. Data Collection & Labeling**: This is the most critical step. You need a dataset of thousands of reasoning graphs (`networkx.DiGraph` objects), each labeled with a "logical coherence" score. This typically requires multiple human experts to rate each graph, with the average score serving as the ground truth label.

**2. Feature Engineering**: GNNs operate on numerical tensors. You must convert the graph's components into vectors:
-   **Node Features**: A vector for each claim. This would primarily be the semantic embedding of the claim's text, but could also include one-hot encodings for `claim_type`.
-   **Edge Features**: A vector for each relationship. This could be a one-hot encoding of the `RelationType` enum and the numerical `strength`.

**3. GNN Model Architecture (PyTorch Skeleton)**: You can use libraries like `PyTorch Geometric` to build a GNN model. A Graph Attention Network (GAT) is a strong candidate because it can learn to weigh the importance of different relationships.

```python
# NOTE: This is a non-runnable conceptual skeleton.
# It requires PyTorch, PyTorch Geometric, and a labeled dataset to run.
import torch
import torch.nn.functional as F
from torch_geometric.nn import GATConv, global_mean_pool

class GNNLogicCriticModel(torch.nn.Module):
    """A conceptual GNN model to predict a graph's logical coherence."""
    def __init__(self, num_node_features, num_edge_features):
        super().__init__()
        # Graph Attention Network layers are well-suited for this task.
        self.conv1 = GATConv(num_node_features, 64, heads=4, dropout=0.5)
        self.conv2 = GATConv(64 * 4, 128, heads=4, dropout=0.5)

        # A final layer to predict a single score for the entire graph.
        self.output_layer = torch.nn.Linear(128 * 4, 1)

    def forward(self, data):
        x, edge_index, edge_attr = data.x, data.edge_index, data.edge_attr

        # Pass through GAT layers
        x = F.dropout(x, p=0.5, training=self.training)
        x = F.elu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.5, training=self.training)
        x = F.elu(self.conv2(x, edge_index))

        # Pool node features to get a single vector for the whole graph.
        graph_embedding = global_mean_pool(x, data.batch)

        # Predict the final score (a value between 0 and 1).
        return torch.sigmoid(self.output_layer(graph_embedding))

# --- Conceptual Training Loop ---
def train_gnn_critic(model, train_loader, optimizer, loss_fn):
    model.train()
    for data in train_loader: # train_loader yields batches of graph data
        optimizer.zero_grad()
        predicted_score = model(data)
        true_score = data.y # The human-labeled scores
        loss = loss_fn(predicted_score, true_score)
        loss.backward()
        optimizer.step()
```

**4. Training**: The GNN is trained on a **graph regression** task. The model's goal is to minimize the difference (e.g., Mean Squared Error) between its predicted score and the human-labeled score. By completing this process, you create a powerful, data-driven model of logical coherence.

## 3. Novelty-Parsimony Critic

This critic balances two competing virtues: the desire for new ideas (novelty) and the principle of simplicity (parsimony).

> **From the Paper (Section 2.2):**
> $$ \text{Score}_N = \alpha \cdot \min_i \|H - H_i\|_2 - \beta \cdot \frac{|E_G|}{|V|} $$

#### Formula Breakdown: `Score_N`
This formula is a simple linear combination of a reward and a penalty:
-   **`α * min_i ||H - H_i||₂`**: This is the **novelty reward**.
    -   `||H - H_i||₂`: The Euclidean distance between the current SNO's embedding (`H`) and the embedding of another SNO (`H_i`) in the population. A larger distance means the ideas are further apart, or more "novel."
    -   `min_i`: We find the distance to the *closest* (most similar) SNO in the entire population. This measures how much of a leap the new idea is making from the most related existing idea.
    -   `α`: The alpha parameter is a weight that lets us control how much we care about novelty. A high `α` encourages more exploratory, "out-there" ideas.
-   **`- β * (|E_G| / |V|)`**: This is the **parsimony penalty**.
    -   `|E_G| / |V|`: The ratio of edges to nodes in the reasoning graph. This is a simple measure of graph complexity or density.
    -   `β`: The beta parameter weights this penalty. A high `β` strongly encourages simpler, more elegant arguments (Occam's Razor).

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

A key feature of CNS 2.0 is its adaptability. By adjusting the weights $w_i$ in the main reward formula, we can change the system's "priorities." For example, during an initial "exploration" phase, we might heavily weight novelty. During a later "verification" phase, we would shift the weights to prioritize grounding and logic.

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

This ability to programmatically shift the system's "values" is a practical tool for guiding the knowledge discovery process, making CNS 2.0 a powerful and flexible framework.
