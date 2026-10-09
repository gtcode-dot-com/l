---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-04T00:14:55.389840+00:00'
exported_at: '2026-10-04T00:14:58.587293+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/new-method-enables-ai-safety-critical-situations-0914
structured_data:
  about: []
  author: ''
  description: HardFlow is a new algorithm developed at MIT that helps pretrained
    generative AI models satisfy hard constraints while improving solution quality
    without retraining, in applications spanning robotics, control of physical systems,
    and computer vision.
  headline: New method enables AI for safety-critical situations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/new-method-enables-ai-safety-critical-situations-0914
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New method enables AI for safety-critical situations
updated_at: '2026-10-04T00:14:55.389840+00:00'
url_hash: 1ccfa6a4e947b14e81106a433f95164fcce5d3fe
---

MIT researchers have developed a new technique that helps generative artificial intelligence models find solutions to high-stakes problems.

In these settings, a plausible answer is not enough: The output often must also satisfy nonnegotiable safety, physical, or task-specific requirements, known as hard constraints.

The researchers developed a method that helps generative models meet these strict requirements without sacrificing the quality of their outputs.

The key to their technique is to give the model more freedom during the generation process and enforce hard constraints on the final output, rather than at every intermediate step.

In experiments spanning robotics, control of physical processes, and computer vision, the new method consistently satisfied the required constraints while identifying better solutions than existing techniques.

This adaptable, plug-and-play technique works at deployment time, so it can be applied to pretrained generative models without retraining them. It can make such models more useful in applications where safety rules, physical laws, or other strict requirements cannot be violated.

“The promise of generative AI is its ability to explore a rich space of possibilities, but the real world places boundaries on which possibilities are acceptable. Our approach lets us preserve that generative power while enforcing the nonnegotiable requirements of high-stakes or safety-critical applications,” says Navid Azizan, the Alfred H. and Jean M. Hayes Career Development Associate Professor in the Department of Mechanical Engineering and the Institute for Data, Systems, and Society (IDSS), a principal investigator of the Laboratory for Information and Decision Systems (LIDS), and the senior author of a paper on this technique.

Azizan is joined on the paper by lead author Zeyang Li, a graduate student in mechanical engineering and LIDS; and Kaveh Alim, a graduate student in IDSS and LIDS. The
[research appears this week](https://ieeexplore.ieee.org/abstract/document/11592684)
in the
*IEEE Transactions on Pattern Analysis and Machine Intelligence*
.

**Freedom to explore**

Pretrained generative AI models, such as diffusion models like Stable Diffusion and flow-matching models like FLUX, are now widely available. These powerful models learn to create new data by transforming random noise. Their availability has enabled people to adapt them to a wide range of applications.

These highly capable models excel at providing answers that come close to satisfying most queries, but in safety-critical applications like robot path planning on a crowded factory floor, an answer that is “nearly correct” may not be good enough.

For instance, a “nearly correct” path from one machine to another might still result in the robot colliding with a human co-worker.

In such safety-critical applications, users often employ a technique called projection-based sampling, which repeatedly forces the model’s partial solutions, called intermediate samples, to satisfy strict requirements during the generation process.

But constraining the entire generation process can prevent the model from reaching a better final solution. These methods also typically focus only on satisfying the hard constraints, missing the opportunity to improve other qualities of the solution, like reducing the length of the robot’s trajectory.

“For constraint satisfaction, what ultimately matters is the model’s final output, since the internal process is discarded. By not requiring every intermediate step to satisfy the constraints, we give the model more freedom to find high-quality solutions that are still feasible in the end,” says Li.

The researchers developed an algorithm called HardFlow that steers the sampling process so that the final output satisfies the user’s hard constraints without being overly restrictive and is of higher quality.

**Subtle steering**

HardFlow reformulates hard-constrained sampling as a trajectory-optimization problem, using tools from the field of optimal control. This enables the framework to steer the model’s sampling trajectory toward a goal, making subtle corrections along the way while enforcing hard constraints on the final output.

“Control theory gives us a powerful framework for formalizing the optimal way of making these corrections,” Azizan says.

But solving the trajectory-optimization problem around an enormous neural network was no easy task. The model may have hundreds of interconnected layers that process data.

To make the problem tractable, the researchers leveraged the structure of flow-matching models to decompose the problem into a sequence of smaller, single-step subproblems. They then applied systematic transformations and approximations to derive an efficient, scalable algorithm that still finds a feasible solution.

“Essentially, we transformed the trajectory-optimization problem into something that preserves the key properties of the original problem, but can be solved very efficiently at deployment time,” Azizan adds.

Reformulating the task as an optimization problem allows HardFlow to incorporate additional goals that can improve the quality of the final answer. For instance, HardFlow could find a collision-free path for a robot that is also the shortest distance to its goal.

“Our framework can jointly handle both aspects, which helps it perform much better than existing methods,” says Li.

Across experiments in robotic manipulation, maze navigation, and text-guided image editing, HardFlow achieved perfect constraint satisfaction while consistently outperforming baseline methods on measures of solution quality.

For example, it enabled a robotic manipulator to avoid collisions with obstacles while also finding the quickest path to the target object. Most other methods either resulted in collisions or found paths that took significantly more time.

In addition, HardFlow’s computation time was comparable to or lower than that of most competing methods.

In the future, the researchers could extend the framework to settings in which the AI model itself can also be updated, so that constraint satisfaction and sample quality can be improved in a more adaptive manner.