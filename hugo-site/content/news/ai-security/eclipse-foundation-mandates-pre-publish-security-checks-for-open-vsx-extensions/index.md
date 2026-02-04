---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-04T08:15:15.597448+00:00'
exported_at: '2026-02-04T08:15:18.054565+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html
structured_data:
  about: []
  author: ''
  description: Eclipse Foundation to require pre-publish security checks for Open
    VSX extensions to reduce VS Code supply-chain risk.
  headline: Eclipse Foundation Mandates Pre-Publish Security Checks for Open VSX Extensions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Eclipse Foundation Mandates Pre-Publish Security Checks for Open VSX Extensions
updated_at: '2026-02-04T08:15:15.597448+00:00'
url_hash: 15d68715c81c45db605a5f35075e0cfcfbaea820
---

**

Ravie Lakshmanan
**

Feb 04, 2026

Supply Chain Security / Secure Coding

The Eclipse Foundation, which maintains the Open VSX Registry, has announced plans to enforce security checks before Microsoft Visual Studio Code (VS Code) extensions are published to the open-source repository to combat supply chain threats.

The move marks a shift from a reactive to a proactive approach to ensure that malicious extensions don't end up getting published on the Open VSX Registry.

"Up to now, the Open VSX Registry has relied primarily on post-publication response and investigation. When a bad extension is reported, we investigate and remove it," Christopher Guindon, director of software development at the Eclipse Foundation,
[said](https://blogs.eclipse.org/post/christopher-guindon/strengthening-supply-chain-security-open-vsx)
.

"While this approach remains relevant and necessary, it does not scale as publication volume increases and threat models evolve."

The change comes as open-source package registries and extension marketplaces have increasingly become attack magnets, enabling bad actors to target developers at scale through a variety of methods such as namespace impersonation and typosquatting. As recently as last week, Socket
[flagged](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html)
an incident where a compromised publisher's account was used to push poisoned updates.

By implementing pre-publish checks, the idea is to limit the window of exposure and flag the following scenarios, as well as quarantine suspicious uploads for review instead of publishing them immediately -

* Clear cases of extension name or namespace impersonation
* Accidentally published credentials or secrets
* Known malicious patterns

It's worth noting that Microsoft already has a
[similar multi-step vetting process](https://developer.microsoft.com/blog/security-and-trust-in-visual-studio-marketplace)
in place for its Visual Studio Marketplace. This includes scanning incoming packages for malware, then rescanning every newly published package "shortly" after it's been published, and periodic bulk rescanning of all the packages.

The extension verification program is expected to be rolled out in a staged fashion, with the maintainers using the month of February 2026 to monitor newly published extensions without blocking publication to fine-tune the system, reduce false positives, and improve feedback. The enforcement will begin next month.

"The goal and intent are to raise the security floor, help publishers catch issues early, and keep the experience predictable and fair for good-faith publishers," Guindon said.

"Pre-publish checks reduce the likelihood that obviously malicious or unsafe extensions make it into the ecosystem, which increases confidence in the Open VSX Registry as shared infrastructure."