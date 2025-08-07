---
title: "Chapter 3: The Multi-Component Critic Pipeline"
description: "Implementing transparent evaluation systems for grounding, logic, and novelty assessment"
meta_keywords: "AI critic pipeline, narrative evaluation AI, grounding critic, logic critic, novelty critic"
weight: 3
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

## Why a Multi-Component Critic? The Problem with "Oracles"

Many AI systems rely on opaque, monolithic "oracle" models for evaluation. These models produce a score but offer no insight into their reasoning, making them difficult to debug, trust, or adapt. If an oracle gives a low score, is it because the input was factually wrong, illogical, or simply unoriginal? It's impossible to know.

CNS 2.0 explicitly rejects this "black box" approach. Instead, it decomposes evaluation into a **transparent, auditable pipeline of specialized critics**. This design choice is fundamental and provides several key advantages:

-   **Transparency & Debuggability**: By separating evaluation into components—Grounding, Logic, and Novelty—we can pinpoint the exact strengths and weaknesses of a narrative. A low score from the `LogicCritic` tells us to examine the argument's structure, while a low score from the `GroundingCritic` points to a lack of evidence.
-   **Adaptability**: The system's "values" can be dynamically adjusted. By changing the weights assigned to each critic, we can shift the system's focus. In an exploratory phase, we might prioritize novelty. In a verification phase, we would prioritize grounding and logic.
-   **Explainability**: The final `Trust Score` is not a mystery. It can be explained as a weighted combination of clear, understandable criteria, making the entire system more trustworthy and interpretable.

### The Mathematical Foundation: Weighted Averaging

The final `Trust Score` emerges from a weighted combination of the individual critic scores, as defined by Equation (1) in Section 2.2 of the paper. This formula is the heart of the pipeline's adaptability.

> **From the Paper (Equation 1):**
> $$\text{Reward}(\mathcal{S}) = \sum_{i \in \{G, L, N\}} w_i \cdot \text{Score}_i(\mathcal{S})$$
> where $w_i$ are dynamically adjustable weights for the Grounding, Logic, and Novelty-Parsimony critics.

Our `CriticPipeline` class directly implements this formula. It iterates through each registered critic, calculates its score, applies the corresponding weight $w_i$, and normalizes the result to produce the final `Trust Score`.

## Implementing the Critic Infrastructure

First, we define the basic infrastructure: a `BaseCritic` abstract class to ensure all critics have a standard interface, a `CriticResult` dataclass for structured and explainable output, and the `CriticPipeline` orchestrator.

```python
"""
Multi-Component Critic Pipeline Implementation
============================================
Transparent, auditable evaluation of SNO quality
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Optional, Any
import numpy as np
from dataclasses import dataclass, field
from enum import Enum
# Assume StructuredNarrativeObject is available from Chapter 2 and HAS_TRANSFORMERS is defined

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
    """Abstract base class for all CNS 2.0 critics, ensuring a consistent interface."""
    
    def __init__(self, critic_type: CriticType, weight: float = 1.0):
        self.critic_type = critic_type
        self.weight = weight
        self.evaluation_count = 0
        self.performance_history = []
    
    @abstractmethod
    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        """The core method for any critic. Must be implemented by subclasses."""
        pass
    
    def update_weight(self, new_weight: float):
        """Allows for dynamic adjustment of the critic's importance in the pipeline."""
        self.weight = new_weight
    
    def get_statistics(self) -> Dict[str, Any]:
        """Provides performance metrics for monitoring."""
        return {
            'type': self.critic_type.value,
            'weight': self.weight,
            'evaluations': self.evaluation_count,
            'avg_score': np.mean([r['score'] for r in self.performance_history]) if self.performance_history else 0.0,
        }

class CriticPipeline:
    """Orchestrates multiple critics to produce a comprehensive SNO evaluation."""
    
    def __init__(self):
        self.critics: Dict[CriticType, BaseCritic] = {}
        self.evaluation_history = []
    
    def add_critic(self, critic: BaseCritic):
        """Registers a critic with the pipeline."""
        self.critics[critic.critic_type] = critic
    
    def evaluate_sno(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Evaluates an SNO by running it through all registered critics and computing
        the final weighted Trust Score, directly implementing the paper's Reward formula.
        """
        results = {}
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for critic_type, critic in self.critics.items():
            result = critic.evaluate(sno, context)
            results[critic_type.value] = result
            # This is the core of the formula: score * weight
            total_weighted_score += result.score * critic.weight
            total_weight += critic.weight
            critic.performance_history.append({'score': result.score, 'confidence': result.confidence})
            critic.evaluation_count += 1
        
        # Normalize by the sum of weights to get the final score
        trust_score = total_weighted_score / total_weight if total_weight > 0 else 0.0
        sno.trust_score = trust_score
        
        evaluation_result = {
            'trust_score': trust_score,
            'critic_results': {k: v.to_dict() for k, v in results.items()}, # Assuming CriticResult has to_dict
            'weights_used': {ct.value: c.weight for ct, c in self.critics.items()},
        }
        self.evaluation_history.append(evaluation_result)
        return evaluation_result
    
    def adjust_weights(self, weight_updates: Dict[CriticType, float]):
        """Dynamically adjusts the weights of the critics."""
        for critic_type, new_weight in weight_updates.items():
            if critic_type in self.critics:
                self.critics[critic_type].update_weight(new_weight)
```

