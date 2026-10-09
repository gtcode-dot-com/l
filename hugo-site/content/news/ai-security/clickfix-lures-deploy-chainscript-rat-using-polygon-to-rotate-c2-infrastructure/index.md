---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:28:49.301270+00:00'
exported_at: '2026-10-03T23:28:50.989409+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html
structured_data:
  about: []
  author: ''
  description: ClickFix lures deliver the ChainScript RAT, which uses a Polygon smart
    contract to locate active WebSocket command-and-control servers.
  headline: ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure
updated_at: '2026-10-03T23:28:49.301270+00:00'
url_hash: 466b4f516547fabdb97a03a1f0764181bb9b9330
---

Threat actors are leveraging
[ClickFix-like lures](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
to deliver a previously undocumented remote access trojan (RAT) called
**ChainScript**
.

"ChainScript has appeared under multiple build names, including ComponentTask33, UpdateDigital, HostShared, and OrchidViolet66, while presenting itself as Spotify, Zoom Workplace, and Microsoft Teams software," Blackpoint Adversary Pursuit Group (APG) researchers Sam Decker, Andi Ursry, and Nevan Beal
[said](https://blackpointcyber.com/blog/chainscript-tracing-a-nodejs-rat-across-the-blockchain/)
.

Like many malware families observed in recent months, ChainScript employs an
[EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)
-style command-and-control (C2) discovery technique that makes use of a Polygon smart contract to locate its active WebSocket infrastructure.

ChainScript is a full-featured RAT that provides extensive remote access to the operator, including interactive CMD and PowerShell, file operations, screenshot capture, payload deployment, cryptocurrency wallet enumeration (both desktop apps and browser extensions), and remote JavaScript execution.

The starting point of the attack chain is a ClickFix lure that leads to the download and execution of a malicious Windows installer using "msiexec.exe." The installer ("ComponentTask33-4d14e6ac.msi"), disguised as Spotify, deploys the Node.js runtime and launches the ChainScript JavaScript agent through hidden PowerShell and VBScript stages.

The PowerShell script drops various components, namely, the runtime, agent source, configuration, and other auxiliary binaries, across different Microsoft-looking paths in the "%LOCALAPPDATA%" folder. The VBScript serves as the main launcher for ChainScript.

The running agent then establishes user level persistence through a scheduled task with a Registry Run key fallback. Upon execution, ChainScript connects to the C2 server over WebSockets and retrieves additional tasking, giving the threat actor direct control over the compromised system. The supported commands also allow it to self-update and remove persistence.

The findings illustrate how threat actors are increasingly adopting a flexible decentralized infrastructure as a way to resist takedown efforts and ensure uninterrupted operations.

"ChainScript reflects an emerging pattern of malware using development frameworks and blockchain-based C2 discovery to enable infrastructure rotation and complicate traditional indicator-based detection," Blackpoint said. "By separating backend discovery from the malware itself and using the Polygon contract as an external resolver, the operator can redirect infected hosts to new infrastructure while retaining the same implant and reconnect workflow."

### ClickFix, a Way for Mac and Windows Users to Infect Themselves

The disclosure comes as threat actors
[compromised](https://www.reddit.com/r/cybersecurity/comments/1w8gu91/reddit_infostealer_adverts/)
HBO Max's official Reddit account ("u/hbomax") and abused it to push malicious ads that launched ClickFix attacks to infect Windows and macOS devices with information-stealing malware. The activity has been codenamed PasteSwitch by
[Hudson Rock](https://www.hudsonrock.com/blog/hbo-max-ads-on-a-compromised-reddit-account-exposed-a-massive-pasteswitch-clickfix-operation)
and
[ADAMnetworks](https://adamnet.works/blog/hbo-max-ads-exposed-the-pasteswitch-clickfix-operation/)
. It's not known how the account was breached, and how many people clicked on these fake ads and how many were compromised as a result.

On macOS, PasteSwitch has been found to deliver MacSync, Atomic macOS Stealer (AMOS), and fake cryptocurrency wallet applications designed to steal recovery phrases. The Windows branch, on the other hand, distributes Amatera Stealer and cryptocurrency clippers like AnimateClipper and ZigClipper. In all, the verified Reddit account served 108 malicious ads over a 48-hour period in mid-September 2026.

According to data shared by Seqrite Labs, MacSync infections have concentrated in the U.S., followed by the U.K., Germany, Japan, Canada, France, Singapore, Australia, India, and the Netherlands. "MacSync campaigns primarily target regions with widespread macOS enterprise use, tech and software development sectors, and active cryptocurrency or Web3 communities," researcher Chandra Kant Bauri
[said](https://www.seqrite.com/blog/macsync-the-evasive-macos-stealer-exploiting-clickfix-lures/)
.

"The threat actors utilized highly polished assets to establish trust before delivering the malicious payload," Hudson Rock said. "By hijacking a verified corporate account, they bypassed the initial skepticism many users apply to internet advertisements."

The findings dovetail with another ClickFix campaign that employs a fake Codex download experience surfaced via search results to lead users to bogus Google Sites pages and trick macOS users into pasting a malicious command into Terminal, resulting in the execution of Atomic Stealer. Visitors using non-Mac devices are served a harmless decoy page.

"The copied Terminal command first retrieves a shell-script loader: the first stage," Cato Networks
[said](https://www.catonetworks.com/blog/cato-ctrl-when-trust-becomes-payload-in-fake-codex-clickfix-campaign/)
. "This loader contains an embedded blob that it decodes and executes with eval, producing the second-stage shell script. The second stage then records execution and retrieves the final, third-stage Mach-O payload."

The cybersecurity company described the activity as
[part](https://www.malwarebytes.com/blog/news/2026/05/fake-claude-search-results-lure-mac-users-into-clickfix-attack)
of a
[broader pattern](https://pushsecurity.com/blog/llmshare-malvertising-campaign)
of
[attacks](https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html)
that employ trusted services and large language model (LLM) shared chats to serve fake installation instructions, while bypassing browser warnings, URL inspection, and Safe Browsing heuristics.

In a report published last month, Microsoft said it observed a macOS ClickFix campaign propagating MacSync and Atomic Stealer using a cluster of no less than 250 look-alike domains.

"The campaign evolved from broadly serving ClickFix lures to using a server-side browser-fingerprinting gate that shows the lure primarily to visitors whose environment appears consistent with a genuine macOS browser," it
[said](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)
. "This cloaking limits visibility for crawlers, sandboxes, and some automated analysis workflows."