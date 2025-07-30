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
> $$
> \text{Reward}(\mathcal{S}) = \sum_{i \in \{G, L, N\}} w_i \cdot \text{Score}_i(\mathcal{S})
> $$
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
# ... (standard imports like ABC, abstractmethod, typing, etc.) ...
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

# ... (BaseCritic and CriticPipeline class implementations remain the same) ...
```

## 1. Grounding Critic

The Grounding Critic ensures that narratives remain tethered to verifiable facts by evaluating how well claims are supported by evidence.

> **From the Paper (Section 2.2):**
> $$ \text{Score}_G = \frac{1}{|V|}\sum_{v \in V} \max_{e \in \mathcal{E}} p(v|e) $$
> where $p(v|e)$ is the plausibility of a claim $v$ given evidence $e$.

#### Formula Breakdown: `Score_G`
This formula calculates the average "best possible support" for all claims in a narrative. Let's break it down from inside out:
-   **`p(v|e)`**: This is the core judgment: "Given this piece of evidence `e`, how plausible is claim `v`?" We use a Natural Language Inference (NLI) model to calculate this, where `p(v|e)` is the model's confidence in the "entailment" relationship.
-   **`max_{e \in E}`**: For each individual claim `v`, we loop through *all* available evidence in the set `E` and find the *single best piece of evidence* that supports it. A claim only needs one strong piece of evidence to be considered well-supported.
-   **`∑_{v \in V}`**: We sum up these "maximum plausibility" scores for every claim `v` in the reasoning graph's vertex set `V`.
-   **`1/|V|`**: Finally, we average the total score by dividing by the number of claims. This ensures that SNOs with many claims aren't unfairly advantaged or disadvantaged.

```python
class GroundingCritic(BaseCritic):
    # ... (implementation remains the same as in the original file) ...
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
    # ... (implementation remains the same as in the original file) ...
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
    # ... (implementation remains the same as in the original file) ...
```

## Contextual Evaluation: Dynamic Weight Adjustment

A key feature of CNS 2.0 is its adaptability. By adjusting the weights $w_i$ in the main reward formula, we can change the system's "priorities." For example, during an initial "exploration" phase, we might heavily weight novelty. During a later "verification" phase, we would shift the weights to prioritize grounding and logic.

### Scenario: Shifting from Exploration to Verification
(The example code and explanation for this section remain the same as they are already clear and effective.)
```python
# ... (mock critic setup and evaluation scenarios) ...
```
This ability to programmatically shift the system's "values" is a practical tool for guiding the knowledge discovery process, making CNS 2.0 a powerful and flexible framework.
