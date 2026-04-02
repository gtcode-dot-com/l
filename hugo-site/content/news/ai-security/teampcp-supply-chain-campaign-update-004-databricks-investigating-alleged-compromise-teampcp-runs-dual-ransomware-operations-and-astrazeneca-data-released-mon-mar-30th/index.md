---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T12:15:15.782557+00:00'
exported_at: '2026-04-02T12:15:19.170315+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32846
structured_data:
  about: []
  author: ''
  description: 'TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating
    Alleged Compromise, TeamPCP Runs Dual Ransomware Operations, and AstraZeneca Data
    Released, Author: Kenneth Hartman'
  headline: 'TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating
    Alleged Compromise, TeamPCP Runs Dual Ransomware Operations, and Ast...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32846
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'TeamPCP Supply Chain Campaign: Update 004 - Databricks Investigating Alleged
  Compromise, TeamPCP Runs Dual Ransomware Operations, and AstraZeneca Data Released,
  (Mon, Mar 30th)'
updated_at: '2026-04-02T12:15:15.782557+00:00'
url_hash: 43804885e9f461509903936ccc3a0389cff8c44e
---

This is the fourth update to the TeamPCP supply chain campaign threat intelligence report,
["When the Security Scanner Became the Weapon"](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
(v3.0, March 25, 2026). Update 003 covered developments through March 28, including the first 48-hour pause in new compromises and the campaign's shift to monetization. This update consolidates intelligence from March 28-30, 2026 -- two days since our last update.

## HIGH: Databricks Investigating Alleged Compromise Linked to TeamPCP Credential Harvest

[CybersecurityNews](https://cybersecuritynews.com/databricks-teampcp-supply-chain/amp/)
reports that Databricks, the cloud data analytics platform, is investigating an alleged security compromise linked to the TeamPCP credential harvest. International Cyber Digest
[stated on X](https://x.com/IntCyberDigest/status/2038552600375648701)
that they "notified them last week" and Databricks "scaled up to investigate." A separate analyst corroborated that screenshots showing AWS artifacts, CloudFormation dumps, and STS tokens "match TeamPCP's exact playbook."

Databricks has not issued an official statement. If confirmed, this would be the first major cloud platform identified as a downstream victim of TeamPCP's credential trove -- distinct from the security tool vendors (Aqua, Checkmarx, BerriAI, Telnyx) directly compromised in the supply chain phase. The distinction matters: tool vendor compromises expanded TeamPCP's credential pool, while a Databricks compromise would represent the monetization of that pool against an enterprise target processing sensitive data across AWS, GCP, and Azure.


***U*
pdate (2026-03-30):**
Databricks' Head of Global Communications and their external PR agency FGS Global have confirmed the authenticity of the new @DatabricksSec X account.  In their https://x.com/DatabricksSec/status/2038649955401794042, Databricks says they "thoroughly investigated this information in our internal systems and found nothing" and have "asked for more information beyond this screenshot." They state they will "transparently continue to share any new updates on all security matters."

**Recommended action:**
Organizations using Databricks should monitor for an official statement. If your CI/CD pipelines were exposed to any TeamPCP-compromised component AND those pipelines had access to Databricks credentials, treat those credentials as potentially compromised regardless of whether Databricks confirms the breach.

## HIGH: TeamPCP Operates Dual Ransomware Tracks - CipherForce Is Their Own Operation

Update 002 documented TeamPCP's partnership with the Vect ransomware-as-a-service operation and BreachForums mass affiliate key distribution. New intelligence reveals that Vect is not TeamPCP's only ransomware channel.

According to
[Flare](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware)
and corroborated by
[Rami McCarthy's IOC tracker](https://ramimac.me/teampcp/)
, TeamPCP operates under five confirmed aliases:
**PCPcat, ShellForce, DeadCatx3, CipherForce, and Persy\_PCP**
. TeamPCP's own Telegram channel states: "you may already know us as TeamPCP or Shellforce... CipherForce is a newer project we are starting to find affiliates."

**CipherForce is TeamPCP's own ransomware operation**
, separate from the Vect partnership. This means TeamPCP is running two parallel ransomware tracks simultaneously: their proprietary CipherForce program for direct operations, and the mass Vect affiliate program via BreachForums for distributed operations. The
[SANS ISC Stormcast for March 30](https://isc.sans.edu/podcastdetail/9870)
also notes "more and more links between the TeamPCP crew and various ransomware actors" -- plural -- consistent with this dual-track model.

Analysts assess this dual-track approach allows TeamPCP to maintain direct control over high-value targets (via CipherForce) while simultaneously flooding the ecosystem with mass affiliate operations (via Vect). The 300 GB stolen credential trove can feed both tracks simultaneously.

**Recommended action:**
Detection teams monitoring for Vect ransomware indicators should also add CipherForce to their watchlist. The strongest attribution link across all TeamPCP operations is a shared RSA-4096 public key embedded in payloads -- search for this key in forensic artifacts from any suspected TeamPCP exposure.

## HIGH: LAPSUS$ Releases AstraZeneca Data Free After Failed Sale Attempt

The LAPSUS$/AstraZeneca breach claim documented in Updates 002-003 has escalated.
[Cybernews](https://cybernews.com/security/astrazeneca-hackers-claim-source-code-breach/)
and
[Cybersecurity Insiders](https://www.cybersecurity-insiders.com/lapsus-hackers-disclose-more-about-astrazeneca-data-breach/)
report two developments:

1. **LAPSUS$ released the claimed 3 GB archive for free**
   after failing to find buyers via Session encrypted messaging. This shifts the incident from an extortion attempt to a full data exposure event.
2. **Cybernews research team has partially verified the dump's contents**
   -- GitHub user information for internal AstraZeneca software developers, employee data spanning clinical research subsidiaries, and internal source code tree structures were assessed as consistent with legitimate AstraZeneca infrastructure.

AstraZeneca has still not issued any public statement confirming or denying the breach at approximately 96 hours since the initial claim. Analysts assess that AstraZeneca's continued silence, combined with GDPR obligations if EU employee data is in the dump, creates increasing regulatory exposure with each passing day.

**Recommended action:**
Organizations should treat this as a probable confirmed breach for defensive planning purposes. If your organization shares integrations, data, or credentials with AstraZeneca, assess whether the exposed repository structures and configurations could affect your security posture. Given AstraZeneca's clinical research operations, the dump may contain protected health information (PHI) subject to HIPAA in the US and GDPR in the EU. Organizations with data-sharing agreements with AstraZeneca should evaluate whether their data may be in the exposed archive and prepare breach notification workflows accordingly.

## MEDIUM: ownCloud Discloses Build Infrastructure Impact From CVE-2026-33634

[ownCloud](https://central.owncloud.org/t/security-notice-impact-of-cve-2026-33634-on-owncloud-build-infrastructure/65655)
published a security notice confirming their build infrastructure -- the systems producing container images and client binaries -- was affected by CVE-2026-33634 (the Trivy compromise). ownCloud confirms: no customer data compromised, no source code altered, impact limited to build systems only.

This is one of the first named downstream organizations to publicly disclose that they were in the blast radius of the Trivy supply chain compromise. The disclosure is notable for its transparency -- most affected organizations have remained silent despite the CISA KEV entry and federal remediation deadline of April 8.

**Recommended action:**
Organizations using ownCloud should review the security notice and verify their deployments are using images produced after the remediation. More broadly, ownCloud's disclosure should prompt other organizations that used Trivy in their build pipelines between March 19-22 to conduct their own impact assessments and consider similar disclosure.

## MEDIUM: Supply Chain Pause Extends Past 96 Hours

No new package compromises across any ecosystem have been publicly reported since the Telnyx PyPI disclosure on March 27, extending the supply chain pause documented in Update 003 past 96 hours. This is the longest quiet period since TeamPCP began active supply chain operations on March 19.

**Expanded ecosystem search results (March 30):**
An independent search of RubyGems,
[crates.io](http://crates.io)
, and Maven Central -- the three ecosystems identified as plausible expansion targets in Update 003 -- found
**zero TeamPCP-related IOCs**
in any of them. The RubyGems,
[crates.io](http://crates.io)
, and Maven Central watch items remain "Not observed." While the CanisterWorm's propagation technique is registry-agnostic (any stolen publish token would work), there is no evidence TeamPCP has moved beyond the five confirmed ecosystems (GitHub Actions, PyPI, npm, Docker Hub/GHCR, OpenVSX).

**Note on sourcing:**
CybersecurityNews listed "NPM and OpenVSX" alongside the other compromised ecosystems in their Databricks article. These are accurate in the sense that both ecosystems were hit, but they refer to the known CanisterWorm npm worm (March 20, 66+ packages) and the Checkmarx OpenVSX extensions (March 23, ast-results and cx-dev-assist) -- not new compromises. No new npm or OpenVSX activity has been documented since the original incidents.

**Recommended action:**
Use this supply chain pause as a remediation window. The CISA KEV deadline for CVE-2026-33634 is now
**9 days away**
(April 8, 2026). Complete credential rotations and IOC sweeps before the deadline.

## HIGH: Campaign Transitions to Three Parallel Monetization Tracks

While supply chain poisoning has paused, TeamPCP is not dormant. Analysts assess the group has completed its supply chain expansion phase and transitioned fully to credential exploitation and monetization. Three distinct operational tracks are now running simultaneously:

1. **Direct credential exploitation**
   against high-value targets -- the Databricks investigation (see above) represents the first alleged downstream victim of the ~300 GB stolen credential trove, distinct from the tool vendors directly compromised in the supply chain phase.
2. **Proprietary ransomware via CipherForce**
   -- TeamPCP's own ransomware operation, with recruitment via their Telegram channel. No confirmed deployments yet, but the infrastructure and affiliate recruitment are active.
3. **Mass affiliate ransomware via Vect/BreachForums**
   -- Distributed operations leveraging the BreachForums mass affiliate key distribution documented in Update 002. The distribution window is now ~96 hours with no confirmed deployments.

The distinction between these tracks matters for defenders: detection teams monitoring for Vect ransomware indicators should also add CipherForce to their watchlist. The shared RSA-4096 public key embedded in payloads is the strongest attribution link across all TeamPCP operations.

## INFO: Cloud Security Alliance Publishes Second Research Note on AI/ML Supply Chain Risk

The
[Cloud Security Alliance AI Safety Initiative](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-pypi-supply-chain-campaign-20260329-csa/)
published a research note on March 29 framing the TeamPCP campaign as a structural shift in adversary methodology -- from opportunistic typosquatting to deliberate pipeline compromise of trusted AI/ML packages. The note assesses that "the economics of targeting high-value AI credential stores are accelerating adversary investment." This is the second CSA publication covering TeamPCP (the first was the Kubernetes wiper lab analysis documented in Update 003) and focuses specifically on the AI/ML ecosystem implications rather than technical TTPs.

## Watch Item Status

| Watch Item | Status |
| --- | --- |
| Vect ransomware first confirmed deployment | **No confirmed deployments** -- Distribution window now ~96 hours |
| CipherForce ransomware first confirmed deployment | **NEW WATCH ITEM** -- TeamPCP's own ransomware operation, no confirmed deployments yet |
| Databricks official statement | **NEW WATCH ITEM** -- Investigation acknowledged via third parties, no official disclosure |
| Additional package compromises breaking 96-hour pause | **No new compromises** -- Longest pause since campaign began |
| AstraZeneca confirmation or denial | **Escalated** -- Data released free, Cybernews partially verified, still no official statement at ~96 hours |
| Mandiant formal attribution report | **Pending** -- BerriAI engagement confirmed, no public report |
| CISA standalone advisory | **Pending at day 12** -- KEV entries only, no dedicated advisory or emergency directive |
| Expansion to RubyGems, [crates.io](http://crates.io) , Maven Central | **Not observed** -- Independent registry search on Mar 30 found zero TeamPCP IOCs in all three. Separate unrelated malicious crate campaigns found on [crates.io](http://crates.io) (polymarket typosquats, time-utility exfiltrators) but no TeamPCP attribution |
| NPM/OpenVSX new activity | **No new activity** -- CybersecurityNews listing refers to known CanisterWorm (npm, Mar 20) and Checkmarx extensions (OpenVSX, Mar 23), not new compromises |
| LiteLLM/BerriAI release resumption | **Pending** -- Release freeze continues, last safe version v1.82.6.rc.2 |
| Law enforcement action | **No public action** -- No arrests, indictments, or infrastructure seizures at day 12 |
| CISA KEV deadline compliance (April 8) | **9 days remaining** |

The full campaign report is available at
[sans.org/white-papers/when-security-scanner-became-weapon](https://www.sans.org/white-papers/when-security-scanner-became-weapon)
. A SANS Emergency Webcast replay is available at
[sans.org/webcasts/when-security-scanner-became-weapon](https://www.sans.org/webcasts/when-security-scanner-became-weapon)
. Updates to the report will be in the form of these ISC diaries.