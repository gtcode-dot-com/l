---
title: "Chapter 5: System Integration"
description: "Combining all CNS 2.0 components into a working system with workflow management"
weight: 5
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 5: System Integration

## Building the Complete CNS 2.0 System

Now that we've implemented the core components, it's time to integrate them into a cohesive system. This chapter focuses on the operational workflow, system dynamics, and the critical narrative ingestion pipeline. The result will be a stateful, autonomous system capable of running continuously.

## System Architecture with Persistence

A key enhancement in this chapter is adding **persistence**. An autonomous system that runs for long periods must be able to save its state and resume after a shutdown. We will add methods to save the entire SNO population and system metrics to a file, making our workflow manager robust.

```python
"""
CNS 2.0 System Integration with Persistence
===========================================
Complete system architecture that can save and load its state.
"""

import asyncio
import logging
import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from queue import PriorityQueue

# ... (Assume other classes like SystemMetrics are defined) ...

# For an async system, we use asyncio's Queue
from asyncio import Queue

class CNSWorkflowManager:
    """
    Manages the complete CNS 2.0 operational workflow with state persistence.
    This version includes the full asynchronous processing loop.
    """
    
    def __init__(self, state_file: str = "cns_system_state.json"):
        # Core components
        self.sno_population: List[StructuredNarrativeObject] = []
        self.critic_pipeline = CriticPipeline()
        self.synthesis_engine = None # Will be initialized after models are loaded
        
        # ML Models
        self.embedding_model = None
        self.nli_model = None
        self.nli_tokenizer = None
        
        # System state and control
        self.is_running = False
        self.task_queue = Queue() # Use asyncio's Queue for async operations
        self.metrics = SystemMetrics()
        self.start_time = datetime.now()
        self.state_file = state_file
        
        self._load_models_and_components()
        self._load_system_state()

    def _load_models_and_components(self):
        """Loads all necessary ML models and initializes components that depend on them."""
        logger.info("Loading ML models and initializing components...")
        if not HAS_TRANSFORMERS:
            logger.error("Transformers library not available. Cannot run research-grade system.")
            return

        from sentence_transformers import SentenceTransformer
        import transformers

        # Load models
        self.embedding_model = SentenceTransformer(cns_config.models['embedding'])
        self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(cns_config.models['nli'])
        self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(cns_config.models['nli'])

        # Initialize components that require models
        self.ingestion_pipeline = NarrativeIngestionPipeline(self.embedding_model)
        self.chiral_detector = ChiralPairDetector(embedding_model=self.embedding_model)
        self._initialize_critics()
        # self.synthesis_engine = AdvancedSynthesisEngine(...) # Assume this is initialized

        logger.info("All models and components loaded successfully.")

    def _initialize_critics(self):
        # ... (implementation is the same as before) ...

    ### --- The Asynchronous Main Loop --- ###
    
    async def run(self):
        """The main entry point to start the continuous operation of the CNS system."""
        self.is_running = True
        logger.info("CNS Workflow Manager is running...")
        
        # Create a background task for processing the queue
        self.processing_task = asyncio.create_task(self._process_task_queue())

        # Keep the main loop alive (e.g., to handle API requests or other inputs)
        while self.is_running:
            await asyncio.sleep(1)

        # On shutdown, ensure the processing task is cancelled
        self.processing_task.cancel()
        await self.shutdown_system()

    async def _process_task_queue(self):
        """Continuously fetches tasks from the queue and handles them."""
        while self.is_running:
            try:
                task = await self.task_queue.get()
                task_type, data = task

                if task_type == "ingest":
                    await self._handle_ingestion_task(data)
                elif task_type == "evaluate":
                    await self._handle_evaluation_task(data)
                elif task_type == "synthesize":
                    await self._handle_synthesis_task()

                self.task_queue.task_done()
            except asyncio.CancelledError:
                logger.info("Task processing loop cancelled.")
                break
            except Exception as e:
                logger.error(f"Error in task processing loop: {e}")

    async def _handle_ingestion_task(self, data):
        """Processes a document ingestion task."""
        logger.info(f"Ingesting document: {data['source']}")
        sno = self.ingestion_pipeline.ingest_document(data['text'], data['source'])
        self.sno_population.append(sno)
        self.metrics.sno_ingested()
        # New SNOs should be evaluated
        await self.task_queue.put(("evaluate", sno))

    async def _handle_evaluation_task(self, sno: StructuredNarrativeObject):
        """Processes an SNO evaluation task."""
        logger.info(f"Evaluating SNO: {sno.sno_id[:8]}")
        context = {'sno_population': self.sno_population}
        self.critic_pipeline.evaluate_sno(sno, context)
        self.metrics.sno_evaluated()
        
        # After evaluation, check if synthesis should be triggered
        if len(self.sno_population) > 1:
            await self.task_queue.put(("synthesize", None))

    async def _handle_synthesis_task(self):
        """Finds chiral pairs and synthesizes a new SNO if conditions are met."""
        logger.info("Checking for synthesis opportunities...")
        chiral_pairs = self.chiral_detector.find_chiral_pairs(self.sno_population)
        if chiral_pairs:
            # For simplicity, we'll try to synthesize the top pair
            top_pair = chiral_pairs[0]
            logger.info(f"Synthesizing new SNO from pair: {top_pair.sno_a.sno_id[:8]} and {top_pair.sno_b.sno_id[:8]}")
            # result = await self.synthesis_engine.synthesize_chiral_pair(top_pair)
            # if result.success:
            #     self.sno_population.append(result.synthesized_sno)
            #     self.metrics.sno_synthesized()
            #     await self.task_queue.put(("evaluate", result.synthesized_sno))
        else:
            logger.info("No suitable pairs found for synthesis.")

    ### --- Persistence and Shutdown --- ###

    async def shutdown_system(self):
        """Gracefully shuts down the CNS 2.0 system and saves state."""
        self.is_running = False
        logger.info("CNS 2.0 System shutting down...")
        await self._save_system_state()
        logger.info("System shutdown complete.")
    
    async def _save_system_state(self):
        # ... (implementation is the same as before) ...

    def _load_system_state(self):
        # ... (implementation is the same as before) ...
```

