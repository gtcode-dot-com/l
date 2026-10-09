---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T20:15:14.326659+00:00'
exported_at: '2026-04-08T20:15:16.543529+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html
structured_data:
  about: []
  author: ''
  description: Chaos malware targets misconfigured cloud deployments, detected by
    Darktrace in 2025, expanding botnet monetization via proxy services.
  headline: New Chaos Variant Targets Misconfigured Cloud Deployments, Adds SOCKS
    Proxy
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/new-chaos-variant-targets-misconfigured.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Chaos Variant Targets Misconfigured Cloud Deployments, Adds SOCKS Proxy
updated_at: '2026-04-08T20:15:14.326659+00:00'
url_hash: 4954e711034450368989fedf1445163372e84465
---

**

Ravie Lakshmanan
**

Apr 08, 2026

Cryptomining / Network Security

Cybersecurity researchers have flagged a new variant ofmalware called
**Chaos**
that'scapable of hitting misconfigured cloud deployments, marking an expansion of the botnet's targeting infrastructure.

"Chaos malware is increasingly targeting misconfigured cloud deployments, expanding beyond its traditional focus on routers and edge devices," Darktrace
[said](https://www.darktrace.com/blog/darktrace-identifies-new-chaos-malware-variant-exploiting-misconfigurations-in-the-cloud)
in a new report.

Chaos was
[first documented](https://thehackernews.com/2022/09/researchers-warn-of-new-go-based.html)
by Lumen Black Lotus Labs in September 2022, describing it as a cross-platform malware capable of targeting Windows and Linux environments to run remote shell commands, drop additional modules, propagate to other hosts by brute-forcing SSH keys, mine cryptocurrency, and launch distributed denial-of-service (DDoS) attacks via HTTP, TLS, TCP, UDP, and WebSocket.

The malware is assessed to be an evolution of another DDoS malware known as
[Kaiji](https://thehackernews.com/2025/12/react2shell-exploitation-delivers.html)
that has singled out misconfigured Docker instances.It's currently not known who is behind the operation, but the presence of Chinese language characters and the use of China-based infrastructure suggest that the threat actor could be of Chinese origin.

Darktrace said it identified the new variant targeting its honeypot network last month, a deliberately misconfigured Hadoop instance that enables remote code execution on the service. In the attack spotted by the cybersecurity company, the intrusion commenced with an HTTP request to the Hadoop deployment to create a new application.

The application, for its part, embedded a sequence of shell commands to retrieve a Chaos agent binary from an attacker-controlled server ("pan.tenire[.]com"), set permissions to allow all users to read, modify, or run it ("chmod 777"), and then actually execute the binary and delete the artifact from disk to minimize the forensic trail.

An interesting aspect of the attack is that the domain was previously put to use in connection with an email phishing campaign carried out by the Chinese cybercrime group Silver Fox to deliver decoy documents and ValleyRAT malware. The campaign was codenamed
[Operation Silk Lure](https://thehackernews.com/2025/10/silver-fox-expands-winos-40-attacks-to.html#operation-silk-lure-targets-china-with-valleyrat)
by Seqrite Labs in October 2025.

The 64-bit ELF binary is a restructured and updated version of Chaos that reworks several of its functions, while keeping most of its core feature set intact. One of the more significant changes, however, concerns the removal of functions that enabled it to spread via SSH and exploit router vulnerabilities.

Taking their place is a new SOCKS proxy feature that allows the compromised system to be used for ferrying traffic, thereby concealing the true origins of malicious activity and making it harder for defenders to detect and block the attack.

"In addition, several functions that were previously believed to be inherited from Kaiji have also been changed, suggesting that the threat actors have either rewritten the malware or refactored it extensively," Darktrace added.

The addition of the proxy feature is likely a sign that threat actors behind the malware are lookingto further monetize the botnet beyond cryptocurrency mining and
[DDoS-for-hire](https://thehackernews.com/2026/04/masjesu-botnet-emerges-as-ddos-for-hire.html)
, and keep up with their competitors in the cybercrime market by offering a diverse slate of illicit services.

"While Chaos is not a new malware, its continued evolution highlights the dedication of cybercriminals to expand their botnets and enhance the capabilities at their disposal," Darktrace concluded. "The recent shift in botnets such as
[AISURU](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html)
and Chaos to include proxy services as core features demonstrates that denial-of-service is no longer the only risk these botnets pose to organizations and their security teams."