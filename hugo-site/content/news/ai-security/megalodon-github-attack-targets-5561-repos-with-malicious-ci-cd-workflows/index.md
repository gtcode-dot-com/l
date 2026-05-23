---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-23T03:04:19.256849+00:00'
exported_at: '2026-05-23T03:04:21.556981+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
structured_data:
  about: []
  author: ''
  description: Megalodon pushed 5,718 malicious GitHub commits in 6 hours, exposing
    CI secrets and cloud credentials at scale.
  headline: Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Megalodon GitHub Attack Targets 5,561 Repos with Malicious CI/CD Workflows
updated_at: '2026-05-23T03:04:19.256849+00:00'
url_hash: 143167e87dbe820093cbea33ac9d60e83ed06daf
---

Cybersecurity researchers have disclosed details of a new automated campaign called
**Megalodon**
that has pushed 5,718 malicious commits to 5,561 GitHub repositories within a six-hour window.

"Using throwaway accounts and forged author identities (build-bot, auto-ci, ci-bot, pipeline-bot), the attacker injected GitHub Actions workflows containing base64-encoded bash payloads that exfiltrate CI secrets, cloud credentials, SSH keys, OIDC tokens, and source code secrets to a C2 server at 216.126.225[.]129:8443," SafeDep
[said](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/)
in a report.

The complete list of data harvested by the malware is below -

* CI environment variables, /proc/\*/environ, and PID 1 environment
* Amazon Web Services (AWS) credentials
* Google Cloud access tokens
* Instance role credentials obtained by querying AWS IMDSv2, Google Cloud metadata, and Microsoft Azure Instance Metadata Service (IMDS) endpoints
* SSH private keys
* Docker and Kubernetes configurations
* Vault tokens
* Terraform credentials
* Shell history
* API keys, database connection strings, JWTs, PEM private keys, and cloud tokens matching more than 30 secret regular expression patterns
* GitHub Actions OIDC token request URL and token
* GITHUB\_TOKEN, GitLab CI/CD tokens, and Bitbucket tokens
* .env files, credentials.json, service-account.json, and other configuration files

One of the impacted packages is @tiledesk/tiledesk-server, which bundles a Base64-encoded bash payload within a GitHub Actions workflow file. In all, 5,718 commits were pushed against 5,561 distinct repositories on May 18, 2026, between 11:36 a.m. and 5:48 p.m. UTC.

"The attacker rotated through four author names (build-bot, auto-ci, ci-bot, pipeline-bot) and seven commit messages, all mimicking routine CI maintenance," SafeDep said. "The attacker used throwaway GitHub accounts with random 8-character usernames (e.g., rkb8el9r, bhlru9nr, lo6wt4t6), set git config to forge the author identity, and pushed via compromised PATs or deploy keys."

Two payload variants have been observed as part of the large-scale campaign: SysDiag, a mass variant which adds a new workflow that's triggered on every push and pull request, and Optimize-Build, a targeted variant that activates only on
[workflow\_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch)
, a GitHub Actions trigger that allows users to manually run a workflow on-demand. In the case of Tiledesk, the targeted approach is used to target CI/CD runners, and not when the npm package is installed.

"The tradeoff is reach: on: push would guarantee execution on every commit to master, hitting more targets without intervention," SafeDep added. "Workflow\_dispatch sacrifices that for operational security. With 5,700+ repos compromised, even a small fraction yielding a usable GITHUB\_TOKEN gives the attacker enough targets for on-demand triggering."

The result is that once a repository owner merges the commit, the malware executes inside their CI/CD pipelines and spreads further, enabling the theft of credentials and secrets at scale.

"We've entered a new supply chain attack era, and
[TeamPCP compromising GitHub](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
was only the beginning," OX Security's Moshe Siman Tov Bustan
[said](https://www.ox.security/blog/megalodon-cicd-malware-github/)
. "What's coming next is an endless wave, a tsunami of cyber attacks on developers worldwide."

The development comes as TeamPCP has weaponized the interlinked software supply chain to corrupt hundreds of open-source tools, worming their way through several ecosystems and extorting victims for profit in some cases. Microsoft-owned GitHub has become the latest addition to the group's long list of victims, which also includes TanStack, Grafana Labs, OpenAI, and Mistral AI.

TeamPCP attacks have fueled a cyclical exploitation of popular open-source projects, where one compromise feeds the next, allowing the malware to spread like wildfire in a worm-like fashion. The group also appears to be financially motivated and has established partnerships with BreachForums and other extortion crews like LAPSUS$ and VECT.

What's more, the group seems to be geopolitically motivated as well, as evidenced by the
[deployment of wiper malware](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html)
upon detecting machines located in Iran and Israel.

The fallout from TeamPCP's attack spree and the
[Mini Shai-Hulud worm](https://trustedsec.com/blog/shai-hulud-is-back)
has
[prompted](https://x.com/npmjs/status/2056960835030016286)
npm to invalidate granular access tokens with write access that bypasses two-factor authentication (2FA). NPM is also urging users to switch to
[Trusted Publishing](https://docs.npmjs.com/trusted-publishers/)
to reduce reliance on such tokens.

"By burning every bypass-2FA token on the platform, npm cuts off the credentials the worm has already collected," application security firm Socket
[said](https://socket.dev/blog/npm-invalidates-tokens-mini-shai-hulud)
. "Maintainers issue new ones. The worm, still active in the wild, goes back to harvesting them. The reset buys breathing room. It does not close the underlying hole."

Activity clusters like Megalodon and TeamPCP involve compromising legitimate packages to distribute malware. In contrast, a throwaway account named "
[polymarketdev](https://www.npmjs.com/~polymarketdev)
" has been found to publish nine malicious npm packages impersonating Polymarket trading CLI tools within a 30-second window to steal victims' Ethereum/Polygon private keys via a postinstall hook.

As of writing, they are still available for download from npm. The names of the packages are below -

* polymarket-trading-cli
* polymarket-terminal
* polymarket-trade
* polymarket-auto-trade
* polymarket-copy-trading
* polymarket-bot
* polymarket-claude-code
* polymarket-ai-agent
* polymarket-trader

"On install, a postinstall script displays a fake wallet onboarding prompt that asks the user to paste their private key, claiming 'it stays encrypted,'" SafeDep
[said](https://safedep.io/malicious-polymarket-npm-crypto-wallet-drainer/)
. "The script POSTs the raw key in plaintext to a Cloudflare Worker at hxxps://polymarketbot.polymarketdev.workers[.]dev/v1/wallets/keys."

"The attacker built a functional trading CLI around a credential theft operation. Social engineering carries the attack: the postinstall prompt looks like standard wallet onboarding, the masking mimics secure input, and the GitHub repo provides false credibility"