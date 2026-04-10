---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-10T10:15:13.357284+00:00'
exported_at: '2026-04-10T10:15:15.910242+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
structured_data:
  about: []
  author: ''
  description: Google releases DBSC in Chrome 146 for Windows, binding cookies to
    devices to reduce session theft and prevent unauthorized access.
  headline: Google Rolls Out DBSC in Chrome 146 to Block Session Theft on Windows
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Rolls Out DBSC in Chrome 146 to Block Session Theft on Windows
updated_at: '2026-04-10T10:15:13.357284+00:00'
url_hash: f10d6526aaeb3e7d638257c4f7eff6c37cdbf6e6
---

**

Ravie Lakshmanan
**

Apr 10, 2026

Malware / Browser Security

Google has made
**Device Bound Session Credentials**
(
[DBSC](https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html)
) generally available to all Windows users of its Chrome web browser, months after it
[began testing](https://thehackernews.com/2025/07/google-launches-dbsc-open-beta-in.html)
the security feature in open beta.

The public availability is currently limited to Windows users on Chrome 146, with macOS expansion planned in an upcoming Chrome release.

"This project represents a significant step forward in our ongoing efforts to combat session theft, which remains a prevalent threat in the modern security landscape," Google's Chrome and Account Security teams
[said](https://security.googleblog.com/2026/04/protecting-cookies-with-device-bound.html)
in a Thursday post.

Session theft involves the covert exfiltration of session cookies from the web browser, either by gathering existing ones or waiting for a victim to log in to an account, to an attacker-controlled server.

Typically, this happens when users inadvertently download information-stealing malware into their systems. These stealer malware families – of which there are many, such as Atomic, Lumma, and Vidar Stealer – come with capabilities to harvest a wide range of information from compromised systems, including cookies.

Because session cookies often have extended lifespans, attackers can leverage them to gain unauthorized access to victims' online accounts without having to know their passwords. Once collected, these tokens are packaged and sold to other threat actors for financial gain. Cybercriminals who acquire them can follow up with their attacks of their own.

DBSC, first
[announced](https://thehackernews.com/2024/04/google-chrome-beta-tests-new-dbsc.html)
by Google in April 2024, aims to counter this abuse by cryptographically tying the authentication session to a specific device. In doing so, the idea is to render cookies worthless even if they get stolen by malware.

"It does this using hardware-backed security modules, such as the Trusted Platform Module (TPM) on Windows and the Secure Enclave on macOS, to generate a unique public/private key pair that cannot be exported from the machine," Google explained.

"The issuance of new short-lived session cookies is contingent upon Chrome proving possession of the corresponding private key to the server. Because attackers cannot steal this key, any exfiltrated cookies quickly expire and become useless to those attackers."

In the event a user's device does not support secure key storage, DBSC gracefully falls back to standard behavior without breaking the authentication flow, Google
[said](https://developer.chrome.com/docs/web-platform/device-bound-session-credentials)
in its developer documentation.

The tech giant said it has observed a significant reduction in session theft since its launch, an early indication of the success of the countermeasure. The official launch is just the start, as the company plans to bring DBSC to a broader range of devices and introduce advanced capabilities to better integrate with enterprise environments.

Google, which worked with Microsoft to design the standard with an aim to make it an open web standard, also emphasized that the DBSC architecture is private by design and that the distinct key approach ensures that websites cannot use the session credentials to correlate a user's activity across different sessions or sites on the same device.

"Furthermore, the protocol is designed to be lean: it does not leak device identifiers or attestation data to the server beyond the per-session public key required to certify proof of possession," it added. "This minimal information exchange ensures DBSC helps secure sessions without enabling cross-site tracking or acting as a device fingerprinting mechanism."