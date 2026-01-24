---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-24T10:15:12.576905+00:00'
exported_at: '2026-01-24T10:15:15.082633+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/who-approved-this-agent-rethinking.html
structured_data:
  about: []
  author: ''
  description: AI agents break traditional IAM by enabling delegated access, authorization
    bypass, and high-risk ownerless organizational automation.
  headline: Who Approved This Agent? Rethinking Access, Accountability, and Risk in
    the Age of AI Agents
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/who-approved-this-agent-rethinking.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Who Approved This Agent? Rethinking Access, Accountability, and Risk in the
  Age of AI Agents
updated_at: '2026-01-24T10:15:12.576905+00:00'
url_hash: 5c30163b6b83712b42e17824e3ca06a66f5adb8f
---

AI agents are accelerating how work gets done. They schedule meetings, access data, trigger workflows, write code, and take action in real time, pushing productivity beyond human speed across the enterprise.

Then comes the moment every security team eventually hits:

*“Wait… who approved this?”*

Unlike users or applications, AI agents are often deployed quickly, shared broadly, and granted wide access permissions, making ownership, approval, and accountability difficult to trace. What was once a straightforward question is now surprisingly hard to answer.

## AI Agents Break Traditional Access Models

AI agents are not just another type of user. They fundamentally differ from both humans and traditional service accounts, and those differences are what break existing access and approval models.

Human access is built around clear intent. Permissions are tied to a role, reviewed periodically, and constrained by time and context. Service accounts, while non-human, are typically purpose-built, narrowly scoped, and tied to a specific application or function.

AI agents are different. They operate with delegated authority and can act on behalf of multiple users or teams without requiring ongoing human involvement. Once authorized, they are autonomous, persistent, and often act across systems, moving between various systems and data sources to complete tasks end-to-end.

In this model, delegated access doesn’t just automate user actions, it expands them. Human users are constrained by the permissions they are explicitly granted, but AI agents are often given broader, more powerful access to operate effectively. As a result, the agent can perform actions that the user themselves was never authorized to take. Once that access exists, the agent can act - even if the user never meant to perform the action, or wasn’t aware it was possible, the agent can still execute it. As a result, the agent can create exposure - sometimes accidentally, sometimes implicitly, but always legitimately from a technical standpoint.

This is how access drift occurs. Agents quietly accumulate permissions as their scope expands. Integrations are added, roles change, teams come and go, but the agent’s access remains. They become a powerful intermediary with broad, long-lived permissions and often with no clear owner.

It’s no wonder existing IAM assumptions break down. IAM assumes a clear identity, a defined owner, static roles, and periodic reviews that map to human behavior. AI agents don’t follow those patterns. They don’t fit neatly into user or service account categories, they operate continuously, and their effective access is defined by how they are used, not how they were originally approved. Without rethinking these assumptions, IAM becomes blind to the real risk AI agents introduce.

## The Three Types of AI Agents in the Enterprise

Not all AI agents carry the same risk in enterprise environments. Risk varies based on who owns the agent, how broadly it’s used, and what access it has, resulting in distinct categories with very different security, accountability, and blast-radius implications:

### Personal Agents (User-Owned)

Personal agents are
[AI assistants](https://wing.security/ai-code-assistants/)
used by individual employees to help with day-to-day tasks. They draft content, summarize information, schedule meetings, or assist with coding, always in the context of a single user.

These agents typically operate within the permissions of the user who owns them. Their access is inherited, not expanded. If the user loses access, the agent does too. Because ownership is clear and scope is limited, the blast radius is relatively small. Risk is tied directly to the individual user, making personal agents the easiest to understand, govern, and remediate.

### Third-Party Agents (Vendor-Owned)

Third-party agents are embedded into SaaS and AI platforms, provided by vendors as part of their product. Examples include AI features embedded into CRM systems, collaboration tools, or security platforms.

These agents are governed through vendor controls, contracts, and shared responsibility models. While customers may have limited visibility into how they work internally, accountability is clearly defined: the vendor owns the agent.

The primary concern here is the
[AI supply-chain risk](https://wing.security/use-cases/ai-supply-chain-risks/)
: trusting that the vendor secures its agents appropriately. But from an enterprise perspective, ownership, approval paths, and responsibility are usually well understood.

### Organizational Agents (Shared and Often Ownerless)

Organizational agents are deployed internally and shared across teams, workflows, and use cases. They automate processes, integrate systems, and act on behalf of multiple users. To be effective, these agents are often granted broad, persistent permissions that exceed any single user’s access.

This is where risk concentrates. Organizational agents frequently have no clear owner, no single approver, and no defined lifecycle. When something goes wrong, it’s unclear who is responsible or even who fully understands what the agent can do.

As a result, organizational agents represent the highest risk and the largest blast radius, not because they are malicious, but because they operate at scale without clear accountability.

## The Agentic Authorization Bypass Problem

As we explained in our article,
[agents creating authorization bypass paths](https://thehackernews.com/2026/01/ai-agents-are-becoming-privilege.html)
, AI agents don’t just execute tasks, they act as access intermediaries. Instead of users interacting directly with systems, agents operate on their behalf, using their own credentials, tokens, and integrations. This shifts where authorization decisions actually happen.

When agents operate on behalf of individual users, they can provide the user access and capabilities beyond the user’s approved permissions. A user who cannot directly access certain data or perform specific actions may still trigger an agent that can. The agent becomes a proxy, enabling actions the user could never execute on their own.

These actions are technically authorized - the agent has valid access. However, they are contextually unsafe. Traditional access controls don’t trigger any alert because the credentials are legitimate. This is the core of the agentic authorization bypass: access is granted correctly, but used in ways security models were never designed to handle.

## Rethinking Risk: What Needs to Change

Securing AI agents requires a fundamental shift in how risk is defined and managed. Agents can no longer be treated as extensions of users or as background automation processes. They must be treated as sensitive, potentially high-risk entities with their own identities, permissions, and risk profiles.

This starts with
[clear ownership and accountability](https://wing.security/wings-ai-security-platform/#Operational-Inventory)
. Every agent must have a defined owner responsible for its purpose, scope of access, and ongoing review. Without ownership, approval is meaningless and risk remains unmanaged.

Critically, organizations must also map how users interact with agents. It is not enough to understand what an agent can access; security teams need visibility into which users can invoke an agent, under what conditions, and with what effective permissions. Without this user–agent connection map, agents can silently become authorization bypass paths, enabling users to indirectly perform actions they are not permitted to execute directly.

Finally, organizations must map agent access, integrations, and data paths across systems. Only by correlating user → agent → system → action can teams accurately assess blast radius, detect misuse, and reliably investigate suspicious activity when something goes wrong.

## The Cost of Uncontrolled Organizational AI Agents

Uncontrolled organizational AI agents turn productivity gains into systemic risk. Shared across teams and granted broad, persistent access, these agents operate without clear ownership or accountability. Over time, they can be used for new tasks, create new execution paths, and their actions become harder to trace or contain. When something goes wrong, there is no clear owner to respond, remediate, or even understand the full blast radius. Without visibility, ownership, and access controls, organizational AI agents become one of the most dangerous, and least governed elements in the enterprise security landscape.

To learn more visit
<https://wing.security/>

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.