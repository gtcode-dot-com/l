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

# ... (Assume SystemMetrics, ProcessingTask, NarrativeIngestionPipeline are defined as before) ...

class CNSWorkflowManager:
    """
    Manages the complete CNS 2.0 operational workflow with state persistence.
    """
    
    def __init__(self, state_file: str = "cns_system_state.json"):
        self.sno_population: List[StructuredNarrativeObject] = []
        self.critic_pipeline = CriticPipeline()
        self.synthesis_engine = None
        
        self.embedding_model = None
        self.nli_model = None
        self.nli_tokenizer = None
        
        self.is_running = False
        self.task_queue = PriorityQueue()
        self.metrics = SystemMetrics()
        self.start_time = datetime.now()
        self.state_file = state_file
        
        self._load_models()

        # Initialize components that require models
        self.ingestion_pipeline = NarrativeIngestionPipeline(self.embedding_model)
        # Pass embedding model to detector for semantic conflict analysis
        self.chiral_detector = ChiralPairDetector(embedding_model=self.embedding_model)
        self._initialize_critics()

        # Load previous state from disk if it exists
        self._load_system_state()
    
    def _load_models(self):
        """Loads all necessary ML models into memory at startup for efficient reuse"""
        logger.info("Loading ML models into memory...")
        
        if HAS_TRANSFORMERS:
            from sentence_transformers import SentenceTransformer
            import transformers
            
            self.embedding_model = SentenceTransformer(cns_config.models['embedding'])
            self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(cns_config.models['nli'])
            self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(cns_config.models['nli'])
            
            logger.info("All models loaded successfully.")
        else:
            logger.warning("Transformers library not available - using fallback implementations")

    def _initialize_critics(self):
        """Set up the critic pipeline with pre-loaded models for efficiency"""
        if not HAS_TRANSFORMERS:
            logger.warning("Cannot initialize research-grade critics without transformers.")
            return

        grounding_critic = GroundingCritic(
            weight=cns_config.critic_weights['grounding'],
            nli_model=self.nli_model,
            nli_tokenizer=self.nli_tokenizer
        )
        logic_critic = LogicCritic(weight=cns_config.critic_weights['logic'])
        novelty_critic = NoveltyParsimonyCritic(
            weight=cns_config.critic_weights['novelty'],
            alpha=cns_config.novelty_alpha,
            beta=cns_config.novelty_beta
        )
        
        self.critic_pipeline.add_critic(grounding_critic)
        self.critic_pipeline.add_critic(logic_critic)
        self.critic_pipeline.add_critic(novelty_critic)
        logger.info("Research-grade critic pipeline initialized.")


    # --- Methods for Ingestion, Evaluation, Synthesis ---
    # ... (All async task handling methods like _process_task_queue,
    #      _handle_ingestion_task, etc., remain the same as previous version) ...

    async def shutdown_system(self):
        """Gracefully shutdown the CNS 2.0 system and save state."""
        self.is_running = False
        logger.info("CNS 2.0 System shutting down...")
        await self._save_system_state()
        logger.info("System shutdown complete.")
    
    async def _save_system_state(self):
        """Saves the entire system state to a JSON file."""
        logger.info(f"Saving system state to {self.state_file}...")
        try:
            state = {
                'sno_population': [sno.to_dict() for sno in self.sno_population],
                'metrics': self.metrics.to_dict(),
                'ingestion_stats': self.ingestion_pipeline.extraction_stats,
                'critic_stats': {ct.value: c.get_statistics() for ct, c in self.critic_pipeline.critics.items()}
            }
            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)
            logger.info("System state saved successfully.")
        except Exception as e:
            logger.error(f"Failed to save system state: {e}")

    def _load_system_state(self):
        """Loads system state from a JSON file if it exists."""
        if not os.path.exists(self.state_file):
            logger.info("No state file found. Starting with a fresh system.")
            return

        logger.info(f"Loading system state from {self.state_file}...")
        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)

            self.sno_population = [StructuredNarrativeObject.from_dict(sno_data) for sno_data in state.get('sno_population', [])]
            self.metrics = SystemMetrics(**state.get('metrics', {}))
            self.ingestion_pipeline.extraction_stats = state.get('ingestion_stats', {})

            logger.info(f"Successfully loaded {len(self.sno_population)} SNOs. System restored.")
        except Exception as e:
            logger.error(f"Failed to load system state: {e}. Starting fresh.")
            self.sno_population = []
            self.metrics = SystemMetrics()
    
    # ... (Other methods like submit_document, get_system_status remain the same) ...
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
