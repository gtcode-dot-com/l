---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:14:34.929592+00:00'
exported_at: '2026-05-14T21:14:38.119662+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition
structured_data:
  about: []
  author: ''
  description: Patch Tuesday, May 2026 Edition
  headline: Patch Tuesday, May 2026 Edition
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Patch Tuesday, May 2026 Edition
updated_at: '2026-05-14T21:14:34.929592+00:00'
url_hash: 324bf43b6fbd041f4ba698d0159a90b1091dbea0
---

Artificial intelligence platforms may be just as susceptible to social engineering as human beings, but they are proving remarkably good at finding security vulnerabilities in human-made computer code. That reality is on full display this month with some of the more widely-used software makers — including
**Apple**
,
**Google**
,
**Microsoft**
,
**Mozilla**
and
**Oracle**
— fixing near record volumes of security bugs, and/or quickening the tempo of their patch releases.

As it does on the second Tuesday of every month, Microsoft today released software updates to address at least 118 security vulnerabilities in its various
**Windows**
operating systems and other products. Remarkably, this is the first Patch Tuesday in nearly two years that Microsoft is not shipping any fixes to deal with emergency zero-day flaws that are already being exploited. Nor have any of the flaws fixed today been previously disclosed (potentially giving attackers a heads up in how to exploit the weakness).

Sixteen of the vulnerabilities earned Microsoft’s most-dire “critical” label, meaning malware or miscreants could abuse these bugs to seize remote control over a vulnerable Windows device with little or no help from the user.
**Rapid7**
has done much of the heavy lifting in identifying some of the more concerning critical weaknesses this month, including:

* [CVE-2026-41089](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41089)
  : A critical stack-based buffer overflow in Windows Netlogon that offers an attacker SYSTEM privileges on the domain controller. No privileges or user interaction are required, and attack complexity is low. Patches are available for all versions of Windows Server from 2012 onwards.
* [CVE-2026-41096](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41096)
  : A critical RCE in the Windows DNS client implementation worthy of attention despite Microsoft assessing exploitation as less likely.
* [CVE-2026-41103](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41103)
  : A critical elevation of privilege vulnerability that allows an unauthorized attacker to impersonate an existing user by presenting forged credentials, thus bypassing Entra ID. Microsoft expects that exploitation is more likely.

May’s Patch Tuesday is a welcome respite from April, which saw Microsoft
[fix a near-record 167 security flaws](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/)
. Microsoft was among a few dozen tech giants given access to a “
**Project Glasswing**
,” a much-hyped AI capability developed by
**Anthropic**
that appears quite effective at unearthing security vulnerabilities in code.

Apple, another early participant in Project Glasswing, typically fixes an average of 20 vulnerabilities each time it ships a security update for iOS devices, said
**Chris Goettl**
, vice president of product management at
**Ivanti**
. On May 11, Apple shipped updates to address at least 52 vulnerabilities and backported the changes all the way to iPhone 6s and iOS 15.

Last month, Mozilla released
**Firefox 150**
, which resolved
[a whopping 271 vulnerabilities](https://arstechnica.com/ai/2026/04/mozilla-anthropics-mythos-found-271-zero-day-vulnerabilities-in-firefox-150/)
that were reportedly discovered during the Glasswing evaluation.

“Since Firefox 150.0.0 released, they have been on a more aggressive weekly cadence for security updates including the release of Firefox 150.0.3 on May Patch Tuesday resolving between three to five CVEs in each release,” Goettl said.

The software giant Oracle likewise recently increased its patch pace in response to their work with Glasswing. In its most recent quarterly patch update, Oracle addressed at least 450 flaws, including
[more than 300 fixes for remotely exploitable, unauthenticated flaws](https://www.securityweek.com/oracle-patches-450-vulnerabilities-with-april-2026-cpu/)
. But at the end of April, Oracle announced it was switching to a monthly update cycle for critical security issues.

On May 8, Google started rolling out updates to its Chrome browser that
[fixed an astonishing 127 security flaws](https://www.forbes.com/sites/daveywinder/2026/05/08/critical-new-google-security-update-127-chrome-security-vulnerabilities-confirmed/)
(up from just 30 the previous month). Chrome automagically downloads available security updates, but installing them requires fully restarting the browser.

If you encounter any weirdness applying the updates from Microsoft or any other vendor mentioned here, feel free to sound off in the comments below. Meantime, if you haven’t backed up your data and/or drive lately, doing that
*before*
updating is generally sound advice. For a more granular look at the Microsoft updates released today, checkout
[this inventory](https://isc.sans.edu/forums/diary/Microsoft%20May%202026%20Patch%20Tuesday/32980/)
by the
**SANS Internet Storm Center**
.