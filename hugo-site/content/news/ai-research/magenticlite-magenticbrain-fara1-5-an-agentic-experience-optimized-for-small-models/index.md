---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-23T03:04:47.656515+00:00'
exported_at: '2026-05-23T03:04:53.469699+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/magenticlite-magenticbrain-fara1-5-an-agentic-experience-optimized-for-small-models
structured_data:
  about: []
  author: ''
  description: 'MagenticLite is an agentic system for small models that works across
    the browser and local file system in a single workflow. It combines specialized
    models and orchestration to support efficient agentic performance on everyday
    tasks:'
  headline: 'MagenticLite, MagenticBrain, Fara1.5: An agentic experience optimized
    for small models'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/magenticlite-magenticbrain-fara1-5-an-agentic-experience-optimized-for-small-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'MagenticLite, MagenticBrain, Fara1.5: An agentic experience optimized for
  small models'
updated_at: '2026-05-23T03:04:47.656515+00:00'
url_hash: f96a606167973a6c3f1fabbd8675b04750916890
---

![MagenticLite](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/MagenticLite-BlogHeroFeature-1400x788-1-scaled.jpg)

## At a glance

* MagenticLite is an agentic application that works across both the browser and local file system in a single workflow. Built as the next generation of Magentic-UI, it combines a redesigned app with a harness optimized for small models.
* MagenticBrain and Fara1.5 are small models designed for orchestration and computer-use tasks, respectively. Fara1.5 is the next iteration of Fara and delivers measurable gains on real-world browser tasks.
* Together, these releases explore how far agentic performance can be pushed with smaller models, codesigned tools, and an optimized execution harness.

