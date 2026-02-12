---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-12T19:31:22.763098+00:00'
exported_at: '2026-02-12T19:31:28.281381+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/rethinking-imitation-learning-with-predictive-inverse-dynamics-models
structured_data:
  about: []
  author: ''
  description: 'This research looks at why Predictive Inverse Dynamics Models often
    outperform standard Behavior Cloning in imitation learning. By using simple predictions
    of what happens next, PIDMs reduce ambiguity and learn from far fewer demonstrations.
    Learn more:'
  headline: Rethinking imitation learning with Predictive Inverse Dynamics Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/rethinking-imitation-learning-with-predictive-inverse-dynamics-models
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Rethinking imitation learning with Predictive Inverse Dynamics Models
updated_at: '2026-02-12T19:31:22.763098+00:00'
url_hash: 74633fb50db77bce3d23a7d1002ac669c2eb89fc
---

![Smart Replay - flowchart diagram showing the flow between Encoder, State Predictor, and Policy](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/SmartReplay-BlogHeroFeature-1400x788_New.jpg)

## At a glance

* Imitation learning becomes easier when an AI agent understands why an action is taken.
* Predictive Inverse Dynamics Models (PIDMs) predict plausible future states, clarifying the direction of behavior during imitation learning.
* Even imperfect predictions reduce ambiguity, making it clearer which action makes sense in the moment.
* This makes PIDMs far more data‑efficient than traditional approaches.

Imitation learning teaches AI agents by example: show the agent recordings of how people perform a task and let it infer what to do. The most common approach, Behavior Cloning (BC), frames this as a simple question: “Given the current state of the environment, what action would an expert take?”

In practice, this is done through supervised learning, where the states serve as inputs and expert actions as outputs. While simple in principle, BC often requires large demonstration datasets to account for the natural variability in human behavior, but collecting such datasets can be costly and difficult in real-world settings.

Predictive Inverse Dynamics Models (PIDMs) offer a different take on imitation learning by changing how agents interpret human behavior. Instead of directly mapping states to actions, PIDMs break down the problem into two subproblems: predicting what should happen next and inferring an appropriate action to go from the current state to the predicted future state. While PIDMs often outperform BC, it has not been clear why they work so well, motivating a closer look at the mechanisms behind their performance.

