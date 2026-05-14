---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T20:39:58.383093+00:00'
exported_at: '2026-05-14T20:40:00.081746+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html
structured_data:
  about: []
  author: ''
  description: A new TrickMo Android banking trojan variant uses TON blockchain infrastructure
    for stealthy command-and-control communications.
  headline: New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots
updated_at: '2026-05-14T20:39:58.383093+00:00'
url_hash: 4340e9c3f0587ed7c0b738bc3dedde5ebe513ab2
---

**

Ravie Lakshmanan
**

May 12, 2026

Malware / Mobile Security

Cybersecurity researchers have flagged a new version of the
**TrickMo**
Android banking trojan that uses The Open Network (TON) for command-and-control (C2).

The new variant, observed by ThreatFabric between January and February 2026, has been observed actively targeting banking and cryptocurrency wallet users in France, Italy, and Austria.

"TrickMo relies on a runtime-loaded APK  (dex.module), used also by the previous variant, but updated with new features adding new network-oriented functionality, including reconnaissance, SSH tunnelling, and SOCKS5 proxying capabilities that allow infected devices to function as programmable network pivots and traffic-exit nodes," the Dutch mobile security company
[said](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)
in a report shared with The Hacker News.

TrickMo is the name assigned to a device takeover (DTO) malware that's been active in the wild since late 2019. It was
[first flagged by CERT-Bund and IBM X-Force](https://thehackernews.com/2020/03/trickbot-two-factor-mobile-malware.html)
, describing its ability to abuse Android's accessibility services to hijack one-time passwords (OTPs).

It's also
[equipped](https://thehackernews.com/2024/10/trickmo-banking-trojan-can-now-capture.html)
with a wide range of features to phish for credentials, log keystrokes, record screen, facilitate live screen streaming, intercept SMS messages, essentially granting the operator complete remote control of the device.

The latest versions, labeled TrickMo C, are distributed via phasing websites and dropper apps, the latter of which serve as a conduit for a dynamically loaded APK ("dex.module") that's retrieved at runtime from attacker-controlled infrastructure. A notable shift in the architecture entails the use of the TON decentralized blockchain for stealthy C2 communications.

"TrickMo carries an embedded native TON proxy that the host APK starts on a loopback port at process start," ThreatFabric said. "The bot's HTTP client is wired through that proxy, so every outbound command-and-control request is addressed to an .adnl hostname and resolved through the TON overlay."

Dropper apps containing the malware masquerade as adult-friendly versions of TikTok through Facebook, whereas the actual malware impersonates Google Play Services -

* [com.app16330.core20461](https://www.virustotal.com/gui/file/01889a9ec2abecb73e5e8792be68a4e3bc7dcbe1c3f19ac06763682d63aa8c21)
  or com.app15318.core1173 (Dropper)
* uncle.collop416.wifekin78 or nibong.lida531.butler836 (TrickMo)

While previous iterations of "dex.module" implemented the accessibility-driven remote control functionality through a socket.io-based channel, the new version utilizes a network-operative subsystem that turns the malware into a tool for managed foothold than a traditional banking trojan.

The subsystem supports commands like curl, dnslookup, ping, telnet, and traceroute, giving the attacker a "remote shell-equivalent for network reconnaissance from the victim's network position, including any internal corporate or home network the device is currently associated with," per ThreatFabric.

Another important feature is a SOCKS5 proxy that turns the compromised device into a network exit node that routes malicious traffic, while defeating IP-based fraud-detection signatures on banking, e-commerce and cryptocurrency exchange services.

Furthermore, TrickMo includes two dormant features that bundle the Pine hooking framework and declare extensive NFC-related permissions. But neither of them are actually implemented. This likely indicates the core developers are looking to expand on the trojan's capabilities in the future.

"Instead of relying on conventional DNS and public internet infrastructure, the malware communicates through .adnl endpoints routed via an embedded local TON proxy, reducing the effectiveness of traditional takedown and network-blocking efforts while making the traffic blend with legitimate TON activity," ThreatFabric said.

"This latest variant also expands the operational role of infected devices through SSH tunnelling and authenticated SOCKS5 proxying, effectively turning compromised phones into programmable network pivots and traffic-exit nodes whose connections originate from the victim’s own network environment."