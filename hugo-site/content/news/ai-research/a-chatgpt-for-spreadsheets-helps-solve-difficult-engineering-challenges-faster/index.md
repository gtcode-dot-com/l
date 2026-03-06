---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-06T00:15:32.290925+00:00'
exported_at: '2026-03-06T00:15:34.728425+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/chatgpt-spreadsheets-helps-solve-difficult-engineering-challenges-faster-0304
structured_data:
  about: []
  author: ''
  description: MIT researchers developed a computational approach that can be used
    to solve problems with hundreds of variables. In tests on realistic engineering
    challenges, the approach found top solutions 10 to 100 times faster than methods
    such as Bayesian optimization.
  headline: A “ChatGPT for spreadsheets” helps solve difficult engineering challenges
    faster
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/chatgpt-spreadsheets-helps-solve-difficult-engineering-challenges-faster-0304
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A “ChatGPT for spreadsheets” helps solve difficult engineering challenges faster
updated_at: '2026-03-06T00:15:32.290925+00:00'
url_hash: 6e37335aeecdef6da2dbbd996667fa5fe5d0e40c
---

Many engineering challenges come down to the same headache — too many knobs to turn and too few chances to test them. Whether tuning a power grid or designing a safer vehicle, each evaluation can be costly, and there may be hundreds of variables that could matter.

Consider car safety design. Engineers must integrate thousands of parts, and many design choices can affect how a vehicle performs in a collision. Classic optimization tools could start to struggle when searching for the best combination.

MIT researchers developed a new approach that rethinks how a classic method, known as Bayesian optimization, can be used to solve problems with hundreds of variables. In tests on realistic engineering-style benchmarks, like power-system optimization, the approach found top solutions 10 to 100 times faster than widely used methods.

Their technique leverages a foundation model trained on tabular data that automatically identifies the variables that matter most for improving performance, repeating the process to hone in on better and better solutions. Foundation models are huge artificial intelligence systems trained on vast, general datasets. This allows them to adapt to different applications.

The researchers’ tabular foundation model does not need to be constantly retrained as it works toward a solution, increasing the efficiency of the optimization process. The technique also delivers greater speedups for more complicated problems, so it could be especially useful in demanding applications like materials development or drug discovery.

“Modern AI and machine-learning models can fundamentally change the way engineers and scientists create complex systems. We came up with one algorithm that can not only solve high-dimensional problems, but is also reusable so it can be applied to many problems without the need to start everything from scratch,” says Rosen Yu, a graduate student in computational science and engineering and lead author of a
[paper on this technique](https://arxiv.org/html/2505.20685v3)
.

Yu is joined on the paper by Cyril Picard, a former MIT postdoc and research scientist, and Faez Ahmed, associate professor of mechanical engineering and a core member of the MIT Center for Computational Science and Engineering. The research will be presented at the International Conference on Learning Representations.

**Improving a proven method**

When scientists seek to solve a multifaceted problem but have expensive methods to evaluate success, like crash testing a car to know how good each design is, they often use a tried-and-true method called Bayesian optimization. This iterative method finds the best configuration for a complicated system by building a surrogate model that helps estimate what to explore next while considering the uncertainty of its predictions.

But the surrogate model must be retrained after each iteration, which can quickly become computationally intractable when the space of potential solutions is very large. In addition, scientists need to build a new model from scratch any time they want to tackle a different scenario.

To address both shortcomings, the MIT researchers utilized a generative AI system known as a tabular foundation model as the surrogate model inside a Bayesian optimization algorithm.

“A tabular foundation model is like a ChatGPT for spreadsheets. The input and output of these models are tabular data, which in the engineering domain is much more common to see and use than language,” Yu says.

Just like large language models such as ChatGPT,  Claude, and Gemini, the model has been pre-trained on an enormous amount of tabular data. This makes it well-equipped to tackle a range of prediction problems. In addition, the model can be deployed as-is, without the need for any retraining.

To make their system more accurate and efficient for optimization, the researchers employed a trick that enables the model to identify features of the design space that will have the biggest impact on the solution.

“A car might have 300 design criteria, but not all of them are the main driver of the best design if you are trying to increase some safety parameters. Our algorithm can smartly select the most critical features to focus on,” Yu says.

It does this by using a tabular foundation model to estimate which variables (or combinations of variables) most influence the outcome.

It then focuses the search on those high-impact variables instead of wasting time exploring everything equally. For instance, if the size of the front crumple zone significantly increased and the car’s safety rating improved, that feature likely played a role in the enhancement.

**Bigger problems, better solutions**

One of their biggest challenges was finding the best tabular foundation model for this task, Yu says. Then they had to connect it with a Bayesian optimization algorithm in such a way that it could identify the most prominent design features.

“Finding the most prominent dimension is a well-known problem in math and computer science, but coming up with a way that leveraged the properties of a tabular foundation model was a real challenge,” Yu says.

With the algorithmic framework in place, the researchers tested their method by comparing it to five state-of-the-art optimization algorithms.

On 60 benchmark problems, including realistic situations like power grid design and car crash testing, their method consistently found the best solution between 10 and 100 times faster than the other algorithms.

“When an optimization problem gets more and more dimensions, our algorithm really shines,” Yu added.

But their method did not outperform the baselines on all problems, such as robotic path planning. This likely indicates that scenario was not well-defined in the model’s training data, Yu says.

In the future, the researchers want to study methods that could boost the performance of tabular foundation models. They also want to apply their technique to problems with thousands or even millions of dimensions, like the design of a naval ship.

“At a higher level, this work points to a broader shift: using foundation models not just for perception or language, but as algorithmic engines inside scientific and engineering tools, allowing classical methods like Bayesian optimization to scale to regimes that were previously impractical,” says Ahmed.

“The approach presented in this work, using a pretrained foundation model together with high‑dimensional Bayesian optimization, is a creative and promising way to reduce the heavy data requirements of simulation‑based design. Overall, this work is a practical and powerful step toward making advanced design optimization more accessible and easier to apply in real-world settings,” says Wei Chen, the Wilson-Cook Professor in Engineering Design and chair of the Department of Mechanical Engineering at Northwestern University, who was not involved in this research.