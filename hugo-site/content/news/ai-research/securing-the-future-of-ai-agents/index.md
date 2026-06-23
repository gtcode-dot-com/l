---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-23T04:30:58.461342+00:00'
exported_at: '2026-06-23T04:31:00.899758+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/securing-the-future-of-ai-agents
structured_data:
  about: []
  author: ''
  description: 'Discover our AI Control Roadmap: a defense-in-depth system to securely
    manage advanced, potentially misaligned AI agents.'
  headline: Securing the future of AI agents
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/securing-the-future-of-ai-agents
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Securing the future of AI agents
updated_at: '2026-06-23T04:30:58.461342+00:00'
url_hash: 367ca70b57b816d927d391560975326982ad229b
---

How weâre securing internal systems against increasingly capable and imperfectly aligned AI

AI agents are transforming our relationship with technology. By autonomously executing complex tasks â from cyber defence to scientific discovery and product development â these systems are unlocking a new era of productivity. In the U.S alone, AI agents could create $2.9
[trillion in economic value](https://www.mckinsey.com/mgi/our-research/agents-robots-and-us-skill-partnerships-in-the-age-of-ai#/)
by 2030.

As these agents become more capable, they also require more sophisticated safeguards. Thatâs why we developed our
[AI Control Roadmap](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf)
: a framework for building and managing the advanced AI we deploy within Google. This âdefense-in-depthâ approach, which could serve as a model for the wider industry, goes beyond traditional model alignment, adding a crucial layer of system-level security that provides assurance even if alignment is imperfect.

## Understanding AI Control

Our approach to security starts with a strong foundation, incorporating traditional safeguards like sandboxing, endpoint security, and prompt injection resistance. On top of this, the AI Control Roadmap uses model alignment, i.e. training AI to be inherently safe and helpful, as a primary defense. It provides an additional layer of security by treating internal agents as potentially misaligned, providing assurance even if alignment is imperfect.

Think of it like a driving instructor with dual controls. The instructor trusts the student but stays ready to take the wheel or hit the brakes if a mistake occurs. Similarly, our AI control system grants AI agents permissions based on their verified behavior, allowing us to build trust through controlled, incremental access.

Our roadmap is built on a simple but cautious assumption: what if a highly capable AI agent isnât aligned with our goals and acts in unexpected ways? To address this, our plan focuses on three key areas.

First, following best practices in cybersecurity, we have developed a novel threat-modelling framework for AI. The roadmap treats untrusted AI agents as potential âinsider threatsâ â similar to the way a company would treat a potential rogue employee who already has access to the office. By building on the industry-standard
[MITRE ATT&amp;CK](https://attack.mitre.org/)
framework, a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations, we break down potential attacks into smaller tactics and techniques. This allows us to methodically track risks, spot bad behavior before it causes damage and safely run drills to test if our defenses actually hold up.

Second, we develop a plan to deploy AI control mitigations to address these risks.

* Identifying the problem (Detection): Monitoring is the backbone of AI control. We use other, trusted AI systems as "supervisors" to constantly review a working agent's reasoning, actions and plans to see if it is going off track.
* Managing the problem (Prevention and Response): If a supervisor sees the agent trying to do something harmful, it can step in to block the action before damage occurs.

Finally, to ensure our systems are functional, we constantly measure performance across three critical metrics: coverage (the fraction of traffic monitored), recall (the fraction of misaligned behaviors caught), and time-to-response.

## Scaling security as AI gets smarter

As AI models continue to advance, our defenses must also strengthen in tandem. In our AI Control Roadmap, we map security protocols to measurable milestones in AI capabilities on two critical fronts:

* **Ability to evade detection:**
  Today, we monitor a model's visible chain-of-thought. However, as models learn to hide their reasoning â either through
  *oversight awareness*
  (knowing they are being monitored) or
  *opaque reasoning*
  (reasoning without using visible text) â simply reading their verbalized reasoning will not be enough. We will need to analyze their behavior and potentially inspect the modelâs inner workings.
* **Ability for potential harm:**
  For low-risk and reversible actions, we can rely on reviewing transcripts with a delay and remediating issues quickly after they occur (asynchronous response). For particularly high-risk actions, such as major cyber attacks, we must shift to real-time prevention, blocking harmful actions before they can be executed (synchronous response). In other words, our response strategy must scale with the severity of the threat.