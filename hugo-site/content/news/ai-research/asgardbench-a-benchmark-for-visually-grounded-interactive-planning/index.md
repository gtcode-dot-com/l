---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T02:45:32.464234+00:00'
exported_at: '2026-04-02T02:45:35.598555+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning
structured_data:
  about: []
  author: ''
  description: AsgardBench evaluates whether embodied agents can revise their plans
    based on visual observations as tasks unfold. By focusing on perception-driven
    planning, it exposes key limitations and guides improvements in agent reliability.
  headline: 'AsgardBench: A benchmark for visually grounded interactive planning'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'AsgardBench: A benchmark for visually grounded interactive planning'
updated_at: '2026-04-02T02:45:32.464234+00:00'
url_hash: a4075bdbb344b15f37572798d4999a7379e53486
---

![AsgardBench | three whit icons on a blue to purple gradient background | first icon shows a laptop screen with a eye in the upper right corner, second icon shows relational nodes | third icon is a security shield with a checkmark](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/AsgardBench-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* To successfully complete tasks, embodied AI agents must ground and update their plans based on visual feedback.
* AsgardBench isolates whether agents can use visual observations to revise their plans as tasks unfold.
* Spanning 108 controlled task instances across 12 task types, the benchmark requires agents to adapt their plans based on what they observe.
* Because objects can be in different positions and states (e.g., clean or dirty), the same instruction can require different action sequences, even in the same environment.

Imagine a robot tasked with cleaning a kitchen. It needs to observe its environment, decide what to do, and adjust when things don’t go as expected, for example, when the mug it was tasked to wash is already clean, or the sink is full of other items. This is the domain of embodied AI: systems that perceive their environment and act within it.

The field has made rapid progress, but evaluating these systems is harder than it looks. Many benchmarks test perception, navigation, and physical control all at once, making it difficult to isolate whether an AI agent is actually using what it perceives to make better decisions or just getting lucky because the environment is predictable enough to script around.

To address this, we created AsgardBench. In the paper,
[AsgardBench — Evaluating Visually Grounded Interactive Planning Under Minimal Feedback](https://www.microsoft.com/en-us/research/publication/asgardbench-evaluating-visually-grounded-interactive-planning-under-minimal-feedback/)
,” we describe how this benchmark poses a simple but demanding challenge: give an AI agent a household task, let it observe the environment through images, and see whether it can adjust its plan when what it perceives contradicts what it anticipated. Can it notice that the mug it needs to clean is already in the sink, or that it isn’t, and behave accordingly? That is the core question AsgardBench is designed to answer.

Built on AI2-THOR, an interactive 3D simulation environment used to train and evaluate AI agents on household tasks, AsgardBench positions agents near objects and gives them a small, fixed set of actions, such as
*find*
,
*pickup*
,
*put*
,
*clean*
, and
*toggle\_on/off*
. At each turn, the agent proposes a full sequence of steps to complete the task, but only the first step executes. Throughout, the focus is squarely on plan adaptation, not whether an agent can navigate a room or manipulate an object, but whether it can use what it perceives to revise its next step.

For example, the agent may discover a mug to be clean, dirty, or filled with coffee, or it may observe that a sink contains many other items, so the same instruction can require different action sequences as the task unfolds. This process is illustrated in Figure 1.

![Model changes the steps in its plan as new observations are observed](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/AsgardBench-fig1.png)


Figure 1: Agent observations and corresponding action plans in AsgardBench. Each image is paired with the plan generated from that observation. This illustrates how AsgardBench requires agents to update or change their plans based on new visual evidence rather than following a fixed sequence.

## How it works

Agents start in interaction-ready positions, so navigation and viewpoint selection are not factors. A
*find*
action brings objects into view, and the environment handles the details of container sizing and placement, so the agent does not need to reason about which cabinet or countertop to use. The only inputs are color images, a history of attempted actions with simple success or failure signals, and the agent’s own record of what it plans to do next.

At each turn, the agent proposes a complete sequence of steps to finish the task, but only the first step proceeds. It then receives new images and a simple signal—did that action succeed or fail? This prevents the agent from scripting everything upfront and forces it to re-evaluate and revise its plan at every step. Built-in limits on total steps and repeated actions prevent endless loops. Because the environment provides only simple feedback, the agent must be able to notice what it perceives (e.g., whether a mug is dirty, whether a faucet is running) and keep track of where it is in the task from one step to the next.

## Evaluating AsgardBench

We tested several leading vision-capable models on AsgardBench and observed that high-performing models require visual grounding to consistently succeed. Across the models, visual input substantially improved performance: most models more than doubled success rates when given images versus text-only descriptions of the scene. This is in contrast to some prior benchmarks where agents could perform reasonably well without vision by relying on textual feedback on what went wrong.

Providing that kind of detailed failure information raises performance for all models in AsgardBench, too, but it can mask the real problem. The strongest vision-capable models still outperform text-only agents even when those agents are given detailed feedback, demonstrating that the benchmark requires visual grounding that text alone cannot replicate. AsgardBench’s performance is illustrated in Figure 2.

![Chart showing input substantially improves performance for all but the weakest models when images are included](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/AsgardBench-fig2.png)


Figure 2. Success rates for image-based and text-only conditions. Visual input substantially improves performance for all but the weakest agents, while text-only performance remains low, indicating that AsgardBench requires perception-based reasoning.

The results also revealed where today’s agents consistently fall short. Across all models, the same problems kept appearing: agents attempted undoable actions (e.g., trying to clean a mug that was not in the sink), got stuck in repeated action loops, misinterpreted subtle visual cues (on/off, clean/dirty), and lost track of where they were in the task progress from one step to the next. This points to three weaknesses: the inability to distinguish subtle visual details in cluttered scenes, the inability to maintain an accurate picture of task progress across multiple steps, and the inability to consistently translate what the agent sees into timely updates to its plan. Taken together, these point to where the next generation of embodied agents will need to improve.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## Implications and looking ahead

AsgardBench is useful as both a diagnostic and development tool. By varying what feedback agents receive (none, minimal, or detailed), researchers can isolate whether performance gains come from better perception, better memory, or better planning. Promising directions include systems that combine stronger visual understanding with better state tracking, training approaches that emphasize learning to repair plans mid-task, and evaluation methods that measure not just whether an agent succeeds but how well it adapted along the way.

The failure patterns AsgardBench surfaces point toward a concrete next step: building systems that can make finer visual distinctions, keep track of what changed more reliably across steps, and learn to revise plans mid-task rather than plowing ahead on a script. Agents that make progress on these challenges should be meaningfully better equipped for the messiness of real-world environments: unexpected object states, cluttered scenes, and the constant need to adapt.

AsgardBench is open source and available on
[GitHub
(opens in new tab)](https://github.com/microsoft/AsgardBench)
, providing a foundation for advancing research in visually grounded planning.

## Acknowledgements

We thank the AI2-THOR community for building the simulation platform and making reproducible embodied evaluation possible.

Opens in a new tab