## 1. Grounding Critic

The Grounding Critic ensures that narratives remain tethered to verifiable facts by evaluating how well claims are supported by the provided evidence.

> **From the Paper (Section 2.2):**
> $$ \text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e) $$
> where $p(v|e)$ is the plausibility of a claim $v$ given evidence $e$, computed using a Natural Language Inference (NLI) model.

#### Formula Breakdown: `Score_G`
This formula calculates the average "best possible support" for all claims in a narrative. Let's break it down from inside out:
-   **`p(v|e)`**: This is the core judgment: "Given this piece of evidence `e`, how plausible is claim `v`?" We use a Natural Language Inference (NLI) model to calculate this, where `p(v|e)` is the model's confidence in the "entailment" relationship between the evidence (premise) and the claim (hypothesis).
-   **`max_{e \in E}`**: For each individual claim `v`, we loop through *all* available evidence in the set `E` and find the *single best piece of evidence* that supports it. A claim only needs one strong piece of evidence to be considered well-supported.
-   **`∑_{v \in V}`**: We sum up these "maximum plausibility" scores for every claim `v` in the reasoning graph's vertex set `V`.
-   **`1/|V|`**: Finally, we average the total score by dividing by the number of claims. This ensures that SNOs with many claims aren't unfairly advantaged or disadvantaged.

