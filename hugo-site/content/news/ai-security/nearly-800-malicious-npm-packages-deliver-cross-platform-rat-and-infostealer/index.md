---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-09T09:50:06.396264+00:00'
exported_at: '2026-08-09T09:50:08.412526+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
structured_data:
  about: []
  author: ''
  description: Nearly 800 malicious npm packages deliver a cross-platform RAT and
    infostealer, using WEL1DROPPER to target Windows, macOS, and Linux systems.
  headline: Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer
updated_at: '2026-08-09T09:50:06.396264+00:00'
url_hash: da919a79098b7d0333cf21650f02612de61fdb75
---

A cluster of nearly 800 malicious packages has been published to the npm registry as part of a new campaign designed to deliver cross-platform malware targeting Windows, Mac, and Linux systems.

"These packages appear to use AI slop squatted, or randomly generated typo-squatting package names, but all of them deliver a powerful RAT and infostealer payload," OpenSourceMalware researcher Paul McCarty
[said](https://opensourcemalware.com/blog/russian-ai-slopsquatting-npm-campaign)
.

Unlike other npm-oriented software supply chain attacks that make use of lifecycle hooks like preinstall or postinstall to trigger the execution of malicious code, the newly identified packages come with a README that instructs developers to load them with require(), a built-in function to import modules, local files, and third-party packages.

The attack leads to the execution of a downloader named
**[WEL1DROPPER](https://opensourcemalware.com/?search=%23wel1dropper)**
, which, when executed, identifies the host operating system and processor architecture and fetches a compatible payload from one of the three Cloudflare Workers hosts. The three Cloudflare Workers domains are listed below -

* oob-worker.cf103-070.workers[.]dev
* oob-worker.cf102-baf.workers[.]dev
* oob-worker.cf99-9b3.workers[.]dev

If the HTTPS-based downloads fail, the malware switches to a platform-specific domain and uses DNS TXT records to obtain the next-stage from the domain "wel1[.]ru." The payload domain for each operating system and CPU architecture is as follows -

* Linux x64 - sdk.dl.wel1[.]ru
* Linux ARM64 - ext.dl.wel1[.]ru
* macOS - pkg.dl.wel1[.]ru
* Windows - net.dl.wel1[.]ru

"The package first requests a TXT record from c.&lt;domain&gt;," McCarty explained. "It parses the response as the number of payload chunks, accepting a value between 1 and 2,000. It then requests numbered TXT records. The returned strings are joined together and Base64-decoded into a binary buffer."

In the final stage, the payload is written to a temporary folder and executed either using "/bin/sh" on Linux and macOS, or "cmd.exe" on Windows.

Sonatype, which is also
[tracking](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)
the campaign under the moniker Flooding Dropper, said the final stage is launched as a detached process, with the Windows version taking steps to patch Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) to interfere with monitoring, check for sandboxes and virtual environments, establish persistence through a Registry Run key and a scheduled task, and download an encrypted payload ("/pkg/update\_win.exe") and run it.

The macOS infection chain is similar, performing an identical set of actions to look for debuggers and analysis artifacts before retrieving a compatible payload ("/pkg/beacon\_mac.bin") from a remote server. If this fails, it employs the aforementioned DNS TXT delivery, sets up persistence using a LaunchAgent, and then starts the executable in a detached process.

The Linux sample, on the other hand, is an
[UPX-packed](https://www.iblue.team/malware-analysis/identifying-upx-packed-elf-decompressing-fixing-and-analysing-linux-malware)
ELF binary that's configured to download auxiliary payloads from a Cloudflare Worker URL ("oob-worker[.]cf99-9b3.workers[.]dev"), ultimately leading to the deployment of
[Sliver](https://thehackernews.com/2022/08/cybercrime-groups-increasingly-adopting.html)
, an open-source command-and-control (C2) framework.

The packages have also been found to contain a file called "lib/telemetry.js" that implements a plausible-looking telemetry SDK but also contains the same downloader logic.

"The package entry point does not import this file, and it contains no additional hard-coded infrastructure," OpenSourceMalware said. "The oversized telemetry implementation appears intended to add noise and make the malicious behavior look like native profiling or analytics functionality during a quick review."

The presence of domains like "tcsbank[.]ru" and "cloudpayments[.]ru" in the macOS payload indicates that the campaign could be targeting Russian financial institutions and mobile payments.

It's also suspected to be an evolution of a
[dependency confusion](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html)
campaign codenamed
[Moika](https://opensourcemalware.com/?search=%23moika)
that was observed earlier this April and saw over 250 packages published to the npm registry to steal environment information and deliver an operating system-specific second-stage payload.

The development comes as Palo Alto Networks Unit 42 documented multiple campaigns targeting npm and the Python Package Index (PyPI) repository -

* A set of
  [10 npm packages](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-08-06-Obfuscated-JavaScript-Crypto-Stealer.txt)
  that download an obfuscated cryptocurrency stealer and a remote access trojan from an external server. "After installation, the packages export a 'getPlugin' function that constructs the URL from which the payload is downloaded as an obfuscated IIFE (Immediately Invoked Function Expression) JavaScript code embedded in a JSON object," Unit 42 said. "The payload implements a crypto stealer and Remote-Access Trojan (RAT) that allows the attacker to execute arbitrary commands on the infected host."
* A set of
  [malicious packages across npm and PyPI](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-21-Malicious-npm-PyPI-Supply-Chain-packages.txt)
  representing multiple distinct threat actors that are capable of cloud credential exfiltration, delivering EtherHiding blockchain-based C2 droppers, Solana cryptocurrency wallet key theft via Telegram, .env file secret exfiltration, fake-CAPTCHA social engineering remote code execution, and Discord token theft and GitHub Actions CI/CD credential exfiltration.

### From Packages to Chrome Extensions

Threat actors have also been observed using Google Chrome extensions marketed as game emulators, password managers, productivity tools, CSS inspectors, and markdown converters to turn the web browser into a web crawling proxy. The crawl commands are received remotely via a persistent WebSocket connection.

"These extensions embed an identical commercial web bandwidth-sharing SDK that connects the user's browser to a 3rd party residential proxy network for web scraping operations," Unit 42
[said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-29-Browser-as-proxy-extensions.txt)
, adding it crawls pages by injecting a hidden iframe into active browser tabs, converts page content to Markdown in the background, and sends it to a remote cloud backend.

The cybersecurity company noted that some of these extensions disclose the practice in their Chrome Web Store descriptions and in the privacy policies on their SaaS websites. Once installed, the third-party SDK prompts users to opt-in to the service.

"While the proxy and crawling features remain inactive if the user declines, some extensions frame this opt-in as necessary for uninterrupted service,'" Unit 42 said. "A notable example is InstaSkip (mdondgockboebafloibbhjofmoedmnnn), which embeds this SDK."