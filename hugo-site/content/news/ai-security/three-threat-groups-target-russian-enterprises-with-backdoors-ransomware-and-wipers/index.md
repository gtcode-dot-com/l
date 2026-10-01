---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-01T19:24:29.346770+00:00'
exported_at: '2026-10-01T19:24:31.357066+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/three-threat-groups-target-russian.html
structured_data:
  about: []
  author: ''
  description: Kaspersky reports three threat clusters targeting Russian enterprises
    with backdoors, ransomware, wipers, and compromised VPN credentials.
  headline: Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware,
    and Wipers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/three-threat-groups-target-russian.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware,
  and Wipers
updated_at: '2026-10-01T19:24:29.346770+00:00'
url_hash: 1bdc2ec5139d0d18d51b1d100bbc2761611594c3
---

Enterprises in Russia have emerged as the target of three threat activity clusters tracked as
**NightEagle**
,
**Hacking Cat**
, and
**Toy Ghouls**
, according to multiple reports from Kaspersky.

The cybersecurity vendor said it has
[identified attacks](https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/)
mounted by
[NightEagle](https://thehackernews.com/2025/07/nighteagle-apt-exploits-microsoft.html)
(aka APT-Q-95), a threat actor known to be active since at least 2023, that involve new techniques for persistence and lateral movement.

"In most incidents, the attackers used compromised valid credentials to gain access to corporate VPNs," Kaspersky said in an analysis published today. "VPN connections originated from IP addresses in the Russian segment linked to Cloudflare WARP tunnels, as well as from IP addresses associated with European virtual infrastructure providers."

The attacks, as highlighted in July 2025, involve the deployment of
[GhostContainer](https://thehackernews.com/2025/07/hackers-exploit-apache-http-server-flaw.html#exchange-servers-targeted-by-ghostcontainer-backdoor)
, a known modular backdoor that grants the operators complete access to a victim's Microsoft Exchange Server, as well as run arbitrary code, perform file operations, and load additional modules.

To sidestep detection, the malware masquerades as a common server component to blend in with regular operations. It can also function as a traffic redirection or tunnel. Prior attacks involving the malware have targeted a government agency and a high-tech company located in Asia.

"It incorporates components from several open-source projects, including the Neo-reGeorg tunnel, an exploit for the CVE-2020-0688 vulnerability, and the GhostWebShell class from the ysoserial utility," Kaspersky explained. "All of these components are publicly available on GitHub."

The exact method used by the attackers to deliver GhostContainer to Microsoft Exchange servers is unknown, although it's believed to have involved the extraction of cryptographic keys used by the server from the ASP.NET configuration, followed by overwriting the VIEWSTATE framework parameter, and injecting a payload into it, causing the backdoor to be launched in memory.

To move laterally within the internal network, NightEagle has been observed downloading tunneling tools to redirect network traffic via RDP using
[Microsoft dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview)
and an open-source program called
[rdp2tcp](https://github.com/V-E-O/rdp2tcp)
.

"To obtain elevated privileges and move laterally through the network, NightEagle exploited various vulnerabilities in Active Directory," Kaspersky added. "The attackers used previously established tunnels to connect to internal infrastructure systems."

This includes the exploitation of
[CVE-2019-0708](https://nvd.nist.gov/vuln/detail/cve-2019-0708)
(aka
[BlueKeep](https://support.microsoft.com/en-us/servicing/os/windows/2019/05/customer-guidance-for-cve-2019-0708-remote-desktop-services-remote-code-execution-vulnerability-may)
) to create a local account on the system and add it to the Administrators and Remote Desktop Users groups. Furthermore, the attackers have attempted to impersonate the domain controller by means of a
[DCSync attack](https://www.trellix.com/blogs/platform/impersonating-the-boss-how-attackers-drain-active-directory/)
.

The end goal is to establish persistence in the victim infrastructure, get password hashes for domain accounts, use long-lived Kerberos tickets to gain legitimate access to target resources, and ultimately break into domain controllers and the victim's entire Active Directory infrastructure.

### Pro-Ukrainian Hacking Cat Deploys Gorilla RAT and Monkey Ransomware

The second group to single out Russian enterprises is Hacking Cat, a pro-Ukrainian hacktivist entity with a history of conducting website defacements and data breaches since February 2024. In recent months, however, the group is said to have shifted tactics and pivoted to encryption and destructive attacks.

"Hacking Cat actively collaborates with other hacktivists such as Cyber Anarchy Squad and the Ukrainian Cyber Alliance, which can complicate the attribution of tools to specific attackers," Kaspersky
[said](https://securelist.ru/tr/hacking-cat/117062/)
.

Attacks mounted by the group have weaponized vulnerabilities in Exchange servers (e.g.,
[CVE-2021-26855](https://nvd.nist.gov/vuln/detail/cve-2021-26855)
and
[CVE-2026-42897](https://nvd.nist.gov/vuln/detail/CVE-2026-42897)
) to deliver a Go-based remote access trojan dubbed Gorilla RAT, which can tunnel traffic to allow the operator to access the victim's internal network.

Once launched, the malware establishes a connection with a remote server, registers the victim, and awaits further instructions that allow it to run arbitrary commands, enumerate processes, gather system information, upload/download files, and open or close a TCP tunnel.

Also delivered by the threat actor are multiple variants of a ransomware family dubbed Monkey that are written in Rust, .NET, C++, and Golang to target Windows, Linux, and VMware ESXi systems. The earliest Monkey ransomware artifact dates back to late summer 2025. The malware also takes steps to terminate unnecessary processes and inhibit system recovery before starting the encryption process.

"A Rust-based variant of Monkey Ransomware generates a 32-byte key and encrypts the victim's files using ChaCha20-Poly1305," Kaspersky said. "Some variants do not store the key anywhere, which effectively turns them into full-fledged wiper malware, yet they still leave a ransom note. Other variants, on the other hand, store the key but do not include any contact information in the note."

Some of the notable features spread across the other three variants are listed below -

* The .NET variant generates a 32-byte key, sends it to the command-and-control (C2) server, and encrypts victim files using AES-256-CBC. It's equipped to escalate privileges and disable Windows recovery mechanisms, extract Microsoft Outlook credentials and send them to the C2 server, delete files with .bak, .backup, .bkf, .bck extensions, and remove itself after execution.
* The C++ variant offers similar functionality, but can establish persistence via a scheduled task or a
  [RunOnce](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
  registry key, clear system logs, disable logging, wipe PowerShell Command History and Windows Command Prompt, bypass AMSI, turn off Event Tracing for Windows (ETW), configure Microsoft Defender exclusions for the encryptor, make Registry modifications to disable Task Manager and Windows Command Prompt, obtain the public IP address by querying api.ipify[.]org and ipapi[.]co, and disable a number of backup, database, and recovery mechanisms, including the Volume Shadow Copy Service (VSS).
* The Golang variant, which is mainly used to target Linux and ESXi systems, establishes persistence via a crontab entry, disables SELinux and AppArmor, and attempts to delete volume shadow copies.

"This [Golang] version also includes functionality for removing shadow volume copies, which serves no purpose in Linux and ESXi environments – a fact that suggests the attackers were careless and likely used AI in developing the toolkit," Kaspersky theorized.

Hacking Cat has also been observed teaming up with the
[Cyber Anarchy Squad](https://securelist.ru/cyber-anarchy-squad-attacks-with-uncommon-trojans/111309/)
, another pro-Ukraine hacktivist group, to deliver a different ransomware strain known as ClearWater by means of a batch script. ClearWater is assessed to be distributed under a ransomware-as-a-service (RaaS) to pro-Ukrainian hacktivist crews.

In another collaborative operation with the Ukrainian Cyber Alliance, the threat actor is said to have deployed a wiper malware called Nemo Wiper that overwrites files with random bytes and fills the remaining free disk space with files containing random alphanumeric names and the .lock extension.

"Different hacktivist groups are using the same self-written tools in different attacks, including multi-stage infection chains," Kaspersky noted. "This may indicate the existence of a common source for such tools – for example, a developer or a small group of developers who create, maintain, and modify the malware, which is subsequently used by various hacktivist groups."

However, following the publication of the report, Hacking Cat
[posted](https://t.me/hacking_cat/2517)
on its Telegram channel that "a couple of the tools are ours, but the lockers are definitely not." It has also alleged Kaspersky is attributing tools from completely unrelated actors to them and that it should "learn to reverse-engineer groups better."

### Toy Ghouls Deploys Custom Backdoor for the First Time

Rounding off the list of groups targeting Russian organizations is Toy Ghouls (aka Bearlyfy, Laboo.boo, and Feral Wolf), which has moved from using leaked Babuk and LockBit ransomware builders to its own custom
[GenieLocker](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html#custom-ransomware-targets-russia)
ransomware and now to a bespoke backdoor. The financially motivated group is known to be active since 2025.

The backdoor, first detected in July 2026, appears in two variants -

* mqtt-bird-agent 0.1.0, which uses HiveMQ MQTT broker for C2
* matrix-bird-agent 0.1.0, which uses Element, a Matrix-based end-to-end encrypted messenger app, for C2

"In this campaign, the attackers use Windows Remote Management (WinRM) to deliver the backdoors and their configuration files to compromised systems," Kaspersky
[said](https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/)
. "The group relies on open-source tools such as Evil-WinRM and WinRM-fs to do this."

The Bird Agent backdoor can run within an interactive command-line session, as well as set up persistence as a Windows service. Once launched, it looks for a configuration file ("config.toml") in the same directory from where it's located. Alternatively, the full path to the file can be specified via the "-c" or "--config" option while running it.

The malware then proceeds to read the file and partially encrypts it with a key derived from the victim machine's MachineGuid value stored in the Windows Registry so that the configuration is bound to that specific system. The backdoor stops execution if it cannot decrypt the configuration on subsequent runs.

The configuration, depending on the variant used, contains either the cluster identifier used to communicate with the HiveMQ MQTT broker or the Element
[internal room identifier](https://docs.element.io/latest/element-support/matrix-rooms/managing-a-room-room-settings/#advanced)
along with the access token necessary to access that room. If this parameter is empty, the backdoor is designed such that it prompts for the token during installation, after which it gets stored.

Once the connection is established, the backdoor proceeds to send system information and issues HTTP GET requests to the HiveMQ broker to fetch commands from the C2 server, execute them via PowerShell in hidden mode (-NonInteractive -NoProfile -Command), and transmit the results back to the server.

The Element variant of Bird Agent is functionally similar to its HiveMQ counterpart, the main difference being that the received commands are executed through the Windows command-line interface (CLI) and send the command output back to the C2 server.

"The new tools use unconventional channels to communicate with their C2 server: the HiveMQ MQTT broker and the Matrix-based Element messenger," Kaspersky said. "This shift away from publicly available open-source projects toward custom-built tools suggests that Toy Ghouls is working to make its attacks more sophisticated and to evade detection for longer."

Toy Ghouls' use of the two backdoor variants has also been
[highlighted](https://bi.zone/eng/expertise/blog/idem-po-sledam-feral-wolf-novye-instrumenty-i-tekhniki-atak/)
by security vendor BI.ZONE, which linked the adversarial collective to a four-month-long campaign targeting retail, construction, manufacturing, and information technology sectors in Russia. The Rust-based backdoors have been codenamed MQTTDoor and MatrixDoor.

In one case, the threat actor exploited a known flaw in a publicly accessible Atlassian Confluence instance (
[CVE‑2023‑22515](https://thehackernews.com/2023/10/atlassian-confluence-hit-by-newly.html)
) to obtain initial access and drop the
[GSocket utility](https://github.com/hackerschoice/gsocket)
, while other attacks involved infiltrating target environments through contractor infrastructures or leveraging insecure 1C:Enterprise cluster configurations to upload a
[1C shell](https://github.com/starev-org/1C-Shell)
and run arbitrary commands on the server.

Other post-compromise actions undertaken by the threat actor are below -

* Deploying a C++ utility named RDPSocksProxy to proxy network traffic via an RDP Dynamic Virtual Channel (DVC).
* Dropping local privilege escalation (LPE) exploits for
  [CVE‑2021‑4034](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html)
  (aka PwnKit) and
  [CVE‑2026‑31431](https://thehackernews.com/2022/06/cisa-warns-of-active-exploitation-of.html)
  (aka Copy Fail).
* Loading the fscan network scanning utility into the Docker container on which the vulnerable Confluence instance was deployed.
* Escaping the compromised Docker container and gaining access to the Docker host.
* Attempting to upload
  [PrintSpoofer](https://github.com/itm4n/printspoofer)
  utility to the host after gaining the ability to execute operating system commands.
* Creating RAM dumps likely with an aim to extract credentials.

"The threat actor uses backdoors that masquerade C2 communications as legitimate MQTT and Matrix traffic, impeding detection and extending dwell time," BI.ZONE said. "The use of common application layer protocols can make it difficult to distinguish C2 communications from legitimate network connections and reduce the effectiveness of detection rules that rely on non‑standard protocol analysis."