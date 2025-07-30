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
> - **Hypothesis Embedding** $H \in \mathbb{R}^d$: A $d$-dimensional dense vector encoding the narrative's central claim, enabling geometric similarity computations while preserving semantic content
> - **Reasoning Graph** $G = (V, E_G)$: A directed acyclic graph with vertices $V$ representing sub-claims and edges $E_G \subseteq V \times V \times \mathcal{R}$ encoding typed logical relationships (e.g., "supports," "contradicts," "implies") from the relation set $\mathcal{R}$
> - **Evidence Set** $\mathcal{E} = \{e_1, e_2, \ldots, e_n\}$: Pointers to grounding data sources, including document identifiers, data hashes, or persistent identifiers (DOIs), establishing verifiable connections to primary sources
> - **Trust Score** $T \in [0, 1]$: A derived confidence measure computed by the critic pipeline, not an intrinsic property of the narrative

**From Paper to Code:**

Our `StructuredNarrativeObject` Python class is the direct, practical implementation of this mathematical 4-tuple. Let's map the theory to our code:

- **`H` (Hypothesis Embedding):** This corresponds to the `self.hypothesis_embedding` attribute in our class. It's an optional `np.ndarray` that will hold the dense vector representation of the SNO's central claim, calculated by the `compute_hypothesis_embedding` method.
- **`G` (Reasoning Graph):** This is implemented as `self.reasoning_graph`, a `networkx.DiGraph` object. The vertices `V` are the nodes added via `add_claim`, and the edges `E_G` are the relationships added with `add_reasoning_edge`. The paper's requirement that it be a *directed acyclic graph* is enforced by our check for cycles within the `add_reasoning_edge` method.
- **`ℰ` (Evidence Set):** This is our `self.evidence_set`, a Python `set` containing `EvidenceItem` objects. This perfectly matches the definition of a collection of pointers to grounding data.
- **`T` (Trust Score):** This is the `self.trust_score` attribute. As the paper states, it is "not an intrinsic property" but is "derived," which is why it's initialized as `None` and will be populated later by our `CriticPipeline`.

Understanding this mapping is key. We're not just creating a data class; we're instantiating a formal mathematical object described in the paper.

#### A Note on Embeddings
For the mathematical primitives like the Chirality Score and Novelty Score to work as intended, we need a semantically meaningful vector space. Simple fallbacks like hash-based vectors produce random outputs that destroy any geometric meaning, rendering the core CNS 2.0 mechanics useless. Therefore, our implementation treats a real embedding model as a mandatory component.

## Core SNO Implementation

