---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-15T10:15:14.508504+00:00'
exported_at: '2026-04-15T10:15:16.757654+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html
structured_data:
  about: []
  author: ''
  description: Microsoft fixes 169 vulnerabilities including exploited SharePoint
    CVE-2026-32201, prompting CISA remediation by April 28, 2026.
  headline: Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities
updated_at: '2026-04-15T10:15:14.508504+00:00'
url_hash: a781723982f1cab69e6e00ec13d283661e2f417b
---

Microsoft on Tuesday released updates to address a record
[169 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2026-apr)
across its product portfolio, including one vulnerability that has been actively exploited in the wild.

Of these 169 vulnerabilities, 157 are rated Important, eight are rated Critical, three are rated Moderate, and one is rated Low in severity. Ninety-three of the flaws are classified as privilege escalation, followed by 21 information disclosure, 21 remote code execution, 14 security feature bypass, 10 spoofing, and nine denial-of-service vulnerabilities.

Also included among the 169 flaws are four non-Microsoft issued CVEs impacting AMD (CVE-2023-20585), Node.js (CVE-2026-21637), Windows Secure Boot (CVE-2026-25250), and Git for Windows (CVE-2026-32631). The updates are in addition to
[78 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
that have been addressed in its Chromium-based Edge browser since the
[update that was released last month](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)
.

The release makes it the second biggest Patch Tuesday ever, a little below the record set in October 2025, when Microsoft addressed a
[massive 183 security flaws](https://thehackernews.com/2025/10/two-new-windows-zero-days-exploited-in.html)
. "At this pace, 2026 is on track to affirm that 1,000+ Patch Tuesday CVEs annually is the norm," Satnam Narang, senior staff research engineer at Tenable, said.

"Not only that, but elevation of privilege bugs continue to dominate the Patch Tuesday cycle over the last eight months, accounting for a record 57% of all CVEs patched in April, while remote code execution (RCE) vulnerabilities have dropped to just 12%, tied with information disclosure vulnerabilities this month."

The vulnerability that has come under active exploitation is
[CVE-2026-32201](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32201)
(CVSS score: 6.5), a spoofing vulnerability impacting Microsoft SharePoint Server.

"Improper input validation in Microsoft Office SharePoint allows an unauthorized attacker to perform spoofing over a network," Microsoft said in an advisory. "An attacker who successfully exploited the vulnerability could view some sensitive information (Confidentiality), make changes to disclosed information (Integrity), but cannot limit access to the resource (Availability)."

Although the vulnerability was internally discovered, it's currently not known how it'sbeing exploited, and who may be behind the activity, and the scale of such efforts.

"This zero-day vulnerability in Microsoft SharePoint Server is caused by improper input validation, allowing attackers to spoof trusted content or interfaces over a network," Mike Walters, president and co-founder of Action1, said.

"By exploiting this flaw, an attacker can manipulate how information is presented to users, potentially tricking them into trusting malicious content. While the direct impact on data is limited, the ability to deceive users makes this a powerful tool for broader attacks."

The active exploitation of CVE-2026-32201 has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to
[add](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog)
it to the Known Exploited Vulnerabilities (
[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to remediate the shortcoming by April 28, 2026.

Another vulnerability of note is a privilege escalation flaw in Microsoft Defender (
[CVE-2026-33825](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825)
, CVSS score: 7.8), which has been flagged as publicly known at the time of release. According to Redmond, the vulnerability could allow an authorized attacker to elevate privileges locally by taking advantage ofDefender'slack of adequate granular access controls.

Microsoft noted that no user action is required to install the update for CVE-2026-33825, as the platform updates itself frequently by default. Systems that have disabled Microsoft Defender are not in an exploitable state.

While Microsoft's advisory makes no mention of public exploit code, the patch is said to resolve a zero-day known as
[BlueHammer](https://www.tenable.com/blog/microsofts-april-2026-patch-tuesday-addresses-163-cves-cve-2026-32201)
that was
[shared](https://deadeclipse666.blogspot.com/2026/04/public-disclosure.html)
on GitHub on April 3, 2026, by a disgruntled security researcher using the alias "
[Chaotic Eclipse](https://x.com/ChaoticEclipse0/status/2040052131491660027)
" after a breakdown in communication with the tech giant over its handling of the vulnerability disclosure process. As of writing, access to the public exploit repository requires a user to sign in to GitHub.

Per Cyderes, the vulnerability exploits the Microsoft Defender update process through Volume Shadow Copy abuse to escalate a low-privileged user to NT AUTHORITY\SYSTEM by chaining together legitimate Windows features.

"During certain Defender update and remediation workflows, Defender creates a temporary Volume Shadow Copy snapshot," security researchers Rahul Ramesh and Reegun Jayapaul
[explained](https://www.cyderes.com/howler-cell/windows-zero-day-bluehammer)
earlier this month. "BlueHammer uses Cloud Files callbacks and oplocks to pause Defender at precisely the right moment, leaving the snapshot mounted and the SAM, SYSTEM, and SECURITY registry hives accessible – files that are normally locked at runtime."

"Successful exploitation allows an attacker to read the SAM database, decrypt NTLM password hashes, take over a local administrator account, and spawn a SYSTEM-level shell, all while restoring the original password hash to avoid detection."

Security researcher Will Dormann, in a
[post on Mastodon](https://infosec.exchange/@wdormann/116358064691025711)
, confirmed the BlueHammer exploit no longer works and "seems fixed as of CVE-2026-33825," although "some of the suspicious parts of the exploit still seem to work."

One of the most severe vulnerabilities is a case of remote code execution impacting the Windows Internet Key Exchange (IKE) Service Extensions.Tracked as
[CVE-2026-33824](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33824)
, the security defect has a CVSS score of 9.8 out of 10.0.

"Exploitation requires an attacker to send specially crafted packets to a Windows machine with IKE v2 enabled, which could enable remote code execution," Adam Barnett, lead software engineer at Rapid7, said in a statement.

"Vulnerabilities leading to unauthenticated RCE against modern Windows assets are relatively rare, or we’d see more wormable vulnerabilities self-propagating across the internet. However, since IKE provides secure tunnel negotiation services, for instance, for VPNs, it is necessarily exposed to untrusted networks and reachable in a pre-authorization context."

Walters noted that the security flaw poses a serious threat to enterprise environments, particularly those relying on VPN or IPsec for secure communications. Successful exploitation of the vulnerability could result in complete system compromise, allowing bad actors to steal sensitive data, disrupt operations, or move laterally across the network.

"The lack of required user interaction makes this especially dangerous for internet-facing systems. Its low attack complexity and full system impact make it a prime candidate for rapid weaponization," Walters added. "Internet-facing systems running IKEv2 services are particularly at risk, and delaying patch deployment increases exposure to potential widespread attacks."