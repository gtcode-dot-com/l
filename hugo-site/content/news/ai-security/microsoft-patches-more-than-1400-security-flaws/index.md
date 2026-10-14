---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-14T23:34:43.539987+00:00'
exported_at: '2026-10-14T23:34:45.451543+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws
structured_data:
  about: []
  author: ''
  description: Microsoft Patches More Than 1,400 Security Flaws
  headline: Microsoft Patches More Than 1,400 Security Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches More Than 1,400 Security Flaws
updated_at: '2026-10-14T23:34:43.539987+00:00'
url_hash: 2ad84ab401bee4f9161dcd6d8a2e588dab7b4f8d
---

**Microsoft**
today issued updates to fix more than 1,400 security vulnerabilities in its
**Windows**
operating systems and other software. Today’s epic patch batch dwarfs September’s record of nearly 1,000 fixes, which was already about ten times the normal monthly patch load from Redmond.

![](https://krebsonsecurity.com/wp-content/uploads/2020/08/windowsec.png)

Just one of the weaknesses patched this week is considered a “zero day,” or already exploited in the wild.
[CVE-2026-96951](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-96951)
is a security feature bypass in the
**Windows Shell**
that affects Windows 10 and 11 systems, as well as some Server versions.

Windows 10 users might be wondering if they can still expect security updates after this month. Microsoft had been slated to stop shipping updates for Windows 10 systems in October 2025, but ended up adding another year of free updates after considerable pushback. A few months ago, Microsoft
[quietly extended that support](https://www.windowscentral.com/microsoft/windows-10/microsoft-quietly-extends-windows-10s-extra-security-updates-program-for-free-users-can-now-stay-on-windows-10-until-october-2027-securely)
for another year (until October 2027).

At least 78 of the flaws fixed this month are rated “critical,” meaning they could be exploited with little or no action by the user, and most of those critical bugs allow an attacker to execute code of their choice on the vulnerable system.

While Microsoft said there are no signs anyone is exploiting it yet, a security feature bypass in the .NET Framework (
[CVE-2026-108398](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-108398)
) was publicly disclosed prior to today, potentially giving attackers advance time to work out how to exploit the bug.

**Satnam Narang**
at
**Tenable**
said the number of flaws fixed this month far surpasses the previous record-setting year 2020, when Microsoft patched 1,261 CVEs.

“We’ve now crossed the 4,000 CVE mark with two months left to go,” he said.

Microsoft credits large language models for the high volume of bug discovery, and presumably AI gets credit for many of the patches used to fix these flaw. Meanwhile, security experts have been warning that these unusually large patch volleys from Microsoft are placing extra strain on corporate security teams, which often have to test individual updates before deploying them across a network to ensure the fixes don’t cause problems for other software.

**Tyler Reguly**
, associate director of security research and development at
**Fortra**
, notes that just 26 Microsoft vulnerabilities appeared in the “Known Exploited Vulnerabilities” (KEV) catalog maintained by the U.S. Cybersecurity &amp; Infrastructure Security Agency (CISA) so far this year, and security teams would do well to prioritize patching those 26 vulnerabilities first.

“Security leaders should focus on exploitable risk, and ask whether their teams have the clarity, capacity and support to act,” Reguly said.

Which vulnerabilities deserve the most scrutiny in your organization? The folks at
**Cisco Talos**
have
[a useful roundup](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-october-2026/)
of the more noteworthy flaws that Microsoft fixed today, and of course the
**SANS Internet Storm Center**
has
[a reliable roundup](https://isc.sans.edu/diary/October%202026%20Microsoft%20Patch%20Tuesday/33422)
that indexes vulnerabilities by severity, CVE number and affected software.