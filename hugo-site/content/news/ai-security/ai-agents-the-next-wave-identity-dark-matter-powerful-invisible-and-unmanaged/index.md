---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T05:30:34.306578+00:00'
exported_at: '2026-03-09T05:30:36.919452+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/ai-agents-next-wave-identity-dark.html
structured_data:
  about: []
  author: ''
  description: 70% of enterprises run AI agents, but weak IAM governance risks identity
    “dark matter” and cross-cloud exposure, survey finds.
  headline: 'AI Agents: The Next Wave Identity Dark Matter - Powerful, Invisible,
    and Unmanaged'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/ai-agents-next-wave-identity-dark.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'AI Agents: The Next Wave Identity Dark Matter - Powerful, Invisible, and Unmanaged'
updated_at: '2026-03-09T05:30:34.306578+00:00'
url_hash: b4123d87dd227bcee21c5a82dab133bfd3b39993
---

## **The Rise of MCPs in the Enterprise**

The Model Context Protocol (MCP) is quickly becoming a practical way to push LLMs from “chat” into real work. By providing structured access to applications, APIs, and data, MCP enables prompt-driven AI agents that can retrieve information, take action, and automate end-to-end business workflows across the enterprise. This is already showing up in production through horizontal assistants and custom vertical agents. like Microsoft Copilot, ServiceNow, Zendesk bots, and Salesforce Agentforce, with custom and vertical agents moving fast behind them. This echoes the recent
[Gartner](https://gartner.com)
“Market Guide for Guardian Agents”
[report](https://www.gartner.com/document/7509053)
, where analysts note that the rapid enterprise adoption of these AI agents is significantly outpacing the maturity of the governance and policy controls required to manage them.

We believe the primary disconnect is that these AI “colleagues” don’t look like humans.

* They don’t join or leave through HR
* They don’t submit access requests
* They don’t retire accounts when projects end

They’re often invisible to traditional IAM, and that’s how they become identity dark matter: real identity risk outside the governance fabric. And agentic systems don’t just use access, they hunt for the path of least resistance. They’re optimized to finish the job with minimal friction: fewer approvals, fewer prompts, fewer blockers. In identity terms, that means they’ll gravitate toward whatever already works, in-app-local accounts, stale service identities, long-lived tokens, API keys, bypass auth paths, and if it works, it gets reused.

Team8’s
[2025 CISO Village Survey](https://team8.vc/ciso-village-survey-2025/)
found:

* Nearly
  **70% of enterprises already run AI agents (any system that can answer and act) in production**
  .
* Another
  **23% are planning deployments in 2026**
  .
* **Two-thirds**
  are building them in-house.

MCP adoption isn’t a question of if; it’s a question of how fast and wisely. It’s already here, and it’s only accelerating. Complicating this further is the reality of hybrid environments. Based on the Gartner research, it seems that organizations face significant hurdles in managing these non-human identities because native platform controls and vendor safeguards generally do not extend beyond their own cloud or platform borders. Without an independent oversight mechanism, cross-cloud agent interactions remain entirely ungoverned. The real question is whether your AI agents become trusted teammates or
[unmanaged identity dark matter](https://eu1.hubs.ly/H0sbqmr0)
?

​​
VIDEO

## **How Identity Dark Matter Gets Abused by Agent-AI**

As autonomous AI agents that can plan and execute multi-step tasks with minimal human input, Agent AI is a powerful assistant but also a major cyber risk. Interestingly, leading industry analysts seem to expect that the vast majority of unauthorized agent actions will stem from internal enterprise policy violations, such as misguided AI behavior or information oversharing, rather than malicious external attacks.

The typical abuse pattern we see is similar, driven by agent automation and shortcut-seeking:

* Enumerate what exists: Agent crawls apps and integrations, lists users/tokens, discovers “alternate” auth paths.
* Try what’s easy first: Local accounts, legacy creds, long-lived tokens, anything that avoids a fresh approval.
* Lock onto “good enough” access: Even low privilege is enough to pivot: read configuration files, pull logs, discover secrets, map organization structure.
* Upgrade quietly: Find over-scoped tokens, stale entitlements, or dormant-but-privileged identities and escalate with minimal noise.
* Operate at machine speed: Thousands of small actions occur across many systems, too fast and too wide for humans to spot early.

The real risk here is the scale of impact: one neglected identity becomes a reusable shortcut across the estate.

## **The Dark Matter Risks**

In addition to abusing identity dark matter, left unchecked, MCP agents (AI Agents that use the MCP protocol to connect to apps, A2A, APIs, and data sources) introduce their own hidden exposures. Orchid uncovers these exposures every day:

* Over-permissioned access: Agents get “god mode” so they don’t fail, and then that privilege becomes the default operating state.
* Untracked usage: Agents can execute sensitive workflows through tools where logs are partial, inconsistent, or not correlated back to a sponsor.
* Static credentials: Hardcoded tokens don’t just “live forever”, they become shared infrastructure across agents, pipelines, and environments.
* Regulatory blind spots: Auditors ask, “who approved access, who used it, and what data was touched?” Dark matter makes those answers slow, or impossible.
* Privilege drift: Agents accumulate access over time because removing permissions is scarier than granting them, until an attacker inherits the drift.

We believe addressing these blind spots aligns with Gartner’s observation that modern AI governance requires identity and access management to tightly converge with information governance. This ensures organizations can dynamically classify data sensitivity and monitor real-time agent behavior instead of relying solely on static credentials.

AI agents aren’t just users without badges. They’re
[dark matter](https://139840798.fs1.hubspotusercontent-eu1.net/hubfs/139840798/Buyers%20Guide%20%E2%80%93%20Content.pdf)
identities: powerful, invisible, and outside the reach of today’s IAM. And the uncomfortable part: even well-intentioned agents will exploit dark matter. They don’t understand your org chart or your governance intent; they understand what works. If an
[orphaned account](https://eu1.hubs.ly/H0scyWc0)
or over-scoped token is the fastest path to completion, it becomes the “efficient” choice.

## **Principles for Safe MCP Adoption**

To avoid repeating the mistakes of the past (with orphaned or overprivileged accounts, shadow IT, unmanaged keys, and invisible activity), organizations need to adapt and apply core identity principles to AI agents. Gartner introduced the concept of specialized "guardian" systems, supervisory AI solutions that continuously evaluate, monitor, and enforce boundaries on working agents.

We recommend organizations follow 5 core principles as they deploy MCP-based agentic solutions.

1. **Pair AI Agents with Human Sponsors:**
   Every agent should be tied to an accountable human operator. If the human changes roles or leaves, the agent’s access should change with them. We agree with Gartner on the necessity of ownership mapping, ensuring full lineage from creation to deployment is tracked to both the machine and its human owner.
2. **Dynamic, Context-Aware Access:**
   AI agents should not hold standing, permanent privileges. Their entitlements should be time-bound, session-aware, and limited to least privilege.
3. **Visibility and Auditability:**
   Gartner has been increasingly calling for organizations to maintain a centralized AI agent catalog that inventories all official, shadow, and third-party agents, alongside comprehensive posture management and tamper-evident audit trails. In our view, every action an AI agent takes should be logged, correlated back to its human sponsor, and made available for review. This ensures accountability and prepares organizations for future compliance scrutiny. Visibility isn’t just “we logged it.” You need to tie actions to data reach: what the agent accessed, what it changed, what it exported, and whether that action touched regulated or sensitive datasets. Otherwise, you can’t distinguish “useful automation” from “silent data movement”.
4. **Governance at Enterprise Scale:**
   MCP adoption should extend across both new and legacy systems within a single, consistent governance fabric, so that security, compliance, and infrastructure teams are not working in silos. This is also where Gartner emphasizes the importance of an enterprise-owned supervisory layer, one that ensures consistent controls and reduces the risk of vendor lock-in as MCP adoption expands.
5. **Commitment to Good IAM Hygiene:**
   As with all identities, authentication flows, authorization permissions and implemented controls, strong hygiene- on the application server as well as the MCP server- is critical to keep every user within the proper bounds.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgekfJPPvwpcbcF0TXn6lkh0g15C804-PhKwnvERZ3m3CyqBJtSxxLYdtHeT0n8y4cTvVVX5FbUUAXEJ_pkkc9VNJcIz8KcozGkByO5brvW7nrelux0-vJHuZbvKoI1nfWQ0BWxBiXYcj6Uu7J7jiwZhla5OllOojWuaRs8NcprXeF6xp-MNohxBOaU2Os/s1600/2.png)](https://139840798.fs1.hubspotusercontent-eu1.net/hubfs/139840798/Buyers%20Guide%20%E2%80%93%20Content.pdf)

## **The Bigger Picture**

AI agents pose a unique challenge beyond mere integration. They represent a shift in how work is delegated and executed inside enterprises. Left unmanaged, they will follow the same trajectory as other hidden identities: in-app-local accounts, stale service identities, long-lived tokens, API keys, and bypass auth paths that have become identity dark matter over time. And because LLM-driven agents are optimized for efficiency, least friction and fewest steps, they will naturally gravitate to those ungoverned identities as the fastest path to success. If an orphaned local admin or an over-scoped token “just works,” the agent will use it, and reuse it.

The opportunity is to get ahead of this curve.

By treating AI agents as first-class identities from day one (discoverable, governable, and auditable), organizations can harness their potential without creating blind spots.

Enterprises that do this will not only reduce their immediate attack surface but also position themselves for the regulatory and operational expectations that are sure to follow.

In practice, most Agent-AI incidents won’t start with a zero-day. They’ll start with an identity shortcut that someone forgot to clean up, then get amplified by automation until it appears to be a systemic breach.

## **The Bottom Line**

AI agents are here. They are already changing how enterprises operate.

The challenge is not whether to use them, but how to govern them.

Safe MCP adoption requires applying the same principles that identity practitioners know well, least privilege, lifecycle management, and auditability, to a new class of non-human identities that follow this protocol.

If identity dark matter is the sum of what we can’t see or control, then unmanaged AI agents may become its fastest-growing source. The organizations that act now to bring them into the light will be the ones who can move quickly with AI without sacrificing trust, compliance, or security. That’s why
[Orchid Security](https://eu1.hubs.ly/H0qBxh00)
is building identity infrastructure to eliminate dark matter, and make Agent AI adoption safe to deploy at enterprise scale.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.