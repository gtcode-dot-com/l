---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-08T16:15:40.075399+00:00'
exported_at: '2026-04-08T16:15:42.302853+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/ibm-research/altk-evolve
structured_data:
  about: []
  author: ''
  description: A Blog post by IBM Research on Hugging Face
  headline: 'ALTK‑Evolve: On‑the‑Job Learning for AI Agents'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/ibm-research/altk-evolve
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ALTK‑Evolve: On‑the‑Job Learning for AI Agents'
updated_at: '2026-04-08T16:15:40.075399+00:00'
url_hash: 1702c67bf9a3f0af1d953058f63a72d146fb7acc
---

# ALTK‑Evolve: On‑the‑Job Learning for AI Agents

* Most AI agents re‑read transcripts instead of learning principles, so they repeat mistakes and don’t transfer lessons to new situations.
* **ALTK‑Evolve**
  turns raw agent trajectories into reusable guidelines.
* In benchmarks, the approach boosted reliability, especially on hard (Δ 14.2% on AppWorld), multi‑step tasks, without bloating context.

## The “eternal intern” problem

Imagine a brilliant line cook who has memorized every cookbook but forgets your kitchen every morning. They don’t remember your oven runs hot, or that regulars like extra salt; they’ll follow a recipe card yet freeze when you’re out of lemons. That’s most AI agents: excellent at following prompts, poor at
**accumulating wisdom**
about your environment. Feeding yesterday’s logs back into the prompt just makes them
**re‑read**
history; it doesn’t help them
**generalize**
from it.

A junior needs different recipes for “vinaigrette” and “duck à l’orange.” A chef learns “acid balances fat” and applies it everywhere. Likewise, reliable agents should distill principles from experience and apply them to new tasks, not just near duplicates of old ones. This
**long‑term memory subsystem**
does exactly that: it converts interaction traces into candidate guidelines, filters for quality, and injects only relevant guidance at the moment of action. Agents need principles, not transcripts.

A recent
[MIT study](https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/)
found that 95% of pilots fail because agents don't adapt and learn on the job. ALTK-Evolve addresses this learning gap using long term episodic memory to help agents reason better.

## Solution: long term memory with ALTK-Evolve

Evolve is a memory system for AI agents, that can help agents improve over time, learning from and using guidelines generated from previous executions.

Operationally, the system runs as a continuous loop:

1. **Downward flow (observation & extraction):**
   Capture full agent trajectories (user utterances, thoughts, tool calls, results) in an Interaction Layer (e.g., Langfuse or another OpenTelemetry‑based observability tool). Pluggable extractors mine traces for structural patterns and persist them as candidate entities.
2. **Upward flow (refinement & retrieval):**
   A background consolidate‑and‑score job merges duplicates, prunes weak rules, and boosts proven strategies, evolving a high‑quality library of entities such as guidelines, policies, and SOPs. Retrieval pulls only the relevant items via the Interaction Layer and injects them back into context at the Application Layer.

