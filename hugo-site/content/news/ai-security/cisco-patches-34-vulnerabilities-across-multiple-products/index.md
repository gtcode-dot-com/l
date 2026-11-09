---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-09T03:34:29.590865+00:00'
exported_at: '2026-11-09T03:34:30.360780+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/cisco-patches-34-vulnerabilities-across-multiple-products
structured_data:
  about: []
  author: ''
  description: Cisco has patched 34 vulnerabilities across Expressway Series, IOS
    XR, Snort 3, and Unified Communications products.
  headline: Cisco Patches 34 Vulnerabilities Across Multiple Products
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/cisco-patches-34-vulnerabilities-across-multiple-products
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cisco Patches 34 Vulnerabilities Across Multiple Products
updated_at: '2026-11-09T03:34:29.590865+00:00'
url_hash: b3d99a3d973f9b778f7b49ca99c3a9066fc66183
---

**Cisco on Wednesday announced patches for 34 vulnerabilities across Expressway Series, IOS XR, Snort 3, and Unified Communications products.**

Expressway Series received fixes for 10 vulnerabilities, including a critical-severity remote code execution (RCE) bug tracked as CVE-2026-76466.

According to Cisco, the use of persistent cookies and insufficient validation of client certificates in certain configurations could allow attackers to connect to the database service and invoke specific remote procedure call (RPC) commands to exploit the bug.

“A successful exploit could allow the attacker to execute arbitrary commands as root on the underlying operating system of an affected device,” Cisco notes.

The security defect was patched in Expressway Series version X15.5.20, which also resolves eight CVEs that group multiple vulnerabilities under their specific CWE category. A medium-severity information disclosure bug was also fixed.

Cisco patched nine CVEs in Unified Communications products, including Emergency Responder, Prime Collaboration Deployment, Unified Communications Manager (CM), Unified Communications Manager IM &amp; Presence Service (CM IM&amp;P), Unified Communications Manager Session Management Edition (CM SME), and Unity Connection.

Advertisement. Scroll to continue reading.

The most severe are CVE-2026-76473, CVE-2026-76474, and CVE-2026-76475, three critical-severity issues that group multiple improper resource control, improper authentication, and improper input neutralization holes.

Multiple Cisco products received patches for 13 CVEs affecting Snort 3, including CVE-2026-20236 and CVE-2026-20043, which group critical-severity incorrect calculation and out-of-bounds write issues.

The fixes also resolve high-severity privilege management, resource consumption, and arbitrary command execution bugs, as well as medium-severity issues, and were included in Snort 3 version 3.12.4.0 and in security updates for Cyber Vision, CDFW, Meraki MX, CSA, Secure Firewall ASA, Secure FMC, Secure FTD, and UTD for IOS XE.

Additionally, Cisco patched a high-severity denial-of-service (DoS) vulnerability in IOS XR, tracked as CVE-2026-76505, and a high-severity privilege escalation bug in Secure Client’s Secure Firewall Posture module (CVE-2026-76462).

Cisco says it is not aware of any of these vulnerabilities being exploited in the wild. Additional information can be found on the company’s
[security advisories](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
page and in its October 21
[notification](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-QGwHnJ6k)
.

**Related:**
[Oracle Patches Over 1,200 Vulnerabilities With October 2026 CPU](https://www.securityweek.com/oracle-patches-over-1200-vulnerabilities-with-october-2026-cpu/)

**Related:**
[PHP2Shell Patches Land as First Exploitation Attempts Hit Sensors](https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/)

**Related:**
[Google Hardens Chrome Against ClickFix Attacks, Insecure HTTP Connections](https://www.securityweek.com/google-hardens-chrome-against-clickfix-attacks-insecure-http-connections/)

**Related:**
[Memory Bugs Account for Most of Chrome’s 353 New Security Fixes](https://www.securityweek.com/memory-bugs-account-for-most-of-chromes-353-new-security-fixes/)