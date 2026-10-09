---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-05T04:00:20.972796+00:00'
exported_at: '2026-10-05T04:00:23.368347+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/zero-trust-for-ai-agents-starts-with.html
structured_data:
  about: []
  author: ''
  description: METR says an attacker bypassed authentication on an agentic app, obtained
    an API key, and used $600,000 in tokens over three weeks.
  headline: Zero Trust for AI Agents Starts With Fixing Zero Visibility
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/zero-trust-for-ai-agents-starts-with.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Zero Trust for AI Agents Starts With Fixing Zero Visibility
updated_at: '2026-10-05T04:00:20.972796+00:00'
url_hash: 4e66adccc3e470f43e5d5f1a2cd562bb2084a48a
---

Before an AI agent gets access to your environment, you should be able to answer a few basic questions. Who owns it? What is it allowed to do? What can it reach, and how will you know when it does something outside its assigned task?

These are familiar questions in security architecture. Agents make them harder to answer because they can select tools, act on external content, and, in some deployments, delegate work to other agents. An attacker who hijacks an agent’s intent may be able to turn its legitimate access against you. The agent may still present valid credentials and call an expected API while acting outside its assigned task.

[Research from Veeam](https://www.veeam.com/company/press-release/emea-organizations-facing-a-shadow-agent-crisis-as-boardroom-anxiety-over-personal-liability-grows-veeam-research-finds.html)
illustrates the visibility gap: 70% of organizations surveyed reported AI workflows interacting with sensitive corporate data without full oversight, and 67% reported that employees were creating autonomous workflows IT could not fully track. These workflows can acquire access to business systems before security teams know they exist.

Zero Trust principles can support an AI governance program, but only in the right order. "You cannot govern what you cannot see" is the underlying principle right at the top of the SANS cheat sheet,
[Zero Trust for AI Agents: The Security Checklist](https://www.sans.org/posters/zero-trust-ai-agents-security-checklist?utm_medium=Sponsored_Content&amp;utm_source=Hacker_News&amp;utm_rdetail=NA&amp;utm_goal=Orders&amp;utm_type=Live_Training_Events&amp;utm_content=THN_CDI26_Sep_OA_AIChecklist&amp;utm_campaign=SANS_CDI_2026)
. The checklist starts with inventory for a reason: every agent needs a named owner, a defined purpose, and an explicit scope of authority. In practice, organizations may deploy a policy enforcement point or an authorization layer without establishing those basics. Those controls can still restrict access, but how do you decide which actions to authorize if you haven’t defined what the agent is supposed to do? Establish that scope before granting access and keep discovering unmanaged agents while enforcing restrictions on what they can reach.

Here are three visibility challenges to look for, with implications for you to consider when you “Think Red” like an attacker, and the solutions you can employ when you “Act Blue” as an informed defender.

## **Challenge One: Agent Use Is a New Form of Shadow IT**

With any new technology, adoption moves first, and governance follows later, if it follows at all. Once security teams notice this gap, the first instinct is often prevention, which can include blocking unapproved tools, cutting off access, or just shutting down anything unfamiliar. Budget and attention accumulate for these processes first, but blocking things before anyone has a picture of what already exists risks shutting down legitimate use along with the shadow deployments. While the problem of Shadow IT has been acknowledged and addressed in other technologies for a long time, we are still crawling when it comes to doing this for AI.

**Think Red:**
When the agent is effectively invisible to you, an attacker doesn't need to breach much of anything to gain a foothold. A recent example in the news was
[an incident at METR](https://thehackernews.com/2026/09/attackers-steal-metr-api-key-and.html)
, the nonprofit known recently for their evaluation of the Hugging Face incident. An attacker discovered an employee’s personal EC2 instance running a vibe-coded agentic app, where a fail-open vulnerability had silently disabled authentication, and prompted the agent to hand over its model provider API key. Over three weeks, the intruder used the equivalent of $600,000 in tokens, as there was no spending limit on the API key. METR’s internal dashboard simply didn’t show rate-limited requests to all users, and token volume alone was not enough to raise any flags.

**Act Blue:**
Cloud technology has experienced these same growing pains, and we can look there for the road to visibility. Apply familiar cloud controls to agent deployments, including usage monitoring, credential management, and removal of unused resources. Treat AI spending and API-key issuance as discovery signals and involve finance and procurement. Spending alone will miss free credits, local models, and capabilities bundled into existing subscriptions. Provide an approved path for legitimate use while restricting unauthorized access. Discovery and enforcement should happen together, with each agent tied to a named owner, a defined purpose, and scoped permissions.

## **Challenge Two: No Single Camera Can Take the Full Picture**

Even once an organization commits to discovery, there is no single vantage point that gives you the whole population. Agents live across the network, the endpoint, the browser, and inside SaaS hosted elsewhere, and any one lens leaves large blind spots. Without TLS decryption, network sensors cannot inspect encrypted prompts or tool-call contents, but connection metadata can still provide useful leads. Endpoint tools may identify browser extensions and local agent runtimes, while SaaS and identity logs provide evidence of activity outside the endpoint. Each source offers partial visibility; understanding the workflow requires correlating them.

**Think Red:**
Imagine a marketing analyst installing a browser tool that summarizes customer records and drafts outbound email. Endpoint tools may identify the extension without revealing everything it does inside connected SaaS applications. Network monitoring sees only encrypted traffic to a domain that also hosts a dozen sanctioned SaaS products. The tool, and whatever attacker can compromise it, could hold access to a CRM full of sensitive data without anyone else realizing the tool exists.

**Act Blue:**
Recovering visibility means giving up on any single source and instead correlating a variety of sources that each give you a section of visibility. While traffic can camouflage easily or hide in local MCP servers or CLI tools, metadata can tell you something is talking to a model provider, through DNS/SNI, JA4 fingerprints, and egress-proxy logs. Layer your network visibility with endpoint telemetry about processes, API keys sitting in environment variables, or local agent runtimes. Also look for telemetry at the browser level, about extensions, in-page copilots, and enterprise-browser logs, as well as identity and SaaS logs like OAuth grants, API-key issuance, provider admin consoles. When you work to correlate all these signals, they can give you an inventory.

An LLM gateway such as LiteLLM can centralize both visibility and governance by acting as the policy enforcement point the cheat sheet calls for, but it only governs agents already pointed at it, which loops the problem back to our missing inventory. A gateway can control agents you know about, but it doesn't discover the ones you don't.

## **Challenge Three: Audits Need to Keep Pace With What You’re Auditing**

Traditional audits alone cannot maintain visibility into short-lived agents. Record creation, access changes, delegation, and termination continuously, and use audits to verify that those controls work. When it takes seconds for agents to get deployed and cloned, by the time a review cycle closes, the inventory it produced is already inaccurate. Continuous monitoring is the most obvious answer, but removing a human from that loop carries its own risk.

**Think Red:**
If an organization audits periodically, an attacker could take advantage of this by telling a compromised agent to spawn short-lived clones to complete a task, if the runtime permits those agents to inherit or reuse the parent’s credentials. The clones exist just long enough to exfiltrate data or carry out other malicious activities, but they are gone before the regular review would ever see them.

**Act Blue:**
Automated monitoring can help, but another agent reviewing the same manipulated evidence may reach the same wrong conclusion. Verify actions against independent identity, tool, and service logs, and keep authorization controls outside the agent’s control. Keep in mind, though, if automated systems are watching automated systems, who is accountable? Auditability still needs a named person who is responsible for the outcome, whatever the automation reports. You can mitigate some risk ahead of time with quality gates.

Test how you would contain a compromised agent: revoke its credentials, terminate delegated workers, and stop pending actions. Disabling model access alone may leave other parts of the workflow running. Preserve the evidence and verify that access has actually ended.

Agent identity is part of this prerequisite, and it’s what makes your monitoring thresholds meaningful. To echo the cheat sheet again, you cannot threshold what you cannot attribute. Douglas McKee and I raised some concepts that can be helpful here in
[The Monday Brief](https://themondaybrief.substack.com/p/prompt-injection-is-an-architectural)
on Substack: "Agent tool access must be modeled as a distinct identity and policy enforcement problem, not as an extension of the user who deployed the agent. Give every agent its own identity, bind permissions to the active task, constrain what data may leave the environment, and place an authorization layer between the model and connected services." Logging needs the same shift, from logging prompts alone to recording the tool calls and actions an agent takes.

## **Where This Puts Your Program**

Visibility gives you the context to define and validate an agent’s access. Build the inventory while enforcing restrictions, connect each agent to an owner and a defined task, and correlate its identity with the actions it takes. The full Zero Trust for AI Agents security checklist brings together inventory and governance, architecture and enforcement, and detection and response. These capabilities need to improve together as deployments grow.

For a deeper walkthrough of these controls, join me for
[SEC530: Defensible Security Architecture and Engineering, Implementing Zero Trust for the Hybrid Enterprise](https://www.sans.org/cyber-security-courses/defensible-security-architecture-and-engineering?utm_medium=Sponsored_Content&amp;utm_source=Hacker_News&amp;utm_rdetail=NA&amp;utm_goal=Orders&amp;utm_type=Live_Training_Events&amp;utm_content=THN_CDI26_Sep_OA_530CP&amp;utm_campaign=SANS_CDI_2026)
, this December at
[SANS Cyber Defense Initiative 2026](https://www.sans.org/cyber-security-training-events/cyber-defense-initiative-2026?utm_medium=Sponsored_Content&amp;utm_source=Hacker_News&amp;utm_rdetail=NA&amp;utm_goal=Orders&amp;utm_type=Live_Training_Events&amp;utm_content=THN_CDI26_Sep_OA_EP&amp;utm_campaign=SANS_CDI_2026)
.

**Note:**
*This article has been expertly written and contributed by Ismael Valenzuela.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.