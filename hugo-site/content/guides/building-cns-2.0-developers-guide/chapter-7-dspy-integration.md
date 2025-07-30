---
title: "Chapter 7: Advanced Optimization with DSPy"
description: "Evolving CNS 2.0 from prompt engineering to programmatic optimization using DSPy"
weight: 7
---

<div class="guide-header">
    <a href="/" class="home-link">← Back to GTCode.com Homepage</a>
</div>

# Chapter 7: Advanced Optimization with DSPy

## From Prompting to Programming

Throughout this guide, we have assumed that a developer would write fixed prompts to instruct the LLMs in our system. This approach, often called "prompt engineering," has critical weaknesses: a prompt that works well on one model (e.g., GPT-4) may fail on another (e.g., Llama 3), and it's difficult to systematically optimize.

To create a truly robust, self-improving system, we must move from *prompting* to *programming*. This is where **DSPy** comes in.

### What is DSPy and Why Use It?
DSPy is a framework that changes how we build systems with LLMs. Instead of writing specific prompts, we define the building blocks of our program and the metric we want to maximize. The DSPy "compiler" then does the hard work of generating and optimizing the best possible prompts and few-shot examples for our specific task and model.

The core concepts are:
-   **Signatures**: These are like function signatures or type hints for LLMs. They declaratively define the inputs and outputs we need (e.g., `document -> hypothesis`).
-   **Modules**: These are the reusable building blocks of our program. A module takes a signature and defines how to use it to call an LLM (e.g., as a simple call or a chain-of-thought).
-   **Optimizers (Compilers)**: This is where the magic happens. An optimizer (like `BootstrapFewShot`) takes your modules, a metric for success, and a small amount of training data. It then runs a series of experiments to find the best prompt and few-shot examples to maximize your metric.

This approach turns brittle prompt engineering into a systematic, programmatic optimization process.

## Solving the Ingestion Challenge with DSPy

The CNS 2.0 paper identifies the **Narrative Ingestion Pipeline** as a "major research challenge." Instead of manually guessing prompts to extract a hypothesis and claims from a document, we can use DSPy to solve this programmatically.

A key improvement here is using a **graded evaluation metric** instead of a simple binary one. A graded metric provides a much richer signal to the optimizer, allowing it to find and refine partially correct solutions.

```python
# ... (DSPy setup and Pydantic model definitions remain the same) ...

# 3. Define the DSPy Signature for the ingestion task
class DocumentToSNO(dspy.Signature):
    """Extracts the central hypothesis and a structured list of claims from a document."""
    document_text: str = dspy.InputField(desc="The full text of the source document.")
    central_hypothesis: str = dspy.OutputField(desc="A single, concise sentence summarizing the main argument.")
    claims: List[ExtractedClaim] = dspy.OutputField(desc="A structured list of key claims and relationships.")

# 4. Create the DSPy Module to execute the signature
class SNOIngestionModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # Use ChainOfThought to encourage the LLM to "think step-by-step"
        self.generate_structure = dspy.ChainOfThought(DocumentToSNO)

    def forward(self, document_text):
        return self.generate_structure(document_text=document_text)

# 5. Create a Graded Evaluation Metric
def graded_sno_structure_metric(example, pred, trace=None) -> float:
    # ... (Implementation of the graded metric remains the same) ...
```

#### Why Use a Graded Metric?
A simple binary metric (e.g., `1.0` if the structure is perfect, `0.0` otherwise) provides a very weak signal to the DSPy optimizer. If most of its attempts score `0.0`, it has no way of knowing if one failed attempt was "more correct" than another.

A **graded metric** that provides partial credit is far more effective. It creates a smoother optimization landscape. For example, a prompt that correctly extracts the hypothesis (`score += 0.5`) but fails on the claims is clearly better than one that fails at both. This gradient gives the optimizer a clear direction for improvement, leading to much faster and more reliable optimization.

## The Ultimate Goal: A Self-Optimizing Synthesis Engine

The true power of combining CNS 2.0 and DSPy is realized when we turn the system's critical judgment upon itself. We can use our own **Critic Pipeline** as the metric to optimize the **Synthesis Engine**. This creates a feedback loop where the system learns to generate syntheses that it itself considers to be high-quality, fulfilling the paper's vision of a system capable of "continuous improvement."

The diagram below illustrates this self-optimizing loop. The goal is to "compile" a `SynthesisModule` that is optimized to produce SNOs that score highly on our `CriticPipeline` metric.

<div style="text-align: center;">
  <img src="/img/diagram-02.svg" alt="Centered SVG" style="display: inline-block;" />
</div>

This process allows the system to programmatically discover what makes a "good" synthesis from its own perspective. It will tune the prompts and few-shot examples used by the `SynthesisModule` until it reliably produces outputs that are logical, well-grounded, and novel according to our own critics.

### 1. Define the Synthesis Signature & Module

First, we define the desired input/output behavior for our synthesis task. Then we wrap it in a `dspy.Module`.

