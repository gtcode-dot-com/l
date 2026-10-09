---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T16:15:14.785437+00:00'
exported_at: '2026-02-02T16:15:18.153322+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/microsoft-begins-ntlm-phase-out-with.html
structured_data:
  about: []
  author: ''
  description: Microsoft confirms a 3-phase strategy to deprecate NTLM, improve auditing,
    prioritize Kerberos, and disable NTLM by default in future Windows releases
  headline: Microsoft Begins NTLM Phase-Out With Three-Stage Plan to Move Windows
    to Kerberos
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/microsoft-begins-ntlm-phase-out-with.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Begins NTLM Phase-Out With Three-Stage Plan to Move Windows to Kerberos
updated_at: '2026-02-02T16:15:14.785437+00:00'
url_hash: 2c2cefa34882705a56d19de2961728061480908d
---

**

Ravie Lakshmanan
**

Feb 02, 2026

Kerberos / Enterprise Security

Microsoft has
[announced](https://techcommunity.microsoft.com/blog/windows-itpro-blog/advancing-windows-security-disabling-ntlm-by-default/4489526)
a three-phase approach to phase out New Technology LAN Manager (NTLM) as part of its efforts to shift Windows environments toward stronger, Kerberos-based options.

The development comes more than two years after the tech giant
[revealed](https://thehackernews.com/2023/10/microsoft-to-phase-out-ntlm-in-favor-of.html)
its plans to deprecate the legacy technology, citing its susceptibility to weaknesses that could facilitate relay attacks and allow bad actors to gain unauthorized access to network resources. NTLM was
[formally deprecated](https://thehackernews.com/2024/05/windows-11-to-deprecate-ntlm-add-ai.html)
in
[June 2024](https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features#deprecated-features)
and no longer receives updates.

"NTLM consists of security protocols originally designed to provide authentication, integrity, and confidentiality to users," Mariam Gewida, Technical Program Manager II at Microsoft, explained. "However, as security threats have evolved, so have our standards to meet modern security expectations. Today, NTLM is susceptible to various attacks, including replay and man-in-the-middle attacks, due to its use of weak cryptography."

Despite the deprecated status, Microsoft said it continues to find the use of NTLM prevalent in enterprise environments where modern protocols like Kerberos cannot be implemented due to legacy dependencies, network limitations, or ingrained application logic. This, in turn, exposes organizations to security risks, such as replay, relay, and pass-the-hash attacks.

To mitigate this problem in a secure manner, the company has adopted a three-phase strategy that paves the way for NTLM to be disabled by default -

* Phase 1: Building visibility and control using
  [enhanced NTLM auditing](https://support.microsoft.com/en-us/topic/overview-of-ntlm-auditing-enhancements-in-windows-11-version-24h2-and-windows-server-2025-b7ead732-6fc5-46a3-a943-27a4571d9e7b)
  to better understand where and why NTLM is still being used (Available now)
* Phase 2: Addressing common roadblocks that prevent a migration to NTLM through features like IAKerb and local Key Distribution Center (KDC) (pre-release), as well as updating core Windows components to prioritize Kerberos authentication (Expected in H2 2026)
* Phase 3: Disabling NTLM in the next version of Windows Server and associated Windows client, and requiring explicit re-enablement through new policy controls

Microsoft has positioned the transition as a major step toward a passwordless, phishing-resistant future. This also requires organizations relying on NTLM to conduct audits, map dependencies, migrate to Kerberos, test NTLM-off configurations in non-production environments, and enable Kerberos upgrades.

"Disabling NTLM by default does not mean completely removing NTLM from Windows yet," Gewida said. "Instead, it means that Windows will be delivered in a secure-by-default state where network NTLM authentication is blocked and no longer used automatically."

"The OS will prefer modern, more secure Kerberos-based alternatives. At the same time, common legacy scenarios will be addressed through new upcoming capabilities such as Local KDC and IAKerb (pre-release)."