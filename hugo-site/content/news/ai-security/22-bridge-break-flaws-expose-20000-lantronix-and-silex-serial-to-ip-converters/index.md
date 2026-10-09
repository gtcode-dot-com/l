---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-21T16:15:14.347097+00:00'
exported_at: '2026-04-21T16:15:17.363061+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/22-bridgebreak-flaws-expose-20000.html
structured_data:
  about: []
  author: ''
  description: 22 BRIDGE:BREAK flaws in Lantronix and Silex converters expose nearly
    20,000 devices online, enabling takeover and data tampering.
  headline: 22 BRIDGE:BREAK Flaws Expose 20,000 Lantronix and Silex Serial-to-IP Converters
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/22-bridgebreak-flaws-expose-20000.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 22 BRIDGE:BREAK Flaws Expose 20,000 Lantronix and Silex Serial-to-IP Converters
updated_at: '2026-04-21T16:15:14.347097+00:00'
url_hash: aacfbeb7a9c6180a59ec5d0016b748469a13f728
---

**

Ravie Lakshmanan
**

Apr 21, 2026

Network Security / Vulnerability

Cybersecurity researchers have identified 22 new vulnerabilities in popular models of serial-to-IP converters from Lantronix and Silex that could be exploited to hijack susceptible devices and tamper with data exchanged by them.

The vulnerabilities have been collectively codenamed
**[BRIDGE:BREAK](https://www.forescout.com/research-labs/bridgebreak-vulnerabilities-thrive-in-serial-to-ethernet-converters/)**
by Forescout Research Vedere Labs, which identified nearly 20,000 Serial-to-Ethernet converters exposed online globally.

"Some of these vulnerabilities allow attackers to take full control of mission-critical devices connected via serial links," the cybersecurity company said in a report shared with The Hacker News.

Serial-to-IP converters are hardware devices that enable users to remotely access, control, and manage any serial device over an IP network or the internet by "bridging" legacy applications and industrial control systems (ICS) that operate over TCP/IP.

At a high level, as many as eight security flaws have been discovered in Lantronix products (EDS3000PS Series and EDS5000 Series) and 14 in Silex SD330-AC. These shortcomings fall under the following broad categories -

* Remote code execution - CVE-2026-32955, CVE-2026-32956, CVE-2026-32961, CVE-2025-67041, CVE-2025-67034, CVE-2025-67035, CVE-2025-67036, CVE-2025-67037, and CVE-2025-67038
* Client-side code execution - CVE-2026-32963
* Denial-of-service (DoS) - CVE-2026-32961, CVE-2015-5621, CVE-2024-24487
* Authentication bypass - CVE-2026-32960, CVE-2025-67039
* Device takeover - FSCT-2025-0021 (no CVE assigned), CVE-2026-32965, CVE-2025-70082
* Firmware tampering - CVE-2026-32958
* Configuration tampering - CVE-2026-32962, CVE-2026-32964
* Information disclosure - CVE-2026-32959
* Arbitrary file upload - CVE-2026-32957

Successful exploitation of the aforementioned flaws could allow attackers to disrupt serial communications with field assets, conduct lateral movement, and tamper with sensor values or modify actuator behavior.

In a hypothetical attack scenario, a threat actor could gain initial access to a remote facility through an
[internet-exposed edge device](https://thehackernews.com/2026/01/poland-attributes-december-cyber.html)
, such as an industrial router or firewall, and then weaponize BRIDGE:BREAK vulnerabilities to compromise the serial-to-IP converter, and alter serial data moving to or from the IP network.

Lantronix and Silex have released security updates to address the identified issues -

Besides applying patches, users are advised to replace default credentials, avoid using weak passwords, segment networks to prevent bad actors from reaching vulnerable serial-to-IP converters or using them as jumping-off points to other critical assets, and ensure the devices are not exposed to the internet.

"This research highlights weaknesses in serial-to-IP converters and the risks they can introduce in critical environments," Forescout said. "As these devices are increasingly deployed to connect legacy serial equipment to IP networks, vendors and end-users should treat their security implications as a core operational requirement."