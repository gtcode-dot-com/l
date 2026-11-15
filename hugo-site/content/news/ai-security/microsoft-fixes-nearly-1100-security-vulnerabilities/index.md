---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:10:06.154808+00:00'
exported_at: '2026-11-15T06:10:07.470473+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities
structured_data:
  about: []
  author: ''
  description: Microsoft Fixes Nearly 1,100 Security Vulnerabilities
  headline: Microsoft Fixes Nearly 1,100 Security Vulnerabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Fixes Nearly 1,100 Security Vulnerabilities
updated_at: '2026-11-15T06:10:06.154808+00:00'
url_hash: bda5de5f5ee664c9c7aeed33eec8a4464a84e69a
---

**Microsoft**
did another four-digit patch drop today, releasing updates to fix almost 1,100 security vulnerabilities in its
**Windows**
operating systems and supported software. This month’s Patch Tuesday addresses 63 critical flaws — including a zero-day in
**Microsoft Outlook**
— and comes amid important security updates from other software makers, including
**Adobe**
,
**Apple**
,
**Google**
and
**Mozilla**
.

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/ss-orangemencomputer.png)

Image: Shutterstock.com. Diorama by @zepp1969.

November’s patch release from Redmond tackles 1,093 vulnerabilities, fixing 63 “critical” flaws that can be exploited to seize control over a Windows system with little or no help from users. Nearly half of those critical bugs are remote code execution vulnerabilities. Overall, 535 of the flaws addressed this month allow an attacker to elevate their privileges on a vulnerable device.

This latest round of updates means Microsoft has shipped more than 5,100 security patches so far this year, a staggering number considering that a year ago Microsoft was averaging around 100 patches per month. Microsoft credits advances in artificial intelligence for helping to find (and fix) such a large volume of security bugs in recent months. Last month, Microsoft pushed more than 1,400 fixes.

According to Redmond, just one of the flaws is already seeing active exploitation:
[CVE-2026-124194](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-124194)
, a spoofing bug in Outlook. The advisory for CVE-2026-124194 says it affects
**Microsoft 365 Apps for Enterprise**
and editions of
**Microsoft Office**
.

Several other major software makers pushed security updates this week to fix critical weaknesses in their products. Apple on Monday released out-of-cycle security updates to fix at least nine vulnerabilities in
**iOS/iPadOS**
,
**macOS**
,
**watchOS**
and
**visionOS**
. Among the weaknesses
[reportedly fixed](https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html?is=1ef7934f6635b02395adcab09a0c1b24bf0ea745b648bfe87189de8aadc7300b)
in Apple’s release include an
**iMessage**
flaw that could let a remote attacker join a group chat and receive its messages; the updates also fix a separate iMessage flaw that could let someone added to a group access messages sent before they joined.

**Lee Neely**
, an instructor at the
**SANS Institute**
, noted that Apple backported the fix to iOS 18.

“I take notice when Apple releases fixes to more than two versions,” Neely wrote in a SANS newsletter today. “You really need to get to version 27.2.1 of their OSes and push folks who are holding onto devices which cannot run the current version. The best plan often involves setting an upgrade date for old hardware. Run through all your Apple devices and make sure everything is up to date, don’t assume the fixes went out automatically.”

Google this week released
[Chrome
*version 157.0.8103.50*](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html)
, which resolves nine security holes, including
[CVE-2026-125350](https://www.cve.org/CVERecord?id=CVE-2026-125350)
, the sixth zero-day vulnerability this year for Chrome (this bug also is being patched in Chromium-based browsers like Edge). The latest Chrome version follows its November 3 release, which fixed 213 vulnerabilities. A new version of
**Mozilla Firefox**
out today (
*Firefox 160*
) resolves almost 100 CVEs, about half of them high severity.

Adobe today released patches for
[at least 110 vulnerabilities](https://www.adobe.com/trust/security/bulletins-and-advisories.html)
across a range of products, with nearly half of the flaws rated high severity. Adobe said there is no evidence any of the security holes it addressed this month are being actively exploited.

**Chris Goettl**
, vice president of product management at
**Ivanti**
, said it’s easy for security teams at large enterprises to feel overwhelmed by the volume and criticality of patches from Microsoft lately. But he notes that while some 95,000 vulnerabilities have been assigned CVEs this year across all vendors, only 217 have so far this year been added to the Known Exploited Vulnerabilities (KEV) list maintained by the U.S. Cybersecurity and Infrastructure Security Agency (CISA).

“Roughly four in ten of this year’s exploited vulnerabilities sit in operating systems, endpoint software, browsers, and server platforms, which a continuous patch strategy can close quickly,” Goettl said.”The rest calls for exposure management alongside patching, especially the 44% that sit in edge devices and IT management or remote access tools, the internet-facing systems that hold privileged access. Teams that can quickly identify those assets, confirm exposure and act on confirmed exploitation can focus on the small slice of vulnerabilities attackers are actively using, while the rest stays on the normal patch cadence.”

Please don’t neglect to back up any important data if you haven’t recently; generally speaking, this is a task best accomplished
*before*
applying operating system updates. As ever, if you experience any issues installing this month’s bundle of love from Microsoft, please drop a comment about it in the space below.