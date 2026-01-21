---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-21T22:15:29.400676+00:00'
exported_at: '2026-01-21T22:15:35.406769+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/optimind-a-small-language-model-with-optimization-expertise
structured_data:
  about: []
  author: ''
  description: 'OptiMind is a small language model that converts business operation
    challenges, described naturally, into mathematical formulations that optimization
    software can solve. It reduces formulation time & errors & enables fast, privacy-preserving
    local use:'
  headline: 'OptiMind: A small language model with optimization expertise'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/optimind-a-small-language-model-with-optimization-expertise
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'OptiMind: A small language model with optimization expertise'
updated_at: '2026-01-21T22:15:29.400676+00:00'
url_hash: 86e8c755656cf616e012997d20c2b5dbe0e738d1
---

![A flowchart with three horizontal sections on a blue-to-green gradient background. The first section, labeled “Classification,” shows icons of a computer, an arrow pointing to a robot face, and another arrow pointing to a box labeled “TSP.” The second section, labeled “Inference,” displays a robot icon connected by arrows to two document icons, one of which includes a magnifying glass. The third section, labeled “Test-time scaling,” shows a document with a checkmark connected by an arrow to a circular refresh icon. Arrows indicate the flow between sections, starting from Classification to Inference and then to Test-time scaling.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/OptiMind-BlogHeroFeature-1400x788-2.jpg)

## At a glance

* Many real-world business problems can benefit from optimization, but translating decisions, constraints, and goals from natural language into optimization algorithms is slow.
* OptiMind is a small language model designed to convert business problems described in natural language into the mathematical formulations needed by optimization software.
* OptiMind is trained on a carefully curated, expert-aligned dataset and applies domain-specific hints and self-checks at inference time, improving its accuracy.
* OptiMind matches or exceeds the performance of much larger systems, can run locally to protect sensitive data, produces more reliable formulations, and reduces the time and expertise needed to prepare optimization models.

Enterprises across industries, from energy to finance, use optimization models to plan complex operations like supply chains and logistics. These models work by defining three elements: the choices that can be made (such as production quantities or delivery routes), the rules and limits those choices must follow, and the goal, whether that’s minimizing costs, meeting customer demand, or improving efficiency.

Over the past few decades, many businesses have shifted from judgment-based decision-making to data-driven approaches, leading to major efficiency gains and cost savings. Advances in AI promise to accelerate this shift even further, potentially cutting decision times from days to minutes while delivering better results.

In practice, however, turning real-world business problems into a form that optimization software can understand is challenging. This translation process requires expressing decisions, constraints, and objectives in mathematical terms. The work demands specialized expertise, and it can take anywhere from one day to several weeks to solve complex problems.

To address this challenge, we’re introducing
[OptiMind](https://www.microsoft.com/en-us/research/publication/optimind-teaching-llms-to-think-like-optimization-experts/)
, a small language model designed to convert problems described in plain language into the mathematical formulations that optimization software needs. Built on a 20-billion parameter model, OptiMind is compact by today’s standards yet matches the performance of larger, more complex systems. Its modest size means it can run locally on users’ devices, enabling fast iteration while keeping sensitive business data on users’ devices rather than transmitting it to external servers.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## How it works

OptiMind incorporates knowledge from optimization experts both during training and when it’s being used to improve formulation accuracy at scale. Three stages enable this: domain-specific hints improve training data quality, the model undergoes fine-tuning, and expert reasoning guides the model as it works.

![The image illustrates a linear programming model for a manufacturing facility, detailing the production quantities, setup indicators, and inventory levels for different products over a six-month period, aiming to optimize costs.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/OptiMind-1-scaled.jpg)


Figure 1. From problem description to solution

One of the central challenges in developing OptiMind was the poor quality of existing public datasets for optimization problems. Many examples were incomplete or contained incorrect solutions. To address this, we developed a systematic approach that combines automation with expert review. It organizes problems into well-known categories, such as scheduling or routing, and identifies common error patterns within each. Using these insights, we generated expert-verified “hints” to guide the process, enabling the system to regenerate higher-quality solutions and filter out unsolvable examples (Figure 2). The result is a training dataset that more accurately reflects how optimization experts structure problems.

![Process for correcting training data](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/training-data-cleaning.png)


Figure 2. Process for correcting training data

Using this refined dataset, we applied supervised fine-tuning to the base model. Rather than simply generating code, we trained OptiMind to produce structured mathematical formulations alongside intermediate reasoning steps, helping it avoid the common mistakes found in earlier datasets.

When in use, the model’s reliability further improves. When given a new problem, OptiMind first classifies it into a category, such as scheduling or network design. It then applies expert hints relevant to that type of problem, which act as reminders to check for errors before generating a solution. For particularly challenging problems, the system generates multiple solutions and either selects the most frequently occurring one or uses feedback to refine its response. This approach increases accuracy without requiring a larger model, as illustrated in Figure 3.

![OptiMind’s inference process](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/inference-pipeline.png)


Figure 3. OptiMind’s inference process

## Evaluation

To test the system, we turned to three widely used public benchmarks that represent some of the most complex formulation tasks in the field. On closer inspection, we discovered that 30 to 50 percent of the original test data was flawed. After manually correcting the issues, OptiMind improved accuracy by approximately 10 percent over the base model. Figure 4 and Table 1 show detailed comparisons: OptiMind outperformed other open-source models under 32 billion parameters and, when combined with expert hints and correction strategies, matched or exceeded the performance of current leading models.

![Average accuracy percentages over all models.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/main_barplot_new-1.png)


Figure 4. Average accuracy percentages over all models.


![Performance of all models on corrected benchmark datasets](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/main-results-table.png)


Table 1. Performance of all models on corrected benchmark datasets

OptiMind is more reliable than other models because it learns from higher-quality, domain-aligned data. And by correcting errors and inconsistencies in standard datasets, we significantly reduced the model’s tendency to hallucinate relative to the base and comparison models.

## Looking forward

While supervised fine-tuning has provided a strong foundation, we are exploring reinforcement learning to further refine OptiMind’s reasoning capabilities. We’re also investigating automated frameworks that would allow LLMs to generate their own expert hints, enabling continuous autonomous improvement. Additionally, we are working with Microsoft product teams and industry collaborators to expand OptiMind’s utility, adding support for more programming languages and a variety of input formats, including Excel and other widely used tools.

We’re releasing OptiMind as an experimental model to gather community feedback and inform future development. The model is available through
[Microsoft Foundry
(opens in new tab)](https://aka.ms/OptiMindCatalog)
and
[Hugging Face
(opens in new tab)](https://aka.ms/OptiMindHF)
, and we’ve open-sourced the benchmarks and data-processing procedures on
[GitHub
(opens in new tab)](https://aka.ms/OptiGuideGithub)
to support more reliable evaluation across the field. We welcome feedback through
[GitHub
(opens in new tab)](https://aka.ms/OptiGuideGithub)
, and invite those interested in shaping the future of optimization to apply for one of our
[open roles](https://www.microsoft.com/en-us/research/careers/)
.

Opens in a new tab