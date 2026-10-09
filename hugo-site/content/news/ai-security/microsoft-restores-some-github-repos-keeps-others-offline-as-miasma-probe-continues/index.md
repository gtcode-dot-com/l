---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T22:15:18.835130+00:00'
exported_at: '2026-06-10T22:15:20.164902+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/microsoft-restores-some-github-repos.html
structured_data:
  about: []
  author: ''
  description: Microsoft confirms it temporarily removed GitHub repos after Miasma
    worm compromised 73 of its open-source projects to inject an information stealer.
  headline: Microsoft Restores Some GitHub Repos, Keeps Others Offline as Miasma Probe
    Continues
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/microsoft-restores-some-github-repos.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Restores Some GitHub Repos, Keeps Others Offline as Miasma Probe
  Continues
updated_at: '2026-06-10T22:15:18.835130+00:00'
url_hash: a9e3028ff3a5b45a869621ff5b66be33fac19e63
---

Microsoft on Monday confirmed that it temporarily removed some GitHub repositories in response to a
[recent security incident](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)
that led to 73 of its open-source projects being compromised to inject an information stealer into the code.

"Our priority is to protect customers and the broader ecosystem," a Microsoft spokesperson told The Hacker News via email. "We temporarily removed some repositories as we investigated potential malicious content. Some of these repos have been restored after review, while others may remain offline while work continues."

"As part of our investigation, we notified a small number of customers who may have pulled down content from the affected repositories. We will continue to investigate, and if anything further is identified that requires customer action, we will reach out directly through our established support channels."

The development comes days after the Windows maker cut off access to dozens of its open-source projects hosted on GitHub following reports that they were compromised as part of an ongoing software supply chain campaign codenamed Miasma.

Among the projects that were infected included "durabletask," a Python package that was first compromised last month by a cybercrime group known as TeamPCP to deliver an information stealer designed for Linux systems.

Further analysis of the Miasma payload embedded into the projects has uncovered capabilities to trigger automatic code execution when an unsuspecting developer opens the repository in an artificial intelligence (AI)-powered coding tool or integrated development environment (IDE).

The findings are the latest in a sustained software supply chain campaign that has breached widely used open-source packages to plant malware capable of propagating to downstream users and beyond.

This includes a newer PyPI wave tied to the broader Mini Shai-Hulud, Miasma, and Hades waves, infecting an additional set of 23 packages, including some
[bioinformatics-related libraries](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)
used in graph learning, patient phenotyping, phenopacket tooling, and scientific workflows.

Some of the other packages include a collection of AI and Model Context Protocol (MCP)-themed packages and typosquat-style packages such as rsquests, tlask, and rlask that impersonate requests and flask, and a langchain-core-mcp. The complete list of legitimate and bait packages is below -

* dreamgen 1.8.1
* embiggen 0.11.97
* ensmallen 0.8.101
* gpsea 0.9.14
* instructor-mcp 1.15.2, 1.15.3
* langchain-core-mcp 1.4.2, 1.4.3
* mem8 6.0.1
* mflux-streamlit 0.0.3, 0.0.4
* openai-mcp 2.41.1, 2.41.2
* orchestr8-platform 3.3.2
* phenopacket-store-toolkit 0.1.7
* ppkt2synergy 0.1.1
* pyphetools 0.9.120
* ray-mcp-server 0.2.1
* rlask 3.1.7
* rsquests 2.34.3
* tiktoken-mcp 0.13.1, 0.13.2
* tlask 3.1.4

The new cluster employs a new payload delivery mechanism, per
[Socket](https://socket.dev/blog/mini-shai-hulud-miasma-and-hades-worms-target-bioinformatics-and-mcp-developers-via-malicious)
, indicating that the threat actors are adapting and actively experimenting with different methods as part of what has been described as a "fast-moving supply chain campaign."

While the earlier packages used executable .pth startup hooks to bootstrap Bun and run an obfuscated JavaScript stealer, the latest set incorporates different approaches -

* Trojanized native .abi3.so extensions that execute the stealer when the package is imported
* A .pth startup hook loader variant that searches sys.path for the "\_index.js" payload instead of bundling the payload in the same wheel

"That last variant separates the loader from the JavaScript payload, which could make the package look less obviously malicious during static analysis," Socket told The Hacker News.

Regardless of the method used, the end result is the same. Once executed, the malware targets developer workstations and CI/CD environments, harvesting high-value secrets and exfiltrating them to a public GitHub repository.

Kirill Boychenko, senior threat intelligence analyst at the company, told The Hacker News via email that the latest assortment of Python libraries marks the first time the Mini Shai-Hulud / Miasma / Hades-linked attacks have mixed compromised legitimate packages with threat actor-published typosquats and ecosystem-lure packages.

"Earlier publicly documented TeamPCP-linked attacks primarily involved poisoned releases of real projects, compromised publisher accounts, or compromised CI/CD release paths, rather than brand-new lookalike packages," Boychenko said.

As for why the threat actors would embrace the approach at this stage of the operation, the researcher said the likely reason is tactical diversification. "Compromised legitimate packages give them trust and reach, but those paths depend on stolen credentials or CI/CD access that can be revoked quickly," Boychenko added.

"Typosquats and ecosystem-bait packages are easier to publish, faster to iterate on, and useful for testing new malware loader behavior without burning a high-value compromised project. The MCP and AI-themed names also fit a fast-moving ecosystem where developers may install unfamiliar packages that look plausible."

A key capability of the bioinformatics package is its ability to derail and bypass AI-powered scanners and analyst copilots by means of an adversarial prompt injection embedded within a JavaScript block comment, an aspect
[previously detailed](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)
by StepSecurity.

"The Hades branch of the Shai-Hulud and Miasma activity is best understood as a fast-moving supply chain campaign, not a single package incident," Boychenko said. "The langchain-core-mcp variant goes further by installing a .pth loader that searches sys.path for \_index.js, meaning the loader and payload do not need to live in the same wheel."

*(The story was updated after publication to include a response from Socket.)*