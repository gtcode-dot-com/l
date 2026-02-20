---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-20T20:15:15.784217+00:00'
exported_at: '2026-02-20T20:15:18.039150+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html
structured_data:
  about: []
  author: ''
  description: CVE-2026-1731 in BeyondTrust RS and PRA is exploited for ransomware,
    web shells, C2, and data theft across multiple sectors
  headline: BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration
updated_at: '2026-02-20T20:15:15.784217+00:00'
url_hash: a169910a32ef307db48289493499c0e7c5fe478d
---

**

Ravie Lakshmanan
**

Feb 20, 2026

Vulnerability / Cyber Attack

Threat actors have been observed exploiting a recently disclosed critical security flaw impacting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products to conduct a wide range of malicious actions, including deploying VShell and

The vulnerability, tracked as
[**CVE-2026-1731**](https://thehackernews.com/2026/02/researchers-observe-in-wild.html)
(CVSS score: 9.9), allows attackers to execute operating system commands in the context of the site user.

In a report published Thursday, Palo Alto Networks Unit 42
[said](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)
it detected the security flaw being actively exploited in the wild for network reconnaissance, web shell deployment, command-and-control (C2), backdoor and remote management tool installs, lateral movement, and data theft.

The campaign has targeted financial services, legal services, high technology, higher education, wholesale and retail, and healthcare sectors across the U.S., France, Germany, Australia, and Canada.

The cybersecurity company described the vulnerability as a case of sanitization failure that enables an attacker to leverage the affected "thin-scc-wrapper" script that's reachable via WebSocket interface to inject and execute arbitrary shell commands in the context of the site user.

"While this account is distinct from the root user, compromising it effectively grants the attacker control over the appliance's configuration, managed sessions and network traffic," security researcher Justin Moore said.

The current scope of attacks exploiting the flaw range from reconnaissance to backdoor deployment -

* Using a custom Python script to gain access to an administrative account.
* Installing multiple web shells across directories, including a PHP backdoor that's capable of executing raw PHP code or running arbitrary PHP code without writing new files to disk, as well as a bash dropper that establishes a persistent web shell.
* Deploying malware such as
  [VShell](https://www.trellix.com/blogs/research/the-silent-fileless-threat-of-vshell/)
  and
  [Spark RAT](https://thehackernews.com/2023/01/chinese-hackers-utilize-golang-malware.html)
  .
* Using out-of-band application security testing (OAST) techniques to validate successful code execution and fingerprint compromised systems.
* Executing commands to stage, compress and exfiltrate sensitive data, including configuration files, internal system databases and a full PostgreSQL dump, to an external server.

"The relationship between CVE-2026-1731 and
[CVE-2024-12356](https://thehackernews.com/2025/02/beyondtrust-zero-day-breach-exposes-17.html)
highlights a localized, recurring challenge with input validation within distinct execution pathways," Unit 42 said.

"CVE-2024-12356's insufficient validation was using third-party software (postgres), while CVE-2026-1731's insufficient validation problem occurred in the BeyondTrust Remote Support (RS) and older versions of the BeyondTrust Privileged Remote Access (PRA) codebase."

With CVE-2024-12356 exploited by China-nexus threat actors like
[Silk Typhoon](https://thehackernews.com/2025/03/china-linked-silk-typhoon-expands-cyber.html)
, the cybersecurity company noted that CVE-2026-1731 could also be a target for sophisticated threat actors.

The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA)
[updated](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-1731&field_date_added_wrapper=all&field_cve=&sort_by=field_date_added&items_per_page=20&url=)
its Known Exploited Vulnerabilities (KEV) catalog entry for CVE-2026-1731 to confirm that the bug has been exploited in ransomware campaigns.