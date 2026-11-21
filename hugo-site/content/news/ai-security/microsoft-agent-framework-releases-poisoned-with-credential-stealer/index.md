---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-21T00:31:29.474054+00:00'
exported_at: '2026-11-21T00:31:31.618771+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer
structured_data:
  about: []
  author: ''
  description: Two malicious Microsoft agent-framework releases on PyPI carried a
    stealer targeting Azure, Azure DevOps, and GitHub Actions tokens.
  headline: Microsoft Agent Framework Releases Poisoned With Credential Stealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Agent Framework Releases Poisoned With Credential Stealer
updated_at: '2026-11-21T00:31:29.474054+00:00'
url_hash: 982c6cc3ded16efe353d237ec0680f8d9c9f687f
---

**Hackers distributed two malicious versions of Microsoft’s Agent Framework Python package through PyPI in a November 17 supply chain attack, potentially exposing cloud and CI/CD credentials belonging to users who installed them.**

Microsoft Agent Framework is designed for developing AI agents and multi-agent applications. The affected package, agent-framework, has approximately 190,000 downloads per month.

The malicious versions, 1.26.1 and 1.26.2, were released roughly 33 minutes apart. Both have since been quarantined on PyPI, where version 1.26.0 remains the latest clean release.

Microsoft has acknowledged the incident, with an Agent Framework maintainer confirming in a
[GitHub discussion](https://github.com/microsoft/agent-framework/issues/10411)
that the compromised releases were removed from PyPI and that an investigation was underway.

The malicious distributions retained the legitimate framework components while introducing additional code that attempted to steal credentials. This allowed applications to continue functioning normally despite the compromise.

Researchers at
[OX Security](https://www.ox.security/blog/breaking-hijacked-releases-of-microsofts-official-agent-framework-steals-azure-and-ci-credentials/)
,
[Wiz](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi)
,
[Endor Labs](https://www.endorlabs.com/learn/agent-framework-compromised-software-supply-chain-attack)
, and
[SafeDep](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)
independently analyzed the malware, which exploits a Python startup mechanism to execute automatically in an affected environment.

Advertisement. Scroll to continue reading.

The malware runs whenever the Python interpreter starts, even if the application doesn’t explicitly import the compromised package.

Its targets include secrets stored in environment variables and configuration files, as well as credentials belonging to other running processes. It also attempts to obtain Azure managed identity tokens and Azure DevOps authentication tokens that could provide access to cloud resources.

The second malicious release expanded the credential-stealing functionality to GitHub Actions.

The method used to publish the malicious packages remains unknown. Unlike legitimate releases, which included both built and source distributions, the malicious versions contained only built packages. Wiz also found no corresponding releases or malicious code in Microsoft’s main source repository, suggesting the packages may have been uploaded outside the normal release process.

SafeDep identified a PyPI maintainer account named vibiret, created on the day of the attack, with publishing permissions for the affected package and five related projects. However, the account’s involvement in the malicious uploads has not been confirmed.

Organizations are advised to check developer environments, CI/CD pipelines, and container images for the compromised versions, and replace affected installations with verified packages. They should also rotate potentially exposed credentials, investigate suspicious cloud activity, and rebuild affected environments.

Microsoft’s Agent Framework repository on GitHub is inaccessible at the time of writing. Several other Microsoft repositories, including ONNX Runtime projects, have similarly
[disappeared](https://news.ycombinator.com/item?id=50539610)
, but it is unclear whether the incidents are related.

**Related**
:
[Java4Shell Vulnerability Puts Many Enterprise Applications at Risk of Takeover](https://www.securityweek.com/java4shell-vulnerability-puts-many-enterprise-applications-at-risk-of-takeover/)

**Related**
:
[Critical Perforce Puppet RCE Exploited in Attacks](https://www.securityweek.com/critical-perforce-puppet-rce-exploited-in-attacks/)

**Related**
:
[Optimizely Vulnerability Exploited to Serve Malware on Major Websites](https://www.securityweek.com/optimizely-vulnerability-exploited-to-serve-malware-on-major-websites/)