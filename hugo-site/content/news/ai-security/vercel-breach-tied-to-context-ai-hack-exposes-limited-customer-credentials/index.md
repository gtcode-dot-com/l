---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-20T06:15:14.570993+00:00'
exported_at: '2026-04-20T06:15:16.778699+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html
structured_data:
  about: []
  author: ''
  description: Context.ai breach enabled Google Workspace takeover at Vercel, exposing
    limited customer credentials and prompting $2M data sale claim.
  headline: Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Vercel Breach Tied to Context AI Hack Exposes Limited Customer Credentials
updated_at: '2026-04-20T06:15:14.570993+00:00'
url_hash: 8dd64d4317308660da164f21df3e08b0ec65813c
---

**

Ravie Lakshmanan
**

Apr 20, 2026

Cloud Security / Data Breach

Web infrastructure provider Vercel has disclosed a security breach that allows bad actors to gain unauthorized access to "certain" internal Vercel systems.

The incident stemmed from the compromise of Context.ai, a third-party artificial intelligence (AI) tool, that was used by an employee at the company.

"The attacker used that access to take over the employee's Vercel Google Workspace account, which enabled them to gain access to some Vercel environments and environment variables that were not marked as 'sensitive,'" the company
[said](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)
in a bulletin.

Vercel said environment variables marked as "sensitive" are stored in an encrypted manner that prevents them from being read, and that there is currently no evidence suggesting that those values were accessed by the attacker.

It described the threat actor behind the incident as "sophisticated" based on their "operational velocity and detailed understanding of Vercel's systems." The company also said it's working with Google-owned Mandiant and other cybersecurity firms, as well as notifying law enforcement and engaging with Context.ai to better understand the full scope of the breach.

A "limited subset" of customers is said to have had their credentials compromised, with Vercel reaching out to them directly and urging them to rotate their credentials with immediate effect. The company is continuing to investigate what data was exfiltrated, and plans to contact customers if further evidence of compromise is discovered.

Vercel is also advising Google Workspace administrators and Google account owners to check for the following application OAuth application:

> 110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com

As additional mitigations, the following best practices have been recommended -

While Vercel has yet to share details about which of its systems were broken into, how many customers were affected, and who may be behind it, a threat actor using the ShinyHunters persona has
[claimed](https://x.com/DiffeKey/status/2045813085408051670)
responsibility for the hack, selling the stolen data for an asking price of $2 million.

"We've deployed extensive protection measures and monitoring. We've analyzed our supply chain, ensuring Next.js, Turbopack, and our many open source projects remain safe for our community," Vercel CEO Guillermo Rauch
[said](https://x.com/rauchg/status/2045995362499076169)
in a post on X.

"In response to this, and to aid in the improvement of all of our customers’ security postures, we've already rolled out new capabilities in the dashboard, including an overview page of environment variables, and a better user interface for sensitive environment variable creation and management."