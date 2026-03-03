---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T19:23:07.410561+00:00'
exported_at: '2026-03-03T19:23:10.985934+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/new-method-could-increase-llm-training-efficiency-0226
structured_data:
  about: []
  author: ''
  description: A new technique leverages computing downtime to accelerate the training
    process for reasoning large language models (LLMs) without any additional computational
    overhead.
  headline: New method could increase LLM training efficiency
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/new-method-could-increase-llm-training-efficiency-0226
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New method could increase LLM training efficiency
updated_at: '2026-03-03T19:23:07.410561+00:00'
url_hash: 1f2579539dc8edc0b6fa59c2db5ed3453fd189dc
---

Reasoning large language models (LLMs) are designed to solve complex problems by breaking them down into a series of smaller steps. These powerful models are particularly good at challenging tasks like advanced programming and multistep planning.

But developing reasoning models demands an enormous amount of computation and energy due to inefficiencies in the training process. While a few of the high-power processors continuously work through complicated queries, others in the group sit idle.

Researchers from MIT and elsewhere found a way to use this computational downtime to efficiently accelerate reasoning-model training.

Their new method automatically trains a smaller, faster model to predict the outputs of the larger reasoning LLM, which the larger model verifies. This reduces the amount of work the reasoning model must do, accelerating the training process.

The key to this system is its ability to train and deploy the smaller model adaptively, so it kicks in only when some processors are idle. By leveraging computational resources that would otherwise have been wasted, it accelerates training without incurring additional overhead.

When tested on multiple reasoning LLMs, the method doubled the training speed while preserving accuracy. This could reduce the cost and increase the energy efficiency of developing advanced LLMs for applications such as forecasting financial trends or detecting risks in power grids.

“People want models that can handle more complex tasks. But if that is the goal of model development, then we need to prioritize efficiency. We found a lossless solution to this problem and then developed a full-stack system that can deliver quite dramatic speedups in practice,” says Qinghao Hu, an MIT postdoc and co-lead author of a
[paper on this technique](https://arxiv.org/pdf/2511.16665)
.

He is joined on the paper by co-lead author Shang Yang, an electrical engineering and computer science (EECS) graduate student; Junxian Guo, an EECS graduate student; senior author Song Han, an associate professor in EECS, member of the Research Laboratory of Electronics and a distinguished scientist of NVIDIA; as well as others at NVIDIA, ETH Zurich, the MIT-IBM Watson AI Lab, and the University of Massachusetts at Amherst. The research will be presented at the ACM International Conference on Architectural Support for Programming Languages and Operating Systems.

**Training bottleneck**

Developers want reasoning LLMs to identify and correct mistakes in their critical thinking process. This capability allows them to ace complicated queries that would trip up a standard LLM.

To teach them this skill, developers train reasoning LLMs using a technique called reinforcement learning (RL). The model generates multiple potential answers to a query, receives a reward for the best candidate, and is updated based on the top answer. These steps repeat thousands of times as the model learns.

But the researchers found that the process of generating multiple answers, called rollout, can consume as much as 85 percent of the execution time needed for RL training.

“Updating the model — which is the actual ‘training’ part — consumes very little time by comparison,” Hu says.

This bottleneck occurs in standard RL algorithms because all processors in the training group must finish their responses before they can move on to the next step. Because some processors might be working on very long responses, others that generated shorter responses wait for them to finish.

“Our goal was to turn this idle time into speedup without any wasted costs,” Hu adds.

They sought to use an existing technique, called speculative decoding, to speed things up. Speculative decoding involves training a smaller model called a drafter to rapidly guess the future outputs of the larger model.

The larger model verifies the drafter’s guesses, and the responses it accepts are used for training.

Because the larger model can verify all the drafter’s guesses at once, rather than generating each output sequentially, it accelerates the process.

**An adaptive solution**

But in speculative decoding, the drafter model is typically trained only once and remains static. This makes the technique infeasible for reinforcement learning, since the reasoning model is updated thousands of times during training.

A static drafter would quickly become stale and useless after a few steps.

To overcome this problem, the researchers created a flexible system known as “Taming the Long Tail,” or TLT.

The first part of TLT is an adaptive drafter trainer, which uses free time on idle processors to train the drafter model on the fly, keeping it well-aligned with the target model without using extra computational resources.

The second component, an adaptive rollout engine, manages speculative decoding to automatically select the optimal strategy for each new batch of inputs. This mechanism changes the speculative decoding configuration based on the training workload features, such as the number of inputs processed by the draft model and the number of inputs accepted by the target model during verification.

In addition, the researchers designed the draft model to be lightweight so it can be trained quickly. TLT reuses some components of the reasoning model training process to train the drafter, leading to extra gains in acceleration.

“As soon as some processors finish their short queries and become idle, we immediately switch them to do draft model training using the same data they are using for the rollout process. The key mechanism is our adaptive speculative decoding — these gains wouldn’t be possible without it,” Hu says.

They tested TLT across multiple reasoning LLMs that were trained using real-world datasets. The system accelerated training between 70 and 210 percent while preserving the accuracy of each model.

As an added bonus, the small drafter model could readily be utilized for efficient deployment as a free byproduct.

In the future, the researchers want to integrate TLT into more types of training and inference frameworks and find new reinforcement learning applications that could be accelerated using this approach.

“As reasoning continues to become the major workload driving the demand for inference, Qinghao’s TLT is great work to cope with the computation bottleneck of training these reasoning models. I think this method will be very helpful in the context of efficient AI computing,” Han says.

This work is funded by the MIT-IBM Watson AI Lab, the MIT AI Hardware Program, the MIT Amazon Science Hub, Hyundai Motor Company, and the National Science Foundation.