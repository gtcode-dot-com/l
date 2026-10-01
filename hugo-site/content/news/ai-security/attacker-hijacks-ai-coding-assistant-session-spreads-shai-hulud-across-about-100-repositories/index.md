---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-01T19:24:30.096865+00:00'
exported_at: '2026-10-01T19:24:31.346654+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html
structured_data:
  about: []
  author: ''
  description: Mandiant says an attacker hijacked an active AI coding session, stole
    GitHub OAuth tokens, and spread Shai-Hulud across about 100 repositories.
  headline: Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across
    About 100 Repositories
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About
  100 Repositories
updated_at: '2026-10-01T19:24:30.096865+00:00'
url_hash: c14e0be31c83f2cd607c0a2eda80814dc2f3395f
---

**

Swati Khandelwal
**

Sep 16, 2026

Artificial Intelligence / Software Security

Mandiant says an attacker hijacked an active AI coding-assistant session at an unnamed software-as-a-service provider and later spread
[Shai-Hulud](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html)
across about 100 internal code repositories.

Before the repository spread, the assistant recommended software that the attacker had poisoned, and the recommendation was accepted. The worm stole repository secrets and source code for the company's products.

The case appears in
[Mandiant's September 2026 report](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)
. The public case study does not say when the intrusion happened or how the attacker took over the active coding-assistant session.

### How the Attack Unfolded

After the recommendation was accepted, the attacker used the developer's active session to install an infostealer through a poisoned PyPI package. The attacker also stole GitHub OAuth tokens.

The attacker then deployed the self-spreading Shai-Hulud worm across approximately 100 internal code repositories.

The attacker also poisoned a package in the company's official namespace. Another employee pulled the compromised version, causing a second infection.

Mandiant had already documented attackers using AI in real attacks. In a
[March 2026 report](https://cloud.google.com/security/resources/ai-risk-and-resilience)
, it said attackers had moved during 2025 from using generative AI mainly to speed up work to using large language models in malware and active attacks.

### How Defenders Can Protect AI-Assisted Development

For this case, Mandiant recommends three controls for AI-assisted development:

* Check AI-recommended third-party dependencies against cryptographic checksums and approved allowlists.
* Keep raw API keys, long-lived OAuth tokens, and other secrets out of direct reach of extensions.
* Route dependency traffic through controlled internal repositories.

Recent Shai-Hulud-family attacks have also targeted developer tools and credentials. In August, a
[Keyv-linked npm worm](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html)
poisoned hundreds of packages and planted hooks for Claude Code and Visual Studio Code, while a later analysis found a Shai-Hulud variant scanning
[469 locations for credentials](https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html)
across developer systems, CI/CD tools, cloud configurations, and AI tool files.

These were separate campaigns, and the available evidence does not link them to the unnamed Mandiant intrusion.