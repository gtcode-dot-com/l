---
title: "Chapter 2: SNO Foundations"
description: "Building Structured Narrative Objects - the core data structure of CNS 2.0"
weight: 2
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 2: SNO Foundations

## Understanding Structured Narrative Objects

Structured Narrative Objects (SNOs) are the heart of CNS 2.0. Unlike simple vector representations that lose critical structural information, SNOs preserve the full richness of argumentative structure while maintaining computational tractability.

An SNO is formally defined as a 4-tuple: **𝒮 = (H, G, ℰ, T)** where:

- **H**: Hypothesis Embedding (dense vector)
- **G**: Reasoning Graph (directed acyclic graph)
- **ℰ**: Evidence Set (grounding data sources)
- **T**: Trust Score (derived confidence measure)

### From Paper to Code: The Mathematical Foundation

First, let's look at the formal definition from the paper. Section 2.1 defines a Structured Narrative Object as a mathematical construct.

> **Definition 2.1 (Structured Narrative Object)**
> An SNO is a 4-tuple $\mathcal{S} = (H, G, \mathcal{E}, T)$ where:
> - **Hypothesis Embedding** $H \in \mathbb{R}^d$: A $d$-dimensional dense vector encoding the narrative's central claim.
> - **Reasoning Graph** $G = (V, E_G)$: A directed acyclic graph where vertices $V$ are sub-claims and edges $E_G$ are typed logical relationships.
> - **Evidence Set** $\mathcal{E} = \{e_1, \ldots, e_n\}$: Pointers to grounding data sources.
> - **Trust Score** $T \in [0, 1]$: A derived confidence measure computed by the critic pipeline.

**From Paper to Code:**

Our `StructuredNarrativeObject` Python class is the direct, practical implementation of this mathematical 4-tuple. Let's map the theory to our code:

- **`H` (Hypothesis Embedding):** Corresponds to `self.hypothesis_embedding`, an `np.ndarray` holding the dense vector of the central claim.
- **`G` (Reasoning Graph):** Implemented as `self.reasoning_graph`, a `networkx.DiGraph`. The paper's acyclic requirement is enforced by a check for cycles when adding edges.
- **`ℰ` (Evidence Set):** This is our `self.evidence_set`, a Python `set` of `EvidenceItem` objects.
- **`T` (Trust Score):** This is `self.trust_score`, initialized as `None` and populated later by the `CriticPipeline`.

Understanding this mapping is key. We're not just creating a data class; we're instantiating a formal mathematical object.

#### A Note on Embeddings
For mathematical primitives like the Chirality and Novelty Scores to work, we need a semantically meaningful vector space. Simple fallbacks like hash-based vectors produce random outputs that destroy any geometric meaning. Therefore, our implementation treats a real embedding model as a mandatory component.

## Core SNO Implementation

The following code block contains the complete, updated `StructuredNarrativeObject` class. We have enhanced it with more detailed comments and robust serialization methods, which we will discuss in detail.

### The Importance of Structured Graph Components

Before diving into the main class, it's important to understand *why* we use `dataclasses` like `ClaimNode` and `ReasoningEdge` to structure the components of our reasoning graph. While we could use simple dictionaries, these structured classes provide several key advantages:

-   **Type Safety**: Dataclasses enforce data types, reducing runtime errors. For example, `ReasoningEdge.strength` is explicitly a `float`, preventing accidental assignment of incorrect types.
-   **Self-Documentation**: The class definitions clearly document the expected data structure for a claim or a relationship. This makes the code easier to read, understand, and maintain.
-   **Extensibility**: If we need to add a new attribute to a claim (e.g., an author field), we can simply add it to the `ClaimNode` definition. This is much cleaner and more explicit than hoping a dictionary key is present everywhere it's used.

These design choices make our implementation more robust and scalable, which is crucial for a complex system like CNS 2.0.

