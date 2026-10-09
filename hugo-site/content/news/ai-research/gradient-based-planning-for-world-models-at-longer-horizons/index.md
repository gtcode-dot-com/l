---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-20T22:15:51.301955+00:00'
exported_at: '2026-04-20T22:15:53.629344+00:00'
feed: http://bair.berkeley.edu/blog/feed.xml
language: en
source_url: http://bair.berkeley.edu/blog/2026/04/20/grasp
structured_data:
  about: []
  author: ''
  description: The BAIR Blog
  headline: Gradient-based Planning for World Models at Longer Horizons
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://bair.berkeley.edu/blog/2026/04/20/grasp
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Gradient-based Planning for World Models at Longer Horizons
updated_at: '2026-04-20T22:15:51.301955+00:00'
url_hash: ad212735eb1ec68c7218af5506d1b512c0d2bd5a
---

**GRASP**
is a new gradient-based planner for learned dynamics (a âworld modelâ) that makes long-horizon planning practical by (1) lifting the trajectory into virtual states so optimization is parallel across time, (2) adding stochasticity directly to the state iterates for exploration, and (3) reshaping gradients so actions get clean signals while we avoid brittle âstate-inputâ gradients through high-dimensional vision models.

Large, learned world models are becoming increasingly capable. They can predict long sequences of future observations in high-dimensional visual spaces and generalize across tasks in ways that were difficult to imagine a few years ago. As these models scale, they start to look less like task-specific predictors and more like general-purpose simulators.

But having a powerful predictive model is not the same as being able to use it effectively for control/learning/planning. In practice, long-horizon planning with modern world models remains fragile: optimization becomes ill-conditioned, non-greedy structure creates bad local minima, and high-dimensional latent spaces introduce subtle failure modes.

In this blog post, I describe the problems that motivated this project and our approach to address them: why planning with modern world models can be surprisingly fragile, why long horizons are the real stress test, and what we changed to make gradient-based planning much more robust.

---

> This blog post discusses work done with Mike Rabbat, Aditi Krishnapriyan, Yann LeCun, and Amir Bar (\* denotes equal advisorship), where we propose GRASP.

---

## What is a world model?

These days, the term âworld modelâ is quite overloaded, and depending on the context can either mean an explicit dynamics model or some implicit, reliable internal state that a generative model relies on (e.g. when an LLM generates chess moves, whether there is some internal representation of the board). We give our loose working definition below.

Suppose you take actions $a\_t \in \mathcal{A}$ and observe states $s\_t \in \mathcal{S}$ (images, latent vectors, proprioception). A
**world model**
is a learned model that, given the current state and a sequence of future actions, predicts what will happen next. Formally, it defines a predictive distribution on a sequence of observed states $s\_{t-h:t}$ and current action $a\_t$:

\[P\_\theta(s\_{t+1} \mid s\_{t-h:t},\; a\_t)\]

that approximates the environmentâs true conditional $P(s\_{t+1} \mid s\_{t-h:t},\; a\_t)$. For this blog post, weâll assume a Markovian model $P(s\_{t+1} \mid s\_{t-h:t},\; a\_t)$ for simplicity (all results here can be extended to the more general case), and when the model is deterministic it reduces to a map over states:

\[s\_{t+1} = F\_\theta(s\_t, a\_t).\]

In practice the state $s\_t$ is often a learned latent representation (e.g., encoded from pixels), so the model operates in a (theoretically) compact, differentiable space. The key point is that a world model gives you a
*differentiable simulator*
; you can roll it forward under hypothetical action sequences and backpropagate through the predictions.

---

## Planning: choosing actions by optimizing through the model

Given a start $s\_0$ and a goal $g$, the simplest planner chooses an action sequence $\mathbf{a}=(a\_0,\dots,a\_{T-1})$ by rolling out the model and minimizing terminal error:

\[\min\_{\mathbf{a}} \; \| s\_T(\mathbf{a}) - g \|\_2^2, \quad \text{where } s\_T(\mathbf{a}) = \mathcal{F}\_{\theta}^{T}(s\_0,\mathbf{a}).\]

Here we use $\mathcal{F}^T$ as shorthand for the full rollout through the world model (dependence on model parameters $\theta$ is implicit):

\[\mathcal{F}\_{\theta}^{T}(s\_0, \mathbf{a}) = F\_\theta(F\_\theta(\cdots F\_\theta(s\_0, a\_0), \cdots, a\_{T-2}), a\_{T-1}).\]

