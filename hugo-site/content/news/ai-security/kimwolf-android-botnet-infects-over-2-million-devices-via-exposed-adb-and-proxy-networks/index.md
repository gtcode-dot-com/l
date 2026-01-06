---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-06T12:15:14.959095+00:00'
exported_at: '2026-01-06T12:15:17.184129+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html
structured_data:
  about: []
  author: ''
  description: Kimwolf is an Android botnet that infected 2M+ devices via exposed
    ADB, using proxy networks to run DDoS attacks and sell residential bandwidth.
  headline: Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB
    and Proxy Networks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy
  Networks
updated_at: '2026-01-06T12:15:14.959095+00:00'
url_hash: b8a70eee0e1aa843668f112576035ea8f659be4c
---

**

Jan 05, 2026
**

Ravie Lakshmanan

IoT Security / Mobile Security

The botnet known as
**Kimwolf**
has infected more than 2 million Android devices by tunneling through residential proxy networks, according to findings from Synthient.

"Key actors involved in the Kimwolf botnet are observed monetizing the botnet through app installs, selling residential proxy bandwidth, and selling its DDoS functionality," the company
[said](https://synthient.com/blog/a-broken-system-fueling-botnets)
in an analysis published last week.

Kimwolf was
[first publicly documented](https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html)
by QiAnXin XLab last month, while documenting its connections to another botnet known as AISURU. Active since at least August 2025, Kimwolf is assessed to be an Android variant of AISURU. There is growing evidence to suggest that the botnet is actually behind a series of
[record-setting DDoS attacks](https://thehackernews.com/2025/12/record-297-tbps-ddos-attack-linked-to.html)
late last year.

The malware turns infected systems into conduits for relaying malicious traffic and orchestrating distributed denial-of-service (DDoS) attacks at scale. The vast majority of the infections are concentrated in Vietnam, Brazil, India, and Saudi Arabia, with Synthient observing approximately 12 million unique IP addresses per week.

Attacks distributing the botnet have been primarily found to target Android devices running an exposed Android Debug Bridge (ADB) service using a scanning infrastructure that uses residential proxies to install the malware. No less than 67% of the devices connected to the botnet are unauthenticated and have ADB enabled by default.

It's suspected that these devices come pre-infected with software development kits (SDKs) from proxy providers so as to surreptitiously enlist them in the botnet. The
[top compromised devices](https://github.com/synthient/public-research/tree/main/2026/01/kimwolf)
include unofficial Android-based smart TVs and set-top boxes.

As recently as December 2025, Kimwolf infections have leveraged proxy IP addresses offered for rent by China-based IPIDEA, which implemented a security patch on December 27 to block access to local network devices and various sensitive ports. IPIDEA
[describes](https://www.ipidea.io)
itself as the "world's leading provider of IP proxy" with more than 6.1 million daily updated IP addresses and 69,000 daily new IP addresses.

In other words, the modus operandi is to leverage IPIDEA's proxy network and other proxy providers, and then tunnel through the local networks of systems running the proxy software to drop the malware. The main payload listens on port 40860 and connects to 85.234.91[.]247:1337 to receive further commands.

"The scale of this vulnerability was unprecedented, exposing millions of devices to attacks," Synthient said.

Furthermore, the attacks infect the devices with a bandwidth monetization service known as Plainproxies Byteconnect SDK, indicating broader attempts at monetization. The SDK uses 119 relay servers that receive proxy tasks from a command-and-control server, which are then executed by the compromised device.

Synthient said it detected the infrastructure being used to conduct credential-stuffing attacks targeting IMAP servers and popular online websites.

"Kimwolf's monetization strategy became apparent early on through its aggressive sale of residential proxies," the company said. "By offering proxies as low as 0.20 cents per GB or $1.4K a month for unlimited bandwidth, it would gain early adoption by several proxy providers."

"The discovery of pre-infected TV boxes and the monetization of these bots through secondary SDKs like Byteconnect indicates a deepening relationship between threat actors and commercial proxy providers."

To counter the risk, proxy providers are recommended to block requests to
[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)
addresses, which are
[private IP address ranges](https://en.wikipedia.org/wiki/Private_network)
defined for use in private networks. Organizations are advised to lock down devices running unauthenticated ADB shells to prevent unauthorized access.