---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-21T16:15:12.682126+00:00'
exported_at: '2026-01-21T16:15:14.969875+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/zoom-and-gitlab-release-security.html
structured_data:
  about: []
  author: ''
  description: Zoom patched a critical CVE-2026-22844 RCE flaw in Node MMRs, while
    GitLab fixed DoS and 2FA bypass vulnerabilities affecting CE and EE versions.
  headline: Zoom and GitLab Release Security Updates Fixing RCE, DoS, and 2FA Bypass
    Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/zoom-and-gitlab-release-security.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Zoom and GitLab Release Security Updates Fixing RCE, DoS, and 2FA Bypass Flaws
updated_at: '2026-01-21T16:15:12.682126+00:00'
url_hash: 07806ecab39c613d35d27b788fb4096fb5dcea56
---

**

Ravie Lakshmanan
**

Jan 21, 2026

Vulnerability / Network Security

Zoom and GitLab have released security updates to resolve a number of security vulnerabilities that could result in denial-of-service (DoS) and remote code execution.

The most severe of the lot is a critical security flaw impacting Zoom Node Multimedia Routers (MMRs) that could permit a meeting participant to conduct remote code execution attacks. The vulnerability, tracked as
**CVE-2026-22844**
and discovered internally by its Offensive Security team, carries a CVSS score of 9.9 out of 10.0.

"A command injection vulnerability in Zoom Node Multimedia Routers (MMRs) before version 5.2.1716.0 may allow a meeting participant to conduct remote code execution of the MMR via network access," the company
[noted](https://www.zoom.com/en/trust/security-bulletin/zsb-26001/)
in a Tuesday alert.

Zoom is recommending that customers using Zoom Node Meetings, Hybrid, or Meeting Connector deployments update to the latest available MMR version to safeguard against any potential threat.

There is no evidence that the security flaw has been exploited in the wild. The vulnerability affects the following versions -

* Zoom Node Meetings Hybrid (ZMH) MMR module versions prior to 5.2.1716.0
* Zoom Node Meeting Connector (MC) MMR module versions prior to 5.2.1716.0

### GitLab Releases Patches for Severe Flaws

The disclosure comes as GitLab
[released](https://about.gitlab.com/releases/2026/01/21/patch-release-gitlab-18-8-2-released/)
fixes for multiple high-severity flaws affecting its Community Edition (CE) and Enterprise Edition (EE) that could result in DoS and a bypass of two-factor authentication (2FA) protections. The shortcomings are listed below -

* **CVE-2025-13927**
  (CVSS score: 7.5) - A vulnerability that could allow an unauthenticated user to create a DoS condition by sending crafted requests with malformed authentication data (Affects all versions from 11.9 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2)
* **CVE-2025-13928**
  (CVSS score: 7.5) - An incorrect authorization vulnerability in the Releases API that could allow an unauthenticated user to cause a DoS condition (Affects all versions from 17.7 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2)
* **CVE-2026-0723**
  (CVSS score: 7.4) - A vulnerability that could allow an individual with existing knowledge of a victim's credential ID to bypass 2FA by submitting forged device responses (Affects all versions from 18.6 before 18.6.4, 18.7 before 18.7.2, and 18.8 before 18.8.2 )

Also remediated by GitLab are two other medium-severity bugs that could also trigger a DoS condition (CVE-2025-13335, CVSS score: 6.5, and CVE-2026-1102, CVSS score: 5.3) by configuring malformed Wiki documents that bypass cycle detection and sending repeated malformed SSH authentication requests, respectively.