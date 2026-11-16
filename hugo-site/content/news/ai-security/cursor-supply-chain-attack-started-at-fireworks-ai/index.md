---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T18:21:52.585419+00:00'
exported_at: '2026-11-16T18:21:53.781101+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks
structured_data:
  about: []
  author: ''
  description: 'Cursor supply chain attack: malicious Claude Code extension copies
    pushed after credentials were compromised through Fireworks.'
  headline: Cursor Supply Chain Attack Started at Fireworks AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cursor Supply Chain Attack Started at Fireworks AI
updated_at: '2026-11-16T18:21:52.585419+00:00'
url_hash: 17e52c3eda319d05cbf43663e2ea199350d928a6
---

**Credentials compromised in the hack of AI inference platform Fireworks AI allowed attackers to steal more secrets and push malicious Claude Code extension copies, Cursor says.**

The
[supply chain attack](https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/)
was discovered on October 29 and resulted in threat actors making two modified versions of the anthropic.claude-code extension (2.1.312 and 2.1.313) available through the Cursor VS Code Extension Marketplace for roughly 11 hours.

Anthropic was never hacked, and all the malicious activity occurred in Cursor’s environment, the company explains.

Instead, Cursor was hit after Fireworks was
[hacked twice](https://fireworks.ai/security/bulletins/october-2026-security-incident-update)
in October. First, internal Fireworks credentials were used to access Fireworks stored secrets and account and billing information. Then, a third-party cloud provider was compromised, Fireworks development machines were reached, and customer data was stolen.

A Cursor access key issued to Fireworks was compromised in one of these incidents and the attacker used it to copy data from a read-only storage bucket, including unredacted credentials that opened the door to SaaS tools used by Cursor.

“From these tools they accessed select archived non-production Cursor source code repositories (some containing business contact information), limited customer support data and email conversations, product usage metrics and contact details, summaries of some coding agent conversations, and some credentials users had sent to the Cursor support team,”
[Cursor explains](https://cursor.com/blog/security-incident-update)
.

Advertisement. Scroll to continue reading.

While Cursor blocked the attacker’s access immediately after discovering the unauthorized activity, the attacker used secrets exfiltrated from the company’s internal systems to place “malicious, unauthorized copies of Anthropic’s Claude Code extension directly on the cache used to serve the Cursor VS Code extension marketplace.”

The malware was never present in the Open VSX marketplace source, but was served to the users who requested the cached versions of the extension. According to Cursor, at most 5,000 users were affected.

“If customers installed or updated to the tampered version Anthropic.claude-code 2.1.312 or 2.1.313 from the Cursor VS Code extension marketplace during the exposure window, we ask customers to follow the steps in our
[security notice](https://cursor.com/blog/claude-code-extension-security-notice)
. Uninstalling the extension alone may not be enough,” Cursor notes.

The company considers the incident contained, as it has not seen attacker activity in its environment since November 1.

[Notion](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/)
and
[Uber](https://www.securityweek.com/uber-data-breach-impacts-150000-people/)
also disclosed data breaches stemming from the Fireworks compromise.

**Related:**
[Maersk Confirms Data Theft Amid $5 Million Extortion Attempt](https://www.securityweek.com/maersk-confirms-data-theft-amid-5-million-extortion-attempt/)

**Related:**
[Revolve Puts Data Breach Victim Count at 1.5 Million](https://www.securityweek.com/revolve-puts-data-breach-victim-count-at-1-5-million/)

**Related:**
[Iris Plaza Breach May Have Exposed Data of 7.7 Million Customers](https://www.securityweek.com/iris-plaza-breach-may-have-exposed-data-of-7-7-million-customers/)

**Related:**
[Over 3 Million People Hit by Frontline Education Data Breach](https://www.securityweek.com/3-million-people-hit-by-frontline-education-data-breach/)