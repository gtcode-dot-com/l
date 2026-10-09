---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T20:56:15.755406+00:00'
exported_at: '2026-05-14T20:56:18.221535+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/why-agentic-ai-is-securitys-next-blind.html
structured_data:
  about: []
  author: ''
  description: Agentic AI expands enterprise attack surfaces through broad permissions
    and unreviewed deployments, increasing lateral movement risks.
  headline: Why Agentic AI Is Security's Next Blind Spot
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/why-agentic-ai-is-securitys-next-blind.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Why Agentic AI Is Security's Next Blind Spot
updated_at: '2026-05-14T20:56:15.755406+00:00'
url_hash: 0d53d116bbf22e56e58c4db0c5573b9f67c34cc9
---

Agentic AI is already running in production environments across many organizations today. It is executing tasks, consuming data, and taking actions — most likely without meaningful involvement from the security team. The industry conversation has largely framed this as a question of policy: allow it, restrict it, or monitor it? However, that framing misses the point.

The more urgent question is whether security professionals actually understand what they are dealing with. In most organizations, they don't right now. And that gap is compounding by the week.

## **You cannot secure what you do not understand**

The foundational principle of information security has not changed: genuine fluency in a technology must come before you can meaningfully defend it.

Think about firewalls. You cannot configure one well without understanding networking. When cloud computing arrived, organizations that skipped the foundational work ended up with environments they could not reason about — tools purchased, policies written, and still no real control. We have cloud security as its own discipline today precisely because the technology demanded that practitioners develop deep familiarity with it before security could follow.

The same dynamic is playing out with AI, at a faster pace and with higher stakes.

The practical consequence of being behind on agentic AI goes beyond technical exposure. Security teams that cannot speak the language of AI engineering — that cannot challenge design decisions, propose workable controls, or ask informed questions — get bypassed. Business units move forward without them, not out of bad faith, but because a security team that cannot engage substantively with the technology is not a useful partner for decisions about it. This has played out with every major technology shift over the past two to three decades. AI will be no different.

The starting point is engagement. Try building an agent. Experiment with the tools your developers are already using. This hands-on familiarity is where real understanding begins, and real understanding is what makes everything else possible.

## **Three categories of agents, three categories of risk**

The agentic AI landscape is broad, and the risk profile varies significantly across it. Three categories are worth understanding distinctly.

The first is
**general-purpose coding and productivity agents**
— tools like Claude Code and GitHub Copilot. These are already embedded in developer and engineering workflows across your organization. Whether they have been formally approved or not, they are being used. What data they can access, how they interact with codebases, and what actions they can take is baseline security knowledge at this point.

The second is
**vendor-built agents powered by the Model Context Protocol**
, or MCP. MCP is the integration layer that allows agents to connect to external services and act on their behalf. Nearly every major vendor either has an MCP server in production or is actively building one. In practice, this means an agent managing a user's calendar, email, or internal ticketing system can receive input from those channels and act on it. A malicious calendar invite carrying hidden instructions in the event description is a real attack vector — the agent reads it, interprets the embedded prompt, and executes. This is a live attack surface that requires deliberate configuration and security review.

The third category is
**custom agents built by individual users**
, and this is where the dynamic gets particularly interesting. For years, a real barrier existed between security practitioners who understood risk and the code that ran in their environments. Most security professionals are not programmers. Building custom tooling required development skills that were not widely distributed across security teams.

That barrier is gone.

With agentic AI, anyone in the organization can build functional tools — automations, workflows, agents with real system access — without writing traditional code. For security teams, this is genuinely valuable. Incident investigation, forensic triage, threat hunting workflows — these can be accelerated when practitioners can build the tools they actually need. But that same capability extends to every other team. Marketing, finance, operations — everyone can build agents now. Many will. Most of those agents will not go through a security review before they go live. This is a supply chain problem in a different form.

## **The cost of arriving late**

When security teams lag behind on a major technology shift, the pattern is consistent.

First, the rest of the organization moves forward without security input. Developers deploy, business units adopt, and security is consulted as a formality — or not at all. Second, the exposure compounds. The more powerful the agents an organization deploys, the more access those agents require. Broad permissions are what make agents useful: access to calendars, communication platforms, file systems, code repositories, internal APIs. That access is also what makes the blast radius significant when something goes wrong.

An agent with access to both a terminal and an email inbox can be manipulated through either channel to act in the other. That is a lateral movement path an attacker will look for. Reasoning about it requires understanding how the agent was built — the kind of understanding that only comes from genuine engagement with the technology.

## **The skills that matter right now**

Building competency in agentic AI security requires two distinct layers of knowledge.

The first is
**understanding how AI applications are architected**
— from a practitioner's perspective, not a data scientist's. What are the components of an AI application? How do agents consume inputs, chain tools together, and produce outputs? What does a session with an MCP-connected agent actually look like from an access control standpoint? This is the foundation that makes everything else actionable.

The second layer is
**currency**
. The tooling and threat landscape around AI is moving fast. Vendors are building security controls for AI systems, though most are still maturing. Open-source frameworks are emerging. OWASP and others are publishing threat taxonomies that evolve week to week. Once the foundational layer is in place, staying current becomes the ongoing discipline — knowing which tools are worth evaluating, which frameworks are gaining traction, and what questions to ask when vendors come in with solutions.

That second point matters more than it might seem. Security teams are already being approached by vendors selling AI security products. Without foundational knowledge of how these applications are built, those conversations are almost impossible to navigate well. You cannot distinguish a well-designed control from a marketing wrapper if you don't understand what you're trying to control.

## **Configuration as a security control**

Many agentic AI deployments carry risk because they were stood up without security-conscious configuration — not because the underlying tools are fundamentally broken.

Take a self-hosted AI assistant connected to a communication channel like Telegram, which can be common. without proper controls, the agent could respond to anyone who messages it. That is a wide-open entry point. A simple configuration change — pairing the agent with a single trusted account — closes most of that exposure. One decision, made early, with a meaningful security outcome.

The broader principle is scope. An agent built to manage your calendar should not have access to your terminal. An agent processing incoming requests should not have write access to your code repository. Scoping agents to their intended function limits the blast radius and reduces the attack surface available for exploitation.

The tension is real: powerful agents need broad access to be useful. That is the trade-off organizations will push back on. Finding the right balance requires security involvement early in the design process — before the architecture is set and before the permissions are already in place.

## **Getting ahead of it at SANSFIRE 2026**

The organizations building genuine AI security fluency now will be positioned to shape how these systems are deployed. Those who arrive late will find themselves, once again, applying controls to an architecture that was already decided without them.

This July, I will be teaching
[SEC545: GenAI and LLM Application Security](https://www.sans.org/cyber-security-courses/genai-llm-application-security-5day?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_SF26_May_OA_545&utm_campaign=SANSFIRE_2026)
at SANSFIRE 2026. The course covers how AI applications are actually built, how agentic systems work in practice, the real attack surfaces security teams need to understand, and the tools and controls available to address them — including hands-on work with techniques like model scanning to detect compromised models before they run in your environment. For practitioners who want to engage with AI systems from a foundation of real understanding, this is where to start.

> **[Register for SANSFIRE 2026 here.](https://www.sans.org/cyber-security-training-events/sansfire-2026?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_SF26_May_OA_EP&utm_campaign=SANSFIRE_2026)**

**Note:**
*This article has been expertly written and contributed by
[Ahmed Abugharbia,](https://www.sans.org/profiles/ahmed-abugharbia?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_SF26_May_OA_AA&utm_campaign=SANSFIRE_2026)
SANS Certified Instructor.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.