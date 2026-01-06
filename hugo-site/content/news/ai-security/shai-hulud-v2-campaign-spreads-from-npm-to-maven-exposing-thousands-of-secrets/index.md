---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-27T00:00:08.195274+00:00'
exported_at: '2025-11-27T00:00:10.656326+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html
structured_data:
  about: []
  author: ''
  description: Shai-Hulud v2 breached npm and Maven, impacting 28,000+ repos and leaking
    11,858 secrets.
  headline: Shai-Hulud v2 Campaign Spreads From npm to Maven, Exposing Thousands of
    Secrets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Shai-Hulud v2 Campaign Spreads From npm to Maven, Exposing Thousands of Secrets
updated_at: '2025-11-27T00:00:08.195274+00:00'
url_hash: a89b9556b9e446dfd4bd15fb5138fbc554bf1dba
---

The second wave of the
[Shai-Hulud supply chain attack](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html)
has spilled over to the Maven ecosystem after compromising more than 830 packages in the npm registry.

The Socket Research Team said it identified a Maven Central package named org.mvnpm:posthog-node:4.18.1 that embeds the same two components associated with Sha1-Hulud: the "setup\_bun.js" loader and the main payload "bun\_environment.js."

"This means the PostHog project has compromised releases in both the JavaScript/npm and Java/Maven ecosystems, driven by the same Shai Hulud v2 payload," the cybersecurity company
[said](https://socket.dev/blog/shai-hulud-strikes-again-v2)
in a Tuesday update.

It's worth noting that the Maven Central package is not published by PostHog itself. Rather, the "org.mvnpm"
[coordinates](https://maven.apache.org/pom.html#Maven_Coordinates)
are generated via an automated
[mvnpm process](https://github.com/mvnpm/mvnpm)
that rebuilds npm packages as Maven artifacts. The Maven Central said they are working to implement extra protections to prevent already known compromised npm components from being rebundled. As of November 25, 2025, 22:44 UTC, all mirrored copies have been purged.

The development comes as the "second coming" of the supply chain incident has
[targeted](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html)
developers globally with an aim to steal sensitive data like API keys, cloud credentials, and npm and GitHub tokens, and facilitate deeper supply chain compromise in a worm-like fashion. The latest iteration has also evolved to be more stealthy, aggressive, scalable, and destructive.

Besides borrowing the overall infection chain of the initial September variant, the
[attack](https://checkmarx.com/zero-post/shai-huluds-second-coming-npm-malware-attack-evolved/)
allows threat actors to gain unauthorized access to npm maintainer accounts and publish trojanized versions of their packages. When unsuspecting developers download and run these libraries, the embedded malicious code backdoors their own machines and scans for secrets and exfiltrates them to GitHub repositories using the stolen tokens.

The
[attack](https://semgrep.dev/blog/2025/digging-for-secrets-sha1-hulud-the-second-coming-of-the-npm-worm/)
accomplishes this by injecting
[two rogue workflows](https://www.upwind.io/feed/shai-hulud-2-npm-supply-chain-worm-attack)
, one of which registers the victim machine as a self-hosted runner and enables arbitrary command execution whenever a GitHub Discussion is opened. A second workflow is designed to systematically harvest all secrets. Over 28,000 repositories have been affected by the incident.

"This version significantly enhances stealth by utilizing the Bun runtime to hide its core logic and increases its potential scale by raising the infection cap from 20 to 100 packages," Cycode's Ronen Slavin and Roni Kuznicki
[said](https://cycode.com/blog/shai-hulud-second-coming-supply-chain-attack/)
. "It also uses a new evasion technique, exfiltrating stolen data to randomly named public GitHub repositories instead of a single, hard-coded one."

The attacks illustrate how trivial it is for attackers to take advantage of trusted software distribution pathways to push malicious versions at scale and compromise thousands of downstream developers. What's more, the self-replication nature of the malware means a single infected account is enough to amplify the blast radius of the attack and turn it into a
[widespread outbreak](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)
in a short span of time.

Further analysis by Aikido has
[uncovered](https://www.aikido.dev/blog/github-actions-incident-shai-hulud-supply-chain-attack)
that the threat actors exploited vulnerabilities, specifically focusing on CI misconfigurations in pull\_request\_target and workflow\_run workflows, in existing GitHub Actions workflows to pull off the attack and compromise projects associated with AsyncAPI, PostHog, and Postman.

The vulnerability "used the risky pull\_request\_target trigger in a way that allowed code supplied by any new pull request to be executed during the CI run," security researcher Ilyas Makari said. "A single misconfiguration can turn a repository into a patient zero for a fast-spreading attack, giving an adversary the ability to push malicious code through automated pipelines you rely on every day."

It's assessed that the activity is the continuation of a broader set of attacks targeting the ecosystem that commenced with the August 2025
[S1ngularity campaign](https://thehackernews.com/2025/08/malicious-nx-packages-in-s1ngularity.html)
impacting several Nx packages on npm.

"As a new and significantly more aggressive wave of npm supply chain malware, Shai-Hulud 2 combines stealthy execution, credential breadth, and fallback destructive behavior, making it one of the most impactful supply chain attacks of the year," Nadav Sharkazy, a product manager at
[Apiiro](https://apiiro.com/blog/shai-hulud-2-a-new-wave-of-npm-supply-chain-malware-targeting-developers-and-ci-cd-systems/)
, said in a statement.

"This malware shows how a single compromise in a popular library can cascade into thousands of downstream applications by trojanizing legitimate packages during installation."

Data compiled by
[GitGuardian](https://blog.gitguardian.com/shai-hulud-2/)
,
[OX Security](https://www.ox.security/blog/the-second-coming-shai-hulud-is-back-at-it-how-to-protect-your-org/)
, and Wiz shows that the campaign has leaked hundreds of GitHub access tokens and credentials associated with Amazon Web Services (AWS), Google Cloud, and Microsoft Azure. More than 5,000 files were uploaded to GitHub with the exfiltrated secrets. GitGuardian's analysis of 4,645 GitHub repositories has identified 11,858 unique secrets, out of which 2,298 remained valid and publicly exposed as of November 24, 2025.

Users are
[advised](https://mondoo.com/blog/navigating-the-sands-of-dune-protecting-npm-from-the-shai-hulud-worm)
to rotate all tokens and keys, audit all dependencies, remove compromised versions, reinstall clean packages, and harden developer and CI/CD environments with least-privilege access, secret scanning, and automated policy enforcement.

"Sha1-Hulud is another reminder that the modern software supply chain is still way too easy to break," Dan Lorenc, co-founder and CEO of Chainguard, said. "A single compromised maintainer and a malicious install script is all it takes to ripple through thousands of downstream projects in a matter of hours."

"The techniques attackers are using are constantly evolving. Most of these attacks don't rely on zero-days. They exploit the gaps in how open source software is published, packaged, and pulled into production systems. The only real defense is changing the way software gets built and consumed."