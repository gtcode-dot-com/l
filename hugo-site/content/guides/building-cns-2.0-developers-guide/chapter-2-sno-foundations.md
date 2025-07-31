---
title: "Chapter 2: SNO Foundations"
description: "Building Structured Narrative Objects - the core data structure of CNS 2.0"
weight: 2
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 2: SNO Foundations

## Why Structured Narrative Objects?

At the heart of CNS 2.0 is the **Structured Narrative Object (SNO)**. To understand its importance, we must first recognize the limitations of simpler representations. Traditional vector embeddings, while powerful for capturing semantic similarity, are insufficient for dialectical reasoning because they discard three critical elements:
1.  **Logical Structure:** The "how" and "why" behind a conclusion.
2.  **Evidential Grounding:** The link between a claim and the data that supports it.
3.  **Evaluated Quality:** A measure of the narrative's trustworthiness.

SNOs are designed to capture this richness, transforming a narrative from an opaque string of text into a transparent, structured, and computationally evaluable object.

## The Formal Definition

An SNO is formally defined in the research paper as a 4-tuple. This mathematical precision is what allows the rest of the system to operate on it in a principled way.

> **From the Paper: Definition 2.1 (Structured Narrative Object)**
> An SNO is a 4-tuple $\mathcal{S} = (H, G, \mathcal{E}, T)$ where:
> - **Hypothesis Embedding** $H \in \mathbb{R}^d$: A $d$-dimensional dense vector encoding the narrative's central claim, enabling geometric similarity computations while preserving semantic content.
> - **Reasoning Graph** $G = (V, E_G)$: A directed acyclic graph with vertices $V$ representing sub-claims and edges $E_G$ encoding typed logical relationships.
> - **Evidence Set** $\mathcal{E} = \{e_1, e_2, \ldots, e_n\}$: Pointers to grounding data sources, establishing verifiable connections to primary sources.
> - **Trust Score** $T \in [0, 1]$: A derived confidence measure computed by the critic pipeline, not an intrinsic property of the narrative.

### The Role of Each Component

It is crucial to understand that `H`, `G`, `E`, and `T` are not just data fields; they are the specific inputs and outputs for the different functional parts of the CNS 2.0 system.

-   **`H` (Hypothesis Embedding): The SNO's "Address" in Conceptual Space.**
    -   **Purpose:** To represent the semantic essence of the SNO's central claim in a mathematical form.
    -   **Used By:** The `RelationalMetrics` (Chapter 4) to calculate the `Chirality Score` (i.e., how much do two SNOs disagree?) and the `NoveltyParsimonyCritic` (Chapter 3) to measure the distance to other SNOs. It gives the SNO a "location" in a high-dimensional map of ideas, making conceptual relationships measurable.

-   **`G` (Reasoning Graph): The SNO's Internal Logic.**
    -   **Purpose:** To explicitly encode the structure of the argument—how different claims support, contradict, or imply one another.
    -   **Used By:** The `LogicCritic` (Chapter 3), which analyzes `G`'s structure (e.g., for orphaned claims or circular reasoning) to assess the argument's coherence. This moves beyond *what* is being claimed to *how* the claim is justified.

-   **`ℰ` (Evidence Set): The SNO's Connection to Reality.**
    -   **Purpose:** To ground the abstract claims of the narrative in verifiable, external data, preventing hallucination and providing a basis for factual verification.
    -   **Used By:** The `GroundingCritic` (Chapter 3), which checks the claims in `G` against the evidence in `E` to see if they are factually supported. This ensures the narrative is not just logically sound but also empirically tethered.

-   **`T` (Trust Score): The SNO's Evaluated Quality.**
    -   **Purpose:** To represent the final, holistic quality score of the SNO after being evaluated by the critic pipeline. It is an **output** of the system's judgment, not an intrinsic property of the narrative itself.
    -   **Used By:** The `RelationalMetrics` (Chapter 4), where it weights the `Chirality Score`, ensuring that conflicts between two high-trust SNOs are prioritized. It's also the final metric for the "survival of the fittest" selection mechanism that determines which narratives persist in the population.

Understanding this functional separation is key. We are not just creating a data class; we are instantiating a formal mathematical object where each component serves a distinct and vital purpose in the system's workflow.

## Core SNO Implementation

The following code block contains the complete `StructuredNarrativeObject` class. The comments have been enhanced to explicitly map the Python implementation to the formal definition from the paper.

