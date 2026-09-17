---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-17T06:19:00.181248+00:00'
exported_at: '2026-09-17T06:19:02.068473+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html
structured_data:
  about: []
  author: ''
  description: Akamai finds the top 5% of enterprise AI users interact at 12 times
    the rate of the bottom 50%, concentrating shadow AI risk.
  headline: 'The Outsized Shadow: Why 5% of AI Users Are Your Biggest Security Risk'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'The Outsized Shadow: Why 5% of AI Users Are Your Biggest Security Risk'
updated_at: '2026-09-17T06:19:00.181248+00:00'
url_hash: 6dfd38f177f2678ef10276598d941ff8a14a38be
---

Big security risks come in small packages. While enterprise security teams focus on policing the proliferation of employees using ChatGPT and Claude for quick drafting tasks, a more urgent threat is posed by a handful of AI super-adopters who are quietly hardcoding unvetted tools into critical business operations.

According to new research published by Akamai, the top 5% of enterprise power users interact with AI models at 12 times the rate of the bottom 50% of the workforce. The findings, published in
[Akamai’s](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/enterprise-ai-risk-report.pdf)
*[State of the Internet: Enterprise AI Usage Risk Report 2026](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/enterprise-ai-risk-report.pdf)*
[,](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/enterprise-ai-risk-report.pdf)
are based on real-world usage and telemetry data as well as research and threat analysis.

These AI super-adopters are creating a disproportionate security risk by expanding the use of shadow AI, increasing opportunities for data leakage, and introducing autonomous AI agents that operate within the enterprise but outside its established guardrails.

“Small groups of AI power users are casting outsized shadows across enterprise threat surfaces that are already riddled with dips and blind spots,” says Or Eshed, Vice President Enterprise Security Product &amp; Engineering at Akamai. “While security teams are focused on trying to govern all employees’ access to big frontier LLMs, the cumulative long-tail shadow of dozens of smaller AI tools used by power users arguably poses a more significant security risk.”

According to Akamai data, the average employee conversation lasts about five prompts, while the top 5% of power users routinely engage in conversations of 18 prompts or more — evidence that AI models are becoming embedded collaborators in essential business operations.

"AI is no longer just a productivity booster; it is a virtual colleague with keycard access to the company vault,” says Eshed. “Security teams need to identify which employees depend most on AI to know where risk is concentrated."

## **Enterprise Control vs. Consumer Leakage**

Nearly half of all enterprise AI conversations (47.11%) occur through personal identities rather than corporate-managed accounts, according to Akamai’s report.

The situation creates a stark contrast between housebroken AI and feral AI.

AI platforms with dedicated governance controls successfully enforce corporate identity boundaries, while personal-access accounts create significant visibility gaps for IT, security, and compliance teams.

* **Gemini Enterprise (98.15%)**
  and
  **Microsoft Copilot M365 (90.55%)**
  keep the vast majority of interactions inside corporate identity systems.
* **DeepSeek (99.8%)**
  ,
  **Microsoft Copilot Standard (63.92%)**
  ,
  **ChatGPT (61.36%)**
  , and
  **Claude (61.09%)**
  are overwhelmingly dominated by personal identity logins.

Governance becomes even more muddled when employees use corporate email addresses to register personal AI subscriptions.

"One of the most surprising findings was that 14.4% of enterprise AI conversations occurred via corporate email addresses linked to personal 'freemium' AI subscriptions rather than enterprise-managed licenses," says Eshed. "This means that even when accessed through a corporate identity, the sensitive data employees inject into prompts may be used for public model training."

But even organizations that successfully manage enterprise AI accounts often have little visibility into the growing ecosystem of niche AI tools employees install outside approved channels, the report found.

## **Long-Tail Blindness**

While security teams focus on governing ChatGPT, Claude, Copilot, and Gemini, employees are quietly adopting dozens of niche AI tools, AI-enabled SaaS applications, and personal subscriptions without IT oversight.

“As with mobile devices, employees increasingly 'bring their own AI tools — or BYOAI' to access AI through personal accounts,” says Eshed.  “That creates additional visibility gaps around how business data is stored, retained, and processed.”

Browser and IDE extensions represent another rapidly expanding blind spot. Akamai found that 17.7% of employees at midsize enterprises use at least one AI extension, compared with 9.53% at larger organizations. Nearly 75% request high or critical permissions.

Crucially, 16.31% of AI extensions contain known CVE vulnerabilities, compared to 10.80% of browser extensions overall.

“These tools are creating broad, unmanaged pathways directly into active user sessions and sensitive corporate data,” warns Eshed ”This Shadow AI landscape is not just a data privacy issue; it is the infrastructure for the next generation of automated cyberattacks.”

## **The CISO Imperative**

For security teams, this shifting landscape requires a fundamental mindset shift.

The AI problem facing CISOs is no longer whether employees are using AI. They are. The new mission is to identify where AI is operating, which teams depend on it most, and whether those systems remain inside enterprise guardrails.

The challenge is to answer those questions before adversaries do.

## **Weaponizing the AI Surface**

This expanding AI surface is also creating new attack vectors that bypass traditional controls. The Akamai report highlights a few:

* **Vibe Hacking:**
  Attackers subtly modify local instruction files (such as AI\_CONFIG.md) to covertly manipulate AI coding assistants into generating vulnerable code or executing unauthorized actions.
* **CursorJacking:**
  Rogue extensions are weaponized to silently harvest API keys, session tokens, and proprietary source code directly from local databases.
* **CometJacking:**
  Adversaries use indirect prompt injection embedded in malicious web pages to trick AI agents into exfiltrating local user files, shifting the target from the human endpoint to the AI collaborator.

## **Akamai’s CISO Checklist to Secure Enterprise AI:**

* **Establish Continuous Visibility:**
  Discover all AI applications, browser/IDE extensions, and agents across the network; inspect prompts, uploads, and responses in real time.
* **Eliminate Shadow AI:**
  Enforce corporate Single Sign-On (SSO), block unmanaged personal logins, and audit corporate email addresses tied to "freemium" subscriptions.
* **Deploy Contextual AI DLP:**
  Implement prompt-level inspection to catch unstructured data leakage—such as code snippets or internal text—that legacy pattern-matching tools miss.
* **Audit Extensions and Permissions:**
  Maintain a rigorous inventory of browser and IDE extensions, enforce strict permission boundaries, and screen add-ons for known CVEs.
* **Govern AI Agents as Identities:**
  Treat autonomous AI agents and browsers as privileged digital identities, applying least-privilege access, strict scope limits, and real-time monitoring.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.