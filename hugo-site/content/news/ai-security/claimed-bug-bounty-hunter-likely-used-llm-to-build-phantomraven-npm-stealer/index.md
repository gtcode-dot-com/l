---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T22:04:21.044896+00:00'
exported_at: '2026-10-03T22:04:22.916992+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
structured_data:
  about: []
  author: ''
  description: CrowdStrike says PhantomRaven was likely LLM-generated and spread through
    malicious npm packages that collect developer credentials and CI/CD secrets.
  headline: Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer
updated_at: '2026-10-03T22:04:21.044896+00:00'
url_hash: 9be6eecf6db2844d80009f944a4715a5e9a0eaeb
---

**

Ravie Lakshmanan
**

Sep 18, 2026

Malware / Cybercrime

A financially motivated threat actor has been linked to the development and distribution of a JavaScript (JS)-based information stealer known as
**PhantomRaven**
via the npm package registry.

"The developer likely wrote the malware using a large language model (LLM), an assessment made with high confidence based on verbose comments, placeholder code, and statistical token-analysis patterns," CrowdStrike's Counter Adversary Operations
[said](https://www.crowdstrike.com/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/)
in an analysis published this week.

PhantomRaven was
[first flagged](https://thehackernews.com/2025/10/phantomraven-malware-found-in-126-npm.html)
by Koi Security and DCODX in late October 2025, calling attention to a slopsquatting and typosquatted campaign in which more than 100 malicious packages were uploaded to npm to steal authentication tokens, CI/CD secrets, and GitHub credentials from developers' machines.

The software supply chain attack used these packages as a cover to retrieve a remote dynamic dependency (RDD) from an external server so that the libraries themselves are not flagged by security tools.

Once installed, the malware embedded in the remote dependency scans the developer environment for email addresses, gathers information about the CI/CD environment, collects a system fingerprint, including the public IP address, and transmits the results to an attacker-controlled server.

It's also equipped to collect runtime details, current date and time, username and email addresses from Git/npm configurations, as well as CI/CD environment variables for GitHub Actions, GitLab CI, Jenkins, and CircleCI.

The latest findings from CrowdStrike show that the threat actor has been active since November 2022 and claims to be a bug bounty hunter who has collected bounties from no less than nine entities across the technology, retail, and hospitality sectors.

The cybersecurity company said it has not observed information stolen from the malware appearing on stealer log shops, indicating "the operator likely uses the information stealer solely to identify bug bounty opportunities."

At least two different npm user accounts maintained by the operator have been observed pushing npm packages containing PhantomRaven. Both npm accounts are no longer accessible as of writing.

* jpdhellonpm1 - transform-jsbi-to-bigint
* jpd15 - sort-imports-es6-autofix

Some of the other online identities linked to the same operation include jpd12, jpd13, npmhell, npmpackagejpd, npmtestdharsh, jpdhackerone11, and packagedharsh.

"In August 2025, the threat actor claimed to have discovered a remote code execution (RCE) vulnerability via a malicious npm package they published," security researcher Maddie Stewart noted. "The threat actor explained that they had compromised the target machine and executed their preinstall script, which purportedly allowed them to achieve RCE."

In addition, evidence has emerged that the threat actor attempted to push packages to the Python Package Index (PyPI) repository containing code for an information stealer that exhibits similarities with PhantomRaven.

The likely use of a large language model (LLM) to generate the malware once again highlights how threat actors are increasingly adopting the technology in their operations, compressing the time and effort it takes to pull off such campaigns.

"Most criminal actors [...] rent commodity tools or operate their own proprietary malware; however, this threat actor has likely developed their proprietary PhantomRaven to compromise company assets and then used these compromises as leverage to claim rewards from reputable disclosure programs," CrowdStrike said.