In the paper, “
[When does predictive inverse dynamics outperform behavior cloning?](https://www.microsoft.com/en-us/research/publication/when-does-predictive-inverse-dynamics-outperform-behavior-cloning/)
” we show how this two-stage approach enables PIDMs to learn effective policies from far fewer demonstrations than BC. By grounding the selection process in a plausible future, PIDMs provide a clearer basis for choosing an action during inference. In practice, this can mean achieving comparable performance with as few as one-fifth the demonstrations required by BC, even when predictions are imperfect.

![Figure 1. BC vs. PIDM architectures. (Top) Behavior Cloning learns how to perform a direct mapping from the current state to an action. (Bottom) PIDMs add a state predictor that predicts future states. They then use an inverse dynamics model to predict the action required to move from the current state towards that future state. Both approaches share a common latent representation through a shared state encoder.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/02/SmartReplay_FIG1.png)


Figure 1. BC vs. PIDM architectures. (Top) Behavior Cloning learns how to perform a direct mapping from the current state to an action. (Bottom) PIDMs add a state predictor that predicts future states. They then use an inverse dynamics model to predict the action required to move from the current state towards that future state. Both approaches share a common latent representation through a shared state encoder.

## How PIDMs rethink imitation

PIDMs’ approach to imitation learning consists of two core elements: a model that forecasts plausible future states, and an inverse dynamics model (IDM) that predicts the action needed to move from the present state toward that future. Instead of asking, “What action would an expert take?” PIDMs effectively ask, “What would an expert try to achieve, and what action would lead to it?” This shift turns the information in the current observation (e.g., video frame) into a coherent sense of direction, reducing ambiguity about intent and making action prediction easier.

Spotlight: Event Series

## Microsoft Research Forum

Join us for a continuous exchange of ideas about research in the era of general AI. Watch the first four episodes on demand.

Opens in a new tab

## Real-world validation in a 3D gameplay environment

To evaluate PIDMs under realistic conditions, we trained agents on human gameplay demonstrations in a visually rich video game. These conditions include operating directly from raw video input, interacting with a complex 3D environment in real time at 30 frames per second, and handling visual artifacts and unpredictable system delays.

The agents ran from beginning to end, taking video frames as input and continuously deciding which buttons to press and how to move the joysticks. Instead of relying on a hand-coded set of game variables and rules, the model worked directly from visual input, using past examples to predict what comes next and choosing actions that moved play in that direction.

We ran all experiments on a cloud gaming platform, which introduced additional delays and visual distortions. Despite these challenges, the PIDM agents consistently matched human patterns of play and achieved high success rates across tasks, as shown in Video 1 below and Videos 2 and 3 in the appendix.

Video 1. A player (left) and a PIDM agent (right) side by side playing the game
*Bleeding Edge*
. Both navigate the same trajectory, jumping over obstacles and engaging with nonplayer characters. Despite network delays, the agent closely matches the player’s timing and movement in real time.

## Why and when PIDMs outperform BC

Of course, AI agents do not have access to future outcomes. They can only generate predictions based on available data, and those predictions are sometimes wrong. This creates a central trade‑off for PIDMs.

On one hand, anticipating where the agent should be heading can clarify what action makes sense in the present. Knowing the intended direction helps narrow an otherwise ambiguous choice. On the other hand, inaccurate predictions can occasionally steer the model toward the wrong action.

The key insight is that these effects are not symmetric. While prediction errors introduce some risk, reducing ambiguity in the present often matters more. Our theoretical analysis shows that even with imperfect predictions, PIDMs outperform BC as long as the prediction error remains modest. If future states were known perfectly, PIDMs would outperform BC outright.

In practice, this means that clarifying intent often matters more than accurately predicting the future. That advantage is most evident in the situations where BC struggles: where human behavior varies and actions are driven by underlying goals rather than by what is immediately visible on the screen.

BC requires many demonstrations because each example is noisy and open to multiple interpretations. PIDMs, by contrast, sharpen each demonstration by linking actions to the future states they aim to reach. As a result, PIDMs can learn effective action strategies from far fewer examples.

## Evaluation

To test these ideas under realistic conditions, we designed a sequence of experiments that begins with a simple, interpretable 2D environment (Video 4 in the appendix) and culminates in a complex 3D video game. We trained both BC and PIDM on very small datasets, ranging from one to fifty demonstrations in the 2D environment and from five to thirty for the 3D video game. Across all tasks, PIDM reached high success rates with far fewer demonstrations than BC.

In the 2D setting, BC needed two to five times more data to match PIDM’s performance (Figure 2). In the 3D game, BC needed 66% more data to achieve comparable results (Video 5 in the appendix).

![Figure 2. Performance gains in the 2D environment. As the number of training demonstrations increases, PIDM consistently achieves higher success rates than BC across all four tasks. Curves show mean performance, with shading indicating variability across 20 experiments for reproducibility.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/SmartReplay_blog_Fig2a-d.png)


Figure 2. Performance gains in the 2D environment. As the number of training demonstrations increases, PIDM consistently achieves higher success rates than BC across all four tasks. Curves show mean performance, with shading indicating variability across 20 experiments for reproducibility.

## Takeaway: Intent matters in imitation learning

The main message of our investigation is simple: imitation becomes easier when intent is made explicit. Predicting a plausible future, even an imperfect one, helps resolve ambiguity about which action makes sense right now, much like driving more confidently in the fog when the driver already knows where the road is headed. PIDM shifts imitation learning from pure copying toward goal-oriented action.

This approach has limits. If predictions of future states become too unreliable, they can mislead the model about the intended next move. In those cases, the added uncertainty can outweigh the benefit of reduced ambiguity, causing PIDM to underperform BC.

But when predictions are reasonably accurate, reframing action prediction as “
*How do I get there from here*
?” helps explain why learning from small, messy human datasets can be surprisingly effective. In settings where data is expensive and demonstrations are limited, that shift in perspective can make a meaningful difference.

## Appendix: Visualizations and results (videos)

### A player, a naïve action-replay baseline, and a PIDM agent playing *Bleeding Edge*

Video 2. (Left) The player completes the task under normal conditions. (Middle) The baseline replays the recorded actions at their original timestamps, which initially appears to work. Because the game runs on a cloud gaming platform, however, random network delays quickly push the replay out of sync, causing the trajectory to fail. (Right) Under the same conditions, the PIDM agent behaves differently. Instead of naively replaying actions, it continuously interprets visual input, predicts how the behavior is likely to unfold, and adapts its actions in real time. This allows it to correct delays, recover from deviations, and successfully reproduce the task in settings where naïve replay inevitably fails.

### A player and a PIDM agent performing a complex task in *Bleeding Edge*

Video 3. In this video, the task exhibits strong partial observability: correct behavior depends on whether a location is being visited for the first or second time. For example, in the first encounter, the agent proceeds straight up the ramp; on the second, it turns right toward the bridge. Similarly, it may jump over a box on the first pass but walk around it on the second. The PIDM agent reproduces this trajectory reliably, using coarse future guidance to select actions in the correct direction.

### Visualization of the 2D navigation environment

Video 4. These videos show ten demonstrations for each of four tasks: Four Room, Zigzag, Maze, and Multiroom. In all cases, the setup is the same: the character (blue box) moves through the environment and must reach a sequence of goals (red squares). The overlaid trajectories visualize the paths the player took; the models never see these paths. Instead, they observe only their character’s current location, the position of all goals, and whether each goal has already been reached. Because these demonstrations come from real players, no two paths are identical: players pause, take detours, or correct small mistakes along the way. That natural variability is exactly what the models must learn to handle.

### PIDM vs. BC in a 3D environment

Video 5. The PIDM agent achieves an 85% success rate with only fifteen demonstrations used in training. The BC agent struggles to stay on track and levels off around 60%. The contrast illustrates how differently the two approaches perform when training data is limited.

Opens in a new tab