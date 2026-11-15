---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T02:41:05.585627+00:00'
exported_at: '2026-11-15T02:41:06.795395+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/researchers-find-residential-proxies-on-white-house-network
structured_data:
  about: []
  author: ''
  description: Windows computers on the White House network run the InfaticaSDK, which
    is used by numerous residential proxy services.
  headline: Researchers Find Residential Proxies on White House Network
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/researchers-find-residential-proxies-on-white-house-network
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers Find Residential Proxies on White House Network
updated_at: '2026-11-15T02:41:05.585627+00:00'
url_hash: f98f424c210d11ce28447d675f785b1144b4add9
---

**Security researchers have discovered multiple computers on the White House network that are used as residential proxy exit nodes.**

According to Layer3 Intel, six IP addresses on AS2650, the network reserved for the Executive Office of the President, were used by 28 residential proxy services between October 5 and November 3.

“Our residential proxy enumeration pipeline exited through the White House network 236 separate times,”
[Layer3 Intel](https://layer3intel.com/blog/residential-proxies-white-house-network)
says.

These exits, the security firm says, can be used by anyone signing up to a public residential proxy service to send requests through them.

Most of the observed activity happens in the evening, between 5 p.m. and midnight, Eastern Time, and almost none in the early morning.

“That pattern suggests a person rather than a public guest Wi-Fi network: someone regularly on the White House network late into the evening, whose device is infected with a proxy SDK,” Layer3 Intel notes.

Advertisement. Scroll to continue reading.

According to cybersecurity startup
[Synthient](https://x.com/synthient/status/2118115310922518777)
, which specializes in identifying residential proxies, VPNs, and bot infrastructure, the traffic comes from Windows 11 machines running the InfaticaSDK.

Based in Singapore, Infatica is a web-data intelligence and proxy service provider that claims to provide access to more than 45 million ethically sourced residential, mobile, and datacenter IP addresses worldwide.

Infatica’s founder Vladimir Fomenko also owns web hosting and IT infrastructure provider King Servers, which hosted “six of the eight internet addresses” that Russian state-sponsored hackers used in the 2016
[US election attacks](https://www.securityweek.com/us-election-assistance-commission-hacked/)
, investigative journalist Brian Krebs
[reports](https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/)
.

Per Layer3 Intel’s report, residential proxies have reached every corner of the world, even some of the most isolated places, such as the South Atlantic territory Saint Helena, Ascension and Tristan da Cunha.

“We recorded 413 addresses and more than 32,000 observations there, split between Starlink and the island’s local internet provider, Sure Saint Helena,” the company says.

Residential proxy exits were also observed in Antarctica, the Chagos Islands, the Falklands, Norfolk Island, Pitcairn, South Georgia, Svalbard, and Tokelau.

**Related:**
[AI-Linked Breaches Mount as WorkOS, Northflank, Trigger.dev Disclose Hacks](https://www.securityweek.com/ai-linked-breaches-mount-as-workos-northflank-trigger-dev-disclose-hacks/)

**Related:**
[AI Agents Got Root on Linux via 948 Kernel Flaws in OpenAI Research](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)

**Related:**
[Bank Phishing Sites Show Fake ‘Suspended’ Pages to Evade Takedowns](https://www.securityweek.com/bank-phishing-sites-show-fake-suspended-pages-to-evade-takedowns/)

**Related:**
[CISO Conversations: Ryan Davis – The Unknown Is Where Security Meets Reality](https://www.securityweek.com/ciso-conversations-ryan-davis-the-unknown-is-where-security-meets-reality/)