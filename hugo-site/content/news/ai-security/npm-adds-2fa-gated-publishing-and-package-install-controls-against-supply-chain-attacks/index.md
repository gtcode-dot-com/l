---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-24T00:20:01.846937+00:00'
exported_at: '2026-05-24T00:20:05.145116+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html
structured_data:
  about: []
  author: ''
  description: GitHub added npm staged publishing with mandatory 2FA approval to reduce
    software supply chain attack risks.
  headline: npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply
    Chain Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain
  Attacks
updated_at: '2026-05-24T00:20:01.846937+00:00'
url_hash: a3fd847c33e47db078397ec9abd3bf043eef7a69
---

**

Ravie Lakshmanan
**

May 23, 2026

Software Supply Chain / DevSecOps

GitHub has rolled out new controls for npm to improve the security of the software supply chain, giving maintainers the ability to explicitly approve a release prior to the packages becoming publicly available for installation.

Called staged publishing, the feature is now generally available on npm. It mandates that a human maintainer pass a two-factor authentication (2FA) challenge to approve a package before it is pushed to the npmjs[.]com.

"Instead of a direct publish that immediately makes a package version available to consumers, the prebuilt tarball is uploaded to a stage queue where a maintainer must explicitly approve it before it becomes installable," GitHub
[said](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/)
.

The Microsoft-owned subsidiary said the change ensures "proof of presence" for every publish, including those that come from non-interactive CI/CD workflows and trusted publishing with OpenID Connect (OIDC) authentication.

Before using
[staged publishing](https://docs.npmjs.com/staged-publishing)
, package maintainers have to meet the following criteria -

* Have publish access to the package
* Package already exists on the npm registry, meaning a brand new package cannot be staged
* 2FA is enabled for the account

Developers can use the command "npm stage publish" from the root directory of the package to submit it to a staging area. To use this command, it's essential to update to npm CLI 11.15.0 or newer. For optimal protection, GitHub is recommending that staged publishing be paired with
[trusted publishing](https://docs.npmjs.com/trusted-publishers)
using OIDC.

A second update focused on npm relates to the introduction of three new install source flags alongside the existing -allow-git flag -

* --allow-file: Controls installs from local file paths and local tarballs
* --allow-remote: Controls installs from remote URLs, including https tarballs
* --allow-directory: Controls installs from local directories

The flags allow developers to "apply the same explicit-allowlist approach to every non-registry install source," GitHub said.

The development comes amid a
[massive surge](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)
in software supply chain attacks targeting open-source ecosystems over the past few months, with one cybercriminal group known as
[TeamPCP](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
engaging in poisoning popular packages at an unprecedented scale through a self-perpetuating cycle of compromises.