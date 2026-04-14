---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T22:15:17.962043+00:00'
exported_at: '2026-04-14T22:15:20.449070+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition
structured_data:
  about: []
  author: ''
  description: Patch Tuesday, April 2026 Edition
  headline: Patch Tuesday, April 2026 Edition
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Patch Tuesday, April 2026 Edition
updated_at: '2026-04-14T22:15:17.962043+00:00'
url_hash: abd8582afcac131ddb71944ce6d6706650b3e0ab
---

**Microsoft**
today pushed software updates to fix a staggering 167 security vulnerabilities in its
**Windows**
operating systems and related software, including a
**SharePoint Server**
zero-day and a publicly disclosed weakness in
**Windows Defender**
dubbed “
**BlueHammer**
.” Separately,
**Google Chrome**
fixed its fourth zero-day of 2026, and an emergency update for
**Adobe Reader**
nixes an actively exploited flaw that can lead to remote code execution.

![A picture of a windows laptop in its updating stage, saying do not turn off the computer. ](https://krebsonsecurity.com/wp-content/uploads/2021/07/windupate.png)

Redmond warns that attackers are already targeting
[CVE-2026-32201](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-32201)
, a vulnerability in Microsoft SharePoint Server that allows attackers to spoof trusted content or interfaces over a network.

**Mike Walters**
, president and co-founder of
**Action1**
, said CVE-2026-32201 can be used to deceive employees, partners, or customers by presenting falsified information within trusted SharePoint environments.

“This CVE can enable phishing attacks, unauthorized data manipulation, or social engineering campaigns that lead to further compromise,” Walters said. “The presence of active exploitation significantly increases organizational risk.”

This flaw drops alongside a separate SQL Server remote code execution vulnerability (
[CVE-2026-33120](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33120)
), notes
**Ryan Braunstein**
, manager of Security and IT at
**Automox**
.

“One bug allows an attacker to get into your SQL instance from the network,” Braundstein said. “The other lets someone already inside promote themselves to full control.”

Microsoft also addressed BlueHammer (
[CVE-2026-33825](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-33825)
), a privilege escalation bug in Windows Defender. According to BleepingComputer, the researcher who discovered the flaw
[published exploit code for it](https://www.bleepingcomputer.com/news/security/disgruntled-researcher-leaks-bluehammer-windows-zero-day-exploit/)
after notifying Microsoft and growing exasperated with their response.
**Will Dormann**
, senior principal vulnerability analyst at
**Tharros**
, says he
[confirmed](https://infosec.exchange/@wdormann/116404516592597593)
that the public BlueHammer exploit code no longer works after installing today’s patches.

**Satnam Narang**
, senior staff research engineer at
**Tenable**
, said April marks the second-biggest Patch Tuesday ever for Microsoft. Narang also said there are indications that a zero-day flaw Adobe patched in an emergency update on April 11 —
[CVE-2026-34621](https://helpx.adobe.com/security/products/acrobat/apsb26-43.html)
— has seen active exploitation since at least November 2025.

**Adam Barnett**
, lead software engineer at
**Rapid7**
, called the patch total from Microsoft today “a new record in that category” because it includes nearly 60 browser vulnerabilities. Barnett said it might be tempting to imagine that this sudden spike was tied to the buzz around the announcement a week ago today of
[Project Glasswing](https://www.anthropic.com/glasswing)
— a much-hyped but still unreleased new AI capability from Anthropic that is reportedly quite good at finding bugs in a vast array of software.

But he notes that
**Microsoft Edge**
is based on the Chromium engine, and the Chromium maintainers acknowledge a wide range of researchers for the vulnerabilities which Microsoft republished last Friday.

“A safe conclusion is that this increase in volume is driven by ever-expanding AI capabilities,” Barnett said. “We should expect to see further increases in vulnerability reporting volume as the impact of AI models extend further, both in terms of capability and availability.”

Finally, no matter what browser you use to surf the web, it’s important to completely close out and restart the browser periodically. This is really easy to put off (especially if you have a bajillion tabs open at any time) but it’s the only way to ensure that any available updates get installed. For example, a Google Chrome update released earlier this month fixed 21 security holes, including the high-severity zero-day flaw
[CVE-2026-5281](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5281)
.

For a clickable, per-patch breakdown, check out the
**SANS Internet Storm Center**
[Patch Tuesday roundup](https://isc.sans.edu/forums/diary/Microsoft%20Patch%20Tuesday%20April%202026./32898/)
. Running into problems applying any of these updates? Leave a note about it in the comments below and there’s a decent chance someone here will pipe in with a solution.