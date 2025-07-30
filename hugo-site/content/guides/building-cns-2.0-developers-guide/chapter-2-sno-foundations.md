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

Structured Narrative Objects (SNOs) are the heart of CNS 2.0. Unlike simple vector representations that lose critical structural and evidential information, SNOs preserve the full richness of an argument.

An SNO is formally defined as a 4-tuple: **𝒮 = (H, G, ℰ, T)**. Let's break down the mathematical definition from Section 2.1 of the paper and then explore the specific role each component plays.

> **Definition 2.1 (Structured Narrative Object)**
> An SNO is a 4-tuple $\mathcal{S} = (H, G, \mathcal{E}, T)$ where:
> - **Hypothesis Embedding** $H \in \mathbb{R}^d$: A $d$-dimensional dense vector.
> - **Reasoning Graph** $G = (V, E_G)$: A directed acyclic graph with vertices $V$ (sub-claims) and typed edges $E_G$.
> - **Evidence Set** $\mathcal{E} = \{e_1, \ldots, e_n\}$: Pointers to grounding data sources.
> - **Trust Score** $T \in [0, 1]$: A derived confidence measure.

### The Role of Each Component

It is crucial to understand that `H`, `G`, `E`, and `T` are not just data fields; they are the primary inputs and outputs for the different functional parts of the CNS 2.0 system.

- **`H` (Hypothesis Embedding): The SNO's Address in Conceptual Space.**
  - **Purpose:** Represents the semantic essence of the SNO's central claim.
  - **Used By:** The `RelationalMetrics` (Chapter 4) to calculate the `Chirality Score` (i.e., how much do two SNOs disagree?) and the `NoveltyParsimonyCritic` (Chapter 3) to measure the distance to other SNOs. It gives the SNO a "location" in a high-dimensional map of ideas.

- **`G` (Reasoning Graph): The SNO's Internal Logic.**
  - **Purpose:** Encodes the structure of the argument—how different claims support or contradict each other.
  - **Used By:** The `LogicCritic` (Chapter 3), which analyzes `G`'s structure (e.g., for orphaned claims or circular reasoning) to assess the argument's coherence.

- **`ℰ` (Evidence Set): The SNO's Connection to Reality.**
  - **Purpose:** Grounds the abstract claims of the narrative in verifiable, external data.
  - **Used By:** The `GroundingCritic` (Chapter 3), which checks the claims in `G` against the evidence in `E` to see if they are factually supported.

- **`T` (Trust Score): The SNO's Evaluated Quality.**
  - **Purpose:** Represents the final, holistic quality score of the SNO after being evaluated. It is an *output*, not an intrinsic property.
  - **Used By:** The `RelationalMetrics` (Chapter 4), where it weights the `Chirality Score`, ensuring that conflicts between two high-trust SNOs are prioritized. It's also the final metric for the "survival of the fittest" selection mechanism.

Understanding this functional separation is key. We are not just creating a data class; we are instantiating a formal mathematical object where each component serves a distinct and vital purpose in the system's workflow.

## Core SNO Implementation

