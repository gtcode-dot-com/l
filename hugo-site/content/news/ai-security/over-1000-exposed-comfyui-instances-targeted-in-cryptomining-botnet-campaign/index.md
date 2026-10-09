---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-07T23:36:33.560436+00:00'
exported_at: '2026-04-07T23:36:36.097817+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/over-1000-exposed-comfyui-instances.html
structured_data:
  about: []
  author: ''
  description: Over 1,000 exposed ComfyUI instances exploited via unauthenticated
    code execution, enabling Monero mining and botnet expansion.
  headline: Over 1,000 Exposed ComfyUI Instances Targeted in Cryptomining Botnet Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/over-1000-exposed-comfyui-instances.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Over 1,000 Exposed ComfyUI Instances Targeted in Cryptomining Botnet Campaign
updated_at: '2026-04-07T23:36:33.560436+00:00'
url_hash: 13cdb5c7587188e004f554407026782e4e2b478b
---

An active campaign has been observed targeting internet-exposed instances running ComfyUI, a popular stable diffusion platform, to enlist them into a cryptocurrency mining and proxy botnet.

"A purpose-built Python scanner continuously sweeps major cloud IP ranges for vulnerable targets, automatically installing malicious nodes via
[ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)
if no exploitable node is already present," Censys security researcher Mark Ellzey
[said](https://censys.com/blog/comfyui-servers-cryptomining-proxy-botnet/)
in a report published Monday.

The attack activity, at its core, systemically scans for exposed ComfyUI instances and exploits a misconfiguration that allows remote code execution on unauthenticated deployments through
[custom nodes](https://docs.comfy.org/development/core-concepts/nodes)
.

Upon successful exploitation, the compromised hosts are added to a cryptomining operation that mines Monero via XMRig and Conflux via lolMiner, as well as to a Hysteria V2 botnet. Both of them are centrally managed through a Flask-based command-and-control (C2) dashboard.

Data from the attack surface management platforms shows that there are more than
[1,000 publicly-accessible ComfyUI instances](https://platform.censys.io/search?q=%28host.services.endpoints.http.html_tags+%3D+%22%3Ctitle%3EComfyUI%3C%2Ftitle%3E%22%29+and+not+host.services.labels.value+%3D+%22HONEYPOT%22)
. While not a huge number, it's sufficient for a threat actor to run opportunistic campaigns to reap financial gains.

Censys said it discovered the campaign last month after identifying an open directory on
[77.110.96[.]200](https://platform.censys.io/hosts/77.110.96.200)
, an IP address associated with a bulletproofing hosting services provider,
[Aeza Group](https://thehackernews.com/2025/07/us-sanctions-russian-bulletproof.html)
. The directory is said to have contained a previously undocumented set of tools to pull off the attacks.

This includes two reconnaissance tools to enumerate exposed ComfyUI instances across cloud infrastructure, identify those that have ComfyUI-Manager installed, and shortlist those that are susceptible to the code execution exploit.

One of the two scanner Python scripts also functions as an exploitation framework that weaponizes ComfyUI's custom nodes to achieve code execution. This technique, some aspects of which were
[documented](https://labs.snyk.io/resources/hacking-comfyui-through-custom-nodes/)
by Snyk in December 2024, takes advantage of the fact that some custom nodes accept raw Python code as input and run it directly without requiring any authentication.

As a result, an attacker can scan exposed ComfyUI instances for specific custom node families that support arbitrary code execution, effectively turning the service into a channel for delivering attacker-controlled Python payloads. Some of the custom node families that the attack particularly looks for are listed below -

* Vova75Rus/ComfyUI-Shell-Executor
* filliptm/ComfyUI\_Fill-Nodes
* seanlynch/srl-nodes
* ruiqutech/ComfyUI-RuiquNodes

"If none of the target nodes are present, the scanner checks whether ComfyUI-Manager is installed," Censys said. "If available, it installs a vulnerable node package itself, then retries exploitation."

It's worth noting that "ComfyUI-Shell-Executor" is a malicious package created by the attacker to fetch a next-stage shell script ("ghost.sh") from the aforementioned IP address. Once code execution is obtained, the scanner removes evidence of the exploit by clearing the ComfyUI prompt history.

A newer version of the scanner also incorporates persistence mechanisms that cause the shell script to be downloaded every six hours and the exploit workflow to be re-executed every time ComfyUI is started.

The shell script, for its part, disables shell history, kills competing miners, launches the miner process, anduses the
[LD\_PRELOAD](https://thehackernews.com/2023/03/cryptojacking-group-teamtnt-suspected.html)
hook to hide a watchdog process that ensures the miner process is revived in the event it gets terminated.

In addition, the miner program is copied to multiple locations so that even if the primary install directory gets wiped, it can be launched from one of the fallback locations. A third mechanism the malware uses to ensure persistence is the use of the "
[chattr +i](https://man7.org/linux/man-pages/man1/chattr.1.html)
" command to lock the miner binaries and prevent them from being deleted, modified, or renamed, even by the root user.

"There is also dedicated code targeting a specific competitor, 'Hisana' (which is referenced throughout the code), which appears to be another mining botnet," Censys explained. "Rather than just killing it, ghost.sh overwrites its configuration to redirect Hisana's mining output to its own wallet address, then occupies Hisana’s C2 port (10808) with a dummy Python listener so Hisana can't restart."

The infected hosts are commandeered by means of a Flask-based C2 panel, which allows the operator to push instructions or deploy additional payloads, including a shell script that installs Hysteria V2 with the likely goal of selling compromised nodes as proxies.

Further analysis of the attacker's shell command history has revealed an SSH login attempt as root to the IP address
[120.241.40[.]237](https://www.virustotal.com/gui/ip-address/120.241.40.237/detection)
, which has been linked to an
[ongoing worm campaign](https://censys.com/blog/databases-exposed-redis/)
targeting exposed Redis database servers.

"Much of the tooling in this repository appears hastily assembled, and the overall tactics and techniques might initially suggest unsophisticated activity," Censys said. "Specifically, the operator identifies exposed ComfyUI instances running custom nodes, determines which of those nodes expose unsafe functionality, and then uses them as a pathway to remote code execution."

"The infrastructure accessed by the operator further supports the idea that this activity is part of a broader campaign focused on discovering and exploiting exposed services, followed by the deployment of custom tooling for persistence, scanning, or monetization."

The discovery coincides with the emergence of multiple botnet campaigns in recent weeks -

* Exploitation of
  [command injection vulnerabilities](https://thehackernews.com/2026/03/weekly-recap-sd-wan-0-day-critical-cves.html#:~:text=Zerobot%20Exploits%20Flaws%20in%20n8n%20and%20Tenda%20Routers)
  in n8n (
  [CVE-2025-68613](https://thehackernews.com/2026/03/cisa-flags-actively-exploited-n8n-rce.html)
  ) and Tenda AC1206 routers (
  [CVE-2025-7544](https://nvd.nist.gov/vuln/detail/CVE-2025-7544)
  ) to
  [add them](https://www.intel471.com/blog/cve-2025-68613-zerobot-botnet-exploits-critical-vulnerability-impacting-n8n-ai-orchestration-platform)
  to a Mirai-based botnet known as
  [Zerobot](https://thehackernews.com/2022/12/zerobot-botnet-emerges-as-growing.html)
  .
* Exploitation of
  [vulnerabilities](https://www.vulncheck.com/blog/return-of-the-kinsing)
  in Apache ActiveMQ (
  [CVE-2023-46604](https://thehackernews.com/2023/11/new-poc-exploit-for-apache-activemq.html)
  ), Metabase (
  [CVE-2023-38646](https://thehackernews.com/2023/07/major-security-flaw-discovered-in.html)
  ), and React Server Components (
  [CVE-2025-55182](https://thehackernews.com/2026/04/hackers-exploit-cve-2025-55182-to.html)
  aka React2Shell) to deliver
  [Kinsing](https://thehackernews.com/2024/05/kinsing-hacker-group-exploits-more.html)
  , a persistent malware used for cryptocurrency mining and launching Distributed Denial of Service (DDoS) attacks.
* Exploitation of a suspected zero-day vulnerability in fnOS Network Attached Storage (NAS) to target internet-exposed systems and implant them with a DDoS malware called
  [Netdragon](https://blog.xlab.qianxin.com/netdragon/)
  . "NetDragon establishes an HTTP backdoor interface on compromised devices, enabling attackers to remotely access and control the infected systems," QiAnXin XLab said. "It tampers with the 'hosts' file to hijack the official Feiniu NAS system update domains, effectively preventing devices from obtaining system updates and security patches."
* Expansion of
  [RondoDox](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html#botnet-exploiting-174-flaws)
  's exploit list to 174 different vulnerabilities, while shifting the attack methodology from a "shotgun approach" to more targeted and recent flaws that are more likely to lead to infections.
* Exploitation of
  [known security vulnerabilities](https://eclypsium.com/blog/condibot-monaco-malware-network-infrastructure/)
  to deploy a new variant of
  [Condi](https://thehackernews.com/2025/03/ballista-botnet-exploits-unpatched-tp.html)
  , a Linux malware that turns compromised linux devices into bots capable of conducting DDoS attacks. The binary references a string "QTXBOT," either indicating the name of the forked version or the internal project name.
* Brute-force attacks against SSH servers to launch an XMRig miner and generate illicit cryptocurrency revenue as part of an active cryptojacking operation called Monaco. Weak SSH passwords have also been
  [used as attack pathways](https://isc.sans.edu/diary/32708)
  to deploy malware that establishes persistence, kills competing miners, connects to an external server, and performs a ZMap scan to propagate the malware in a worm-like fashion to other vulnerable hosts.

"Botnet activity has surged over the last year, with Spauhaus noting 26% and 24% increases in the two six-month periods Jan - Jun 2025 and Jul - Dec 2025, respectively," Pulsedive
[said](https://blog.pulsedive.com/the-operations-of-the-swarm-inside-the-complex-world-of-mirai-based-botnets/)
.

"This increase is associated with bots and nodes appearing in the United States. The increase also stems from the availability of source code for botnets such as Mirai. Mirai offshoots and variants are responsible for some of the largest DDoS attacks by volume."