```python
class GroundingCritic(BaseCritic):
    def __init__(self, weight: float, nli_model=None, nli_tokenizer=None, nli_model_name: str = "roberta-large-mnli"):
        super().__init__(CriticType.GROUNDING, weight)
        if nli_model and nli_tokenizer:
            self.nli_model, self.nli_tokenizer = nli_model, nli_tokenizer
        elif HAS_TRANSFORMERS:
            import transformers
            self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(nli_model_name)
            self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(nli_model_name)
        else:
            raise ImportError("Transformers library is required for the GroundingCritic.")
        # Find the index for the 'entailment' label in the model's configuration
        self.entailment_id = self.nli_model.config.label2id.get('entailment', 2)

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        claims = [data['claim'] for _, data in sno.reasoning_graph.nodes(data=True)]
        evidence_contents = [item.content for item in sno.evidence_set]
        
        if not claims or not evidence_contents:
            return CriticResult(0.0, 1.0, "SNO has no claims or no evidence to evaluate.", {}, {})

        total_max_plausibility, sub_scores = 0.0, {}
        # This outer loop corresponds to the Σ[v ∈ V] part of the formula
        for claim in claims:
            # Prepare (evidence, claim) pairs to calculate p(v|e) for all e ∈ E at once
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
> The ideal Logic Score is produced by a Graph Neural Network (GNN) trained to detect logical weaknesses:
> $$ \text{Score}_L = f_{\text{GNN}}(G; \theta) $$
> Training a full GNN is a major research project. For our implementation, we create a **functional heuristic proxy** for $f_{\text{GNN}}$ that uses graph-theoretic metrics to approximate logical coherence.
>
> > For a deep-dive into the state-of-the-art approach, see the research project on **[GNNs for Logical Reasoning](/guides/cns-2.0-research-roadmap/technical-research/1-gnn-for-logical-reasoning/)**.

#### `Score_L` (Heuristic Proxy)
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
        # An orphan is a node with no incoming edges, excluding the root hypothesis.
        orphaned_nodes = [n for n, d in G.in_degree() if d == 0 and n != 'root']
        orphan_penalty = len(orphaned_nodes) / (num_nodes - 1) if num_nodes > 1 else 0
        orphan_score = 1.0 - orphan_penalty
        
        # Heuristic 2: Penalize unfocused claims (a single claim supporting too many others)
        avg_out_degree = sum(d for _, d in G.out_degree()) / num_nodes
        # Penalize if the average claim supports more than 3 others. This is a simple heuristic.
        coherence_score = max(0, 1.0 - (avg_out_degree / 3.0))

        # Heuristic 3: Penalize complexity (convoluted, "spaghetti" arguments) using graph density
        density = nx.density(G)
        parsimony_score = 1.0 - density

        # Our functional proxy for f_GNN is a weighted average of these heuristics.
        # These weights are internal to the critic and can be tuned.
        final_score = 0.5 * orphan_score + 0.3 * coherence_score + 0.2 * parsimony_score
        sub_scores = {'orphan_score': orphan_score, 'coherence_score': coherence_score, 'parsimony_score': parsimony_score}

        return CriticResult(
            score=final_score, confidence=0.9,
            explanation=f"Logic score based on graph structure heuristics: {final_score:.3f}",
            evidence={'num_orphans': len(orphaned_nodes), 'avg_out_degree': avg_out_degree, 'density': density},
            sub_scores=sub_scores
        )
```

## 3. Novelty-Parsimony Critic

This critic balances two competing virtues: the desire for new ideas (**novelty**) and the principle of simplicity (**parsimony**), also known as Occam's Razor.

> **From the Paper (Section 2.2):**
> $$ \text{Score}_N = \alpha \cdot \min_i \|H - H_i\|_2 - \beta \cdot \frac{|E_G|}{|V|} $$

#### Formula Breakdown: `Score_N`
This formula is a simple linear combination of a reward and a penalty:
-   **`α * min_i ||H - H_i||₂`**: This is the **novelty reward**.
    -   `||H - H_i||₂`: The Euclidean distance between the current SNO's embedding (`H`) and the embedding of another SNO (`H_i`) in the population. A larger distance means the ideas are further apart, or more "novel."
    -   `min_i`: We find the distance to the *closest* (most similar) SNO in the entire population. This measures how much of a leap the new idea is making from the most related existing idea.
    -   `α`: The alpha parameter is a weight that lets us control how much we care about novelty. A high `α` encourages more exploratory, "out-there" ideas.
-   **`- β * (|E_G| / |V|)`**: This is the **parsimony penalty**.
    -   `|E_G| / |V|`: The ratio of edges to nodes in the reasoning graph. This is a simple measure of graph complexity or density. An argument with 10 claims and 30 relationships is more complex than one with 10 claims and 9 relationships.
    -   `β`: The beta parameter weights this penalty. A high `β` strongly encourages simpler, more elegant arguments.