```python
"""
Structured Narrative Objects (SNO) Implementation
===============================================
The foundational data structure for CNS 2.0
"""

import numpy as np
import networkx as nx
from typing import Dict, List, Tuple, Set, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class ReasoningEdge:
    """Represents a typed logical relationship in the reasoning graph"""
    source: str
    target: str
    relation_type: RelationType
    strength: float = 1.0  # Relationship strength [0,1]
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ClaimNode:
    """Represents a claim or sub-claim in the reasoning graph"""
    claim_id: str
    content: str
    claim_type: str = "assertion"  # assertion, premise, conclusion, etc.
    embedding: Optional[np.ndarray] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

class StructuredNarrativeObject:
    """
    Complete implementation of a Structured Narrative Object (SNO)
    
    This class encapsulates all four components of an SNO:
    - Hypothesis Embedding (H)
    - Reasoning Graph (G) 
    - Evidence Set (E)
    - Trust Score (T)
    """
    
    def __init__(self, 
                 central_hypothesis: str,
                 sno_id: Optional[str] = None):
        """
        Initialize a new SNO with a central hypothesis
        
        Args:
            central_hypothesis: The main claim or hypothesis
            sno_id: Unique identifier (auto-generated if None)
        """
        self.sno_id = sno_id or str(uuid.uuid4())
        self.central_hypothesis = central_hypothesis
        self.created_at = datetime.now()
        
        # H: Hypothesis Embedding - will be computed later
        self.hypothesis_embedding: Optional[np.ndarray] = None
        
        # G: Reasoning Graph - NetworkX directed graph
        self.reasoning_graph = nx.DiGraph()
        
        # E: Evidence Set - collection of evidence items
        self.evidence_set: Set[EvidenceItem] = set()
        
        # T: Trust Score - computed by critic pipeline
        self.trust_score: Optional[float] = None
        
        # Additional metadata
        self.metadata: Dict[str, Any] = {}
        
        # Initialize with central hypothesis as root node
        self._add_root_claim()
    
    def _add_root_claim(self):
        """Add the central hypothesis as the root node of the reasoning graph"""
        root_node = ClaimNode(
            claim_id="root",
            content=self.central_hypothesis,
            claim_type="central_hypothesis"
        )
        self.reasoning_graph.add_node("root", claim=root_node)
    
    def add_claim(self, 
                  claim_content: str, 
                  claim_id: Optional[str] = None,
                  claim_type: str = "assertion") -> str:
        """
        Add a new claim to the reasoning graph
        
        Args:
            claim_content: Text content of the claim
            claim_id: Unique identifier (auto-generated if None)
            claim_type: Type of claim (assertion, premise, conclusion, etc.)
            
        Returns:
            The claim_id of the added claim
        """
        if claim_id is None:
            claim_id = f"claim_{len(self.reasoning_graph.nodes)}"
        
        claim_node = ClaimNode(
            claim_id=claim_id,
            content=claim_content,
            claim_type=claim_type
        )
        
        self.reasoning_graph.add_node(claim_id, claim=claim_node)
        return claim_id
    
    def add_reasoning_edge(self,
                          source_claim_id: str,
                          target_claim_id: str,
                          relation_type: RelationType,
                          strength: float = 1.0) -> bool:
        """
        Add a reasoning relationship between two claims
        
        Args:
            source_claim_id: ID of the source claim
            target_claim_id: ID of the target claim
            relation_type: Type of logical relationship
            strength: Strength of the relationship [0,1]
            
        Returns:
            True if edge was added successfully
        """
        if (source_claim_id not in self.reasoning_graph.nodes or 
            target_claim_id not in self.reasoning_graph.nodes):
            return False
        
        # Check for cycles (reasoning graph must be acyclic)
        if nx.has_path(self.reasoning_graph, target_claim_id, source_claim_id):
            raise ValueError("Adding this edge would create a cycle")
        
        edge = ReasoningEdge(
            source=source_claim_id,
            target=target_claim_id,
            relation_type=relation_type,
            strength=strength
        )
        
        self.reasoning_graph.add_edge(
            source_claim_id, 
            target_claim_id, 
            reasoning_edge=edge
        )
        return True
    
    def add_evidence(self, evidence_item: EvidenceItem):
        """Add evidence to support claims in this SNO"""
        self.evidence_set.add(evidence_item)
    
    def compute_hypothesis_embedding(self, embedding_model):
        """
        Compute the hypothesis embedding using a sentence transformer model.
        This is a critical step for all geometric operations in CNS 2.0.

        Args:
            embedding_model: A loaded sentence-transformer model instance.
        """
        # A real embedding is non-negotiable for research-grade implementation.
        self.hypothesis_embedding = embedding_model.encode(self.central_hypothesis)
    
    def get_graph_statistics(self) -> Dict[str, Any]:
        """Compute statistics about the reasoning graph"""
        stats = {
            'num_nodes': self.reasoning_graph.number_of_nodes(),
            'num_edges': self.reasoning_graph.number_of_edges(),
            'is_acyclic': nx.is_directed_acyclic_graph(self.reasoning_graph),
            'density': nx.density(self.reasoning_graph),
            'relation_type_counts': {}
        }
        
        # Count relation types
        for _, _, edge_data in self.reasoning_graph.edges(data=True):
            if 'reasoning_edge' in edge_data:
                rel_type = edge_data['reasoning_edge'].relation_type.value
                stats['relation_type_counts'][rel_type] = stats['relation_type_counts'].get(rel_type, 0) + 1
        
        return stats
    
    def __repr__(self) -> str:
        return f"SNO(id={self.sno_id[:8]}, hypothesis='{self.central_hypothesis[:50]}...')"

