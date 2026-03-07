---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-07T04:00:06.857566+00:00'
exported_at: '2026-03-07T04:00:09.837199+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/china-linked-hackers-use-terndoor.html
structured_data:
  about: []
  author: ''
  description: China-linked UAT-9244 targets South American telecom networks with
    TernDoor, PeerTime, and BruteEntry malware on Windows, Linux, and edge devices.
  headline: China-Linked Hackers Use TernDoor, PeerTime, BruteEntry in South American
    Telecom Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/china-linked-hackers-use-terndoor.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked Hackers Use TernDoor, PeerTime, BruteEntry in South American Telecom
  Attacks
updated_at: '2026-03-07T04:00:06.857566+00:00'
url_hash: 10e9f8d80d21ae73374d75958e4cb9598cd1b9a4
---

**

Ravie Lakshmanan
**

Mar 06, 2026

Cyber Espionage / Threat Intelligence

A China-linked advanced persistent threat (APT) actor has been targeting critical telecommunications infrastructure in South America since 2024, targeting Windows and Linux systems and edge devices with three different implants.

The activity is being
[tracked](https://blog.talosintelligence.com/uat-9244/)
by Cisco Talos under the moniker
**UAT-9244**
, describing it as closely associated with another cluster known as
[FamousSparrow](https://thehackernews.com/2025/03/new-sparrowdoor-backdoor-variants-found.html)
.

It's worth noting that FamousSparrow is assessed to share tactical overlaps with
[Salt Typhoon](https://thehackernews.com/2024/11/chinese-hackers-use-ghostspider-malware.html)
, a China-nexus espionage group known for its targeting of telecommunication service providers. Despite the similar targeting footprint between UAT-9244 and Salt Typhoon, there is no conclusive evidence that ties the two clusters together.

In the campaign analyzed by the cybersecurity company, the attack chains have been found to distribute three previously undocumented implants: TernDoor targeting Windows, PeerTime (aka angrypeer) targeting Linux, and BruteEntry, which is installed on network edge devices.

The exact initial access method used in the attacks is not known, although the adversary has previously targeted systems running outdated versions of Windows Server and Microsoft Exchange Server to drop web shells for follow-on activity.

TernDoor is deployed through DLL side-loading, leveraging the legitimate executable "wsprint.exe" to launch a rogue DLL ("BugSplatRc64.dll") that decrypts and executes the final payload in memory. A variant of
[Crowdoor](https://thehackernews.com/2024/09/chinese-speaking-hacker-group-targets.html)
(itself a variant of SparrowDoor), the backdoor is said to have been put to use by UAT-9244 since at least November 2024.

It establishes persistence on the host by means of a scheduled task or the Registry Run key. It also exhibits differences with CrowDoor by making use of a disparate set of command codes and embedding a Windows driver to suspend, resume, and terminate processes. Furthermore, it only supports one command-line switch ("-u") to uninstall itself from the host and delete all associated artifacts.

Once launched, it runs a check to make sure that it has been injected into "msiexec.exe," after which it decodes a configuration to extract the command-and-control (C2) parameters. Subsequently, it establishes communication with the C2 server, allowing it to create processes, run arbitrary commands, read/write files, collect system information, and deploy the driver to hide malicious components and manage processes.

Further analysis of the UAT-9244's infrastructure has led to the discovery of a Linux peer-to-peer (P2P) backdoor dubbed PeerTime, which is compiled for several architectures (i.e., ARM, AARCH, PPC, and MIPS) so as to infect a variety of embedded systems. The ELF backdoor, along with an instrumentor binary, is deployed via a shell script.

"The instrumentor ELF binary will check for the presence of Docker on the compromised host using the commands docker and docker –q," Talos researchers Asheer Malhotra and Brandon White said. "If Docker is found, then the PeerTime loader is executed. The instrumentor consists of debug strings in Simplified Chinese, indicating that it is a custom binary created and deployed by Chinese-speaking threat actors."

The primary goal of the loader is to decrypt and decompress the final PeerTime payload and execute it directly in memory. PeerTime comes in two flavors: one version written in C/C++ and a newer variant programmed in Rust. Besides having the ability to rename itself as a harmless process to sidestep detection, the backdoor employs the BitTorrent protocol to fetch C2 information, download files from its peers, and execute them on the compromised system.

Also staged in the threat actor's servers are a set of shell scripts and payloads, including a brute-force scanner codenamed BruteEntry that's installed on edge devices to turn them into mass-scanning proxy nodes within an Operational Relay Box (ORB) capable of brute-forcing Postgres, SSH, and Tomcat servers.

This is accomplished by means of a shell script that drops two Golang-based components: an orchestrator that delivers BruteEntry, which then contacts a C2 server to obtain the list of IP addresses to be targeted for performing brute-force attacks. The backdoor ultimately reports successful logins back to the C2 server.

"'Success' indicates if the brute force was successful (true or false), and 'notes' provides specific information on whether the brute force was successful," Talos said. "If the login failed, the note reads 'All credentials tried.'"