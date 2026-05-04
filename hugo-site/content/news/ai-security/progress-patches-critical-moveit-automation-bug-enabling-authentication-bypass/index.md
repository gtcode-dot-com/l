---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-04T18:15:13.928901+00:00'
exported_at: '2026-05-04T18:15:16.995640+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/progress-patches-critical-moveit.html
structured_data:
  about: []
  author: ''
  description: MOVEit Automation flaws (CVE-2026-4670, CVE-2026-5174) enable bypass
    and escalation, risking enterprise data exposure.
  headline: Progress Patches Critical MOVEit Automation Bug Enabling Authentication
    Bypass
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/progress-patches-critical-moveit.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Progress Patches Critical MOVEit Automation Bug Enabling Authentication Bypass
updated_at: '2026-05-04T18:15:13.928901+00:00'
url_hash: 2f4f35446dc4963babf596bfaec17e6ce786c133
---

**

Ravie Lakshmanan
**

May 04, 2026

Vulnerability / Enterprise Software

Progress Software has released updates to address two security flaws in MOVEit Automation, including a critical bug that could result in an authentication bypass.

MOVEit Automation (formerly Central) is a secure, server-based managed file transfer (MFT) solution used to schedule and automate file movement workflows in enterprise environments without requiring any custom scripts.

The vulnerabilities in question are
[CVE-2026-4670](https://nvd.nist.gov/vuln/detail/CVE-2026-4670)
(CVSS score: 9.8), an authentication bypass vulnerability, and
[CVE-2026-5174](https://nvd.nist.gov/vuln/detail/CVE-2026-5174)
(CVSS score: 7.7), an improper input validation vulnerability that could allow privilege escalation.

"Critical and high vulnerabilities in MOVEit Automation may allow authentication bypass and privilege escalation through the service backend command port interfaces," Progress Software
[said](https://community.progress.com/s/article/MOVEit-Automation-Critical-Security-Alert-Bulletin-April-2026-CVE-2026-4670-CVE-2026-5174)
in an advisory. "Exploitation may lead to unauthorized access, administrative control, and data exposure."

The shortcomings affect the following versions -

* MOVEit Automation <= 2025.1.4 (Fixed in MOVEit Automation 2025.1.5)
* MOVEit Automation <= 2025.0.8 (Fixed in MOVEit Automation 2025.0.9)
* MOVEit Automation <= 2024.1.7 (Fixed in MOVEit Automation 2024.1.8)

Airbus SecLab researchers Anaïs Gantet, Delphine Gourdou, Quentin Liddell, and Matteo Ricordeau have been
[credited](https://airbus-seclab.github.io/#2026)
with discovering and reporting the two vulnerabilities. There are no workarounds that resolve the issues.

While Progress makes no mention of the flaws being exploited in the wild, it's essential that users apply the fixes as soon as possible for optimal protection, particularly given that
[prior flaws](https://thehackernews.com/2023/06/third-flaw-uncovered-in-moveit-transfer.html)
in
[MOVEit Transfer](https://thehackernews.com/2025/06/moveit-transfer-faces-increased-threats.html)
have been exploited by ransomware gangs like Cl0p.