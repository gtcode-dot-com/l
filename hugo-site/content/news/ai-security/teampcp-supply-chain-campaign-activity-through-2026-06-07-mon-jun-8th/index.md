---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T19:25:35.226858+00:00'
exported_at: '2026-06-10T19:25:38.907437+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33060
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Activity Through 2026-06-07, Author:
    Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Activity Through 2026-06-07, (Mon, Jun
    8th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33060
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Activity Through 2026-06-07, (Mon, Jun 8th)'
updated_at: '2026-06-10T19:25:35.226858+00:00'
url_hash: 84e3e154d6ea6eedf23d3a45c50d883e5f6aa8c4
---

This diary continues the Internet Storm Center's tracking of the TeamPCP supply chain campaign, first documented in the SANS white paper
[When the Security Scanner Became the Weapon](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
and most recently in the handler diary
[Activity Through 2026-05-24](https://isc.sans.edu/diary/33014)
. Since that update, the story moved into two new places: the United States government, which formally caught up to the campaign, and the wider population of attackers now wielding the Mini Shai-Hulud framework that TeamPCP open-sourced last month.

## Bottom line up front

Two developments stand out since the last update. First, the federal response that prior coverage flagged as conspicuously absent arrived in a roughly 48-hour burst: on 2026-05-27 CISA added the campaign's primary tracking vulnerabilities to its Known Exploited Vulnerabilities catalog, and on 2026-05-28 it issued its first standalone advisory naming the Nx Console and GitHub repository compromises. Second, the leaked Mini Shai-Hulud framework produced its first significant in-the-wild npm wave: beginning 2026-06-01, a credential-stealing worm that Wiz named "Miasma" compromised dozens of @redhat-cloud-services packages, followed two days later by a "Phantom Gyp" variant that reached 57 more. Vendors trace the malware to the TeamPCP lineage but now explicitly caution that a copycat using the public toolkit cannot be ruled out. The affiliated extortion channels stayed frozen, so this period's activity was ecosystem-scale worming rather than named-victim extortion.

## How this developed

The last update closed with two open questions: whether CISA would act on a campaign it had so far left out of the KEV catalog, and whether the framework TeamPCP published to GitHub would produce copycat attacks. Both resolved in the affirmative. CISA's KEV addition and standalone advisory closed the government-silence gap within roughly a day of each other. A week later, the Red Hat npm compromise demonstrated that the open-sourced code is now operational in other hands. The throughline is that the campaign has entered a phase where its tradecraft outlives any single operator: the same techniques, subverted build pipelines that emit validly signed artifacts and install-time credential theft, now arrive from attackers who may have no direct connection to TeamPCP at all.

## What changed, by theme

### CISA formally caught up

On 2026-05-27, CISA added
[three vulnerabilities to the KEV catalog](https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog)
, including
[CVE-2026-45321](/vuln.html?cve=2026-45321)
(the TanStack / Mini Shai-Hulud tracking identifier) and
[CVE-2026-48027](/vuln.html?cve=2026-48027)
(the malicious code embedded in the Nx Console v18.95.0 build), both carrying a federal remediation due date of 2026-06-10, alongside
[CVE-2026-8398](/vuln.html?cve=2026-8398)
(DAEMON Tools Lite). This resolved the multi-week KEV omission that earlier coverage tracked as an open question. The additions were corroborated by
[SC Media](https://www.scworld.com/brief/cisa-adds-daemon-tools-tanstack-and-nx-console-flaws-to-known-exploited-vulnerabilities-catalog)
and
[Security Affairs](https://securityaffairs.com/192776/security/u-s-cisa-adds-daemon-tools-tanstack-and-nx-console-flaws-to-its-known-exploited-vulnerabilities-catalog.html)
.

The next day, 2026-05-28, CISA published its first standalone advisory on the campaign,
[Supply Chain Compromises Impact Nx Console and GitHub Repositories](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories)
. The advisory documents the poisoned Nx Console VS Code extension auto-distributed through the editor update mechanism, the exfiltration of approximately 3,800 GitHub-internal repositories, the assignment of
[CVE-2026-48027](/vuln.html?cve=2026-48027)
, and a separate "Megalodon" campaign that injected malicious GitHub Actions workflows to harvest CI/CD secrets and cloud credentials in public repositories. CISA urges forensic review of CI/CD logs and cloud audit trails and rotation of all CI/CD-accessible secrets.
[TechRadar Pro](https://www.techradar.com/pro/security/cisa-warns-that-nx-console-and-github-repositories-abused-in-multiple-supply-chain-compromises-tools-across-enterprise-cloud-and-devops-environments-exploited)
and
[Cybersecurity Dive](https://www.cybersecuritydive.com/news/cisa-security-software-supply-chain-compromises-GitHub/821487/)
carried the advisory to a wider audience.

### The leaked framework produced its first major wave: Red Hat npm

On 2026-06-01, a supply chain attack that Wiz named
["Miasma"](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages)
compromised at least 32 packages (across roughly 90 or more versions) published under the @redhat-cloud-services npm scope, with the affected packages cumulatively averaging about 80,000 weekly downloads. The attacker used a compromised Red Hat employee GitHub account to inject malicious GitHub Actions workflows into RedHatInsights repositories, so the malicious releases carried valid SLSA provenance attestations: the pipeline genuinely ran Red Hat code that contained attacker-injected steps. The payload was a credential-stealing worm with a preinstall script and new cloud-identity collectors for GCP and Azure, and the obfuscated index.js grew from roughly 200 KB to about 4.29 MB. Corroborated by
[BleepingComputer](https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/)
and
[Cybersecurity Dive](https://www.cybersecuritydive.com/news/dozens-red-hat-npm-packages-supply-chain-attack/821723/)
.

[Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/)
published its analysis on 2026-06-02, confirming the 32 packages across more than 90 versions and characterizing the payload as a lightly reskinned descendant of the Mini Shai-Hulud worm.
[Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)
folded the compromise into its running npm tracker the same day.

### Install-time tradecraft advanced within days: Phantom Gyp

On 2026-06-03, a follow-on variant that StepSecurity named "Phantom Gyp" compromised 57 additional packages across 286 or more malicious versions in under two hours. Rather than modifying the package.json scripts field, the variant weaponized binding.gyp files to trigger node-gyp execution at install time, evading monitors that watch only package.json. The largest named victim was @vapi-ai/server-sdk, the official server SDK for the
[Vapi.ai](http://Vapi.ai)
voice platform, with over 408,000 monthly downloads. See
[TechTimes](https://www.techtimes.com/articles/317832/20260605/red-hat-npm-packages-compromised-57-more-follow-signed-attestations-cannot-block-pipeline-hijack.htm)
, corroborated by Wiz and
[Protos Labs](https://www.protoslabs.io/resources/teampcp-shai-hulud-megalodon-supply-chain-jun-2026)
.

### Attribution is now genuinely ambiguous

Wiz, Microsoft, and Unit 42 all describe the Red Hat payload as Mini Shai-Hulud derived while explicitly warning that a copycat leveraging the public toolkit cannot be excluded. Wiz states the similarities should be treated as evidence of TTP overlap rather than definitive attribution to TeamPCP. This is the practical materialization of the copycat risk flagged when TeamPCP open-sourced its framework: the defender takeaway is unchanged, but single-incident attribution to the operators is now weaker than it was during the operator-run phase earlier in the campaign.

### Signed provenance still does not save you

As with the earlier TanStack incident, the Red Hat packages shipped valid provenance attestations because the build pipeline itself was subverted from within. Trade reporting this period foregrounded the point that signed attestations cannot block a pipeline hijack. Build-provenance attestation confirms that an artifact came from a given pipeline; it does not confirm that the pipeline was free of attacker-injected steps.

### Monetization stayed frozen

The affiliated extortion channels posted nothing in this period. Per direct checks of
[ransomware.live](https://www.ransomware.live/group/vect)
, the Vect leak site remained at 25 victims with its most recent listing dated 2026-04-15, and
[CipherForce](https://www.ransomware.live/group/cipherforce)
remained at 6 victims with last activity dated 2026-02-23. The contrast from earlier in the campaign holds: the supply chain operation draws government and vendor attention while the affiliate-ransomware channel remains dormant.

## What defenders should do now

* Treat the 2026-06-10 CISA remediation deadline for
  [CVE-2026-45321](/vuln.html?cve=2026-45321)
  and
  [CVE-2026-48027](/vuln.html?cve=2026-48027)
  as binding. Confirm no exposed Nx Console v18.95.0 install remains and that TanStack-related exposure is remediated.
* Rotate all CI/CD-accessible secrets and cloud credentials, and review CI/CD logs and cloud audit trails, per the CISA advisory. Assume any token reachable from a build pipeline is potentially exposed.
* Inventory use of the affected scopes (@redhat-cloud-services, and the earlier @antv) and packages such as @vapi-ai/server-sdk. Pin to known-good versions and rebuild from a trusted state.
* Monitor install-time execution beyond the package.json scripts field. Include binding.gyp and node-gyp hooks in detection, since Phantom Gyp moved specifically to evade scripts-only monitors. Consider running install with scripts disabled in CI where feasible.
* Do not rely on SLSA provenance attestations alone. Valid provenance does not defend against a compromised build environment; pair it with build-environment integrity controls and behavioral monitoring of install steps.
* Enforce two-factor authentication on registry maintainer accounts, scope publish tokens narrowly, and alert on anomalous workflow changes in source repositories.

## Watch items

* A formal Red Hat post-incident statement and a definitive package and version inventory, including confirmation of the compromised employee-account vector and any downstream notification to consumers.
* Convergence or divergence on attribution. Watch for whether Mandiant or the Google Threat Intelligence Group issues a dedicated note either claiming the Miasma and Phantom Gyp waves as UNC6780 or designating a separate copycat cluster.
* Further binding.gyp and node-gyp install-time abuse beyond the @redhat-cloud-services scope, and whether registry-side or scanner-side detection adapts to install hooks outside package.json.
* The CISA KEV remediation deadline of 2026-06-10. Watch for deadline-driven follow-on guidance, KEV additions covering the Red Hat activity, or disclosure of federal-agency exposure as the date passes.
* Resumption of named-victim extortion. Watch the Vect and CipherForce leak sites for any end to their multi-month dormancy, which would signal a shift back from ecosystem worming to monetization.