## Production-Grade Persistence: From JSON to a Database

An autonomous knowledge synthesis system is designed for long-running tasks, making robust data persistence a non-negotiable requirement. While the `_save_system_state` and `_load_system_state` methods using a single JSON file are a good starting point for development, a production system requires a more scalable and robust solution. This section provides a guide to upgrading the persistence layer.

### The Limitations of File-Based Persistence
-   **Performance & Scalability**: As the SNO population grows, the `cns_system_state.json` file can become enormous. Loading and parsing a multi-gigabyte JSON file on every startup is unacceptably slow.
-   **Concurrency**: A single file cannot be safely written to by multiple processes or workers simultaneously, which is essential for a scaled-out system. This creates a major bottleneck.
-   **Querying**: Answering simple questions like "Find all SNOs with a trust score above 0.8" requires loading and scanning the entire file, which is grossly inefficient.

### Solution 1: Adopting a Document Database (e.g., MongoDB)
A **document database** is the ideal solution for storing SNOs, as the JSON-like dictionary from `sno.to_dict()` maps directly to a document structure.

**Conceptual Implementation:**
1.  **Setup**: Install a database client library (e.g., `pip install pymongo`).
2.  **Connection**: Your `CNSWorkflowManager` should establish a connection to your database server.
3.  **Data Operations**: Replace file I/O with database operations. The `sno_id` can serve as the unique `_id` for documents.

```python
# Conceptual example of saving an SNO to MongoDB
from pymongo import MongoClient, ReplaceOne

# client = MongoClient('mongodb://your-mongo-uri/')
# db = client.cns_database
# sno_collection = db.sno_population

def save_sno_to_db(sno: StructuredNarrativeObject):
    """Saves a single SNO, inserting or updating as needed."""
    sno_dict = sno.to_dict()
    # Use update_one with upsert=True for an efficient insert-or-update operation.
    sno_collection.update_one(
        {'_id': sno.sno_id},
        {'$set': sno_dict},
        upsert=True
    )
```
This approach provides **indexed queries** (e.g., `db.sno_population.find({'trust_score': {'$gt': 0.8}})`), massive **scalability**, and safe **concurrent access**.

