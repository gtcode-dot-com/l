---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T04:15:15.015045+00:00'
exported_at: '2026-04-08T04:15:18.517100+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32864
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European
    Commission Cloud Breach, Sportradar Details Emerge, and Mandiant Quantifies Campaign
    at 1,000+ SaaS Environments, Author: Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European
    Commission Cloud Breach, Sportradar Details Emerge, and Mandiant Qu...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32864
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 006 - CERT-EU Confirms European Commission
  Cloud Breach, Sportradar Details Emerge, and Mandiant Quantifies Campaign at 1,000&#x2b;
  SaaS Environments, (Fri, Apr 3rd)'
updated_at: '2026-04-08T04:15:15.015045+00:00'
url_hash: c7cce347fe1acf350923f220355cbe9a8640521c
---

This is the sixth update to the TeamPCP supply chain campaign threat intelligence report,
["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
(v3.0, March 25, 2026).
[Update 005](https://isc.sans.edu/diary/32856)
covered developments through April 1, including the first confirmed victim disclosure (Mercor AI), Wiz's post-compromise cloud enumeration findings, DPRK attribution of the axios compromise, and LiteLLM's release resumption after Mandiant's forensic audit. This update covers intelligence from April 1 through April 3, 2026.

## CRITICAL: CERT-EU Confirms European Commission Cloud Breach via Trivy Supply Chain Compromise

[CERT-EU disclosed](https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain)
on April 2-3, 2026 that the European Commission's Europa web hosting platform on AWS was breached through the Trivy supply chain compromise (CVE-2026-33634). This is the highest-profile governmental victim disclosure to date.

Key details from the CERT-EU advisory:

* **Initial access:**
  AWS API keys stolen via the compromised Trivy scanner on March 19
* **Detection:**
  European Commission Security Operations Center fired alerts on March 24 (5 days after initial intrusion)
* **CERT-EU notified:**
  March 25; access revoked same day
* **Data exfiltrated:**
  340 GB uncompressed (91.7 GB compressed archive) from the compromised AWS account
* **Email exposure:**
  Approximately 52,000 email-related files (2.22 GB) of outbound communications
* **Scope:**
  71 clients affected: 42 internal European Commission departments plus 29 other EU entities, meaning at least 30 Union entities were potentially impacted
* **Data publication:**
  ShinyHunters published the stolen data on their dark web leak site on March 28
* **Lateral movement:**
  CERT-EU confirmed no lateral movement to other Commission AWS accounts was detected
* **[Europa.eu](http://Europa.eu)
  websites**
  remained unaffected throughout

Analysts assess this disclosure is significant on multiple dimensions. First, it confirms that TeamPCP-harvested credentials reached a major governmental institution, not just private-sector targets. Second, the involvement of ShinyHunters in the data publication raises questions about the credential distribution chain, as ShinyHunters is operationally distinct from TeamPCP's known LAPSUS$ and Vect partnerships. Third, the five-day dwell time between initial access (March 19) and detection (March 24) is consistent with the 24-hour operational tempo that
[Wiz documented](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild)
for TeamPCP's post-compromise cloud enumeration.

**Recommended action:**
EU institutions and organizations hosted on Europa infrastructure should review CERT-EU's advisory for specific exposure indicators. Organizations with AWS credentials that may have been exposed through the Trivy compromise should treat the EC breach as confirmation that stolen credentials are being actively used against high-value targets. The CERT-EU disclosure timeline (initial access March 19, detection March 24, notification March 25, public disclosure April 2) demonstrates that even well-resourced organizations required five days to detect the intrusion.

## HIGH: Sportradar AG Breach Details Confirmed: TeamPCP and Vect Joint Operation

VECERT reported on April 2, 2026 that the Sportradar AG breach (first claimed as a CipherForce victim in
[Update 004](https://isc.sans.edu/diary/32846)
) has been confirmed as a "systemic compromise" jointly operated by TeamPCP and Vect ransomware. Sportradar is a $4.98 billion Swiss sports technology company.

Confirmed breach details:

* **Entry vector:**
  Supply chain via compromised Trivy (CVE-2026-33634)
* **Personal data:**
  Approximately 26,000 users' personal information exposed
* **Athlete records:**
  23,169 records including names, dates of birth, gender, and nationality
* **Client exposure:**
  Client table listing 161 organizations including ESPN, Nike, NBA Asia, and IMG Arena
* **Credential exposure:**
  8 production RDS database passwords, 328 platform API key/secret pairs, Kafka SASL credentials, and New Relic monitoring tokens
* **CipherForce ransomware:**
  Listed on the CipherForce shame site with the original 14-15 day publication deadline (approaching approximately April 10-11)

This is the first confirmed case of TeamPCP and Vect operating jointly against a single target, validating the dual-track ransomware model documented in earlier updates. The exposure of 161 client organizations including major sports leagues and media companies creates a cascading notification and risk assessment obligation for Sportradar.

**Recommended action:**
Organizations with Sportradar business relationships should proactively assess whether their data appears in the exposed client table. The 328 exposed API key/secret pairs create a secondary supply chain risk for Sportradar's integration partners.

## HIGH: Mandiant Quantifies Campaign Scale: Over 1,000 SaaS Environments, Estimated 500,000 Machines

Multiple vendor statements published April 1-2 have provided the first authoritative quantification of the campaign's total blast radius:

* **Mandiant CTO Charles Carmakal**
  stated that Google-owned Mandiant knew of
  ["over 1,000 impacted SaaS environments"](https://www.theregister.com/2026/04/02/mercor_supply_chain_attack/)
  actively dealing with cascading effects from the TeamPCP supply chain compromises.
* **Google Cloud researchers**
  warned that "hundreds of thousands of stolen secrets could potentially be circulating" from the credential trove.
* **[The Register](https://www.theregister.com/2026/04/02/mercor_supply_chain_attack/)**
  cited estimates suggesting attackers exfiltrated data and secrets from approximately
  **500,000 machines**
  total across all victims.
* **[Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/)**
  identified affected organizations across the US, Europe, Middle East, South Asia, and Australia, spanning financial services, technology, retail, legal, insurance, and education sectors.

These numbers move the campaign's assessed scale from qualitative ("thousands of downstream environments," per the FBI alert) to quantitative. The 1,000+ SaaS environments figure is particularly significant because it implies credential exploitation is ongoing across a far larger surface than the handful of publicly named victims suggests.

**Recommended action:**
Organizations that have not yet completed credential rotation should treat the Mandiant quantification as definitive evidence that delayed rotation increases exposure to an actively exploited credential pool of industrial scale.

## MEDIUM: Elastic Security Labs Publishes Container Attack Detection Guide with MITRE ATT&CK Mapping

[Elastic Security Labs published](https://www.elastic.co/security-labs/teampcp-container-attack-scenario)
a new technical resource, "Linux & Cloud Detection Engineering: TeamPCP Container Attack Scenario," providing a full walkthrough of TeamPCP's multi-stage container compromise methodology. This is distinct from Elastic's earlier
[axios supply chain compromise detections](https://www.elastic.co/security-labs/axios-supply-chain-compromise-detections)
covered in
[Update 005](https://isc.sans.edu/diary/32856)
and focuses specifically on the TeamPCP toolchain.

New technical details documented:

* **Tunneling tools:**
  TeamPCP uses
  **frps**
  (fast reverse proxy) and
  **gost**
  for establishing persistent tunnels and proxying through compromised container environments
* **React2Shell:**
  A web server exploitation technique used for initial foothold in containerized workloads
* **D4C telemetry:**
  Full detection walkthrough using Elastic's Defend for Containers telemetry
* **MITRE ATT&CK mapping:**
  Each stage of the container attack chain mapped to specific ATT&CK techniques, providing structured detection logic

**Recommended action:**
SOC teams operating containerized workloads should review the Elastic guide for detection rules specific to TeamPCP's container attack methodology. The frps and gost indicators are new IOCs not previously documented in the campaign's public reporting.

## MEDIUM: Mercor Breach Triggers Class Action Investigations

The
[Mercor AI breach](https://isc.sans.edu/diary/32856)
(first confirmed in
[Update 005](https://isc.sans.edu/diary/32856)
) has escalated beyond incident response into legal proceedings. Shamis & Gentile P.A. has launched a class action investigation into Mercor's data breach, focusing on the exposure of contractor and customer data including biometric identity verification materials (passports and video interviews).

Additional context that emerged April 1-2:

* **[Fortune](https://fortune.com/2026/04/02/mercor-ai-startup-security-incident-10-billion/)**
  reported Mercor is valued at $10 billion (raised $350M Series C in October 2025)
* Mercor's customers confirmed to include
  **Anthropic, OpenAI, and Meta**
* LAPSUS$ published samples including Slack data, internal ticketing records, and two videos of AI-contractor conversations
* Data is listed for
  **live auction on the dark web**

The class action investigation introduces a legal dimension to the campaign's downstream consequences. The exposure of biometric identity verification materials (passports) for an estimated 30,000+ AI contractors raises GDPR, CCPA, and potentially BIPA obligations.

## INFO: New Vendor Publications and Analysis

Several new vendor publications appeared in the April 1-3 window:

* **[Datadog Security Labs](https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/)**
  published a detailed technical trace of the full LiteLLM and Telnyx PyPI compromise chain, tracing it back to the March 19 Trivy origin and recommending that any host that installed compromised versions be treated as a "full-credential exposure event."
* **[Oligo Security](https://www.oligo.security/blog/teampcp-campaign-the-evolution-of-modern-supply-chain-attacks)**
  published "Evolution of Modern Supply Chain Attacks," documenting TeamPCP's credential harvesting timeline and framing the campaign as a "meaningful shift" in how sophisticated actors approach supply chain as an attack surface.
* **[The New Stack](https://thenewstack.io/cicd-pipeline-front-line/)**
  (April 2) published "The CI/CD Pipeline Is the New Front Line," positioning TeamPCP as a watershed moment for CI/CD pipeline security.
* **[CYFIRMA Weekly Intelligence Report](https://www.cyfirma.com/news/weekly-intelligence-report-03-april-2026/)**
  (April 3) covered the campaign, noting the Europa hosting platform impact and the 71 affected clients.

## INFO: Supply Chain Pause Extends to Approximately 16 Days

No new package compromises have been reported since the Telnyx PyPI disclosure on March 27. The supply chain pause is now approximately 384 hours (16 days), doubling the 192-hour pause reported in
[Update 005](https://isc.sans.edu/diary/32856)
. Independent searches of RubyGems,
[crates.io](http://crates.io)
, and Maven Central continue to show zero TeamPCP-related IOCs. The campaign remains confined to five ecosystems: GitHub Actions, PyPI, npm, Docker Hub/GHCR, and OpenVSX.

The CISA KEV remediation deadline for CVE-2026-33634 is now
**5 days away**
(April 8, 2026).

## Watch Item Status

| Watch Item | Status |
| --- | --- |
| European Commission breach response | **NEW** : CERT-EU disclosed April 2-3; 71 clients affected, 30 EU entities; ShinyHunters published data March 28 |
| Sportradar data publication deadline | **NEW/APPROACHING** : CipherForce 14-15 day deadline from March 26-27 claim approaches approximately April 10-11 |
| Campaign scale quantification | **CONFIRMED** : Mandiant: 1,000+ SaaS environments; estimates of 500,000 machines across all victims |
| Mercor legal proceedings | **NEW** : Class action investigation launched by Shamis & Gentile; Fortune values Mercor at $10B |
| CISA KEV deadline (April 8) | **5 days remaining** : Organizations running Trivy must remediate to v0.69.2+, trivy-action v0.35.0, or setup-trivy v0.2.6 |
| Databricks official statement | **Pending** : No official disclosure; internal investigation ongoing per Update 004 |
| Vect ransomware confirmed deployments | **No confirmed downstream deployments** from affiliate program; distribution window now approximately 16 days |
| AstraZeneca confirmation or denial | **No official statement** : Now approximately 8 days since initial LAPSUS$ claim |
| Additional package compromises | **No new compromises** : 16-day pause, longest since campaign began |
| CISA standalone advisory | **Pending at day 20** : KEV entries, FBI alert, and Singapore CSA advisories only; no dedicated advisory or emergency directive |
| Expansion to RubyGems/crates.io/Maven | **Not observed** : Zero IOCs in independent registry searches |
| Law enforcement action | **No public action** : FBI advisory issued but no arrests, indictments, or infrastructure seizures |
| ownCloud build restoration | **Pending** : Several weeks estimated; no timeline update since initial disclosure |
| Nation-state credential exploitation | **CONFIRMED** : DPRK UNC1069/Sapphire Sleet axios attack attributed by four vendors per Update 005; credential link to TeamPCP trove not ruled out |
| ShinyHunters involvement | **NEW** : Published EC data March 28; relationship to TeamPCP/LAPSUS$/Vect ecosystem unclear |