---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T12:15:15.325805+00:00'
exported_at: '2026-03-10T12:15:17.782562+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/the-zero-day-scramble-is-avoidable.html
structured_data:
  about: []
  author: ''
  description: Attack surface exposure leaves services reachable as exploits appear
    within 24–48 hours after disclosure, increasing breach risk.
  headline: 'The Zero-Day Scramble is Avoidable: A Guide to Attack Surface Reduction'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/the-zero-day-scramble-is-avoidable.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'The Zero-Day Scramble is Avoidable: A Guide to Attack Surface Reduction'
updated_at: '2026-03-10T12:15:15.325805+00:00'
url_hash: c4e08cea3359586ecf8c660fdfa11a91d3b0b99c
---

You can't control when the next critical vulnerability drops. You can control how much of your environment is exposed when it does. The problem is that most teams have more internet-facing exposure than they realise.
[Intruder's](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casr)
Head of Security digs into why this happens and how teams can manage it deliberately.

## Time-to-exploit is shrinking

The larger and less controlled your attack surface is, the more opportunities exist for exploitation. And the window to act on them is shrinking fast. For the most serious vulnerabilities, disclosure to exploitation can be as short as 24 to 48 hours.
[Zero Day Clock](https://zerodayclock.com/)
projects that time-to-exploit will be just minutes by 2028.

That's not a lot of time when you consider what has to happen before a patch is deployed: running scans, waiting for results, raising tickets, agreeing priorities, implementing, and verifying the fix. If disclosure lands out of hours, it takes even longer.

In many cases, vulnerable systems don’t need to be internet-facing in the first place. With visibility of the attack surface, teams can reduce unnecessary exposure upfront and avoid the scramble altogether when a new vulnerability drops.

## When a zero-day drops on a Saturday

[ToolShell](https://cvemon.intruder.io/cves/CVE-2025-53770?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casr)
was an unauthenticated remote code execution vulnerability in Microsoft SharePoint. If an attacker could reach it, they could run code on your server - and because SharePoint is Active Directory-connected, they'd be starting in a highly sensitive part of your environment.

This was a zero-day, meaning attackers were exploiting it before a patch was available. Microsoft disclosed on a Saturday and confirmed that Chinese state-sponsored groups had been exploiting it for up to two weeks before that. By the time most teams knew about it, opportunistic attackers were scanning for exposed instances and exploiting at scale.

Intruder’s research found thousands of publicly accessible SharePoint instances at the time of disclosure - despite the fact that SharePoint doesn't need to be internet-facing. Every one of those exposures was unnecessary - and every unpatched server was an open door.

## Why exposures get missed

So why do exposures so often get missed by security teams?

In a typical external scan, informational findings sit beneath hundreds of criticals, highs, mediums, and lows. But that information can include detections that represent real exposure risk, such as:

* An exposed SharePoint server
* A database exposed to the internet, such as MySQL or Postgres
* Other protocols, which should usually be reserved for the internal network, such as RDP and SNMP

Here’s a real example of what that looks like:

VIDEO

In vulnerability scanning terms, classifying these as informationals sometimes makes sense. If the scanner sits on the same private subnet as the targets, an exposed service might genuinely be low risk. But when that same service is exposed to the internet, it carries real risk even without a known vulnerability attached to it. Yet.

The danger is that traditional scan reports treat both cases the same way, so the real risks slip through the gaps.

## What proactive attack surface reduction actually involves

There are three key elements to making attack surface reduction work in practice.

### 1. Asset discovery: define your attack surface

Before you can reduce your attack surface, you need a clear picture of what you own and what's externally reachable. That starts with identifying shadow IT - systems your organization owns or operates but isn't currently scanning or monitoring.

Closing that gap is important, and there are three key elements we recommend having in place:

1. **Integrating with your cloud and DNS providers**
   so that when new infrastructure is created, it's automatically picked up and scanned. This is one area where defenders have a genuine advantage: you can integrate directly with your own environments, attackers can't.
2. **Using subdomain enumeration**
   to surface externally reachable hosts that aren't in your inventory. This matters especially after acquisitions, where you may be inheriting infrastructure you don't yet have visibility of.
3. **Identifying infrastructure hosted with smaller, unknown cloud providers**
   . You may have a security policy that mandates development teams only use your primary cloud provider, but you need to check that practice is being followed.

Watch a deep dive into these techniques:

VIDEO

### . Treat exposure as risk

The next step is treating attack surface exposure as a risk category in its own right.

That requires a
**detection capability**
that identifies which informational findings represent an exposure and assigns appropriate severity. An exposed SharePoint instance, for example, might reasonably be treated as a medium-risk issue.

It also means carving out space for this work in
**how you prioritize**
. If strategic efforts like attack surface reduction are always competing against urgent patching, they will always lose. That might mean setting aside time each quarter to review and reduce exposure, or assigning clear ownership so someone is accountable for it - not just when a crisis hits, but routinely.

### 3. Continuous monitoring

Attack surface reduction isn't a one-time exercise. Exposure changes constantly - a firewall rule gets edited, a new service gets deployed, a subdomain gets forgotten - and your team needs to detect those changes quickly.

Vulnerability scans take time to complete, and running full scans daily isn't usually possible.
**Daily port scanning**
is a better fit. It's lightweight, fast, and means you can detect newly exposed services as they appear. If someone edits a firewall rule and accidentally exposes Remote Desktop, you find out the day it happens - not at the next scheduled scan, which could be up to a month later.

## Fewer exposed services, fewer surprises

When unnecessary services aren't exposed in the first place, they're far less likely to be caught up in the mass exploitation that follows a critical disclosure. That means fewer surprises, less urgent scrambling, and more time to respond deliberately when new vulnerabilities emerge.

Intruder automates this process - from discovering shadow IT and monitoring for new exposures, to alerting your team the moment something changes - so your security team can stay ahead of exposure rather than reacting to it.

***If you want to see what's exposed in your environment,
[book a demo of Intruder](https://www.intruder.io/get-demo?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7Casr)
.***

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.