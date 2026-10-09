---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-25T00:00:08.572831+00:00'
exported_at: '2025-11-25T00:00:11.214406+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html
structured_data:
  about: []
  author: ''
  description: Security vendors warn Sha1-Hulud has hijacked 25,000+ GitHub repos
    via npm packages, stealing cloud credentials or wiping dev home directories.
  headline: Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall
    Credential Theft
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/second-sha1-hulud-wave-affects-25000.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Second Sha1-Hulud Wave Affects 25,000+ Repositories via npm Preinstall Credential
  Theft
updated_at: '2025-11-25T00:00:08.572831+00:00'
url_hash: 1a1f24040b09b91c3e5189506468c6bf3f52d66c
---

**

Nov 24, 2025
**

Ravie Lakshmanan

Cloud Security / Vulnerability

Multiple security vendors are sounding the alarm about a second wave of attacks targeting the npm registry in a manner that's reminiscent of the
[Shai-Hulud attack](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html)
.

The new supply chain campaign, dubbed
**Sha1-Hulud**
, has compromised hundreds of npm packages, according to reports from
[Aikido](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains)
,
[HelixGuard](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)
,
[Koi Security](https://www.koi.ai/incident/live-updates-sha1-hulud-the-second-coming-hundred-npm-packages-compromised)
,
[Socket](https://socket.dev/blog/shai-hulud-strikes-again-v2)
,
[Step Security](https://www.stepsecurity.io/blog/sha1-hulud-the-second-coming-zapier-ens-domains-and-other-prominent-npm-packages-compromised)
, and
[Wiz](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack)
. The trojanized npm packages were uploaded to npm between November 21 and 23, 2025.

"The campaign introduces a new variant that executes malicious code during the preinstall phase, significantly increasing potential exposure in build and runtime environments," Wiz researchers Hila Ramati, Merav Bar, Gal Benmocha, and Gili Tikochinski said.

Like the Shai-Hulud attack that came to light in September 2025, the latest activity also publishes stolen secrets to GitHub, this time with the repository description: "Sha1-Hulud: The Second Coming."

The prior wave was characterized by the compromise of legitimate packages to push malicious code designed to search developer machines for secrets using TruffleHog's credential scanner and transmit them to an external server under the attacker's control.

The infected variants also came with the ability to propagate in a self-replicating manner by re-publishing itself into other npm packages owned by the compromised maintainer.

In the latest set of attacks, the attackers have been found to add to a preinstall script ("setup\_bun.js") in the package.json file, which is configured to stealthily install or locate the Bun runtime and run a bundled malicious script ("bun\_environment.js").

The malicious payload carries out the following sequence of actions through two different workflows -

* Registers the infected machine as a self-hosted runner named "SHA1HULUD" and adds a workflow called .github/workflows/discussion.yaml that contains an injection vulnerability and runs specifically on self-hosted runners, allowing the attacker to run arbitrary commands on the infected machines by opening discussions in the GitHub repository
* Exfiltrates all secrets defined in the GitHub secrets section and uploads them as an artifact to a file named "actionsSecrets.json" in the exfiltration repositories, after which it's downloaded to the compromised machine and the workflow is deleted to conceal the activity

"Upon execution, the malware downloads and runs TruffleHog to scan the local machine, stealing sensitive information such as NPM Tokens, AWS/GCP/Azure credentials, and environment variables," Helixuard noted.

Wiz said it spotted over 25,000 affected repositories across about 350 unique users, with 1,000 new repositories being added consistently every 30 minutes in the last couple of hours.

"This campaign continues the trend of npm supply-chain compromises referencing Shai-Hulud naming and tradecraft, though it may involve different actors," Wiz said. "The threat leverages compromised maintainer accounts to publish trojanized versions of legitimate npm packages that execute credential theft and exfiltration code during installation."

Koi Security called the second wave a lot more aggressive, adding that the malware attempts to destroy the victim's entire home directory if it fails to authenticate or establish persistence. This includes every writable file owned by the current user under their home folder. However, this wiper-like functionality is triggered only when the following conditions are satisfied -

* It cannot authenticate to GitHub
* It cannot create a GitHub repository
* It cannot fetch a GitHub token
* It cannot find an npm token

"In other words, if Sha1-Hulud is unable to steal credentials, obtain tokens, or secure any exfiltration channel, it defaults to catastrophic data destruction," security researchers Yuval Ronen and Idan Dardikman said. "This marks a significant escalation from the first wave, shifting the actor's tactics from purely data-theft to punitive sabotage."

The malware has also been found to obtain root privileges by executing a Docker command that mounts the host's root filesystem into a privileged container with the goal of copying a malicious sudoers file, granting the attacker passwordless root access to the compromised user.

To mitigate the risk posed by the threat, organizations are being urged to scan all endpoints for the presence of impacted packages, remove compromised versions with immediate effect, rotate all credentials, and audit repositories for persistence mechanisms by reviewing .github/workflows/ for suspicious files such as shai-hulud-workflow.yml or unexpected branches.

*(This is a developing story and will be updated as new details emerge.)*