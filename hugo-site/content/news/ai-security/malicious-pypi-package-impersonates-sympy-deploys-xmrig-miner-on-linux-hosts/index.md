---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T12:15:13.106013+00:00'
exported_at: '2026-01-22T12:15:15.552062+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/malicious-pypi-package-impersonates.html
structured_data:
  about: []
  author: ''
  description: A fake sympy-dev package on PyPI impersonates the SymPy library to
    download and run XMRig cryptominers on Linux using in-memory execution.
  headline: Malicious PyPI Package Impersonates SymPy, Deploys XMRig Miner on Linux
    Hosts
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/malicious-pypi-package-impersonates.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious PyPI Package Impersonates SymPy, Deploys XMRig Miner on Linux Hosts
updated_at: '2026-01-22T12:15:13.106013+00:00'
url_hash: 1edce63014b269331f0f11f10b806b0439a53745
---

**

Ravie Lakshmanan
**

Jan 22, 2026

Cryptojacking / Malware

A new malicious package discovered in the Python Package Index (PyPI) has been found to impersonate a popular library for symbolic mathematics to deploy malicious payloads, including a cryptocurrency miner, on Linux hosts.

The package, named
**[sympy-dev](https://pypi.org/project/sympy-dev/)**
, mimics
[SymPy](https://www.sympy.org/en/index.html)
, replicating the latter's project description verbatim in an attempt to deceive unsuspecting users into thinking that they are downloading a "development version" of the library. It has been downloaded over 1,100 times since it was first published on January 17, 2026.

Although the download count is not a reliable yardstick for measuring the number of infections, the figure likely suggests some developers may have fallen victim to the malicious campaign. The package remains available for download as of writing.

According to
[Socket](https://socket.dev/blog/pypi-package-impersonates-sympy-to-deliver-cryptomining-malware)
, the original library has been modified to act as a downloader for an XMRig cryptocurrency miner on compromised systems. The malicious behavior is designed to trigger only when specific polynomial routines are called so as to fly under the radar.

"When invoked, the backdoored functions retrieve a remote JSON configuration, download a threat actor-controlled ELF payload, then execute it from an anonymous memory-backed file descriptor using Linux memfd\_create and /proc/self/fd, which reduces on-disk artifacts," security researcher Kirill Boychenko said in a Wednesday analysis.

The altered functions are used to execute a downloader, which fetches a remote JSON configuration and an ELF payload from "63.250.56[.]54," and then launches the ELF binary along with the configuration as input directly in memory to avoid leaving artifacts on disk. This technique has been previously adopted by cryptojacking campaigns orchestrated by
[FritzFrog](https://thehackernews.com/2024/02/fritzfrog-returns-with-log4shell-and.html)
and
[Mimo](https://thehackernews.com/2025/07/threat-actor-mimo-targets-magento-and.html)
.

The end goal of the attack is to download two Linux ELF binaries that are designed to mine cryptocurrency using XMRig on Linux hosts.

"Both retrieved configurations use an XMRig compatible schema that enables CPU mining, disables GPU backends, and directs the miner to Stratum over TLS endpoints on port 3333 hosted on the same threat actor-controlled IP addresses," Socket said.

"Although we observed cryptomining in this campaign, the Python implant functions as a general purpose loader that can fetch and execute arbitrary second stage code under the privileges of the Python process."