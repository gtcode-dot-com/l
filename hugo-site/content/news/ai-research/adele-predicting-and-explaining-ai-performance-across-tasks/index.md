---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T05:35:21.311961+00:00'
exported_at: '2026-04-02T05:35:24.308850+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/adele-predicting-and-explaining-ai-performance-across-tasks
structured_data:
  about: []
  author: ''
  description: AI benchmarks report how large language models (LLMs) perform on specific
    tasks but provide little insight into their underlying capabilities that drive
    their performance. They do not explain failures or reliably predict outcomes on
    new tasks. To address this, Microsoft researchers in collaboration with Princeton
    Un...
  headline: 'ADeLe: Predicting and explaining AI performance across tasks'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/adele-predicting-and-explaining-ai-performance-across-tasks
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ADeLe: Predicting and explaining AI performance across tasks'
updated_at: '2026-04-02T05:35:21.311961+00:00'
url_hash: 06d1caa3009c1cf031ad4fb98263bce9a967df53
---

![ADeLe | Three white line icons, showing a circle with a checkmark, a search document, and a set of tools, on a blue‑to‑green gradient background.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/NatureADELE-BlogHeroFeature-1400x788-1-1024x576.jpg)

## At a glance

* AI benchmarks report performance on specific tasks but provide limited insight into underlying capabilities; ADeLe evaluates models by scoring both tasks and models across 18 core abilities, enabling direct comparison between task demands and model capabilities.
* Using these ability scores, the method predicts performance on new tasks with ~88% accuracy, including for models such as GPT-4o and Llama-3.1.
* It builds ability profiles and identifies where models are likely to succeed or fail, highlighting strengths and limitations across tasks.
* By linking outcomes to task demands, ADeLe explains differences in performance, showing how it changes as task complexity increases.

