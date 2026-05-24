---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-24T00:02:02.227043+00:00'
exported_at: '2026-05-24T00:02:03.671492+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32994
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Activity Through 2026-05-17, Author:
    Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Activity Through 2026-05-17, (Mon, May
    18th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32994
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Activity Through 2026-05-17, (Mon, May 18th)'
updated_at: '2026-05-24T00:02:02.227043+00:00'
url_hash: 36a8181118f4a68ebe6baa13d5dd0f9f330961bd
---

Since the
[last update](https://isc.sans.edu/diary/32950)
, the TeamPCP supply chain campaign produced its loudest stretch since the March Trivy disclosure: an officially confirmed Checkmarx Jenkins plugin compromise and a new self-spreading Mini Shai-Hulud worm across npm and PyPI.

## Bottom line up front

Two TeamPCP events broke within 48 hours of each other and doubled attention on the campaign. Checkmarx confirmed its Jenkins AST plugin was trojanized, its third compromise in three months, validating an earlier single-researcher claim. In parallel, a new Mini Shai-Hulud worm poisoned roughly 170 npm and PyPI packages (42 @tanstack packages in about six minutes, downloads above 500 million) and was the first documented npm malware shipping with valid SLSA Build Level 3 provenance, plus a 1-in-6 disk-wipe payload on Israeli and Iranian locale hosts. NHS England issued the campaign's first government alert; CISA stayed silent. Action: audit CI for the indicators below, stop trusting provenance alone, pin and lockfile-verify dependencies.

## How this developed

The period opened quiet and derivative: the lead story was
[PCPJack](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/)
, a rival worm that evicts TeamPCP before stealing credentials, alongside a single-researcher claim that a Checkmarx Jenkins plugin had been backdoored. Days later it turned loud: Checkmarx officially confirmed that exact Jenkins compromise, and a new Mini Shai-Hulud worm hit the npm and PyPI ecosystems hard. The through-line is escalation: an unconfirmed rumor became a confirmed incident, and the campaign moved from a quiet competitor-eviction story to a high-impact, signed-malware supply chain wave.

## What changed, by theme

### Checkmarx Jenkins plugin: an unconfirmed claim, then official confirmation

**Takeaway: a single-researcher claim, explicitly logged as unconfirmed at the time, was confirmed by Checkmarx four days later.**

On 2026-05-09, researcher Berk Albayrak
[reported on X](https://x.com/brkalbyrk7/status/2053175077194117590)
that the Checkmarx Jenkins AST scanner plugin had been backdoored. No Tier 1 outlet, no vendor, and no Checkmarx statement corroborated it at the time, so it was carried as information-only pending confirmation. On 2026-05-11 Checkmarx published an
[official update](https://checkmarx.com/blog/ongoing-security-updates/)
acknowledging that a tampered plugin (version 2026.5.09) had been published to the Jenkins Marketplace, with an exposure window of 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC.
[The Register](https://www.theregister.com/devops/2026/05/11/checkmarx-tackles-another-teampcp-intrusion-as-jenkins-plugin-sabotaged/5237780)
,
[BleepingComputer](https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/)
,
[SecurityWeek](https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/)
, and
[The Hacker News](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html)
carried it the same day. This is the third TeamPCP compromise of Checkmarx in three months, and the malicious plugin was installed by several hundred Jenkins controllers. Last known-good build: 2.0.13-829.vc72453fa\_1c16 (2025-12-17). Remediated builds (both 2026-05-09): 2.0.13-848.v76e89de8a\_053 and 2.0.13-847.v08c0072b\_2fd5.

### The Mini Shai-Hulud TanStack wave

**Takeaway: a self-spreading worm poisoned roughly 170 npm and PyPI packages, and the publishes came from TanStack's own trusted release pipeline.**

Starting 2026-05-11 at 19:20 UTC, the worm published 84 malicious artifacts across 42 @tanstack npm packages in about six minutes, including @tanstack/react-router (roughly 12 million weekly downloads). It then propagated to Mistral AI, UiPath, OpenSearch, Guardrails AI, and roughly 170 packages across npm and PyPI, with combined cumulative downloads above 500 million. Primary technical disclosures came from
[Wiz](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)
and
[StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
, with
[Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
and
[BleepingComputer](https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/)
adding scope and counts. The tracking identifier is
[CVE-2026-45321](/vuln.html?cve=2026-45321)
(CVSS 9.6 per The Hacker News; advisory GHSA-g7cv-rxg3-hmpx per Snyk; Wiz and StepSecurity did not assign a CVE). A reported operator error matters for defenders: per Wiz's 2026-05-13 update, the credential stealer is non-functional in the @uipath and @mistralai variants because the payload is reassembled incorrectly there, which limits the harvest from the largest non-TanStack targets.

### Signed malware: the SLSA Build Level 3 first

**Takeaway: this is the first documented npm supply chain attack shipping malware with valid SLSA Build Level 3 provenance, so "has provenance" no longer means "not malicious."**

Per Wiz, StepSecurity, and Snyk, the malicious versions carried valid SLSA Build Level 3 provenance attestations. Analysts assess this is novel and material: the attacker never stole maintainer npm credentials. Instead the malicious versions were published by TanStack's legitimate release pipeline using its own trusted OIDC identity, so the provenance is genuine and proves only that TanStack's pipeline built the artifact, not that the artifact is safe. The practical consequence: provenance and attestation checks alone do not detect this class of attack. Pinning exact versions and verifying lockfile hashes against a known-good baseline are still required.

### Destructive and persistent: a 1-in-6 wipe and AI-agent persistence

**Takeaway: this wave added a sabotage payload and a developer-tool persistence mechanism not seen in earlier Mini Shai-Hulud waves.**

[BleepingComputer (Bill Toulas)](https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/)
reported a probabilistic sabotage mechanism with a 1-in-6 chance of running a recursive wipe on systems matching Israeli or Iranian locales, a new behavior class for this malware family.
[Expel](https://expel.com/blog/mini-shai-hulud-cross-ecosystem-supply-chain-worm-targeting-npm-pypi/)
reported that the worm injects persistence hooks into developer tooling, specifically
`.vscode/tasks.json`
and
`~/.claude/settings.json`
, so it survives reboots on developer endpoints. Defenders in the affected regions should treat the wipe behavior as a credible data-loss risk, and all teams should inspect those two file locations on engineer machines.

This destructive, geopolitically-targeted behavior is not new to the campaign. The original TeamPCP campaign report documented a conditional wiper in the earlier CanisterWorm payload that checked whether the infected system's timezone was set to Iran or its default language was Farsi, and on a match attempted to destroy data, wiping Kubernetes clusters node by node, or the local machine if no cluster was found. The current mechanism is a different payload and uses a probabilistic 1-in-6 trigger rather than a deterministic locale check, but it continues the same documented pattern of region-targeted data destruction layered onto a credential-theft operation.

### PCPJack: a rival worm evicting TeamPCP

**Takeaway: the first publicly documented actor to hunt and remove TeamPCP before stealing credentials, assessed with moderate confidence as a former affiliate.**

On 2026-05-07
[SentinelLABS](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/)
disclosed PCPJack, a cloud worm that scans for exposed Docker, Kubernetes, Redis, MongoDB, and RayML services, exploits five vulnerabilities for initial access (
[CVE-2025-29927](/vuln.html?cve=2025-29927)
Next.js middleware authentication bypass,
[CVE-2025-55182](/vuln.html?cve=2025-55182)
Next.js Server Actions deserialization,
[CVE-2026-1357](/vuln.html?cve=2026-1357)
WPVivid arbitrary file upload,
[CVE-2025-9501](/vuln.html?cve=2025-9501)
W3 Total Cache RCE,
[CVE-2025-48703](/vuln.html?cve=2025-48703)
CentOS Web Panel command injection), then kills TeamPCP processes and removes TeamPCP artifacts before harvesting npm, GitHub, and cloud credentials. SentinelLABS assesses with moderate confidence that PCPJack may be operated by a former TeamPCP affiliate, based on tradecraft overlap with the December 2025 PCPCat phase.
[BleepingComputer](https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/)
,
[SecurityWeek](https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/)
, and
[The Register](https://www.theregister.com/security/2026/05/08/worm-rubs-out-competitors-malware-then-takes-control/5237389)
covered it within 36 hours. A follow-up on 2026-05-13 continued the PCPJack story.

### Monetization stays frozen: Vect and CipherForce

**Takeaway: the affiliated extortion channels stayed inactive through the period, supporting the view that TeamPCP's ransomware monetization is impaired.**

Direct fetches of the
[ransomware.live Vect tracker](https://www.ransomware.live/group/vect)
show the victim count unchanged at 25, with the most recent posting dated 2026-04-15, leaving Vect operationally quiet for roughly 32 days by 2026-05-15.
[CipherForce](https://www.ransomware.live/group/cipherforce)
remained inactive at roughly 84 days, with 6 victims unchanged. Combined with the earlier Check Point disclosure of a cryptographic flaw in Vect 2.0, this reinforces the prior assessment that TeamPCP is currently monetizing through supply chain credential theft rather than affiliate ransomware.

### Institutional response: NHS moved, CISA did not

**Takeaway: a meaningful first government alert, against continued and now increasingly anomalous US federal silence.**

[NHS England Digital](https://digital.nhs.uk/cyber-alerts/2026/cc-4781)
issued cyber alert cc-4781 on 2026-05-12, the first government advisory of the campaign to name the affected packages. Against that, the meaningful negatives still hold: CISA did not issue a standalone TeamPCP advisory, did not add
[CVE-2026-45321](/vuln.html?cve=2026-45321)
to the Known Exploited Vulnerabilities catalog within the window, and has not named the operator. No Mandiant or Google Threat Intelligence Group named-actor product on the TanStack wave was published; technical attribution to TeamPCP rests on StepSecurity, Wiz, and Snyk. OpenAI published a corporate response titled "
[Our response to the TanStack npm supply chain attack](https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/)
".

## How the TanStack compromise worked (short version)

The attacker did not steal npm credentials. They abused CI: a
`pull_request_target`
workflow ran fork-controlled code on a privileged GitHub Actions runner, GitHub Actions cache poisoning was staged through a renamed attacker fork, and the pipeline's OIDC token was extracted from runner process memory. The malicious package versions were then published by TanStack's own trusted release identity, which is why the provenance attestations are valid. Two staged attacker forks were used and should not be conflated: github[.]com/voicproducoes/router (created 2026-05-10, per StepSecurity) and github[.]com/zblgg/configuration (account zblgg, commits 2026-05-11 19:20 to 19:26 UTC, per Wiz and Snyk).

## What defenders should do now

* Inventory installs of @tanstack/\* and the named packages (mistralai, guardrails-ai, @opensearch-project/opensearch, @uipath/
  *, @squawk/mcp, @tallyui/*
  ) created during the compromise windows below; treat matching installs as suspect.
* Rotate npm, GitHub, cloud provider, and CI/CD tokens that were exposed to affected CI runners.
* Stop treating SLSA provenance or attestation as sufficient; pin exact versions and verify lockfile hashes against a known-good baseline.
* Block and alert on the indicators below at egress, including the C2 IP and domain and the Session messenger exfiltration nodes.
* Inspect developer endpoints for persistence in
  `.vscode/tasks.json`
  and
  `~/.claude/settings.json`
  .
* Audit GitHub Actions for
  `pull_request_target`
  running on forks and for cache-poisoning exposure.
* For the Checkmarx Jenkins AST plugin, confirm you are on a remediated build (2.0.13-848.v76e89de8a\_053 or 2.0.13-847.v08c0072b\_2fd5) and not the tampered 2026.5.09.

## Compromise time windows (for CI self-check)

* Checkmarx Jenkins AST plugin tampered version exposure: 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC.
* TanStack malicious npm publishes: 2026-05-11 19:20 UTC to 19:26 UTC; broader worm propagation across npm and PyPI continued through 2026-05-13.

## Indicators of compromise

| Type | Indicator | Notes |
| --- | --- | --- |
| C2 IP | [83.142.209.194](/ipinfo.html?ip=83.142.209.194) | TanStack wave command and control (Wiz) |
| C2 domain | git-tanstack[.]com | TanStack wave command and control (Wiz, StepSecurity, Snyk) |
| Exfil node | filev2[.]getsession[.]org | Session messenger exfiltration (Wiz, StepSecurity, Snyk) |
| Exfil node | seed1[.]getsession[.]org | Session messenger exfiltration (Wiz, StepSecurity, Snyk) |
| Attacker fork | github[.]com/voicproducoes/router | Staged 2026-05-10 (StepSecurity) |
| Attacker fork | github[.]com/zblgg/configuration | Account zblgg, commits 2026-05-11 19:20 to 19:26 UTC (Wiz, Snyk) |
| File hash | router\_init.js SHA-256 ab4fcadaec49c03278063dd269ea5eef82d24f2124a8e15d7b90f2fa8601266c | TanStack malicious payload (Wiz, StepSecurity, Snyk) |
| Plugin version | Checkmarx Jenkins AST plugin 2026.5.09 | Tampered build (Checkmarx) |
| Vulnerability | [CVE-2026-45321](/vuln.html?cve=2026-45321) | TanStack compromise tracking ID, CVSS 9.6 (THN), GHSA-g7cv-rxg3-hmpx (Snyk) |
| Persistence | `.vscode/tasks.json` , `~/.claude/settings.json` | Developer-tool persistence hooks (Expel) |

## Watch items

* CISA action: a Known Exploited Vulnerabilities addition for
  [CVE-2026-45321](/vuln.html?cve=2026-45321)
  , a standalone TeamPCP advisory, or an emergency directive. The continued federal silence on a campaign of this profile is itself the watch item.
* Attribution: a Mandiant or Google Threat Intelligence Group named-actor product on the TanStack wave (the operator is tracked as UNC6780); current technical attribution rests only on StepSecurity, Wiz, and Snyk.
* Maintainer disclosures: postmortems or breach notifications from TanStack, Mistral AI, or Guardrails AI, including any SEC or privacy-law filings.
* A formal Checkmarx postmortem naming TeamPCP, given this is the third Checkmarx compromise in three months.
* Any verified wipe event, or a CERT-IL or CERT-IR advisory, tied to the locale-targeted destructive payload.
* Any patched Vect 2.1 release fixing the disclosed Vect 2.0 cryptographic flaw, or a CipherForce return after the prolonged freeze.