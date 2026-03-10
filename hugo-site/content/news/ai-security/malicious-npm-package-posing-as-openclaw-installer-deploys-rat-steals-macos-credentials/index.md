---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T00:15:14.541840+00:00'
exported_at: '2026-03-10T00:15:17.956621+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html
structured_data:
  about: []
  author: ''
  description: Malicious npm package '@openclaw-ai/openclawai' downloaded 178 times
    installs GhostLoader RAT, stealing credentials and crypto wallets.
  headline: Malicious npm Package Posing as OpenClaw Installer Deploys RAT, Steals
    macOS Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious npm Package Posing as OpenClaw Installer Deploys RAT, Steals macOS
  Credentials
updated_at: '2026-03-10T00:15:14.541840+00:00'
url_hash: 6b92e60c5682894aa4f01d1ed19feffc1ffa8249
---

Cybersecurity researchers have discovered a malicious npm package that masquerades as an
[OpenClaw](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html)
installer to deploy a remote access trojan (RAT) and steal sensitive data from compromised hosts.

The package, named "
[@openclaw-ai/openclawai](https://www.npmjs.com/package/@openclaw-ai/openclawai)
," was uploaded to the registry by a user named "openclaw-ai" on March 3, 2026. It has been downloaded 178 times to date. The library is still available for download as of writing.

JFrog, which discovered the package, said it's designed to steal system credentials, browser data, crypto wallets, SSH keys, Apple Keychain databases, and iMessage history, as well as install a persistent RAT with remote access capabilities, SOCKS5 proxy, and live browser session cloning.

"The attack is notable for its broad data collection, its use of social engineering to harvest the victim's system password, and the sophistication of its persistence and C2 [command-and-control] infrastructure," security researcher Meitar Palas
[said](https://research.jfrog.com/post/ghostclaw-unmasked/)
. "Internally, the malware identifies itself as GhostLoader."

The malicious logic is triggered by means of a postinstall hook, which
[re-installs the package globally](https://docs.npmjs.com/downloading-and-installing-packages-globally)
using the command: "npm i -g @openclaw-ai/openclawai." Once the installation is complete, the OpenClaw binary points to "scripts/setup.js" by means of the "bin" property in the "package.json" file.

It's worth noting that the "
[bin](https://docs.npmjs.com/cli/v11/configuring-npm/package-json#bin)
" field is used to define executable files that should be added to the user's PATH during package installation. This, in turn, turns the package into a globally accessible command-line tool.

The file "setup.js" serves as the first-stage dropper that, upon running, displays a convincing fake command-line interface with animated progress bars to give the impression that OpenClaw is being installed on the host. After the purported installation step is complete, the script shows a bogus iCloud Keychain authorization prompt, asking users to enter their system password.

Simultaneously, the script retrieves an encrypted second-stage JavaScript payload from the C2 server ("trackpipe[.]dev"), which is then decoded, written to a temporary file, and spawned as a detached child process to continue running in the background. The temp file is deleted after 60 seconds to cover up traces of the activity.

"If the Safari directory is inaccessible (no Full Disk Access), the script displays an AppleScript dialog urging the user to grant FDA to Terminal, complete with step-by-step instructions and a button that opens System Preferences directly," JFrog explained. "This enables the second-stage payload to steal Apple Notes, iMessage, Safari history, and Mail data."

The JavaScript second-stage, featuring about 11,700 lines, is a full-fledged information stealer and RAT framework that's capable of persistence, data collection, browser decryption, C2 communication, a SOCKS5 proxy, and live browser cloning. It's also equipped to steal a wide range of data -

* macOS Keychain, including both the local login.keychain-db and all iCloud Keychain databases
* Credentials, cookies, credit cards, and autofill data from all Chromium-based browsers, such as Google Chrome, Microsoft Edge, Brave, Vivaldi, Opera, Yandex, and Comet
* Data from desktop wallet applications and browser extensions
* Cryptocurrency wallet seed phrases
* SSH keys
* Developer and cloud credentials for AWS, Microsoft Azure, Google Cloud, Kubernetes, Docker, and GitHub
* Artificial intelligence (AI) agent configurations, and
* Data protected by the FDA, including Apple Notes, iMessage history, Safari browsing history, Mail account configurations, and Apple account information

In the final stage, the collected data is compressed into a tar.gz archive and exfiltrated through multiple channels, including directly to the C2 server, Telegram Bot API, and GoFile.io.

What's more, the malware enters a persistent daemon mode that allows it to monitor clipboard content every three seconds and transmit any data that matches one of the nine pre-defined patterns corresponding to private keys,
[WIF key](https://learnmeabitcoin.com/technical/keys/private-key/wif/)
, SOL private key, RSA private key, BTC address, Ethereum address, AWS key, OpenAI key, and Strike key.

Other features include keeping tabs on running processes, scanning incoming iMessage chats in real-time, and executing commands sent from the C2 server to run arbitrary shell command, open a URL on the victim's default browser, download additional payloads, upload files, start/stop a SOCKS5 proxy, list available browsers, clone a browser profile and launch it in headless mode, stop the browser clone, self-destruct, and update itself.

The browser cloning function is particularly dangerous as it launches a headless Chromium instance with the existing browser profile that contains cookies, login, and history data. This gives the attacker a fully authenticated browser session without the need for accessing credentials.

"The @openclaw-ai/openclawai package combines social engineering, encrypted payload delivery, broad data collection, and a persistent RAT into a single npm package," JFrog said.

"The polished fake CLI installer and Keychain prompt are convincing enough to extract system passwords from cautious developers, and once captured, those credentials unlock macOS Keychain decryption and browser credential extraction that would otherwise be blocked by OS-level protections."