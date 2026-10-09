---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-15T02:03:12.607882+00:00'
exported_at: '2026-05-15T02:03:15.502060+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html
structured_data:
  about: []
  author: ''
  description: Fragnesia CVE-2026-46300 corrupts Linux page cache via XFRM ESP-in-TCP,
    enabling local root access on major distros.
  headline: New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption
updated_at: '2026-05-15T02:03:12.607882+00:00'
url_hash: b77db9a757e6652ca3fb8ae80763f049827b2aa8
---

**

Ravie Lakshmanan
**

May 14, 2026

Vulnerability / Linux

Details have emerged about a new variant of the recent
[Dirty Frag](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html)
Linux local privilege escalation (LPE) vulnerability that allows local attackers to gain root access, making it the third such bug to be identified in the kernel within a span of two weeks.

Codenamed
**[Fragnesia](https://github.com/v12-security/pocs/blob/main/fragnesia%2FREADME.md)**
, the security vulnerability is tracked as CVE-2026-46300 (CVSS score: 7.8) and is rooted in the Linux kernel's XFRM ESP-in-TCP subsystem. It was discovered by researcher William Bowling of the V12 security team.

"The vulnerability allows unprivileged local attackers to modify read-only file contents in the kernel page cache and achieve root privileges through a deterministic page-cache corruption primitive," Google-owned Wiz
[said](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
.

Advisories have been released by multiple Linux distributions -

"This is a separate bug in the ESP/XFRM from Dirty Frag which has received its own patch," V12 said. "However, it is in the same surface and the mitigation is the same as for Dirty Frag. It abuses a logic bug in the Linux XFRM ESP-in-TCP subsystem to achieve arbitrary byte writes into the kernel page cache of read-only files, without requiring any race condition."

Fragnesia is similar to
[Copy Fail](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/)
and
[Dirty Frag](https://www.automox.com/blog/dirty-frag-what-you-need-to-know-and-how-to-respond)
(aka Copy Fail 2) in that it immediately yields root on all major distributions by achieving a memory write primitive in the kernel and corrupting the page cache memory of the /usr/bin/su binary. A proof-of-concept (PoC) exploit has been released by V12.

"Customers who have already applied the Dirty Frag mitigation need no further action until patched kernels are released," CloudLinux maintainers said. Red Hat
[said](https://access.redhat.com/security/vulnerabilities/RHSB-2026-003)
it's performing an assessment to confirm if existing mitigations extend to CVE-2026-46300.

Wiz also noted that AppArmor restrictions on unprivileged user namespaces may serve as a partial mitigation, requiring additional bypasses for successful exploitation. However, unlike Dirty Frag, no host-level privileges are required.

"A patch is available, and while no in-the-wild exploitation has been observed at this time, we urge users and organizations to apply the patch as soon as possible by running update tools," Microsoft
[said](https://x.com/MsftSecIntel/status/2054701609024934064)
. "If patching is not possible at this point, consider applying the same mitigations for Dirty Frag."

This includes disabling esp4, esp6, and related xfrm/IPsec functionality, restricting unnecessary local shell access, hardening containerized workloads, and increasing monitoring for abnormal privilege escalation activity.

The development comes as a threat actor named "berz0k" has been observed advertising on cybercrime forums a zero-day Linux LPE exploit for $170,000, claiming it works on multiple major Linux distributions.

"The threat actor claims the vulnerability is TOCTOU-based (Time-of-Check Time-of-Use), capable of stable local privilege escalation without causing system crashes, and leverages a shared object (.so) payload dropped into the /tmp directory," ThreatMon
[said](https://x.com/MonThreat/status/2054516027912769579)
in a post on X.