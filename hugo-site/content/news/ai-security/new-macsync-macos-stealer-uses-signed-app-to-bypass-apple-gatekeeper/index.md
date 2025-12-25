---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-25T00:03:18.560643+00:00'
exported_at: '2025-12-25T00:03:21.025060+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html
structured_data:
  about: []
  author: ''
  description: A new MacSync macOS stealer spreads via a signed, notarized fake installer,
    bypassing Apple Gatekeeper before Apple revoked the certificate.
  headline: New MacSync macOS Stealer Uses Signed App to Bypass Apple Gatekeeper
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New MacSync macOS Stealer Uses Signed App to Bypass Apple Gatekeeper
updated_at: '2025-12-25T00:03:18.560643+00:00'
url_hash: 27f31df1b6a61aae8708c9cfb41de558ffc7d98f
---

**

Dec 24, 2025
**

Ravie Lakshmanan

Malware / Endpoint Security

Cybersecurity researchers have discovered a new variant of a macOS information stealer called
**MacSync**
that's delivered by means of a digitally signed, notarized Swift application masquerading as a messaging app installer to bypass Apple's Gatekeeper checks.

"Unlike earlier MacSync Stealer variants that primarily rely on drag-to-terminal or
[ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)
-style techniques, this sample adopts a more deceptive, hands-off approach," Jamf researcher Thijs Xhaflaire
[said](https://www.jamf.com/blog/macsync-stealer-evolution-code-signed-swift-malware-analysis/)
.

The Apple device management firm and security company said the latest version is distributed as a code-signed and notarized Swift application within a disk image (DMG) file named "zk-call-messenger-installer-3.9.2-lts.dmg" that's hosted on "zkcall[.]net/download."

The fact that it's signed and notarized means it can be run without being blocked or flagged by built-in security controls like Gatekeeper or XProtect. Despite this, the installer has been found to display instructions prompting users to right-click and open the app – a common tactic used to sidestep such safeguards. Apple has since revoked the code signing certificate.

The Swift-based dropper then performs a series of checks before downloading and executing an encoded script through a helper component. This includes verifying internet connectivity, enforcing a minimum execution interval of around 3600 seconds to enforce a rate limit, and removing quarantine attributes and validating the file prior to execution.

"Notably, the curl command used to retrieve the payload shows clear deviations from earlier variants," Xhaflaire explained. "Rather than using the commonly seen -fsSL combination, the flags have been split into -fL and -sS, and additional options like --noproxy have been introduced."

"These changes, along with the use of dynamically populated variables, point to a deliberate shift in how the payload is fetched and validated, likely aimed at improving reliability or evading detection."

Another evasion mechanism used in the campaign is the use of an unusually large DMG file, inflating its size to 25.5 MB by embedding unrelated PDF documents.

The Base64-encoded payload, once parsed, corresponds to
[MacSync](https://g0njxa.medium.com/approaching-stealers-devs-a-brief-interview-with-macsync-ex-mentalpositive-62504db3e761)
, a rebranded version of
[Mac.c](https://moonlock.com/new-mac-stealer-spreading)
that first emerged in April 2025. MacSync, per MacPaw's Moonlock Lab,
[comes fitted](https://moonlock.com/macc-stealer-macsync-backdoor)
with a fully-featured Go-based agent that goes beyond simple data theft and enables remote command and control capabilities.

It's worth noting that code-signed versions of malicious DMG files mimicking Google Meet have also been observed in attacks propagating other macOS stealers like
[Odyssey](https://www.jamf.com/blog/signed-and-stealing-uncovering-new-insights-on-odyssey-infostealer/)
. That said, threat actors have continued to rely on unsigned disk images to deliver
[DigitStealer](https://www.jamf.com/blog/jtl-digitstealer-macos-infostealer-analysis/)
as recently as last month.

"This shift in distribution reflects a broader trend across the macOS malware landscape, where attackers increasingly attempt to sneak their malware into executables that are signed and notarized, allowing them to look more like legitimate applications," Jamf said.