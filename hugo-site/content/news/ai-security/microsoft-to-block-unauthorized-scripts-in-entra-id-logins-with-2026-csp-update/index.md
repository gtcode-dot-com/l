---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-28T00:00:07.638692+00:00'
exported_at: '2025-11-28T00:00:09.872775+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/microsoft-to-block-unauthorized-scripts.html
structured_data:
  about: []
  author: ''
  description: Microsoft is tightening Entra ID security with CSP updates blocking
    unauthorized scripts by October 2026.
  headline: Microsoft to Block Unauthorized Scripts in Entra ID Logins with 2026 CSP
    Update
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/microsoft-to-block-unauthorized-scripts.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft to Block Unauthorized Scripts in Entra ID Logins with 2026 CSP Update
updated_at: '2025-11-28T00:00:07.638692+00:00'
url_hash: 6289c5b25d8eab6c5d95b22fd19375a6623b2a4c
---

**

Nov 27, 2025
**

Ravie Lakshmanan

Web Security / Zero Trust

Microsoft has announced plans to improve the security of Entra ID authentication by blocking unauthorized script injection attacks starting a year from now.

The update to its Content Security Policy (CSP) aims to enhance the Entra ID sign-in experience at "login.microsoftonline[.]com" by only letting scripts from trusted Microsoft domains run.

"This update strengthens security and adds an extra layer of protection by allowing only scripts from trusted Microsoft domains to run during authentication, blocking unauthorized or injected code from executing during the sign-in experience," the Windows maker
[said](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/enhance-protection-of-microsoft-entra-id-authentication-by-blocking-external-scr/4435200)
.

Specifically, it only allows script downloads from Microsoft trusted CDN domains and inline script execution from a Microsoft trusted source. The updated policy is limited to browser-based sign-in experiences for URLs beginning with login.microsoftonline.com. Microsoft Entra External ID will not be affected.

The change, which has been described as a proactive measure, is part of Microsoft's Secure Future Initiative (
[SFI](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative)
) and is designed to safeguard users against cross-site scripting (XSS) attacks that make it possible to inject malicious code into websites. It's expected to be rolled out globally starting mid-to-late October 2026.

Microsoft is urging organizations to test their sign-in flows thoroughly ahead of time to ensure that there are no issues and the sign-in experience has no friction.

It's also advising customers to refrain from using browser extensions or tools that inject code or script into the Microsoft Entra sign-in experience. Those who follow this approach are recommended to switch to other tools that don't inject code.

To identify any CSP violations, users can go through a sign-in flow with the dev console open and access the browser's Console tool within the developer tools to check for errors that say "Refused to load the script" for going against the "
[script-src](https://content-security-policy.com/script-src/)
" and "
[nonce](https://content-security-policy.com/nonce/)
" directives.

Microsoft's SFI is a multi-year effort that seeks to put security above all else when designing new products and better prepare for the growing sophistication of cyber threats.

It was first launched in November 2023 and expanded in May 2024 following a report from the U.S. Cyber Safety Review Board (CSRB), which
[concluded](https://thehackernews.com/2024/04/us-cyber-safety-board-slams-microsoft.html)
that the company's "security culture was inadequate and requires an overhaul."

In its
[third progress report](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative/sfi-progress-report-november-2025)
published this month, the tech giant said it has deployed over 50 new detections in its infrastructure to target high-priority tactics, techniques, and procedures, and that the adoption of phishing-resistant multi-factor authentication (MFA) for users and devices has hit 99.6%.

Other notable changes enacted by Microsoft are as follows -

* Enforced Mandatory MFA across all services, including for all Azure service users
* Introduced Automatic recovery capabilities via Quick Machine Recovery, expanded passkey and Windows Hello support, and improved memory safety in UEFI firmware and drivers by using Rust
* Migrated 95% of Microsoft Entra ID signing VMs to Azure Confidential Compute and moved 94.3% of Microsoft Entra ID security token validation to its standard identity Software Development Kit (SDK)
* Discontinued the use of Active Directory Federation Services (ADFS) in our productivity environment
* Decommissioned 560,000 additional unused and aged tenants and 83,000 unused Microsoft Entra ID apps across Microsoft production and productivity environments
* Advanced threat hunting by centrally tracking 98% of production infrastructure
* Achieved complete network device inventory and mature asset lifecycle management
* Almost entirely locked code signing to production identities
* Published 1,096 CVEs, including 53 no-action cloud CVEs, and paid out $17 million in bounties

"To align with Zero Trust principles, organizations should automate vulnerability detection, response, and remediation using integrated security tools and threat intelligence," Microsoft said. "Maintaining real-time visibility into security incidents across hybrid and cloud environments enables faster containment and recovery."