```python
"""
Structured Narrative Objects (SNO) Implementation
===============================================
The foundational data structure for CNS 2.0, now with enhanced
comments and robust serialization.
"""

import numpy as np
import networkx as nx
from typing import Dict, List, Tuple, Set, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime
import uuid
import json
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Assuming RelationType and EvidenceItem are defined as in Chapter 1
# For brevity, their definitions from the previous chapter are omitted here.

@dataclass
class ReasoningEdge:
    """Represents a typed logical relationship in the reasoning graph."""
    source: str
    target: str
    relation_type: RelationType
    strength: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ClaimNode:
    """Represents a claim or sub-claim in the reasoning graph."""
    claim_id: str
    content: str
    claim_type: str = "assertion"
    embedding: Optional[np.ndarray] = field(default=None, repr=False) # Exclude large embedding from repr
    metadata: Dict[str, Any] = field(default_factory=dict)

class StructuredNarrativeObject:
    """
    Complete implementation of a Structured Narrative Object (SNO).
    This class encapsulates H, G, E, and T and includes robust
    serialization and deserialization methods.
    """
    
    def __init__(self, 
                 central_hypothesis: str,
                 sno_id: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 metadata: Optional[Dict] = None):
        """
        Initializes a new SNO.

        Args:
            central_hypothesis: The core claim of the narrative.
            sno_id: A unique identifier. If None, a new UUID is generated.
            created_at: The creation timestamp. If None, the current time is used.
            metadata: A dictionary for storing any extra information about the SNO.
        """
        self.sno_id = sno_id or str(uuid.uuid4())
        self.central_hypothesis = central_hypothesis
        self.created_at = created_at or datetime.now()
        
        # H: Hypothesis Embedding - A dense vector representing the central hypothesis.
        self.hypothesis_embedding: Optional[np.ndarray] = None
        
        # G: Reasoning Graph - A NetworkX DiGraph storing claims and their relationships.
        self.reasoning_graph = nx.DiGraph()
        
        # E: Evidence Set - A set of EvidenceItem objects grounding the narrative.
        self.evidence_set: Set[EvidenceItem] = set()
        
        # T: Trust Score - A score from [0, 1] computed by the Critic Pipeline.
        self.trust_score: Optional[float] = None
        
        self.metadata: Dict[str, Any] = metadata or {}
        
        self._add_root_claim()
    
    def _add_root_claim(self):
        """Internal method to create the root node of the graph from the central hypothesis."""
        root_node = ClaimNode(
            claim_id="root",
            content=self.central_hypothesis,
            claim_type="central_hypothesis"
        )
        self.reasoning_graph.add_node("root", claim=root_node)
    
    def add_claim(self, claim_content: str, claim_id: Optional[str] = None, claim_type: str = "assertion") -> str:
        """Adds a new claim (node) to the reasoning graph."""
        if claim_id is None:
            claim_id = f"claim_{len(self.reasoning_graph.nodes)}"
        
        claim_node = ClaimNode(claim_id=claim_id, content=claim_content, claim_type=claim_type)
        self.reasoning_graph.add_node(claim_id, claim=claim_node)
        return claim_id
    
    def add_reasoning_edge(self, source_claim_id: str, target_claim_id: str, relation_type: RelationType, strength: float = 1.0) -> bool:
        """Adds a new reasoning edge (relationship) between claims, ensuring no cycles are created."""
        if (source_claim_id not in self.reasoning_graph.nodes or target_claim_id not in self.reasoning_graph.nodes):
            logging.warning(f"Attempted to create edge with non-existent node: {source_claim_id} or {target_claim_id}")
            return False
        
        # Prevent creating cycles, which would invalidate the logical structure.
        if nx.has_path(self.reasoning_graph, target_claim_id, source_claim_id):
            raise ValueError(f"Adding edge from {source_claim_id} to {target_claim_id} would create a cycle.")
        
        edge = ReasoningEdge(source=source_claim_id, target=target_claim_id, relation_type=relation_type, strength=strength)
        self.reasoning_graph.add_edge(source_claim_id, target_claim_id, reasoning_edge=edge)
        return True
    
    def add_evidence(self, evidence_item: EvidenceItem):
        """Adds a piece of evidence to the SNO's evidence set."""
        self.evidence_set.add(evidence_item)
    
    def compute_hypothesis_embedding(self, embedding_model):
        """Computes and stores the vector embedding for the central hypothesis."""
        self.hypothesis_embedding = embedding_model.encode(self.central_hypothesis)
    
    def get_graph_statistics(self) -> Dict[str, Any]:
        """Calculates key statistics about the reasoning graph's structure."""
        if self.reasoning_graph.number_of_nodes() == 0:
            return {'num_nodes': 0, 'num_edges': 0, 'is_acyclic': True, 'density': 0, 'relation_type_counts': {}}

        stats = {
            'num_nodes': self.reasoning_graph.number_of_nodes(),
            'num_edges': self.reasoning_graph.number_of_edges(),
            'is_acyclic': nx.is_directed_acyclic_graph(self.reasoning_graph),
            'density': nx.density(self.reasoning_graph),
            'relation_type_counts': {}
        }
        for _, _, edge_data in self.reasoning_graph.edges(data=True):
            if 'reasoning_edge' in edge_data:
                rel_type = edge_data['reasoning_edge'].relation_type.value
                stats['relation_type_counts'][rel_type] = stats['relation_type_counts'].get(rel_type, 0) + 1
        return stats

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the SNO to a JSON-compatible dictionary.
        This method carefully handles complex types like NumPy arrays, datetimes,
        and NetworkX graphs to ensure clean serialization.
        """
        # Convert graph to a serializable format, ensuring dataclasses are converted to dicts
        serializable_graph = nx.node_link_data(self.reasoning_graph)
        for node in serializable_graph.get('nodes', []):
            if 'claim' in node and hasattr(node['claim'], '__dict__'):
                node['claim'] = asdict(node['claim'])
        for link in serializable_graph.get('links', []):
            if 'reasoning_edge' in link and hasattr(link['reasoning_edge'], '__dict__'):
                link['reasoning_edge'] = asdict(link['reasoning_edge'])

        return {
            'sno_id': self.sno_id,
            'central_hypothesis': self.central_hypothesis,
            'created_at': self.created_at.isoformat(),
            'hypothesis_embedding': self.hypothesis_embedding.tolist() if self.hypothesis_embedding is not None else None,
            'reasoning_graph': serializable_graph,
            'evidence_set': [asdict(e) for e in self.evidence_set],
            'trust_score': self.trust_score,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StructuredNarrativeObject':
        """
        Deserializes an SNO from a dictionary with robust error handling.
        This method safely reconstructs an SNO, validating key fields and
        handling potential malformations in the input data.
        """
        try:
            sno = cls(
                central_hypothesis=data['central_hypothesis'],
                sno_id=data['sno_id'],
                created_at=datetime.fromisoformat(data['created_at']),
                metadata=data.get('metadata', {})
            )

            if data.get('hypothesis_embedding') is not None:
                sno.hypothesis_embedding = np.array(data['hypothesis_embedding'])

            # Reconstruct the graph and its structured data
            graph_data = data.get('reasoning_graph', {})
            # NetworkX's node_link_graph can't automatically re-instantiate our dataclasses,
            # so we do it manually for robustness.
            sno.reasoning_graph = nx.DiGraph()
            for node_data in graph_data.get('nodes', []):
                claim_obj = ClaimNode(**node_data.pop('claim'))
                sno.reasoning_graph.add_node(node_data['id'], **node_data, claim=claim_obj)

            for link_data in graph_data.get('links', []):
                edge_data = link_data.pop('reasoning_edge')
                # Handle case where relation_type might be a string
                edge_data['relation_type'] = RelationType(edge_data['relation_type'])
                edge_obj = ReasoningEdge(**edge_data)
                sno.reasoning_graph.add_edge(link_data['source'], link_data['target'], **link_data, reasoning_edge=edge_obj)

            sno.evidence_set = {EvidenceItem(**e_data) for e_data in data.get('evidence_set', [])}
            sno.trust_score = data.get('trust_score')

            return sno

        except KeyError as e:
            logging.error(f"Missing mandatory key in SNO data: {e}")
            raise ValueError(f"Invalid SNO data: Missing key {e}") from e
        except (TypeError, ValueError) as e:
            logging.error(f"Data type error during SNO deserialization: {e}")
            raise ValueError(f"Invalid SNO data: Malformed value. Details: {e}") from e


    def __repr__(self) -> str:
        return f"SNO(id={self.sno_id[:8]}, hypothesis='{self.central_hypothesis[:50]}...')"
```

