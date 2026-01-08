---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:44:02.736863+00:00'
exported_at: '2026-01-08T21:44:05.323216+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/researchers-uncover-nodecordrat-hidden.html
structured_data:
  about: []
  author: ''
  description: Security researchers found 3 npm packages that installed NodeCordRAT
    malware, stealing browser data, crypto wallet secrets & tokens using Discord C2.
  headline: Researchers Uncover NodeCordRAT Hidden in npm Bitcoin-Themed Packages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/researchers-uncover-nodecordrat-hidden.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Uncover NodeCordRAT Hidden in npm Bitcoin-Themed Packages
updated_at: '2026-01-08T21:44:02.736863+00:00'
url_hash: 01ae9c4f870198b7af28c3173ca2c6b12976bf78
---

**

Jan 08, 2026
**

Ravie Lakshmanan

Malware / Cloud Security

Cybersecurity researchers have
[discovered](https://www.zscaler.com/blogs/security-research/malicious-npm-packages-deliver-nodecordrat)
three malicious npm packages that are designed to deliver a previously undocumented malware called
**NodeCordRAT**
.

The names of the packages, all of which were taken down as of November 2025, are listed below. They were uploaded by a user named "wenmoonx."

"The bitcoin-main-lib and bitcoin-lib-js packages execute a postinstall.cjs script during installation, which installs bip40, the package that contains the malicious payload," Zscaler ThreatLabz researchers Satyam Singh and Lakhan Parashar said. "This final payload, named NodeCordRAT by ThreatLabz, is a remote access trojan (RAT) with data-stealing capabilities."

NodeCordRAT gets its name from the use of npm as a propagation vector and Discord servers for command-and-control (C2) communications. The malware is equipped to steal Google Chrome credentials, API tokens, and seed phrases from cryptocurrency wallets like MetaMask.

According to the cybersecurity company, the threat actor behind the campaign is assessed to have named the packages after real repositories found within the legitimate
[bitcoinjs](https://github.com/orgs/bitcoinjs/repositories)
project, such as bitcoinjs-lib, bip32, bip38, and bip38.

Both "bitcoin-main-lib" and "bitcoin-lib-js" include a "package.json" file that features "postinstall.cjs" as a postinstall script, leading to the execution of "bip40" that contains the NodeCordRAT payload.

The malware, besides fingerprinting the infected host to generate a unique identifier across Windows, Linux, and macOS systems, leverages a hard-coded Discord server to open a covert communication channel to receive instructions and execute them -

* !run, to execute arbitrary shell commands using Node.js' exec function
* !screenshot, to take a full desktop screenshot and exfiltrate the PNG file to the Discord channel
* !sendfile, to upload a specified file to the Discord channel

"This data is exfiltrated using Discord's API with a hardcoded token and sent to a private channel," Zscaler said. "The stolen files are uploaded as message attachments via Discord's REST endpoint /channels/{id}/messages."