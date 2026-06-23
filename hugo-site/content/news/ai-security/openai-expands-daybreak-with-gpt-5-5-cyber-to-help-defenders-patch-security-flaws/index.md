---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T04:33:41.515578+00:00'
exported_at: '2026-06-23T04:33:42.870945+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/openai-expands-daybreak-with-gpt-55.html
structured_data:
  about: []
  author: ''
  description: OpenAI is releasing GPT-5.5-Cyber, Codex Security updates, and Patch
    the Planet to help defenders validate and patch vulnerabilities.
  headline: OpenAI Expands Daybreak With GPT-5.5-Cyber to Help Defenders Patch Security
    Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/openai-expands-daybreak-with-gpt-55.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Expands Daybreak With GPT-5.5-Cyber to Help Defenders Patch Security
  Flaws
updated_at: '2026-06-23T04:33:41.515578+00:00'
url_hash: 748be225aee212cc5b160a340d1f278fab2e48ae
---

OpenAI on Monday
[said](https://openai.com/index/daybreak-securing-the-world/)
it's releasing an improved version of its GPT‑5.5‑Cyber model to trusted defenders as part of the
[Daybreak initiative](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)
, the artificial intelligence (AI) company announced last month.

Calling GPT‑5.5‑Cyber its "strongest model yet for finding and helping patch software vulnerabilities," OpenAI said the model can "sustain deeper analysis across large codebases" to identify security issues, validate them in a controlled environment, and develop and test patches.

In tandem, the tech upstart is releasing an update to the Codex Security plugin⁠ to speed up the process of discovering and patching vulnerabilities in existing systems, alongside preventing new vulnerabilities from entering production codebases.

"Developers can run deep scans or review recent changes, generate reports with severity, affected code locations, validation evidence, and remediation guidance, trace attack paths, build threat models, validate findings, and generate codebase-specific patches for review," OpenAI said.

On top of that, the plugin⁠ can triage and validate existing findings from scanners, advisories, bug-bounty reports, or ticketing systems, and then facilitate patch generation at scale to quickly close a backlog of vulnerabilities.

OpenAI is also launching a new initiative called
[Patch the Planet](https://openai.com/index/patch-the-planet/)
in partnership with
[Trail of Bits](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet)
to help secure open-source projects. Initial participants include cURL, NATS Server, pyca/cryptography, Sigstore, aiohttp, the Go project, freenginx, Python, and python.org.

These moves come as frontier models from Anthropic and OpenAI are accelerating vulnerability discovery, leaving software maintainers overwhelmed with an ever-increasing volume of bugs that need to be verified, triaged, and patched. While previously the challenge lay in finding vulnerabilities, the bottleneck has now shifted to patching them.

AI models come with capabilities to navigate large codebases, reason through attack paths, and flag security issues that might have otherwise stayed hidden. Case in point is a 29-year-old flaw in the Squid web proxy (
[CVE-2026-47729](https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html)
, aka Squidbleed) that can leak cleartext HTTP requests belonging to other users under certain conditions.

Cyber experts have also raised concerns that more advanced AI models are turbocharging bad actors' abilities to take advantage of security vulnerabilities, forcing the industry to plug the holes almost as soon as they are discovered.

"Threat actors with limited technical expertise can use publicly available AI models for malicious purposes," the Canadian Centre for Cyber Security
[said](https://www.cyber.gc.ca/en/guidance/frontier-artificial-intelligence-itsap10050)
in guidance released in May 2026. "Organizations should assume that AI-driven exploitation may bypass preventative controls, significantly outpace vendors' capacity to publish corrective measures and challenge the organization's ability to deploy."

Patch the Planet aims to reduce this undue burden placed on maintainers by letting security engineers review and validate findings, work with projects to develop patches and tests, and help build reusable vulnerability discovery workflows with the goal of improving security even after the initial fixes are released.

"With Patch the Planet, we are working with researchers, maintainers, enterprises, and partners to make powerful cyber capability available to defenders with appropriate access, governance, and human oversight," OpenAI said.

The AI company also said the Daybreak initiative has already helped
[surface a number of vulnerabilities](https://gist.github.com/patch-the-planet/69fd1aa925c8e73edea9e6e967043cbb)
across various operating systems and web browsers -

* 8 kernel pointer information leak proofs-of-concept (PoCs) and 24 local privilege escalation exploits in the Linux Kernel
* A 23-year-old use-after-free⁠ in
  [OpenBSD's kernel implementation](https://github.com/openbsd/src/commit/1957873d2063db11dab780eca75b5e629d1e838d)
  of System V semaphores
* 34 vulnerabilities and 7 local privilege escalation PoCs in FreeBSD
* 6 vulnerabilities in dnsmasq (CVE-2026-4890⁠, CVE-2026-4891⁠, CVE-2026-4892⁠, and CVE-2026-5172⁠)
* A denial-of-service (DoS) technique called
  [HTTP/2 Bomb](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html)
  impacting major HTTP/2 implementations, including NGINX, Apache, IIS, and Pingora
* 5 exploitable vulnerabilities in Google Chrome's V8 JavaScript engine
* 10 exploitable Apple Safari vulnerabilities
* A WebAssembly vulnerability (CVE-2026-8390⁠) in Mozilla Firefox

"Patch the Planet is designed to put that full defensive loop in service of maintainers: discovery, validation, severity review, disclosure, patch development, testing, and deployment," OpenAI said. "Frontier models can make parts of that loop faster, but the aim is to give the people responsible for shared infrastructure better tools and more capacity, while preserving their agency over how changes land."

The developments go hand in hand with bad actors misusing AI to compress the time between finding and exploiting a weakness, shrinking the window defenders have to respond. The use of
[vibe-coded exploits](https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html)
also heralds a new chapter where the technology is not only lowering the barrier to exploit development, but also enabling attackers to cast a wide net across newly disclosed vulnerabilities with lesser effort.

Intelligence agencies from Australia, Canada, New Zealand, the U.K., and the U.S. have warned that advanced AI models can speed up the speed, scale, and sophistication of cyber threats, while lowering the barrier for malicious actors and shrinking the window between vulnerability discovery and exploitation ever more quickly.

"Frontier Al models are anticipated to exceed current industry expectations, fundamentally transforming both offensive and defensive cyber capabilities. The timeline is not years, it is months, the agencies
[noted](https://www.ncsc.gov.uk/news/the-ai-shift-in-cyber-risk-why-leaders-must-act-now)
. "In this environment, cyber resilience is integral to advancing business continuity, market confidence, and long-term value."

"Success will come from getting the basics right, acting quickly, and integrating cyber security into core business strategy. Those that do not will face growing operational and strategic disadvantage."