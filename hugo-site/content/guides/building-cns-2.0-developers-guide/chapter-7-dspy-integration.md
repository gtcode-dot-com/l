---
title: "Chapter 7: Advanced Optimization with DSPy"
description: "Evolving CNS 2.0 from prompt engineering to programmatic optimization using DSPy"
weight: 7
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 7: Advanced Optimization with DSPy

## From Prompt Engineering to Programmatic Optimization

Our CNS 2.0 system relies on hand-crafted prompts to instruct LLMs. This approach has critical weaknesses: it's brittle across different LLM versions, hard to compose, and difficult to optimize. To create a truly robust, self-improving system, we must move from *prompting* to *programming*. This is where **DSPy** comes in.

DSPy is a framework for programming LLMs. We define the logic of our program and the metric we want to maximize, and DSPy's optimizers (or "compilers") automatically find the best prompts and few-shot examples to achieve that goal.

### From Paper to Code: Tackling the Research Challenge

The CNS 2.0 paper identifies the **Narrative Ingestion Pipeline** as a "major research challenge." DSPy provides the framework to solve this programmatically. Instead of guessing prompts to extract a hypothesis and claims, we can define what a "good" extraction looks like with a metric and let a DSPy optimizer do the work.

## Refactoring Ingestion with an Improved DSPy Metric

Our first step is to refactor the ingestion pipeline with DSPy. A key improvement here is using a **graded evaluation metric** instead of a simple binary one. A graded metric provides a much richer signal to the optimizer, allowing it to find and refine partially correct solutions.

```python
"""
Chapter 7: Optimizing Narrative Ingestion with DSPy
===================================================
Refactoring the CNS 2.0 Ingestion Pipeline for robustness and performance.
"""

import dspy
from pydantic import BaseModel, Field
from typing import List

# --- 1. Configure DSPy ---
# (Assume dspy.OpenAI is configured as before)

# --- 2. Define Structured Output ---
class ExtractedClaim(BaseModel):
    claim_id: str = Field(description="A unique identifier for the claim, e.g., 'claim_1'")
    content: str = Field(description="The text content of the claim.")
    claim_type: str = Field(description="The type of claim, e.g., 'premise', 'conclusion'.")
    relationships: List[str] = Field(description="List of claim_ids this claim supports or contradicts.")

# --- 3. Define the DSPy Signature ---
class DocumentToSNO(dspy.Signature):
    """Extracts the central hypothesis and a structured list of claims from a document."""
    document_text: str = dspy.InputField(desc="The full text of the source document.")
    central_hypothesis: str = dspy.OutputField(desc="A single, concise sentence summarizing the document's main argument.")
    claims: List[ExtractedClaim] = dspy.OutputField(desc="A structured list of key claims and their relationships from the document.")

# --- 4. Create the DSPy Module ---
class SNOIngestionModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_structure = dspy.ChainOfThought(DocumentToSNO)

    def forward(self, document_text):
        return self.generate_structure(document_text=document_text)

# --- 5. Create a Graded Evaluation Metric ---
def graded_sno_structure_metric(example, pred, trace=None) -> float:
    """
    A graded metric that provides partial credit for partially correct structures.
    This gives the optimizer a much better signal for improvement.
    """
    score = 0.0
    try:
        # Award points for a valid, non-trivial hypothesis
        if isinstance(pred.central_hypothesis, str) and len(pred.central_hypothesis) > 20:
            score += 0.5
        
        # Award points for a correctly typed list of claims
        if isinstance(pred.claims, list):
            score += 0.25

            # Award final points if the list contains valid ExtractedClaim objects
            if len(pred.claims) > 0 and all(isinstance(c, ExtractedClaim) for c in pred.claims):
                score += 0.25
    except Exception:
        # The prediction was so malformed it caused an error.
        return 0.0

    return score

# --- 6. Optimize (Compile) the Module ---
# (The training examples and optimization process remain the same, but now use the graded metric)
# optimizer = BootstrapFewShot(metric=graded_sno_structure_metric, max_bootstrapped_demos=2)
# optimized_ingestion_module = optimizer.compile(SNOIngestionModule(), trainset=train_examples)
```

This graded metric allows the DSPy compiler to "hill-climb" towards better prompts more effectively, rewarding prompts that, for example, correctly extract the hypothesis even if they fail on the claims structure.

## Closing the Loop: A Self-Optimizing Synthesis Engine

The true power of combining CNS 2.0 and DSPy is realized when we turn the system's critical judgment upon itself. We can use our own **Critic Pipeline** as the metric to optimize the **Synthesis Engine**. This creates a feedback loop where the system learns to generate syntheses that it itself considers to be high-quality.