```python
"""
Structured Narrative Objects (SNO) Implementation
===============================================
The foundational data structure for CNS 2.0, now with enhanced
comments and robust serialization.
"""

import numpy as np
import networkx as nx
from typing import Dict, List, Set, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime
import uuid
import json
import logging

# Configure basic logging for warnings and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Assume RelationType and EvidenceItem are defined as in Chapter 1.

@dataclass
class ReasoningEdge:
    """
    Represents a typed logical relationship (an edge E_G) in the reasoning graph G.
    Each edge connects two claims and has a specific type (e.g., SUPPORTS)
    and strength.
    """
    source: str
    target: str
    relation_type: RelationType
    strength: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ClaimNode:
    """
    Represents a claim or sub-claim (a vertex V) in the reasoning graph G.
    Each node contains the text of the claim and can hold its own embedding
    for more granular analysis.
    """
    claim_id: str
    content: str
    claim_type: str = "assertion"
    # repr=False prevents the large embedding array from cluttering log outputs.
    embedding: Optional[np.ndarray] = field(default=None, repr=False)
    metadata: Dict[str, Any] = field(default_factory=dict)

class StructuredNarrativeObject:
    """
    The complete Python implementation of a Structured Narrative Object (SNO).
    This class is the practical instantiation of the mathematical 4-tuple S = (H, G, E, T)
    from the CNS 2.0 research paper.
    """
    
    def __init__(self, 
                 central_hypothesis: str,
                 sno_id: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 metadata: Optional[Dict] = None,
                 sno_schema_version: int = 2):

        self.sno_id = sno_id or str(uuid.uuid4())
        self.central_hypothesis = central_hypothesis
        self.created_at = created_at or datetime.now()
        
        # --- SNO Components (The Formal 4-Tuple) ---

        # H: Hypothesis Embedding (Optional[np.ndarray])
        # A dense vector representing the central hypothesis.
        self.hypothesis_embedding: Optional[np.ndarray] = None
        
        # G: Reasoning Graph (nx.DiGraph)
        # A NetworkX DiGraph storing claims (nodes) and their relationships (edges).
        self.reasoning_graph = nx.DiGraph()
        
        # E: Evidence Set (Set[EvidenceItem])
        # A set of EvidenceItem objects grounding the narrative in verifiable data.
        self.evidence_set: Set[EvidenceItem] = set()
        
        # T: Trust Score (Optional[float])
        # A score from [0, 1] computed by the Critic Pipeline. Initially None.
        self.trust_score: Optional[float] = None

        # --- End SNO Components ---
        
        self.metadata: Dict[str, Any] = metadata or {}
        self.sno_schema_version = sno_schema_version
        
        # The root node of the graph G is the central hypothesis itself.
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
        """Adds a new claim (a vertex V) to the reasoning graph G."""
        if claim_id is None:
            claim_id = f"claim_{len(self.reasoning_graph.nodes)}"
        
        claim_node = ClaimNode(claim_id=claim_id, content=claim_content, claim_type=claim_type)
        self.reasoning_graph.add_node(claim_id, claim=claim_node)
        return claim_id
    
    def add_reasoning_edge(self, source_claim_id: str, target_claim_id: str, relation_type: RelationType, strength: float = 1.0) -> bool:
        """
        Adds a new reasoning edge (an edge E_G) between claims in the graph G.

        Paper Reference: Section 2.1. This method enforces the "directed acyclic graph"
        (DAG) property required by the SNO formal definition by checking for cycles.
        This prevents circular logic within an argument.
        """
        if (source_claim_id not in self.reasoning_graph.nodes or target_claim_id not in self.reasoning_graph.nodes):
            logging.warning(f"Attempted to create edge with non-existent node: {source_claim_id} or {target_claim_id}")
            return False
        
        # This check enforces the "acyclic" property of the Reasoning Graph G.
        # If a path already exists from the target back to the source, adding an edge
        # from source to target would create a logical loop (a cycle).
        if nx.has_path(self.reasoning_graph, target_claim_id, source_claim_id):
            logging.error(f"Failed to add edge: Adding edge from {source_claim_id} to {target_claim_id} would create a cycle.")
            raise ValueError(f"Adding edge from {source_claim_id} to {target_claim_id} would create a cycle.")
        
        edge = ReasoningEdge(source=source_claim_id, target=target_claim_id, relation_type=relation_type, strength=strength)
        self.reasoning_graph.add_edge(source_claim_id, target_claim_id, reasoning_edge=edge)
        return True
    
    def add_evidence(self, evidence_item: EvidenceItem):
        """Adds a piece of evidence (an element e_i) to the evidence set E."""
        self.evidence_set.add(evidence_item)
    
    def compute_hypothesis_embedding(self, embedding_model):
        """Computes and stores the hypothesis embedding H using a provided sentence-transformer model."""
        if not hasattr(embedding_model, 'encode'):
            raise TypeError("embedding_model must have an 'encode' method.")
        self.hypothesis_embedding = embedding_model.encode(self.central_hypothesis)
    
    def get_graph_statistics(self) -> Dict[str, Any]:
        """Calculates key statistics about the reasoning graph G for analysis."""
        num_nodes = self.reasoning_graph.number_of_nodes()
        if num_nodes == 0:
            return {'nodes': 0, 'edges': 0, 'density': 0, 'is_dag': True}

        return {
            'nodes': num_nodes,
            'edges': self.reasoning_graph.number_of_edges(),
            'density': nx.density(self.reasoning_graph),
            'is_dag': nx.is_directed_acyclic_graph(self.reasoning_graph),
            'avg_in_degree': np.mean([d for _, d in self.reasoning_graph.in_degree()]),
            'avg_out_degree': np.mean([d for _, d in self.reasoning_graph.out_degree()]),
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the SNO to a JSON-compatible dictionary for persistence.
        This method carefully handles complex types like NumPy arrays, datetimes,
        and NetworkX graphs to ensure clean, portable serialization.
        """
        # Convert graph to a serializable format using NetworkX's node-link representation.
        serializable_graph = nx.node_link_data(self.reasoning_graph)

        # Manually convert our custom dataclasses within the graph to dictionaries.
        for node in serializable_graph.get('nodes', []):
            if 'claim' in node and isinstance(node['claim'], ClaimNode):
                claim_dict = asdict(node['claim'])
                # Convert embedding to list for JSON compatibility
                if claim_dict.get('embedding') is not None:
                    claim_dict['embedding'] = claim_dict['embedding'].tolist()
                node['claim'] = claim_dict

        for link in serializable_graph.get('links', []):
            if 'reasoning_edge' in link and isinstance(link['reasoning_edge'], ReasoningEdge):
                edge_dict = asdict(link['reasoning_edge'])
                edge_dict['relation_type'] = edge_dict['relation_type'].value # Convert enum to string
                link['reasoning_edge'] = edge_dict

        return {
            'sno_id': self.sno_id,
            'sno_schema_version': self.sno_schema_version,
            'central_hypothesis': self.central_hypothesis,
            'created_at': self.created_at.isoformat(),
            # NumPy arrays are not native to JSON, so we convert H to a list.
            'hypothesis_embedding': self.hypothesis_embedding.tolist() if self.hypothesis_embedding is not None else None,
            'reasoning_graph': serializable_graph,
            'evidence_set': [asdict(e) for e in self.evidence_set],
            'trust_score': self.trust_score,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StructuredNarrativeObject':
        """
        Deserializes an SNO from a dictionary, handling data migrations.
        This method safely reconstructs an SNO and includes a schema versioning
        system to handle future changes to the SNO class.
        """
        schema_version = data.get('sno_schema_version', 1)
        if schema_version < 2:
            # This is where you would handle migrations from older SNO formats.
            # For example, if v2 added a new mandatory field, you'd add a default here.
            pass

        try:
            sno = cls(
                central_hypothesis=data['central_hypothesis'],
                sno_id=data['sno_id'],
                created_at=datetime.fromisoformat(data['created_at']),
                metadata=data.get('metadata', {}),
                sno_schema_version=schema_version
            )

            # Re-create complex types from their serialized forms.
            if data.get('hypothesis_embedding') is not None:
                sno.hypothesis_embedding = np.array(data['hypothesis_embedding'])

            graph_data = data.get('reasoning_graph', {})
            sno.reasoning_graph = nx.DiGraph()

            # Re-instantiate our custom dataclasses for nodes and edges.
            for node_data in graph_data.get('nodes', []):
                claim_data = node_data.pop('claim')
                if claim_data.get('embedding') is not None:
                    claim_data['embedding'] = np.array(claim_data['embedding'])
                claim_obj = ClaimNode(**claim_data)
                sno.reasoning_graph.add_node(node_data['id'], claim=claim_obj, **node_data)

            for link_data in graph_data.get('links', []):
                edge_data = link_data.pop('reasoning_edge')
                if isinstance(edge_data['relation_type'], str):
                    edge_data['relation_type'] = RelationType(edge_data['relation_type'])
                edge_obj = ReasoningEdge(**edge_data)
                sno.reasoning_graph.add_edge(link_data['source'], link_data['target'], reasoning_edge=edge_obj, **link_data)

            sno.evidence_set = {EvidenceItem(**e_data) for e_data in data.get('evidence_set', [])}
            sno.trust_score = data.get('trust_score')

            return sno

        except KeyError as e:
            logging.error(f"Missing mandatory key in SNO data: {e}")
            raise ValueError(f"Invalid SNO data: Missing key {e}") from e
        except Exception as e:
            logging.error(f"Error during SNO deserialization: {e}", exc_info=True)
            raise ValueError(f"Invalid SNO data. Details: {e}") from e

    def __repr__(self) -> str:
        return f"SNO(id={self.sno_id[:8]}, hypothesis='{self.central_hypothesis[:50]}...')"
```