```python
class NoveltyParsimonyCritic(BaseCritic):
    def __init__(self, weight: float, alpha: float, beta: float):
        super().__init__(CriticType.NOVELTY, weight)
        self.alpha = alpha
        self.beta = beta

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        context = context or {}
        sno_population = context.get('sno_population', [])
        population_embeddings = [s.hypothesis_embedding for s in sno_population if s.sno_id != sno.sno_id and s.hypothesis_embedding is not None]
        
        # --- Novelty Term Calculation ---
        if not population_embeddings or sno.hypothesis_embedding is None:
            # If this is the first SNO, it is maximally novel by definition.
            novelty_score = 1.0
            min_dist_str = "N/A (first SNO)"
        else:
            # Corresponds to the ||H - H_i||₂ part of the formula
            distances = [np.linalg.norm(sno.hypothesis_embedding - h) for h in population_embeddings]
            # Corresponds to the min_i part of the formula
            min_distance = min(distances) if distances else 0
            # Normalize the distance. Max possible distance for normalized vectors is 2.0.
            novelty_score = min_distance / 2.0
            min_dist_str = f"{min_distance:.3f}"

        novelty_term = self.alpha * novelty_score

        # --- Parsimony Term Calculation ---
        G = sno.reasoning_graph
        num_nodes = G.number_of_nodes()
        # Corresponds to the |E_G|/|V| part of the formula
        complexity_ratio = G.number_of_edges() / num_nodes if num_nodes > 0 else 0
        # Normalize penalty (assuming max complexity ratio is around 5 for a reasonable argument graph)
        parsimony_penalty = self.beta * min(1.0, complexity_ratio / 5.0)

        # Combine terms and clamp the final score to the valid [0, 1] range.
        raw_score = novelty_term - parsimony_penalty
        final_score = np.clip(raw_score, 0, 1)

        explanation = f"Score({final_score:.3f}) = α*Novelty({novelty_term:.3f}) - β*Parsimony({parsimony_penalty:.3f}). Min dist: {min_dist_str}."
        return CriticResult(
            score=final_score, confidence=0.9, explanation=explanation,
            evidence={'novelty_term': novelty_term, 'parsimony_penalty': parsimony_penalty},
            sub_scores={'novelty_score': novelty_score, 'complexity_ratio': complexity_ratio}
        )
```



### Roadmap to a GNN-based Logic Critic

The heuristic-based `LogicCritic` is a functional and transparent starting point. However, the research proposal correctly identifies that a **Graph Neural Network (GNN)** is the state-of-the-art solution.

**Why a GNN is the Next Step:**
Hand-coded heuristics can only capture simple structural flaws. A GNN, in contrast, can *learn* subtle, complex, and non-local patterns of faulty reasoning directly from data. By training on a dataset of valid and fallacious argument graphs, a GNN can learn to identify sophisticated weaknesses like:
-   **Missing Warrants**: Implicit logical leaps between claims.
-   **Fallacies of Relevance**: Arguments where the support is only superficially related to the conclusion.
-   **Complex Circular Reasoning**: Logical loops that span multiple nodes and are hard to detect with simple cycle checks.

A GNN-based critic moves from a "rules-based" system to a "learning-based" system, dramatically increasing the sophistication and accuracy of the logic evaluation.

**Conceptual GNN Implementation (PyTorch & PyG):**
Below is a conceptual skeleton of what a GNN-based `LogicCritic` might look like using PyTorch and the PyTorch Geometric (`PyG`) library, which is specialized for GNNs.

