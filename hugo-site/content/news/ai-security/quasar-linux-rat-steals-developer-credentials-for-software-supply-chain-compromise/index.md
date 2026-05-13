---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-13T04:14:16.366733+00:00'
exported_at: '2026-05-13T04:14:18.101583+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html
structured_data:
  about: []
  author: ''
  description: Quasar Linux RAT (QLNX) harvests DevOps credentials to enable software
    supply chain attacks with fileless execution and dual rootkit stealth.
  headline: Quasar Linux RAT Steals Developer Credentials for Software Supply Chain
    Compromise
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Quasar Linux RAT Steals Developer Credentials for Software Supply Chain Compromise
updated_at: '2026-05-13T04:14:16.366733+00:00'
url_hash: 0cb2317f127153aa070ed0e959835a8ffef0b7fc
---

**

Ravie Lakshmanan
**

May 08, 2026

Linux / DevOps

A previously undocumented Linux implant codenamed
**Quasar Linux RAT (QLNX)**
is targeting developers' systems to establish a silent foothold as well as facilitate a broad range of post-compromise functionality, such as credential harvesting, keylogging, file manipulation, clipboard monitoring, and network tunneling.

"QLNX targets developers and DevOps credentials across the software supply chain," Trend Micro researchers Aliakbar Zahravi and Ahmed Mohamed Ibrahim
[said](https://www.trendmicro.com/en_us/research/26/e/quasar-linux-qlnx-a-silent-foothold-in-the-software-supply-chain.html)
in a technical analysis of the malware.

"Its credential harvester extracts secrets from high-value files such as .npmrc (npm tokens), .pypirc (PyPI credentials), .git-credentials, .aws/credentials, .kube/config, .docker/config.json, .vault-token, Terraform credentials, GitHub CLI tokens, and .env files. The compromise of these assets could allow the operator to push malicious packages to NPM or PyPI registries, access cloud infrastructure, or pivot through CI/CD pipelines."

The malware's ability to systematically harvest a wide range of credentials poses a severe risk to developer environments. A threat actor who successfully deploys QLNX against a package maintainer gains unauthorized access to their publishing pipeline, allowing the attacker to push poisoned versions that can lead to cascading downstream impacts.

QLNX executes filelessly from memory, masquerades itself as a kernel thread (e.g., kworker or ksoftirqd), and is capable of profiling the host to detect containerized environments, wiping system logs to cover up the tracks, and setting up persistence using no less than seven different methods, including systemd, crontab, and .bashrc shell injection.

Furthermore, it exfiltrates the collected data to an attacker-controlled infrastructure, and receives commands that make it possible to execute shell commands, manage files, inject code into processes, take screenshots, log keystrokes, establish SOCKS proxies and TCP tunnels, run Beacon Object Files (BOFs), and even manage a peer-to-peer (P2P) mesh network.

Exactly how the malware is delivered is unclear. However, once a foothold is established, it enters a primary operational phase by running a persistent loop that continuously attempts to establish and maintain communication with the command-and-control (C2) server over raw TCP, HTTPS, and HTTP. In total, QLNX supports 58 distinct commands that give the operators complete control of the compromised host.

QLNX also comes with a Pluggable Authentication Module (
[PAM](https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html)
) inline-hook backdoor that intercepts plaintext credentials during authentication events, logs outbound SSH session data, and transmits the data to the C2 server. The malware also supports a second PAM-based credentials logger that's automatically loaded into every dynamically linked process to extract the service name, username, and authentication token.

It employs a two-tiered rootkit architecture: a userland rootkit deployed through the Linux dynamic linker's LD\_PRELOAD mechanism to ensure that the implant's artifacts and processes stay hidden. There also exists a kernel-level eBPF component that uses BPF subsystem to conceal processes, files, and network ports from standard userland tools such as ps, ls, and netstat upon receiving instructions from the C2 server.

"The QLNX implant was built for long-term stealth and credential theft," Trend Micro said. "What makes it particularly dangerous is not any single feature, but how its capabilities chain together into a coherent attack workflow: arrive, erase from disk, persist through six redundant mechanisms, hide at both userspace and kernel level, and then harvest the credentials that matter most."