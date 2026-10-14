---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-14T05:07:04.204508+00:00'
exported_at: '2026-10-14T05:07:05.557360+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
structured_data:
  about: []
  author: ''
  description: An attacker exploited three Ivanti Connect Secure zero-days to run
    commands as root and steal stored credentials from one appliance.
  headline: Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access,
    Only Two Patched So Far
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only
  Two Patched So Far
updated_at: '2026-10-14T05:07:04.204508+00:00'
url_hash: fb99d329a170ccdf90361b408a1b6b357ac741ed
---

**

Swati Khandelwal
**

Oct 13, 2026

Vulnerability / Enterprise Security

An attacker chained three zero-day flaws in Ivanti Connect Secure, a VPN appliance, to run commands as root without logging in, security firm
[Volexity said](https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/)
on October 13. Ivanti has released fixes for two of the flaws and told customers on affected versions to "act immediately." A fix for the third is still pending, according to Volexity.

Volexity, which reported the flaws to Ivanti, found the attack on one customer's appliance. The appliance was fully patched at the time and running version 22.8R2.4. The attacker, which Volexity tracks as UTA0576, began exploiting it on October 3.

[Ivanti said](https://www.ivanti.com/en-gb/blog/october-2026-security-update)
on October 13 that it is aware of "limited exploitation in the wild."

The first two flaws are an authentication bypass and a remote code execution flaw, tracked together as
[CVE-2026-104935](https://www.cve.org/CVERecord?id=CVE-2026-104935)
. Together they let an attacker run code as the appliance's cgi-server user, and the third flaw, a privilege escalation, raises that to root, Volexity said.

The CVE record Ivanti filed shows which Connect Secure versions are affected:

* **Affected:**
  Connect Secure "before version 25.1.3.0"
* **Not affected:**
  version 22.7R2.14 "or prior"
* **Listed as unaffected:**
  versions 22.8R2.5, 25.1.3.0 and 25.1.3.1

Ivanti's
[security advisory](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935)
has more on the affected versions and the fixes.

The
[release notes for 25.1.3.0](https://help.ivanti.com/ps/help/en_US/ICS/25.1.x/25.1.3.0/25.xICSRN.pdf)
are dated July 2026. Customers already on that version are outside the range the CVE record gives.

Ivanti is working on a fix for the privilege escalation flaw, which will come "in a future release in the coming weeks," Volexity said. Its report does not say what risk that flaw carries on an appliance where the first two are fixed.

Ivanti tells customers to upgrade and to run its Integrity Checker Tool regularly. That tool misses this chain, Volexity said, because the exploit changes library code only in memory and restores the configuration data it alters. The attacker also took steps to stay hidden from the tool.

Confirming a compromise takes forensic investigation, including network and memory forensics, according to Volexity. These signs come from the one incident it investigated:

* **URL path:**
  /dana-na/auth/url\_default/welcome.cgi, requested in large numbers
* **HTTP header:**
  X-DSCGI-PATH on those requests, with a value that does not match the URL path
* **Directory:**
  /data/.icscap/
* **IP:**
  108.165.147[.]64, the host the attacker used

In that incident, the attacker stole stored credentials, including LDAP domain credentials, searched Active Directory for passwords, and ran password-spraying attacks against its accounts. No backdoor or web shell was left behind. The attacker reran the entire exploit chain for each command.

Volexity's report and Ivanti's post do not name a temporary workaround for customers who cannot upgrade yet. They also do not say whether upgrading removes access an attacker has already gained.

Volexity assessed with low confidence that UTA0576's motive is criminal, not espionage. Neither company said how many customers were attacked.

Ivanti rates CVE-2026-104935 8.6 out of 10 on the CVSS severity scale. In its own entry in the CVE record, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) marks exploitation as "active" and the technical impact as "total."

Separately, the same Ivanti post covers fixes for two other products, Xtraction and Neurons Patch for Intune, and Ivanti said it is not aware of those flaws being exploited. Each has a flaw Ivanti rates 9.9 out of 10:
[CVE-2026-106042](https://www.cve.org/CVERecord?id=CVE-2026-106042)
in Xtraction before version 2026.4, and
[CVE-2026-109412](https://www.cve.org/CVERecord?id=CVE-2026-109412)
in Neurons Patch for Intune.