---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-24T04:44:17.573129+00:00'
exported_at: '2026-03-24T04:44:19.780278+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html
structured_data:
  about: []
  author: ''
  description: Trivy attack force-pushed 75 tags via GitHub Actions, exposing CI/CD
    secrets, enabling data theft and persistence across developer systems.
  headline: Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal
    CI/CD Secrets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD
  Secrets
updated_at: '2026-03-24T04:44:17.573129+00:00'
url_hash: 17c4277c895d8319f54bb28ac271f39547127e6d
---

Trivy, a popular open-source vulnerability scanner maintained by Aqua Security, was compromised a second time within the span of a month to deliver malware capable of stealing sensitive CI/CD secrets.

The latest incident impacted GitHub Actions "
[aquasecurity/trivy-action](https://github.com/aquasecurity/trivy-action)
" and "
[aquasecurity/setup-trivy](https://github.com/aquasecurity/setup-trivy)
," which are used to scan Docker container images for vulnerabilities and set up GitHub Actions workflow with a specific version of the scanner, respectively.

"We identified that an attacker force-pushed 75 out of 76 version tags in the aquasecurity/trivy-action repository, the official GitHub Action for running Trivy vulnerability scans in CI/CD pipelines," Socket security researcher Philipp Burckhardt
[said](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise)
. "These tags were modified to serve a malicious payload, effectively turning trusted version references into a distribution mechanism for an infostealer."

The payload executes within GitHub Actions runners and aims to extract valuable developer secrets from CI/CD environments, such as SSH keys, credentials for cloud service providers, databases, Git, Docker configurations, Kubernetes tokens, and cryptocurrency wallets.

The
[development](https://www.stepsecurity.io/blog/trivy-compromised-a-second-time---malicious-v0-69-4-release)
marks the second supply chain incident involving Trivy. Towards the end of February and early March 2026, an autonomous bot called hackerbot-claw
[exploited](https://thehackernews.com/2026/03/five-malicious-rust-crates-and-ai-bot.html#ai-powered-bot-exploits-github-actions)
a "pull\_request\_target" workflow to steal a Personal Access Token (PAT), which was then weaponized to seize control of the GitHub repository, delete several release versions, and push two malicious versions of its Visual Studio Code (VS Code) extension to Open VSX.

The first sign of the compromise was
[flagged](https://www.linkedin.com/posts/mccartypaul_heads-up-trivy-version-0694-has-been-share-7440548547609079808-Uloi/)
by security researcher Paul McCarty after a new compromised release (version 0.69.4) was published to the "aquasecurity/trivy" GitHub repository. The rogue version has since been removed. According to
[Wiz](https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack)
, version 0.69.4 starts both the legitimate Trivy service and the malicious code responsible for a series of tasks -

* Conduct data theft by scanning the system for environmental variables and credentials, encrypting the data, and exfiltrating it via an HTTP POST request to scan.aquasecurtiy[.]org.
* Set up persistence by using a
  [systemd service](https://redcanary.com/blog/threat-detection/attck-t1501-understanding-systemd-service-persistence/)
  after confirming that it's running on a developer machine. The systemd service is configured to run a Python script ("sysmon.py") that polls an external server to retrieve the payload and execute it.

In a statement, Itay Shakury, vice president of open source at Aqua Security,
[said](https://github.com/aquasecurity/trivy/discussions/10425)
the attackers abused a compromised credential to publish malicious trivy, trivy-action, and setup-trivy releases. In the case of "aquasecurity/trivy-action," the adversary
[force-pushed](https://www.git-tower.com/blog/force-push-in-git)
75 version tags to point to the malicious commits containing the Python infostealer payload without creating a new release or pushing to a branch, as is standard practice. Seven "aquasecurity/setup-trivy" tags were force-pushed in the same manner.

"So in this case, the attacker didn't need to exploit Git itself," Burckhardt told The Hacker News. "They had valid credentials with sufficient privileges to push code and rewrite tags, which is what enabled the tag poisoning we observed. What remains unclear is the exact credential used in this specific step (e.g., a maintainer PAT vs. automation token), but the root cause is now understood to be credential compromise carried over from the earlier incident."

The security vendor also acknowledged that the latest attack stemmed from incomplete containment of the hackerbot-claw incident. "We rotated secrets and tokens, but the process wasn't atomic, and attackers may have been privy to refreshed tokens," Shakury said. "We are now taking a more restrictive approach and locking down all automated actions and any token in order to thoroughly eliminate the problem."

The stealer operates in three stages: harvesting environment variables from the runner process memory and the file system, encrypting the data, and exfiltrating it to the attacker-controlled server ("scan.aquasecurtiy[.]org").

Should the exfiltration attempt fail, the victim's own GitHub account is abused to stage the stolen data in a public repository named "tpcp-docs" by making use of the captured INPUT\_GITHUB\_PAT, an environment variable used in GitHub Actions to pass a GitHub PAT for authentication with the GitHub API.

It's currently not known who is behind the attack, although there are signs that the threat actor known as
[TeamPCP](https://thehackernews.com/2026/02/teampcp-worm-exploits-cloud.html)
may be behind it. This assessment is based on the fact that the credential harvester self-identifies as "TeamPCP Cloud stealer" in the source code. Also known as DeadCatx3, PCPcat, PersyPCP, ShellForce, and CipherForce, the
[group](https://www.elastic.co/security-labs/teampcp-container-attack-scenario)
is known for acting as a cloud-native cybercrime platform designed to breach modern cloud infrastructure to facilitate data theft and extortion.

"The credential targets in this payload are consistent with the group's broader cloud-native theft-and-monetization profile," Socket said. "The heavy emphasis on Solana validator key pairs and cryptocurrency wallets is less well-documented as a TeamPCP hallmark, though it aligns with the group's known financial motivations. The self-labeling could be a false flag, but the technical overlap with prior TeamPCP tooling makes genuine attribution plausible."

Users are advised to ensure that they are using the latest safe releases -

"If you suspect you were running a compromised version, treat all pipeline secrets as compromised and rotate immediately," Shakury said. Additional mitigation steps include blocking the exfiltration domain and the associated IP address (45.148.10[.]212) at the network level, and checking GitHub accounts for repositories named "tpcp-docs," which may indicate successful exfiltration via the fallback mechanism.

"Pin GitHub Actions to full SHA hashes, not version tags," Wiz researcher Rami McCarthy said. "Version tags can be moved to point at malicious commits, as demonstrated in this attack."

### Update

The supply chain attack on Trivy appears to have had a cascading impact, with threat actors leveraging the stolen data to compromise several npm packages and push malicious versions containing a self-propagating worm. More details about the activity
[can be found here](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html)
.

Aqua Security has published a
[detailed advisory](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23)
of the supply chain attack, stating the attacker created a malicious version of Trivy (0.69.4) by following the below three steps -

* Pushing a commit (1885610c) that swapped the actions/checkout reference to an imposter commit (70379aad) containing a composite action that downloaded malicious Go source files from a typosquatted domain.
* Adding --skip=validate to goreleaser to bypass binary validation.
* Tagging this commit as v0.69.4, triggering the release pipeline.

Aqua also noted that the attacker compromised "trivy-action" by force-pushing 76 of 77 version tags to malicious commits that injected an infostealer malware. It's worth noting that 76 of the 77 version tags in the GitHub repository (v0.0.1 through v0.34.2) were poisoned, and one of them is a duplicate (v0.0.10). The sole clean tag was v0.35.0.

"The v0.0.10 tag appears to be a legacy inconsistency in naming (not following the usual semver format), which is why we treated it as a duplicate rather than a distinct affected version," Socket told The Hacker News. "It looks like Aqua’s advisory is counting all tag names, including the duplicates, which explains the difference."

In a similar manner, the threat actors force-pushed seven existing tags associated with "setup-trivy" (v0.2.0 – v0.2.6) to malicious commits. "The malicious 'action.yaml' contained the same infostealer as trivy-action, injected as a 'Setup environment' step that executes before the legitimate Trivy installation," Aqua said.

As recommended actions, the company is also urging users who may have run any of the infected versions to assume compromise and perform the following actions -

* Audit Trivy versions
* Review all workflows using aquasecurity/trivy-action or aquasecurity/setup-trivy for signs of compromise
* Look for repositories named "tpcp-docs" in the GitHub organization
* Pin GitHub Actions to full, immutable commit SHA hashes instead of version tags