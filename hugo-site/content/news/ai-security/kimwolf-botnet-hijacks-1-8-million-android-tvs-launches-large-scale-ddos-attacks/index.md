---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-19T04:44:03.996099+00:00'
exported_at: '2025-12-19T04:44:07.576921+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html
structured_data:
  about: []
  author: ''
  description: Kimwolf botnet infected 1.8 million Android TV devices and issued 1.7
    billion DDoS commands, using ENS to hide its control servers.
  headline: Kimwolf Botnet Hijacks 1.8 Million Android TVs, Launches Large-Scale DDoS
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Kimwolf Botnet Hijacks 1.8 Million Android TVs, Launches Large-Scale DDoS Attacks
updated_at: '2025-12-19T04:44:03.996099+00:00'
url_hash: 5c83ee4a7a676b7b2caea0171590594eb97f8bf0
---

A new distributed denial-of-service (DDoS) botnet known as
**Kimwolf**
has enlisted a massive army of no less than 1.8 million infected devices comprising Android-based TVs, set-top boxes, and tablets, and may be associated with another botnet known as
[AISURU](https://thehackernews.com/2025/12/record-297-tbps-ddos-attack-linked-to.html)
, according to findings from QiAnXin XLab.

"Kimwolf is a botnet compiled using the
[NDK](https://developer.android.com/ndk)
[Native Development Kit]," the company
[said](https://blog.xlab.qianxin.com/kimwolf-botnet-en/)
in a report published today. "In addition to typical DDoS attack capabilities, it integrates proxy forwarding, reverse shell, and file management functions."

The hyper-scale botnet is estimated to have issued 1.7 billion DDoS attack commands within a three-day period between November 19 and 22, 2025, around the same time one of its command-and-control (C2) domains – 14emeliaterracewestroxburyma02132[.]su –
[came first](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploit-chrome-0.html#:~:text=environments.-,Microsoft%20Mitigates%20Record%2015.72%20Tbps%20DDoS%20Attack)
in Cloudflare's list of top 100 domains, briefly even surpassing Google.

Kimwolf's primary infection targets are TV boxes deployed in residential network environments. Some of the affected device models include TV BOX, SuperBOX, HiDPTAndroid, P200, X96Q, XBOX, SmartTV, and MX10. Infections are scattered globally, with Brazil, India, the U.S., Argentina, South Africa, and the Philippines registering higher concentrations. That said, the exact means by which the malware is propagated to these devices is presently unclear.

XLab said its investigation into the botnet commenced after it received a "version 4" artifact of Kimwolf from a trusted community partner on October 24, 2025. Since then, an additional eight samples have been discovered as of last month.

"We observed that Kimwolf's C2 domains have been successfully taken down by unknown parties at least three times [in December], forcing it to upgrade its tactics and turn to using ENS (Ethereum Name Service) to harden its infrastructure, demonstrating its powerful evolutionary capability," XLab researchers said.

That's not all. Earlier this month, XLab managed to successfully seize control of one of the C2 domains, enabling it to assess the scale of the botnet and observing a peak daily active bot IP count of approximately 1.83 million.

An interesting aspect of Kimwolf is that it's tied to the infamous AISURU botnet, which has been behind some of the record-breaking DDoS attacks over the past year. It's suspected that the attackers reused code from AISURU in the early stages, before opting to develop the Kimwolf botnet to evade detection.

XLab said it's possible some of these attacks may not have come from AISURU alone, and that Kimwolf may be either participating or even leading the efforts.

"These two major botnets propagated through the same infection scripts between September and November, coexisting in the same batch of devices," the company said. "They actually belong to the same hacker group."

This assessment is based on
[similarities](https://www.virustotal.com/gui/file/84cf4aac1e063394be3be68fea3cb9526e567c0aeaaf39b4834411970c00921e)
in APK packages uploaded to the VirusTotal platform, in
[some cases](https://www.virustotal.com/gui/file/750a3e2ab2941705672cbeb6ec4d265e7ed79f21a18371de0c960a873b8cbbfd)
even using the
[same code signing certificate](https://www.virustotal.com/gui/file/77366b3b2dc016fea0f8461a1cb06e089b9186059a73d67e6ba28d088c06431d)
("John Dinglebert Dinglenut VIII VanSack Smith"). Further definitive evidence arrived on December 8, 2025, with the discovery of an active downloader server ("93.95.112[.]59") that contained a script referencing APKs for both Kimwolf and AISURU.

The malware in itself is fairly straightforward. Once launched, it ensures that only one instance of the process runs on the infected device, and then proceeds to decrypt the embedded C2 domain, uses DNS-over-TLS to obtain the C2 IP address, and connects to it in order to receive and execute commands.

Recent versions of the botnet malware detected as recently as December 12, 2025, have introduced a technique known as
[EtherHiding](https://thehackernews.com/2025/10/hackers-abuse-blockchain-smart.html)
that makes use of an ENS domain ("pawsatyou[.]eth") to fetch the actual C2 IP from the associated smart contract (
[0xde569B825877c47fE637913eCE5216C644dE081F](https://etherscan.io/address/0xde569B825877c47fE637913eCE5216C644dE081F)
) in an effort to render its infrastructure more resilient to takedown efforts.

Specifically, this involves extracting an IPv6 address from the
["lol" field of the transaction](https://etherscan.io/tx/0xac165115069ea91503c29af14322cf84cbd39133bb59a447c2aa704999cd334f)
, then taking the last four bytes of the address and performing an XOR operation with the key "0x93141715" to get the actual IP address.

Besides encrypting sensitive data related to C2 servers and DNS resolvers, Kimwolf uses TLS encryption for network communications to receive DDoS commands. In all, the malware supports 13 DDoS attack methods over UDP, TCP, and ICMP. The attack targets, per XLab, are located in the U.S., China, France, Germany, and Canada.

Further analysis has determined that over 96% of the commands relate to using the bot nodes for providing proxy services. This indicates the attackers' attempts to exploit the bandwidth from compromised devices and maximize profit. As part of the effort, a Rust-based Command Client module is deployed to form a proxy network.

Also delivered to the nodes is a ByteConnect software development kit (SDK), a monetization solution that allows app developers and IoT device owners to monetize their traffic.

"Giant botnets originated with Mirai in 2016, with infection targets mainly concentrated on IoT devices like home broadband routers and cameras," XLab said. "However, in recent years, information on multiple million-level giant botnets like Badbox, Bigpanzi, Vo1d, and Kimwolf has been disclosed, indicating that some attackers have started to turn their attention to various smart TVs and TV boxes."