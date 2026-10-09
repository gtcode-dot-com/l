---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-18T03:01:10.633185+00:00'
exported_at: '2026-03-18T03:01:14.044370+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/leaknet-ransomware-uses-clickfix-via.html
structured_data:
  about: []
  author: ''
  description: LeakNet uses ClickFix via compromised sites to gain access, enabling
    stealth attacks and scalable ransomware operations.
  headline: LeakNet Ransomware Uses ClickFix via Hacked Sites, Deploys Deno In-Memory
    Loader
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/leaknet-ransomware-uses-clickfix-via.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: LeakNet Ransomware Uses ClickFix via Hacked Sites, Deploys Deno In-Memory Loader
updated_at: '2026-03-18T03:01:10.633185+00:00'
url_hash: 2e7b83a2566b10a372eec8b2e5243e49b310ada0
---

The ransomware operation known as
**LeakNet**
has adopted the
[ClickFix](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html)
social engineering tactic delivered through compromised websites as an initial access method.

The use of ClickFix, where users are tricked into manually running malicious commands to address non-existent errors, is a departure from relying on traditional methods for obtaining initial access, such as through stolen credentials acquired from initial access brokers (IABs), ReliaQuest
[said](https://reliaquest.com/blog/threat-spotlight-casting-a-wider-net-clickfix-deno-and-leaknets-scaling-threat)
in a technical report published today.

The second important aspect of these attacks is the use of a staged command-and-control (C2) loader built on the Deno JavaScript runtime to execute malicious payloads directly in memory.

"The key takeaway here is that both entry paths lead to the same repeatable post-exploitation sequence every time," the cybersecurity company said. "That gives defenders something concrete to work with: known behaviors you can detect and disrupt at each stage, well before ransomware deployment, regardless of how LeakNet got in."

LeakNet first emerged in
[November 2024](https://www.watchguard.com/wgrd-security-hub/ransomware-tracker/leaknet)
,
[describing](https://x.com/ido_cohen2/status/1957353482089877838)
itself as a "digital watchdog" and framing its activities as focused on internet freedom and transparency. According to data captured by
[Dragos](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2025)
, the group has also
[targeted](https://redpiranha.net/news/threat-intelligence-report-august-19-august-25-2025)
industrial entities.

The use of ClickFix to breach victims offers several advantages, the most significant being that it reduces dependence on third-party suppliers, lowers per-victim acquisition cost, and removes the operational bottleneck of waiting for valuable accounts to hit the market.

In these attacks, the legitimate-but-compromised sites are used to serve fake CAPTCHA verification checks that instruct users to copy and paste a "msiexec.exe" command to the Windows Run dialog. The attacks are not confined to a specific industry vertical, instead casting a wide net to infect as many victims as possible.

The development comes as more threat actors are adopting the ClickFix playbook, as it abuses trusted, everyday workflows to entice users into running rogue commands via legitimate Windows tooling in a manner that feels routine and safe.

"LeakNet's adoption of ClickFix marks both the first documented expansion of the group’s initial access capability and a meaningful strategic shift," ReliaQuest said.

"By moving away from IABs, LeakNet removes a dependency that naturally constrained how quickly and broadly it could operate. And because ClickFix is delivered through legitimate—but compromised—websites, it doesn’t present the same obvious signals at the network layer as attacker-owned infrastructure."

Besides the use of ClickFix to initiate the attack chain, LeakNet is assessed to be using a Deno-based loader to execute Base64-encoded JavaScript directly in memory so as to minimize on-disk evidence and evade detection. The payload is designed to fingerprint the compromised system, contact an external server to fetch next-stage malware, and enter into a polling loop that repeatedly fetches and executes additional code through Deno.

Separately, ReliaQuest said it also observed an intrusion attempt in which threat actors used Microsoft Teams-based phishing to socially engineer a user into launching a payload chain that ended in a similar Deno-based loader. While the activity remains unattributed, the use of the bring your own runtime (BYOR) approach either signals a broadening of LeakNet's initial access vectors, or that other threat actors have adopted the technique.

LeakNet's post-compromise activity follows a consistent methodology: it starts with the use of DLL side-loading to launch a malicious DLL delivered via the loader, followed by lateral movement using PsExec, data exfiltration, and encryption.

"LeakNet runs cmd.exe /c klist, a built-in Windows command that displays active authentication credentials on the compromised system. This tells the attacker which accounts and services are already reachable without the need for requesting new credentials, so they can move faster and more deliberately," ReliaQuest said.

"For staging and exfiltration, LeakNet uses S3 buckets, exploiting the appearance of normal cloud traffic to reduce its detection footprint."

The development comes as Google revealed that Qilin (aka Agenda), Akira (aka RedBike), Cl0p, Play, SafePay, INC Ransom, Lynx, RansomHub, DragonForce (aka FireFlame and FuryStorm), and Sinobi emerged as the top 10 ransomware brands with the most victims claimed on their data leak sites.

"In a third of incidents, the initial access vector was confirmed or suspected exploitation of vulnerabilities, most often in common VPNs and firewalls," Google Threat Intelligence Group (GTIG)
[said](https://cloud.google.com/blog/topics/threat-intelligence/ransomware-ttps-shifting-threat-landscape/)
, adding 77% of analyzed ransomware intrusions included suspected data theft, an increase from 57% in 2024.

"Despite ongoing turmoil caused by actor conflicts and disruption, ransomware actors remain highly motivated and the extortion ecosystem demonstrates continued resilience. Several indicators suggest the
[overall profitability of these operations is, however, declining,](https://www.coveware.com/blog/2026/2/3/mass-data-exfiltration-campaigns-lose-their-edge-in-q4-2025)
and at least some threat actors are shifting their targeting calculus away from large companies to instead focus on higher volume attacks against smaller organizations."