[![architecture (1)](https://cdn-uploads.huggingface.co/production/uploads/6435a1131860001f144239ea/9PDbajGcnsI1nQ8NZ8LEM.png)](https://cdn-uploads.huggingface.co/production/uploads/6435a1131860001f144239ea/9PDbajGcnsI1nQ8NZ8LEM.png)

This approach works for a few key reasons:

* **Teaches judgment:**
  Converts one‑off events into portable strategies that transfer across tasks.
* **Controls noise:**
  Scoring keeps memory lean and useful, not a growing junk drawer.
* **Progressive Disclosure:**
  Retrieval is just‑in‑time, not stuffing everything into the context.

## Results: better reliability, especially on hard tasks

We evaluated the framework on
[AppWorld](https://appworld.dev)
, where agents complete realistic multi‑step tasks via APIs, averaging 9.5 APIs across 1.8 apps, with hard cases requiring more complex control flow. A ReAct agent received the task instruction plus the top 5 retrieved guidelines generated on a prior run (train/dev) and tested on an unseen partition (test-normal). We report Scenario Goal Completion (SGC), a strict consistency metric requiring success across variants.

| Difficulty | Baseline SGC | + Memory | Δ |
| --- | --- | --- | --- |
| Easy | 79.0% | 84.2% | +5.2 |
| Medium | 56.2% | 62.5% | +6.3 |
| **Hard** | **19.1%** | **33.3%** | **+14.2** |
| **Aggregate** | **50.0%** | **58.9%** | **+8.9** |

Here are some key conclusions from the evaluations:

* **Generalization:**
  The agent improves on the unseen Test‑Normal tasks, evidence that it’s learning principles, not memorizing recipes.
* **Complexity scaling:**
  The harder the task, the more the agent benefits from concise learned guidelines, with the largest lift on the more difficult tasks. The Hard tasks saw a 74% relative increase in success, where guidelines are useful to navigate the intricate control flows.
* **Consistency:**
  SGC gains exceeded raw pass‑rate improvements, reducing “flaky” behavior across scenario variants. The guidelines don’t just help the agent solve tasks, they help them solve them reliably across variants.

Find more details about the experiments in the paper at
<https://arxiv.org/abs/2603.10600>
.

## Getting started (choose your path)

You have a choice in how to integrate
**ALTK‑Evolve**
into your agent.

### No‑code with Claude Code, Codex, and IBM Bob (Lite mode)

Install the plugin into Claude Code:

```
claude plugin marketplace add AgentToolkit/altk-evolve
claude plugin install evolve@evolve-marketplace
```

That’s it! The plugin extracts entities from trajectories and stores them as files on your filesystem. It uses Claude Code’s hooks for automatic retrieval.

Prefer to watch instead of read? See the short
**Evolve-Lite Claude Code walkthrough**
(video):
[Demo](https://youtu.be/XIlYA79pYp4)

Check out the walkthroughs
[here](https://github.com/AgentToolkit/altk-evolve/blob/main/docs/integrations/claude/evolve-lite.md)
for examples of how to learn with Claude Code in Lite mode.

Lite mode is easy to test‑drive but has limitations. For example, it doesn’t glean insights from across agent sessions or perform consolidation and garbage collection of entities. The low‑code and pro‑code versions below address these limitations.

There are also one-step integrations with
[Codex](https://agenttoolkit.github.io/altk-evolve/examples/hello_world/codex/)
and
[IBM Bob](https://agenttoolkit.github.io/altk-evolve/examples/hello_world/bob/)
. Try them out!

### Low‑code with a ReAct agent

Add a single
`altk_evolve.auto`
import and flip a flag to emit traces to an Arize Phoenix UI. Then sync traces to generate improvement guidelines without changing your current stack. It works with popular LLM clients and agent frameworks (e.g., OpenAI, LiteLLM, and Hugging Face agents), so you keep your current stack and simply gain visibility.

To see just how easily this fits into existing projects, explore our
[hands‑on examples](https://github.com/AgentToolkit/altk-evolve/tree/main/examples/low_code)
showcasing different framework integrations. For full details on configuration and capabilities, read our
[low‑code tracing documentation](https://github.com/AgentToolkit/altk-evolve/blob/main/docs/guides/low-code-tracing.md)
.

### Pro‑code with CUGA

We integrated ALTK‑Evolve directly into
[CUGA](https://github.com/cuga-project/cuga-agent)
via MCP to create a tight, low‑overhead learning loop. Before each run, the
[`get_guidelines`](https://github.com/cuga-project/cuga-agent/blob/kaizen-lite-mode/src/cuga/backend/cuga_graph/nodes/cuga_lite/cuga_lite_graph.py#L738-L755)
MCP tool is called to surface task‑specific steering and reduce trial‑and‑error. After the run, CUGA sends back structured execution traces via
[`save_trajectory`](https://github.com/cuga-project/cuga-agent/blob/9773d66aba33895d42e335af780dbd3ff202fec9/src/cuga/backend/cuga_graph/nodes/cuga_lite/cuga_lite_node.py#L393-L408)
, so Evolve can learn from what actually happened and improve future guidance. The result is an integration that gets better over time while staying transparent, composable, and easy to adopt.

Prefer a visual tour? Watch the
**CUGA integration walkthrough**
:
[video](https://youtu.be/r9gQ1LsP61A)

## Try it & tell us what your agent learned

Your agent shouldn’t wake up as an intern every morning. This approach helps it learn on the job.
If you're using Claude Code, Codex, and IBM Bob, try it out in minutes and see how it improves your agent.

> Star the repo, it helps others discover the project and directly guides what we build next.

## Watch the demos

* **Claude Code walkthrough (video):**
  [Demo](https://youtu.be/XIlYA79pYp4)
* **OpenAI Codex walkthrough (video):**
  [Demo](https://youtu.be/IBc59bLjdi8)
* **IBM Bob demo walkthrough (video):**
  [Demo](https://youtu.be/YlTJoSJ4eDg)
* **CUGA integration walkthrough**
  :
  [video](https://youtu.be/r9gQ1LsP61A)