```python
class ChiralPairToSynthesis(dspy.Signature):
    """Given two conflicting narratives, generate a novel, higher-order hypothesis that resolves the conflict."""
    narrative_A: str = dspy.InputField(desc="The first narrative, including its central hypothesis and key supporting claims.")
    narrative_B: str = dspy.InputField(desc="The second, conflicting narrative, including its central hypothesis and key supporting claims.")
    shared_evidence: str = dspy.InputField(desc="A summary of the key evidence that both narratives are trying to explain.")
    synthesized_hypothesis: str = dspy.OutputField(desc="A new, single-sentence hypothesis that resolves the conflict and synthesizes the core insights of both narratives.")

class SynthesisModule(dspy.Module):
    """A DSPy module for synthesizing conflicting narratives."""
    def __init__(self):
        super().__init__()
        self.synthesizer = dspy.ChainOfThought(ChiralPairToSynthesis)

    def forward(self, narrative_A, narrative_B, shared_evidence):
        return self.synthesizer(narrative_A=narrative_A, narrative_B=narrative_B, shared_evidence=shared_evidence)
```

### 2. The Critic Pipeline as a Metric

This is the core of the self-improvement loop. We create a metric function that takes a predicted `synthesized_hypothesis`, builds a new SNO from it, and then runs that SNO through our full `CriticPipeline`. The resulting `trust_score` is the metric that DSPy will try to maximize.

```python
def critic_pipeline_metric(cns_workflow_manager, example, pred, trace=None) -> float:
    """
    Uses the entire CNS critic pipeline to evaluate the quality of a synthesized hypothesis.
    This function is the bridge between DSPy's optimization and our system's own judgment.
    """
    try:
        # Step 1: Extract the predicted hypothesis from the DSPy prediction object.
        synthesized_hypothesis = pred.synthesized_hypothesis

        # Step 2: Perform basic validation. An invalid or trivial output gets the worst score.
        if not isinstance(synthesized_hypothesis, str) or len(synthesized_hypothesis) < 20:
            return 0.0

        # Step 3: Instantiate a candidate SNO from the LLM's generated hypothesis.
        # This turns the raw text output into a rich, structured object.
        candidate_sno = StructuredNarrativeObject(central_hypothesis=synthesized_hypothesis)
        candidate_sno.compute_hypothesis_embedding(cns_workflow_manager.embedding_model)

        # Step 4: Prepare the context for evaluation. The Novelty Critic needs to see
        # the existing SNO population to do its job.
        context = {'sno_population': cns_workflow_manager.sno_population}

        # Step 5: THE CORE OF THE LOOP. Run the candidate SNO through our complete,
        # multi-component critic pipeline from Chapter 3.
        evaluation_result = cns_workflow_manager.critic_pipeline.evaluate_sno(candidate_sno, context)

        # Step 6: The final, holistic trust_score produced by our pipeline is the metric.
        # DSPy's optimizer will now tune the synthesizer's prompts to maximize this score.
        trust_score = evaluation_result.get('trust_score', 0.0)
        return trust_score

    except Exception as e:
        # Penalize any prompt that produces an output that breaks our system.
        logger.error(f"Critic pipeline metric failed: {e}")
        return 0.0
```

### 3. Compiling the Self-Optimizing Synthesizer

With the signature, module, and metric defined, we can now "compile" our `SynthesisModule`. The optimizer will try different prompts for the synthesis task, and for each attempt, it will check the quality of the output using our `critic_pipeline_metric`. It will learn to generate hypotheses that are well-grounded, logical, and novel *according to the system's own internal criteria*.

```python
# Assume 'cns_manager' is an instance of our CNSWorkflowManager.
# We wrap our metric in a lambda to pass the cns_manager instance into it.
metric_with_context = lambda ex, pred, trace: critic_pipeline_metric(cns_manager, ex, pred, trace)

# We choose an optimizer. `BootstrapFewShot` generates both high-quality
# prompts and effective few-shot examples.
optimizer = BootstrapFewShot(metric=metric_with_context, max_bootstrapped_demos=2)

# We only need a small set of representative inputs for the optimizer to work with.
# Note that we don't need to provide the "correct" synthesized output; the metric does that.
synthesis_train_examples = [
    dspy.Example(
        narrative_A="Hypothesis: AI regulation stifles innovation. Claims: Excessive rules slow down development.",
        narrative_B="Hypothesis: AI regulation is essential for safety. Claims: Unchecked AI poses existential risks.",
        shared_evidence="The rapid development of large language models."
    ).with_inputs('narrative_A', 'narrative_B', 'shared_evidence'),
    # ... more examples of conflicting pairs ...
]

# This is the compilation step. DSPy runs a series of experiments: it generates
# new prompts for the SynthesisModule, gets the output, and scores it with our
# critic pipeline. Over many iterations, it finds the prompt that maximizes the
# trust score, effectively teaching the synthesizer what we value.
optimized_synthesis_module = optimizer.compile(SynthesisModule(), trainset=synthesis_train_examples)
```

## Conclusion: From Blueprint to a Dynamic System

This guide has walked through the entire process of translating the CNS 2.0 research paper from a theoretical blueprint into a practical, working system. We have built each component step-by-step: the core `StructuredNarrativeObject`, the transparent `CriticPipeline`, the scalable `ChiralPairDetector`, and the `AdvancedSynthesisEngine`. We have shown how to assemble these components into a continuous, autonomous system and how to deploy that system in a robust, scalable production environment.

Finally, by integrating DSPy, we have shown a path from a static system to a dynamic one—a system that can programmatically optimize and improve its own reasoning capabilities. This closing of the loop, where the system's own judgment is used to refine its generative components, represents a key step toward the goal of automated, robust, and continuously improving knowledge discovery.
