---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-12T12:03:12.800616+00:00'
exported_at: '2025-12-12T12:03:16.010900+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2025/11/the-cloudflare-outage-may-be-a-security-roadmap
structured_data:
  about: []
  author: ''
  description: The Cloudflare Outage May Be a Security Roadmap
  headline: The Cloudflare Outage May Be a Security Roadmap
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2025/11/the-cloudflare-outage-may-be-a-security-roadmap
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: The Cloudflare Outage May Be a Security Roadmap
updated_at: '2025-12-12T12:03:12.800616+00:00'
url_hash: ce8757c363c47e0a9d77dacd503093b761565b8e
---

An intermittent outage at
**Cloudflare**
on Tuesday briefly knocked many of the Internet’s top destinations offline. Some affected Cloudflare customers were able to pivot away from the platform temporarily so that visitors could still access their websites. But security experts say doing so may have also triggered an impromptu network penetration test for organizations that have come to rely on Cloudflare to block many types of abusive and malicious traffic.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/cfoutage.png)

At around 6:30 EST/11:30 UTC on Nov. 18, Cloudflare’s status page acknowledged the company was experiencing “an internal service degradation.” After several hours of Cloudflare services coming back up and failing again, many websites behind Cloudflare found they could not migrate away from using the company’s services because the Cloudflare portal was unreachable and/or because they also were getting their domain name system (DNS) services from Cloudflare.

However, some customers did manage to pivot their domains away from Cloudflare during the outage. And many of those organizations probably need to take a closer look at their web application firewall (WAF) logs during that time, said
**Aaron Turner**
, a faculty member at
**IANS Research**
.

Turner said Cloudflare’s WAF does a good job filtering out malicious traffic that matches any one of
[the top ten types of application-layer attacks](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
, including credential stuffing, cross-site scripting, SQL injection, bot attacks and API abuse. But he said this outage might be a good opportunity for Cloudflare customers to better understand how their own app and website defenses may be failing without Cloudflare’s help.

“Your developers could have been lazy in the past for SQL injection because Cloudflare stopped that stuff at the edge,” Turner said. “Maybe you didn’t have the best security QA [quality assurance] for certain things because Cloudflare was the control layer to compensate for that.”

Turner said one company he’s working with saw a huge increase in log volume and they are still trying to figure out what was “legit malicious” versus just noise.

“It looks like there was about an eight hour window when several high-profile sites decided to bypass Cloudflare for the sake of availability,” Turner said. “Many companies have essentially relied on Cloudflare for the
[OWASP Top Ten](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
[web application vulnerabilities] and a whole range of bot blocking. How much badness could have happened in that window? Any organization that made that decision needs to look closely at any exposed infrastructure to see if they have someone persisting after they’ve switched back to Cloudflare protections.”

Turner said some cybercrime groups likely noticed when an online merchant they normally stalk stopped using Cloudflare’s services during the outage.

“Let’s say you were an attacker, trying to grind your way into a target, but you felt that Cloudflare was in the way in the past,” he said. “Then you see through DNS changes that the target has eliminated Cloudflare from their web stack due to the outage. You’re now going to launch a whole bunch of new attacks because the protective layer is no longer in place.”

**Nicole Scott**
, senior product marketing manager at the McLean, Va. based
**Replica Cyber**
, called yesterday’s outage “a free tabletop exercise, whether you meant to run one or not.”

“That few-hour window was a live stress test of how your organization routes around its own control plane and shadow IT blossoms under the sunlamp of time pressure,” Scott said in
[a post](https://www.linkedin.com/feed/update/urn:li:activity:7396624084958146560/)
on LinkedIn. “Yes, look at the traffic that hit you while protections were weakened. But also look hard at the behavior inside your org.”

Scott said organizations seeking security insights from the Cloudflare outage should ask themselves:

1. What was turned off or bypassed (WAF, bot protections, geo blocks), and for how long?

2. What emergency DNS or routing changes were made, and who approved them?

3. Did people shift work to personal devices, home Wi-Fi, or unsanctioned Software-as-a-Service providers to get around the outage?

4. Did anyone stand up new services, tunnels, or vendor accounts “just for now”?

5. Is there a plan to unwind those changes, or are they now permanent workarounds?

6. For the next incident, what’s the intentional fallback plan, instead of decentralized improvisation?

In
[a postmortem](https://blog.cloudflare.com/18-november-2025-outage/)
published Tuesday evening, Cloudflare said the disruption was not caused, directly or indirectly, by a cyberattack or malicious activity of any kind.

“Instead, it was triggered by a change to one of our database systems’ permissions which caused the database to output multiple entries into a ‘feature file’ used by our Bot Management system,” Cloudflare CEO
**Matthew Prince**
wrote. “That feature file, in turn, doubled in size. The larger-than-expected feature file was then propagated to all the machines that make up our network.”

Cloudflare estimates that roughly 20 percent of websites use its services, and with much of the modern web relying heavily on a handful of other cloud providers including
**AWS**
and
**Azure**
, even a brief outage at one of these platforms can create a single point of failure for many organizations.

**Martin Greenfield**
, CEO at the IT consultancy
**Quod Orbis**
, said Tuesday’s outage was another reminder that many organizations may be putting too many of their eggs in one basket.

“There are several practical and overdue fixes,” Greenfield advised. “Split your estate. Spread WAF and DDoS protection across multiple zones. Use multi-vendor DNS. Segment applications so a single provider outage doesn’t cascade. And continuously monitor controls to detect single-vendor dependency.”