AI benchmarks report how large language models (LLMs) perform on specific tasks but provide little insight into their underlying capabilities that drive their performance. They do not explain failures or reliably predict outcomes on new tasks. To address this, Microsoft researchers in collaboration with Princeton University and Universitat Politècnica de València introduce
[ADeLe
(opens in new tab)](https://kinds-of-intelligence-cfi.github.io/ADELE/)
(AI Evaluation with Demand Levels), a method that characterizes both models and tasks using a broad set of capabilities, such as reasoning and domain knowledge, so performance on new tasks can be predicted and linked to specific strengths and weaknesses in a model.

In a paper published in
*Nature*
, “
[General Scales Unlock AI Evaluation with Explanatory and Predictive Power
(opens in new tab)](https://www.nature.com/articles/s41586-026-10303-2)
,” the team describes how ADeLe moves beyond aggregate benchmark scores. Rather than treating evaluation as a collection of isolated tests, it represents both benchmarks and LLMs using the same set of capability scores. These scores can then be used to estimate how a model will perform on tasks it has not encountered before. The research was supported by
[Microsoft’s Accelerating Foundation Models Research (AFMR)](https://www.microsoft.com/en-us/research/collaboration/accelerating-foundation-models-research/)
grant program.

## ADeLe-based evaluation

ADeLe scores tasks across 18 core abilities, such as attention, reasoning, domain knowledge, and assigns each task a value from 0 to 5 based on how much it requires each ability. For example, a basic arithmetic problem might score low on quantitative reasoning, but an Olympiad-level proof would score much higher.

Evaluating a model across many such tasks produces an ability profile—a structured view of where the model performs and where it breaks down. Comparing this profile to the demands of a new task makes it possible to identify the specific gaps that lead to failure. The process is illustrated in Figure 1.

![Diagram illustrating a two-stage AI evaluation framework: the top panel shows model performance on the ADeLe benchmark and resulting ability profiles, while the bottom panel shows how task-level scoring criteria are applied to derive task demand profiles.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/adele_methodology.png)


Figure 1. Top: (1) Model performance on the ADeLe benchmark and (2) the resulting ability profiles, showing each model’s strengths and limitations across core abilities. Bottom: (1) Application of 18 scoring criteria to each task and (2) the resulting task profiles, showing the abilities each task requires.

## Evaluating ADeLe

Using ADeLe, the team evaluated a range of AI benchmarks and model behaviors to understand what current evaluations capture and what they miss. The results show that many widely used benchmarks provide an incomplete and sometimes misleading picture of model capabilities and that a more structured approach can clarify those gaps and help predict how models will behave in new settings.

ADeLe shows that many benchmarks do not isolate the abilities they are intended to measure or only cover a limited range of difficulty levels. For example, a test designed to evaluate logical reasoning may also depend heavily on specialized knowledge or metacognition. Others focus on a narrow range of difficulty, omitting both simpler and more complex cases. By scoring tasks based on the abilities they require, ADeLe makes these mismatches visible and provides a way to diagnose existing benchmarks and design better ones.

Applying this framework to 15 LLMs, the team constructed ability profiles using 0–5 scores for each of 18 abilities. For each ability, the team measured how performance changes with task difficulty and used the difficulty level at which the model has a 50% chance of success as its ability score. Figure 2 illustrates these results as radial plots that show where the model performs well and where it breaks down.

![Radar charts comparing ability profiles of 15 large language models across 18 abilities, grouped by model families: OpenAI models on the left, LLaMA models in the middle, and DeepSeek-R1-Distill-Qwen models on the right.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/adele_ability_profiles.png)


Figure 2. Ability profiles for 15 LLMs across 18 abilities. Left: OpenAI models. Middle: Llama models. Right: DeepSeek-R1 distilled models.

This analysis shows that models differ in their strengths and weaknesses across abilities. Newer models generally outperform older ones, but not consistently across all abilities. Performance on knowledge-heavy tasks depends strongly on model size and training, while reasoning-oriented models show clear gains on tasks requiring logic, learning, abstraction, and social inference. These patterns typically require multiple, separate analyses across different benchmarks and can still produce conflicting conclusions when task demands are not carefully controlled. ADeLe surfaces them within a single framework.

ADeLe also enables prediction. By comparing a model’s ability profile to the demands of a task, it can forecast whether the model will succeed, even on tasks that are unfamiliar. In experiments, this approach achieved approximately 88% accuracy for models like GPT-4o and LLaMA-3.1-405B, outperforming traditional methods. This makes it possible to both explain and anticipate potential failures before deployment, improving the reliability and predictability of AI model assessment.

Whether AI systems can truly reason is a central debate in the field. Some studies report strong reasoning performance, while others show they break down at scale. These results reflect differences in task difficulty. ADeLe shows that benchmarks labeled as measuring “reasoning” vary in what they require, from basic problem-solving to tasks that combine the need for advanced logic, abstraction, and domain knowledge. The same model can score above 90% on lower-demand tests and below 15% on more demanding ones, reflecting differences in task requirements rather than a change in capability.

Reasoning-oriented models like OpenAI’s o1 and GPT-5 show measurable gains over standard models—not only in logic and mathematics but also with interpreting user intent. However, performance declines as task demands increase. AI systems can reason, but only up to a point, and ADeLe identifies where that point is for each model.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## Looking ahead

ADeLe is designed to evolve alongside advances in AI and can be extended to multimodal and embodied AI systems. It also has the potential to serve as a standardized framework for AI research, policymaking, and security auditing.

More broadly, it advances a more systematic approach to AI evaluation—one that explains system behavior and predicts performance. This work builds on earlier efforts, including Microsoft research on
[applying psychometrics to AI evaluation](https://www.microsoft.com/en-us/research/publication/evaluating-general-purpose-ai-with-psychometrics/)
and recent work on
[Societal AI](https://www.microsoft.com/en-us/research/project/societal-ai/white-paper/)
, emphasizing the importance of AI evaluation.

As general-purpose AI systems continue to outpace existing evaluation methods, approaches like ADeLe offer a path toward more rigorous and transparent assessment in real-world use. The research team is working to expand this effort through a broader community. Additional experiments, benchmark annotations, and resources are available on
[GitHub
(opens in new tab)](https://kinds-of-intelligence-cfi.github.io/ADELE/)
.

Opens in a new tab