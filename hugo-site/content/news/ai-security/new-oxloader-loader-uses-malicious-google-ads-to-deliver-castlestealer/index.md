---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:51:08.869835+00:00'
exported_at: '2026-06-23T03:51:10.693000+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html
structured_data:
  about: []
  author: ''
  description: Researchers detail REF8372, a malvertising campaign using fake Node.js
    ads, Storj-hosted payloads, and OXLOADER to deploy CastleStealer.
  headline: New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New OXLOADER Loader Uses Malicious Google Ads to Deliver CastleStealer
updated_at: '2026-06-23T03:51:08.869835+00:00'
url_hash: 8d498f2a085f91d884a30963bd2cc17ed14fe30d
---

**

Ravie Lakshmanan
**

Jun 22, 2026

Malvertising / Endpoint Security

Cybersecurity researchers have disclosed details of a new campaign that delivers CastleStealer by means of a previously unreported malware loader dubbed
**OXLOADER**
.

According to Elastic Security Labs, the campaign leverages malicious Google Ads as a starting point to distribute the malware. Evidence indicates that the threat actor is likely Russian-speaking and financially motivated, owing to the presence of explicit exclusions to prevent infecting machines located in the Commonwealth of Independent States (CIS) region. The campaign has been codenamed REF8372.

"The loader uses several obfuscation layers (control-flow flattening, opaque predicates, mixed Boolean-Arithmetic), self-modifying decryption stubs, and abuses the Windows .reloc section to stage shellcode," researchers Daniel Stepanic and Jia Yu Chan
[said](https://www.elastic.co/security-labs/oxloader-malware-loader-infostealer)
in a technical breakdown.

The attack begins when unsuspecting users enter queries such as "lts version of node.js" on search engines like Google, redirecting them to a fake website ("node-js[.]prentiva99[.]info") surfaced via bogus ads published under the verified name "ВОЛОДИМИР ТЕРЕЩЕНКО" that's purportedly based in Ukraine.

It's currently unknown if the advertiser account is linked to the actual threat actor, or if it's a front account or a purchased identity. The advertiser account, along with its ad campaigns, was removed from Google on May 14, 2026.

Users who end up interacting with the site are served a batch script hosted on Storj, a decentralized, open-source cloud storage platform. The abuse of Storj once again illustrates how threat actors continue to leverage legitimate services to evade domain-based reputation filters.

Running the batch script displays a bogus installation wizard user interface (UI), while stealthily downloading a next-stage payload, a
[Storj-hosted executable](https://www.virustotal.com/gui/file/9a9939dff297997732aaade9b243d695632cbd64033c5fbcb9de3d09b7e6c28d/detection)
dubbed OXLOADER through a PowerShell command and executing it with -Verb RunAs to trigger a Windows User Account Control (UAC) prompt.

The attack then employs DLL side-loading to launch a rogue DLL, which then proceeds to decrypt and execute the CastleStealer payload. OXLOADER also makes use of techniques like control-flow flattening (CFF) and mixed Boolean-Arithmetic (MBA) to evade static detection, while also taking steps to ensure it's not run on sandboxed environments.

CastleStealer is a .NET information stealer that was recently distributed alongside CastleLoader through a ClickFix-style lure masquerading as a free image-editing tool as part of a campaign codenamed
[BackgroundFix](https://thehackernews.com/2026/06/threatsday-bulletin-ai-agents-gone.html#fake-image-tools-deliver-malware)
. CastleLoader is
[attributed](https://thehackernews.com/2025/12/four-threat-clusters-using-castleloader.html)
to a threat activity cluster known as GrayBravo.

"OXLOADER is in an early operational phase, but the engineering behind it suggests this family is worth watching," Elastic said. "The code obfuscation, anti-VM measures, benign-looking code used to masquerade its binaries, and unique staging techniques reflect deliberate engineering choices to evade analysis."

"That investment is paying off, resulting in low detection rates across static engines and detonation runs, giving OXLOADER a window to operate before it gets hunted down."