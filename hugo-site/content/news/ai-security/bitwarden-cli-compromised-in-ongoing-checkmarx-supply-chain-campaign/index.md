---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T16:15:23.307024+00:00'
exported_at: '2026-04-23T16:15:25.767989+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html
structured_data:
  about: []
  author: ''
  description: Bitwarden CLI 2026.4.0 was compromised via GitHub Actions in Checkmarx
    campaign, exposing secrets and distributing malicious npm code
  headline: Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign
updated_at: '2026-04-23T16:15:23.307024+00:00'
url_hash: 6efd8aabaa2d293aac535b0d67341511ba0e7ecd
---

[Bitwarden CLI](https://www.npmjs.com/package/@bitwarden/cli?activeTab=versions)
has been compromised as part of the newly discovered and ongoing
[Checkmarx supply chain campaign](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html)
, according to new findings from JFrog and Socket.

"The affected package version appears to be
[@bitwarden/cli@2026.4.0](https://socket.dev/npm/package/@bitwarden/cli/overview/2026.4.0)
, and the malicious code was published in 'bw1.js,' a file included in the package contents," the application security company
[said](https://socket.dev/blog/bitwarden-cli-compromised)
.

"The attack appears to have leveraged a compromised GitHub Action in Bitwarden's CI/CD pipeline, consistent with the pattern seen across other affected repositories in this campaign."

In a post on X, JFrog
[said](https://x.com/JFrogSecurity/status/2047268576071991766)
the rogue version of the package "steals GitHub/npm tokens, .ssh, .env, shell history, GitHub Actions and cloud secrets, then exfiltrates the data to private domains and as GitHub commits."

Specifically, the malicious code is
[executed](https://research.jfrog.com/post/bitwarden-cli-hijack/)
by means of a preinstall hook, resulting in the theft of local, CI, GitHub, and cloud secrets. The data is exfiltrated to the domain "audit.checkmarx[.]cx" and to a GitHub repository as a fallback if the primary method fails.

The entire series of actions is listed below -

* It launches a credential stealer that targets developer secrets, GitHub Actions environments, and artificial intelligence (AI) coding tool configurations, including Claude, Kiro, Cursor, Codex CLI, and Aider.
* The stolen data is encrypted with AES-256-GCM and exfiltrated to audit.checkmarx[.]cx, a domain impersonating Checkmarx.
* If GitHub tokens are found, the malware weaponizes them to inject malicious Actions workflows into repositories and extract CI/CD secrets.

"A single developer with @bitwarden/cli@2026.4.0 installed can become the entry point for a broader supply chain compromise, with the attacker gaining persistent workflow injection access to every CI/CD pipeline the developer’s token can reach," StepSecurity
[said](https://www.stepsecurity.io/blog/bitwarden-cli-hijacked-on-npm-bun-staged-credential-stealer-targets-developers-github-actions-and-ai-tools)
.

While the malicious version is no longer available for download from npm, Socket said the compromise follows the same GitHub Actions supply chain vector identified in the Checkmarx campaign.

As part of the effort, threat actors have been
[found](https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html)
abusing stolen GitHub tokens to inject a new GitHub Actions workflow that captures secrets available to the workflow run, and uses harvested npm credentials to push malicious versions of the package to read the malware to downstream users.

According to security researcher Adnan Khan, the threat actor is said to have used a
[malicious workflow](https://github.com/bitwarden/clients/blob/03df1ecd86132e06643d24c856d8976d1b497945/.github/workflows/publish-cli.yml)
to publish the malicious bitwarden CLI. "I believe this is the first time a package using NPM trusted publishing has been compromised," Khan
[added](https://x.com/adnanthekhan/status/2047276201429897679)
.

|  |
| --- |
|  |
| Bitwarden CLI Attack Chain | Source: OX Security |

It's suspected that the threat actor known as TeamPCP is behind the latest attack aimed at Checkmarx. As of writing, TeamPCP's
[X account has been suspended](https://x.com/pcpcats/)
for violating the platform's rules.

OX Security, in a breakdown of the attack,
[said](https://www.ox.security/blog/shai-hulud-bitwarden-cli-supply-chain-attack/)
it identified the string "Shai-Hulud: The Third Coming" in the package, suggesting this could likely be the next phase of the
[supply chain attack campaign](https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html)
that came to light last year.

|  |
| --- |
|  |
| Reference to the "Shai-Hulud: The Third Coming" |

"The latest Shai Hulud incident is just the latest in a long chain of threats targeting developers around the world. User data is being publicly exfiltrated to GitHub, often going undetected because security tools typically don't flag data being sent there," Moshe Siman Tov Bustan, Security Research Team Lead at OX Security, said.

"This makes the risk significantly more dangerous: anyone searching GitHub can potentially find and access those credentials. At that point, sensitive data is no longer in the hands of a single threat actor – it’s exposed to anyone."

Like in the case of the Checkmarx incident, the stolen data is exfiltrated to public repositories created under victim accounts using a Dune-themed naming scheme in the same format "<word>-<word>-<3 digits>."But in an interesting shift, the malware is also designed to quit execution on systems if their locale corresponds to Russia.

"The shared tooling strongly suggests a connection to the same malware ecosystem, but the operational signatures differ in ways that complicate attribution," Socket said. "This suggests either a different operator using shared infrastructure, a splinter group with stronger ideological motivations, or an evolution in the campaign's public posture."

When reached for comment, Bitwarden
[confirmed](https://community.bitwarden.com/t/bitwarden-statement-on-checkmarx-supply-chain-incident/96127)
the incident and said it stemmed from the compromise of its npm distribution mechanism following the Checkmarx supply chain attack, but emphasized that no end-user data was accessed as part of the attack. The entire statement shared with The Hacker News is reproduced verbatim below -

*The Bitwarden security team identified and contained a malicious package that was briefly distributed through the npm delivery path for @bitwarden/cli@2026.4.0 between 5:57 PM and 7:30 PM (ET) on April 22, 2026, in connection with a broader Checkmarx supply chain incident.*

*The investigation found no evidence that end user vault data was accessed or at risk, or that production data or production systems were compromised. Once the issue was detected, compromised access was revoked, the malicious npm release was deprecated, and remediation steps were initiated immediately.*

*The issue affected the npm distribution mechanism for the CLI during that limited window, not the integrity of the legitimate Bitwarden CLI codebase or stored vault data.*

*Users who did not download the package from npm during that window were not affected. Bitwarden has completed a review of internal environments, release paths, and related systems, and no additional impacted products or environments have been identified at this time. A CVE for Bitwarden CLI version 2026.4.0 is being issued in connection with this incident.*

*(This is a developing story. Please check for more details.)*