## SNO Serialization and Production-Level Persistence

For any real-world system, you must be able to save and load your data. The `to_dict()` and `from_dict()` methods are the engine for this, but a robust strategy requires more than just converting to a dictionary.

### The Mechanism: `to_dict()` and `from_dict()`

A successful persistence strategy hinges on robust serialization. Here's a deeper look at how our methods work:
-   **`to_dict()`**: This method acts as a "dehydrator," carefully converting the SNO instance into a JSON-compatible dictionary. It systematically handles complex types:
    -   `hypothesis_embedding`: The NumPy array is converted to a standard Python list.
    -   `reasoning_graph`: We use NetworkX's built-in `node_link_data` function, which produces a clean, JSON-compliant representation. Crucially, we then iterate through its output to explicitly convert our `ClaimNode` and `ReasoningEdge` dataclass objects into dictionaries using `asdict`.
    -   `datetime` and `Enum`: These are converted to standard string representations (ISO 8601 for dates, `.value` for enums).
-   **`from_dict()`**: This class method is the "rehydrator." It takes a dictionary and meticulously reconstructs the live SNO object, converting lists back to NumPy arrays, strings to `datetime` objects, and carefully rebuilding the graph and its custom dataclasses. This ensures all methods and type-safety of the original object are restored.

The code below demonstrates this round-trip process:
```python
# Assume 'sno' is an object with an embedding computed.

# --- Saving the SNO ---
sno_dict = sno.to_dict()

# Save to a JSON file
with open("sno_example.json", "w") as f:
    json.dump(sno_dict, f, indent=2)

print("\nSNO saved to sno_example.json")

# --- Loading the SNO ---
with open("sno_example.json", "r") as f:
    loaded_sno_dict = json.load(f)

# Reconstruct the SNO object
loaded_sno = StructuredNarrativeObject.from_dict(loaded_sno_dict)

print(f"\nSuccessfully loaded SNO: {loaded_sno.sno_id}")
print(f"Original Trust Score: {sno.trust_score}, Loaded Trust Score: {loaded_sno.trust_score}")
print(f"Graph is a DAG: {nx.is_directed_acyclic_graph(loaded_sno.reasoning_graph)}")
```

