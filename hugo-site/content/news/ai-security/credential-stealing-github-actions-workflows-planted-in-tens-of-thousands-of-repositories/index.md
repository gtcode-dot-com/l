---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-09T22:09:08.878278+00:00'
exported_at: '2026-10-09T22:09:11.934145+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/credential-stealing-github-actions.html
structured_data:
  about: []
  author: ''
  description: More than 500 GitHub accounts committed credential-stealing workflows
    to tens of thousands of repositories since October 7, Socket says.
  headline: Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands
    of Repositories
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/credential-stealing-github-actions.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of
  Repositories
updated_at: '2026-10-09T22:09:08.878278+00:00'
url_hash: fbb467666674859b4730b1f8bf300e9ca5986880
---

Cybersecurity researchers have disclosed details of an ongoing credential-theft campaign that has compromised two high-profile open-source maintainer accounts to push a malicious workflow into over 340 repositories.

"Using the account of Takashi Kitao, author of the 18,400-star game engine pyxel, the attacker pushed a malicious workflow to 27 repositories starting at 13:20 UTC," StepSecurity
[said](https://www.stepsecurity.io/blog/ghostaction-returns)
. "Eight hours later, the account of Henry Wu (henrywoo), the original author of Uber's athenadriver, was used to push the same workflow to 318 repositories in a 16-minute window, 21:10–21:26 UTC."

As of October 9, 2026, Socket
[said](https://socket.dev/blog/ghostaction-cloud-credentials)
it has identified more than 500 GitHub accounts that committed the malicious workflow to tens of thousands of repositories since October 7, 2026.

The activity has been attributed to
**[GhostAction](https://thehackernews.com/2025/09/weekly-recap-drift-breach-chaos-zero.html#:~:text=GhostAction%20Supply%20Chain%20Attack%20Steals%203%2C325%20Secrets)**
, a massive supply chain attack campaign that
[first came to light](https://www.stepsecurity.io/blog/ghostaction-campaign-over-3-000-secrets-stolen-through-malicious-github-workflows)
in September 2025. The activity impacted 817 repositories across 327 GitHub users, resulting in the exfiltration of 3,325 secrets, including PyPI, npm, and DockerHub tokens through compromised developer accounts.

Like before, both accounts have been found to push a workflow named Security Audit ("security-audit.yml") or GitHub Actions Security ("github\_actions\_security.yml"), which are designed to exfiltrate sensitive data to a hard-coded IP address ("193.32.204[.]199") over plain HTTP.

The captured data contains the repository's named GitHub Actions secrets, including CI/CD secrets, and cloud, AI, and SaaS credentials present in the working tree and the entire git history, such as AWS keys, Anthropic, OpenAI, and OpenRouter API keys, and GitHub and GitLab tokens.

The entire attack chain plays out as follows -

* The attacker obtains a maintainer's GitHub credentials, most likely a leaked personal access token (PAT) from infostealer logs or credential dumps.
* The repository's workflow files are scanned for secrets as part of a reconnaissance step.
* A workflow masquerading as a security audit is injected into the default branch under the victim's own identity.
* The embedded payload extracts the data and sends it to an attacker-controlled endpoint via curl.

"It triggers on workflow\_dispatch and an unfiltered push (any branch, any tag), checks out with fetch-depth: 0, and runs a single 'Audit' step that does four things," StepSecurity added. This includes -

* Append the repository's named secrets found during reconnaissance
* Scan the working tree for 13 credential patterns associated with AWS keys, AI services, source control services, and SaaS and cloud API keys
* Check the entire git history for the same 13 patterns to harvest credentials that may have inadvertently committed to the repository and subsequently deleted
* Pair AWS access key IDs with their matching secret access keys

Earlier this week, GitGuardian
[reported](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)
that the
**GhostAction**
campaign pushed the malicious workflow to 772 public repositories belonging to 373 GitHub users and organizations between August 31 and September 30, 2026.

The injected workflows target 2,577 secrets, including SSH private keys, Azure credentials, DockerHub and GHCR container registry credentials, database credentials, AWS access keys, FTP credentials, Google Cloud and Firebase credentials, GitHub tokens, Telegram, Slack, and Discord bot tokens, and keys associated with Cloudflare, npm, PyPI, and AI providers.

In at least one case observed on August 30, 2026, the threat actors altered the "kuafuai/DevOpsGPT" repository to embed an XMRig cryptocurrency miner in the project's Docker image. As of writing, no malicious package releases have been published using compromised publishing credentials.

Developers are advised to check their repositories for either of the two GitHub workflows since August 31, 2026, and assume compromise, if present. It's recommended to revoke the compromised GitHub credential, rotate credentials, delete the malicious workflow from all branches, and check forks of the infected repositories.

"The 279 forks in the henrywoo namespace each carry the workflow file. If Actions are enabled, subsequent pushes can trigger credential harvesting," Socket said. "Downstream forks are also at risk if they inherit the malicious workflow, either when newly created or by synchronizing with the affected upstream repository."

"Private forks and downstream mirrors are the most exposed, because private repositories are where committed credentials are actually found. Across both accounts, every run also returns a repository identifier whether or not credentials were found, so the operator holds a map of reachable execution contexts independent of any credential theft."