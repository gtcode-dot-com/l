---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:10:06.444083+00:00'
exported_at: '2026-11-15T06:10:07.467578+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/microsoft-365-outage-disrupts-outlook-exchange-online-and-teams
structured_data:
  about: []
  author: ''
  description: A Microsoft 365 outage disrupted Outlook, Exchange Online and Teams.
    Microsoft is investigating server failures and has disclosed no evidence of a
    cyberattack.
  headline: Microsoft 365 Outage Disrupts Outlook, Exchange Online and Teams
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/microsoft-365-outage-disrupts-outlook-exchange-online-and-teams
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft 365 Outage Disrupts Outlook, Exchange Online and Teams
updated_at: '2026-11-15T06:10:06.444083+00:00'
url_hash: 0cddf7b800746504a5b4edf0177f6e6dc401ed31
---

**UPDATE – Microsoft 365 suffered a widespread outage Thursday, which has extended into Friday, disrupting access to business email and other cloud services across multiple regions. Microsoft initially reported that users in the Americas were having trouble connecting to Exchange Online mailboxes. It later identified potential disruption to Teams, SharePoint Online, Microsoft 365 Copilot, Defender XDR, and many other services.**

Some users of Google Workspace (formerly G Suite) also reported trouble accessing their Google-hosted email through Outlook desktop and mobile email clients.

Microsoft traced the increased load on its infrastructure to a large number of servers becoming unavailable, leaving the remaining systems to handle the traffic. The
[company said](https://status.cloud.microsoft/m365/referrer=serviceStatusRedirect)
overall traffic had not increased.

&gt; **Update: November 12 – 9:00PM ET**
&gt; – Microsoft said restarting affected servers was showing signs of improvement, though it was still monitoring their stability and had yet to confirm full recovery.
&gt;
&gt; Microsoft said a process that establishes secure connections was becoming overwhelmed, causing affected servers to stop handling requests. The company began rolling back a recent network configuration change that coincided with the start of the disruption and was monitoring whether the rollback helped.
&gt;
&gt; Advertisement. Scroll to continue reading.
&gt;
&gt; Both the Exchange Online incident (EX1550543) and the broader Microsoft 365 incident (MO1550821) remained open in its service health dashboard. Features of many Microsoft 365 services that interact with Exchange Online and email services are impacted. Elements of those services that do not depend on interaction with Exchange Online remain functional, Microsoft said.

Microsoft said a process that establishes secure connections was becoming overwhelmed, causing affected servers to stop handling requests. The company began rolling back a recent network configuration change that coincided with the start of the disruption and was monitoring whether the rollback helped. Microsoft had yet to confirm the root cause or disclose evidence of a cyberattack.

In an update just before 3 p.m. ET, Microsoft said affected servers were failing automated health checks and that it was testing a workaround that bypasses the component responsible for processing those checks. The company said it was also investigating elevated processor usage on affected servers.

## Was the Microsoft outage caused by a cyberattack?

At the original time of publishing, Microsoft was investigating what triggered the failures and disclosed no evidence of a cyberattack. In an update Friday, the company said there was no indication of a malicious attack. “At this time, we have no evidence of malicious activity associated with this incident,” the status page said. “We will continue to treat this with urgency until full mitigation, and we will share a full Post-Incident Report with root cause and defense-in-depth actions after mitigation is complete.”

The disruption came two days after Microsoft released its November Patch Tuesday updates, which
[addressed 1,094 vulnerabilities](https://www.securityweek.com/exploited-outlook-zero-day-among-1094-flaws-patched-by-microsoft/)
across its products. They included
**CVE-2026-124194**
, an Outlook spoofing flaw Microsoft says attackers have exploited. The flaw can expose a user’s authentication material if the user opens a specially crafted file in an affected Outlook client. Microsoft’s service advisories have not linked the vulnerability to the Exchange Online outage.

Microsoft is tracking the Exchange Online disruption under
**[EX1550543](https://x.com/MSFT365Status/status/2120941584220827979)**
and the broader Microsoft 365 incident under
**[MO1550821](https://x.com/MSFT365Status/status/2120948642991182117)**
in the Microsoft 365 admin center. As of just before 3 p.m. ET, both incidents were listed as service degradations.