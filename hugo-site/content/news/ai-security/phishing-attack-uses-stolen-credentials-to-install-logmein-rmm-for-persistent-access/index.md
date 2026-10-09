---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-23T12:15:12.683372+00:00'
exported_at: '2026-01-23T12:15:14.987674+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/phishing-attack-uses-stolen-credentials.html
structured_data:
  about: []
  author: ''
  description: Researchers uncovered a two-stage phishing attack stealing email logins
    to install LogMeIn Resolve RMM for persistent, hidden Windows access.
  headline: Phishing Attack Uses Stolen Credentials to Install LogMeIn RMM for Persistent
    Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/phishing-attack-uses-stolen-credentials.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Phishing Attack Uses Stolen Credentials to Install LogMeIn RMM for Persistent
  Access
updated_at: '2026-01-23T12:15:12.683372+00:00'
url_hash: 661216906585437d4f1919f6deaebdddf8d9c345
---

**

Ravie Lakshmanan
**

Jan 23, 2026

Email Security / Endpoint Security

Cybersecurity researchers have disclosed details of a new dual-vector campaign that leverages stolen credentials to deploy legitimate Remote Monitoring and Management (RMM) software for persistent remote access to compromised hosts.

"Instead of deploying custom viruses, attackers are bypassing security perimeters by weaponizing the necessary IT tools that administrators trust," KnowBe4 Threat Labs researchers Jeewan Singh Jalal, Prabhakaran Ravichandhiran, and Anand Bodke
[said](https://blog.knowbe4.com/the-skeleton-key-how-attackers-weaponize-trusted-rmm-tools-for-backdoor-access)
. "By stealing a 'skeleton key' to the system, they turn legitimate Remote Monitoring and Management (RMM) software into a persistent backdoor."

The attack unfolds in two distinct waves, where the threat actors leverage fake invitation notifications to steal victim credentials, and then leverage those pilfered credentials to deploy RMM tools to establish persistent access.

The bogus emails are disguised as an invitation from a legitimate platform called Greenvelope, and aim to trick recipients into clicking on a phishing URL that's designed to harvest their Microsoft Outlook, Yahoo!, AOL.com login information. Once this information is obtained, the attack moves to the next phase.

Specifically, this involves the threat actor registering with LogMeIn using the compromised email to generate RMM access tokens, which are then deployed in a follow-on attack through an executable named "GreenVelopeCard.exe" to establish persistent remote access to victim systems.

The binary, signed with a valid certificate, contains a JSON configuration that acts as a conduit to silently install LogMeIn Resolve (formerly GoTo Resolve) and connect to an attacker-controlled URL without the victim's knowledge.

With the RMM tool now deployed, the threat actors weaponize the remote access to alter its service settings so that it runs with unrestricted access on Windows. The attack also establishes hidden scheduled tasks to automatically launch the RMM program even if it's manually terminated by the user.

To counter the threat, it's advised that organizations monitor for unauthorized RMM installations and usage patterns.