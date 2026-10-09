---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T04:45:10.534111+00:00'
exported_at: '2026-03-09T04:45:13.388198+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/north-korean-hackers-publish-26-npm.html
structured_data:
  about: []
  author: ''
  description: North Korean-linked campaign publishes 26 malicious npm packages hiding
    C2 in Pastebin, deploying credential stealers & RAT via 31 Vercel deployments.
  headline: North Korean Hackers Publish 26 npm Packages Hiding Pastebin C2 for Cross-Platform
    RAT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/north-korean-hackers-publish-26-npm.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: North Korean Hackers Publish 26 npm Packages Hiding Pastebin C2 for Cross-Platform
  RAT
updated_at: '2026-03-09T04:45:10.534111+00:00'
url_hash: 5b8666f4a26c50425ee8c8152a23726dce849948
---

**

Ravie Lakshmanan
**

Mar 02, 2026

Supply Chain Attack / Malware

Cybersecurity researchers have disclosed a new iteration of the ongoing
[Contagious Interview](https://thehackernews.com/2026/02/fake-nextjs-repos-target-developers.html)
campaign, where the North Korean threat actors have published a set of 26 malicious packages to the npm registry.

The packages masquerade as developer tools, but contain functionality to extract the actual command-and-control (C2) by using seemingly harmless Pastebin content as a dead drop resolver and ultimately drop a developer-targeted credential stealer and remote access trojan. The C2 infrastructure is hosted on Vercel across 31 deployments.

The
[campaign](https://kmsec.uk/blog/dprk-text-steganography/)
, discovered by Socket and kmsec.uk's Kieran Miyamoto, is being tracked under the moniker
**StegaBin**
. It's attributed to a North Korean threat activity cluster known as Famous Chollima.

"The loader extracts C2 URLs steganographically encoded within three Pastebin pastes, innocuous computer science essays in which characters at evenly-spaced positions have been replaced to spell out hidden infrastructure addresses," Socket researchers Philipp Burckhardt and Peter van der Zee
[said](https://socket.dev/blog/stegabin-26-malicious-npm-packages-use-pastebin-steganography)
.

The list of the malicious npm packages is as follows -

* argonist@0.41.0
* bcryptance@6.5.2
* bee-quarl@2.1.2
* bubble-core@6.26.2
* corstoken@2.14.7
* daytonjs@1.11.20
* ether-lint@5.9.4
* expressjs-lint@5.3.2
* fastify-lint@5.8.0
* formmiderable@3.5.7
* hapi-lint@19.1.2
* iosysredis@5.13.2
* jslint-config@10.22.2
* jsnwebapptoken@8.40.2
* kafkajs-lint@2.21.3
* loadash-lint@4.17.24
* mqttoken@5.40.2
* prism-lint@7.4.2
* promanage@6.0.21
* sequelization@6.40.2
* typoriem@0.4.17
* undicy-lint@7.23.1
* uuindex@13.1.0
* vitetest-lint@4.1.21
* windowston@3.19.2
* zoddle@4.4.2

All identified packages come with an install script ("install.js") that's automatically executed during package installation, which, in turn, runs the malicious payload located in "vendor/scrypt-js/version.js." Another common aspect that unites the 26 packages is that they explicitly declare the legitimate package they are typosquatting as a dependency, likely in an attempt to make them appear credible.

The payload serves as a text steganography decoder by contacting a Pastebin URL and extracting its contents to retrieve the actual C2 Vercel URLs. While the pastes seemingly contain a benign essay about computer science, the decoder is designed to look at specific characters in certain positions in the text and string them together to create a list of C2 domains.

"The decoder strips zero-width Unicode characters, reads a 5-digit length marker from the beginning, calculates evenly-spaced character positions throughout the text, and extracts the characters at those positions," Socket said. "The extracted characters are then split on a ||| separator (with an ===END=== termination marker) to produce an array of C2 domain names."

The malware then reaches out to the decoded domain to fetch platform-specific payloads for Windows, macOS, and Linux, a tactic widely observed in the Contagious Interview campaign. One such domain, "ext-checkdin.vercel[.]app" has been found to serve a shell script, which then contacts the same URL to retrieve a RAT component.

The Trojan connects to 103.106.67[.]63:1244 to await further instructions that allow it to change the current directory and execute shell commands, through which a comprehensive intelligence collection suite is deployed. It contains nine modules to facilitate Microsoft Visual Studio Code (VS Code) persistence, keylogging and clipboard theft, browser credential harvesting, TruffleHog secret scanning, and Git repository and SSH key exfiltration -

* **vs**
  , which uses a malicious tasks.json file to contact a Vercel domain every time a project is opened in VS Code by taking advantage of the
  [runOn: "folderOpen" trigge](https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html)
  r. The module specifically scans the victim's VS Code config directory across all three platforms and writes the malicious tasks.json directly into it.
* **clip**
  , which acts as a keylogger, mouse tracker, and clipboard stealer with support for active window tracking and conducts periodic exfiltration every 10 minutes.
* **bro**
  , which is a Python payload to steal browser credential stores.
* **j**
  , which is a Node.js module used for browser and cryptocurrency theft by targeting Google Chrome, Brave, Firefox, Opera, and Microsoft Edge, and extensions like MetaMask, Phantom, Coinbase Wallet, Binance, Trust, Exodus, and Keplr, among others. On macOS, it also targets the iCloud Keychain.
* **z**
  , which enumerates the file system and steals files matching certain predefined patterns.
* **n**
  , which acts as a RAT to grant the attacker the ability to remotely control the infected host in real-time via a persistent WebSocket connection to 103.106.67[.]63:1247 and exfiltrate data of interest over FTP.
* **truffle**
  , which downloads the legitimate
  [TruffleHog secrets scanner](https://github.com/trufflesecurity/trufflehog)
  from the official GitHub page to discover and exfiltrate developer secrets.
* **git**
  , which collects files from .ssh directories, extracts Git credentials, and scans repositories.
* **sched**
  , which is the same as "vendor/scrypt-js/version.js" and is redeployed as a persistence mechanism.

"While previous waves of the Contagious Interview campaign relied on relatively straightforward malicious scripts and Bitbucket-hosted payloads, this latest iteration demonstrates a concerted effort to bypass both automated detection and human review," Socket concluded.

"The use of character-level steganography on Pastebin and multi-stage Vercel routing points to an adversary that is refining its evasion techniques and attempting to make its operations more resilient."

The disclosure comes as the North Korean actors have also been observed publishing malicious npm packages (e.g., express-core-validator) to fetch a next-stage JavaScript payload hosted on Google Drive.

"Only a single package has been published with this new technique," Miyamoto
[said](https://kmsec.uk/blog/dprk-gdrive-stager/)
. "It is likely Famous Chollima will continue to leverage multiple techniques and infrastructure to deliver follow-on payloads. It is unlikely this signals a complete overhaul of their stager behaviour on npm."