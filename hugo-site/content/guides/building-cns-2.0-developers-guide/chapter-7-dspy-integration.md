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

#### Why Use a Graded Metric?
A simple binary metric (e.g., `1.0` if the structure is perfect, `0.0` otherwise) provides a very weak signal to the DSPy optimizer. The optimizer works by trying different prompts, and if it only receives a score of `0.0` for most of its attempts, it has no way of knowing if one failed attempt was "more correct" than another.

A **graded metric** that provides partial credit is far more effective. It creates a smoother optimization landscape. For example:
- A prompt that correctly extracts the hypothesis but fails on the claims gets a score of `0.5`.
- A prompt that gets the hypothesis and also produces a list (even if the list items are malformed) gets `0.75`.

This gradient gives the optimizer a clear direction for improvement. It can learn what works for one part of the output and then refine the prompt to solve the remaining parts, leading to much faster and more reliable optimization.

# --- 6. Optimize (Compile) the Module ---
# (The training examples and optimization process remain the same, but now use the graded metric)
# optimizer = BootstrapFewShot(metric=graded_sno_structure_metric, max_bootstrapped_demos=2)
# optimized_ingestion_module = optimizer.compile(SNOIngestionModule(), trainset=train_examples)
```

This graded metric allows the DSPy compiler to "hill-climb" towards better prompts more effectively, rewarding prompts that, for example, correctly extract the hypothesis even if they fail on the claims structure.

## Closing the Loop: A Self-Optimizing Synthesis Engine

The true power of combining CNS 2.0 and DSPy is realized when we turn the system's critical judgment upon itself. We can use our own **Critic Pipeline** as the metric to optimize the **Synthesis Engine**. This creates a feedback loop where the system learns to generate syntheses that it itself considers to be high-quality. This fulfills the vision from the paper of a system capable of "continuous improvement."

The diagram below illustrates this self-optimizing loop. The goal is to "compile" a `SynthesisModule` that is optimized to produce SNOs that score highly on our `CriticPipeline` metric.

<div style="text-align: center;">
  <img src="/img/diagram-02.svg" alt="Centered SVG" style="display: inline-block;" />
</div>

This process allows the system to programmatically discover what makes a "good" synthesis from its own perspective. It will tune the prompts and few-shot examples used by the `SynthesisModule` until it reliably produces outputs that are logical, well-grounded, and novel according to our own critics.

### 1. Define the Synthesis Signature

First, we define what we want the synthesis LLM to do. It should take two conflicting narratives and produce a new, unified hypothesis.

```python
class ChiralPairToSynthesis(dspy.Signature):
    """
    Given two conflicting narratives, generate a novel, higher-order hypothesis that resolves the conflict.
    This signature defines the inputs and outputs for our synthesis task. The descriptions (`desc`)
    are crucial, as they are used by the DSPy optimizer to construct effective prompts.
    """
    narrative_A: str = dspy.InputField(desc="The first narrative, including its central hypothesis and key supporting claims.")
    narrative_B: str = dspy.InputField(desc="The second, conflicting narrative, including its central hypothesis and key supporting claims.")
    shared_evidence: str = dspy.InputField(desc="A summary of the key evidence that both narratives are trying to explain.")

    synthesized_hypothesis: str = dspy.OutputField(desc="A new, single-sentence hypothesis that resolves the conflict and synthesizes the core insights of both narratives.")
```

### 2. Create the Synthesis Module

Next, we create a DSPy module that uses this signature. A module is a reusable component that encapsulates a specific LLM behavior.

```python
class SynthesisModule(dspy.Module):
    """A DSPy module for synthesizing conflicting narratives."""
    def __init__(self):
        super().__init__()
        # We define the LLM reasoning strategy here. `dspy.ChainOfThought` tells the LLM
        # to "think step-by-step" to arrive at the answer, which is effective for
        # complex reasoning tasks like synthesis.
        self.synthesizer = dspy.ChainOfThought(ChiralPairToSynthesis)

    def forward(self, narrative_A, narrative_B, shared_evidence):
        """The forward method defines how data flows through the module."""
        return self.synthesizer(narrative_A=narrative_A, narrative_B=narrative_B, shared_evidence=shared_evidence)
