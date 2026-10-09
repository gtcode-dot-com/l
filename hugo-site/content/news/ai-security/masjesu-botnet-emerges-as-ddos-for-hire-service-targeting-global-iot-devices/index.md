---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T18:15:14.282661+00:00'
exported_at: '2026-04-08T18:15:17.135700+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html
structured_data:
  about: []
  author: ''
  description: Masjesu botnet drives global DDoS attacks since 2023, with nearly 50%
    traffic from Vietnam, threatening enterprises and IoT devices.
  headline: Masjesu Botnet Emerges as DDoS-for-Hire Service Targeting Global IoT Devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Masjesu Botnet Emerges as DDoS-for-Hire Service Targeting Global IoT Devices
updated_at: '2026-04-08T18:15:14.282661+00:00'
url_hash: bd89429194fd19e24f6197e47bb13934ad67126d
---

**

Ravie Lakshmanan
**

Apr 08, 2026

IoT Security / Network Security

Cybersecurity researchers have lifted the curtain on a stealthy botnet that's designed for distributed denial-of-service (DDoS) attacks.

Called
**Masjesu**
, the botnet has been advertised via Telegram as a DDoS-for-hire service since it first surfaced in 2023. It's capable of targeting a wide range of IoT devices, such as routers and gateways, spanning multiple architectures.

"Built for persistence and low visibility, Masjesu favors careful, low-key execution over widespread infection, deliberately avoiding blocklisted IP ranges such as those belonging to the Department of Defense (DoD) to ensure long-term survival," Trellix security researcher Mohideen Abdul Khader F
[said](https://www.trellix.com/blogs/research/masjesu-rising-stealth-iot-botnet-ddos-evasion/)
in a Tuesday report.

It's worth noting that the commercial offering also goes by the moniker XorBot owing to its use of XOR-based encryption to conceal strings, configurations, and payload data. It was
[first documented](https://nsfocusglobal.com/xorbot-a-stealthy-botnet-family-that-defies-detection/)
by Chinese security vendor NSFOCUS in December 2023, linking it to an operator named "synmaestro."

A
[subsequent iteration](https://thehackernews.com/2024/11/matrix-botnet-exploits-iot-devices-in.html)
of the botnet observed a year later was found to have added 12 different command injection and code execution exploits to target routers, cameras, DVRs, and NVRs from D-Link, Eir, GPON, Huawei, Intelbras, MVPower, NETGEAR, TP-Link, and Vacron, and obtain initial access. Also added were new modules to conduct DDoS flood attacks.

"As an emerging botnet family, XorBot is showing a strong growth momentum, continuously infiltrating and controlling new IoT devices," NSFOCUS said in November 2024. "Notably, these controllers are increasingly inclined to use social media platforms such as Telegram as the main channels for recruitment and promotion, attracting target 'customers' through initial active promotional activities, laying a solid foundation for the subsequent expansion and development of the botnet."

The latest findings from Trellix show that Masjesu has marketed the ability to carry out volumetric DDoS attacks, emphasizing its diverse botnet infrastructure and its suitability for targeting content delivery networks (CDNs), game servers, and enterprises. Attacks mounted by the botnet primarily originate from Vietnam, Ukraine, Iran, Brazil, Kenya, and India, with Vietnam accounting for nearly 50% of the observed traffic.

Once deployed on a compromised device, the malware moves to create and bind a socket with a hard-coded TCP port (55988) to enable the attacker to connect directly. If this operation fails, the attack chain is immediately killed.

Otherwise, the malware proceeds to set up persistence, ignore termination-related signals, stop commonly used processes like wget and curl, possibly to disrupt competing botnets, and then connects to an external server to receive DDoS attack commands for executing them against targets of interest.

Masjesu also boasts of self-propagating capabilities, allowing it to probe random IP addresses for open ports and wrangle successfully compromised devices into its infrastructure. One notable addition to the list of exploitation targets is Realtek routers, which is carried out by scanning for 52869 – a port associated with
[Realtek SDK's](https://www.trendmicro.com/en_us/research/19/c/upnp-enabled-connected-devices-in-home-unpatched-known-vulnerabilities.html)
[miniigd](https://www.akamai.com/blog/security/universal-plug-and-play-upnp-what-you-need-to-know)
daemon. Multiple DDoS botnets, such as
[JenX](https://www.radware.com/security/ddos-threats-attacks/threat-advisories-attack-reports/jenx/)
and
[Satori](https://ics-cert.kaspersky.com/publications/blog/2017/12/14/satori/)
, have embraced the
[same approach](https://www.fortinet.com/blog/threat-research/satori-adds-known-exploit-chain-to-slave-wireless-ip-cameras)
in the past.

"The botnet continues to expand by infecting a broad range of IoT devices across multiple architectures and manufacturers," Trellix said. "Notably, Masjesu appears to avoid targeting sensitive critical organizations that could trigger significant legal or law-enforcement attention, a strategy that likely improves its long-term survivability."