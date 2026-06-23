---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T17:57:50.618358+00:00'
exported_at: '2026-06-23T17:57:51.899541+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
structured_data:
  about: []
  author: ''
  description: JFrog found malicious npm packages that deploy a Windows RAT to steal
    Chrome credentials, run commands, and transfer files.
  headline: Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT
updated_at: '2026-06-23T17:57:50.618358+00:00'
url_hash: ac23ac225457cf9200dfa6277bdb7b6719f184a1
---

**

Ravie Lakshmanan
**

Jun 23, 2026

Supply Chain Attack / Developer Security

Cybersecurity researchers have discovered a set of malicious npm packages that are designed to deliver a Windows-based remote access trojan (RAT).

The list of identified packages, is below -

* aes-decode-runner-pro (145 downloads)
* postcss-minify-selector (256 downloads)
* postcss-minify-selector-parser (615 downloads)

All the packages were published over the past month by an npm user named "
[abdrizak](https://www.npmjs.com/~abdrizak)
" and continue to be available for download from npm as of writing.

"Aes-decode-runner-pro and postcss-minify-selector-parser both present themselves as layered AES/custom-codec packages and depend on the legitimate postcss-selector-parser," JFrog
[said](https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/)
in an analysis. "Postcss-minify-selector presents itself as a PostCSS selector minifier and depends on postcss-minify-selector-parser."

As for "postcss-minify-selector-parser," the name is a reference to "
[postcss-selector-parser](https://www.npmjs.com/package/postcss-selector-parser)
," a widely used npm library with more than 127 million weekly downloads. Regardless of the package downloaded, the attack chain leads to the deployment of the same Windows malware.

The packages come embedded with a JavaScript dropper that writes a PowerShell script ("settings.ps1") to disk and executes it. The PowerShell script then acts as a downloader for a next-stage payload retrieved from an external server ("nvidiadriver[.]net") using the "curl.exe."

The retrieved payload is a ZIP archive, from which a Visual Basic Script ("update.vbs") file is extracted and run using "wscript.exe." Also bundled in the downloaded ZIP file is a Python runtime, a Python loader ("loader.py"), and a number of Python extension modules (\*.pyd) compiled using
[Nuitka](https://nuitka.net/)
.

Visual Basic is responsible for setting up the Python environment on the compromised host and launching the "loader.py" script, which then triggers the core logic of the malware. The RAT is equipped to gather host information, siphon credentials from Google Chrome, collect data from Chrome extensions, run shell commands, and download/upload files to and from a command-and-control (C2) server ("95.216.92[.]207:8080").

These features are realized through a set of Python native extension modules -

* config.pyd, which contains constants, command IDs, C2 URL, registry key names
* api.pyd, which handles HTTP C2 packet exchange
* audiodriver.pyd, which handles the main RAT orchestration loop
* command.pyd, which profiles the host, runs virtual machine (VM) checks, file transfer, and shell execution
* auto.pyd, which performs Chrome credential and extension theft, bypassing app-bound encryption (
  [ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
  ) protections
* util.pyd, which acts as tar/gzip archive helpers

"This case shows how a small parser-like package can hide a multi-stage Windows payload while appearing related to legitimate build tooling with massive weekly usage," JFrog said. "For defenders, the important lesson is to treat lookalike build dependencies as potential delivery mechanisms, not just harmless naming noise."

The discovery coincides with three other campaigns targeting the npm and TypeScript ecosystem -

* A malicious package named "
  [apintergrationpost](https://safedep.io/malicious-apintergrationpost-npm-myra-rat/)
  " that delivers a full-featured Linux RAT dubbed MYRA, while claiming to be a Node.js integration client for authorized red team exercises. "It compiles a native C rootkit during install, establishes three independent persistence mechanisms, masquerades as a systemd service, supports fileless execution, and provides interactive shell access with live screen streaming," SafeDep said.
* A malicious package named "
  [@withgoogle/stitch-sdk](https://safedep.io/withgoogle-stitch-sdk-scope-squat-credential-harvester/)
  " that impersonates Google's Stitch AI design tool but comes with capabilities to steal developer credentials from eight sources (Claude Code, git config, ~/.git-credentials, SSH public keys, GitHub CLI, npm config, ~/.npmrc, and ~/.docker/config.json) and exfiltrates them to an attacker-controlled domain ("stitch-production[.]org/api/v1").
* A cluster of
  [five packages](https://safedep.io/procwire-npm-windows-dropper-campaign/)
  ("procwire," "routecraft," "endpointmap," "bytecraft," and "staticlayer") that delivers a dropper binary on Windows hosts from an external server and executes it during npm install. The "routecraft" package lists "procwire" as a dependency, while the latter lists "endpointmap" and "bytecraft" as dependencies. The last package, "staticlayer," is designed to run on the server side and deliver files to a client that presents the dropper's exact User-Agent.

Users who have installed any of the above packages are advised to remove them with immediate effect, remove any artifacts created by them, and rotate credentials from impacted developer machines.

The findings also coincide with a
[supply chain attack](https://safedep.io/astro-config-blockchain-c2-supply-chain/)
targeting the "
[gonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)
" knowledge graph tool to push a malicious payload that "beacons one of three hardcoded C2 servers, exfiltrates a campaign marker, XOR-decrypts and evaluates a downloaded bot client, then independently resolves a second-stage command from a Tron blockchain address whose latest transaction encodes a BSC transaction hash carrying the active payload."

The activity overlaps with a North Korean supply chain operation dubbed
[PolinRider](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)
, which has been
[observed](https://opensourcemalware.com/blog/polinrider-rides-again-north-korean-attack-expands-across-github)
injecting obfuscated JavaScript into legitimate developers' configuration files across nearly 2,000 compromised GitHub repositories to deliver a known malware downloader and stealer referred to as
[BeaverTail](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html)
, which then paves the way for the InvisibleFerret backdoor.

"This attack combines three things that individually are familiar but together open a detection gap: an elaborate fake PR description with fabricated test evidence, a diff that hides its payload in horizontal whitespace, and a two-stage C2 where the second stage uses public blockchain infrastructure as a write-once, read-anywhere relay," SafeDep said.