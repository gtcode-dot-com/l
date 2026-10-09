---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-16T20:15:14.151670+00:00'
exported_at: '2026-04-16T20:15:16.390599+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/newly-discovered-powmix-botnet-hits.html
structured_data:
  about: []
  author: ''
  description: PowMix targets Czech workforce since Dec 2025 using jittered C2 and
    ZIP phishing, enabling stealthy remote access and persistence.
  headline: Newly Discovered PowMix Botnet Hits Czech Workers Using Randomized C2
    Traffic
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/newly-discovered-powmix-botnet-hits.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Newly Discovered PowMix Botnet Hits Czech Workers Using Randomized C2 Traffic
updated_at: '2026-04-16T20:15:14.151670+00:00'
url_hash: 13c973aeafb90253c9157f5a96fd486fa621c61b
---

**

Ravie Lakshmanan
**

Apr 16, 2026

Botnet / Cryptomining

Cybersecurity researchers have warned of an active malicious campaign that's targeting the workforce in the Czech Republic with a previously undocumented botnet dubbed
**PowMix**
since at least December 2025.

"PowMix employs randomized command-and-control (C2) beaconing intervals, rather than persistent connection to the C2 server, to evade the network signature detections," Cisco Talos researcher Chetan Raghuprasad
[said](https://blog.talosintelligence.com/powmix-botnet-targets-czech-workforce/)
in a report published today.

"PowMix embeds the encrypted heartbeat data along with unique identifiers of the victim machine into the C2 URL paths, mimicking legitimate REST API URLs. PowMix has the capability to remotely update the new C2 domain to the botnet configuration file dynamically."

The attack chain begins with a malicious ZIP file, likely delivered via a phishing email, to activate a multi-stage infection chain that drops PowMix. Specifically, it involves a Windows Shortcut (LNK) that's used to launch a PowerShell loader, which then extracts the malware embedded within the archive, decrypts it, and runs it in memory.

The never-before-seen botnet is designed to facilitate remote access, reconnaissance, and remote code execution, while establishing persistence by means of a scheduled task. At the same time, it verifies the process tree to ensure that another instance of the same malware is not running on the compromised host.

PowMix's remote management logic allows it to process two different kinds of commands sent from the C2 server. Any non #-prefixed response causes PowMix to shift to arbitrary execution mode, and decrypt and run the obtained payload.

* #KILL, to initiate a self-deletion routine and wipe traces of all malicious artifacts
* #HOST, to enable C2 migration to a new server URL.

In parallel, it also opens a decoy document with compliance-themed lures as a distraction mechanism. The lure documents reference legitimate brands like Edeka and include compensation data and valid legislative references, potentially in an effort to enhance their credibility and trick recipients, like job aspirants.

Talos said the campaign shares some level of tactical overlap with a campaign dubbed
[ZipLine](https://thehackernews.com/2025/08/mixshell-malware-delivered-via-contact.html)
that was disclosed by Check Point in late August 2025 as targeting supply chain-critical manufacturing companies with an in-memory malware called MixShell.

This includes the use of the same ZIP-based payload delivery, scheduled task persistence, and the abuse of Heroku for C2. That said, no final payloads have been observed beyond the botnet malware itself, leaving questions about its exact motives unanswered.

"PowMix avoids persistent connections to the C2 server," Talos said. "Instead, it implements a jitter via the Get-Random PowerShell command to vary the beaconing intervals initially between 0 and 261 seconds, and subsequently between 1,075 and 1,450 seconds. This technique attempts to prevent detection of C2 traffic through predictable network signatures."

The disclosure comes as Bitsight sheds light on the infection chain associated with the
[RondoDox](https://thehackernews.com/2026/04/over-1000-exposed-comfyui-instances.html)
botnet, highlighting the malware's evolving capabilities to illicitly mine cryptocurrency on infected systems using XMRig on top of the existing distributed denial-of-service (DDoS) attack functionality.

The findings paint the picture of an actively maintained malware that offers improved evasion, better resilience, aggressive competition removal, and an expanded feature set.

RondoDox is capable of exploiting over 170 known vulnerabilities in various internet-facing applications to obtain initial access and drop a shell script that performs basic anti-analysis and removes competing malware before dropping the appropriate botnet binary for the architecture.

The malware "does multiple checks and implements techniques to hinder analysis, which include the usage of nanomites, renaming/removing files, killing processes, and actively checking for debuggers during execution," Bitsight Principal Research Scientist João Godinho
[said](https://www.bitsight.com/blog/rondodox-botnet-malware-analysis)
.

"The bot is able to run DoS attacks at the internet, transport and application layer, depending on the command and arguments issued by the C2."