Today,
[Microsoft Research AI Frontiers](https://www.microsoft.com/en-us/research/lab/ai-frontiers/)
releases
[MagenticLite
(opens in new tab)](https://aka.ms/MagenticLite)
, an experimental agentic application designed for small models. As the next generation of Magentic-UI, it works across the browser and local file system in a single workflow.

MagenticLite is powered by two purpose-built models: MagenticBrain, for reasoning, delegation, and terminal use, and Fara1.5, a computer-use model family for browser-based tasks. The three components were designed to work together as a single system. The result is an agent that runs efficiently, keeps data on the user’s machine, and supports a broad range of agentic tasks. It also points toward a broader goal: capable agents that can run directly on users’ hardware.

The project is built around a key research bet: that agentic capability depends on tool orchestration and action rather than knowledge alone. That insight makes it possible to use smaller models while still enabling a broad range of agentic tasks at a fraction of the cost.

MagenticLite also reflects how we approach agentic AI end-to-end—from training data and model design to orchestration, interaction design, and human oversight throughout the experience.

![Figure 1 – One experience, three components.png | A diagram titled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/magentic_releases.png)


Figure 1. One experience, three components: MagenticLite, MagenticBrain, and Fara1.5.

## Included in this release

[**MagenticLite**

(opens in new tab)](https://aka.ms/MagenticLite)

The next generation of
[Magentic-UI](https://www.microsoft.com/en-us/research/blog/magentic-ui-an-experimental-human-centered-web-agent/)
, our experimental agentic experience, is powered by an agent harness rebuilt for small models, with an updated user interface informed by community feedback. It works across users’ browsers and local file systems in a single workflow.

**[MagenticBrain
(opens in new tab)](https://aka.ms/MagenticBrain-foundry)**

MagenticBrain is MagenticLite’s planner, coder, and delegator in one. It turns vague requests into concrete plans, selects the right tool or subagent for each step, writes code when needed, and recovers should something break mid-task.

[**Fara1.5**](https://www.microsoft.com/en-us/research/articles/fara1-5-computer-use-agent/)

The next generation of our computer-use model family, Fara1.5 comes  in three sizes, with a flagship 9-billion-parameter model for most use cases. Fara1.5 sets new state-of-the-art (SOTA) results among small computer-use models and nearly doubles Fara-7B’s performance on web navigation, with sharper handling of forms, credentialed sites, and long-running tasks.

Each component is useful on its own, but they work best together. Codesigning the app, models, and the harness enables capable and reliable agentic performance at this scale.

### Our research approach: Doing more with less

We started with a simple question: what does it take to make a small model genuinely good at agentic tasks? The answer spanned the full lifecycle—data generation, training objectives, model design, and orchestration had to be redesigned together rather than in isolation.

We identified requirements from real-world use cases like filling out forms, conducting browser research, and managing files locally, and built an evaluation dataset around them. Standard benchmarks capture part of the picture, but they are not always a direct measure of real-world usefulness. Scenario-based evaluations complemented those benchmarks and became a key signal for iterative improvement across both the models and the harness, as shown in Figure 2.

![Figure 2 – Eval flywheel.png | A flowchart titled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure-2-Eval-flywheel-e1778687653105.png)


Figure 2. An iterative process for building agentic systems involves defining success criteria, evaluating performance, and refining the models or system design (or both). Then repeat.

For the user experience, we retained key elements from Magentic-UI, including visibility into the agent’s reasoning and actions, the ability for users to take direct control, and explicit approval at critical points. Based on
[recent user studies](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/07/magentic-ui-report.pdf?msockid=1d972c2941d266e30aae39e740b967e6)
, we also made MagenticLite easier to learn and collaborate with through updated browser and chat views, designed to make it easier for users to understand the agent’s actions and intervene when needed. This is illustrated in Figure 3.

![Figure 3 – MAGUI new interface.png | A screenshot of the MagenticLite 2.0.063 application interface. The left sidebar shows a session history with task names and statuses, including one active task highlighted in pink. The central panel displays an ongoing agent session with a sequential log of actions—including ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure-3-MAGUI-new-interface-scaled-e1778687236569.png)


Figure 3. MagenticLite’s interface includes updated browser and chat views designed to make it easier to understand agent actions and intervene when needed.

Spotlight: AI-POWERED EXPERIENCE

## Microsoft research copilot experience

Discover more about research at Microsoft through our AI-powered experience

Opens in a new tab

## System components

### Fara1.5: A computer-use model that outperforms its weight class

Fara1.5 is the next generation of our computer-use model family, which is available in three sizes, with a flagship 9B model recommended for most use cases. Fara1.5 achieves new SOTA performance among small computer-use models and nearly doubles Fara-7B’s performance on web navigation, with better handling of forms, credentialed sites, and long-running tasks.

Last November,
[we released Fara-7B](https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/)
, a small agentic model built for completing tasks in a web browser. It was trained using a novel synthetic data generation engine that enabled best-in-class performance. Fara1.5 is the next step in that bet: a family of three models (4B, 9B, 27B) based on Qwen 3.5, designed to close the gaps we saw in the prior release.

### What’s new

**State-of-the-art results**
. On the popular Online-Mind2Web benchmark, which contains 300 tasks across widely used web domains, Fara1.5 sets new SOTA results for models in its size class. Fara1.5 outperforms all similarly sized models and nearly doubles the performance of Fara-7B. The larger Fara1.5-27B variant achieves more than 90% performance on the same benchmark.

![Figure 4 – Fara-1.5 latest results.png | A bar chart titled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure4-high-res_magenticlite-scaled.png)


Figure 4. On the OnlineMind2Web benchmark, Fara‑1.5-9B achieves state-of-the-art performance among models in its size class and substantially outperforms prior models.

**Improved user experience**
. In addition to improvements on benchmarks, we improved the user experience of Fara1.5. Users should observe stronger performance on everyday tasks like filling out forms, handling logins for credentialed sites, and booking appointments. These improvements are driven by the next evolution of our FaraGen data generation pipeline. Alongside training on live websites, we also trained the model on highly realistic synthetic environments designed to simulate scenarios like logins and irreversible actions.

**A native action space tuned for long-running tasks**
. Beyond clicks and keyboard actions, Fara1.5 has built-in tools to store key information in its context across hundreds of steps and ask the user for permission or preferences when needed, helping it stay coherent on tasks that span many minutes of real work.

**Recalibrated critical points**
. Fara-7B was trained to detect critical points for activities like transactions, login flows, or irreversible submissions and flag them. In Fara1.5, we refined our design around critical points based on our learnings from real use, so safety triggers still occur when they should but do not block useful tasks, such as form-filling.

![Figure 5 – Critical point.png | A screenshot of Fara1.5's browser interface showing a live view of the LinkedIn sign-up and sign-in page, with fields for email and password visible. Below the browser panel, a section titled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure5-Critical-points-high-res_magenticlite.png)


Figure 5. Fara1.5 pauses and requests user intervention when it detects a critical point, in this case during a sign-in to a LinkedIn account using email credentials.

### MagenticBrain: The orchestrator model

MagenticBrain is a 14B-parameter orchestration model—planner, coder, and delegator in one. Fine-tuned from Qwen 3 14B, MagenticBrain was trained end-to-end within the MagenticLite harness with the same tool schemas and execution environment it will encounter at inference time. As a result, there is no gap between how it learned to orchestrate and how it runs.

In many agentic systems, orchestration (planning and coordination) is the most reasoning-intensive component, so teams have historically relied on their most capable models for this role. Our bet is that small models can handle this role without sacrificing capability. Two design choices make that possible.

The first involves combining multistep tool-calling trajectories—where the model learns to pick the right tool and call it correctly—with coding and terminal trajectories—where the right answer is sometimes five lines of Python, not a tool call. This is paired with tight coupling between the tool format used during training and inference.

The second is computer-use agent (CUA) delegation. A key part of the orchestrator’s job is knowing when not to act itself and instead handing off a task to Fara1.5. Our data pipeline includes explicit delegation trajectories: sequences where the orchestrator recognizes a browser or user interface (UI) task, issues a structured handoff to the CUA model, waits for the result, and resumes the task. The result is an orchestrator model that reasons, codes, calls tools, and delegates fluidly within a single 14B footprint. We are releasing MagenticBrain which is designed for use with MagenticLite.

![Figure 6 – MagenticBrain.png | A flow diagram illustrating MagenticBrain's role as an orchestration model. At the top, a box represents the user's natural-language request: ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure-6-MagenticBrain.png)


Figure 6. MagenticBrain is a small orchestration model that can break down a natural-language request into smaller steps, select the right tools, write code when needed, and delegate browser tasks to Fara1.5.

### The Harness: Built for small models

The harness combines the orchestrator and browser-use models into a single workflow. Three design choices matter most:

* **Step-by-step planning**
  . The harness plans incrementally, keeping the system flexible and enabling smoother course correction and recovery throughout long-running tasks.
* **Active context management**
  . Small models have smaller effective context windows and degrade faster as context grows. The harness actively curates what each model receives at each step, keeping prompts focused, surfacing only the necessary information, condensing earlier interactions into concise summaries, and offloading the rest, so the orchestrator and Fara1.5 remain effective across long tasks.
* **Delegation through subagents**
  . Rather than relying on a single small model for every task, the orchestrator acts as the main agent and delegates specialized work to subagents. This means handing off browser tasks to Fara1.5. This pattern plays to the strengths of small language models by allowing each model to handle a narrower, more specialized part of the problem. It also lays the foundation for future expansion: later versions could introduce additional subagents and run them in parallel for richer, more efficient workflows.

The harness preserves the human-in-the-loop guarantees from Magentic-UI 1.0. Critical points across both browser and code actions still pause for explicit user approval, and the entire system runs inside
[Quicksand
(opens in new tab)](https://github.com/microsoft/quicksand)
, an open-source wrapper created for a QEMU-based sandbox, which isolates browser sessions and code execution from the host system.

![Figure 7 – MagenticLite architecture diagram | A layered system architecture diagram for MagenticLite, organized top to bottom across four labeled sections. The topmost layer, User Interface, contains the Frontend (React SPA) with four components: Chat (conversational task input), Live Browser (noVNC stream of agent session), Approvals (human-in-the-loop gates), and Files (inputs and generated outputs). Below it, connected via WebSocket and REST, is the Orchestration layer containing the Agentic Harness (FastAPI + WebSocket). It includes four components: Orchestration (run lifecycle, streaming), Context Compaction (summarize and prune long contexts), Pause/Resume (user-in-the-loop control), and Critical Points (detection of critical code actions), which is visually highlighted in yellow to signal its importance. The next layer is reached via a Dispatch connector and contains two parallel model components. On the left, MagenticBrain (14B model, purple) handles reasoning, coding, and delegation, with two sub-components: Reasoning Loop (think → tool → result) and Tool Dispatch (bash, edit, search, open). On the right, Fara 1.5 (9B model, teal) handles web navigation and browser use, with three sub-components: Screenshot → Action (vision-driven loop), Browser Actions (navigate, click, type, scroll), and Critical Points (forms, payments, logins). An arrow labeled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/Figure-7-MagenticLite-Architecture-Diagram.png)


Figure 7. Overview of the MagenticLite architecture. The system uses a layered architecture spanning the front end, harness, models, and sandboxed execution environment.

### See it in action

MagenticLite can perform a wide range of tasks across the browser and local file system, such as filling out forms, making appointments, organizing local files, and searching for and analyzing information.

[
](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/MagenticLite-Fill-Expenses-Forms-Final-Demo.mp4)


MagenticLite | Fill expense forms demo

[
](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/MagenticLite-Finding-and-Booking-a-Restaurant-Final-Demo.mp4)


MagenticLite | Find and book a restaurant demo

[
](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/MagenticLite-Find-Prices-for-Recipe-Ingredients-Final-Demo.mp4)


MagenticLite | Find prices for recipe ingredients demo

[
](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/MagenticLite-Organize-Local-Files-Final-Demo.mp4)


MagenticLite | Organize local files demo

## Try it, and build with us

MagenticLite, MagenticBrain, and Fara1.5 are research releases intended to support continued exploration and development. We are releasing them to encourage experimentation, evaluation, and feedback from the broader community.

## Contributors

* **Agentic experience**
  :
  [Cheng Tan](https://www.microsoft.com/en-us/research/people/chetan/)
  ,
  [Maya Murad](https://www.microsoft.com/en-us/research/people/mayamurad/)
  ,
  [Weili Shi](https://www.microsoft.com/en-us/research/people/weilishi/)
* **Agentic harness**
  :
  [Adam Fourney](https://www.microsoft.com/en-us/research/people/adamfo/)
  ,
  [Tyler Payne](https://www.microsoft.com/en-us/research/people/tylerpayne/)
* **Fara1.5**
  :
  [Alexey Taymanov](https://www.microsoft.com/en-us/research/people/ataymano/)
  ,
  [Andrew Zhao](https://www.microsoft.com/en-us/research/people/andrewzhao/)
  ,
  [Aravind Rajeswaran](https://www.microsoft.com/en-us/research/people/arrajeswaran/)
  ,
  [Corby Rosset](https://www.microsoft.com/en-us/research/people/corbyrosset/)
  ,
  [Hussein Mozannar](https://www.microsoft.com/en-us/research/people/hmozannar/)
  ,
  [Luiz Do Valle](https://www.microsoft.com/en-us/research/people/luizdovalle/)
  ,
  [Spencer Whitehead](https://www.microsoft.com/en-us/research/people/spwhitehead/)
  ,
  [Vibhav Vineet](https://www.microsoft.com/en-us/research/people/vivineet/)
  , Zach Nussbaum,
  [Sahil Gupta](https://www.microsoft.com/en-us/research/people/t-sahilgupta/)
  ,
  [Yadong Lu](https://www.microsoft.com/en-us/research/people/luyadong/)
* **MagenticBrain**
  :
  [Ahmed Elgohary Ghoneim](https://www.microsoft.com/en-us/research/people/ahmedghoneim/)
  ,
  [Akshay Nambi](https://www.microsoft.com/en-us/research/people/akshayn/)
  , Amir Saeidi, Caio César Teodoro Mendes,
  [Harkirat Behl](https://www.microsoft.com/en-us/research/people/hbehl/)
  , Karan Gupta,
  [Pashmina Cameron](https://www.microsoft.com/en-us/research/people/pcameron/)
  , Pranav Vajreshwari,
  [Shital Shah](https://www.microsoft.com/en-us/research/people/shitals/)
  ,
  [Yash Lara](https://www.microsoft.com/en-us/research/people/yashlara/)
  ,
  [Yash Pandya](https://www.microsoft.com/en-us/research/people/yashpandya/)
* **Collaborators**
  : Abhishek Gowami,
  [Amanda Swearngin](https://www.microsoft.com/en-us/research/people/aswearngin/)
  ,
  [Michael Harrison](https://www.microsoft.com/en-us/research/people/mharrison/)
  ,
  [Sara Abdali](https://www.microsoft.com/en-us/research/people/saraabdali/)
  , Sarthak Harne,
  [Vidhisha Balachandran](https://www.microsoft.com/en-us/research/people/vidhishab/)
* **Project leads**
  :
  [Ahmed Awadallah](https://www.microsoft.com/en-us/research/people/hassanam/)
  ,
  [Rafah Hosn](https://www.microsoft.com/en-us/research/people/raaboulh/)
* **Sponsors**
  :
  [Ahmed Awadallah](https://www.microsoft.com/en-us/research/people/hassanam/)
  ,
  [Ece Kamar](https://www.microsoft.com/en-us/research/people/eckamar/)
  ,
  [Rafah Hosn](https://www.microsoft.com/en-us/research/people/raaboulh/)
  ,
  [Saleema Amershi,](https://www.microsoft.com/en-us/research/people/samershi/)
  [Shital Shah](https://www.microsoft.com/en-us/research/people/shitals/)

Opens in a new tab