---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T20:56:15.386157+00:00'
exported_at: '2026-05-14T20:56:18.225754+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
structured_data:
  about: []
  author: ''
  description: TeamPCP’s Mini Shai-Hulud campaign used hijacked GitHub OIDC tokens
    to spread a credential-stealing worm through TanStack npm packages.
  headline: Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI &
    More Packages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI & More
  Packages
updated_at: '2026-05-14T20:56:15.386157+00:00'
url_hash: 06dd92f800722c8f03ae618721bb5a37e98c00ca
---

**TeamPCP**
, the threat actor behind the recentsupply chain attack spree, has been linked to the compromise of the npm and PyPI packages from TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI as part of a fresh Mini Shai-Hulud campaign.

The affected npm packages have been modified to include an obfuscated JavaScript file ("router\_init.js") that's designed to profile the execution environment and launch a comprehensive credential stealer capable of targeting cloud providers, cryptocurrency wallets, AI tools, messaging apps, and CI systems, including Github Actions, multiple reports from
[Aikido Security](https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised)
,
[Endor Labs](https://www.endorlabs.com/learn/shai-hulud-compromises-the-tanstack-ecosystem-80-packages-compromised)
,
[SafeDep](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)
,
[Socket](https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack)
,
[StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
, and
[Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
show. The data is exfiltrated to the "filev2.getsession[.]org" domain.

Using Session Protocol infrastructure is a deliberate attempt on the part of the attackers to evade detection, as the domain is unlikely to be blocked within enterprise environments, given that it belongs to a decentralized, privacy-focused messaging service. As a fallback option, the encrypted data is committed to attacker-controlled repositories under the author name "claude@users.noreply.github.com" via the GitHub GraphQL API using the stolen GitHub tokens.

The malware is also capable of establishing persistence hooks in Claude Code and Microsoft Visual Studio Code (VS Code) to survive reboots and re-execute the stealer on every launch of the IDEs.

Furthermore, it installs a gh-token-monitor service to monitor and re-exfiltrate GitHub tokens, and injects two malicious GitHub Actions workflows to serialize repository secrets into a JSON object and upload the data to an external server ("api.masscan[.]cloud").

Unlike the
[previous SAP wave](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html)
, where the compromised packages added a preinstall hook to trigger the infection sequence, the latest TanStack cluster adopts a different strategy by including a JavaScript file within the package tarball and adding an optional dependency that points to a GitHub-hosted package. The GitHub dependency contains a prepare lifecycle hook that executes the JavaScript payload via the Bun runtime.

The updates to the Mistral AI packages, on the other hand, follow the earlier approach, replacing the contents of the "package.json" file with a preinstall hook to invoke "node setup.mjs," which downloads Bun and runs the same JavaScript malware.

The TanStack supply chain compromise has been assigned the CVE identifier
[CVE-2026-45321](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)
. It carries a CVSS score of 9.6 out of a maximum of 10.0, indicating critical severity. The incident has impacted 42 packages and 84 versions across the TanStack ecosystem.

TanStack has since
[traced](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
the compromise to a chained GitHub Actions attack involving the "pull\_request\_target" trigger,
[GitHub Actions cache poisoning](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/)
, and runtime memory extraction of an OIDC token from the GitHub Actions runner process. "No npm tokens were stolen, and the npm publish workflow itself was not compromised," TanStack said.

Specifically, the attackers are assessed to have staged the malicious payload in a GitHub fork via an orphaned commit, injected it into published npm tarballs, then hijacked the project's legitimate "TanStack/router" workflow to publish the compromised versions with valid SLSA provenance.

"The attack published malicious versions through the project's own GitHub Actions release pipeline using hijacked OIDC tokens," StepSecurity researcher Ashish Kurmi said.

"In an extremely rare escalation, the compromised packages carry valid SLSA Build Level 3 provenance attestations, making this the first documented npm worm that produces validly attested malicious packages. The worm has since spread beyond TanStack to packages from UiPath, DraftLab, and other maintainers."

The attack is noteworthy for the fact that it abuses trusted publishing, allowing attacker-controlled code running within a workflow to leverage its OIDC permissions to "mint" a short-lived publish token during the build and use it to publish the packages without having to steal an npm token.

What makes the worm stand out is its ability to spread itself to other packages by locating a publishable npm token with bypass\_2fa set to true, enumerating every package published by the same maintainer, and exchanging a GitHub OIDC token for a per-package publish token to sidestep traditional authentication entirely.

"The orphaned commit additionally triggered a GitHub Actions workflow run against the legitimate TanStack/router workflow surface," Endor Labs researcher Peyton Kennedy said. "Because the repository's OIDC trusted publisher configuration granted trust at the repository level rather than scoped to a specific protected branch and workflow file, the workflow run triggered by that commit was able to request a valid short-lived npm publish token."

Another new behavior
[introduced](https://github.com/TanStack/router/issues/7383#issuecomment-4425225340)
in the obfuscated JavaScript malware is the installation of a dead-man's switch that uses a shell script to periodically check if an npm token created by the malware is not revoked by polling the "api.github.com/user" endpoint every 60 seconds. The token has the description "IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner."

Should the developer revoke the token from their npm dashboard, the script triggers a destructive routine that executes "rm -rf ~/" on the infected machine, essentially turning it into a wiper malware. These changes indicate that TeamPCP is growing aggressive and evolving its tradecraft with every campaign. It's therefore essential that developers do not revoke the npm tokens before isolating and imaging the system.

"This campaign reflects a broader shift in supply chain attacks from isolated package compromise to identity-driven propagation through trusted CI/CD infrastructure," Avital Harel, security research lead at Upwind,
[said](https://www.upwind.io/feed/shai-hulud-tanstack-supply-chain-worm)
in a statement shared with The Hacker News.

"Once attackers gain access to publishing workflows and pipeline identities, the software delivery process itself becomes the distribution mechanism. The challenge for defenders is that much of this activity can appear legitimate on the surface, which makes behavioral visibility during installs and builds increasingly important."

Besides TanStack, the Mini Shai-Hulud campaign has also spread to several other packages, including some in PyPI -

* guardrails-ai@0.10.1 (PyPI)
* mistralai@2.4.6 (PyPI)
* @opensearch-project/opensearch@3.5.3, 3.6.2, 3.7.0, and 3.8.0
* @squawk/mcp@0.9.5
* @squawk/weather@0.5.10
* @squawk/flightplan@0.5.6
* @tallyui/connector-medusa@1.0.1, 1.0.2, and 1.0.3
* @tallyui/connector-vendure@1.0.1, 1.0.2, and 1.0.3

According to
[data from OX Security](https://www.ox.security/blog/shai-hulud-here-we-go-again-170-packages-hit-across-npm-pypi/)
, the incident has affected over 170 packages spanning both the npm and PyPI registries. The packages have more than 518 million downloads cumulatively. No less than
[400 repositories](https://github.com/search?q=%22Shai-Hulud%3A%20Here%20We%20Go%20Again%22&type=repositories)
with stolen credentials have been created as part of the attack wave. All the repositories contain the string "Shai-Hulud: Here We Go Again."

Google-owned Wiz
[said](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)
the payload also exfiltrates stolen credentials via a third redundant channel, a typosquat domain named "git-tanstack[.]com," along with the Session messenger network and GitHub API dead drops using the stolen token, adding the trojanized PyPI packages associated with both Mistral AI and Guardrails AI contain the same malware, which "operates notably differently" from the JavaScript versions distributed via npm.

Microsoft, in its
[analysis](https://x.com/MsftSecIntel/status/2054041471280423424)
of the malicious mistralai PyPI package, said it's designed to download a credential stealer from a remote server ("83.142.209[.]194") that includes country-aware logic to avoid Russian-language environments and a "geofenced destructive branch that has a 1-in-6 chance of executing rm -rf / when the system appears to be in Israel or Iran."

Mistral AI has published two advisories related to the compromise of its
[npm](https://github.com/mistralai/client-ts/security/advisories/GHSA-jgg6-4rpr-wfh7)
and
[PyPI](https://github.com/mistralai/client-python/security/advisories/GHSA-wx9m-wx4f-4cmg)
packages, confirming that it was impacted by a supply chain attack related to the TanStack security incident. "Current investigation indicates that an affected developer device was involved," it
[said](https://docs.mistral.ai/resources/security-advisories)
.

"The guardrails-ai@0.10.1 compromise is especially notable because the malicious code executes on import," Socket said. "The package checks for Linux systems, downloads a remote Python artifact from https://git-tanstack.com/transformers.pyz, writes it to /tmp/transformers.pyz, and executes it with python3 without integrity verification."

"This latest activity shows the campaign continuing to propagate across both npm and PyPI, with affected packages spanning search infrastructure, AI tooling, aviation-related developer packages, enterprise automation, frontend tooling, and CI/CD-adjacent ecosystems."

*(The story was updated after publication to include additional insights.)*