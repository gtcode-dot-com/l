---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-15T17:19:51.975703+00:00'
exported_at: '2026-05-15T17:19:53.927776+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
structured_data:
  about: []
  author: ''
  description: Mini Shai-Hulud hit 2 OpenAI devices via TanStack, exposing limited
    credentials and forcing macOS certificate updates by June 12, 2026.
  headline: TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces
    macOS Updates
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces macOS
  Updates
updated_at: '2026-05-15T17:19:51.975703+00:00'
url_hash: a90e59666c1ba544143b327d717ee576f89e8953
---

OpenAI has disclosed that two of its employee devices in its corporate environment were impacted via the
[Mini Shai-Hulud supply chain attack](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
on TanStack, but noted that no user data, production systems, or intellectual property were compromised or modified in an unauthorized manner.

"Upon identification of the malicious activity, we worked quickly to investigate, contain, and take steps to protect our systems," OpenAI
[said](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/)
. "We observed activity consistent with the malware's publicly described behavior, including unauthorized access and credential-focused exfiltration activity, in a limited subset of internal source code repositories to which the two impacted employees had access."

The artificial intelligence (AI) upstart said only limited credential material was successfully transferred from these code repositories, adding no other information or code was impacted.

Upon being alerted of the activity, OpenAI said it isolated impacted systems and identities, revoked user sessions, rotated all credentials across impacted repositories, temporarily restricted code-deployment workflows, and audited user and credential behavior.

Since the impacted repositories included signing certificates for iOS, macOS, and Windows products, the company has taken the step of revoking the certificates and issuing new ones. As a result, macOS users of ChatGPT Desktop, Codex App, Codex CLI, and Atlas are required to update their apps to the latest versions.

"This helps prevent any risk, however unlikely, of someone attempting to distribute a fake app that appears to be from OpenAI," OpenAI said. "Users do not need to take any action for Windows and iOS apps."

The certificates are scheduled to be revoked on June 12, 2026, after which new downloads and launches of apps signed with the previous certificate will be blocked by built-in macOS protections. Users are therefore advised to apply the updates before the cut-off date for optimal protection.

This is the second time OpenAI has rotated its code-signing certificates for its macOS in as many months. Around mid-April 2026, it
[rotated](https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html)
the certificates after a GitHub Actions workflow used to sign its macOS apps led to the download of the malicious Axios library on March 31, which was compromised by a North Korean hacking group called UNC1069.

"This incident reflects a broader shift in the threat landscape: attackers are increasingly targeting shared software dependencies and development tooling rather than any single company," OpenAI said.

"Modern software is built on a deeply interconnected ecosystem of open-source libraries, package managers, and continuous integration and continuous deployment infrastructure, which means that a vulnerability introduced upstream can propagate widely and quickly across organizations."

The development comes close on the heels of TeamPCP claiming a number of fresh victims, compromising hundreds of packages associated with TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI as part of an ongoing supply chain attack campaign designed to push malware to downstream developers and steal credentials from their systems to further extend the scale of the breaches.

"Just to be clear, no maintainer was phished, had a password leak, or a token stolen from their account," TanStack
[said](https://tanstack.com/blog/incident-followup)
. "The attacker managed to engineer a path where our own CI pipeline stole its own publish token for them, at the exact moment it was created, by way of a cache that everyone in the chain implicitly trusted. It is a sophisticated approach that we hadn't anticipated and that we're taking very seriously."

TeamPCP has since
[announced](https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html#supply-chain-contest)
a supply chain attack contest in partnership with Breached cybercrime, offering participants with a $1,000 in Monero to compromise open-source packages using the Shai-Hulud worm that it has made freely available to others. The hacking group has also threatened to leak about 5GB of internal source code from Mistral AI, asking for $25,000 BIN from prospective buyers.

"We are looking for $25k BIN or they can pay this and we will shred these permanently, only selling to the best offer and limited to one person, if we cannot find a buyer within a week we will leak all of these for free to the forums," TeamPCP
[said](https://x.com/H4ckmanac/status/2054671490210009307)
in the post.

In an updated advisory, Mistral AI
[confirmed](https://docs.mistral.ai/resources/security-advisories)
it was impacted by a supply chain attack caused by the compromise of TanStac, leading to the release of trojanized versions of its npm and PyPI SDKs. It also said a lone developer device was impacted in the hack. There is no evidence to suggest its infrastructure was breached.

A deeper analysis of the modular Python toolkit delivered to Linux systems via the guardrails-ai and mistralai packages has uncovered that the primary command-and-control (C2) server address ("83.142.209[.]194") is hard-coded. In case the primary C2 becomes unreachable, a fallback mechanism called FIRESCALE is activated.

"When the primary C2 is unavailable, the malware searches all public GitHub commit messages worldwide for a signed alternative server URL, verified against an embedded 4096-bit RSA key," Hunt.io
[said](https://hunt.io/blog/teampcp-python-toolkit-firescale-github-c2-takedown)
. "Exfiltration follows three paths in sequence: primary C2 server, FIRESCALE dead-drop redirect, and the victim's own GitHub repository. Blocking any single tier leaves the other two intact."

The cybersecurity company also revealed that the collection module responsible for harvesting Amazon Web Services (AWS) credentials covers all
[19 availability zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)
in its target list, including us-gov-east-1 (AWS GovCloud - US-East) and us-gov-west-1 (AWS GovCloud - US-West), which are restricted to U.S. government agencies and defense contractors.

Another unusual aspect of the campaign is the destructive behavior attached to it. On machines geolocated to Israel or Iran, a 1-in-6 probability gate activates audio playback at maximum volume, followed by the deletion of all accessible files. The malware exists on systems with a Russian locale.

The destructive actions targeting specific geographic regions mirror the "kamikaze" wiper that was unleashed by TeamPCP on Iran-based Kubernetes clusters in connection with a prior supply chain attack distributing a self-propagating worm known as
[CanisterWorm](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html)
. These recurring behaviours point to a more intentional operation rather than something opportunistic.

"The toolkit is more capable, more resilient, and more sophisticated," Hunt.io said. "Beyond credential files, the malware captures every environment variable on the machine, reads all SSH keys and config, walks the entire home directory for dotenv files, and pulls credentials from running Docker containers."