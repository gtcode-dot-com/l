---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T06:07:52.672655+00:00'
exported_at: '2026-02-26T06:07:55.642781+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/slh-offers-5001000-per-call-to-recruit.html
structured_data:
  about: []
  author: ''
  description: SLH pays $500–$1,000 per call to recruit women for vishing, targeting
    IT help desks and MFA resets to breach Azure and deploy ransomware.
  headline: SLH Offers $500–$1,000 Per Call to Recruit Women for IT Help Desk Vishing
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/slh-offers-5001000-per-call-to-recruit.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: SLH Offers $500–$1,000 Per Call to Recruit Women for IT Help Desk Vishing Attacks
updated_at: '2026-02-26T06:07:52.672655+00:00'
url_hash: 474f55a13f012e85b2b919605e56a55ff516ce87
---

**

Ravie Lakshmanan
**

Feb 25, 2026

Social Engineering / Cloud Security

The notorious cybercrime collective known as
**Scattered LAPSUS$ Hunters**
(SLH) has been observed offering financial incentives to recruit women to pull off social engineering attacks.

The idea is to hire them for voice phishing campaigns targeting IT help desks, Dataminr said in a new threat brief. The group is said to be offering anywhere between $500 and $1,000 upfront per call, in addition to providing them with the necessary pre-written scripts to carry out the attack.

"SLH is diversifying its social engineering pool by specifically recruiting women to conduct vishing attacks, likely to increase the success rate of help desk impersonation," the threat intelligence firm
[said](https://www.dataminr.com/resources/intel-brief/slh-recruiting-women-for-vishing/)
.

A
[high-profile cybercrime supergroup](https://thehackernews.com/2025/08/cybercrime-groups-shinyhunters.html)
comprising LAPSUS$, Scattered Spider, and ShinyHunters, SLH has a record of engaging in advanced social engineering attacks to sidestep multi-factor authentication (MFA) through techniques like
[MFA prompt bombing](https://www.silverfort.com/glossary/mfa-prompt-bombing/)
and SIM swapping.

The group's modus operandi also involves targeting help desks and call centers to breach companies by posing as employees and convincing them to reset a password or install a remote monitoring and management (RMM) tool that grants them remote access. Once initial access is obtained, Scattered Spider has been
[observed](https://thehackernews.com/2025/06/fbi-warns-of-scattered-spiders.html)
moving laterally to virtualized environments, escalating privileges, and exfiltrating sensitive corporate data.

Some of these attacks have further led to the deployment of ransomware. Another hallmark of these attacks is the
[use of legitimate services and residential proxy networks](https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile)
(e.g., Luminati and OxyLabs) to blend in and evade detection. Scattered Spider actors have used various tunneling tools like Ngrok, Teleport, and Pinggy, as well as free file-sharing services such as file.io, gofile.io, mega.nz, and transfer.sh.

|  |
| --- |
|  |
| SLH's Telegram post to recruit women |

In a report published earlier this month, Palo Alto Networks Unit 42, which is tracking Scattered Spider under the moniker Muddled Libra, described the threat actor as "highly proficient at exploiting human psychology" by impersonating employees to attempt password and multi-factor authentication (MFA) resets.

|  |
| --- |
|  |
| Scattered Spider attack chain |

In at least one case investigated by the cybersecurity company in September 2025, Scattered Spider is said to have created and utilized a virtual machine (VM) after obtaining privileged credentials by calling the IT help desk and then used it to conduct reconnaissance (e.g., Active Directory enumeration) and attempt to exfiltrate Outlook mailbox files and data downloaded from the target's Snowflake database.

"While focusing on identity compromise and social engineering, this threat actor leverages legitimate tools and existing infrastructure to blend in," Unit 42
[said](https://unit42.paloaltonetworks.com/muddled-libra-ops-playbook/)
. "They operate quietly and maintain persistence."

The cybersecurity company also
[noted](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)
that Scattered Spider has an "extensive history" of targeting Microsoft Azure environments using the Graph API to facilitate access to Azure cloud resources. Also put to use by the group are cloud enumeration tools such as ADRecon for Active Directory reconnaissance.

With social engineering emerging as the primary entry point for the cybercrime group, organizations are advised to be on alert and train IT help desk and support personnel to watch out for pre-written scripts and polished voice impersonation, enforce strict identity verification, harden MFA policies by shifting away from SMS-based authentication, and audit logs for new user creation or administrative privilege escalation following help desk interactions.

"This recruitment drive represents a calculated evolution in SLH's tactics," Dataminr said. "By specifically seeking female voices, the group likely aims to bypass the 'traditional' profiles of attackers that IT help desk staff may be trained to identify, thereby increasing the effectiveness of their impersonation efforts."