---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-19T02:48:50.472620+00:00'
exported_at: '2026-09-19T02:48:54.814625+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/mindtopo-reveals-vlms-spatial-reasoning-abilities
structured_data:
  about: []
  author: ''
  description: A path, a fence, a knot. MindTopo sets a new benchmark for testing
    how AI understands topological relationships and highlights new opportunities
    to strengthen spatial reasoning and planning.
  headline: MindTopo reveals VLMs’ spatial reasoning abilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/mindtopo-reveals-vlms-spatial-reasoning-abilities
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MindTopo reveals VLMs’ spatial reasoning abilities
updated_at: '2026-09-19T02:48:50.472620+00:00'
url_hash: e8e7671fcde25fb5827559e1483700b9c0634f29
---

![Benchmark overview showing ten spatial reasoning and planning tasks grouped into two rows. The top row, labeled “Reasoning,” includes Maze, Assembly, Bead, Sheep, and Knot. The bottom row, labeled “Planning,” includes Pipe, One Stroke, Swap, Chat Noir, and Untangle. The MindTopo logo and title are centered between the two categories.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/MindTopo-BlogHeroFeature-1400x788-1-scaled.jpg)

## At a glance

* MindTopo is a new benchmark for testing topological reasoning in AI, evaluating whether multimodal models can understand concepts such as connectivity, enclosure, order, separation, and knots.
* The benchmark measures both reasoning and planning, testing not only whether models can recognize topological relationships in static images but also whether they can preserve and manipulate those relationships through a sequence of actions.
* Current multimodal models perform much better on static recognition than interactive tasks, suggesting they struggle to maintain a consistent understanding of topology over time.
* Failures often emerge during planning rather than perception, with models losing track of structural relationships as scenes change or proposing actions that violate physical constraints.
* The findings highlight an important opportunity to advance AI systems for robotics and interactive environments, where understanding what stays connected, enclosed, ordered, or knotted is essential for reliable decision-making.

Can AI determine whether two rooms remain connected after a wall is added? Can it recognize whether an animal is inside a fence, distinguish a true knot from a tangled loop, or rearrange several ropes without allowing them to pass through one another?

These questions concern 3D topology, a form of spatial understanding based not on exact distances, angles, or shapes, but on structural relationships that persist as objects bend, stretch, or deform. Connectivity, enclosure, ordering, and knottedness are examples of topological properties. These properties are a foundational layer of human spatial understanding in Cognitive Science, yet they remain largely absent from how multimodal AI systems are evaluated.

In a new research study, we introduce
[MindTopo
(opens in new tab)](https://mind-topo.github.io/)
, a benchmark designed to evaluate whether multimodal large language models possess this kind of topological intuition. Our findings reveal a substantial gap between recognizing topology in a static image and maintaining an innate understanding of that topology while planning and acting. Current models can sometimes identify a connected path, enclosed region, or knot in a single scene, but that understanding often breaks down once the model must manipulate the scene through a sequence of actions.

## How MindTopo defines topological space

Most spatial evaluations for multimodal models focus on Euclidean properties such as distance, direction, size, and relative position. Inspired by Piaget and other cognitive literature’s classification of topological ability, MindTopo organizes its tasks around the following five categories:

* **Continuity**
  asks whether a path or object remains unbroken.
* **Separation**
  asks whether nearby elements form one structure or distinct parts.
* **Order**
  tracks how elements are arranged along a path or through a transformation.
* **Enclosure**
  tests whether a boundary creates an inside and an outside.
* **Knots**
  tests whether ropes are truly knotted or linked rather than merely tangled in appearance.

Each category is evaluated at two cognitive levels. In reasoning tasks, a model examines one or more rendered scenes and answers a question about their topological structure: whether two points in a maze are connected, whether the sheep are inside the fence, whether a rope is truly knotted. In planning tasks, the model interacts with a simulated environment and selects actions that must create, preserve, or remove a particular relation, such as rotating pipe segments, drawing a separating path, rearranging blocks, trapping a moving agent, or untangling ropes. The environments enforce legal actions, so a model cannot solve a rope puzzle by passing one strand through another.

![This figure provides an overview of MINDTOPO, a benchmark for evaluating topological reasoning in multimodal large language models. The figure illustrates two evaluation settings: reasoning, where models answer visual questions about rendered scenes, and planning, where models interact with environments to transform an initial state into a goal state. The benchmark spans five topological properties—continuity, separation, order, enclosure, and knots—with representative tasks including Maze and Pipe, IKEA and One Stroke, Bead and Swap, Sheep and Chat Noir, and Knot and Untangle. A radar chart on the right summarizes model performance across these categories and shows that current models still struggle, particularly on topological spatial reasoning that requires planning and maintaining invariants across actions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure-1_MINDTOPO-scaled.png)


Figure 1. MindTopo pairs questions about static scenes with interactive tasks that require models to preserve or change the same topological relations.

All scenes are generated from controlled simulators, which provide exact ground truth and adjustable difficulty. That control makes it possible to separate two failure modes that otherwise look alike: a model that fails because a scene is visually complex, and a model that fails because it cannot maintain the underlying relationship as objects move.

![ This figure provides an overview of the 13 MINDTOPO tasks organized by five topological properties and two cognitive levels. Continuity includes 2D Maze and 3D Maze reasoning tasks and the Pipe planning environment; Separation includes IKEA reasoning and One Stroke planning; Order includes Bead and Origami Point reasoning and Swap planning; Enclosure includes Sheep and Hole reasoning and Chat Noir planning; and Knots includes Knot reasoning and Untangle planning. Reasoning tasks pair rendered scenes with visual questions and example answers, while planning tasks, labeled “Gym Env,” show representative initial, intermediate, and final or goal states of interactive environments.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure-2_MINDTOPO-scaled.png)


Figure 2. MindTopo maps reasoning and planning tasks to continuity, separation, order, enclosure, and knots.

## Seeing topology is not the same as acting on it

Across a broad set of proprietary and open-weight models, performance was consistently stronger on static reasoning than on interactive planning, and both remained well below human performance. The contrast was especially clear when success depended on preserving a relationship across many actions.

The error patterns help locate the problem. Static mistakes usually began with perception, such as missing a wall, opening, or crossing. Planning mistakes appeared after the scene had been understood. Models followed a locally plausible move without tracking its later consequences, lost the task over multiple turns, or proposed an action that violated the environment’s dynamics.

Spotlight: Event Series

## Microsoft Research Forum

Join us for a continuous exchange of ideas about research in the era of general AI. Watch the latest episodes on demand.

Opens in a new tab

We also tested whether image and video generation could help models maintain an understanding of topological relationships. Image generation sometimes helped when the relevant relation was visible in a single frame, but it remained unreliable across a sequence of crossings or moves. Video rollouts frequently altered topology or violated task dynamics. Visual simulation appeared useful only to the extent that it preserved structural constraints over time.

## Building agents that preserve structure

MindTopo is intended as a controlled diagnostic for this gap. Robots, accessibility tools, and interactive assistants must understand not only where objects are, but also what remains connected, enclosed, ordered, or knotted as actions unfold. Closing that gap may require models that carry an explicit topological state, or world models whose predictions preserve topology by construction.

Opens in a new tab