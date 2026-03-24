---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-24T04:44:17.097296+00:00'
exported_at: '2026-03-24T04:44:19.786583+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html
structured_data:
  about: []
  author: ''
  description: CanisterWorm infects 28 npm packages via ICP-based C2, enabling self-propagation
    and persistent backdoor access across developer systems.
  headline: Trivy Supply Chain Attack Triggers Self-Spreading CanisterWorm Across
    47 npm Packages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trivy Supply Chain Attack Triggers Self-Spreading CanisterWorm Across 47 npm
  Packages
updated_at: '2026-03-24T04:44:17.097296+00:00'
url_hash: 32b29a0e4deba466b91cfe311c13d8b8b96f266d
---

The threat actors behind the
[supply chain attack](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html)
targeting the popular Trivy scanner are suspected to be conducting follow-on attacks that have led to the compromise of a large number of npm packages with a previously undocumented self-propagating worm dubbed
**CanisterWorm**
.

The name is a reference to the fact that the malware uses an
[ICP canister](https://docs.internetcomputer.org/building-apps/essentials/canisters)
, which denotes a tamperproof smart contract on the Internet Computer blockchain, as a
[dead drop resolver](https://attack.mitre.org/techniques/T1102/001/)
. The development marks the first publicly documented abuse of an ICP canister for the explicit purpose of fetching the command-and-control (C2) server, Aikido Security researcher Charlie Eriksen
[said](https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise)
.

The list of affected packages is below -

* 28 packages in the @EmilGroup scope
* 16 packages in the @opengov scope
* @teale.io/eslint-config
* @airtm/uuid-base32
* @pypestream/floating-ui-dom

The development comes within a day after threat actors leveraged a compromised credential to publish malicious trivy, trivy-action, and setup-trivy releases containing a credential stealer. A cloud-focused
[cybercriminal operation](https://cyble.com/threat-actor-profiles/teampcp/)
known as
[TeamPCP](https://thehackernews.com/2026/02/teampcp-worm-exploits-cloud.html)
is suspected to be behind the attacks.

The infection chain involving the npm packages involves leveraging a postinstall hook to execute a loader, which then drops a Python backdoor that's responsible for contacting the ICP canister dead drop to retrieve a URL pointing to the next-stage payload. The fact that the dead drop infrastructure is decentralized makes it
[resilient and resistant to takedown efforts](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)
.

"The canister controller can swap the URL at any time, pushing new binaries to all infected hosts without touching the implant," Eriksen said.

Persistence is established by means of a systemd user service, which is configured to automatically start the Python backdoor after a 5-second delay if it gets terminated for some reason by using the "
[Restart=always](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
" directive. The systemd service masquerades as PostgreSQL tooling ("pgmon") in an attempt to fly under the radar.

The backdoor, as mentioned before, phones the
[ICP canister](https://dashboard.internetcomputer.org/canister/tdtqy-oyaaa-aaaae-af2dq-cai)
with a spoofed browser User-Agent every 50 minutes to fetch the URL in plaintext. The URL is subsequently parsed to fetch and run the executable.

"If the URL contains youtube[.]com, the script skips it," Eriksen explained. "This is the canister's dormant state. The attacker arms the implant by pointing the canister at a real binary, and disarms it by switching back to a YouTube link. If the attacker updates the canister to point to a new URL, every infected machine picks up the new binary on its next poll. The old binary keeps running in the background since the script never kills previous processes."

It's worth noting that a similar youtube[.]com-based kill switch has also been flagged by Wiz in connection with the trojanized Trivy binary (version 0.69.4), which reaches out to the same ICP canister via another Python dropper ("sysmon.py"). As of writing, the URL returned by the C2 is a
[rickroll YouTube video](https://en.wikipedia.org/wiki/Rickrolling)
.

The Hacker News found that the ICP canister
[supports](https://dashboard.internetcomputer.org/canister/tdtqy-oyaaa-aaaae-af2dq-cai)
three methods – get\_latest\_link, http\_request, update\_link – the last of which allows the threat actor to modify the behavior at any time to serve an actual payload.

In tandem, the packages come with a "deploy.js" file that the attacker runs manually to spread the malicious payload to every package a stolen npm token provides access to in a programmatic fashion. The worm, assessed to be vibe-coded using an artificial intelligence (AI) tool, makes no attempt to conceal its functionality.

"This isn't triggered by npm install," Aikido said. "It's a standalone tool the attacker runs with stolen tokens to maximize blast radius."

To make matters worse, a subsequent mutation of CanisterWorm detected in "@teale.io/eslint-config" versions 1.8.11 and 1.8.12 has been found to steal npm tokens and use them to self-propagate on its own without the need for manual intervention.

Unlike "deploy.js," which was a self-contained script the attacker had to execute with the pilfered npm tokens to push a malicious version of the npm packages to the registry, the new variant incorporates this functionality in "index.js" within a findNpmTokens() function that's run during the postinstall phase to collect npm authentication tokens from the victim's machine.

The main difference here is that the postinstall script, after installing the persistent backdoor, attempts to locate every npm token from the developer's environment and spawns the worm right away with those tokens by launching "deploy.js" as a fully detached background process.

Interestingly, the threat actor is said to have swapped out the ICP backdoor payload for a dummy test string ("hello123"), likely to ensure that the entire attack chain is working as intended before adding the malware.

"This is the point where the attack goes from 'compromised account publishes malware' to 'malware compromises more accounts and publishes itself,'" Eriksen said. "Every developer or CI pipeline that installs this package and has an npm token accessible becomes an unwitting propagation vector. Their packages get infected, their downstream users install those, and if any of them have tokens, the cycle repeats."

### Update

Software supply chain security company Socket said the
[CanisterWorm](https://socket.dev/supply-chain-attacks/canisterworm)
supply chain attack has expanded to 141 malicious package artifacts spanning more than 66 unique packages.

"In the observed activity, the threat actor appears to have obtained one or more npm publishing tokens, or equivalent CI/CD publishing access, and used that access to replace legitimate package contents with malicious code, then republish the payload across additional packages reachable by the compromised credentials," the company
[said](https://socket.dev/blog/canisterworm-npm-publisher-compromise-deploys-backdoor-across-29-packages)
.

Additional analyses into CanisterWorm have been published by
[Endor Labs](https://www.endorlabs.com/learn/canisterworm)
and
[JFrog](https://research.jfrog.com/post/canister-worm/)
, with the malware characterized as both a credential harvester and a malware dropper that searches for npm authentication tokens by scanning the developer machine and then passing the harvested tokens to a secondary script ("deploy.js"), which acts as a worm to propane the malicious logic across the victim's software portfolio.

"While credential harvesting via postinstall hooks is a well-established tactic,
[Shai-Hulud](https://thehackernews.com/2026/02/malicious-npm-packages-harvest-crypto.html)
proved that stolen npm tokens could be immediately weaponized to infect and republish a victim's own packages, turning a single compromise into an exponentially expanding attack," Henrik Plate, head of security research at Endor Labs, said. "The campaign analyzed here follows the same playbook, confirming that worm-like self-propagation has become a recurring technique rather than an isolated incident."