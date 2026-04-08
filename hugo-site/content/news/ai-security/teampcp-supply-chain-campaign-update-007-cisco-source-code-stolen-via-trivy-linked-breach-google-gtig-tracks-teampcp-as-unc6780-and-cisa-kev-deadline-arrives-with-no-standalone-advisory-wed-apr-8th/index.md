---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T18:15:14.909461+00:00'
exported_at: '2026-04-08T18:15:17.131218+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32880
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen
    via Trivy-Linked Breach, Google GTIG Tracks TeamPCP as UNC6780, and CISA KEV Deadline
    Arrives with No Standalone Advisory, Author: Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen
    via Trivy-Linked Breach, Google GTIG Tracks TeamPCP as UNC6780, and...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32880
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 007 - Cisco Source Code Stolen via Trivy-Linked
  Breach, Google GTIG Tracks TeamPCP as UNC6780, and CISA KEV Deadline Arrives with
  No Standalone Advisory, (Wed, Apr 8th)'
updated_at: '2026-04-08T18:15:14.909461+00:00'
url_hash: 6e1f85fa5ddd9ee5f946d69ac42d17ecf303ed35
---

This is the seventh update to the TeamPCP supply chain campaign threat intelligence report,
["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
(v3.0, March 25, 2026).
[Update 006](https://isc.sans.edu/diary/32864)
covered developments through April 3, including the CERT-EU European Commission breach disclosure, ShinyHunters' confirmation of credential sharing, Sportradar breach details, and Mandiant's quantification of 1,000+ compromised SaaS environments. This update consolidates five days of intelligence from April 3 through April 8, 2026.

## HIGH: Cisco Development Environment Breached via Trivy Supply Chain, 300+ Repositories Stolen

[BleepingComputer reported](https://www.bleepingcomputer.com/news/security/cisco-source-code-stolen-in-trivy-linked-dev-environment-breach/)
that threat actors leveraged credentials stolen through the Trivy supply chain compromise (
[CVE-2026-33634](/vuln.html?cve=2026-33634)
) to breach Cisco's internal development environment. The attackers gained access to build systems and developer workstations through a malicious GitHub Action plugin.

The breach scope is substantial:

* **Over 300 private GitHub repositories**
  containing Cisco source code were cloned, including code for AI-powered products and unreleased items
* **Customer repositories**
  belonging to banks, business process outsourcing firms, and US government agencies were among those exfiltrated
* **AWS keys**
  were stolen and used for unauthorized activities across Cisco's cloud accounts
* **Multiple threat actors**
  were reportedly involved in the Cisco CI/CD and AWS account breaches, "with varying degrees of activity"

ShinyHunters subsequently
[expanded their claims](https://cybernews.com/security/hackers-blackmail-cisco-over-stolen-salesforce-data/)
beyond the development environment, alleging access to 3 million or more Salesforce records, additional GitHub repositories, and AWS S3 buckets. The claimed dataset allegedly includes records tied to personnel at FBI, DHS, DISA, IRS, and NASA, as well as the Australian Ministry of Defense and Indian government agencies. These expanded claims have not been independently verified.

ShinyHunters set an extortion deadline of approximately April 3. As of April 8, no public data dump has materialized and Cisco has not issued a public statement specifically addressing the ShinyHunters extortion claim. The deadline passage without publication, combined with CipherForce's infrastructure outage documented below, represents the second data point suggesting potential friction in the campaign's monetization pipeline.

The Cisco breach is significant because it is the highest-profile technology company confirmed as a direct victim of the Trivy supply chain compromise. The involvement of multiple threat actors in a single victim's environment is consistent with the credential-sharing pattern documented in
[Update 006](https://isc.sans.edu/diary/32864)
. The theft of customer source code repositories for banks and US government agencies creates secondary exposure obligations for downstream organizations.

**Recommended action:**
Organizations that are Cisco customers or partners, particularly those with source code or build artifacts hosted in Cisco's development infrastructure, should contact Cisco to determine whether their repositories were among those exfiltrated. Organizations using Cisco AI products should monitor for unauthorized use of stolen source code.

## MEDIUM: Google GTIG Formally Designates TeamPCP as UNC6780

Google Threat Intelligence Group (GTIG) has assigned the formal tracking designation
**UNC6780**
to TeamPCP. The designation appeared in GTIG's
[analysis of the axios npm supply chain attack](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)
, which attributed that separate compromise to North Korean threat actor UNC1069. In distinguishing the two campaigns, GTIG identified TeamPCP/UNC6780 as the financially motivated group responsible for the Trivy, Checkmarx, LiteLLM, and Telnyx compromises. GTIG also named TeamPCP's credential stealer payload as
**SANDCLOCK**
.

The UNC6780 designation is significant for three reasons. First, it confirms Google is formally tracking TeamPCP as a distinct, persistent threat actor rather than treating the campaign as a series of unrelated incidents. Second, UNC (uncategorized) designations in Google's taxonomy indicate the threat actor does not yet map to a known state-sponsored cluster, reinforcing the financially motivated assessment from earlier reporting. Third, the designation provides a standardized reference for cross-vendor threat intelligence sharing as multiple organizations (Mandiant, Wiz, Unit 42, Elastic, Datadog) independently track overlapping aspects of the campaign.

The
[Google Cloud Threat Horizons H1 2026](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026)
report also covers UNC6780. Analysts assess the formal GTIG tracking designation, combined with Mandiant's engagement on the LiteLLM forensics and their quantification of 1,000+ compromised SaaS environments, indicates Google considers UNC6780 a top-tier financially motivated threat actor.

**Recommended action:**
Organizations using Google Chronicle, VirusTotal, or Mandiant Advantage should search for UNC6780 indicators in their environments. The SANDCLOCK designation provides a specific malware family name for detection rule authoring.

## MEDIUM: CipherForce Leak Infrastructure Goes Dark as Sportradar Deadline Approaches

CipherForce's two known Tor-based leak sites remain unavailable, confirmed via
[ransomware tracking services](https://www.ransomware.live/group/cipherforce)
. The group has not posted new victims since February 23, 2026 (a gap of 44 days). This infrastructure outage coincides with the approaching Sportradar AG data publication deadline (approximately April 10-11), which was set when CipherForce first claimed the Sportradar breach around March 26-27.

Analysts assess three possible explanations: (1) the outage may be related to the internal friction and "mole hunt"
[reported in Update 006](https://isc.sans.edu/diary/32864)
, suggesting operational disruption within the TeamPCP ecosystem is affecting CipherForce's ability to maintain infrastructure; (2) the sites may have been deliberately taken offline as an operational security measure following increased law enforcement and researcher attention; or (3) the outage may be temporary and unrelated to operational factors.

The Sportradar deadline remains the key near-term indicator. If CipherForce's infrastructure returns online with published Sportradar data around April 10-11, it would confirm the group remains operationally capable despite reported infighting. If the deadline passes without publication, it may signal meaningful disruption to TeamPCP's ransomware operations. The ShinyHunters/Cisco extortion deadline lapsing on approximately April 3 without a visible data dump adds a second data point suggesting potential friction in the monetization pipeline, though negotiations may be occurring privately.

**Recommended action:**
Organizations monitoring the Sportradar breach (particularly the 161 client organizations and third-party credential holders identified in
[Update 006](https://isc.sans.edu/diary/32864)
) should continue preparing for potential data publication while noting the operational uncertainty.

## MEDIUM: CISA KEV Deadline Arrives, Still No Standalone Advisory at Day 27

The CISA KEV remediation deadline for
[CVE-2026-33634](/vuln.html?cve=2026-33634)
is
**today, April 8, 2026**
. Federal civilian executive branch agencies are required to have remediated under BOD 22-01. CISA has not issued a standalone advisory, emergency directive, or joint advisory with FBI/NSA specific to the TeamPCP campaign. The regulatory response gap noted in
[Update 004](https://isc.sans.edu/diary/32846)
persists at day 27 since the campaign's initial compromise.

For comparison, Singapore's Cyber Security Agency remains the only government worldwide to have issued dedicated advisories, now totaling two:
[AD-2026-001](https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-001/)
(TeamPCP campaign, March 27) and AD-2026-002 (axios npm compromise). No advisories from NCSC (UK), ACSC (Australia), CCCS (Canada), or BSI (Germany) have been identified. The absence of a Five Eyes joint advisory for a campaign of this scale (1,000+ SaaS environments, a confirmed EU government breach, and active ransomware partnerships) is notable.

**Recommended action:**
Organizations that have not yet completed remediation should treat the KEV deadline as a hard compliance checkpoint. Beyond patching Trivy to v0.69.2+, trivy-action to v0.35.0, or setup-trivy to v0.2.6, organizations must also complete credential rotation for any secrets that may have been exposed during the March 19-27 compromise window. Patching alone is insufficient without credential rotation.

## MEDIUM: ShinyHunters Claims Snowflake/Anodot Breach in Parallel Operation

[BleepingComputer reported](https://www.bleepingcomputer.com/news/security/snowflake-customers-hit-in-data-theft-attacks-after-saas-integrator-breach/)
on April 7 that ShinyHunters claimed responsibility for data theft from over a dozen Snowflake customers via compromised authentication tokens from Anodot, a SaaS data anomaly detection provider. ShinyHunters confirmed stealing data "from dozens of companies" and demanded ransom payments.

This breach appears to be a separate operation from the TeamPCP supply chain campaign, with the attack vector being stolen Anodot authentication tokens rather than TeamPCP-sourced credentials. However, it is operationally significant because ShinyHunters is the same group that
[confirmed in Update 006](https://isc.sans.edu/diary/32864)
they had accessed credentials from the TeamPCP trove. ShinyHunters is now running at least two concurrent campaigns: TeamPCP credential exploitation (European Commission data publication, Cisco extortion) and the Anodot/Snowflake breach. Their sustained operational tempo across multiple fronts suggests the group has significant capacity and is not constrained by any single operation.

**Recommended action:**
Organizations using Snowflake or Anodot should follow Snowflake's guidance for affected customers. For the TeamPCP campaign specifically, this development reinforces that ShinyHunters represents an active and expanding threat vector for stolen credential monetization.

## INFO: Supply Chain Pause Extends to 24 Days

No new package compromises have been reported since the Telnyx PyPI disclosure on March 27. The supply chain pause is now approximately 576 hours (24 days). No compromises in RubyGems,
[crates.io](http://crates.io)
, or Maven Central have been reported by any source monitoring these registries. The campaign remains confined to five ecosystems: GitHub Actions, PyPI, npm, Docker Hub/GHCR, and OpenVSX.

The extended pause, now the longest since the campaign began on March 19, is consistent with the operational phase transition from supply chain compromise to credential monetization. TeamPCP/UNC6780 retains an estimated 300 GB+ of stolen credentials, and multiple groups (LAPSUS$, Vect, ShinyHunters) continue actively exploiting this material as documented in prior updates.

## INFO: Campaign Receding from Daily Security News Coverage

Notably, the April 6-8 period produced no new TeamPCP-specific articles from major Tier 1 security publications (BleepingComputer, The Record, SecurityWeek, Dark Reading). The SANS ISC Stormcast episodes for
[April 7](https://isc.sans.edu/podcastdetail/9882)
and
[April 8](https://isc.sans.edu/podcastdetail/9884)
did not mention TeamPCP. This contrasts with the March 25 through April 3 period when the campaign generated daily coverage across multiple outlets.

Analysts assess this reflects the campaign transitioning from active supply chain compromise (which generates immediate news coverage) to credential monetization (which generates coverage only when specific victims are disclosed). The underlying threat has not diminished; Mandiant's assessment of 1,000+ compromised SaaS environments and an estimated 500,000 machines means the blast radius is still expanding through discovery rather than new attacks.

## Watch Item Status

| Watch Item | Status |
| --- | --- |
| Cisco development environment breach | 300+ repos stolen via Trivy supply chain; ShinyHunters April 3 extortion deadline passed without visible data dump; expanded claims include 3M+ Salesforce records; no Cisco public statement |
| Google GTIG tracking | TeamPCP formally designated UNC6780; credential stealer named SANDCLOCK |
| CipherForce infrastructure | **OFFLINE** : Both Tor leak sites unavailable for 44+ days; no new victims posted since Feb 23 |
| Sportradar data publication deadline | **IMMINENT** : CipherForce deadline approximately April 10-11; leak infrastructure currently offline |
| CISA KEV deadline (April 8) | **TODAY** : Federal agencies required to have remediated under BOD 22-01; no standalone advisory at day 27 |
| ShinyHunters operations | Running concurrent campaigns: TeamPCP credential exploitation AND Snowflake/Anodot breach (April 7); high operational tempo |
| TeamPCP internal friction | Infighting and "mole hunt" reported; may be connected to CipherForce infrastructure outage and lapsed extortion deadlines |
| Campaign blast radius | Mandiant: 1,000+ SaaS environments; organizations still discovering breaches from initial wave |
| Databricks official statement | **Pending** : No official disclosure or denial; internal investigation ongoing per Update 004 |
| AstraZeneca confirmation or denial | **No official statement** : Now approximately 19 days since initial LAPSUS$ claim; data released for free after failed monetization |
| Additional package compromises | **No new compromises** : 24-day pause, longest since campaign began |
| CISA standalone advisory | **Pending at day 27** : KEV entries, FBI alert, and Singapore CSA advisories only |
| Expansion to RubyGems/crates.io/Maven | **Not observed** : No compromises reported in these registries |
| Law enforcement action | **No public action** : No arrests, indictments, or infrastructure seizures |
| ownCloud build restoration | **Pending** : Build infrastructure remains fully offline; no restoration timeline provided |
| Vect ransomware affiliate deployments | **No confirmed mass deployments** : Sportradar confirmed as joint operation; no broad affiliate activity reported |