## Building a Reasoning Graph: A Worked Example

The reasoning graph $G$ is what gives an SNO its explanatory power. Let's walk through a practical example. Imagine we are analyzing conflicting reports on a new "QuantumCore" battery technology.

**Our central hypothesis:** "QuantumCore batteries represent a viable next-generation energy solution."

Let's build the SNO for this.

```python
# 1. Initialize the SNO
sno = StructuredNarrativeObject(
    central_hypothesis="QuantumCore batteries represent a viable next-generation energy solution."
)

# 2. Add claims from our research sources
premise1_id = sno.add_claim(
    "The technology offers a 10x increase in energy density over lithium-ion.",
    claim_type="premise"
)
premise2_id = sno.add_claim(
    "Manufacturing scalability has been demonstrated in lab environments.",
    claim_type="premise"
)
counter_claim_id = sno.add_claim(
    "The battery's lifespan degrades by 50% after only 100 charge cycles.",
    claim_type="counter-argument"
)
rebuttal_id = sno.add_claim(
    "New electrolyte solutions are mitigating the lifespan degradation issue.",
    claim_type="rebuttal"
)

# 3. Connect the claims with reasoning edges
# The premises support the main hypothesis
sno.add_reasoning_edge(premise1_id, "root", RelationType.SUPPORTS)
sno.add_reasoning_edge(premise2_id, "root", RelationType.SUPPORTS)

# The counter-claim contradicts the main hypothesis
sno.add_reasoning_edge(counter_claim_id, "root", RelationType.CONTRADICTS, strength=0.8)

# The rebuttal weakens the counter-claim
sno.add_reasoning_edge(rebuttal_id, counter_claim_id, RelationType.WEAKENS, strength=0.7)

# 4. Check the graph's structure
print("Reasoning Graph Statistics:")
print(json.dumps(sno.get_graph_statistics(), indent=2))
```

