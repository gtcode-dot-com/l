---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T05:59:03.353122+00:00'
exported_at: '2026-10-07T05:59:05.643874+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
structured_data:
  about: []
  author: ''
  description: Rejetto HFS CVE-2026-61500 faces exploitation attempts after a public
    PoC showed forged admin sessions can lead to remote code execution.
  headline: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and
    RCE
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE
updated_at: '2026-10-07T05:59:03.353122+00:00'
url_hash: 984946d5750a4e3ab5017b385ac7e7463b964dc7
---

**

Ravie Lakshmanan
**

Oct 05, 2026

Vulnerability / Web Security

A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck.

The vulnerability in question is
**CVE-2026-61500**
(CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and seize control of affected systems.

"Rejetto HFS 3.0.0 through 3.2.0 derives its session-cookie signing key from the non-cryptographic Math.random() generator and discloses outputs of the same generator to unauthenticated clients during login," according to an
[advisory](https://github.com/advisories/GHSA-xxrm-3f86-v97j)
for the flaw.

"A remote attacker can collect a small number of login responses, reconstruct the generator's state, recover the signing key, and forge a valid administrator session cookie, leading to full administrative access and remote code execution via the server\_code configuration feature."

Horizon3.ai researcher Zach Hanley, in a post
[published](https://horizon3.ai/attack-research/disclosures/anthropic-mythos-rejetto-hfs-rce/)
on September 30, 2026, said Anthropic's Mythos model was used to discover the vulnerability, describing it as an authentication bypass that facilitates arbitrary remote code execution on Rejetto HFS.

"Rejetto HFS's administrative API allows for custom endpoints that can execute arbitrary JavaScript," Hanley said. "Combined, this presented a clear path from unauthenticated access to administrative control, and ultimately, remote code execution."

A patch for the vulnerability was released in July 2026 in
[version 3.2.1](https://github.com/rejetto/hfs/releases/tag/v3.2.1)
. However, it was not until late September that a Python-based proof-of-concept (PoC) exploit was publicly released by a security researcher named Alejandro Ramos (aka aramosf).

"HFS generated its Koa session-cookie signing key with JavaScript Math.random() and exposed outputs from the same V8 PRNG in the unauthenticated SRP login handshake," Ramos
[noted](https://github.com/aramosf/CVE-2026-61500)
. "An attacker can reconstruct the PRNG state, recover the signing key, forge an administrator session, and use the documented server\_code configuration feature to execute server-side JavaScript."

According to VulnCheck's Patrick Garrity, exploitation attempts were
[detected](https://www.linkedin.com/feed/update/urn:li:activity:7511590230232256513/)
on October 1, 2026, a day after Horizon3.ai published additional details of the flaw. The cybersecurity company said it identified an unnamed threat actor in China targeting real vulnerable hosts in the U.S.

"Activity so far looks to be small-scale reconnaissance only, with a single China Telecom IP probing Canary deployments in Japan and the United States," Caitlin Condon, vice president of research at VulnCheck,
[said](https://www.linkedin.com/posts/ccondon_new-kev-earlier-today-vulnchecks-canary-share-7511574376446590976-NNh3/)
in a LinkedIn post.

CVE-2026-61500 is the second vulnerability in Rejetto HTTP File Server after
[CVE-2024-23692](https://www.vicarius.io/vsociety/posts/unauthenticated-rce-flaw-in-rejetto-http-file-server-cve-2024-23692)
(CVSS score: 9.8) to come under active exploitation in the wild. In July 2024, multiple threat actors were observed weaponizing the flaw to deliver
[cryptocurrency miners, trojans](https://thehackernews.com/2024/07/microsoft-uncovers-critical-flaws-in.html)
, and a malware named
[HATVIBE](https://thehackernews.com/2024/07/ukrainian-institutions-targeted-using.html)
.