---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-12T23:17:27.975896+00:00'
exported_at: '2026-10-12T23:17:30.197577+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html
structured_data:
  about: []
  author: ''
  description: Personal AI agents can access work apps through OAuth grants, passwords,
    and API keys, while remaining outside managed agent consoles.
  headline: 'Bring Your Own Agent: Your Employees'' Assistants Are Already Logged
    In'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Bring Your Own Agent: Your Employees'' Assistants Are Already Logged In'
updated_at: '2026-10-12T23:17:27.975896+00:00'
url_hash: 172b933e4740eecac7c84ea5d3c422d5a7afc4cd
---

The personal AI agents rollout is going about as smoothly as expected: Amazon
[now blocks Meta's Muse](https://techrepublic.com/article/news-amazon-blocks-meta-muse)
because it doesn't identify itself as a bot while browsing; Instinct keeps
[raising privacy concerns](https://www.scworld.com/brief/instinct-ai-assistant-faces-privacy-concerns-amid-praise)
; and the horror stories from pretty much every personal AI agent keep piling up.

Regardless, the tech world is mesmerized by the capabilities and potential of these services. Less than a year after the first release of the open-source agent now called OpenClaw, the juggernauts are putting their weight behind the idea that each of us needs a personal assistant.

You know what's coming: your employees will connect their personal agents to work systems. There's no stopping that. Their agents already manage their home time, and managing their work time is the next logical step. For them, that is. Not for your security.

Given that personal agents will reach corporate systems whether approved or not, you might be wondering what the best way is to block them. If that’s your thinking, we’re here to offer you another path: enable safe usage instead, with identity as the control plane, and reap the benefits.

## **BYOD, meet BYOA(I)**

The Bring-Your-Own-Device shift is the obvious comparison, but calling this the new era of BYOD would undersell the challenges personal AI agents introduce. These aren't just devices presumed to be insecure that contain company data, but entire AIs that act on company systems in the employee’s name.

Bring-Your-Own-AI (or Bring-Your-Own-Agent) is, then, an identity challenge first and foremost. The best-case scenario is an agent wielding identities with an owner of record, limited approval, and no offboarding. You will also have agents who pretend to be employees, and agents with identities that have no easily recognizable owner.

But the main difference between the two movements is where the control point sits. BYOD gave IT a device to enroll. A personal agent is something you can't register: it lives on the vendor's computer or blends into the employee's. And it's likely in your systems today, whether you can see it or not.

## **How personal agents get in**

Whoever connects a personal AI agent to your systems today likely does this without ever filing a ticket. Instead, they connect it the way they'd connect other apps:

* **OAuth consent.**
  The agent requests access to Google Workspace, Microsoft 365, or Slack, and the employee clicks Allow. If your tenant lets users consent to third-party apps, that's the whole process.
* **A text thread.**
  Take Instinct, for example. Users text it, link their Google, Apple, or Facebook account, and it acts through the services they connect.
* **Saved passwords in the agent's browser.**
  Many of the agents can sign in to supported sites using passwords via a browser and an internal password manager. To your app, it looks like the employee is logging in.
* **API keys and personal access tokens.**
  For unofficial integrations, many agents can use API keys and personal access tokens, which require users to create long-term credentials.
* **The employee's own laptop.**
  A local agent like OpenClaw reaches whatever the machine it's installed on can see. Muse got a Mac app on September 18 that reads files, notes, calendars, and email with the user's permission, and can take optional Full Disk Access. Dots can work from the user's laptop once it's connected. The same goes for AI browsers like Atlassian's Dia, which read your open pages and connect to Slack and Gmail.

## **Meet the agents**

Less than a year into the category, we’re already starting to see sub-categories emerge in the nascent personal AI agent market. Some agents are more corporate, and others are more personal. But you’ll be hard-pressed to find one that’s truly tailored to a work environment in terms of what it does, and, more importantly, doesn’t do.

Take OpenAI’s Dots, for example. It’s as corporate as a product such as this can be. “Specialist dots” will have their own identities and credentials. OpenAI is working with Microsoft to deploy them under Agent 365, and the connectors are based on those created for ChatGPT. Even the rollout is limited to enterprise accounts and high-tier subscriptions.

xAI’s GrokBot has an R&amp;D distribution channel via Cursor. If your devs have Cursor, they might have access to GrokBot. Here, the idea is to turn the AI bot tied to the work-controlled development environment into a personal assistant, but that doesn’t make it more governed. Like its competitors, GrokBot is more than willing to sign in to tools without using a clean API via its virtual computer.

Meta’s muse is consumer-first, and currently US and Canada-only. That said, a few weeks after launch, it gained many organizational connectors, including Slack, Linear, and Vercel. It’s also, ostensibly, the fastest-growing personal AI agent in the fall of 2026.

The buzziest personal AI agent in tech circles is Instinct. It’s a personal AI agent from a small start-up that works through text apps. It can connect to pretty much any work environment. And it has a privacy policy that raised many an eyebrow. Speaking of raising, Instinct itself raised $1 billion at a $10 billion valuation, so it’s one of the best-funded underdogs ever.

Finally, we’d be remiss if we didn’t mention OpenClaw. The open-source agent that runs on the user’s own machine is adapting to a future where it’s not the only personal AI in town. It’s trying to go “multiplayer,” with several trusted users operating the same bot while adding features like session ownership.

## **Everyone is building governance. For their own deployments.**

Most of the aforementioned vendors are currently adding controls for managed deployments. So if you trust your employees to use corporate Dots, Grokbot, or Muse, there’s good news aplenty in recent announcements.

But all of these only work inside a corporate deployment. None of the truly personal AI agents will show up in the relevant admin console. This is not to say that you should necessarily block “unauthorized” agents en masse. Your employees are learning to rely on them, and there’s great productivity improvement potential.

Instead, treat the agent as an external entity. Someone else runs it, and the employee owns it. What you do have is the other end: the accounts, grants, and sessions it uses inside your systems.

For users, it’s good to have the agents run on a computer in the vendor’s cloud or on their own server. For you, it’s a headache, even if the vendor's architecture is thoughtful. Take Muse, which runs a dedicated VM with a guard called Sentinel that checks every outbound request, and tokens that the agent itself never handles. In other words, the Sentinel enforces the users’ policy rather than the employer's, and corporate session tokens end up on someone else’s computer.

Local agents running on laptops have the opposite problem. Credentials stay local, but nothing tells the agent apart from the employee.

## **Enable the agent, govern the identity**

So what’s the ideal solution? It looks something like this: employees can benefit from using their personal agent at work, but the workplace controls the reach via identities.

It means:

* **Discovering**
  the agents already connected. This is your
  [Shadow AI inventory](https://www.token.security/blog/detect-shadow-ai-enterprise?utm_source=thehackernews&amp;utm_medium=3rdparty&amp;utm_campaign=thehackernews&amp;utm_content=oct-12)
  , which you assemble based on the different ways AI agents access your systems. These can be OAuth grants to agent vendors, sign-ins from vendor cloud ranges, long-lived API keys issued to unknown clients, or EDR findings.
* **Attributing**
  each agent to a human owner.
* **Right-sizing**
  the agent’s access. A personal agent inherits everything its owner can do, and it's usually asked to do a sliver of that.
* **Retiring**
  the agent
  [when the owner leaves](https://www.token.security/blog/ai-agent-identity-lifecycle?utm_source=thehackernews&amp;utm_medium=3rdparty&amp;utm_campaign=thehackernews&amp;utm_content=oct-12)
  , including grants, tokens, and sessions that outlive the account.

Easier said than done, obviously, but some of the fundamentals are there. More will likely be added in the coming months to create the connective tissue between personal AI agents and workplaces. For example, we still need to know if whoever signs in with a username and password is an employee or their agent. Agent-to-agent communication isn’t solved yet. And the ability to compartmentalize knowledge, so that a personal agent loses it during offboarding, isn’t here yet.

Additional controls are coming, but you don’t have to wait for the vendors to catch up. Token Security already finds the personal agents connected to your systems, ties each one to its owner, trims its access, and shuts it off when the employee leaves. Identity is the control plane for AI agents and personal agents are no different.
[See it on your own environment](https://www.token.security/book-a-demo?utm_source=thehackernews&amp;utm_medium=3rdparty&amp;utm_campaign=thehackernews&amp;utm_content=oct-12)
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