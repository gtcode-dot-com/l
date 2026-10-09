---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-13T06:48:04.865235+00:00'
exported_at: '2026-02-13T06:48:08.428676+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/lazarus-campaign-plants-malicious.html
structured_data:
  about: []
  author: ''
  description: North Korea-linked Lazarus campaign spreads malicious npm and PyPI
    packages via fake crypto job offers, deploying RATs and data-stealing malware.
  headline: Lazarus Campaign Plants Malicious Packages in npm and PyPI Ecosystems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/lazarus-campaign-plants-malicious.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Lazarus Campaign Plants Malicious Packages in npm and PyPI Ecosystems
updated_at: '2026-02-13T06:48:04.865235+00:00'
url_hash: 3bb20fbcc48448e587019cc6451d190d0237644f
---

Cybersecurity researchers have discovered a fresh set of malicious packages across npm and the Python Package Index (PyPI) repository linked to a fake recruitment-themed campaign orchestrated by the North Korea-linked Lazarus Group.

The coordinated campaign has been codenamed graphalgo in reference to the first package published in the npm registry. It's assessed to be active since May 2025.

"Developers are approached via social platforms like LinkedIn and Facebook, or through job offerings on forums like Reddit," ReversingLabs researcher Karlo Zanki
[said](https://www.reversinglabs.com/blog/fake-recruiter-campaign-crypto-devs)
in a report. "The campaign includes a well-orchestrated story around a company involved in blockchain and cryptocurrency exchanges."

Notably, one of the identified npm packages, bigmathutils, attracted more than 10,000 downloads after the first, non-malicious version was published, and before the second version containing a malicious payload was released. The names of the packages are listed below -

**npm -**

* graphalgo
* graphorithm
* graphstruct
* graphlibcore
* netstruct
* graphnetworkx
* terminalcolor256
* graphkitx
* graphchain
* graphflux
* graphorbit
* graphnet
* graphhub
* terminal-kleur
* graphrix
* bignumx
* bignumberx
* bignumex
* bigmathex
* bigmathlib
* bigmathutils
* graphlink
* bigmathix
* graphflowx

**PyPI -**

* graphalgo
* graphex
* graphlibx
* graphdict
* graphflux
* graphnode
* graphsync
* bigpyx
* bignum
* bigmathex
* bigmathix
* bigmathutils

As with many
[job-focused campaigns](https://thehackernews.com/2026/02/dprk-operatives-impersonate.html)
conducted by North Korean threat actors, the attack chain begins with establishing a fake company like
[Veltrix Capital](https://www.linkedin.com/company/veltrix-capital/)
in the blockchain and cryptocurrency trading space, and then setting up the necessary digital real estate to create an illusion of legitimacy.

This includes registering a domain and creating a related GitHub organization to host several repositories for use in coding assessments. The repositories have been found to contain projects based on Python and JavaScript.

"Examination of these repositories didn't reveal any obvious malicious functionality," Zanki said. "That is because the malicious functionality was not introduced directly via the job interview repositories, but indirectly – through dependencies hosted on the npm and PyPI open-source package repositories."

The idea behind setting up these repositories is to trick candidates who apply to its job listings on Reddit and Facebook Groups into running the projects on their machines, effectively installing the malicious dependency and triggering the infection. In some cases, victims are directly contacted by seemingly legitimate recruiters on LinkedIn.

The packages ultimately act as a conduit to deploy a remote access trojan (RAT) that periodically fetches and executes commands from an external server. It supports various commands to gather system information, enumerate files and directories, list running processes, create folders, rename files, delete files, and upload/download files.

Interestingly, the command-and-control (C2) communication is protected by a token-based mechanism to ensure that only requests with a valid token are accepted. The approach was
[previously observed](https://thehackernews.com/2023/08/north-korean-hackers-deploy-new.html)
in 2023 campaigns linked to a North Korean hacking group called Jade Sleet, which is also known as TraderTraitor or UNC4899.

It essentially works like this: the packages send system data as part of a registration step to the C2 server, which responds with a token. This token is then sent back to the C2 server in subsequent requests to establish that they are originating from an already registered infected system.

"The token-based approach is a similarity [...] in both cases and has not been used by other actors in malware hosted on public package repositories as far as we know," Zanki told The Hacker News at that time.

The findings show that North Korean state-sponsored threat actors
[continue to poison](https://thehackernews.com/2024/09/developers-beware-lazarus-group-uses.html)
open-source ecosystems with malicious packages in hopes of stealing sensitive data and conducting financial theft, a fact evidenced by the RAT's checks to determine if the MetaMask browser extension is installed in the machine.

"Evidence suggests that this is a highly sophisticated campaign," ReversingLabs said. "Its modularity, long-lived nature, patience in building trust across different campaign elements, and the complexity of the multilayered and encrypted malware point to the work of a state-sponsored threat actor."

### More Malicious npm Packages Found

The disclosure comes as JFrog uncovered a sophisticated, malicious npm package called "duer-js" published by a user named "luizaearlyx." While the library claims to be a utility to "make the console window more visible," it harbors a Windows information stealer called Bada Stealer.

It's capable of gathering Discord tokens, passwords, cookies, and autofill data from Google Chrome, Microsoft Edge, Brave, Opera, and Yandex Browser, cryptocurrency wallet details, and system information. The data is then exfiltrated to a Discord webhook, as well as the Gofile file storage service as a backup.

"In addition to stealing information from the host it infected, the malicious package downloads a secondary payload," security researcher Guy Korolevski
[said](https://research.jfrog.com/post/duer-js-malicious-package/)
. "This payload is designed to run on the Discord Desktop app startup, with self-updating capabilities, stealing directly from it, including payment methods used by the user."

It also coincides with the discovery of another malware campaign that weaponizes npm to extort cryptocurrency payments from developers during package installation using the "npm install" command. The campaign, first recorded on February 4, 2026, has been dubbed XPACK ATTACK by OpenSourceMalware.

|  |
| --- |
|  |
| duer-js malicious package flow, hijacking Discord’s Electron environment |

The names of the packages, all uploaded by a user named "dev.chandra\_bose," are listed below -

* xpack-per-user
* xpack-per-device
* xpack-sui
* xpack-subscription
* xpack-arc-gateway
* xpack-video-submission
* test-npm-style
* xpack-subscription-test
* testing-package-xdsfdsfsc

"Unlike traditional malware that steals credentials or executes reverse shells, this attack innovatively abuses the
[HTTP 402 'Payment Required' status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402)
to create a seemingly legitimate payment wall," security researcher Paul McCarty
[said](https://opensourcemalware.com/blog/xpack-attack)
. "The attack blocks installation until victims pay 0.1 USDC/ETH to the attacker's wallet, while collecting GitHub usernames and device fingerprints."

"If they refuse to pay, the installation simply fails after wasting 5+ minutes of their development time, and they may not even realize they've encountered malware versus what appeared to be a legitimate paywall for package access."