```

### 3. The Critic Pipeline as a Metric

This is the core of the self-improvement loop. We create a metric function that takes a predicted `synthesized_hypothesis`, builds a new SNO from it, and then runs that SNO through our full `CriticPipeline`. The resulting `trust_score` is the metric that DSPy will try to maximize.

```python
def critic_pipeline_metric(cns_workflow_manager, example, pred, trace=None) -> float:
    """
    Uses the entire CNS critic pipeline to evaluate the quality of a synthesized hypothesis.
    This function is the bridge between DSPy's optimization and our system's own judgment.

    Args:
        cns_workflow_manager: An instance of our main workflow manager to access the critics.
        example: The input example from the training set.
        pred: The prediction object from the DSPy module.
        trace: The execution trace (unused here, but required by the metric signature).

    Returns:
        A float score from 0.0 to 1.0, where 1.0 is a perfect score.
    """
    try:
        # 1. Extract the predicted hypothesis from the DSPy prediction object.
        synthesized_hypothesis = pred.synthesized_hypothesis

        # 2. Perform basic validation. An invalid or trivial output gets the worst possible score.
        if not isinstance(synthesized_hypothesis, str) or len(synthesized_hypothesis) < 20:
            return 0.0

        # 3. Instantiate a candidate SNO from the LLM's generated hypothesis.
        #    In a full implementation, you would also populate its reasoning graph and
        #    evidence set by combining elements from the parent SNOs in the `example`.
        candidate_sno = StructuredNarrativeObject(central_hypothesis=synthesized_hypothesis)

        # We must compute its embedding to allow the Novelty critic to work.
        candidate_sno.compute_hypothesis_embedding(cns_workflow_manager.embedding_model)

        # 4. The Novelty Critic needs the existing SNO population to compare against.
        #    We provide the full SNO population as context for the evaluation.
        context = {'sno_population': cns_workflow_manager.sno_population}

        # 5. Run the candidate SNO through our complete, multi-component critic pipeline.
        #    This is the core of the feedback loop.
        evaluation_result = cns_workflow_manager.critic_pipeline.evaluate_sno(candidate_sno, context)

        # 6. The final, holistic trust_score produced by our pipeline is the metric.
        #    DSPy's optimizer will now tune the synthesizer's prompts to maximize this score.
        trust_score = evaluation_result.get('trust_score', 0.0)

        return trust_score
    except Exception as e:
        # If any part of the process fails (e.g., malformed prediction), return a score of 0.0.
        # This penalizes prompts that produce unusable outputs.
        logger.error(f"Critic pipeline metric failed: {e}")
        return 0.0
```

### 4. Compiling the Self-Optimizing Synthesizer

With the signature, module, and metric defined, we can now compile our `SynthesisModule`. The optimizer will try different prompts and few-shot examples for the synthesis task, and for each attempt, it will check the quality of the output using the `critic_pipeline_metric`. It will learn to generate hypotheses that are well-grounded, logical, and novel *according to the system's own internal criteria*.

```python
# Assume 'cns_manager' is an instance of our CNSWorkflowManager containing the critic pipeline.
# We wrap our metric in a lambda function to pass the cns_manager instance into it.
# This gives our metric access to the critics and the full SNO population.
metric_with_context = lambda ex, pred, trace: critic_pipeline_metric(cns_manager, ex, pred, trace)

# We choose an optimizer. `BootstrapFewShot` is a powerful choice that generates
# both high-quality prompts and effective few-shot examples for the module.
optimizer = BootstrapFewShot(metric=metric_with_context, max_bootstrapped_demos=2)

# We need a small set of training examples. These don't need to have "correct" output labels,
# as the metric provides the signal for what is good. We just need representative inputs.
synthesis_train_examples = [
    dspy.Example(
        narrative_A="Hypothesis: AI regulation stifles innovation. Claims: Excessive rules slow down development.",
        narrative_B="Hypothesis: AI regulation is essential for safety. Claims: Unchecked AI poses existential risks.",
        shared_evidence="The rapid development of large language models."
    ).with_inputs('narrative_A', 'narrative_B', 'shared_evidence'),
    # ... more examples of conflicting pairs would be added here
]

# This is the "compilation" step. The optimizer will run the SynthesisModule on the
# training examples, evaluate the outputs with our critic_pipeline_metric, and use the
# feedback to iteratively improve the prompts and few-shot examples inside the module.
optimized_synthesis_module = optimizer.compile(SynthesisModule(), trainset=synthesis_train_examples)
```

By integrating DSPy in this way, we have transformed the CNS 2.0 system from a static implementation into a dynamic, learning framework. It not only automates knowledge synthesis but now has the programmatic capability to get better at its own core task over time, truly fulfilling the vision of the original research paper.

## Conclusion: From Blueprint to Dynamic System

This guide has walked through the process of translating the CNS 2.0 research paper from a theoretical blueprint into a practical, working system. We have built each component step-by-step: the core `StructuredNarrativeObject`, the transparent `CriticPipeline`, the scalable `ChiralPairDetector`, and the `AdvancedSynthesisEngine`.

Finally, by integrating DSPy, we have shown a path from a static system to a dynamic one—a system that can programmatically optimize and improve its own reasoning capabilities. This closing of the loop, where the system's own judgment is used to refine its generative components, represents a key step toward the goal of automated, robust, and continuously improving knowledge discovery.
