---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T01:03:54.344447+00:00'
exported_at: '2026-10-08T01:03:55.969218+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html
structured_data:
  about: []
  author: ''
  description: Eight malicious npm packages downloaded 40,767 times deliver Overlord
    RAT, a Node.js stealer, and a downloader to Windows systems.
  headline: Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord
    RAT and Stealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and
  Stealer
updated_at: '2026-10-08T01:03:54.344447+00:00'
url_hash: 9882c305bcdbedb2e0c53445285d4b32da898ab8
---

**

Ravie Lakshmanan
**

Oct 07, 2026

Supply Chain / Malware

Cybersecurity researchers have disclosed details of a long-running npm supply chain malware campaign that pushes information stealers and remote access trojans (RAT) to compromised hosts.

The campaign has been codenamed
**MALFEX**
by
[CloudSEK](https://www.cloudsek.com/blog/malfex-malicious-npm-postinstall-supply-chain-campaign)
and
[Checkmarx](https://checkmarx.com/zero-post/malfex-npm-malware-campaign-three-payloads-and-an-adversary-that-signs-their-work/)
. The activity is assessed to be the work of a lone threat actor who appears to have published 12 packages since August 2023, eight of which have been flagged as malicious.

* The attack is designed to infect Windows systems through three separate pathways -
* A loader for
  [Overlord](https://github.com/vxaboveground/Overlord)
  , an open-source RAT written in Go that uses Solana transactions to extract the command-and-control (C2) address
* A chain that installs movinlike, a Node.js stealer targeting Discord, browsers, Telegram, and cryptocurrency wallets, and
* A downloader

The list of identified malicious packages is below -

* tlxbnhd
* tldriver
* mxdriver
* img-to-native
* native-runner
* function-flag (Still live)
* function-color (Still live)
* cdn-img-fetch (Still live)

In all, these packages have been collectively downloaded 40,767 times. Of these, 37,419 downloads correspond to "function-flag," making it the largest driver of this activity. The package was first published in July 2024. The latest version was released on August 4, 2025.

The project description for the npm package features a welcome message written in Portuguese that states: "This project was created with a lot of love and dedication by the Malfex team, whose owner is Murizada."

Three of the packages, "tlxbnhd," "tldriver," and "mxdriver," act as Overlord RAT loaders, with the malicious code triggered via lifecycle hooks to download and run a Windows executable.

A second subset of the npm packages, such as "img-to-native," requires "cdn-img-fetch" to retrieve and execute a Go executable, which then fetches a Node.js stealer capable of harvesting sensitive data.

Present within "function-flag" is a postinstall hook that runs a JavaScript payload to download a payload from a remote server. Each version of the package has been found to serve a payload from a different location. The "function-color" package embeds no payload of its own, but lists "function-flag" as a dependency.

"In 1.7.3, the current latest version, the postinstall script runs example.js, which calls the package's ASCII art function with the Bloody font," Checkmarx said. "That font value triggers a hidden routine that downloads node.exe from cdnzona.discloud.app, a host on a Brazilian application hosting service, saves it to %APPDATA%\node.exe, and runs it with its window hidden."

Interestingly, Overload RAT has been observed in two other campaigns since July 2026: one involving the
[exploitation of WordPress flaws](https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html)
(CVE-2026-63030 and CVE-2026-60137, aka wp2shell) and a
[macOS campaign](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/)
in which a fake Zoom installer is used to deploy the RAT. The fake Zoom installer campaign shares tactical overlaps with a suspected North Korea-aligned threat cluster dubbed
[UNK\_DeadDrop](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html)
.

"The operator is Portuguese-speaking, the git commits sit at -0300, one repository description is in Portuguese, and the GitHub display name and email give a common Brazilian handle," CloudSEK said. "None of this is an argument that the campaign targets Brazil. It is a piece of attribution to the operator's own linguistic space and nothing more. The delivery is npm and Discord, both of which are global; the second-stage targeting is opportunistic."