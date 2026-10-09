---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:28:49.657739+00:00'
exported_at: '2026-10-03T23:28:50.980507+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html
structured_data:
  about: []
  author: ''
  description: Jade Sleet compromised an Indian IT services provider through a DevOps
    engineer’s MacBook, where FLATROOF and ROOFDECK were detected.
  headline: Jade Sleet Linked to Indian IT Provider Breach With FLATROOF and ROOFDECK
    Backdoors
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Jade Sleet Linked to Indian IT Provider Breach With FLATROOF and ROOFDECK Backdoors
updated_at: '2026-10-03T23:28:49.657739+00:00'
url_hash: d657c58df2d2b77a8dc2667565bc6f948b7d239a
---

**

Ravie Lakshmanan
**

Sep 21, 2026

Malware / Social Engineering

The North Korean threat actor known as
**Jade Sleet**
has been attributed to the compromise of an India-based "much smaller organization" in the information technology (IT) services industry, once again highlighting how the adversary continues to target developers to breach target networks.

Cybersecurity company SentinelOne, which
[disclosed](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)
details of the activity, said it involved the use of Apple macOS backdoors tracked as FLATROOF (aka
[Gaslight](https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html)
) and ROOFDECK, both of which were previously observed in the
[March-April 2026 attack](https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html#state-backed-crypto-heist)
on
[KelpDAO's LayerZero bridge](https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/)
.

Jade Sleet, also tracked under the monikers PUKCHONG, Slow Pisces, TraderTraitor, and UNC4899, has a
[history of targeting](https://thehackernews.com/2025/12/north-korea-linked-hackers-steal-202.html)
the Web3 sector for cryptocurrency heists. In early 2025, the hacking group was
[tied](https://www.nccgroup.com/research/in-depth-technical-analysis-of-the-bybit-hack/)
to the
[theft of about $1.5 billion](https://thehackernews.com/2025/03/safewallet-confirms-north-korean.html)
from Bybit's cold wallet infrastructure following a supply chain compromise of Safe{Wallet}'s developer environment.

"Jade Sleet mostly targets users associated with cryptocurrency and other blockchain-related organizations, but also targets vendors used by those firms," Microsoft-owned GitHub
[noted](https://thehackernews.com/2023/07/north-korean-state-sponsored-hackers.html)
in July 2023.

SentinelOne said the campaign employs social engineering using job interview lures, a common tactic adopted by
[multiple North Korean threat actors](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html)
, to target job seekers from the companies that are breached over the course of the attack. Targeted individuals have been found to work in the DevOps, cryptocurrency, or financial technology space.

"The GitHub repository themes for coding project lures are designed as infrastructure engineering projects related to the company that the DPRK actors are posing as," security researchers Albert Priego, Alex Delamotte, and Matej Havranek said.

Some of the repositories observed are listed below -

* gtn-candidate-repo (used in the KelpDAO incident)
* Northwind-IAC
* novacart-interview
* terraform-candidate-repo

The repositories include a weaponized
[Terraform dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
(".terraform.lock.hcl") pointing to malicious domains (e.g., "registry.hashicorp-aws[.]com") that causes the platform to download attacker-controlled modules when the "
[terraform init](https://developer.hashicorp.com/terraform/cli/commands/init)
" command is run by the unsuspecting developer.

The attack chain culminates in the
[deployment of two Rust-based malware families](https://layerzero.network/publications/kelpdao-incident-report.pdf)
targeting ARM-based macOS systems -

* FLATROOF, a backdoor that uses Telegram for command-and-control (C2) and is capable of command execution, file upload and download, and data theft via a Python module that can collect Chrome, Brave, Firefox, and Safari browser data, Terminal command histories, installed application listings, system hardware and software profile, a snapshot of running processes, and a copy of
  [login.keychain-db](https://attack.mitre.org/techniques/T1555/001/)
* ROOFDECK, a backdoor that uses the
  [Nostr](https://redasgard.com/blog/hunting-lazarus-part5-eleven-hours-on-his-disk)
  protocol for decentralized C2 and is capable of system reconnaissance, file manipulation, remote shell access, lateral movement, and establishing persistence via Launch Agents

"ROOFDECK commands are signed with the operator's private key and their integrity is verified using an embedded public key before execution. The command functionalities are separated into distinct handlers in the source code," SentinelOne said.

"The implant re-implements many common shell commands related to directory and file operations, another tactic often used in more sophisticated North Korea-aligned toolsets, including Lazarus'
[LightlessCan](https://thehackernews.com/2023/09/lazarus-group-impersonates-recruiter.html)
."

The cybersecurity company said its hunt for the two backdoors uncovered an additional unrelated victim, an IT services provider based in India that was compromised through an Apple Silicon MacBook belonging to a DevOps engineer. The backdoors are said to have been detected on the machine as early as March 18, 2026, although the exact delivery mechanism is unknown at this stage.

"They remained dormant until March 29, when beaconing and host activity began," the researchers said. "The implants were first launched by Cursor on March 29, seconds after the cloudshield workspace [~/DevOps-Automation/cloudshield] was opened."

Evidence indicates that ROOFDECK is deployed as a follow-up tool on compromised hosts following the establishment of initial foothold and control. What's more, an updated version of ROOFDECK is said to have been deployed on the DevOps engineer's system on April 20, 2026, a day after
[LayerZero publicly acknowledged](https://layerzero.network/blog/kelpdao-incident-statement)
the KelpDAO hack.

The new variant, besides removing the existing ROOFDECK and FLATROOF binaries, strips symbols and debug information in an attempt to evade detection.

"These groups' initial access efforts include targeting third parties and their software supply chain, which is where much of the industry’s exposure has moved, putting the developer endpoint at the center of the defense," SentinelOne said.

"Endpoints used for development carry access to cloud, pipelines and source code, which makes monitoring and protection a high priority for organizations. These campaigns use purpose-built development environments aimed at one engineer at a time, paired with backdoored Terraform builds that differ for each victim."