This fulfills the vision from the paper of a system capable of "continuous improvement."

### 1. Define the Synthesis Signature

First, we define what we want the synthesis LLM to do. It should take two conflicting narratives and produce a new, unified hypothesis.

```python
class ChiralPairToSynthesis(dspy.Signature):
    """
    Given two conflicting narratives, generate a novel, higher-order hypothesis that resolves the conflict.
    """
    narrative_A: str = dspy.InputField(desc="The first narrative, including its central hypothesis and key supporting claims.")
    narrative_B: str = dspy.InputField(desc="The second, conflicting narrative, including its central hypothesis and key supporting claims.")
    shared_evidence: str = dspy.InputField(desc="A summary of the key evidence that both narratives are trying to explain.")

    synthesized_hypothesis: str = dspy.OutputField(desc="A new, single-sentence hypothesis that resolves the conflict and synthesizes the core insights of both narratives.")
```

### 2. Create the Synthesis Module

Next, we create a DSPy module that uses this signature.

```python
class SynthesisModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # We can experiment with different modules, e.g., dspy.ReAct for more complex reasoning
        self.synthesizer = dspy.ChainOfThought(ChiralPairToSynthesis)

    def forward(self, narrative_A, narrative_B, shared_evidence):
        return self.synthesizer(narrative_A=narrative_A, narrative_B=narrative_B, shared_evidence=shared_evidence)
```

### 3. The Critic Pipeline as a Metric

This is the core of the self-improvement loop. We create a metric function that takes a predicted `synthesized_hypothesis`, builds a new SNO from it, and then runs that SNO through our full `CriticPipeline`. The resulting `trust_score` is the metric that DSPy will try to maximize.

```python
def critic_pipeline_metric(cns_workflow_manager, example, pred, trace=None) -> float:
    """
    Uses the entire CNS critic pipeline to evaluate the quality of a synthesized hypothesis.
    """
    try:
        synthesized_hypothesis = pred.synthesized_hypothesis
        if not isinstance(synthesized_hypothesis, str) or len(synthesized_hypothesis) < 20:
            return 0.0

        # Create a new SNO from the synthesized hypothesis
        # In a real scenario, you'd also populate its graph and evidence from the source SNOs
        candidate_sno = StructuredNarrativeObject(central_hypothesis=synthesized_hypothesis)

        # We need context (the existing population) for the Novelty Critic to work
        context = {'sno_population': cns_workflow_manager.sno_population}

        # Run the full critic pipeline on the new SNO
        evaluation_result = cns_workflow_manager.critic_pipeline.evaluate_sno(candidate_sno, context)

        # The final trust score is our metric!
        trust_score = evaluation_result.get('trust_score', 0.0)

        return trust_score
    except Exception as e:
        logger.error(f"Critic pipeline metric failed: {e}")
        return 0.0
```

### 4. Compiling the Self-Optimizing Synthesizer

With the signature, module, and metric defined, we can now compile our `SynthesisModule`. The optimizer will try different prompts and few-shot examples for the synthesis task, and for each attempt, it will check the quality of the output using the `critic_pipeline_metric`. It will learn to generate hypotheses that are well-grounded, logical, and novel *according to the system's own internal criteria*.

```python
# Assume 'cns_manager' is an instance of our CNSWorkflowManager
# We wrap our metric in a lambda to pass the manager instance to it.
optimizer = BootstrapFewShot(metric=lambda ex, pred, trace: critic_pipeline_metric(cns_manager, ex, pred, trace))

# We need training examples of chiral pairs
synthesis_train_examples = [
    dspy.Example(
        narrative_A="Hypothesis: AI regulation stifles innovation. Claims: Excessive rules slow down development.",
        narrative_B="Hypothesis: AI regulation is essential for safety. Claims: Unchecked AI poses existential risks.",
        shared_evidence="The rapid development of large language models."
    ).with_inputs('narrative_A', 'narrative_B', 'shared_evidence'),
    # ... more examples of conflicting pairs
]

# This compilation step creates a synthesizer that is optimized
# to produce high-trust-score outputs.
optimized_synthesis_module = optimizer.compile(SynthesisModule(), trainset=synthesis_train_examples)
```

By integrating DSPy in this way, we have transformed the CNS 2.0 system from a static implementation into a dynamic, learning framework. It not only automates knowledge synthesis but now has the programmatic capability to get better at its own core task over time, truly fulfilling the vision of the original research paper.
