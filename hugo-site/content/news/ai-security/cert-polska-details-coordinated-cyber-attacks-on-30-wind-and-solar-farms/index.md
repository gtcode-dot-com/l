---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-31T08:15:16.860089+00:00'
exported_at: '2026-01-31T08:15:19.573173+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/poland-attributes-december-cyber.html
structured_data:
  about: []
  author: ''
  description: Poland linked December 2025 cyber attacks on energy and manufacturing
    sites to Static Tundra, involving DynoWiper and FortiGate exploits.
  headline: CERT Polska Details Coordinated Cyber Attacks on 30+ Wind and Solar Farms
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/poland-attributes-december-cyber.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: CERT Polska Details Coordinated Cyber Attacks on 30+ Wind and Solar Farms
updated_at: '2026-01-31T08:15:16.860089+00:00'
url_hash: 80b116b8e8a0e32c174a6b63755eb09ad5c88240
---

**

Ravie Lakshmanan
**

Jan 31, 2026

Network Security / SCADA

CERT Polska, the Polish computer emergency response team, revealed that coordinated cyber attacks targeted more than 30 wind and photovoltaic farms, a private company from the manufacturing sector, and a large combined heat and power plant (CHP) supplying heat to almost half a million customers in the country.

The incident took place on December 29, 2025. The agency has attributed the attacks to a threat cluster dubbed
[Static Tundra](https://thehackernews.com/2025/08/fbi-warns-russian-fsb-linked-hackers.html)
, which is also tracked as Berserk Bear, Blue Kraken, Crouching Yeti, Dragonfly, Energetic Bear, Ghost Blizzard (formerly Bromine), and Havex. Static Tundra is assessed to be linked to Russia's Federal Security Service's (FSB) Center 16 unit.

It's worth noting that recent reports from
[ESET](https://thehackernews.com/2026/01/new-dynowiper-malware-used-in-attempted.html)
and
[Dragos](https://thehackernews.com/2026/01/russian-electrum-tied-to-december-2025.html)
attributed the activity with moderate confidence to a different Russian state-sponsored hacking group known as Sandworm.

"All attacks had a purely destructive objective," CERT Polska
[said](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/)
in a report published Friday. "Although attacks on renewable energy farms disrupted communication between these facilities and the distribution system operator, they did not affect the ongoing production of electricity. Similarly, the attack on the combined heat and power plant did not achieve the attacker's intended effect of disrupting heat supply to end users."

The attackers are said to have gained access to the internal network of power substations associated with a renewable energy facility to carry out reconnaissance and disruptive activities, including damaging the firmware of controllers, deleting system files, or launching custom-built wiper malware codenamed DynoWiper by ESET.

In the intrusion aimed at the CHP, the adversary engaged in long-term data theft dating all the way back to March 2025 that enabled them to escalate privileges and move laterally across the network. The attackers' attempts to detonate the wiper malware were unsuccessful, CERT Polska noted.

On the other hand, the targeting of the manufacturing sector company is believed to be opportunistic, with the threat actor gaining initial access via a vulnerable Fortinet perimeter device. The attack targeting the grid connection point is also likely to have involved the exploitation of a vulnerable FortiGate appliance.

At least four different versions of DynoWiper have been discovered to date. These variants were deployed on Mikronika HMI Computers used by the energy facility and on a network share within the CHP after securing access through the SSL‑VPN portal service of a FortiGate device.

"The attacker gained access to the infrastructure using multiple accounts that were statically defined in the device configuration and did not have two‑factor authentication enabled," CERT Polska said, detailing the actor's modus operandi targeting the CHP. "The attacker connected using Tor nodes, as well as Polish and foreign IP addresses, which were often associated with compromised infrastructure."

The wiper's functionality is fairly straightforward -

* Initialization that involves seeding a pseudorandom number generator (PRNG) called
  [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)
* Enumerate files and corrupt them using the PRNG
* Delete files

It's worth mentioning here that the malware does not have a persistence mechanism, a way to communicate with a command‑and‑control (C2) server, or execute shell commands. Nor does it attempt to hide the activity from security programs.

CERT Polska said the attack targeting the manufacturing sector company involved the use of a PowerShell-based wiper dubbed LazyWiper that scripts overwrites files on the system with pseudorandom 32‑byte sequences to render them unrecoverable. It's suspected that the core wiping functionality was developed using a large language model (LLM).

"The malware used in the incident involving renewable energy farms was executed directly on the HMI machine," CERT Polska pointed out. "In contrast, in the CHP plant (DynoWiper) and the manufacturing sector company (LazyWiper), the malware was distributed within the Active Directory domain via a PowerShell script executed on a domain controller."

The agency also described some of the code-level similarities between DynoWiper and other wipers built by Sandworm as "general" in nature and does not offer any concrete evidence as to whether the threat actor participated in the attack.

"The attacker used credentials obtained from the on‑premises environment in attempts to gain access to cloud services," CERT Polska said. "After identifying credentials for which corresponding accounts existed in the M365 service, the attacker downloaded selected data from services such as Exchange, Teams, and SharePoint."

"The attacker was particularly interested in files and email messages related to OT network modernization, SCADA systems, and technical work carried out within the organizations."