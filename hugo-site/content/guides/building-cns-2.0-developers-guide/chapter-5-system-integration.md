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

Now that we've implemented the core components—Structured Narrative Objects, the Multi-Component Critic Pipeline, and the Generative Synthesis Engine—it's time to integrate them into a cohesive system. This chapter focuses on the operational workflow, system dynamics, and the critical narrative ingestion pipeline.

The complete CNS 2.0 system operates as a continuous loop, processing new information, evaluating conflicts, and generating synthetic knowledge through dialectical reasoning.

## System Architecture Overview

```python
"""
CNS 2.0 System Integration
=========================
Complete system architecture bringing together all components
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, AsyncGenerator
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from queue import PriorityQueue
import json

# Configure system-wide logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SystemMetrics:
    """Track system performance and behavior"""
    total_snos: int = 0
    active_syntheses: int = 0
    successful_syntheses: int = 0
    failed_syntheses: int = 0
    average_trust_score: float = 0.0
    processing_rate: float = 0.0  # SNOs per hour
    uptime: timedelta = field(default_factory=lambda: timedelta(0))
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'total_snos': self.total_snos,
            'active_syntheses': self.active_syntheses,
            'successful_syntheses': self.successful_syntheses,
            'failed_syntheses': self.failed_syntheses,
            'average_trust_score': self.average_trust_score,
            'processing_rate': self.processing_rate,
            'uptime_hours': self.uptime.total_seconds() / 3600
        }

@dataclass
class ProcessingTask:
    """Represents a task in the system processing queue"""
    task_id: str
    task_type: str  # 'ingest', 'synthesize', 'evaluate'
    priority: int  # Lower numbers = higher priority
    payload: Dict[str, Any]
    created_at: datetime = field(default_factory=datetime.now)
    
    def __lt__(self, other):
        return self.priority < other.priority

class NarrativeIngestionPipeline:
    """
    Critical component for converting unstructured sources into SNOs
    This represents a major research challenge in argumentation mining
    """
    
    def __init__(self, embedding_model=None):
        self.embedding_model = embedding_model  # Pre-loaded model for efficiency
        self.extraction_stats = {
            'documents_processed': 0,
            'snos_created': 0,
            'extraction_failures': 0
        }
    
    async def ingest_document(self, 
                            document_text: str, 
                            source_metadata: Dict[str, Any]) -> Optional[StructuredNarrativeObject]:
        """
        Convert unstructured document into SNO through argumentation mining
        
        This is a simplified implementation - in production, this would involve:
        1. Advanced NLP for claim extraction
        2. Sophisticated reasoning graph construction
        3. Evidence linking and verification
        """
        try:
            logger.info(f"Starting document ingestion: {source_metadata.get('title', 'Unknown')}")
            
            # Step 1: Hypothesis Extraction
            central_hypothesis = await self._extract_central_hypothesis(document_text)
            if not central_hypothesis:
                logger.warning("Failed to extract central hypothesis")
                self.extraction_stats['extraction_failures'] += 1
                return None
            
            # Step 2: Create SNO
            sno = StructuredNarrativeObject(central_hypothesis)
            sno.metadata.update(source_metadata)
            
            # Step 3: Reasoning Graph Construction
            await self._construct_reasoning_graph(sno, document_text)
            
            # Step 4: Evidence Set Population
            await self._populate_evidence_set(sno, document_text, source_metadata)
            
            # Step 5: Compute embeddings using the pre-loaded model
            if not self.embedding_model:
                logger.error("Embedding model not loaded; cannot compute hypothesis embedding.")
                return None
            sno.compute_hypothesis_embedding(self.embedding_model)
            
            self.extraction_stats['documents_processed'] += 1
            self.extraction_stats['snos_created'] += 1
            
            logger.info(f"Successfully created SNO: {sno.sno_id}")
            return sno
            
        except Exception as e:
            logger.error(f"Ingestion failed: {str(e)}")
            self.extraction_stats['extraction_failures'] += 1
            return None
    
    async def _extract_central_hypothesis(self, document_text: str) -> Optional[str]:
        """Extract the main claim or hypothesis from document text"""
        # Simplified extraction using heuristics
        # In production: use fine-tuned LLM with specific prompts
        
        sentences = document_text.split('.')
        
        # Look for sentences with hypothesis indicators
        hypothesis_indicators = [
            'we propose', 'we argue', 'we demonstrate', 'we show',
            'this paper', 'our findings', 'we conclude', 'we find'
        ]
        
        for sentence in sentences:
            sentence_lower = sentence.lower().strip()
            if any(indicator in sentence_lower for indicator in hypothesis_indicators):
                if len(sentence.strip()) > 20:  # Reasonable length
                    return sentence.strip()
        
        # Fallback: return first substantial sentence
        for sentence in sentences[:5]:  # Check first 5 sentences
            if len(sentence.strip()) > 30:
                return sentence.strip()
        
        return None
    
    async def _construct_reasoning_graph(self, sno: StructuredNarrativeObject, document_text: str):
        """Extract sub-claims and their relationships"""
        # Simplified implementation - in production, use advanced NLP
        
        sentences = [s.strip() for s in document_text.split('.') if len(s.strip()) > 20]
        
        # Add key sentences as claims
        claim_indicators = ['because', 'therefore', 'thus', 'furthermore', 'however', 'consequently']
        
        for i, sentence in enumerate(sentences[:10]):  # Limit for demo
            if any(indicator in sentence.lower() for indicator in claim_indicators):
                claim_id = sno.add_claim(sentence, claim_type="supporting_claim")
                
                # Simple heuristic: link to root if it contains supporting language
                if any(word in sentence.lower() for word in ['because', 'therefore', 'thus']):
                    try:
                        sno.add_reasoning_edge(claim_id, "root", RelationType.SUPPORTS)
                    except ValueError:
                        pass  # Skip if would create cycle
    
    async def _populate_evidence_set(self, 
                                   sno: StructuredNarrativeObject, 
                                   document_text: str, 
                                   source_metadata: Dict[str, Any]):
        """Link claims to evidence sources"""
        # Extract citations and references
        import re
        
        # Look for citation patterns
        citation_patterns = [
            r'\[(\d+)\]',  # [1], [2], etc.
            r'\(([^)]+\s+\d{4})\)',  # (Author 2023)
            r'doi:\s*([^\s]+)',  # DOI patterns
        ]
        
        evidence_items = []
        for pattern in citation_patterns:
            matches = re.findall(pattern, document_text)
            for match in matches:
                evidence_item = EvidenceItem(
                    content=f"Citation reference: {match}",
                    source_id=f"ref_{hash(match) % 10000}",
                    confidence=0.8
                )
                evidence_items.append(evidence_item)
        
        # Add document itself as evidence
        document_evidence = EvidenceItem(
            content=document_text[:500] + "..." if len(document_text) > 500 else document_text,
            source_id=source_metadata.get('doc_id', f"doc_{hash(document_text) % 10000}"),
            confidence=1.0
        )
        evidence_items.append(document_evidence)
        
        # Add all evidence to SNO
        for evidence in evidence_items:
            sno.add_evidence(evidence)

### From Paper to Code: A Research Challenge in Practice

The paper is very clear in Section 3.1 that the Narrative Ingestion Pipeline is a significant undertaking.

> **From the Paper (Section 3.1):**
> A critical prerequisite for the CNS ecosystem is the ability to generate SNOs from unstructured source materials... This process, a form of advanced argumentation mining, is a major research challenge in itself.

The paper then outlines a proposed three-step pipeline:
1. **Hypothesis Extraction:** Using an LLM to find the central claim.
2. **Reasoning Graph Construction:** Using an LLM to identify sub-claims and their relationships.
3. **Evidence Set Population:** Using pattern matching and semantic search to link claims to sources.

Our `NarrativeIngestionPipeline` class is a *pragmatic, first-pass implementation* of this research roadmap.

- `_extract_central_hypothesis`: Instead of a full LLM, we use heuristics (looking for keywords like "we propose," "we argue") as a simplified stand-in for Step 1.
- `_construct_reasoning_graph`: Similarly, this method uses simple keyword heuristics to find and link supporting claims, representing a basic version of Step 2.
- `_populate_evidence_set`: This method uses regular expressions (`re`) to find citation patterns, directly implementing the "pattern matching" aspect of Step 3.

This is a perfect example of how an engineering blueprint from a paper is translated into an initial, working prototype. Our implementation is a placeholder that demonstrates the system's structure, which can be iteratively improved with more sophisticated NLP and LLM-based models as outlined in the paper's research goals.

### Production Efficiency Enhancement

> **From Paper to Code: Model Management**
> Large models (embedding, NLI) should be loaded once at startup and reused across components rather than being loaded on-demand, which is highly inefficient. Our `CNSWorkflowManager` implements centralized model management for optimal resource usage.

class CNSWorkflowManager:
    """
    Manages the complete CNS 2.0 operational workflow.

    This class acts as the central orchestrator for the system. A key design
    principle for production efficiency is centralized model management: large ML models
    (for embedding and NLI) are loaded once at startup and passed to the relevant
    sub-components, avoiding costly re-loading for each task.
    """
    
    def __init__(self):
        self.sno_population: List[StructuredNarrativeObject] = []
        self.critic_pipeline = CriticPipeline()
        self.chiral_detector = ChiralPairDetector()
        self.synthesis_engine = None  # Will be implemented in next chapter
        
        # Centralized model storage
        self.embedding_model = None
        self.nli_model = None
        self.nli_tokenizer = None
        
        # System state
        self.is_running = False
        self.task_queue = PriorityQueue()
        self.metrics = SystemMetrics()
        self.start_time = datetime.now()
        
        # Load models and initialize components
        self._load_models()
        self.ingestion_pipeline = NarrativeIngestionPipeline(self.embedding_model)
        self._initialize_critics()
    
    def _load_models(self):
        """Loads all necessary ML models into memory at startup for efficient reuse"""
        logger.info("Loading ML models into memory...")
        
        if HAS_TRANSFORMERS:
            from sentence_transformers import SentenceTransformer
            import transformers
            
            # Load embedding model once for all components
            self.embedding_model = SentenceTransformer(cns_config.models['embedding'])
            
            # Load NLI model and tokenizer once for grounding critic
            self.nli_tokenizer = transformers.AutoTokenizer.from_pretrained(cns_config.models['nli'])
            self.nli_model = transformers.AutoModelForSequenceClassification.from_pretrained(cns_config.models['nli'])
            
            logger.info("All models loaded successfully.")
        else:
            logger.warning("Transformers library not available - using fallback implementations")
    
    def _initialize_critics(self):
        """Set up the critic pipeline with pre-loaded models for efficiency"""
        # Initialize critics with parameters from cns_config and pre-loaded models
        grounding_critic = GroundingCritic(
            weight=cns_config.critic_weights['grounding'],
            nli_model=self.nli_model,
            nli_tokenizer=self.nli_tokenizer
        )
        logic_critic = LogicCritic(
            weight=cns_config.critic_weights['logic']
        )
        novelty_critic = NoveltyParsimonyCritic(
            weight=cns_config.critic_weights['novelty'],
            alpha=cns_config.novelty_alpha,
            beta=cns_config.novelty_beta
        )
        
        self.critic_pipeline.add_critic(grounding_critic)
        self.critic_pipeline.add_critic(logic_critic)
        self.critic_pipeline.add_critic(novelty_critic)
        
        logger.info("Research-grade critic pipeline initialized with pre-loaded models for maximum efficiency")
    
    async def start_system(self):
        """Start the CNS 2.0 system operational loop"""
        self.is_running = True
        self.start_time = datetime.now()
        
        logger.info("CNS 2.0 System starting...")
        
        # Start concurrent processing tasks
        tasks = [
            asyncio.create_task(self._process_task_queue()),
            asyncio.create_task(self._synthesis_loop()),
            asyncio.create_task(self._metrics_update_loop())
        ]
        
        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            logger.info("Shutdown requested")
            await self.shutdown_system()
    
    async def _process_task_queue(self):
        """Process incoming tasks from the priority queue"""
        while self.is_running:
            try:
                if not self.task_queue.empty():
                    task = self.task_queue.get_nowait()
                    await self._execute_task(task)
                else:
                    await asyncio.sleep(1)  # Prevent busy waiting
            except Exception as e:
                logger.error(f"Task processing error: {str(e)}")
    
    async def _execute_task(self, task: ProcessingTask):
        """Execute a specific task based on its type"""
        try:
            if task.task_type == 'ingest':
                await self._handle_ingestion_task(task)
            elif task.task_type == 'evaluate':
                await self._handle_evaluation_task(task)
            elif task.task_type == 'synthesize':
                await self._handle_synthesis_task(task)
            else:
                logger.warning(f"Unknown task type: {task.task_type}")
        except Exception as e:
            logger.error(f"Task execution failed: {task.task_id} - {str(e)}")
    
    async def _handle_ingestion_task(self, task: ProcessingTask):
        """Handle document ingestion tasks"""
        document_text = task.payload.get('document_text')
        source_metadata = task.payload.get('source_metadata', {})
        
        if document_text:
            sno = await self.ingestion_pipeline.ingest_document(document_text, source_metadata)
            if sno:
                # Evaluate the new SNO with population context
                context = {'sno_population': self.sno_population}
                evaluation_result = self.critic_pipeline.evaluate_sno(sno, context)
                
                # Add to population if it meets quality threshold
                if sno.trust_score and sno.trust_score > 0.3:
                    self.sno_population.append(sno)
                    self.metrics.total_snos += 1
                    logger.info(f"Added SNO to population: {sno.sno_id} (trust: {sno.trust_score:.3f})")
                else:
                    logger.info(f"SNO rejected due to low trust score: {sno.trust_score}")
    
    async def _handle_evaluation_task(self, task: ProcessingTask):
        """Handle SNO re-evaluation tasks"""
        sno_id = task.payload.get('sno_id')
        sno = next((s for s in self.sno_population if s.sno_id == sno_id), None)
        
        if sno:
            context = {'sno_population': self.sno_population}
            evaluation_result = self.critic_pipeline.evaluate_sno(sno, context)
            logger.info(f"Re-evaluated SNO {sno_id}: trust={sno.trust_score:.3f}")
    
    async def _handle_synthesis_task(self, task: ProcessingTask):
        """Handle synthesis generation tasks by calling the synthesis engine."""
        chiral_pair = task.payload.get('chiral_pair')
        if not chiral_pair or not self.synthesis_engine:
            logger.warning(f"Synthesis task {task.task_id} failed: missing pair or engine.")
            return

        self.metrics.active_syntheses += 1
        synthesis_result = await self.synthesis_engine.synthesize_chiral_pair(chiral_pair)
        self.metrics.active_syntheses -= 1

        if synthesis_result.success:
            self.metrics.successful_syntheses += 1
            new_sno = synthesis_result.synthesized_sno
            # Add the new, successful SNO to the population
            self.sno_population.append(new_sno)
            self.metrics.total_snos += 1
            logger.info(f"New synthesized SNO {new_sno.sno_id} added to population.")
        else:
            self.metrics.failed_syntheses += 1
            logger.warning(f"Synthesis failed for task {task.task_id}: {synthesis_result.explanation}")
    
    async def _synthesis_loop(self):
        """Continuously look for synthesis opportunities"""
        while self.is_running:
            try:
                if len(self.sno_population) >= 2:
                    # Find chiral pairs
                    chiral_pairs = self.chiral_detector.find_chiral_pairs(self.sno_population, max_pairs=5)
                    
                    if chiral_pairs:
                        logger.info(f"Found {len(chiral_pairs)} chiral pairs for potential synthesis")
                        
                        for pair in chiral_pairs:
                            # Queue synthesis task
                            synthesis_task = ProcessingTask(
                                task_id=f"synthesis_{pair.sno_a.sno_id[:8]}_{pair.sno_b.sno_id[:8]}",
                                task_type="synthesize",
                                priority=1,  # High priority
                                payload={'chiral_pair': pair}
                            )
                            self.task_queue.put(synthesis_task)
                
                await asyncio.sleep(30)  # Check for synthesis opportunities every 30 seconds
                
            except Exception as e:
                logger.error(f"Synthesis loop error: {str(e)}")
    
    async def _metrics_update_loop(self):
        """Periodically update system metrics"""
        while self.is_running:
            try:
                # Update metrics
                self.metrics.uptime = datetime.now() - self.start_time
                
                if self.sno_population:
                    trust_scores = [sno.trust_score for sno in self.sno_population if sno.trust_score is not None]
                    self.metrics.average_trust_score = np.mean(trust_scores) if trust_scores else 0.0
                
                # Calculate processing rate
                hours = self.metrics.uptime.total_seconds() / 3600
                self.metrics.processing_rate = self.metrics.total_snos / hours if hours > 0 else 0.0
                
                # Log metrics every 5 minutes
                logger.info(f"System metrics: {json.dumps(self.metrics.to_dict(), indent=2)}")
                
                await asyncio.sleep(300)  # Update every 5 minutes
                
            except Exception as e:
                logger.error(f"Metrics update error: {str(e)}")
    
    async def shutdown_system(self):
        """Gracefully shutdown the CNS 2.0 system"""
        self.is_running = False
        logger.info("CNS 2.0 System shutting down...")
        
        # Save system state
        await self._save_system_state()
        
        logger.info("System shutdown complete")
    
    async def _save_system_state(self):
        """Save current system state for persistence"""
        state = {
            'sno_count': len(self.sno_population),
            'metrics': self.metrics.to_dict(),
            'ingestion_stats': self.ingestion_pipeline.extraction_stats,
            'critic_stats': {ct.value: c.get_statistics() for ct, c in self.critic_pipeline.critics.items()}
        }
        
        # In production, save to persistent storage
        logger.info(f"System state: {json.dumps(state, indent=2)}")
    
    def submit_document(self, document_text: str, source_metadata: Dict[str, Any] = None):
        """Submit a document for processing"""
        if source_metadata is None:
            source_metadata = {}
        
        task = ProcessingTask(
            task_id=f"ingest_{datetime.now().timestamp()}",
            task_type="ingest",
            priority=2,
            payload={
                'document_text': document_text,
                'source_metadata': source_metadata
            }
        )
        
        self.task_queue.put(task)
        logger.info(f"Document submitted for ingestion: {task.task_id}")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            'is_running': self.is_running,
            'population_size': len(self.sno_population),
            'queue_size': self.task_queue.qsize(),
            'metrics': self.metrics.to_dict(),
            'uptime': str(self.metrics.uptime)
        }

# Example usage and testing
async def demo_system_integration():
    """Demonstrate the integrated CNS 2.0 system"""
    
    # Initialize system
    workflow_manager = CNSWorkflowManager()
    
    # Submit sample documents
    sample_documents = [
        {
            'text': "We propose that machine learning algorithms can effectively identify patterns in complex datasets. Our experiments demonstrate significant improvements in accuracy when using ensemble methods. The evidence strongly supports the hypothesis that combining multiple models leads to better performance.",
            'metadata': {'title': 'ML Ensemble Study', 'author': 'Research Team A'}
        },
        {
            'text': "We argue that simple models often outperform complex ensembles in real-world scenarios. Our analysis shows that overly complex models tend to overfit and perform poorly on new data. The results contradict claims about ensemble superiority.",
            'metadata': {'title': 'Simplicity in ML', 'author': 'Research Team B'}
        }
    ]
    
    for doc in sample_documents:
        workflow_manager.submit_document(doc['text'], doc['metadata'])
    
    print("Sample documents submitted to CNS 2.0 system")
    print("System would process these through the complete pipeline:")
    print("1. Narrative ingestion and SNO creation")
    print("2. Multi-component critic evaluation") 
    print("3. Chiral pair detection")
    print("4. Synthesis generation (Chapter 6)")
    
    return workflow_manager

if __name__ == "__main__":
    # Run the demo
    asyncio.run(demo_system_integration())
