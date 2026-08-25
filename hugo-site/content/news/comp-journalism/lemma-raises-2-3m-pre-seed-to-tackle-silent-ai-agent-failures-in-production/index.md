---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-08-25T18:46:19.422357+00:00'
exported_at: '2026-08-25T18:46:25.531480+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/lemma-raises-2-3m-pre-seed-to-tackle-silent-ai-agent-failures-in-production
structured_data:
  about: []
  author: ''
  description: 'AI agent reliability startup Lemma has raised $2.3 million in pre-seed
    funding to build monitoring infrastructure designed to catch a particularly difficult
    class of problem: AI agents that appear to have completed a tas...'
  headline: Lemma Raises $2.3M Pre-Seed to Tackle Silent AI Agent Failures in Production
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/lemma-raises-2-3m-pre-seed-to-tackle-silent-ai-agent-failures-in-production
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Lemma Raises $2.3M Pre-Seed to Tackle Silent AI Agent Failures in Production
updated_at: '2026-08-25T18:46:19.422357+00:00'
url_hash: 52a5cc129ae5763255a60f1c1a7d348fdfcdb02d
---

AI agent reliability startup
[Lemma](https://www.uselemma.ai/)
has raised $2.3 million in pre-seed funding to build monitoring infrastructure designed to catch a particularly difficult class of problem: AI agents that appear to have completed a task successfully while quietly producing the wrong result.

The round includes participation from
[Matrix](https://matrix.vc/)
,
[Y Combinator](https://www.ycombinator.com/)
,
[Liquid 2 Ventures](https://www.liquid2.vc/)
,
[Vermilion Cliffs Ventures](https://www.vermilion.fund/)
,
[Irregular Expressions](https://www.irregex.vc/)
,
[Cervin Ventures](https://www.cervinventures.com/)
,
[Comma Capital](https://comma.vc/)
,
[Position Ventures](https://positionventures.com/)
, and
[Eight Capital](https://www.eightcapital.com/)
, alongside angel investors and operators from OpenAI, xAI, Meta, and DoorDash.

Founded by Jerry Zhang and Cole Gawin, Lemma was part of Y Combinator’s Fall 2025 batch and focuses on production monitoring for AI agents. The company says its platform has now processed more than one million agent traces as engineering teams increasingly look for ways to understand how autonomous systems behave after deployment.

## The Growing Problem of AI Agents That Fail Silently

Traditional software monitoring is largely designed around explicit failure signals. An application crashes, a request returns an error code, latency spikes, or an infrastructure component becomes unavailable.

AI agents introduce a different problem.

An agent can successfully execute every technical step in a workflow and still misunderstand what the user wanted, call the wrong tool, use incorrect information, become stuck in an unproductive loop, or return a plausible but incorrect answer. From the perspective of conventional monitoring infrastructure, the request may look perfectly healthy.

Lemma describes these as semantic failures. Examples include a customer service agent citing the wrong refund policy, an auditing agent generating an outdated report, or an agent calling an external system using information it invented. These are common
[AI agent failure points.](https://www.unite.ai/the-ai-agents-trap-the-hidden-failure-modes-of-autonomous-systems-no-one-is-preparing-for/)

That distinction becomes increasingly important as agents move beyond conversational interfaces and begin executing longer, multi-step workflows where language models interact with databases, application programming interfaces (APIs), retrieval systems, and other software tools.

A failure somewhere in that chain may not produce an exception. The agent may simply continue.

## How Lemma Monitors AI Agents in Production

Lemma is building an observability layer specifically around these agent execution paths.

Its tracing system turns each agent execution into a structured trace containing the underlying large language model calls, tool invocations, inputs, outputs, timing data, retrieval steps, and errors generated throughout the workflow. Engineering teams can then examine an entire execution tree rather than looking only at the agent’s final response.

But tracing is only part of the approach.

Lemma analyzes production traces against an agent’s instructions and groups recurring problems into issues, helping teams identify failure patterns that might otherwise remain buried across thousands of individual interactions. The platform can also prioritize issues and send alerts through Slack when potentially significant problems appear.

The objective is to answer a more difficult question than whether the software ran successfully: Did the agent actually accomplish what it was supposed to accomplish?

That is a significant shift in how observability may need to work for agentic software.

## Turning Production Failures Into Agent Improvements

Lemma is also trying to shorten the distance between finding a problem and fixing it.

Once the platform identifies a recurring failure, it analyzes the surrounding traces and context to determine a likely root cause. From there, it can propose changes to prompts, application logic, or agent workflows rather than requiring engineers to manually reconstruct every problematic interaction.

The company is extending that workflow into development environments through a Model Context Protocol (MCP) server. Developers can query Lemma’s traces from tools including Cursor, Claude Desktop, and Claude Code, allowing the debugging process to happen closer to where the underlying agent is being developed.

After a fix is deployed, Lemma can turn the production failure into an online evaluation and monitor for its recurrence. This creates a feedback loop in which previously unseen real-world failures become future tests rather than remaining isolated incidents.

This approach pushes Lemma somewhat beyond conventional observability. The longer-term goal is infrastructure that helps agents learn systematically from production failures rather than relying entirely on engineers to discover, reproduce, and manually patch every edge case.

## A Problem the Founders Encountered Firsthand

Zhang and Gawin met as freshmen at the University of Southern California and later worked on AI systems at separate AI-native startups. Before founding Lemma, they worked at Tandem, which applies AI in healthcare, and ChipStack, which develops AI agents for chip design.

Those experiences helped expose them to the difficulty of taking agents from controlled development environments into production.

“Cole and I started Lemma because we experienced the pain of building AI agents firsthand,” Zhang said. “We kept running into the same problem: agents would appear to work, but the results weren’t reliable enough in production.”

The founders argue that improving underlying foundation models alone will not eliminate this problem. Real-world agent behavior also depends on prompts, application logic, tools, integrations, retrieval systems, user behavior, and the increasingly complicated chains connecting them.

Lemma’s own engineering thesis is that offline evaluations struggle to reproduce the unpredictable conditions agents encounter after deployment, making production data an important source for understanding where systems actually break down.

## The Broader Challenge of Monitoring AI Agents in Production

The new funding will support further development of Lemma’s monitoring and failure-detection tools, with an initial focus on startups already running AI agents in production.

The company is operating in an area that is becoming more important as AI systems move from isolated demonstrations into real-world workflows. Traditional observability tools are generally good at detecting technical problems such as downtime, latency, or failed requests, but agentic systems introduce another layer of complexity: an application can remain operational while the agent misunderstands a task, chooses the wrong tool, or produces an incorrect result.

That distinction is likely to become more significant as agents are used across customer support, financial analysis, healthcare administration, software development, and research. In these environments, measuring whether an agent completed a workflow may matter less than determining whether it completed the workflow correctly.

For Lemma, the opportunity therefore depends on whether monitoring semantic failures becomes a standard part of operating AI agents in production. The $2.3 million pre-seed round gives the company additional capital to test that thesis as organizations deploy agents across increasingly complex workflows.

## What Better Agent Monitoring Could Mean for AI

As AI agents take on more complex and autonomous work, traditional monitoring may no longer be enough. Future systems will need to assess not only whether an agent completed a task, but whether it understood the objective, used the right tools, and produced the correct outcome.

Tools like
[Lemma](https://www.uselemma.ai/)
could also create tighter feedback loops between production and development, turning real-world failures into new tests and improvements. Over time, this could make agent observability a standard part of the AI infrastructure stack, particularly in high-stakes environments where reliability and accountability matter most.