### Solution 2: Managing Schema Evolution
As your system evolves, your `StructuredNarrativeObject` class will change. This is **schema evolution**. If you deploy new code, it will likely crash when it encounters old data. A robust system must handle this gracefully.

The solution, as introduced in Chapter 2, is **schema versioning and migration**.

1.  **Version your SNOs**: Add a version field to your class, e.g., `sno_schema_version: int = 2`. Increment this when you make a breaking change.
2.  **Implement a Migration Path**: Your data loading logic must be able to handle old versions.

Here is a more robust conceptual example of a data access function that handles migration:
```python
def load_sno_from_db(sno_id: str) -> Optional[StructuredNarrativeObject]:
    """Loads a single SNO from the DB and applies necessary data migrations."""
    sno_data = sno_collection.find_one({'_id': sno_id})
    if not sno_data:
        return None

    schema_version = sno_data.get('sno_schema_version', 1) # Assume legacy data is v1

    # Apply migrations sequentially to bring the data to the current version.
    if schema_version < 2:
        # Migration for v2: 'author' field was added to metadata.
        sno_data['metadata']['author'] = sno_data['metadata'].get('author', 'Unknown')
    if schema_version < 3:
        # Migration for v3: 'claim_type' was renamed to 'node_type' in ClaimNode.
        for node in sno_data.get('reasoning_graph', {}).get('nodes', []):
            if 'claim' in node and 'claim_type' in node['claim']:
                node['claim']['node_type'] = node['claim'].pop('claim_type')

    # After migration, the data dictionary conforms to the latest schema.
    return StructuredNarrativeObject.from_dict(sno_data)
```
By explicitly handling data migrations, you ensure your system can evolve without breaking compatibility with its own historical data—a hallmark of a production-ready application.

## Monitoring the Health of the CNS System

An autonomous system like CNS 2.0 should not be a "black box" once deployed. Continuous monitoring is essential to ensure it is operating correctly, performing efficiently, and producing high-quality knowledge. A monitoring dashboard (e.g., using tools like Grafana, Prometheus, or Datadog) should track the following key metrics:

### System Performance Metrics
-   **Task Queue Size**: The number of pending tasks in the queue. A constantly growing queue indicates that the processing workers cannot keep up with the ingestion rate and that you may need to scale up your resources.
-   **Task Processing Latency**: The average time it takes to process a single task (e.g., ingest a document, evaluate an SNO). Spikes in latency can indicate performance bottlenecks.
-   **Model API Latency & Error Rate**: If using external model APIs, track the response times and error rates for each model (embedding, NLI, synthesis). This can help diagnose issues that are external to the CNS system itself.
-   **Database Performance**: Monitor query latency and throughput for your persistence layer to ensure it is not becoming a bottleneck.

### Knowledge Quality and Dynamics Metrics
-   **SNO Ingestion Rate**: The number of new SNOs being added to the population per hour. This measures the system's overall throughput.
-   **SNO Population Size**: A simple count of the total number of SNOs in the knowledge base.
-   **Average Trust Score**: The mean trust score of all SNOs in the population. A steadily increasing average score suggests the system is successfully refining its knowledge. A sudden drop could indicate a problem with the critic pipeline or the ingestion of low-quality source material.
-   **Synthesis Rate**: The number of new SNOs being generated by the synthesis engine per hour. This measures the system's "creativity" or rate of discovery.
-   **Synthesis Success Rate**: The percentage of synthesized candidate SNOs that achieve a high enough trust score to be added to the population. A low success rate might indicate that the synthesis prompts need to be optimized (as discussed in Chapter 7).
-   **Critic Score Distribution**: A histogram showing the distribution of scores for each individual critic (Grounding, Logic, Novelty). This can help identify if the system is becoming biased (e.g., only producing logical but unoriginal ideas).

By tracking these metrics, you gain crucial visibility into the system's operational health and its effectiveness at the core task of knowledge synthesis, enabling you to tune, scale, and improve it over time.