In short horizons and low-dimensional systems, this can work reasonably well. But as horizons grow and models become larger and more expressive, its weaknesses become amplified.

So why doesnât this just work at scale?

---

## Why long-horizon planning is hard (even when everything is differentiable)

There are two separate pain points for the more general world model, plus a third that is specific to learned, deep learning-based models.

### 1) Long-horizon rollouts create deep, ill-conditioned computation graphs

Those familiar with backprop through time (BPTT) may notice that weâre differentiating through a model applied to itself repeatedly, which will lead to the
**exploding/vanishing gradients**
problem. Namely, if we take derivatives (note weâre differentiating vector-valued functions, resulting in Jacobians that we denote with $D\_x (\cdots)$) with respect to earlier actions (e.g. $a\_0$):

\[D\_{a\_0} \mathcal{F}\_{\theta}^{T}(s\_0, \mathbf{a}) = \Bigl(\prod\_{t=1}^T D\_s F\_\theta(s\_t, a\_t)\Bigr) D\_{a\_0}F\_\theta(s\_0, a\_0).\]

We see that the Jacobianâs conditioning scales exponentially with time $T$:

\[\sigma\_{\text{max/min}}(D\_{a\_0}\mathcal{F}\_{\theta}^{T}) \sim \sigma\_{\text{max/min}}(D\_s F\_\theta)^{T-1},\]

leading to exploding or vanishing gradients.

### 2) The landscape is non-greedy and full of traps

At short horizons, the greedy solution, where we move straight toward the goal at every step, is often good enough. If you only need to plan a few steps ahead, the optimal trajectory usually doesnât deviate much from âhead toward $g$â at each step.

As horizons grow, two things happen. First, longer tasks are more likely to require
*non-greedy*
behavior: going around a wall, repositioning before pushing, backing up to take a better path. And as horizons grow, more of these non-greedy steps are typically needed. Second, the optimization space itself scales with horizon: $\mathrm{dim}(\mathcal{A} \times \cdots \times \mathcal{A}) = T\mathrm{dim}(\mathcal{A})$, further expanding the space of local minima for the optimization problem.