### Production Challenge 1: Scalability and Concurrency

In a live CNS system, the SNO population could grow to millions. Storing this in a single JSON file is unworkable due to:
-   **Performance**: Loading a multi-gigabyte JSON file into memory on every startup is incredibly slow.
-   **Concurrency & Race Conditions**: If multiple processes or workers try to write to the same file simultaneously, they will corrupt the data.
-   **Inefficient Queries**: Finding a specific SNO (e.g., by `sno_id`) requires loading and scanning the entire file every time.

**Solution: Document Database**

A **document database** like **MongoDB** or **PostgreSQL with JSONB columns** is the professional solution. The JSON-like structure of our serialized SNOs maps directly to a document-oriented model, where each SNO is stored as a separate, indexed document. This provides atomic operations, efficient queries, and horizontal scalability.

### Production Challenge 2: Schema Evolution

What happens when you need to change the `StructuredNarrativeObject` class? For example, adding a new `author` field. If you deploy new code, the `from_dict` method will fail when it tries to load an old SNO that doesn't have the new field.

**Solution: Schema Versioning and Migration**

A robust system must anticipate change. The `sno_schema_version` field we added is the key. It allows the `from_dict` method to act as a "migration" function. Before creating the object, it can check the version and apply transformations to the data dictionary to make it compatible with the new code. This ensures your system can evolve without breaking compatibility with its own historical data—a crucial capability for any long-running application.