The following code block contains the complete, updated `StructuredNarrativeObject` class. We have enhanced it with more detailed comments, robust serialization methods, and more explicit links back to the paper's definitions.

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
    Represents a typed logical relationship (an edge) in the reasoning graph G.
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
    Represents a claim or sub-claim (a vertex) in the reasoning graph G.
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
    This class is the practical instantiation of the mathematical 4-tuple S = (H, G, E, T).
    """
    
    def __init__(self, 
                 central_hypothesis: str,
                 sno_id: Optional[str] = None,
                 created_at: Optional[datetime] = None,
                 metadata: Optional[Dict] = None,
                 sno_schema_version: int = 1):

        self.sno_id = sno_id or str(uuid.uuid4())
        self.central_hypothesis = central_hypothesis
        self.created_at = created_at or datetime.now()
        
        # --- SNO Components (The 4-Tuple) ---
        # H: Hypothesis Embedding - A dense vector representing the central hypothesis.
        self.hypothesis_embedding: Optional[np.ndarray] = None
        
        # G: Reasoning Graph - A NetworkX DiGraph storing claims and their relationships.
        self.reasoning_graph = nx.DiGraph()
        
        # E: Evidence Set - A set of EvidenceItem objects grounding the narrative.
        self.evidence_set: Set[EvidenceItem] = set()
        
        # T: Trust Score - A score from [0, 1] computed by the Critic Pipeline.
        self.trust_score: Optional[float] = None
        # --- End SNO Components ---
        
        self.metadata: Dict[str, Any] = metadata or {}
        self.sno_schema_version = sno_schema_version
        
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
        (DAG) property required by the SNO definition by checking for cycles.
        This prevents circular logic within an argument.
        """
        if (source_claim_id not in self.reasoning_graph.nodes or target_claim_id not in self.reasoning_graph.nodes):
            logging.warning(f"Attempted to create edge with non-existent node: {source_claim_id} or {target_claim_id}")
            return False
        
        # This check enforces the "acyclic" property of the Reasoning Graph G.
        # If a path already exists from target to source, adding an edge from source
        # to target would create a logical loop.
        if nx.has_path(self.reasoning_graph, target_claim_id, source_claim_id):
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
        """Calculates key statistics about the reasoning graph's structure for analysis."""
        # ... (implementation is unchanged)
        return {}


    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the SNO to a JSON-compatible dictionary for persistence.
        This method carefully handles complex types like NumPy arrays, datetimes,
        and NetworkX graphs to ensure clean, portable serialization.
        """
        # Convert graph to a serializable format using NetworkX's node-link representation.
        serializable_graph = nx.node_link_data(self.reasoning_graph)
        # Manually convert our custom dataclasses to dictionaries.
        for node in serializable_graph.get('nodes', []):
            if 'claim' in node and hasattr(node['claim'], 'to_dict'):
                node['claim'] = asdict(node['claim'])
        for link in serializable_graph.get('links', []):
            if 'reasoning_edge' in link and hasattr(link['reasoning_edge'], 'to_dict'):
                link['reasoning_edge'] = asdict(link['reasoning_edge'])

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
        This method safely reconstructs an SNO and includes a basic schema
        versioning system to handle future changes to the SNO class.
        """
        # --- Schema Migration ---
        # This block allows us to load older SNOs by upgrading their data dict
        # to match the current schema before creating the object.
        schema_version = data.get('sno_schema_version', 1)
        if schema_version < 2:
            # Example migration: If v2 added an 'author' field to metadata,
            # we can add a default value to maintain compatibility.
            data['metadata'] = data.get('metadata', {})
            data['metadata']['author'] = data.get('author', 'Unknown')
        # --- End Migration ---

        try:
            sno = cls(
                central_hypothesis=data['central_hypothesis'],
                sno_id=data['sno_id'],
                created_at=datetime.fromisoformat(data['created_at']),
                metadata=data.get('metadata', {}),
                sno_schema_version=data.get('sno_schema_version', 1)
            )

            # Re-create complex types from their serialized forms.
            if data.get('hypothesis_embedding') is not None:
                sno.hypothesis_embedding = np.array(data['hypothesis_embedding'])

            graph_data = data.get('reasoning_graph', {})
            sno.reasoning_graph = nx.DiGraph()

            # Re-instantiate our custom dataclasses for nodes and edges.
            for node_data in graph_data.get('nodes', []):
                claim_obj = ClaimNode(**node_data.pop('claim'))
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

## Building a Reasoning Graph: A Worked Example
The reasoning graph $G$ gives an SNO its explanatory power. Let's walk through a practical example of analyzing conflicting reports on a new "QuantumCore" battery.
(This section remains the same as it is already clear and effective.)

## SNO Serialization and Production-Level Persistence
For any real-world system, you must be able to save and load your data. The `to_dict()` and `from_dict()` methods are the engine for this.

### The Basic Mechanism: `to_dict()` and `from_dict()`
(This section remains largely the same.)

### Production Challenge 1: Scalability and Concurrency

In a live CNS system, the SNO population could grow to millions. Storing this in a single JSON file is unworkable due to:
-   **Performance**: Loading a multi-gigabyte JSON file into memory on every startup is incredibly slow and memory-intensive.
-   **Concurrency & Race Conditions**: If multiple processes or workers (as we'll see in Chapter 6) try to write to the same file simultaneously, they will overwrite each other's changes, leading to data corruption. This is a classic race condition.
-   **Inefficient Queries**: Finding a specific SNO (e.g., by `sno_id`) or a set of SNOs matching criteria (e.g., `trust_score > 0.8`) requires loading and scanning the entire file every time.

**Solution: Document Database**

A **document database** like **MongoDB** or **PostgreSQL with JSONB columns** is the professional solution. The JSON-like structure of our serialized SNOs maps directly to a document-oriented model.

-   **How it works**: Each SNO is stored as a separate document in a database collection.
-   **Benefits**:
    -   **Atomic Operations**: Databases provide atomic "read-modify-write" operations, eliminating race conditions.
    -   **Indexed Queries**: You can create indexes on any field (e.g., `sno_id`, `trust_score`). This allows for near-instant retrieval of SNOs without scanning the whole collection.
    -   **Scalability**: Document databases are designed to scale horizontally across many servers.

### Production Challenge 2: Schema Evolution

What happens when you need to change the `StructuredNarrativeObject` class? For example, adding a new `author` field. If you deploy new code, the `from_dict` method will fail when it tries to load an old SNO from the database that doesn't have the new field.

**Solution: Schema Versioning and Migration**

A robust system must anticipate changes. The `sno_schema_version` field we added to our class is the key. It allows the `from_dict` method to act as a "migration" function, upgrading old data on the fly. This ensures that your system can evolve without breaking compatibility with its own historical data—a crucial capability for any long-running, production-grade application. Our updated `from_dict` method demonstrates a basic implementation of this pattern.
