---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T02:44:59.003953+00:00'
exported_at: '2026-04-02T02:45:02.263320+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html
structured_data:
  about: []
  author: ''
  description: Trivy supply chain attack pushed malicious Docker images on March 22,
    enabling credential theft and worm spread, impacting cloud environments.
  headline: Trivy Hack Spreads Infostealer via Docker, Triggers Worm and Kubernetes
    Wiper
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trivy Hack Spreads Infostealer via Docker, Triggers Worm and Kubernetes Wiper
updated_at: '2026-04-02T02:44:59.003953+00:00'
url_hash: 4653c4346e5ead8a3a182851f58c8ce6f6bbe08a
---

Cybersecurity researchers have uncovered malicious artifacts distributed via Docker Hub following the
[Trivy supply chain attack](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html)
, highlighting the widening blast radius across developer environments.

The last known clean release of
[Trivy](https://hub.docker.com/r/aquasec/trivy/tags)
on Docker Hub is 0.69.3. The malicious versions 0.69.4, 0.69.5, and 0.69.6 have since been removed from the container image library.

"New image tags 0.69.5 and 0.69.6 were pushed on March 22 without corresponding GitHub releases or tags. Both images contain indicators of compromise associated with the same TeamPCP infostealer observed in earlier stages of this campaign," Socket security researcher Philipp Burckhardt
[said](https://socket.dev/blog/trivy-docker-images-compromised)
.

The development comes in the wake a
[supply chain compromise](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html)
of Trivy, a popular open-source vulnerability scanner maintained by Aqua Security, allowing the threat actors to leverage a compromised credential to push a credential stealer within trojanized versions of the tool and two related GitHub Actions "aquasecurity/trivy-action" and "aquasecurity/setup-trivy."

The attack has had downstream impacts, with the attackers leveraging the stolen data to compromise dozens of npm packages to distribute a self-propagating worm known as
[CanisterWorm](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html)
. The incident is believed to be the work of a threat actor tracked as TeamPCP.

According to the OpenSourceMalware team, the attackers have defaced all 44 internal repositories associated with Aqua Security's "
[aquasec-com](https://github.com/aquasec-com)
" GitHub organization by renaming each of them with a "tpcp-docs-" prefix, setting all descriptions to "TeamPCP Owns Aqua Security," and exposing them publicly.

It's worth noting that the "aquasec-com" account is distinct from the cloud security vendor's other well-known GitHub organization account, "aquasecurity," which hosts the impacted Trivy scanner and GitHub Actions, along with various open-source projects. The newly compromised organization contains proprietary source code, including source code for Tracee, internal Trivy forks, CI/CD pipelines, Kubernetes operators, and team knowledge bases.

All the repositories are said to have been modified in a scripted 2-minute burst between 20:31:07 UTC and 20:32:26 UTC on March 22, 2026. It's been assessed with high confidence that the threat actor leveraged a compromised "Argon-DevOps-Mgt" service account for this purpose.

"Our forensic analysis of the GitHub Events API points to a compromised service account token — likely stolen during TeamPCP's prior Trivy GitHub Actions compromise — as the attack vector," security researcher Paul McCarty
[said](https://opensourcemalware.com/blog/teampcp-aquasec-com-github-org-compromise)
. "This is a service/bot account (GitHub ID 139343333, created 2023-07-12) with a critical property: it bridges both GitHub orgs."

"One compromised token for this account gives the attacker write/admin access to both organizations," McCarty added.

The development is the latest escalation from a threat actor that's has built a reputation for targeting cloud infrastructures, while progressively building capabilities to systemically exposed Docker APIs, Kubernetes clusters, Ray dashboards, and Redis servers to steal data, deploy ransomware, conduct extortion, and mine cryptocurrency.

Their growing sophistication is best exemplified by the emergence of a new wiper malware that spreads through CanisterWorm, as well as by exploiting SSH via stolen keys and exposed Docker APIs on port 2375 across the local subnet.

The new "kamikaze" wiper attributed to TeamPCP has been found to go beyond credential theft to wiping entire Kubernetes (K8s) clusters located in Iran. The shell script uses the same ICP canister linked to CanisterWorm and then runs checks to identify Iranian systems.

"On Kubernetes: deploys privileged DaemonSets across every node, including control plane," Aikido security researcher Charlie Eriksen
[said](https://www.aikido.dev/blog/teampcp-stage-payload-canisterworm-iran)
. "Iranian nodes get wiped and force-rebooted via a container named 'kamikaze.' Non-Iranian nodes get the CanisterWorm backdoor installed as a systemd service. Non-K8s Iranian hosts get 'rm -rf / --no-preserve-root.'"

Eriksen told The Hacker News it's currently not known if TeamPCP is also behind the "
[hackerbot-claw](https://thehackernews.com/2026/03/five-malicious-rust-crates-and-ai-bot.html#ai-powered-bot-exploits-github-actions)
" incident that led to the breach of Trivy earlier this month. Given the ongoing nature of the attack, it's imperative that organizations review their use of Trivy in CI/CD pipelines, avoid using affected versions, and treat any recent executions as potentially compromised.

"This compromise demonstrates the long tail of supply chain attacks," OpenSourceMalware said. "A credential harvested during the Trivy GitHub Actions compromise months ago was weaponized today to deface an entire internal GitHub organization. The Argon-DevOps-Mgt service account — a single bot account bridging two orgs with a long-lived PAT — was the weak link."

"From cloud exploitation to supply chain worms to Kubernetes wipers, they are building capability and targeting the security vendor ecosystem itself. The irony of a cloud security company being compromised by a cloud-native threat actor should not be lost on the industry.

### Update

In a formal update shared on March 23, 2026, Aqua Security
[said](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/)
its investigation is "actively focused on validating that all access paths have been identified and fully closed," adding there is no indication its commercial products were impacted by the incident. The attack is now being tracked under the CVE identifier
**[CVE-2026-33634](https://nvd.nist.gov/vuln/detail/CVE-2026-33634)**
(CVSS score: 9.4).

"The mechanics here weren't novel. The attacker, with write access to the repository, force-pushed tags to a new commit containing a modified entry point and relied on the fact that most workflows reference actions by tag," CrowdStrike
[said](https://www.crowdstrike.com/en-us/blog/from-scanner-to-stealer-inside-the-trivy-action-supply-chain-compromise/)
. "For a defender, the takeaway is to pin your actions by committing SHA, monitor your CI/CD runners with the same rigor as production hosts, and treat any code that runs in your pipeline as code that runs in your infrastructure."

*(The story was updated after publication on March 25, 2026, with additional insights from Aikido.)*