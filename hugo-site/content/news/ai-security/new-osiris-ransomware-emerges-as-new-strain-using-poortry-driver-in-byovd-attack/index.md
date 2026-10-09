---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T20:15:12.803720+00:00'
exported_at: '2026-01-22T20:15:15.059237+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html
structured_data:
  about: []
  author: ''
  description: Experts uncovered a new Osiris ransomware strain that used a custom
    POORTRY driver in a BYOVD attack to disable security tools & steal data in 2025.
  headline: New Osiris Ransomware Emerges as New Strain Using POORTRY Driver in BYOVD
    Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Osiris Ransomware Emerges as New Strain Using POORTRY Driver in BYOVD Attack
updated_at: '2026-01-22T20:15:12.803720+00:00'
url_hash: 2abb5f515c384b9ad866f6ed51793cdef397f561
---

Cybersecurity researchers have disclosed details of a new ransomware family called
**Osiris**
that targeted a major food service franchisee operator in Southeast Asia in November 2025.

The attack leveraged a malicious driver called
[POORTRY](https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html)
as part of a known technique referred to as bring your own vulnerable driver (BYOVD) to disarm security software, the Symantec and Carbon Black Threat Hunter Team said.

It's worth noting that Osiris is assessed to be a brand-new ransomware strain, sharing no similarities with
[another variant](https://www.tripwire.com/state-of-security/osiris-locky-ransomware-afterlife-files)
of the
[same name](https://www.acronis.com/en/blog/posts/osiris-ransomware-new-addition-locky-family/)
that emerged in December 2016 as an iteration of the Locky ransomware. It's currently not known who the developers of the locker are, or if it's advertised as a ransomware-as-a-service (RaaS).

However, the Broadcom-owned cybersecurity division said it identified clues that suggest the threat actors who deployed the ransomware may have been previously associated with
[INC ransomware](https://thehackernews.com/2024/09/microsoft-warns-of-new-inc-ransomware.html)
(aka Warble).

"A wide range of living off the land and dual-use tools were used in this attack, as was a malicious POORTRY driver, which was likely used as part of a bring your own vulnerable driver (BYOVD) attack to disable security software," the company
[said](https://www.security.com/threat-intelligence/new-ransomware-osiris)
in a report shared with The Hacker News.

"The exfiltration of data by the attackers to Wasabi buckets, and the use of a version of Mimikatz that was previously used, with the same filename (kaz.exe), by attackers deploying the INC ransomware, point to potential links between this attack and some attacks involving INC."

Described as an "effective encryption payload" that's likely wielded by experienced attackers, Osiris makes use of a hybrid encryption scheme and a unique encryption key for each file. It's also flexible in that it can stop services, specify which folders and extensions need to be encrypted, terminate processes, and drop a ransom note.

By default, it's designed to kill a long list of processes and services related to Microsoft Office, Exchange, Mozilla Firefox, WordPad, Notepad, Volume Shadow Copy, and Veeam, among others.

First signs of malicious activity on the target's network involved the exfiltration of sensitive data using Rclone to a Wasabi cloud storage bucket prior to the ransomware deployment. Also utilized in the attack were a number of dual-use tools like Netscan, Netexec, and MeshAgent, as well as a custom version of the Rustdesk remote desktop software.

POORTRY is a little different from traditional BYOVD attacks in that it uses a bespoke driver expressly designed for elevating privileges and terminating security tools, as opposed to deploying a legitimate-but-vulnerable driver to the target network.

"KillAV, which is a tool used to deploy vulnerable drivers for terminating security processes, was also deployed on the target's network," the Symantec and Carbon Black Threat Hunter Team noted. "RDP was also enabled on the network, likely to provide the attackers with remote access."

The development comes as ransomware remains a significant enterprise threat, with the landscape constantly shifting as some groups close their doors and others quickly rise from their ashes or move in to take their place. According to an analysis of data leak sites by Symantec and Carbon Black, ransomware actors claimed a total of 4,737 attacks during 2025, up from 4,701 in 2024, a 0.8% increase.

The
[most active](https://cyble.com/blog/ransomware-groups-july-2025-attacks/)
players during the past year were Akira (aka Darter or Howling Scorpius), Qilin (aka Stinkbug or Water Galura), Play (aka Balloonfly), INC, SafePay, RansomHub (aka Greenbottle), DragonForce (aka Hackledorb), Sinobi, Rhysida, and CACTUS. Some of the other notable developments in the space are listed below -

* Threat actors using the Akira ransomware have leveraged a
  [vulnerable Throttlestop driver](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html)
  , along with the Windows CardSpace User Interface Agent and Microsoft Media Foundation Protected Pipeline, to sideload the
  [Bumblebee](https://thehackernews.com/2024/02/bumblebee-malware-returns-with-new.html)
  loader in attacks observed in mid-to-late 2025.
* Akira ransomware campaigns have also
  [exploited](https://reliaquest.com/blog/threat-spotlight-akira-ransomwares-sonicwall-campaign-creates-enterprise-m&a-risk)
  SonicWall SSL VPNs to breach small- to medium-sized business environments during mergers and acquisitions and ultimately obtain access to the bigger, acquiring enterprises. Another Akira attack has been
  [found](https://unit42.paloaltonetworks.com/fake-captcha-to-compromise/)
  to leverage
  [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
  -style CAPTCHA verification lures to drop a .NET remote access trojan called
  [SectopRAT](https://thehackernews.com/2025/07/hackers-use-leaked-shellter-tool.html)
  , which serves as a conduit for remote control and ransomware delivery.
* LockBit (aka Syrphid), which
  [partnered](https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html)
  with DragonForce and Qilin in October 2025, has continued to
  [maintain its infrastructure](https://flare.io/learn/resources/blog/inside-lockbit-5-0/)
  despite a
  [law enforcement operation](https://thehackernews.com/2024/02/lockbit-ransomware-group-resurfaces.html)
  to shut down its operations in early 2024. It has also released variants of
  [LockBit 5.0](https://asec.ahnlab.com/ko/91834/)
  targeting multiple operating systems and virtualization platforms. A significant update to LockBit 5.0 is the
  [introduction](https://flashpoint.io/blog/lockbit-5-0-analysis-technical-deep-dive-into-the-raas-giants-latest-upgrade/)
  of a two-stage ransomware deployment model that separates the loader from the main payload, while simultaneously maximizing evasion, modularity, and destructive impact.
* A new RaaS operation dubbed
  [Sicarii](https://research.checkpoint.com/2026/sicarii-ransomware-truth-vs-myth/)
  has claimed only one victim since it first surfaced in late 2025. While the group explicitly identifies itself as Israeli/Jewish, analysis has uncovered that underground online activity is primarily carried out in Russian and that the Hebrew content shared by the threat actor contains grammatical and semantic errors. This has raised the possibility of a false flag operation. Sicarii's primary Sicarii operator uses the Telegram account "@Skibcum."
* The threat actor known as
  [Storm-2603](https://www.sophos.com/en-us/blog/gold-salem-tradecraft-for-deploying-warlock-ransomware)
  (aka CL-CRI-1040 or Gold Salem) has been observed leveraging the legitimate
  [Velociraptor](https://thehackernews.com/2025/10/hackers-turn-velociraptor-dfir-tool.html)
  digital forensics and incident response (DFIR) tool as part of precursor activity leading to the deployment of Warlock, LockBit, and Babuk ransomware. The attacks have also utilized two drivers ("rsndispot.sys" and "kl.sys") along with "vmtools.exe" to disable security solutions using a BYOVD attack.
* Entities in India, Brazil, and Germany have been
  [targeted](https://www.acronis.com/en/tru/posts/makop-ransomware-guloader-and-privilege-escalation-in-attacks-against-indian-businesses/)
  by
  [Makop](https://thehackernews.com/2025/08/weekly-recap-badcam-attack-winrar-0-day.html)
  ransomware attacks that exploit exposed and insecure RDP systems to stage tools for network scanning, privilege escalation, disabling security software, credential dumping, and ransomware deployment. The attacks, besides using "hlpdrv.sys" and "ThrottleStop.sys" drivers for BYOVD attacks, also deploy GuLoader to deliver the ransomware payload. This is the first documented case of Makop being distributed via a loader.
* Ransomware attacks have also
  [obtained](https://thedfirreport.com/2025/11/17/cats-got-your-files-lynx-ransomware/)
  initial access using already-compromised RDP credentials to perform reconnaissance, privilege escalation, lateral movement via RDP, followed by exfiltrating data to temp[.]sh on day six of the intrusion and
  [deploying](https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html)
  [Lynx ransomware](https://www.group-ib.com/blog/cat-s-out-of-the-bag-lynx-ransomware/)
  three days later.
* A security flaw in the encryption process associated with the
  [Obscura ransomware](https://www.coveware.com/blog/2025/11/18/obscura-ransomware-data-loss-validation)
  has been found to render large files unrecoverable. "When it encrypts large files, it fails to write the encrypted temporary key to the file's footer," Coveware said. "For files over 1GB, that footer is never created at all — which means the key needed for decryption is lost. These files are permanently unrecoverable."
* A new ransomware family named
  [01flip](https://unit42.paloaltonetworks.com/new-ransomware-01flip-written-in-rust/)
  has targeted a limited set of victims in the Asia-Pacific region. Written in Rust, the ransomware can target both Windows and Linux systems. Attack chains involve the exploitation of known security vulnerabilities (e.g., CVE-2019-11580) to obtain a foothold into target networks. It has been attributed to a financially motivated threat actor known as CL-CRI-1036.

To protect against targeted attacks, organizations are advised to monitor the use of dual-use tools, restrict access to RDP services, enforce multi-factor authentication (2FA), use application allowlisting where applicable, and implement off-site storage of backup copies.

"While attacks involving encrypting ransomware remain as prevalent as ever and still pose a threat, the advent of new types of encryptionless attacks adds another degree of risk, creating a wider extortion ecosystem of which ransomware may become just one component," Symantec and Carbon Black
[said](https://www.security.com/threat-intelligence/ransomware-extortion-epidemic)
.