```python
# You would need to install: pip install torch torch-geometric
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool
from torch_geometric.data import Data

class GNNLogicModel(torch.nn.Module):
    """A simple Graph Convolutional Network (GCN) for graph classification."""
    def __init__(self, num_node_features, hidden_channels):
        super().__init__()
        self.conv1 = GCNConv(num_node_features, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        # A linear layer for the final graph-level classification
        self.lin = torch.nn.Linear(hidden_channels, 1)

    def forward(self, x, edge_index, batch):
        # 1. Obtain node embeddings
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index).relu()

        # 2. Global Pooling: Aggregate node features to get a graph-level embedding
        x = global_mean_pool(x, batch)

        # 3. Apply a final classifier to get a single score for the graph
        x = self.lin(x)

        # Apply sigmoid to get a score between 0 and 1
        return torch.sigmoid(x)

def convert_sno_to_graph_data(sno: StructuredNarrativeObject, embedding_model) -> Data:
    """Converts our NetworkX graph into a PyG Data object for the GNN."""
    G = sno.reasoning_graph

    # Create node features (e.g., from claim embeddings)
    node_features = []
    node_map = {node_id: i for i, node_id in enumerate(G.nodes())}
    for node_id in G.nodes():
        claim_content = G.nodes[node_id]['claim'].content
        # In a real implementation, you'd use pre-computed embeddings
        embedding = embedding_model.encode(claim_content)
        node_features.append(embedding)

    x = torch.tensor(np.array(node_features), dtype=torch.float)

    # Create edge index
    edge_list = [[node_map[u], node_map[v]] for u, v in G.edges()]
    edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()

    return Data(x=x, edge_index=edge_index)

# --- Conceptual Training Loop ---
# This would not run in the guide, but shows the process.
def train_gnn_critic(model, train_loader, optimizer, criterion):
    model.train()
    for data in train_loader: # train_loader yields batches of graph Data objects
        optimizer.zero_grad()
        out = model(data.x, data.edge_index, data.batch)
        # `data.y` would be the ground-truth label (0 for fallacious, 1 for valid)
        loss = criterion(out, data.y.unsqueeze(1).float())
        loss.backward()
        optimizer.step()

# --- The GNN-based Critic Class ---
class GNNLogicCritic(BaseCritic):
    def __init__(self, weight: float, model_path: str, embedding_model):
        super().__init__(CriticType.LOGIC, weight)
        self.model = GNNLogicModel(num_node_features=768, hidden_channels=64) # Example dimensions
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval() # Set model to evaluation mode
        self.embedding_model = embedding_model

    def evaluate(self, sno: StructuredNarrativeObject, context: Optional[Dict] = None) -> CriticResult:
        graph_data = convert_sno_to_graph_data(sno, self.embedding_model)

        with torch.no_grad():
            score = self.model(graph_data.x, graph_data.edge_index, torch.zeros(graph_data.num_nodes, dtype=torch.long)).item()

        return CriticResult(
            score=score,
            confidence=0.95, # Assuming a well-trained model
            explanation=f"GNN-based logical coherence score: {score:.3f}"
        )
```

This roadmap illustrates the clear, principled path from our initial heuristic-based critic to a much more powerful, learned system, which is a core theme of the CNS 2.0 research philosophy.

## Contextual Evaluation: Dynamic Weight Adjustment

A key feature of CNS 2.0 is its adaptability. By adjusting the weights $w_i$ in the main reward formula, we can change the system's "priorities" to suit different phases of knowledge discovery.

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
        return CriticResult(score=self.mock_score, confidence=1.0, explanation="Mocked result")

# Our SNO is very novel (0.9) but has weak logic (0.4) and grounding (0.5)
pipeline = CriticPipeline()
pipeline.add_critic(MockCritic(CriticType.NOVELTY, 1.0, 0.9))
pipeline.add_critic(MockCritic(CriticType.LOGIC, 1.0, 0.4))
pipeline.add_critic(MockCritic(CriticType.GROUNDING, 1.0, 0.5))
sample_sno = StructuredNarrativeObject(central_hypothesis="A sample SNO for testing.")

# --- Phase 1: Exploration Mode ---
# We want to find new ideas, so we heavily weight novelty.
print("--- EVALUATING IN EXPLORATION MODE ---")
pipeline.adjust_weights({
    CriticType.NOVELTY: 0.8,   # High weight for new ideas
    CriticType.LOGIC: 0.1,     # Low weight for rigor
    CriticType.GROUNDING: 0.1  # Low weight for rigor
})
exploration_result = pipeline.evaluate_sno(sample_sno)
print(f"Final Trust Score (Exploration): {exploration_result['trust_score']:.4f}\n")

# --- Phase 2: Verification Mode ---
# Now, we shift to rigorously checking our ideas.
print("--- EVALUATING IN VERIFICATION MODE ---")
pipeline.adjust_weights({
    CriticType.NOVELTY: 0.1,    # Low weight for novelty
    CriticType.LOGIC: 0.45,     # High weight for logical soundness
    CriticType.GROUNDING: 0.45  # High weight for evidential support
})
verification_result = pipeline.evaluate_sno(sample_sno)
print(f"Final Trust Score (Verification): {verification_result['trust_score']:.4f}\n")
```

As the output shows, the **same SNO** is considered high-trust in exploration mode but fails the quality bar in verification mode. This ability to programmatically shift the system's "values" is a practical tool for guiding the knowledge discovery process, making CNS 2.0 a powerful and flexible framework.
