---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:49:03.637217+00:00'
exported_at: '2026-11-15T06:49:09.975028+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches
structured_data:
  about: []
  author: ''
  description: N-able has patched several CVEs in N-central dropped as zero-days over
    the weekend and already targeted in the wild.
  headline: Hackers Target N-central Zero-Days as N-able Rushes Patches
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hackers Target N-central Zero-Days as N-able Rushes Patches
updated_at: '2026-11-15T06:49:03.637217+00:00'
url_hash: 0bba49a341bfd9be4182b59d2dd64e9a3c0e8615
---

**N-able has rolled out patches for several of the zero-days a researcher dropped over the weekend and warned of in-the-wild activity targeting them.**

Security researcher Sean Bales published details and proof-of-concept (PoC) on more than 30 N-central vulnerabilities he calls Able2Shell, saying he did not responsibly disclose them because he was unhappy with N-able not patching two flaws he previously reported in another product.

On Monday, the company
[took hosted N-central environments offline](https://www.securityweek.com/n-able-takes-n-central-offline-as-researcher-drops-over-30-zero-days/)
to investigate the security defects and develop fixes, urging customers to disconnect their on-premises deployments as well.

Although patches have been developed only for the more important bugs, N-able has brought the hosted environments
[back online](https://uptime.n-able.com/event/202584/)
, saying the risk is largely mitigated.

According to the company, all the vulnerabilities that could be exploited without authentication have been resolved, with fixes prioritized based on severity and exploitability.

“The remaining vulnerabilities require an authenticated N-central account often with elevated privileges, or additional conditions that limit exploitability, and will be addressed through subsequent hotfixes as we continue to prioritize the security and protection of our customers,”
[N-able says](https://www.n-able.com/blog/update-on-n-central-2026-4-hf2-and-ongoing-security-response)
.

Advertisement. Scroll to continue reading.

The resolved vulnerabilities include CVE-2026-125883 (multiple XXE issues, CVSS score of 9.3), CVE-2026-125878 (XSS flaws, CVSS score of 8.7), CVE-2026-125879 (privilege escalation, CVSS score of 8.6), CVE-2026-125880 (XSS, CVSS score of 8.3), CVE-2026-125881 (SSRF, CVSS score of 9.3), and CVE-2026-91000 (missing authentication, leading to privilege escalation, CVSS score of 8.4).

Additionally, the update resolves CVE-2026-125882 (path traversal to remote code execution, CVSS score of 8.6), which was reported by Nate Fair of Sprocket Security.

N-central 2026.4 HF2 includes the necessary patches, and all on-premises N-central deployments should be updated as soon as possible, as attackers are already probing exposed instances, the company notes.

“We are observing scanning activity associated with the publicly released proof-of-concept code, but we have seen no indications of compromise within N-central hosted servers,” N-able says.

Cybersecurity firm
[Defused says](https://x.com/DefusedCyber/status/2120177846970691916)
initial scanning started on Monday: “We have seen opening of anonymous agent sessions, pulling appliance config and hitting the remote-control endpoint without auth. These pathways are part of the 0-day exploit surface.”

N-able also refuted Bales’s claim that it ignored responsible disclosure, noting that the researcher did not contact it through its established reporting channels regarding the dropped vulnerabilities. However, it made no mention of previous vulnerability reports submitted by the researcher.

“Publishing exploit code before customers have had the chance to act doesn’t make anyone safer. It hands attackers a head start. This is a moment for our industry to recommit to putting customers first and honoring that duty to protect: being diligent, being transparent, and being measured in how we act,” N-able president and CEO John Pagliuca said.

**Related:**
[Critical Xen Orchestra Flaws Exploited in Attacks](https://www.securityweek.com/critical-xen-orchestra-flaws-exploited-in-attacks/)

**Related:**
[Asus, Zoom Release Security Patches](https://www.securityweek.com/asus-zoom-release-security-patches/)

**Related:**
[Citrix, Ivanti Patch Critical and High-Severity Vulnerabilities](https://www.securityweek.com/citrix-ivanti-patch-critical-and-high-severity-vulnerabilities/)

**Related:**
[Fortinet Patches Nearly 100 Vulnerabilities](https://www.securityweek.com/fortinet-patches-nearly-100-vulnerabilities/)