---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:32:27.820432+00:00'
exported_at: '2026-11-15T07:32:29.228284+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/silentair-hackers-intercept-calls-sms-from-inside-mobile-networks
structured_data:
  about: []
  author: ''
  description: Enea details SilentAir's interception of calls and SMS through compromised
    mobile networks and possible links to Chinese hackers.
  headline: SilentAir Hackers Intercept Calls, SMS From Inside Mobile Networks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/silentair-hackers-intercept-calls-sms-from-inside-mobile-networks
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SilentAir Hackers Intercept Calls, SMS From Inside Mobile Networks
updated_at: '2026-11-15T07:32:27.820432+00:00'
url_hash: ea2ec047b09c8875d90d42159238beefb30c39c5
---

**Telecom software and cybersecurity company Enea has detailed the activity of a previously unknown threat actor that intercepts phone calls and text messages through compromised mobile operator infrastructure, with Taiwan as its main target.**

The company tracks the group as
[SilentAir](https://www.enea.com/insights/the-enemy-within-tracking-liminal-panda-and-silentair-through-mobile-networks/)
and assesses with high confidence that it’s a new state-level actor.

Enea’s researchers also believe, with low confidence, that SilentAir’s activity is aligned with China-nexus operations. Their reasons include the hackers’ interest in Taiwan, the absence of Chinese targets, and attack timing consistent with a workday in China’s time zone.

SilentAir launches its signaling attacks, mostly over SS7 and sometimes over Diameter, from network nodes it has hijacked at mobile operators. The attacks route a target’s incoming calls and SMS messages through the compromised node and harvest subscriber details.

The hackers can also track a target’s location, but this makes up only a small part of their activity. They send silent SMS messages, which don’t appear on the recipient’s phone, possibly to check whether earlier interception attempts succeeded.

Enea has monitored the attacks since early 2025, and further digging revealed suspicious activity from before that.

Advertisement. Scroll to continue reading.

The hijacked nodes belong to operators in at least six Asian countries. Besides Taiwan, the group has targeted a dozen other countries and territories, occasionally going after people in East Africa, Central Asia, the Middle East and Europe. High-profile political and government figures were among those targeted.

The report also covers 2026 activity from Liminal Panda, a group that CrowdStrike linked, with low confidence, to China-nexus operations. Enea says it’s the only actor known to actively exploit the IPX, the interconnect network that mobile operators use to exchange traffic.

Starting in the first quarter of 2026, Enea spotted and blocked Liminal Panda’s GTPDoor backdoor at several of its mobile operator customers. In total, it caught several hundred attempts to covertly reach command-and-control servers.

Enea says it has seen potential infections at between five and ten operators. It estimates that the total could reach several dozen, particularly in Asia, Africa and Latin America.

According to Enea, SilentAir and Liminal Panda could be connected, although the evidence isn’t strong enough to link them.

**Related**
:
[China-Linked Hackers Exploit PHP2Shell to Root Firewalls](https://www.securityweek.com/china-linked-hackers-exploit-php2shell-to-root-firewalls/)

**Related**
:
[China APT Uses AI Pentest Tool Artex in ConnectWise Attacks](https://www.securityweek.com/china-apt-uses-ai-pentest-tool-artex-in-connectwise-attacks/)

**Related**
:
[China’s Top Cybersecurity Firms Hit by Mounting Military Procurement Bans](https://www.securityweek.com/chinas-top-cybersecurity-firms-hit-by-mounting-military-procurement-bans/)