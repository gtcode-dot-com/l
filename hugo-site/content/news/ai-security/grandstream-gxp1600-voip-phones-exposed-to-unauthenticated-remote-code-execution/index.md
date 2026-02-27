---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-27T06:25:15.560875+00:00'
exported_at: '2026-02-27T06:25:18.601593+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/grandstream-gxp1600-voip-phones-exposed.html
structured_data:
  about: []
  author: ''
  description: Critical CVE-2026-2329 flaw in Grandstream GXP1600 VoIP phones enables
    unauthenticated RCE, call interception, and credential theft.
  headline: Grandstream GXP1600 VoIP Phones Exposed to Unauthenticated Remote Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/grandstream-gxp1600-voip-phones-exposed.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Grandstream GXP1600 VoIP Phones Exposed to Unauthenticated Remote Code Execution
updated_at: '2026-02-27T06:25:15.560875+00:00'
url_hash: 83d30863392a0bdb66cc1eb996226673f0f66033
---

**

Ravie Lakshmanan
**

Feb 18, 2026

Network Security / Enterprise Security

Cybersecurity researchers have disclosed a critical security flaw in the Grandstream GXP1600 series of VoIP phones that could allow an attacker to seize control of susceptible devices.

The vulnerability, tracked as
**CVE-2026-2329**
, carries a CVSS score of 9.3 out of a maximum of 10.0. It has been described as a case of unauthenticated stack-based buffer overflow that could result in remote code execution.

"A remote attacker can leverage CVE-2026-2329 to achieve unauthenticated remote code execution (RCE) with root privileges on a target device," Rapid7 researcher Stephen Fewer, who discovered and reported the bug on January 6, 2026,
[said](https://www.rapid7.com/blog/post/ve-cve-2026-2329-critical-unauthenticated-stack-buffer-overflow-in-grandstream-gxp1600-voip-phones-fixed/)
.

According to the cybersecurity company, the issue is rooted in the device's web-based API service ("/cgi-bin/api.values.get") and is accessible in a default configuration without requiring authentication.

This endpoint is designed to fetch one or more configuration values from the phone, such as the firmware version number or the model, through a colon-delimited string in the "request" parameter (e.g., "request=68:phone\_model"), which is then parsed to extract each identifier and append it to a 64 byte buffer on the stack.

"When appending another character to the small 64 byte buffer, no length check is performed to ensure that no more than 63 characters (plus the appended null terminator) are ever written to this buffer," Fewer explained. "Therefore, an attacker-controlled 'request' parameter can write past the bounds of the small 64 byte buffer on the stack, overflowing into adjacent stack memory."

This means that a malicious colon-delimited "request" parameter sent as part of an HTTP request to the "/cgi-bin/api.values.get" endpoint can be used to trigger a stack-based buffer overflow, allowing the threat actors to corrupt the stack contents and ultimately achieve remote code execution on the underlying operating system.

The vulnerability affects GXP1610, GXP1615, GXP1620, GXP1625, GXP1628, and GXP1630 models. It has been addressed as part of a
[firmware update](https://www.grandstream.com/support/firmware)
(
[version 1.0.7.81](https://firmware.grandstream.com/Release_Note_GXP16xx_1.0.7.81.pdf)
) released late last month.

In a
[Metasploit exploit module](https://github.com/rapid7/metasploit-framework/pull/20983)
developed by Rapid7, it has been demonstrated that the vulnerability could be exploited to gain root privileges on a vulnerable device and chain it with a post-exploitation component to extract credentials stored on a compromised device.

Furthermore, the remote code execution capabilities can be weaponized to reconfigure the target device to use a malicious Session Initiation Protocol (SIP) proxy, effectively enabling the attacker to intercept phone calls to and from the device and eavesdrop on VoIP conversations. A
[SIP proxy](https://www.nextiva.com/blog/sip-proxy-server.html)
is an intermediary server in VoIP networks to establish and manage voice/video calls between endpoints.

"This isn't a one-click exploit with fireworks and a victory banner," Rapid7's Douglas McKee
[said](https://www.rapid7.com/blog/post/ve-phone-listening-cold-war-vulnerability-modern-voip/)
. "But the underlying vulnerability lowers the barrier in a way that should concern anyone operating these devices in exposed or lightly-segmented environments."