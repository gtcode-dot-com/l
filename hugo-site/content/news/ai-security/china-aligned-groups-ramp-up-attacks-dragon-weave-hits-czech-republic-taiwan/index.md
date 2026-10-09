---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T01:58:45.791389+00:00'
exported_at: '2026-06-09T01:58:49.026567+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html
structured_data:
  about: []
  author: ''
  description: Operation Dragon Weave delivers AdaptixC2 via phishing; Azure-based
    AZUREVEIL enables covert control, impacting Czech and Taiwan targets.
  headline: 'China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic
    & Taiwan'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan'
updated_at: '2026-06-09T01:58:45.791389+00:00'
url_hash: 7472cf9d01d2031d8824700f622b794da0ad1616
---

A new cyber espionage campaign codenamed
**Operation Dragon Weave**
has been observed targeting officials and citizens in the Czech Republic and Taiwan to deliver an
[AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
agent.

According to Seqrite Labs, targets of the campaign include government, research, academic, technology, and financial services sectors. The activity entails distributing spear-phishing emails containing ZIP attachments to trigger an infection chain that uses a Rust loader to drop the final payload for data exfiltration and remote control.

"When extracted, the archive contains multiple files that appear legitimate but are actually part of a structured infection chain designed to execute malicious payloads in the background," security researcher Priya Patel
[said](https://www.seqrite.com/blog/operation-dragon-weave-uncovering-a-china-linked-campaign-targeting-czech-republic-and-taiwan-using-azure-cloud-c2/)
.

The attack chain uses two different pathways to launch the final-stage malware. One infection sequence begins when the recipient of the ZIP archive opens a malicious Windows Shortcut (LNK) file that masquerades as a PDF document. This leads to the execution of a PowerShell script that's responsible for extracting an executable ("RuntimeBroker\_update.exe") from an intermediate DAT file and running it.

In the second attack chain, the victim directly launches a binary from the same archive. The binary functions as a self-contained Rust-based dropper to launch "RuntimeBroker\_update.exe." Regardless of the path chosen, the executable loads a malicious DLL ("UnityPlayer.dll") via
[DLL side-loading](https://attack.mitre.org/techniques/T1102/001/)
, resulting in the deployment of a Rust-based loader called RUSTCLOAK.

The loader then decrypts and runs the main payload, an AdaptixC2 agent codenamed AZUREVEIL owing to the use of Microsoft Azure Blob Storage for command-and-control (C2). The loader is designed to perform anti-analysis checks to proceed only if the malware determines that it's being run within a sandboxed environment.

"The malware just talks to Azure Blob Storage, the same service used by thousands of legitimate enterprises worldwide," Seqrite Labs said. "Instead of using a traditional pull-based C2 model, AZUREVEIL follows a dead drop approach. The attacker and the infected system never communicate directly. Instead, both sides use the same Azure storage container to exchange data."

AZUREVEIL supports 36 commands that allow it to perform a wide range of post-compromise actions on the host, including file operations, file uploads and downloads, shell command execution, process enumeration and termination, port forwarding, SOCKS proxy control, C2 server management, and in-memory execution of Beacon Object Files (BOFs).

These capabilities grant the attacker complete control over the compromised endpoint. Although the activity has been attributed to a known threat actor or group, it's assessed to be China-aligned.

The disclosure comes as Cato Networks
[said](https://www.catonetworks.com/blog/cato-ctrl-suspected-china-linked-threat-actor-targets-global-manufacturer/)
it detected and blocked an attempted intrusion against the Indian branch of an unnamed global manufacturing customer to deliver TencShell, a previously undocumented Go-based implant derived from the open-source
[rshell](https://thehackernews.com/2022/08/chinese-hackers-backdoored-mimi-chat.html)
C2 framework.

The attack is believed to be the work of China-nexus threat actors based on the historical use of rshell, Tencent-themed API impersonation, and infrastructure patterns. The initial access vector used in the intrusion is currently unknown.

"If successful, TencShell could have given the attacker remote command execution, in-memory payload execution, proxying, pivoting, system profiling, and a path to deploy additional tooling," researchers Idan Tarab, Dr. Guy Waizel, Zohar Buber, and Shani Kurtzberg said.

In a report published last week, ESET
[said](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/)
China-aligned threat actors have remained "highly active" globally from October 2025 through March 2026. This includes an unreported cluster dubbed SteppeDriver that was first discovered in 2024 and has since targeted entities in France, Mongolia, and South America using tools like
[ShadowPad](https://thehackernews.com/2025/02/chinese-linked-attackers-exploit-check.html)
,
[COOLCLIENT](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html)
, CurlyDoor, RudeGull, and MKTDownloader.

Also identified by the Slovakian cybersecurity vendor is a new toolkit linked to
[UNC5221](https://thehackernews.com/2025/09/unc5221-uses-brickstorm-backdoor-to.html)
dubbed PhiliKit that acts as a passive backdoor for executing shell commands, Python scripts, and Perl scripts. It's suspected that PhiliKit is deployed as part of the
[SPAWN](https://thehackernews.com/2025/04/critical-ivanti-flaw-actively-exploited.html)
malware suite used by the Chinese hacking group in the past.

A third China-affiliated threat group is NegativeGlimmer, which is believed to share some level of overlap with
[TGR-STA-1030](https://thehackernews.com/2026/02/asian-state-backed-group-tgr-sta-1030.html)
, which Palo Alto Networks Unit 42 documented earlier this year as having breached at least 70 government and critical infrastructure organizations across 37 countries over the past year.

In at least one instance observed in December 2025, the threat actor has been found to target a governmental organization in Panama, using a DLL side-loading chain initiated via spear-phishing to deliver a downloader that then deploys AdaptixC2 and simultaneously displays a decoy document to the victim.

Subsequent iterations in January 2026 have swapped out AdaptixC2 in favor of Cobalt Strike, with infections also reported in Cambodia and South Korea.

"The latter targeting in South Korea aligns with Beijing's enduring interest in strategic technologies prioritized under the Made in China 2025 industrial development policy," ESET's Jean-Ian Boutin said.