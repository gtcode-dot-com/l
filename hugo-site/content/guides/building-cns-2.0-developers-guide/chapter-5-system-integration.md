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

## Persistence: Saving and Loading System State

An autonomous knowledge synthesis system is designed for long-running tasks. If the system shuts down unexpectedly or needs to be restarted, all the accumulated knowledge—the SNOs in its population—would be lost. This is impractical. To solve this, we introduce **persistence**.

We have added two key methods to our `CNSWorkflowManager`: `_save_system_state()` and `_load_system_state()`.

### Saving the State

The `_save_system_state` method is designed to be called during a graceful shutdown. It orchestrates the serialization of the entire system's current state into a single JSON file.

1.  **Serialize SNO Population**: It iterates through every SNO in the `sno_population` list. For each SNO, it calls the `to_dict()` method we developed in Chapter 2.
2.  **Collect Metrics**: It gathers statistics from the metrics tracker, the ingestion pipeline, and the critic pipeline.
3.  **Write to File**: It bundles everything into a single dictionary and writes it to the `cns_system_state.json` file.

### Loading the State

The `_load_system_state` method is called when the `CNSWorkflowManager` is first initialized. It allows the system to pick up right where it left off.

1.  **Check for State File**: It first checks if `cns_system_state.json` exists.
2.  **Load and Parse**: If the file exists, it loads the JSON data.
3.  **Reconstruct SNOs**: It iterates through the list of SNO dictionaries and uses the `StructuredNarrativeObject.from_dict()` class method to perfectly reconstruct each SNO.
4.  **Restore Metrics**: It restores the other system statistics.

This save/load cycle, powered by the serialization methods we built into our SNOs, transforms our system from a transient process into a persistent, robust knowledge base that can grow and evolve over time.

### Production Considerations for Persistence

While saving the entire state to a single JSON file is simple and effective for this guide, it has limitations in a large-scale production environment. Here are two key challenges and potential solutions:

1.  **Scalability and Performance**: As the `sno_population` grows, the `cns_system_state.json` file could become gigabytes in size. Saving and loading this entire file on every startup/shutdown cycle would be extremely slow and inefficient.
    -   **Solution**: Instead of a monolithic file, use a dedicated database. A document database like **MongoDB** is an excellent fit, as the JSON-like structure of our serialized SNOs (`sno.to_dict()`) maps directly to MongoDB documents. Each SNO can be stored as a separate document, allowing for fast, indexed lookups and updates without needing to read the entire population into memory.

2.  **Schema Versioning**: What happens if we update the `StructuredNarrativeObject` class? For example, if we add a new field, `author: str`, to the `ClaimNode` dataclass, our existing `from_dict` method would fail when trying to load older SNOs that don't have this field.
    -   **Solution**: Implement a migration strategy. This involves versioning your data schema. When you save an SNO, you would include a schema version number (e.g., `"schema_version": 2`). When `from_dict` loads an SNO, it would check this version. If it's an older version, the method would apply the necessary transformations (like adding the new `author` field with a default value of `"unknown"`) to upgrade the old data structure to the current class definition.

Thinking about these challenges early on is crucial for evolving a prototype into a robust, production-grade system.
