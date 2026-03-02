---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-02T03:16:08.858612+00:00'
exported_at: '2026-03-02T03:16:10.812374+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html
structured_data:
  about: []
  author: ''
  description: Cline CLI 2.3.0 was published with a stolen npm token, installing OpenClaw
    in an 8-hour attack affecting ~4,000 downloads.
  headline: Cline CLI 2.3.0 Supply Chain Attack Installed OpenClaw on Developer Systems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cline CLI 2.3.0 Supply Chain Attack Installed OpenClaw on Developer Systems
updated_at: '2026-03-02T03:16:08.858612+00:00'
url_hash: 8551a59d446718dea8a317cd6b1f22581cd38b1f
---

In yet another software supply chain attack, the open-source, artificial intelligence (AI)-powered coding assistant
[Cline CLI](https://www.npmjs.com/package/cline)
was updated to stealthily install
[OpenClaw](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html)
, a self-hosted autonomous AI agent that has become exceedingly popular in the past few months.

"On February 17, 2026, at 3:26 AM PT, an unauthorized party used a compromised npm publish token to publish an update to Cline CLI on the NPM registry: cline@2.3.0," the maintainers of the Cline package
[said](https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7)
in an advisory. "The published package contains a modified package.json with an added postinstall script: 'postinstall": "npm install -g openclaw@latest.'"

As a result, this causes OpenClaw to be installed on the developer's machine when Cline version 2.3.0 is installed. Cline said no additional modifications were introduced to the package and there was no malicious behavior observed. However, it noted that the installation of OpenClaw was not authorized or intended.

The supply chain attack affects all users who installed the Cline CLI package published on npm, specifically version 2.3.0, during an approximately eight-hour window between 3:26 a.m. PT and 11:30 a.m. PT on February 17, 2026. The incident does not impact Cline's Visual Studio Code (VS Code) extension and JetBrains plugin.

To mitigate the unauthorized publication, Cline maintainers have released version 2.4.0. Version 2.3.0 has since been deprecated and the compromised token has been revoked. Cline also said the npm publishing mechanism has been updated to support OpenID Connect (OIDC) via GitHub Actions.

In a
[post](https://x.com/MsftSecIntel/status/2024575596941263040)
on X, the Microsoft Threat Intelligence team said it observed a "small but noticeable uptick" in OpenClaw installations on February 17, 2026, as a result of the
[supply chain compromise](https://socket.dev/blog/cline-cli-npm-package-compromised-via-suspected-cache-poisoning-attack)
of the Cline CLI package. According to
[StepSecurity](https://www.stepsecurity.io/blog/cline-supply-chain-attack-detected-cline-2-3-0-silently-installs-openclaw)
, the compromised Cline package was downloaded roughly 4,000 times during the eight-hour stretch.

Users are advised to update to the latest version, check their environment for any unexpected installation of OpenClaw, and remove it if not required.

"Overall impact is considered low, despite high download counts: OpenClaw itself is not malicious, and the installation does not include the installation/start of the Gateway daemon," Endor Labs researcher Henrik Plate
[said](https://www.endorlabs.com/learn/supply-chain-attack-targeting-cline-installs-openclaw)
.

"Still, this event emphasizes the need for package maintainers to not only enable trusted publishing, but also disable publication through traditional tokens – and for package users to pay attention to the presence (and sudden absence) of corresponding attestations."

### Leveraging Clinejection to Leak Publication Secrets

While it's currently not clear who is behind the breach of the npm package and what their end goals were, it comes after security researcher Adnan Khan
[discovered](https://adnanthekhan.com/posts/clinejection/)
that attackers could steal the repository's authentication tokens through
[prompt injection](https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html)
by taking advantage of the fact that it is configured to automatically triage any incoming issue raised on GitHub.

"When a new issue is opened, the workflow spins up Claude with access to the repository and a broad set of tools to analyze and respond to the issue," Khan explained. "The intent: automate first-response to reduce maintainer burden."

But a misconfiguration in the workflow meant that it gave Claude excessive permissions to achieve arbitrary code execution within the default branch. This aspect, combined with a prompt injection embedded within the GitHub issue title, could be exploited by an attacker with a GitHub account to trick the AI agent into running arbitrary commands and compromise production releases.

This shortcoming, which builds upon
[PromptPwnd](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)
, has been codenamed Clinejection. It was introduced in a
[source code commit](https://github.com/cline/cline/commit/bb1d0681396b41e9b779f9b7db4a27d43570af0c)
made on December 21, 2025. The attack chain is outlined below -

* Prompt Claude to run arbitrary code in issue triage workflow
* Evict legitimate cache entries by filling the cache with more than 10GB of junk data, triggering GitHub's Least Recently Used (LRU) cache eviction policy
* Set
  [poisoned cache entries](https://adnanthekhan.com/2024/12/21/cacheract-the-monster-in-your-build-cache/)
  matching the nightly release workflow's cache keys
* Wait for the nightly publish to run at around 2 a.m. UTC and trigger on the poisoned cache entry

"This would allow an attacker to obtain code execution in the nightly workflow and steal the publication secrets," Khan noted. "If a threat actor were to obtain the production publish tokens, the result would be a devastating supply chain attack."

"A malicious update pushed through compromised publication credentials would execute in the context of every developer who has the extension installed and set to update automatically."

In other words, the attack sequence employs
[GitHub Actions cache poisoning](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/)
to pivot from the triage workflow to a highly privileged workflow, such as the Publish Nightly Release and Publish NPM Nightly workflows, and steal the nightly publication credentials, which have the same access as those used for production releases.

As it turns out,
[this is exactly what happened](https://mbgsec.com/posts/2026-02-18-raptor-finds-cline-compromise/)
, with the unknown threat actor weaponizing an active npm publish token (referred to as NPM\_RELEASE\_TOKEN or NPM\_TOKEN) to authenticate with the Node.js registry and publish Cline version 2.3.0.

"We have been talking about AI supply chain security in theoretical terms for too long, and this week it became an operational reality," Chris Hughes, VP of Security Strategy at Zenity, said in a statement shared with The Hacker News. "When a single issue title can influence an automated build pipeline and affect a published release, the risk is no longer theoretical. The industry needs to start recognizing AI agents as privileged actors that require governance."