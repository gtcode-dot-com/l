---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-14T23:34:42.909381+00:00'
exported_at: '2026-10-14T23:34:45.462566+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
structured_data:
  about: []
  author: ''
  description: GitHub now expires unvalidated npm trusted publisher bindings after
    48 hours to limit package hijacks through reclaimed repository names.
  headline: GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable
    to Hijacking
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable to
  Hijacking
updated_at: '2026-10-14T23:34:42.909381+00:00'
url_hash: 3770e65c491fe5dfacc0fc5b2f8abd2d295a5c1b
---

GitHub has taken the step of expiring unvalidated npm trusted publishing configurations 48 hours after creation after researchers found that it was possible for an attacker to push new versions of a different user's package without having to steal their credentials.

"Your configuration becomes validated and exempt from expiry after its first successful publish," the Microsoft-owned subsidiary
[said](https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire/)
. "Changing the repository or project identity requires a new trust relationship with a fresh 48-hour validation window -- ordinary edits don't restart the deadline."

The change contains the risk associated with trusting a repository or project name that changes ownership, GitHub said, adding npm also rejects trusted publishing tokens from GitHub Actions issue\_comment events going forward, along with the existing
[pull\_request\_target](https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html)
restriction.

In an update to its documentation, GitHub
[states](https://docs.npmjs.com/trusted-publishers#trusted-publisher-configuration-expiry)
that a newly created trusted publisher configuration must complete its first successful publish within two days, which validates the configuration and binds it to the "repository's immutable identity."

The development comes in response to findings from Bloom Security, which
[discovered](https://bloom.security/blog/slugfest-millions-of-ai-agents-download-exposed-npm-packages)
a loophole within npm's trusted publishing to take over thousands of packages and trigger a
[Shai-Hulud-style](https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html)
cascading supply chain attack. The findings were reported to GitHub on June 6, 2026.

"Imagine this: an attacker compromises a single package. An AI agent on a popular package maintainer's device autonomously pulls it for a project," security researcher Golan Myers said. "That single endpoint is used to push malicious code to the popular package. All the package users are exposed. All because one person with the correct access was exposed."

Trusted publishing was
[introduced](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/)
in npm in July 2025 as a credential-free authentication method that allows developers to push npm packages from a CI/CD platform, such as GitHub Actions, using OpenID Connect (OIDC) tokens.

When trusted publishing is configured, the developer's CI/CD provider generates a short-lived cryptographic token for a specific workflow run that the npm registry verifies against a
[pre-authorized configuration](https://docs.npmjs.com/trusted-publishers#step-2-configure-your-cicd-workflow)
.

This eliminates the need to store, rotate, or manually manage long-lived npm secrets, reducing the risk of credential leaks. It also automatically generates
[provenance attestations](https://docs.npmjs.com/generating-provenance-statements)
for npm packages, allowing users to establish where a package was built and who published it, thereby strengthening software supply chain security.

However, as Bloom Security found, this security architecture suffered from a problem in how it identified that repository, also called a slug (i.e, the combination of the owner or organization and the repository name that's formatted as "owner/repository").

"It records the repository's address, [...] instead of the permanent ID GitHub assigns it, at least until a version is first published from that repository," Myers explained. "It is like a lock that checks the address on the door rather than who owns the house: when the owner moves out, whoever moves in gets the key."

Put differently, the numeric IDs that survive through repository renaming and transfers are carried by GitHub's OIDC tokens, but are completely ignored by npm until the first successful publish from that repository.

This means the trust is anchored to a name as opposed to an immutable repository ID, a loophole that can be abused by claiming abandoned slugs to inherit their trust. For this attack to succeed, the only prerequisite is that the victim's trusted publisher points to a GitHub slug an attacker can claim, and the repository has never been used to publish a version of the package to npm.

Once such a slug becomes available for use after a maintainer renames, transfers, or deletes a repository, an attacker can follow the steps below -

* Create a repository at the freed slug at the "owner/repository" path, which causes GitHub to issue a fresh repository ID.
* Create and trigger an npm publish workflow, which mints an OIDC token carrying the reclaimed slug and the new numeric repository ID
* Submit the token to the npm exchange endpoint. Npm finds that the repository claim matches the stored slug and issues a publish credential.
* The attacker receives a time-limited publish token for a package they do not own and pushes malicious changes to the registry.

An attack of this kind, codenamed
**SlugFest**
, can be abused to publish a new "malicious" version of the victim package under the legitimate package name, while inheriting existing reputation, download counts, and dependent relationships. This, in turn, can lead to supply chain attacks at scale.

AI agents running on developer machines can further compound the risk. "Agents resolve dependencies on their own, tend to take the latest version, and rarely check where a package came from," Bloom Security said. "A malicious version published through a reclaimed slug gets pulled in and runs with no human-in-the-loop."

The cybersecurity company said it found over 1,500 vulnerable packages that have been collectively downloaded more than 10 million times.

Developers who maintain npm packages are advised to perform the following actions -

* Audit trusted publisher bindings and verify if the listed repository slug still resolves to the repository under their control.
* If the repository has been renamed or transferred, delete the existing trust binding and re-create it pointing at the current slug.
* Monitor for unexpected npm publish events.
* Delete trust bindings every time a repository is deleted, transferred, or renamed.

"The attack requires no insider knowledge, no credential theft, and no race condition," Myers said. "The only precondition is slug availability (on a binding that has not yet been used to publish), which is entirely a function of the victim's own repository hygiene."

"What this research demonstrates is something the security community has seen repeatedly across supply chain attacks: the binding between a human-readable identifier and the thing it identifies is the most important invariant in any trust system. When that binding can be silently replaced – by the ordinary act of renaming a repository, not by any attacker action – the trust guarantee collapses."

This is not the first time unconventional supply chain attack vectors have been discovered. Earlier this August, Bloom Security also found that both Open VSX and Microsoft's VS Code Marketplace allowed extension packs to reference non-existent extensions in the marketplaces.

The technique, referred to as Extension Resurrection, can be weaponized to hijack extensions already referenced inside these trusted bundles just by claiming a namespace left unclaimed. As many as 87 packs in Open VSX and 677 packs in the VS Code Marketplace were flagged as vulnerable.

"Attackers could claim those empty slots, publish malicious code under them, and have it installed automatically alongside the trusted pack – silently pushing updates to anyone who installed the pack previously," Myers
[noted](https://bloom.security/blog/extension-resurrection)
at the time. "Because extensions run with full host access, this effectively amounts to [remote code execution] delivered under the guise of legitimacy."