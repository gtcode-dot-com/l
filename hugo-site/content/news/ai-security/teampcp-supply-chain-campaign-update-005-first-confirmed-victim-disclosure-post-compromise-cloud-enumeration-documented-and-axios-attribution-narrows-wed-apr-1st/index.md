---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T10:15:15.780208+00:00'
exported_at: '2026-04-02T10:15:18.521992+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32856
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim
    Disclosure, Post-Compromise Cloud Enumeration Documented, and Axios Attribution
    Narrows, Author: Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim Disclosure,
    Post-Compromise Cloud Enumeration Documented, and Axios At...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32856
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 005 - First Confirmed Victim Disclosure,
  Post-Compromise Cloud Enumeration Documented, and Axios Attribution Narrows, (Wed,
  Apr 1st)'
updated_at: '2026-04-02T10:15:15.780208+00:00'
url_hash: e4dde60b673638dc14520b5d2d4bd1a39b3cdabd
---

This is the fifth update to the TeamPCP supply chain campaign threat intelligence report,
["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
(v3.0, March 25, 2026). Update 004 covered developments through March 30, including the Databricks investigation, dual ransomware operations, and AstraZeneca data release. This update consolidates two days of intelligence through April 1, 2026.

## HIGH: Mercor AI Confirms Breach Tied to LiteLLM Supply Chain Compromise - First Official Victim Disclosure

AI recruiting startup Mercor has publicly confirmed it was breached as a direct consequence of the LiteLLM supply chain compromise, making it the
**first organization to officially acknowledge being victimized**
through the TeamPCP campaign.
[TechCrunch](https://techcrunch.com/2026/03/31/mercor-says-it-was-hit-by-cyberattack-tied-to-compromise-of-open-source-litellm-project/)
reported on March 31 that LAPSUS$ claims to have exfiltrated approximately 4TB of data, including 939GB of source code, a 211GB user database, and 3TB of video interviews and identity verification documents (passports). Initial access was reportedly via a compromised Tailscale VPN credential.

Mercor stated it was "one of thousands of companies" affected by the LiteLLM compromise. The nature of the claimed exfiltrated data -- which includes biometric identity verification materials -- raises significant privacy and regulatory implications under GDPR, CCPA, and potentially HIPAA depending on the contents.

This is operationally significant because it moves the campaign's downstream impact from theoretical to confirmed. Prior victim claims (AstraZeneca, Databricks) remain unconfirmed by the named organizations. Mercor's public acknowledgment validates what analysts have assessed since Update 002: the credential trove harvested during the supply chain phase is being actively exploited for data theft and extortion.

**Recommended action:**
Organizations that used LiteLLM v1.82.7 or v1.82.8 should treat this as confirmation that credential exploitation is actively underway. If you have not completed credential rotation, the Mercor disclosure demonstrates the consequence of delay. VPN credentials, cloud access tokens, and API keys accessible in compromised environments should be prioritized for rotation.

## HIGH: Wiz Documents TeamPCP Post-Compromise AWS and Cloud Enumeration in the Wild

[SecurityWeek](https://www.securityweek.com/teampcp-moves-from-oss-to-aws-environments/)
reported on March 31 that Wiz's Cloud Incident Response Team (CIRT) has published detailed findings on TeamPCP's post-compromise cloud operations in
["Tracking TeamPCP: Investigating Post-Compromise Attacks Seen in the Wild"](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild)
. This is the first detailed public documentation of what TeamPCP does after obtaining stolen credentials.

Key findings from the Wiz CIRT investigation:

* **Credential validation via TruffleHog:**
  TeamPCP uses the open-source secret scanning tool TruffleHog to programmatically verify that stolen AWS access keys, Azure application secrets, and SaaS tokens are still valid and in use.
* **24-hour operational tempo:**
  Within 24 hours of validating stolen secrets, the group transitions to discovery operations in compromised AWS environments.
* **AWS enumeration focus:**
  Discovery operations enumerate IAM roles, EC2 instances, Lambda functions, RDS databases, S3 buckets, and ECS clusters, with particular focus on container infrastructure where the group maps clusters and task definitions.
* **Bold operational signatures:**
  The group uses conspicuous resource names including "pawn" and "massive-exfil" -- analysts assess this indicates either operational carelessness or deliberate intimidation, consistent with their public Telegram messaging.

The Wiz findings also contextualize the Flare threat intelligence report, which found that TeamPCP's cloud infrastructure targeting breaks down as Azure (61%) and AWS (36%), accounting for 97% of compromised servers.

**Recommended action:**
Organizations should search cloud audit logs for unauthorized IAM enumeration, EC2/ECS/Lambda discovery calls, and S3 listing operations originating from unfamiliar principals. TruffleHog validation attempts may appear as rapid sequential API calls testing credential validity across multiple services. Search for resources with names containing "pawn", "massive-exfil", or similar conspicuous strings.

**Note for threat hunters:**
The
[full Wiz CIRT report](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild)
contains extensively documented indicators of compromise including specific AWS API call patterns, resource naming conventions, and infrastructure fingerprints observed in the wild. Threat hunters and SOC teams should review the Wiz report in detail for actionable detection content.

## MEDIUM: Axios npm Compromise Attributed to North Korean UNC1069 - Not TeamPCP, but Credential Source Remains Open

The axios npm compromise (March 30-31, malicious versions 1.14.1 and 0.30.4) has received formal attribution.
[Elastic Security Labs](https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all)
published a detailed analysis identifying the macOS Mach-O binary payload as overlapping with WAVESHAPER, a C++ backdoor that Mandiant attributes to
**UNC1069, a suspected North Korean threat actor**
.
[Google's Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)
published a companion analysis confirming the DPRK attribution.

This narrows the assessment from Update 004's "credential provenance raises TeamPCP questions" to a more specific picture: analysts assess with high confidence that
**a different threat actor executed the axios attack**
, but the question of how the maintainer's npm token was originally obtained remains unanswered. The token was a long-lived classic npm access token -- exactly the type that TeamPCP's CanisterWorm
`findNpmTokens()`
function harvests from CI/CD environments. The timing aligns with TeamPCP's monetization phase and the BreachForums credential distribution to approximately 300,000 users.

The SANS ISC Stormcast for
[April 1, 2026](https://isc.sans.edu/podcastdetail/9874)
noted: "Given that TeamPCP recently collected so many developer credentials, it's very possible that they were involved in the Axios compromise, though the follow-up compromise doesn't look like TeamPCP, as the techniques look a little bit different."

Singapore's Cyber Security Agency has issued a second advisory,
[AD-2026-002](https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-002/)
, specifically addressing the axios supply chain attack -- making Singapore the only government to have issued dedicated advisories for both the TeamPCP campaign and the axios incident.

**Recommended action:**
Organizations that installed axios v1.14.1 or v0.30.4 should check for platform-specific IOCs: macOS (
`/Library/Caches/com.apple.act.mond`
), Windows (
`%PROGRAMDATA%\wt.exe`
), Linux (
`/tmp/ld.py`
). Block C2 domain
`sfrclak[.]com`
and IP
`142.11.206[.]73`
. The DPRK attribution elevates the severity -- this is now a nation-state operation exploiting the same credential ecosystem that TeamPCP seeded.

## MEDIUM: LiteLLM Resumes Publishing After Forensic Audit - Release Freeze Lifted

BerriAI has lifted the LiteLLM release freeze that has been in effect since March 25. According to the
[LiteLLM security update](https://docs.litellm.ai/blog/security-update-march-2026)
, the Mandiant-led forensic audit verified every release from v1.78.0 through v1.82.6 via SHA-256 comparison against the Git repository, confirming no additional compromised versions exist beyond the known-malicious v1.82.7 and v1.82.8. A new safe version was published on March 31, 2026.

This resolves the "LiteLLM/BerriAI release resumption" watch item that has been tracked since Update 001. The quarantine lift and publishing resumption signal that the forensic investigation found no evidence of earlier or broader compromise beyond the two known-malicious versions.

**Recommended action:**
Organizations that froze LiteLLM upgrades can resume normal update procedures. Verify you are running a version that post-dates the forensic audit. Continue to treat any historical installation of v1.82.7 or v1.82.8 as a confirmed compromise requiring full credential rotation.

## INFO: ownCloud Discloses CVE-2026-33634 Build Infrastructure Impact

[ownCloud](https://owncloud.com/security-advisories/security-notice-impact-of-cve-2026-33634-on-owncloud-build-infrastructure/)
published a security notice confirming their build infrastructure was affected by the Trivy supply chain compromise (CVE-2026-33634). ownCloud stated that no customer data was compromised, characterizing the impact as limited to build pipeline exposure. This is notable as one of the few organizations to proactively disclose exposure without a corresponding extortion claim. This is a positive example of transparent incident communication.

## INFO: Supply Chain Pause Extends to Approximately 192 Hours

No new package compromises have been reported since the Telnyx PyPI disclosure on March 27. The supply chain pause is now approximately 192 hours (8 days) -- extending the record documented in Updates 003 through the Update 005 draft. The CISA KEV remediation deadline for CVE-2026-33634 is now
**7 days away**
(April 8, 2026).

Independent searches of RubyGems, crates.io, and Maven Central continue to show zero TeamPCP-related IOCs. The campaign remains confined to five ecosystems: GitHub Actions, PyPI, npm, Docker Hub/GHCR, and OpenVSX.

## Watch Item Status

| Watch Item | Status |
| --- | --- |
| First confirmed victim disclosure | **RESOLVED** -- Mercor AI confirmed breach via LiteLLM on March 31 |
| Post-compromise cloud activity | **DOCUMENTED** -- Wiz CIRT published AWS/Azure enumeration findings |
| Axios token provenance | **NARROWED** -- Google TIG/Elastic attribute execution to DPRK UNC1069; token source still undetermined |
| LiteLLM/BerriAI release resumption | **RESOLVED** -- Publishing resumed March 31 after Mandiant forensic audit |
| Databricks official statement | **Pending** -- No official disclosure, internal investigation ongoing |
| AstraZeneca confirmation or denial | **No official statement** -- Data released by LAPSUS$, Cybernews partially verified contents |
| Vect ransomware confirmed deployments from affiliate program | **No confirmed deployments** -- Distribution window now approximately 192 hours |
| Additional package compromises | **No new compromises** -- 192-hour pause, longest since campaign began |
| CISA standalone advisory | **Pending at day 14** -- KEV entry, FBI alert, and Singapore CSA advisories only |
| Expansion to RubyGems/crates[.]io/Maven | **Not observed** -- Zero IOCs in independent registry searches |
| CISA KEV deadline | **April 8, 2026** -- 7 days remaining |
| Nation-state credential exploitation | **NEW** -- DPRK-attributed UNC1069 may be leveraging TeamPCP-seeded credential ecosystem |

The full campaign report is available at
[sans.org/white-papers/when-security-scanner-became-weapon](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
. A SANS Emergency Webcast replay is available at
[sans.org/webcasts/when-security-scanner-became-weapon](https://www.sans.org/webcasts/when-security-scanner-became-weapon)
. Updates to the report will be in the form of these ISC diaries.