![Loss landscape](https://bair.berkeley.edu/static/blog/grasp/loss-landscape.jpg)


*Distance to goal along the optimal path is non-monotonic, and the resulting loss landscape can be rough.*



---

## A long-horizon fix: lifting the dynamics constraint

Suppose we treat the dynamics constraint $s\_{t+1} = F\_{\theta}(s\_t, a\_t)$ as a soft constraint, and we instead optimize the following penalty function over both actions $(a\_0,\ldots,a\_{T-1})$ and states $(s\_0,\ldots,s\_T)$:

\[\min\_{\mathbf{s},\mathbf{a}} \mathcal{L}(\mathbf{s}, \mathbf{a}) = \sum\_{t=0}^{T-1} \big\|F\_\theta(s\_t,a\_t) - s\_{t+1}\big\|\_2^2,
\quad \text{with } s\_0 \text{ fixed and } s\_T=g.\]

This is also sometimes called
*collocation*
in planning/robotics literature. Note the lifted formulation shares the same
*global*
minimizers as the original rollout objective (both are zero exactly when the trajectory is dynamically feasible). But the optimization landscapes are very different, and we get two immediate benefits:

* Each world model evaluation $F\_{\theta}(s\_t,a\_t)$ depends only on local variables, so all $T$ terms can be computed
  *in parallel across time*
  , resulting in a huge speed-up for longer horizons, and
* You no longer backpropagate through a single deep $T$-step composition to get a learning signal, since the previous product of Jacobians now splits into a sum, e.g.:

\[D\_{a\_0} \mathcal{L} = 2(F\_\theta(s\_0, a\_0) - s\_1).\]

Being able to optimize states directly also helps with exploration, as we can temporarily navigate through unphysical domains to find the optimal plan:

![Collocation planning in BallNav](https://bair.berkeley.edu/static/blog/grasp/ballnav_demo.gif)


*Collocation-based planning allows us to directly perturb states and explore midpoints more effectively.*

However, lunch is never free. And indeed, especially for deep learning-based world models, there is a critical issue that makes the above optimization quite difficult in practice.

## An issue for deep learning-based world models: sensitivity of state-input gradients

The
**tl;dr**
of this section is: directly optimizing states through a deep learning-based $F\_{\theta}$ is incredibly brittle, Ã  la
*adversarial robustness*
. Even if you train your world model in a lower-dimensional state space, the training process for the world model makes unseen state landscapes very sharp, whether it be an unseen state itself or simply a normal/orthogonal direction to the data manifold.

### Adversarial robustness and the âdimpled manifoldâ model

Adversarial robustness originally looked at classification models $f\_\theta : \mathbb{R}^{w\times h \times c} \to \mathbb{R}^K$, and showed that by following the gradient of a particular logit $\nabla f\_\theta^k$ from a base image $x$ (not of class $k$), you did not have to move far along $xâ = x + \epsilon\nabla f\_\theta^k$ to make $f\_\theta$ classify $xâ$ as $k$ (
[Szegedy et al., 2014](https://arxiv.org/abs/1312.6199)
;
[Goodfellow et al., 2015](https://arxiv.org/abs/1412.6572)
):

![Adversarial example](https://bair.berkeley.edu/static/blog/grasp/adversarial_animated.gif)


*Depiction of the classic example from (Goodfellow et al., 2015).*

Later work has painted a geometric picture for whatâs going on: for data near a low-dimensional manifold $\mathcal{M}$, the training process controls behavior in tangential directions, but does not regularize behavior in orthogonal directions, thus leading to sensitive behavior (
[Stutz et al., 2019](https://arxiv.org/pdf/1812.00740)
). Another way stated: $f\_\theta$ has a reasonable Lipschitz constant when considering only tangential directions to the data manifold $\mathcal{M}$, but can have very high Lipschitz constants in normal directions. In fact, it often benefits the model to be sharper in these normal directions, so it can fit more complicated functions more precisely.

![Adversarial perturbations leave the data manifold](https://bair.berkeley.edu/static/blog/grasp/manifold_adversarial.gif)

As a result, such adversarial examples are incredibly common even for a single given model. Further, this is not just a computer vision phenomenon; adversarial examples also appear in LLMs (
[Wallace et al., 2019](https://arxiv.org/abs/1908.07125)
) and in RL (
[Gleave et al., 2019](https://arxiv.org/abs/1905.10615)
).

While there are methods to train for more adversarially robust models, there is a known trade-off between model performance and adversarial robustness (
[Tsipras et al., 2019](https://arxiv.org/pdf/1805.12152)
): especially in the presence of many weakly-correlated variables, the model
*must*
be sharper to achieve higher performance. Indeed, most modern training algorithms, whether in computer vision or LLMs, do not train adversarial robustness out. Thus, at least until deep learning sees a major regime change,
**this is a problem weâre stuck with**
.

### Why is adversarial robustness an issue for world model planning?

Consider a single component of the dynamics loss weâre optimizing in the lifted state approach:

\[\min\_{s\_t, a\_t, s\_{t+1}} \|F\_\theta(s\_t, a\_t) - s\_{t+1}\|\_2^2\]

Letâs further focus on just the base state:

\[\min\_{s\_t} \|F\_\theta(s\_t, a\_t) - s\_{t+1}\|\_2^2.\]

Since world models are typically trained on state/action trajectories $(s\_1, a\_1, s\_2, a\_2, \ldots)$, the state-data manifold for $F\_{\theta}$ has dimensionality bounded by the action space:

\[\mathrm{dim}(\mathcal{M}\_s) \le \mathrm{dim}(\mathcal{A}) + 1 + \mathrm{dim}(\mathcal{R}),\]

where $\mathcal{R}$ is some optional space of augmentations (e.g. translations/rotations). Thus, we can typically expect $\mathrm{dim}(\mathcal{M}\_s)$ to be much lower than $\mathrm{dim}(\mathcal{S})$, and thus:
**it is very easy to find adversarial examples that hack any state to any other desired state.**

As a result, the dynamics optimization

\[\sum\_{t=0}^{T-1} \big\|F\_\theta(s\_t,a\_t) - s\_{t+1}\big\|\_2^2\]

feels incredibly âsticky,â as the base points $s\_t$ can easily trick $F\_{\theta}$ into thinking itâs already made its local goal.
[1](#fn1)

![Adversarial world model example](https://bair.berkeley.edu/static/blog/grasp/pusht_adversarial.gif)


---

**1.**
This adversarial robustness issue, while particularly bad for lifted-state approaches, is not unique to them. Even for serial optimization methods that optimize through the full rollout map $\mathcal{F}^T$, it is possible to get into unseen states, where it is very easy to have a normal component fed into the sensitive normal components of $D\_s F\_{\theta}$. The action Jacobianâs chain rule expansion is

\[\Bigl(\prod\_{t=1}^T D\_s F\_\theta(s\_t, a\_t)\Bigr) D\_{a\_0}F\_\theta(s\_0, a\_0).\]

See what happens if any stage of the product has any component normal to the data manifold.
[â©](#ref1)

---

### Our fix

This is where our new planner GRASP comes in. The main observation: while $D\_s F\_{\theta}$ is untrustworthy and adversarial, the action space is usually low-dimensional and exhaustively trained, so $D\_a F\_{\theta}$ is actually reasonable to optimize through and doesnât suffer from the adversarial robustness issue!

![Network diagram showing high-dim state vs low-dim action](https://bair.berkeley.edu/static/blog/grasp/network_diagram.jpg)


*The action input is usually lower-dimensional and densely trained (the model has seen every action direction), so action gradients are much better behaved.*

At its core,
**GRASP builds a first-order lifted state / collocation-based planner that is only dependent on action Jacobians through the world model.**
We thus exploit the differentiability of learned world models $F\_{\theta}$, while not falling victim to the inherent sensitivity of the state Jacobians $D\_s F\_{\theta}$.

## GRASP: Gradient **RelAxed** **S** tochastic **P** lanner

As noted before, we start with the collocation planning objective, where we lift the states and relax dynamics into a penalty:

\[\min\_{\mathbf{s},\mathbf{a}} \mathcal{L}(\mathbf{s}, \mathbf{a}) = \sum\_{t=0}^{T-1} \big\|F\_\theta(s\_t,a\_t) - s\_{t+1}\big\|\_2^2,
\quad \text{with } s\_0 \text{ fixed and } s\_T=g.\]

We then make two key additions.

## Ingredient 1: Exploration by noising the **state iterates**

Even with a smoother objective, planning is nonconvex. We introduce exploration by injecting Gaussian noise into the
**virtual state updates**
during optimization.

A simple version:

\[s\_t \leftarrow s\_t - \eta\_s \nabla\_{s\_t}\mathcal{L} + \sigma\_{\text{state}} \xi, \qquad \xi\sim\mathcal{N}(0,I).\]

Actions are still updated by non-stochastic descent:

\[a\_t \leftarrow a\_t - \eta\_a \nabla\_{a\_t}\mathcal{L}.\]

The state noise helps you âhopâ between basins in the lifted space, while the actions remain guided by gradients. We found that specifically noising states here (as opposed to actions) finds a good balance of exploration and the ability to find sharper minima.
[2](#fn2)

---

**2.**
Because we only noise the states (and not the actions), the corresponding dynamics are not truly Langevin dynamics.
[â©](#ref2)

---

## Ingredient 2: Reshape gradients: stop brittle state-input gradients, keep action gradients

As discussed, the fragile pathway is the gradient that flows
*into the state input*
of the world model,
\(D\_s F\_{\theta}\)
. The most straightforward way to do this initially is to just stop state gradients into
\(F\_{\theta}\)
directly:

* Let $\bar{s}\_t$ be the same value as $s\_t$, but with gradients stopped.

Define the
**stop-gradient dynamics loss**
:

\[\mathcal{L}\_{\text{dyn}}^{\text{sg}}(\mathbf{s},\mathbf{a})
= \sum\_{t=0}^{T-1} \big\|F\_\theta(\bar{s}\_t, a\_t) - s\_{t+1}\big\|\_2^2.\]

This alone does not work. Notice now states only follow the previous stateâs step, without anything forcing the base states to chase the next ones. As a result, there are trivial minima for just stopping at the origin, then only for the final action trying to get to the goal in one step.

### Dense goal shaping

We can view the above issue as the goalâs signal being cut off entirely from previous states. One way to fix this is to simply add a dense goal term throughout prediction:

\[\mathcal{L}\_{\text{goal}}^{\text{sg}}(\mathbf{s},\mathbf{a})
= \sum\_{t=0}^{T-1} \big\|F\_\theta(\bar{s}\_t, a\_t) - g\big\|\_2^2.\]

In normal settings this would over-bias towards the greedy solution of straight chasing the goal, but this is balanced in our setting by the stop-gradient dynamics lossâs bias towards feasible dynamics. The final objective is then as follows:

\[\mathcal{L}(\mathbf{s},\mathbf{a}) = \mathcal{L}\_{\text{dyn}}^{\text{sg}}(\mathbf{s},\mathbf{a}) + \gamma \, \mathcal{L}\_{\text{goal}}^{\text{sg}}(\mathbf{s},\mathbf{a}).\]

The result is a planning optimization objective that does not have dependence on state gradients.

---

## Periodic âsyncâ: briefly return to true rollout gradients

The lifted stop-gradient objective is great for
**fast, guided exploration**
, but itâs still an approximation of the original serial rollout objective.

So every $K\_{\text{sync}}$ iterations, GRASP does a short refinement phase:

1. Roll out from $s\_0$ using current actions $\mathbf{a}$, and take a few small gradient steps on the original serial loss:

\[\mathbf{a} \leftarrow \mathbf{a} - \eta\_{\text{sync}}\,\nabla\_{\mathbf{a}}\,\|s\_T(\mathbf{a})-g\|\_2^2.\]

The lifted-state optimization still provides the core of the optimization, while this refinement step adds some assistance to keep states and actions grounded towards real trajectories. This refinement step can of course be replaced with a serial planner of your choice (e.g. CEM); the core idea is to still get some of the benefit of the full-path synchronization of serial planners, while still mostly using the benefits of the lifted-state planning.

---

## How GRASP addresses long-range planning

Collocation-based planners offer a natural fix for long-horizon planning, but this optimization is quite difficult through modern world models due to adversarial robustness issues.
*GRASP proposes a simple solution for a smoother collocation-based planner, alongside stable stochasticity for exploration*
. As a result, longer-horizon planning ends up not only succeeding more, but also finding such successes faster:

![Push-T planning demo](https://bair.berkeley.edu/static/blog/grasp/pusht_zoomout.gif)


*Push-T demo: longer-horizon planning with GRASP.*

| Horizon | CEM | GD | LatCo | **GRASP** |
| --- | --- | --- | --- | --- |
| H=40 | **61.4%** / 35.3s | 51.0% / 18.0s | 15.0% / 598.0s | 59.0% / **8.5s** |
| H=50 | 30.2% / 96.2s | 37.6% / 76.3s | 4.2% / 1114.7s | **43.4%** / **15.2s** |
| H=60 | 7.2% / 83.1s | 16.4% / 146.5s | 2.0% / 231.5s | **26.2%** / **49.1s** |
| H=70 | 7.8% / 156.1s | 12.0% / 103.1s | 0.0% / â | **16.0%** / **79.9s** |
| H=80 | 2.8% / 132.2s | 6.4% / 161.3s | 0.0% / â | **10.4%** / **58.9s** |

*Push-T results. Success rate (%) / median time to success. Bold = best in row. Note the median success time will bias higher with higher success rate; GRASP manages to be faster despite higher success rate.*

---

## Whatâs next?

There is still plenty of work to be done for modern world model planners. We want to exploit the gradient structure of learned world models, and collocation (lifted-state optimization) is a natural approach for long-horizon planning, but itâs crucial to understand typical gradient structure here: smooth and informative action gradients and brittle state gradients. We view GRASP as an initial iteration for such planners.

Extension to diffusion-based world models (deeper latent timesteps can be viewed as smoothed versions of the world model itself), more sophisticated optimizers and noising strategies, and integrating GRASP into either a closed-loop system or RL policy learning for adaptive long-horizon planning are all natural and interesting next steps.

I do genuinely think itâs an exciting time to be working on world model planners. Itâs a funny sweet spot where the background literature (planning and control overall) is incredibly mature and well-developed, but the current setting (pure planning optimization over modern, large-scale world models) is still heavily underexplored. But, once we figure out all the right ideas, world model planners will likely become as commonplace as RL.

---

For more details, read the
[full paper](https://arxiv.org/pdf/2602.00475)
or visit the
[project website](https://www.michaelpsenka.io/grasp/)
.

---

## Citation

```
@article{psenka2026grasp,
  title={Parallel Stochastic Gradient-Based Planning for World Models},
  author={Michael Psenka and Michael Rabbat and Aditi Krishnapriyan and Yann LeCun and Amir Bar},
  year={2026},
  eprint={2602.00475},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2602.00475}
}
```