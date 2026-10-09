---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T03:16:50.617564+00:00'
exported_at: '2026-10-07T03:16:52.911274+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html
structured_data:
  about: []
  author: ''
  description: China-nexus UAT-11587 targets Asian government and policy groups with
    Antino, a Rust backdoor that uses Microsoft 365 for C2.
  headline: Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign
updated_at: '2026-10-07T03:16:50.617564+00:00'
url_hash: 7d8d9de996965fb985222ab0fbd85affc934f427
---

Government and policy organizations across Asia have become the target of a new campaign orchestrated by a China-nexus threat actor.

The activity, which has targeted government and policy organizations in Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, and Myanmar, involves the deployment of a previously undocumented backdoor codenamed Antino. Cisco Talos is tracking the cluster under the moniker
**UAT-11587**
.

The threat actor was first detected in September 2025 in connection with a spear-phishing campaign directed against Taiwan's academic, think tank, and civil society policy community. Since then, attacks linked to the intrusion set have expanded to target 16 entities across eight Asian countries.

"Antino is a Rust-compiled Windows backdoor that supports host reconnaissance, shell and PowerShell execution, file transfer, in-memory shellcode loading and persistence," security researcher Ashley Shen
[said](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)
. "Its native command-and-control channel operates exclusively through Microsoft 365, using Microsoft Graph to interact with Outlook and OneDrive."

UAT-11587 is assessed to share some level of overlap with Jewelbug, which, in turn, exhibits tactical similarities with China-aligned clusters known as CL-STA-0049, Earth Alux, Ink Dragon, and REF7707. A report published by Broadcom-owned Symantec and Carbon Black in August 2026
[characterized](https://thehackernews.com/2026/08/china-linked-jewelbug-uses-xg-web-for.html)
Jewelbug as a China-based hackers-for-hire group that carries out espionage operations and a for-profit cryptocurrency fraud business.

However, Cisco Talos said its own investigation has failed to unearth a connection between the espionage campaign and Jewelbug's financially motivated activity, prompting it to designate UAT-11587 as a separate activity set.

The challenges in establishing definitive links notwithstanding, the adversary has been classified as China-nexus with high confidence, citing the presence of zh-CN language and Simplified Chinese metadata in the lure documents and the UTC+08:00 time zone in the spear-phishing message header.

"The campaign's lure theme and targeting provide additional contextual support," Talos said. "Its lures and observed targets include Taiwanese political, legislative, civil defense, and policy research subjects, together with regional government, maritime, diplomatic, and security themes. This collection focus is consistent with China-nexus actor interests."

Two other indicators that point to a China-nexus are below -

* Nearly a dozen distinct Antino build outputs feature Cargo registry paths referencing rsproxy[.]cn, a high-speed domestic mirror and proxy service for crates.io catering to mainland China
* A JavaScript downloader associated with UAT-11587 that references "d32tpl7xt7175h.cloudfront[.]net," a CloudFront domain previously flagged by Arctic Wolf in connection with a campaign conducted by a China-affiliated threat actor known as
  [UNC6384](https://thehackernews.com/2025/10/china-linked-hackers-exploit-windows.html)
  targeting European diplomatic and government entities last year using an unpatched Windows shortcut vulnerability.

Evidence indicates that UAT-11587 has also trained its sights on organizations in Syria around May 2026, indicating a focus beyond Asia. Attacks mounted by the threat actor have been found to spike between March and early June 2026, with a "concentrated wave" taking place on June 8 and 9, 2026, targeting dozens of systems associated with government IT infrastructure.

While the choice of spear-phishing as an initial access vector is unsurprising, the choice of the lures employed suggests the threat actor conducted extensive reconnaissance of the target organizations in order to tailor the content and maximize the chance of success.

In an attempt to lend credibility to the emails, UAT-11587 is said to have spoofed sender identities trusted by the intended recipients to bypass
[SPF and DMARC security checks](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)
and ensure that the messages land on the victims' inboxes.

"Another social engineering technique used for initial access in this campaign was the closely replicated reconstruction of Gmail's native attachment preview widget inside the email HTML body," Shen explained. "The actor replicated the styling of Gmail's attachment card using four inline PNG images embedded as Base64-encoded MIME parts."

"The entire attachment card was wrapped in an anchor tag pointing to an attacker-controlled [Cloudflare Pages] URL. When a Gmail user opens the email in a browser, Gmail's renderer faithfully displays the attacker-controlled HTML, producing a fake attachment widget that is visually indistinguishable from a legitimate Gmail attachment preview."

An analysis of the lures demonstrates a propensity to target audiences interested in foreign affairs, international security, and government policy, Talos added. The attack chain itself is a five-stage process that begins with a HTA or WSF stager and culminates in the deployment of Antino.

The Cloudflare URL in the phishing email leads to the download of an HTA or WSF file that's then executed to retrieve a JavaScript downloader and decryptor. The next stage triggers a .NET deserialization chain to load "TestAssembly.dll," a .NET downloader and launcher that's responsible for three actions -

* Download and open the lure document to the victim.
* Download a decoy Calculator executable.
* Download and launch the Antino backdoor.

The implant ("slc.dll") is launched by means of DLL sideloading using a legitimate Microsoft-signed binary ("GatherOsState.exe"). Once launched, the Rust-compiled malware communicates with Microsoft 365 applications and uses Outlook and OneDrive objects as dead drops, instead of depending on a conspicuous dedicated command-and-control (C2) server.

Antino is no different from other backdoors of its kind in that it supports host reconnaissance, command execution, and persistence. It can also list running processes, enumerate directories, run PowerShell scripts, shellcode, operator-supplied programs, and commands using "cmd.exe"

For C2, it uses Outlook for command exchange and OneDrive for heartbeat and file transfer. Specifically, it fetches commands from the threat actor's Outlook mailbox folder every 10 seconds by looking for messages with the subject prefix "command\_req\_[session\_id]."

"The Antino backdoor abuses the Windows Scripted Diagnostics framework to execute attacker-controlled PowerShell through legitimate Windows components," Talos said. "This can complicate behavioral attribution to the original implant, although it does not eliminate observable PowerShell, file-creation, or Registry telemetry."