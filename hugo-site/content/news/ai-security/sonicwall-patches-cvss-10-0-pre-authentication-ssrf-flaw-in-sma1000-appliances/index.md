---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T01:03:54.650915+00:00'
exported_at: '2026-10-08T01:03:55.956840+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html
structured_data:
  about: []
  author: ''
  description: SonicWall fixed four SMA1000 flaws, including a 10.0-rated SSRF reachable
    before authentication; it says none are known to be exploited.
  headline: SonicWall Patches CVSS 10.0 Pre-Authentication SSRF Flaw in SMA1000 Appliances
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SonicWall Patches CVSS 10.0 Pre-Authentication SSRF Flaw in SMA1000 Appliances
updated_at: '2026-10-08T01:03:54.650915+00:00'
url_hash: 6ad8a15b4ab56f6e845423bff847a220287519d6
---

**

Swati Khandelwal
**

Oct 07, 2026

Vulnerability / Network Security

SonicWall has released hotfixes for four flaws in its SMA1000 appliances, the gateways that give remote workers access to a company's network and applications. The most serious could allow an attacker without a login to send requests through the appliance and reach internal functions.

SonicWall rates it 10.0 on the CVSS scale and says it has no evidence that any of the four flaws is being used in attacks.

The most serious flaw, tracked as
[CVE-2026-102255](https://www.cve.org/CVERecord?id=CVE-2026-102255)
, is a server-side request forgery (SSRF) bug in WorkPlace, the portal that SMA1000 users log in to. It exists due to an unintended access path through SonicWall and can be reached before authentication.

An attacker who abuses that path could "reach internal functionality and perform unauthorized operations," SonicWall said in its
[security advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0017)
, dated October 6, without saying which functions.

All four flaws affect SMA1000 models 6210, 7210 and 8200v on these platform-hotfix versions:

* **Version 12.4.3:**
  12.4.3-03526 and older versions are affected. 12.4.3-03670 and higher versions are fixed.
* **Version 12.5.0:**
  12.5.0-02952 and older versions are affected. 12.5.0-03082 and higher versions are fixed.

The affected versions include 12.4.3-03526 and 12.5.0-02952, which SonicWall
[named on September 1](https://thehackernews.com/2026/09/attackers-exploit-two-sonicwall-sma.html)
as the fix for two flaws it reported as exploited. An appliance still on those versions needs the new hotfix.

SSL-VPN on SonicWall firewalls and the SMA 100 Series are not affected.

The hotfix is available from the MySonicWall portal, and the appliance restarts when the installation finishes. No workaround is listed.

The other three flaws can be used only after logging in. Two of them are in the Appliance Management Console (AMC), where administrators configure the appliance.

| CVE | Flaw | Where | Access needed | SonicWall CVSS score |
| --- | --- | --- | --- | --- |
| CVE-2026-102255 | Server-side request forgery (SSRF) | WorkPlace | None | 10.0 |
| CVE-2026-102256 | OS command injection that could lead to remote code execution | SMA1000 appliance, component not named | Administrator login | 7.8 |
| CVE-2026-102257 | Zip Slip: an attacker can use a specially made archive to extract files outside the intended folder, which could lead to remote code execution | AMC | Login | 7.2 |
| CVE-2026-102258 | Stored cross-site scripting (XSS) | AMC | Administrator login | 5.5 |

It is the third time this year that SonicWall has fixed a 10.0-rated SSRF flaw in WorkPlace that needs no login.

SonicWall disclosed
[CVE-2026-15409 and CVE-2026-15410](https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html)
on July 14, and CVE-2026-83548 and CVE-2026-83549 on September 1. Both times, it said it had investigated attacks exploiting the flaws: "multiple cases" in July and "a case" in September. Each pair consisted of an SSRF flaw that required no login and a second flaw that could allow a logged-in administrator to run commands on the appliance.

SonicWall's own staff found both of those pairs. SonicWall credited outside researchers for the four new flaws: Benoît Sevens of Anthropic for CVE-2026-102255 and CVE-2026-102256, and Brian Mariani of DigitalCanion SA for the other two, one of them reported through Trend Micro's Zero Day Initiative.

In the
[July attacks](https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html)
, CVE-2026-15409 allowed an attacker with no login to open a tunnel to services that respond only inside the appliance,
[according to Rapid7](https://www.rapid7.com/blog/post/etr-rapid7-mdr-team-discovers-new-sonicwall-sma1000-zero-days-being-actively-exploited-cve-2026-15409-cve-2026-15410)
. The attacker could then run commands and use CVE-2026-15410 to gain root access, which is full control of the appliance.

SonicWall has not said whether the new SSRF flaw can be combined with the other three in the same way.

In its July and September advisories, SonicWall told customers to check their appliances for indicators of compromise and, if any were found, to re-image or redeploy the appliance, change user and administrator passwords, and reset the TOTP tokens used for one-time login codes. It has given no such instruction for the four new flaws.