This example creates a small but rich argumentative structure. It captures not just supporting points but also acknowledges and rebuts a key weakness, making the SNO a much more robust representation of the narrative than a simple statement.

## SNO Serialization and Persistence

For any real-world system, you need to save and load your data. SNOs, with their mix of standard data types, NumPy arrays, and NetworkX graphs, require a specific serialization strategy. We've added two methods to our class: `to_dict()` and `from_dict()`.

-   **`to_dict()`**: This method converts the SNO instance into a JSON-serializable dictionary. It handles the tricky parts:
    -   `hypothesis_embedding`: The NumPy array is converted to a standard Python list.
    -   `reasoning_graph`: We use NetworkX's built-in `node_link_data` function, which produces a clean, JSON-compliant representation of the graph's nodes and edges.
    -   `datetime`: The `created_at` timestamp is converted to an ISO 8601 string.
-   **`from_dict()`**: This class method takes a dictionary and reconstructs the SNO object. It reverses the process, converting the embedding list back to a NumPy array and using `node_link_graph` to rebuild the graph.

Here's how you would use them to save and load an SNO:

```python
# Assume 'sno' is the object from the previous example
# and it has an embedding computed.

# --- Saving the SNO ---
sno_dict = sno.to_dict()

# Save to a JSON file
with open("sno_quantum_core.json", "w") as f:
    json.dump(sno_dict, f, indent=2)

print("\nSNO saved to sno_quantum_core.json")

# --- Loading the SNO ---
with open("sno_quantum_core.json", "r") as f:
    loaded_sno_dict = json.load(f)

# Reconstruct the SNO object
loaded_sno = StructuredNarrativeObject.from_dict(loaded_sno_dict)

print(f"\nSuccessfully loaded SNO: {loaded_sno.sno_id}")
print(f"Original Trust Score: {sno.trust_score}, Loaded Trust Score: {loaded_sno.trust_score}")
print("Loaded Graph Statistics:")
print(json.dumps(loaded_sno.get_graph_statistics(), indent=2))
```

This serialization capability is essential for building a persistent SNO population, enabling the system to be stopped and restarted without losing its accumulated knowledge.
