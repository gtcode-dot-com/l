---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-24T04:44:17.296176+00:00'
exported_at: '2026-03-24T04:44:19.784276+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/cisa-flags-apple-craft-cms-laravel-bugs.html
structured_data:
  about: []
  author: ''
  description: CISA adds 5 exploited flaws (CVSS up to 10.0) to KEV, mandates April
    3, 2026 patching to prevent malware and espionage attacks.
  headline: CISA Flags Apple, Craft CMS, Laravel Bugs in KEV, Orders Patching by April
    3, 2026
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/cisa-flags-apple-craft-cms-laravel-bugs.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: CISA Flags Apple, Craft CMS, Laravel Bugs in KEV, Orders Patching by April
  3, 2026
updated_at: '2026-03-24T04:44:17.296176+00:00'
url_hash: 3e6ad7000ec2544a0a5f2c5eed3dfe3613937b2e
---

**

Ravie Lakshmanan
**

Mar 21, 2026

Vulnerability / Threat Intelligence

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday
[added](https://www.cisa.gov/news-events/alerts/2026/03/20/cisa-adds-five-known-exploited-vulnerabilities-catalog)
five security flaws impacting Apple, Craft CMS, and Laravel Livewire to its Known Exploited Vulnerabilities (
[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
) catalog, urging federal agencies to patch them by April 3, 2026.

The vulnerabilities that have come under exploitation are listed below -

* **[CVE-2025-31277](https://nvd.nist.gov/vuln/detail/CVE-2025-31277)**
  (CVSS score: 8.8) - A vulnerability in Apple WebKit that could result in memory corruption when processing maliciously crafted web content. (Fixed in July 2025)
* **[CVE-2025-43510](https://nvd.nist.gov/vuln/detail/CVE-2025-43510)**
  (CVSS score: 7.8) - A memory corruption vulnerability in Apple's kernel component that could allow a malicious application to cause unexpected changes in memory shared between processes. (Fixed in December 2025)
* **[CVE-2025-43520](https://nvd.nist.gov/vuln/detail/CVE-2025-43520)**
  (CVSS score: 8.8) - A memory corruption vulnerability in Apple's kernel component that could allow a malicious application to cause unexpected system termination or write kernel memory. (Fixed in December 2025)
* **[CVE-2025-32432](https://nvd.nist.gov/vuln/detail/CVE-2025-32432)**
  (CVSS score: 10.0) - A code injection vulnerability in Craft CMS that could allow a remote attacker to execute arbitrary code. (Fixed in April 2025)
* **[CVE-2025-54068](https://nvd.nist.gov/vuln/detail/CVE-2025-54068)**
  (CVSS score: 9.8) - A code injection vulnerability in Laravel Livewire that could allow unauthenticated attackers to achieve remote command execution in specific scenarios. (Fixed in July 2025)

The addition of the three Apple vulnerabilities to the KEV catalog comes in the wake of reports from Google Threat Intelligence Group (GTIG), iVerify, and Lookout about an iOS exploit kit codenamed
[DarkSword](https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html)
that leverages these shortcomings, along with three bugs, to deploy various malware families like GHOSTBLADE, GHOSTKNIFE, and GHOSTSABER for data theft.

CVE-2025-32432 is assessed to have been
[exploited](https://thehackernews.com/2025/04/hackers-exploit-critical-craft-cms.html)
as a zero-day by unknown threat actors since February 2025, per Orange Cyberdefense SensePost. Since then, an intrusion set tracked as
[Mimo](https://thehackernews.com/2025/05/mimo-hackers-exploit-cve-2025-32432-in.html)
(aka Hezb) has also been observed exploiting the vulnerability to deploy a cryptocurrency miner and residential proxyware.

Rounding off the list is
[CVE-2025-54068](https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html#:~:text=Flaw%20in%20Livewire%20Disclosed)
, whose exploitation was
[recently flagged](https://thehackernews.com/2026/03/weekly-recap-qualcomm-0-day-ios-exploit.html#:~:text=MuddyWater%20Evolves%20Its%20Tactics)
by the Ctrl-Alt-Intel Threat Research team as part of attacks mounted by the Iranian state-sponsored hacking group,
[MuddyWater](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)
(aka Boggy Serpens).

In a report published earlier this week, Palo Alto Networks Unit 42 called out the adversary's consistent targeting of diplomatic and critical infrastructure, including energy, maritime, and finance, across the Middle East and other strategic targets worldwide.

"While social engineering remains its defining trait, the group is also increasing its technological capabilities," Unit 42
[said](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/)
. "Its diverse toolset includes AI-enhanced malware implants that incorporate anti-analysis techniques for long-term persistence. This combination of social engineering and rapidly developed tools creates a potent threat profile."

"To support its large-scale social engineering campaigns, Boggy Serpens uses a custom-built, web-based orchestration platform," Unit 42 said. "This tool enables operators to automate mass email delivery while maintaining granular control over sender identities and target lists."

Attributed to the Iranian Ministry of Intelligence and Security (MOIS), the group is primarily focused on cyber espionage, although it has also been linked to disruptive operations targeting the Technion Israel Institute of Technology by adopting the
[DarkBit](https://thehackernews.com/2024/04/iranian-muddywater-hackers-adopt-new-c2.html)
ransomware persona.

One of the defining hallmarks of MuddyWater's tradecraft has been the use of hijacked accounts belonging to official government and corporate entities in its spear-phishing attacks, and abuse of trusted relationships to evade reputation-based blocking systems and deliver malware.

In a sustained campaign targeting an unnamed national marine and energy company in the U.A.E. between August 16, 2025, and February 11, 2026, the threat actor is said to have conducted four distinct waves of attack, leading to the deployment of various malware families, including
[GhostBackDoor and Nuso](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)
(aka HTTP\_VIP). Some of the other notable tools in the threat actor's arsenal include
[UDPGangster](https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html)
and
[LampoRAT](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)
(aka CHAR).

"Boggy Serpens' recent activity exemplifies a maturing threat profile, as the group integrates its established methodologies with refined mechanisms for operational persistence," Unit 42 said. "By diversifying its development pipeline to include modern coding languages like Rust and AI-assisted workflows, the group creates parallel tracks that ensure the redundancy needed to sustain a high operational tempo."