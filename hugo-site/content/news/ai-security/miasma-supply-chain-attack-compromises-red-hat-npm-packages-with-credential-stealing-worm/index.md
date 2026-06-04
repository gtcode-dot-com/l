---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-04T05:11:47.547911+00:00'
exported_at: '2026-06-04T05:11:49.226805+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
structured_data:
  about: []
  author: ''
  description: Compromised npm packages targeted Red Hat cloud services, enabling
    credential theft and expanding supply chain risks.
  headline: Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing
    Worm
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Miasma Supply Chain Attack Compromises Red Hat npm Packages with Credential-Stealing
  Worm
updated_at: '2026-06-04T05:11:47.547911+00:00'
url_hash: f264f7d6f339b6cf6ae20c102f533b5507b5a5b4
---

A new
[Mini Shai-Hulud](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)
supply chain attack campaign, codenamed
**Miasma**
, has compromised @redhat-cloud-services packages to steal credentials and secrets from developer machines and deliver a self-propagating worm.

"This is effectively a Mini Shai-Hulud campaign: it uses the same core tactics of install-time execution, credential harvesting, CI/CD targeting, encrypted exfiltration, and potential downstream propagation," Socket
[said](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages)
.

Exactly who is behind the attack activity is presently unknown given that TeamPCP (aka Replicating Marauder, TGR-CRI-1135, and UNC6780), an infamous cybercrime group, has open-sourced the attack tools linked to the Shai-Hulud worm, opening the door for other threat actors to pull off similar attacks and making definitive attribution harder.

The names of some of the affected packages are listed below -

* @redhat-cloud-services/vulnerabilities-client
* @redhat-cloud-services/tsc-transform-imports
* @redhat-cloud-services/topological-inventory-client
* @redhat-cloud-services/sources-client
* @redhat-cloud-services/rule-components
* @redhat-cloud-services/remediations-client
* @redhat-cloud-services/rbac-client

Per analyses from
[Aikido Security](https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm)
,
[JFrog](https://research.jfrog.com/post/shai-hulud-miasma-redhat-cloud-services/)
,
[Microsoft](https://x.com/MsftSecIntel/status/2061485730958848188)
,
[OX Security](https://www.ox.security/blog/new-npm-supply-chain-attack-redhat-cloud-services-compromised)
,
[ReversingLabs](https://www.reversinglabs.com/blog/red-hat-cloud-service-npm-packages-backdoored-in-72-seconds)
,
[SafeDep](https://safedep.io/redhat-cloud-services-hit-by-mini-shai-hulud-npm-worm/)
,
[StepSecurity](https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised)
, and
[Wiz](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages)
, the npm packages contain an obfuscated preinstall hook that's designed to collect GitHub Actions secrets, npm tokens, cloud credentials, Kubernetes and Vault material, SSH keys, Git credentials, and other sensitive files.

Like observed in prior Mini Shai-Hulud waves, the malware also contains encrypted exfiltration logic that transmits the data to "api.anthropic[.]com:443/v1/api" and uses GitHub as a fallback mechanism. This indicates attempts made by the attacker to both steal credentials and weaponize them to further poison the software supply chain.

"It commits the encrypted result envelope through the GitHub API," Socket said. "The commit message can include: IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner:&lt;token&gt;."

Another noteworthy step carried out by the malware is to avoid execution on Russian-language systems, a pattern also observed in the
[GlassWorm](https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html)
supply chain campaigns.

"For npm, the payload calls the OIDC token exchange and whoami endpoints, repackages a tarball (updateTarball, package-updated.tgz), and signs the artifact through Sigstore," SafeDep said. "Stolen credentials exfiltrate to attacker-created public GitHub repositories, each carrying the description Miasma: The Spreading Blight."

The first commit containing the "Miasma: The Spreading Blight" string appeared on May 29, 2026, OX Security noted, indicating that either this variant was active since then, or the threat actor started testing around that time.

As for GitHub, the malware enumerates repositories the token can write to, reads action.yml/action.yaml via GraphQL, and commits a workflow through the createCommitOnBranch mutation so that the commit appears as a verified, signed change. Other actions carried out by the malware are listed below -

* Attempt privilege escalation by launching a container that bind-mounts the host /etc/sudoers.d and grants the CI runner passwordless sudo
* Check for endpoint protection from CrowdStrike, SentinelOne, Carbon Black, and StepSecurity Harden-Runner before commencing the malicious actions
* Establish persistence by injecting a SessionStart hook to Anthropic Claude Code and a tasks.json with "runOn": "folderOpen" for Microsoft Visual Studio Code projects so that the malware is automatically launched during every session

"One of the main changes in this new variant is the addition of new data collectors focused on cloud identities," Wiz researchers said. "Specifically, collectors for GCP and Azure identities were added that collect all identities the infected machine has access to. While previous versions of the malware primarily focused on extracting secrets from these environments, this variant suggests an increased attacker focus on gaining and leveraging access to the cloud itself.

Unlike previous versions, the malware has also been found to generate a uniquely encrypted payload for each infection, thereby making detection and version tracking significantly more challenging.

Evidence suggests that the compromise of a Red Hat employee's GitHub account was the patient zero that was used to inject the payload into these packages. The compromised account is said to have pushed malicious orphan commits to two RedHatInsights repositories, bypassing code review.

It's recommended to isolate hosts that have installed the affected versions, remove the malicious versions, rotate exposed credentials, review for any signs of suspicious GitHub or npm activity, audit the environment for persistence artifacts that involve changes to configuration files (~/.claude/settings.json, .vscode/tasks.json, .github/workflows/codeql.yml, .github/setup.js), and enforce strong access controls.

"Because the malware includes background execution and potential developer-tool persistence mechanisms, uninstalling the npm package or deleting node\_modules should not be considered sufficient cleanup," Socket explained.

"For CI/CD systems, suspend affected workflow runs, invalidate build artifacts produced during the exposure window, and review whether any release, container image, npm package, or deployment artifact was created after the malicious package was installed."

### Update

Dark web monitoring and threat intelligence firm Whiteintel
[said](https://whiteintel.io/blog/red-hat-miasma-supply-chain-attack)
it "detected a Red Hat GitHub credential and session cookie in infostealer logs on April 13 and May 15, 2026," raising the possibility that this information may have been used to break into the employee's account.

The development is the latest in a
[number of supply chain attacks](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)
that have targeted the open-source ecosystems over the past couple of months. These attacks have impacted well-known projects, including Aqua Trivy, Checkmarx KICS, Bitwarden, SAP, TanStack, and GitHub, and Nx Console.

Last month, a separate campaign codenamed
[Megalodon](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)
was found to have injected malicious GitHub Action workflows to harvest CI/CD secrets, cloud credentials, and tokens, impacting both development and deployment pipelines in public GitHub repositories.

"These recent incidents, including the GitHub compromise via a malicious Nx Console Visual Studio Code (VS Code) extension and the 'Megalodon' supply chain intrusion campaign, demonstrate how cyber threat actors are abusing tools and processes that support enterprise, cloud, and DevOps environments - specifically CI/CD pipelines, code extensions and workflows," the U.S. Cybersecurity and Infrastructure Security Agency (CISA)
[said](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories)
.