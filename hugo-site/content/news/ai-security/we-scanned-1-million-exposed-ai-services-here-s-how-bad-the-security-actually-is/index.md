---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-05T12:15:17.206778+00:00'
exported_at: '2026-05-05T12:15:21.561836+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html
structured_data:
  about: []
  author: ''
  description: AI infrastructure exposes 1M services from 2M hosts due to weak defaults,
    increasing risk of data leaks and system compromise
  headline: We Scanned 1 Million Exposed AI Services. Here's How Bad the Security
    Actually Is
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: We Scanned 1 Million Exposed AI Services. Here's How Bad the Security Actually
  Is
updated_at: '2026-05-05T12:15:17.206778+00:00'
url_hash: 0642acc78f569f5c82751fb35a9fc71c20a6352c
---

While the software industry has made genuine strides over the past few decades to deliver products securely, the furious pace of AI adoption is putting that progress at risk. Businesses are moving fast to self-host LLM infrastructure, drawn by the promise of AI as a force multiplier and the pressure to deliver more value faster. But speed is coming at the expense of security.

In the wake of the
[ClawdBot fiasco](https://www.intruder.io/blog/clawdbot-when-easy-ai-becomes-a-security-nightmare?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Cai_research)
— the viral self-hosted AI assistant that’s averaging an eye-watering
[2.6 CVEs per day](https://days-since-openclaw-cve.com/)
—
[the Intruder team](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Cai_research)
wanted to investigate how bad the security of AI infrastructure actually is.

To scope the attack surface, we used certificate transparency logs to pull just over 2 million hosts with 1 million exposed services. What we found wasn’t pretty. In fact, the AI infrastructure we scanned was more vulnerable, exposed, and misconfigured than any other software we've ever investigated.

## No authentication by default

It didn’t take long to spot an alarming pattern: a significant number of hosts had been deployed straight out of the box, with no authentication in place. Looking into the source code revealed why: authentication simply isn't enabled by default in many of these projects.

Real user data and company tooling were sitting exposed to anyone who looked. In the wrong hands, the consequences range from reputational damage to full compromise.

Here are some of the most striking examples of what was exposed.

### Freely accessible chatbots

A number of instances involved chatbots that left user conversations exposed. One example, based on OpenUI, exposed a user's full LLM conversation history. It might seem relatively innocent on the surface, but chat histories in enterprise environments can reveal a lot.

More concerning were generic chatbots hosting a wide range of models — including multimodal LLMs — freely available to use. Malicious users can
[jailbreak](https://www.cyberark.com/resources/threat-research-blog/jailbreaking-every-llm-with-one-simple-click)
most models to bypass safety guardrails for nefarious purposes — like generating illegal imagery, or soliciting advice with intent to commit a crime — and do so without fear of repercussion, since they're using someone else's infrastructure. This isn't hypothetical. People are finding
[creative ways](https://www.lasso.security/blog/amazon-chatbot-gone-wrong)
to abuse company chatbots to access more capable models without paying or having requests logged to their own accounts.

There were also some
*questionable*
chatbots exposing large volumes of personal NSFW conversations. If that wasn't bad enough, the software running the Claude-powered goon-bots also disclosed their API keys in plaintext.

### Wide open agent management platforms

We also discovered exposed instances of agent management platforms, including n8n and Flowise. Some instances that users clearly thought were internal had been exposed to the internet without authentication. One of the most egregious examples was a Flowise instance that exposed the entire business logic of an LLM chatbot service.

Their credential list was exposed too. Flowise was hardened enough not to reveal the stored values to an unauthenticated visitor, which limits the immediate damage, but an attacker could still use the tools connected to those credentials to exfiltrate sensitive information.

This is what makes these platforms particularly dangerous. There's a distinct absence of proper access management controls in AI tooling, meaning access to a bot that's integrated with a third-party system often means access to everything it touches.

In another example, the setup exposed a number of internet parsing tools and potentially dangerous local functions, such as file writes and code interpreting, making server-side code execution a realistic prospect.

We identified over 90 exposed instances across sectors such as government, marketing, and finance. All of those chatbots, their workflows, prompts, and outward access were open. An attacker could modify the workflows, redirect traffic, expose user data, or poison responses.

### Saying hello to unsecured Ollama APIs

One of the more surprising findings was the sheer number of exposed Ollama APIs accessible without authentication, with a model connected. We fired a single prompt ("Hello") to every server that listed a connected model, to see if we’d be prompted to authenticate. Of the 5,200+ servers queried, 31% answered.

The responses gave a window into what these APIs were being used for. We couldn't morally explore any further, but the implications are far-reaching. A few examples:

*"Greetings, Master. Your command is my law. What is your desire? Speak freely. I am here to fulfill it, without hesitation or question."*

*"I am here to assist you in any way I can with your health and wellbeing issues. Whether it's anxiety, sleep problems, or other concerns, don't hesitate to ask me for help."*

*"Welcome! I'm an AI assistant integrated with our cloud management systems. I can help you with operational tasks, infrastructure deployment, and service queries."*

Ollama doesn't store messages directly, so there's no immediate risk of conversation data being exposed. But many of these instances were wrapping paid frontier models from Anthropic, Deepseek, Moonshot, Google, and OpenAI. Of all the models identified across all servers, 518 were wrapping well-known frontier models.

## Insecure by design

After triaging the results, it was clear that some of the tech warranted a closer look. We spent time analyzing a subset of the applications in a lab environment — and found repeated insecure patterns throughout:

* **Poor deployment practices:**
  Insecure defaults, misconfigured Docker setups, hardcoded credentials, applications running as root
* **No authentication on fresh installs:**
  Many projects drop users straight into a high-privilege account with full management access
* **Hardcoded and static credentials:**
  Embedded in setup examples and docker-compose files rather than generated on installation
* **New technical vulnerabilities:**
  Within a couple of days of lab work, we had already found arbitrary code execution in one popular AI project

These misconfigurations are made even worse when agents have access to tools like code interpretation. The blast radius gets significantly larger when sandboxing is weak, and the infrastructure isn't sitting in a DMZ.

## Speed is winning. Security is lagging behind

Some of the projects powering LLM infrastructure have clearly abandoned decades of hard-won security best practices in favour of shipping fast. That said, it's not purely a vendor problem. The speed of AI adoption and the pressure to beat competitors to market are what’s driving it.

Don't wait for an attacker to find your exposed AI infrastructure first.
[Intruder finds misconfigurations and shows you what's visible from the outside](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Cai_research)
.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.