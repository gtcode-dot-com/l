---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T19:51:47.815478+00:00'
exported_at: '2026-06-11T19:51:49.965168+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
structured_data:
  about: []
  author: ''
  description: The Gentlemen ransomware claims 478 victims as its AI-assisted RaaS
    operation adds worm-like spread capability.
  headline: The Gentlemen Ransomware Claims 478 Victims, Can Spread Like a Worm
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Gentlemen Ransomware Claims 478 Victims, Can Spread Like a Worm
updated_at: '2026-06-11T19:51:47.815478+00:00'
url_hash: 586671ef848f8bb9c5f39fc9f22ba764189d6398
---

A new analysis of
**The Gentlemen**
operation has revealed that the financially motivated threat group initially operated as an affiliate responsible for conducting double extortion attacks, while
[leveraging resources](https://thehackernews.com/2025/12/weekly-recap-apple-0-days-winrar.html#:~:text=The%20Gentlemen%20Ransomware%20Uses%20BYOVD%20Technique%20in%20Attacks)
from various ransomware-as-a-service (RaaS) schemes like LockBit (aka Tenacious Mantis), Qilin (aka Pestilent Mantis), and Medusa (aka Venomous Mantis).

According to a
[detailed report](https://catalyst.prodaft.com/public/report/inside-the-phantom-mantis-operation/overview)
published by PRODAFT, the group, which it tracks as Phantom Mantis, is led by a Russian-speaking cybercriminal it calls LARVA-368, who goes by the online aliases hastalamuerte, ArmCorp, zeta88, nobody0, and santamuerte.
[The Gentlemen](https://www.trendmicro.com/en_us/research/25/i/unmasking-the-gentlemen-ransomware.html)
is known to be active since March 2025, claiming a total of 478 victims to date, per
[data](https://ransomware.live/group/thegentlemen)
from Ransomware.Live.

"In July 2025, Phantom Mantis transitioned into The Gentlemen, an independent partnership program no longer dependent on other RaaS groups," the Swiss cybersecurity company said. "Additionally, LARVA-368 relies heavily on artificial intelligence for the development and maintenance of ransomware and tools, as well as for assistance with post-exploitation procedures."

As for LARVA-368, the threat actor is assessed to have been a member of the Embargo (aka Primeval Mantis) ransomware group before launching their own operation under the name ArmCorp. It was subsequently rebranded to The Gentlemen four months later.

The individual's identity has since been
[outed](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/)
by cybersecurity journalist Brian Krebs as a 36-year-old Alexander Andreevich Yapaev (Япаев Алексанр Андреевич) from the Russian city of Izhevsk. PRODAFT told The Hacker News that its findings match the same persona with "high confidence."

As
[detailed](https://thehackernews.com/2025/08/weekly-recap-badcam-attack-winrar-0-day.html#:~:text=Ransomware%20Continues%20to%20Evolve)
by Dark Atlas in August 2025, the shift
[coincided](https://thehackernews.com/2026/03/threatsday-bulletin-fortigate-raas.html#emerging-raas-exploiting-fortigate-flaws)
with a payment dispute between LARVA-368 and Qilin, with the threat actor accusing the RaaS operation of carrying out an exit scam and defrauding them of $48,000.

"Although Phantom Mantis was a very active affiliate group with over 20 targets registered on its affiliate panel in less than 30 days, the group's admin (LARVA-368) and LARVA-367 (aka
[DevMan](https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html)
), a former Phantom Mantis's member, claimed that Pestilent Mantis was scamming affiliates and that there was an alleged 'backdoor' within the Pestilent Mantis's affiliate panel victim chats," PRODAFT noted.

"Although we could not confirm these claims, there is a chance that LARVA-368 and LARVA-367 intentionally spread disinformation with the intent of recruiting Pestilent Mantis affiliates to Phantom Mantis by discrediting the group."

Phantom Mantis has also been observed paying for Premium accounts on underground forums to boost their visibility and fend off competition, with the group's communication and the technical support handled by a separate Russian-speaking persona named The Gentlemen Data.

Some of the other salient aspects of the extortion scheme compiled from various reports are as follows -

* In an analysis of the ransomware in late last year, LevelBlue's Cybereason team
  [described](https://www.cybereason.com/blog/the-gentlemen-ransomware)
  The Gentlemen as a "highly adaptive, fast-moving ransomware operation" that combines mature ransomware techniques with RaaS features, double extortion, cross-platform lockers, and flexible propagation, and affiliate support.
* The group has
  [emerged](https://www.halcyon.ai/ransomware-research-reports/threat-assessment-the-gentlemen-ransomware-group)
  as one of the most active threat actors, accounting for 10% of ransomware activity in April 2026. "The Gentlemen follows an enterprise-focused chain beginning with initial access, via vulnerable internet-facing services or stolen credentials," NCC Group
  [said](https://www.nccgroup.com/newsroom/ncc-group-monthly-threat-pulse-review-of-april-2026/)
  . "Analysis suggests The Gentlemen can adapt and change tactics during an attack, such as manipulating GPOs, compromising privileged accounts, and using custom methods to bypass endpoint protections."
* Only about
  [13% of their victims](https://socradar.io/blog/gentlemen-ransomware-leak/)
  are based in the U.S. The majority of the victims are concentrated in Thailand, the U.K., Brazil, Germany, and India.
* LARVA-368 uses The Gentlemen IM app accounts to support affiliates regarding encryption and any intrusion-related issue, such as providing EDR killers to bypass security solutions via the bring your own vulnerable driver (BYOVD) technique.
* Support services for both The Gentlemen and The Gentlemen Data are available via Tox, SimpleX Chat, and Ricochet Refresh open-source messaging platforms.
* Potential affiliates are required to provide the administrator at least 1GB of data exfiltrated from a victim to gain access to the affiliate panel, a tactic designed to prevent researchers and law enforcement authorities from gaining access to the infrastructure under the guise of an affiliate. The affiliate panel supports user management, configuring new targets, and downloading ransomware to a specific target.
* Phantom Mantis provides five versions of ransomware that are designed for Windows, Linux, ESXi, Windows XP+, and Logical Volume Manager (LVM).
* The group courts affiliates with an aggressive profit-sharing model: 90% for affiliates and 10% for the operator.
* Initial access is obtained via edge devices such as VPN appliances, firewalls, and other internet-facing systems, with a specific focus on platforms like Cisco and Fortinet FortiGate.
* Infection chains involve the use of red team utilities like NetExec, RelayKing, TaskHound, PrivHound, and CertiHound to perform Active Directory discovery, certificate abuse, privilege escalation, and file share discovery. A separate set of tools, such as EDRStartupHinder, gfreeze, glinker, and DumpBrowserSecrets, are used for evading security programs, while
  [Velociraptor](https://thehackernews.com/2025/10/hackers-turn-velociraptor-dfir-tool.html)
  is employed for command-and-control (C2).
* The attacks also
  [attempt](https://www.huntress.com/blog/the-gentlemen-ransomware-defense-evasion-ttps)
  to clear System, Application, and Security Windows Event Logs, disable Microsoft Defender, and add antivirus exclusions.
* The ransomware makes use of a
  [hybrid cryptographic scheme](https://falconfeeds.io/blogs/the-gentlemen-russia-raas-operation-rocket-leak-analysis/)
  : X25519 key exchange combined with XChaCha20 symmetric encryption.
* Microsoft, which is tracking the cluster under the moniker Storm-2697, said the ransomware is written in Go and obfuscated with Garble to target the Windows environment. "When enabled with the --spread argument, it turns the malware from a single-host encryptor into a self-propagating worm that attempts to deploy its encryptor to every reachable system on the network," the tech giant
  [said](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/)
  . "If the --wipe argument is provided, The Gentlemen ransomware performs an additional post-encryption routine to eliminate recoverable artifacts from disk."
* According to ZeroFox, the ransomware crew likely runs a multi-channel extortion operation, combining ransomware attacks with email outreach and phone-based pressure tactics targeting victims.
* The group implements a "highly responsive development cycle," an aspect exemplified by the
  [release of a same-day patch](https://www.zerofox.com/reports/the-gentlemen-a-zerofox-intelligence-threat-actor-profile/)
  after a
  [decryptor was released](https://github.com/Bedrock-Safeguard/gentlemen-decryptor)
  in April 2026.
* The average dwell time of an intrusion
  [ranges from two to six weeks](https://redpiranha.net/news/the-gentlemen-ransomware-analysis)
  from initial access to encryption, with the group particularly focusing on organizations running VMware infrastructure.

Last month, a
[leak](https://www.kelacyber.com/blog/the-gentlemen-ransomware-internal-chat-leak-analysis-2026/)
of an
[internal Rocket.Chat database](https://ransom-isac.org/blog/the-gentlemen-leak-analysis/)
used by the group - comprising 3,366 messages between November 2025 to late April 2026 - has
[shed further light](https://www.vectra.ai/blog/from-conti-to-the-gentlemen-tooling-evolved-gaps-didnt)
on the group's inner workings, including its use of known security flaws in VMware Aria Operations, Fortinet, Cisco, and Microsoft software, while painting a picture of a criminal enterprise whose members have a clear division of roles and responsibilities.

"The group actively tracks and evaluates modern vulnerabilities, including
[CVE-2024-55591](https://nvd.nist.gov/vuln/detail/cve-2024-55591)
,
[CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)
, and
[CVE-2025-33073](https://nvd.nist.gov/vuln/detail/CVE-2025-33073)
, and combines them with technique-driven paths like backup and management-controller abuse and NTLM relay workflows, giving them a flexible exploitation pipeline," Check Point
[said](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)
.

That's not all. In March 2026, Hunt.io
[said](https://hunt.io/blog/thegentlemen-ransomware-toolkit-russian-proton66-server)
it discovered an open directory hosted at "176.120.22[.]127:80" on the Russian bulletproof hosting provider
[Proton66](https://thehackernews.com/2025/06/blind-eagle-uses-proton66-hosting-for.html)
that exposed 126 files containing a complete ransomware operator toolkit attributed to a The Gentlemen RaaS affiliate.

This included tools for reconnaissance, privilege escalation, defense evasion, credential theft, lateral movement, persistence, and pre-encryption preparation, essentially spanning all phases of the intrusion lifecycle.

"LARVA-368 is a threat actor specializing in extortion-related activities and has been active since at least 2020," PRODAFT said. "The expertise acquired through previous collaborations with various RaaS groups provided the technical foundation necessary to establish The Gentlemen RaaS."