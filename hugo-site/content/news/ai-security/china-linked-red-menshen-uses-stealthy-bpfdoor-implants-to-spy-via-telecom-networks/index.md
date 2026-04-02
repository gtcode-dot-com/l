---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T03:49:14.942272+00:00'
exported_at: '2026-04-02T03:49:17.718029+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html
structured_data:
  about: []
  author: ''
  description: China-linked Red Menshen embeds BPFDoor in telecom networks since 2021,
    enabling stealth espionage via kernel implants.
  headline: China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom
    Networks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom
  Networks
updated_at: '2026-04-02T03:49:14.942272+00:00'
url_hash: 2ad345672299ee506366ff90a6c465c30c34614b
---

A long-term and ongoing campaign attributed to a China-nexus threat actor has embedded itself in telecom networks to conduct espionage against government networks.

The strategic positioning activity, which involves implanting and maintaining stealthy access mechanisms within critical environments, has been attributed to
**[Red Menshen](https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html)**
, a threat cluster that's also tracked as Earth Bluecrow, DecisiveArchitect, and Red Dev 18. The group has a track record of striking telecom providers across the Middle East and Asia since at least 2021.

Rapid7 described the covert access mechanisms as "some of the stealthiest digital sleeper cells" ever encountered in telecommunications networks.

The campaign is characterized by the use of kernel-level implants, passive backdoors, credential-harvesting utilities, and cross-platform command frameworks, giving the threat actor the ability to persistently inhabit networks of interest. One of the most recognized tools in its malware arsenal is a Linux backdoor called
[BPFDoor](https://thehackernews.com/2023/05/new-variant-of-linux-backdoor-bpfdoor.html)
.

"Unlike conventional malware, BPFdoor does not expose listening ports or maintain visible command-and-control channels," Rapid7 Labs
[said](https://www.rapid7.com/blog/post/tr-bpfdoor-telecom-networks-sleeper-cells-threat-research-report/)
in a report shared with The Hacker News. "Instead, it abuses Berkeley Packet Filter (BPF) functionality to inspect network traffic directly inside the kernel, activating only when it receives a specifically crafted trigger packet."

"There is no persistent listener or obvious beaconing. The result is a hidden trapdoor embedded within the operating system itself."

The attack chains begin with the threat actor targeting internet-facing infrastructure and exposed edge services, such as VPN appliances, firewalls, and web-facing platforms associated with Ivanti, Cisco, Juniper Networks, Fortinet, VMware, Palo Alto Networks, and Apache Struts, to obtain initial access.

Upon gaining a successful foothold, Linux-compatible beacon frameworks such as
[CrossC2](https://thehackernews.com/2025/08/researchers-warn-crossc2-expands-cobalt.html)
are deployed to facilitate post-exploitation activities. Also dropped are
[Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html)
,
[TinyShell](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html)
(a
[Unix backdoor](https://sect.iij.ad.jp/en/2025/12/tinyshell-based-malware-from-unc5325/)
), keyloggers, and brute-force utilities to facilitate credential harvesting and lateral movement.

Central to Red Menshen's operations, however, is BPFDoor. It features two distinct components: One is a passive backdoor deployed on the compromised Linux system to inspect incoming traffic for a predefined "magic" packet by installing a BPF filter and spawning a remote shell upon receiving such a packet. The other integral part of the framework is a controller that's administered by the attacker and is responsible for sending the specially formatted packets.

"The controller is also designed to operate within the victim’s environment itself," Rapid7 explained. "In this mode, it can masquerade as legitimate system processes and trigger additional implants across internal hosts by sending activation packets or by opening a local listener to receive shell connections, effectively enabling controlled lateral movement between compromised systems."

What's more, certain BPFDoor artifacts have been found to support the Stream Control Transmission Protocol (
[SCTP](https://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol)
), potentially enabling the adversary to monitor telecom-native protocols and gain visibility into subscriber behavior and location, and even track individuals of interest.

These aspects demonstrate that the functionality of BPFdoor goes beyond a stealthy Linux backdoor. "BPFdoor functions as an access layer embedded within the telecom backbone, providing long-term, low-noise visibility into critical network operations," the security vendor added.

It doesn't end there. A previously undocumented variant of BPFdoor incorporates architectural changes to make it more evasive and stay undetected for prolonged periods in modern enterprise and telecom environments. These include concealing the trigger packet within seemingly legitimate HTTPS traffic and introducing a novel parsing mechanism that ensures the string "9999" appears at a fixed byte offset within the request.

This camouflage, in turn, allows the magic packet to stay hidden inside HTTPS traffic and avoid causing shifts to the position of data inside the request, and allows the implant to always check for the marker at a specific byte offset and, if it's present, interpret it as the activation command.

The newly discovered sample also debuts a "lightweight communication mechanism" that uses the Internet Control Message Protocol (ICMP) for interacting between two infected hosts.

"These findings reflect a broader evolution in adversary tradecraft," Rapid7 said. "Attackers are embedding implants deeper into the computing stack — targeting operating system kernels and infrastructure platforms rather than relying solely on user-space malware."

"Telecom environments — combining bare-metal systems, virtualization layers, high-performance appliances, and containerized 4G/5G core components — provide ideal terrain for low-noise, long-term persistence. By blending into legitimate hardware services and container runtimes, implants can evade traditional endpoint monitoring and remain undetected for extended periods."