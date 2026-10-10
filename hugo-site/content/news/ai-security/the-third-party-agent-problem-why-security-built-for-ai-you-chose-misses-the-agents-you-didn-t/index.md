---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-10T21:29:39.657471+00:00'
exported_at: '2026-10-10T21:29:41.272410+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/the-third-party-agent-problem-why.html
structured_data:
  about: []
  author: ''
  description: Nearly 1,000 third-party products embedding AI sit outside SSO in studied
    environments, limiting default visibility for identity systems.
  headline: 'The Third-Party Agent Problem: Why Security Built for AI You Chose Misses
    the Agents You Didn''t'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/the-third-party-agent-problem-why.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'The Third-Party Agent Problem: Why Security Built for AI You Chose Misses
  the Agents You Didn''t'
updated_at: '2026-10-10T21:29:39.657471+00:00'
url_hash: 4f95732c4969a2353a318bf6c6580f7079301dd7
---

In environments studied for the
[2026 State of Agent Security Report](https://hubs.ly/Q04zg1dw0)
, roughly 1,280 third-party products now embed AI. About 282 of them sit behind single sign-on. The other thousand are invisible to identity infrastructure by default, not because anyone hid them, but because an identity stack can only govern what authenticates through it, and most agents never do.

That gap is the clearest expression of a shift the security industry is only starting to name. For several years, "AI security" solved a first-party problem: the company decided to use AI, procured licenses, deployed a model behind a gateway, and security pointed controls at the thing the business had chosen. Agents do not arrive that way. They arrive inside software the enterprise already runs, and they arrive without a decision.

## **Why the decision point mattered more than the controls**

Every control in the first-party toolkit assumes a moment exists: model scanning assumes a model was selected, prompt inspection assumes a gateway was deployed, an acceptable-use policy assumes there was an adoption to accept. That moment gave security a review, a surface to instrument, and an owner to name.

Agents skip the moment. Salesforce's Slack Code, launched in August 2026, lets a user tag a coding agent into any conversation; the agent reads the shared context, writes the code, and opens the pull request. The announcement promises agents "inherit Slack's built-in security model, permissions, and admin controls from day one, without any additional IT lift." Read by a security team, that sentence describes an autonomous actor with reach into GitHub and production infrastructure whose governance is a chat tool's channel membership. There was nothing to instrument, because nothing was adopted.

## **Three launch vectors, one destination**

Security leaders tend to sort agents into two buckets: bought and built. There is a third, and it is the largest. Inherited agents ship inside existing platforms via product updates. Configured agents are an enterprise's own prompts and logic running on someone else's runtime, model, and connectors. Built agents are open frameworks on infrastructure the enterprise owns end to end. The first two account for the overwhelming majority of adoption and are growing exponentially as every major application becomes an agent platform. The third is the smallest and slowest growing, and it is the only one with a repo to scan and a build to gate.

The destination is the same regardless of origin. An agent born in a CRM ends up reading a data warehouse and writing to a ticketing system. An agent assembled on a cloud platform ends up holding tokens into Salesforce, Slack, and Drive. The enterprise application layer is where they all execute, and it has no fixed edges.

## **Four questions that work on any agent**

Every agent has two parts: the model that reasons and the scaffolding around it that turns a model into an actor, deciding what it is wired to, what it may call, and when it acts. Almost none of the risk lives in the model. It lives in the scaffolding and the ecosystem the scaffolding sits inside. Four questions cover it, and none of them ask what the model would do on its own.

|  |  |
| --- | --- |
| **Area to review** | **What it looks like in practice** |
| **Identity** | Is the agent registered anywhere? Does a named human raise a hand when asked "whose is this?" Or does it silently run as whoever built it? |
| **Permissions** | What is it allowed to do, and is that more than it needs? Whose OAuth scopes and roles did it inherit at creation, and did anyone decide that on purpose? |
| **Connectivity** | What can it reach, directly and transitively, through the products, grants, data stores, and other agents it touches? This is the blast-radius question, and it is rarely answerable from the agent's own configuration screen. |
| **Activity** | What is it actually doing, and is that normal for what it is? Judged by behavior, not by the description in its prompt. |

The Connectivity row is where agent security separates from everything the market already sells. A vendor questionnaire, a prompt filter, and a model scanner all evaluate an agent in isolation. Reach is a property of the environment.

## **The buyers with the most influence have already moved**

Patrick Opet, global CISO of JPMorgan Chase, told the software industry in 2025 that the third-party supply chain had become a systemic risk, citing incidents serious enough that the bank had to isolate compromised suppliers in an open letter to the industry. He has since applied the same scrutiny to agents: ideally, an agent gets an identity but no entitlements by default, and IT confirms who it acts on behalf of before it touches anything outside that boundary. When a buyer of that size names agents as a supply-chain risk, the question shows up in everyone else's security questionnaires within a few quarters.

Regulators are moving on the same assumption. The EU AI Act's obligations phasing in through 2026 presume an enterprise can inventory its AI systems, name their owners, and evidence oversight. An organization that cannot enumerate its agents cannot comply.

## **What a standing capability looks like**

The approach that keeps up with fifty agents through spreadsheets and quarterly reviews collapses at five hundred, and five hundred is one product update away from five thousand. What replaces it is a live answer, continuously refreshed, to what is operating, what each agent inherited, what it can reach directly and through chains, what it is doing, and how all of that changed since yesterday.

Some platforms are now built around exactly that map. One leading example is Reco, whose Reco Graph connects every human and non-human identity, application, permission, and agent action into a single live view so that reach, not configuration, is the unit of analysis.

The industry spent a decade building security for the AI enterprises decided to use. The agents they did not decide on are now the larger population. The six-chapter series this analysis draws on,
[Into the Expanse](https://www.reco.ai/agent-ecosystem-security?utm_source=hackernews)
, covers where they come from, how to govern them, how attackers use them, where runtime belongs, and what to fund first.

Learn more about Reco's agent discovery at
[reco.ai/platform](https://www.reco.ai/platform?utm_source=hackernews)
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