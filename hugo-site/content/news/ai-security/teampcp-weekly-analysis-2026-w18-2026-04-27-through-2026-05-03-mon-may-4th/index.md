---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-04T18:15:14.698285+00:00'
exported_at: '2026-05-04T18:15:16.990913+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32950
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03),
    Author: Kenneth Hartman'
  headline: 'TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03), (Mon,
    May 4th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32950
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03), (Mon, May
  4th)'
updated_at: '2026-05-04T18:15:14.698285+00:00'
url_hash: 1dc9c175c821081581059fd528fdaf6f724ab58b
---

# [TeamPCP Weekly Analysis: 2026-W18 (2026-04-27 through 2026-05-03)](/forums/diary/TeamPCP+Weekly+Analysis+2026W18+20260427+through+20260503/32950/)

**Published**
: 2026-05-04.
**Last Updated**
: 2026-05-04 17:12:18 UTC

**by**
[Kenneth Hartman](/handler_list.html#kenneth-hartman)
(Version: 1)

[0 comment(s)](/diary/TeamPCP+Weekly+Analysis+2026W18+20260427+through+20260503/32950/#comments)

## Summary

The most significant development of the week was the April 29 to 30 Mini Shai-Hulud worm, a self-propagating supply chain campaign that compromised four official SAP npm packages, two PyTorch Lightning PyPI versions, two intercom-client npm versions, and the intercom-php Packagist package across three package ecosystems. OX Security tracked roughly 1,800 GitHub repositories created with stolen credentials by the worm during the two day campaign, and Wiz attributed the operation to TeamPCP at high confidence based on a shared RSA public key with the prior Bitwarden CLI and Checkmarx KICS operations. Reporting suggests the campaign has now demonstrated cross-ecosystem worm propagation in production (npm to PyPI to Packagist), realizing the theoretical CanisterSprawl-style ecosystem-jump risk flagged in the W17 weekly. Separately, Check Point Research disclosed on April 27 to 28 that TeamPCP's extortion partner Vect ships a ChaCha20-IETF nonce-reuse flaw that effectively turns Vect 2.0 into a data wiper for any file larger than 128 KB, a finding analysts assess materially weakens the credibility of TeamPCP's Trivy-credential-trove monetization channel.

## Dated event log

* 2026-04-27: Check Point Research published "VECT: Ransomware by design, Wiper by accident", a primary technical analysis of TeamPCP-affiliated extortion partner Vect 2.0. Check Point documents that Vect's encryption routine reuses a single ChaCha20-IETF nonce buffer across each 128 KB chunk; only the last nonce written to disk is recoverable, so any file larger than 131,072 bytes (VM disks, databases, document stores) is permanently destroyed even if the ransom is paid. The report ships six SHA-256 hashes for Vect Windows, Linux, and ESXi variants, and confirms the prior Vect-TeamPCP partnership announcement on BreachForums targeting the Trivy, LiteLLM, Telnyx, Checkmarx, and European Commission credential pools. Source: Check Point Research,
  <https://research.checkpoint.com/2026/vect-ransomware-by-design-wiper-by-accident/>
  .
* 2026-04-28: BleepingComputer, The Register, and HelpNetSecurity independently covered the Vect 2.0 wiper-bug disclosure within 24 hours of Check Point's report. Each outlet emphasized that paying the ransom does not recover files larger than 128 KB and that the bug is operationally indistinguishable from a deliberate wiper for the most valuable data classes. No public Vect operator response was identified. Source: BleepingComputer,
  <https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/>
  and The Register,
  <https://www.theregister.com/2026/04/28/dont_pay_vect_a_ransom/>
  and HelpNetSecurity,
  <https://www.helpnetsecurity.com/2026/04/29/vect-ransomware-bug/>
  .
* 2026-04-28: CISA added CVE-2024-1708 (ConnectWise ScreenConnect path traversal, exploited by Kimsuky) and CVE-2026-32202 (Microsoft Windows Shell spoofing, no specific threat actor identified in the KEV entry) to the KEV catalog. Neither addition is TeamPCP-related; the entry is logged here to document that the federal silence on TeamPCP-tied artifacts continued into W18 despite the W17 cascade. Source: CISA,
  <https://www.cisa.gov/news-events/alerts/2026/04/28/cisa-adds-two-known-exploited-vulnerabilities-catalog>
  .
* 2026-04-29: Four official SAP npm packages were poisoned between approximately 09:55 and 12:14 UTC: mbt 1.2.48, @cap-js/db-service 2.10.1, @cap-js/postgres 2.2.2, and @cap-js/sqlite 2.2.2. Combined weekly downloads exceed 500,000 across SAP's Cloud Application Programming (CAP) model and Cloud MTA build tooling. The malicious preinstall hook downloads the Bun runtime from the legitimate oven-sh GitHub release path and executes execution.js, an obfuscated information stealer that targets npm and GitHub tokens, SSH keys, AWS, Azure, and GCP credentials, Kubernetes configs, CI/CD secrets, and environment variables. The malware uniquely weaponizes .claude/settings.json and .vscode/tasks.json for AI coding agent persistence, which Wiz characterizes as the first observed supply chain attack to target AI coding agent configurations. Command and control resolves to the malicious endpoint hxxps://zero[.]masscan[.]cloud:443/v1/telemetry. Wiz attributes the operation to TeamPCP at high confidence based on a shared RSA public key with the Bitwarden and Checkmarx operations, a Russian-locale evasion check ("Exiting as russian language detected!"), and a shared PBKDF2 cipher salt ("ctf-scramble-v2", 200,000 iterations) consistent with prior TeamPCP malware. Source: Wiz Blog,
  <https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm>
  and Socket,
  <https://socket.dev/blog/sap-cap-npm-packages-supply-chain-attack>
  and StepSecurity,
  <https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared>
  and BleepingComputer,
  <https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/>
  .
* 2026-04-30: The Mini Shai-Hulud worm spread from the SAP npm compromise into PyTorch Lightning (PyPI versions 2.6.2 and 2.6.3, approximately 2.1 million weekly downloads) and intercom-client (npm versions 7.0.4 and 7.0.5, approximately 300,000 weekly downloads). OX Security tracked the running count of stolen-credential GitHub repositories from approximately 1,200 (post-SAP wave) to 1,800 by April 30. The Lightning packages were published April 30; intercom-client's compromise is documented by OX as a downstream effect of its Lightning dependency being infected during a local install, demonstrating live worm propagation through ordinary developer activity. Source: OX Security,
  <https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/>
  and SecurityWeek,
  <https://www.securityweek.com/sap-npm-packages-targeted-in-supply-chain-attack/>
  .
* 2026-04-30: Socket reported that Mini Shai-Hulud also reached Packagist via intercom-php 5.0.2 (over 20.7 million lifetime installs, approximately 285,000 installs per month). The Packagist payload uses Composer's plugin system for install-time execution rather than the npm preinstall hook, and Socket published five SHA-256 hashes plus the same C2 endpoint. This converts the worm's cross-ecosystem capability from theoretical to demonstrated across npm, PyPI, and Packagist within a single 36 hour operational window. Source: Socket,
  <https://socket.dev/blog/mini-shai-hulud-packagist-malicious-intercom-php-package-compromise>
  .
* 2026-04-30: Dark Reading published "TeamPCP Hits SAP Packages With Mini Shai-Hulud Attack", returning TeamPCP to Tier 1 mainstream coverage for the second consecutive week. The article ties the Mini Shai-Hulud worm to the late-2025 Shai-Hulud npm worm lineage and to TeamPCP's prior 2026 Trivy and Checkmarx operations, and lists additional GitHub commit dead-drop strings ("beautifulcastle", "EveryBoiWeBuildIsAWormyBoi") plus the repository description marker "A Mini Shai-Hulud has Appeared". Source: Dark Reading,
  <https://www.darkreading.com/cloud-security/teampcp-sap-packages-mini-shai-hulud>
  .
* 2026-05-01: Five Eyes joint guidance "Careful Adoption of Agentic AI Services" was released by CISA, NSA, ASD ACSC (Australia), CCCS (Canada), NCSC-UK, and NCSC-NZ, with the underlying PDF dated April 30. The document covers supply-chain risk for agentic AI deployments at category level but does not name TeamPCP, UNC6780, Trivy, Checkmarx KICS, Bitwarden CLI, xinference, CanisterSprawl, or Mini Shai-Hulud. It is the only six-nation cyber product of W18. Source: CISA,
  <https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai>
  .
* 2026-05-01: SecurityWeek published "Over 1,800 Hit in Mini Shai-Hulud Attack on SAP, Lightning, Intercom", aggregating the four SAP packages, two Lightning PyPI versions, two intercom-client npm versions, and intercom-php Packagist into a single attributed wave with approximately 1,800 GitHub repositories created from harvested credentials across the two day campaign. Source: SecurityWeek,
  <https://www.securityweek.com/1800-hit-in-mini-shai-hulud-attack-on-sap-lightning-intercom/>
  .
* 2026-05-01: CISA added CVE-2026-31431 (Linux Kernel "Copy Fail" local privilege escalation) to the KEV catalog. Not TeamPCP-related; included to document the second of two W18 KEV updates that did not act on TeamPCP artifacts. Source: CISA,
  <https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog>
  .

## Themes and trends

* Mini Shai-Hulud realized the cross-ecosystem worm risk in production. The W17 weekly's third watch item flagged that CanisterSprawl carried PyPI-jump logic without observed execution. In W18 a separate but TTP-aligned worm (Mini Shai-Hulud) executed a complete three-ecosystem chain (npm SAP packages to PyPI Lightning to Packagist intercom-php) within roughly 36 hours. Reporting suggests this is the first observed instance in this campaign of a single worm payload propagating across three package managers within one operational window. Analysts assess the cross-ecosystem capability is now empirically demonstrated and should be treated as table-stakes for future TeamPCP-attributed supply chain operations rather than a future threat.
* AI coding agent configuration files emerged as a new target surface. Wiz, Socket, and StepSecurity all flag that Mini Shai-Hulud explicitly weaponizes .claude/settings.json and .vscode/tasks.json to gain persistence inside developers' AI coding agents. Reporting suggests this is the first documented supply chain attack to target AI agent configuration as an execution vector, which has direct implications for any organization whose developers run Claude Code, Cursor, Continue, Cline, or similar tools with project-scoped trusted-paths. The choice of these specific files indicates the operators researched AI tool conventions before payload design rather than treating AI agents as incidental.
* TeamPCP's monetization arm took a serious technical hit. Check Point Research's April 27 to 28 disclosure that Vect 2.0 is effectively a wiper for files larger than 128 KB undermines the credibility of TeamPCP's primary extortion channel. Multiple Tier 1 outlets immediately framed the disclosure as "do not pay; recovery is not possible". Vect's victim count remained at 25 throughout W18 with no new TeamPCP-tagged listings, and Guesty data (deadline projected near April 24 in the W17 weekly) was not published. Analysts assess this is the third consecutive instance of TeamPCP-affiliated extortion failing to translate access into observable monetization, and the first instance of a fundamental cryptographic flaw being publicly disclosed in TeamPCP-affiliated tooling.
* Tier 1 coverage held for the second consecutive week. BleepingComputer, SecurityWeek, Dark Reading, The Register, and HelpNetSecurity all carried original W18 reporting on either the Mini Shai-Hulud SAP wave, the Vect wiper-bug disclosure, or both. This is the longest sustained Tier 1 cadence in the campaign since the original Trivy disclosure in March, consistent with the W17 observation that mainstream coverage tracks novel technical events rather than victim disclosures.
* The institutional response gap widened. Mini Shai-Hulud crossed three package ecosystems and named SAP (a Fortune 100 enterprise software vendor) as a victim publisher. Despite this, no CISA standalone advisory, no CISA KEV addition for any TeamPCP artifact, no FBI alert, and no Five Eyes product explicitly naming TeamPCP appeared in W18. The Five Eyes "Careful Adoption of Agentic AI Services" guidance dropped on May 1 and addresses supply-chain risk for AI agents categorically but is conspicuously silent on the TeamPCP campaign that demonstrated AI-agent-config weaponization 48 hours earlier. Analysts assess the gap between the operational tempo of the campaign and the cadence of public-sector response is now the single most striking feature of the campaign.

## Watch items

* Additional Mini Shai-Hulud-attributed package compromises. Wiz, Socket, and StepSecurity all assess that the worm's stolen-token harvest will continue producing downstream compromises for as long as those tokens remain valid. Watch for new SAP, PyTorch Lightning, Intercom, or transitive-dependent package compromises in W19, and for any victim organization that publicly discloses pulling one of the malicious versions during the April 29 to 30 window.
* Mandiant or GTIG attribution statement on Mini Shai-Hulud and on xinference. Wiz claims TeamPCP attribution at high confidence via the shared RSA public key; Socket and StepSecurity hedge to medium confidence based on shared cipher salt and dead-drop string lineage. The xinference question (formal UNC6780 attribution by Mandiant or GTIG) remained unresolved through W18. Watch for any Mandiant, GTIG, or Microsoft Threat Intelligence publication that formalizes attribution for either the Mini Shai-Hulud wave or xinference.
* Vect operator response to the wiper-bug disclosure. Check Point's report fundamentally undercuts Vect's bargaining position. Watch for any Vect statement on the leak site, any patched Vect 2.1 release that fixes the nonce reuse, or any silent operational shift away from Vect toward an alternative TeamPCP-affiliated ransomware operator. A CipherForce return after approximately 70 days of silence would be analytically significant in this context.
* SAP, Lightning AI, and Intercom victim disclosures. Each of the three publisher organizations has stayed publicly quiet beyond noting that a security note was issued. Watch for SEC filings (SAP files Form 6-K), data-protection-authority notifications, or Lightning AI public statements regarding the scope of harvested credentials and the disposition of stolen tokens. The 36 hour cross-ecosystem window means downstream forensic disclosures are likely to materialize on a 7 to 21 day delay.
* CISA standalone TeamPCP advisory. The W18 institutional silence is now the longest such gap in the campaign. Watch for any CISA emergency directive, standalone advisory, KEV addition tied to a TeamPCP artifact, or named-actor product that finally breaks the federal silence. The combination of three-ecosystem worm propagation, AI-agent persistence weaponization, named SAP impact, and a publicly disclosed cryptographic flaw in the affiliated extortion tooling creates substantial pressure for a coordinated federal response in W19.

## Source index

### Tier 1 (major security publications)

* BleepingComputer (SAP npm compromise):
  <https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/>
* BleepingComputer (Vect wiper bug):
  <https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/>
* SecurityWeek (SAP npm):
  <https://www.securityweek.com/sap-npm-packages-targeted-in-supply-chain-attack/>
* SecurityWeek (Mini Shai-Hulud 1,800 repos):
  <https://www.securityweek.com/1800-hit-in-mini-shai-hulud-attack-on-sap-lightning-intercom/>
* Dark Reading (TeamPCP SAP):
  <https://www.darkreading.com/cloud-security/teampcp-sap-packages-mini-shai-hulud>
* Dark Reading (Vect wiper design error):
  <https://www.darkreading.com/threat-intelligence/vect-ransomware-wiper-design-error>
* The Register (Vect wiper):
  <https://www.theregister.com/2026/04/28/dont_pay_vect_a_ransom/>
* The Register (Mini Shai-Hulud):
  <https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/>
* HelpNetSecurity (Vect bug):
  <https://www.helpnetsecurity.com/2026/04/29/vect-ransomware-bug/>
* The Record by Recorded Future: searched, no W18 TeamPCP coverage identified
* Ars Technica: searched, no W18 TeamPCP coverage identified
* CyberScoop: searched, no W18 TeamPCP coverage identified

### Tier 2 (vendor threat intelligence)

* Wiz Blog (Mini Shai-Hulud SAP attribution):
  <https://www.wiz.io/blog/mini-shai-hulud-supply-chain-sap-npm>
* Socket (SAP CAP analysis):
  <https://socket.dev/blog/sap-cap-npm-packages-supply-chain-attack>
* Socket (Packagist intercom-php):
  <https://socket.dev/blog/mini-shai-hulud-packagist-malicious-intercom-php-package-compromise>
* StepSecurity (Mini Shai-Hulud Has Appeared):
  <https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared>
* OX Security (Lightning extension):
  <https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/>
* Check Point Research (Vect wiper analysis):
  <https://research.checkpoint.com/2026/vect-ransomware-by-design-wiper-by-accident/>
* Aviatrix Threat Research Center (SAP npm coverage):
  <https://aviatrix.ai/threat-research-center/official-sap-npm-packages-compromised-to-steal-credentials-2026/>
* Mandiant / Google Threat Intelligence: searched, no W18 TeamPCP publication identified
* Unit 42 (Palo Alto Networks): searched, no W18 TeamPCP publication identified
* Elastic Security Labs: searched, no W18 TeamPCP publication identified
* CrowdStrike Blog: searched, no W18 TeamPCP publication identified
* SentinelOne / SentinelLabs: searched, no W18 TeamPCP publication identified
* Microsoft Security Blog: searched, no W18 TeamPCP publication identified
* Arctic Wolf: searched, no W18 TeamPCP publication identified

### Tier 3 (government or institutional)

* CISA KEV addition (Apr 28, ConnectWise plus Windows, NOT TeamPCP-related):
  <https://www.cisa.gov/news-events/alerts/2026/04/28/cisa-adds-two-known-exploited-vulnerabilities-catalog>
* CISA KEV addition (May 1, Linux LPE, NOT TeamPCP-related):
  <https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog>
* CISA / Five Eyes joint guidance (Agentic AI, May 1, does NOT name TeamPCP):
  <https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai>
* CCCS Canada AL26-009 (Linux Copy Fail, NOT TeamPCP-related):
  <https://www.cyber.gc.ca/en/alerts-advisories/al26-009-vulnerability-affecting-linux-cve-2026-31431>
* ISC SANS diary 32926 (Update 008, internal author, included for completeness):
  <https://isc.sans.edu/diary/32926>
* CERT-EU, FBI / IC3, BSI Germany, Singapore CSA, NCSC UK, ACSC Australia, ENISA: searched, no new W18 TeamPCP-specific advisory identified beyond the prior March advisories of record

### Tier 4 (social and dark web signal)

* ransomware.live Vect tracker (verified by direct fetch on 2026-05-04, victim count steady at 25, no new TeamPCP-tagged listings):
  <https://www.ransomware.live/group/vect>
* ransomware.live CipherForce tracker (verified by direct fetch on 2026-05-04, approximately 70 days dark, 6 victims):
  <https://www.ransomware.live/group/cipherforce>
* @pcpcats X account claim text referenced via SANS diary 32926
  <https://isc.sans.edu/diary/32926>
* BreachForums and DarkForums: searched indirectly via aggregator services, no W18-window TeamPCP-specific posts surfaced

Keywords:
[npm](/tag.html?tag=npm)
[TeamPCP](/tag.html?tag=TeamPCP)
[supply chain attack](/tag.html?tag=supply chain attack)
[Mini ShaiHulud](/tag.html?tag=Mini ShaiHulud)
[PyPI](/tag.html?tag=PyPI)
[AI coding agents](/tag.html?tag=AI coding agents)

[0 comment(s)](/diary/TeamPCP+Weekly+Analysis+2026W18+20260427+through+20260503/32950/#comments)

Click
[HERE](https://www.sans.org/profiles/kenneth-g-hartman)
to learn more about classes Kenneth is teaching for SANS

* [previous](/diary/32948)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)