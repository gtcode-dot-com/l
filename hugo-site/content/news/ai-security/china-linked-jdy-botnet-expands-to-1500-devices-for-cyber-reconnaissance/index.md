---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T01:52:47.157511+00:00'
exported_at: '2026-06-11T01:52:48.586910+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html
structured_data:
  about: []
  author: ''
  description: JDY grew from 650 to 1,500+ devices after KV-botnet's takedown, enabling
    rapid reconnaissance and vulnerability targeting.
  headline: China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked JDY Botnet Expands to 1,500+ Devices for Cyber Reconnaissance
updated_at: '2026-06-11T01:52:47.157511+00:00'
url_hash: 55101572cae65d12ee8bff5044483c0fd2b026fe
---

Cybersecurity researchers have warned of a "resurgence and expansion" of
**JDY**
, a covert network associated with China-nexus state-sponsored threat actors.

"The JDY botnet comprises over 1,500 SOHO [small office and home office] and IoT devices and operates as a centrally controlled, high-performance scanner used to discover, fingerprint, and continuously map exposed services at scale," Lumen's Black Lotus Labs
[said](https://www.lumen.com/blog/en-us/expanded-jdy-iot-and-soho-botnet-enables-rapid-vulnerability-exploitation)
in a report shared with The Hacker News.

JDY was
[first flagged](https://thehackernews.com/2023/12/new-kv-botnet-targeting-cisco-draytek.html)
as a cluster within another botnet codenamed KV-botnet in mid-December 2023. Primarily used for broader scanning against internet targets, the stealthy network comprising compromised SOHO routers, firewalls, and IoT devices has been put to use by Chinese hacking groups like Volt Typhoon.

Following KV-botnet's
[takedown](https://thehackernews.com/2024/02/us-feds-shut-down-china-linked-kv.html)
by the U.S. government in early 2024, the botnet operators began making
[behavioral changes](https://thehackernews.com/2024/02/after-fbi-takedown-kv-botnet-operators.html)
to the network, with the second KV cluster largely going offline. It's suspected that the botnet is offered by the operators to various hacking outfits, while carrying out reconnaissance and targeting on their own.

The latest findings from Black Lotus Labs show that the malware has expanded in scope to infect a broader range of devices and act as a conduit to feed "structured reconnaissance data" into a larger scanning ecosystem for follow-on target identification and exploitation.

Specifically, the JDY cluster is being used to conduct targeted scanning and service fingerprinting with an aim to flag vulnerable infrastructure following public disclosures. This points to an industrialized reconnaissance effort, the results of which are leveraged by Chinese nation-state groups.

This has been complemented by a growth in the botnet's size, which has surged from 650 bots at the start of January 2024 to more than 1,500 compromised devices. Most of the hacked nodes are located in the U.S. and Brazil, followed by Europe and Asia.

Where previously the cluster primarily featured Cisco RV320 and RV325 routers, the present makeup of the botnet is a lot more diverse, including devices from Araknis, Mimosa Networks, Ubiquiti, Draytek, Hikvision, and Linksys.

"The botnet's large number of U.S.-based SOHO/IoT devices enables the botnet operators to evade defenses and traditional IP-based controls, such as geofencing, IP reputation-based detection, and static blocklists," Black Lotus Labs said.

"By distributing their scanning and reconnaissance activity across a wide range of IP addresses, the operators make it less likely that any single IP will be labeled as a scanner and blocked. Additionally, using compromised SOHO and IoT devices helps this activity blend in with legitimate user traffic."

The architecture that powers the botnet is best described as layered: the operators use Tor nodes to manage infected infrastructure, including both the command-and-control (C2) and payload servers. The C2 servers direct the bots to perform targeted reconnaissance and system profiling, as opposed to indiscriminate scanning. Results of the scans are sent to central servers for ongoing intelligence gathering in an effort to further Chinese threat actors' objectives.

Attack chains weaponize newly disclosed vulnerabilities in edge devices (e.g., CVE-2026-35616) to deliver a shell script dropper that checks if the malware is already active, and if not, proceeds to download the primary payload based on the detected processor architecture (e.g., mips, mips64, mipsel, or mipsel64). Once the malware is launched, it's deleted from disk.

The malware that facilitates scanning and target reconnaissance is designed to fingerprint the host, receive scanning tasks from a central C2 server, carry out high-volume TCP, SSL, UDP, and ICMP-assisted probing, capture responses (TLS certificates, metadata, etc.), and report the results back to the dispatch server. The goal is to conduct infrastructure reconnaissance rather than exploitation.

A noteworthy functionality of the malware is its ability to adapt its scanning methodology based on its privileges on the local system. If it can open a raw socket, an indication of root privileges, it initiates high-speed
[SYN scanning](https://nmap.org/book/synscan.html)
using custom-crafted TCP packets. If raw sockets are unavailable or if the task is a web scan, the scanning engine resorts to using standard TCP and TLS connections or employs protocols like UDP and ICMP.

This activity most likely informs asset discovery, vulnerability-targeting pipelines, and downstream exploitation or attack-orchestration systems, the cybersecurity company said.

"JDY demonstrates how IoT/SOHO botnets and covert networks of compromised devices are being used for rapid vulnerability exploitation," the company said. "JDY's growth and continued operation illustrate how modern reconnaissance networks persist despite takedowns and adapt as a durable capability within a broader adversary ecosystem."

"JDY's evolution from a supporting component of the KV-botnet to an independent, high-performance reconnaissance capability demonstrates that disruption of individual nodes or clusters does not eliminate the underlying capability. The capability persists, adapts, and continues to provide adversaries with timely targeting data, often within hours of vulnerability disclosure."