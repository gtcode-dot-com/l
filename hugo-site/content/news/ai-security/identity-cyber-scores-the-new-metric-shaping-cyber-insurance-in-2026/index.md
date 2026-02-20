---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-20T16:15:17.875393+00:00'
exported_at: '2026-02-20T16:15:20.218390+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/identity-cyber-scores-new-metric.html
structured_data:
  about: []
  author: ''
  description: Insurers tighten cyber underwriting as identity risks grow; breach
    costs hit $4.4M and MFA gaps affect payouts.
  headline: 'Identity Cyber Scores: The New Metric Shaping Cyber Insurance in 2026'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/identity-cyber-scores-new-metric.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Identity Cyber Scores: The New Metric Shaping Cyber Insurance in 2026'
updated_at: '2026-02-20T16:15:17.875393+00:00'
url_hash: 4dc6c5e3ae344b3d581ebd1a0106e9fec8ba25ba
---

**

The Hacker News
**

Feb 20, 2026

Cyber Insurance / Password Security

With
[one in three cyber-attacks](https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/2025-threat-intelligence-index)
now involving compromised employee accounts, insurers and regulators are placing far greater emphasis on identity posture when assessing cyber risk.

For many organizations, however, these assessments remain largely opaque. Elements such as password hygiene, privileged access management, and the extent of multi-factor authentication (MFA) coverage are increasingly influential in how cyber risk and
[insurance costs](https://specopssoft.com/blog/why-you-need-cyber-insurance/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
are evaluated.

Understanding the identity-centric factors behind these assessments is critical for organizations seeking to demonstrate lower risk exposure and secure more favorable insurance terms.

## Why identity posture now drives underwriting

With the
[global average cost](https://www.ibm.com/reports/data-breach)
of a data breach reaching $4.4 million in 2025, more organizations are turning to cyber insurance to manage financial exposure. In the UK, coverage has increased from
[37%](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2023/cyber-security-breaches-survey-2023)
in 2023 to
[45%](https://www.gov.uk/government/statistics/cyber-security-breaches-survey-2025/cyber-security-breaches-survey-2025)
in 2025, but rising claims volumes are prompting insurers to tighten underwriting requirements.

Credential compromise remains one of the most reliable ways for attackers to gain access,
[escalate privileges](https://specopssoft.com/blog/active-directory-privilege-escalation/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
, and persist within an environment. For insurers, strong
[identity controls](https://specopssoft.com/blog/identity-verification-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
reduce the likelihood that a single compromised account can lead to widespread disruption or data loss, supporting more sustainable underwriting decisions.

## What insurers want to see in identity security

### Password hygiene and credential exposure

Despite the growing use of multi-factor authentication and
[passwordless initiatives](https://specopssoft.com/blog/considerations-when-going-passwordless/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
, passwords still play a key role in authentication. Organizations should pay particular attention to the behaviors and issues that increase the risk of credential theft and abuse, including:

* **Password reuse across identities**
  , particularly among administrative or
  [service accounts](https://specopssoft.com/blog/service-account-security-best-practices/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
  , increases the likelihood that one stolen credential leads to broader access.
* **Legacy authentication protocols**
  are still common in networks and frequently abused to harvest credentials. NTLM persists in many environments despite being functionally replaced by
  [Kerberos](https://specopssoft.com/blog/kerberoasting-attacks-in-active-directory/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
  in Windows 2000.
* **Dormant accounts**
  with valid credentials, which act as unmonitored entry points and often retain unnecessary access.
* **Service accounts**
  with
  [never-expiring passwords](https://specopssoft.com/blog/microsoft-password-expiration-recommendation/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
  , creating long-lived, low-visibility attack paths.
* **Shared administrative credentials**
  , reduce accountability and amplify the impact of compromise.

From an underwriting perspective, evidence that an organization understands and actively manages these risks is often more important than the presence of individual technical controls.
[Regular audits of password hygiene](https://specopssoft.com/product/specops-password-auditor/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
and credential exposure help demonstrate maturity and intent to reduce identity-driven risk.

### Privileged access management

[Privileged access management](https://specopssoft.com/blog/secure-privileged-accounts-keep-business-secrets-belong/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
is a critical measure of an organization’s ability to prevent and mitigate breaches. Privileged accounts can have high-level access to systems and data, but are frequently over-permissioned. As a result, insurers pay close attention to how these accounts are governed.

Service accounts, cloud administrators, and delegated privileges outside central monitoring significantly elevate risk. This is especially true when they operate without
[MFA or logging](https://specopssoft.com/blog/mfa-phishing-fatigue-resistant/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
.

Excessive membership in Domain Admin or Global Administrator roles and overlapping administrative scopes all suggest that privilege escalation would be both rapid and difficult to contain.

Poorly governed or unknown privileged access is typically viewed as higher risk than a small number of tightly controlled administrators. Security teams can use tools such as
[Specops Password Auditor](https://specopssoft.com/product/specops-password-auditor/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
to identify stale, inactive, or over-privileged administrative accounts and prioritize remediation before those credentials are abused.

|  |
| --- |
|  |
| Specops Password Auditor - Dashboard |

When determining the likelihood of a damaging breach, the question is straightforward: if an attacker
[compromises a single account](https://specopssoft.com/blog/business-email-compromise/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
, how quickly can they become an administrator? Where the answer is “immediately” or “with minimal effort,” premiums tend to reflect that exposure.

### MFA coverage

Most organizations can credibly state that
[MFA has been deployed.](https://specopssoft.com/product/specops-secure-access/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
However, MFA only meaningfully reduces risk when it is consistently enforced across all critical systems and accounts. In one documented case, the
[City of Hamilton](https://specopssoft.com/blog/mfa-failure-costs-hamilton-cyber-insurance/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
was denied an $18 million cyber insurance payout after a ransomware attack because MFA had not been fully implemented across affected systems.

While
[MFA isn’t infallible](https://specopssoft.com/blog/mfa-alone-not-enough-protect-passwords-and-logon/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
, fatigue attacks first require valid account credentials and then depend on a user approving an unfamiliar authentication request, an outcome that is far from guaranteed.

Meanwhile, accounts that authenticate via older protocols, non-interactive service accounts, or privileged roles exempted for convenience all offer viable bypass paths once initial access is achieved.

That’s why insurers increasingly require MFA for all privileged accounts, as well as for email and remote access. Organizations that neglect it may face higher premiums.

## Four steps to improve your identity cyber score

There are many ways organizations can improve identity security, but insurers look for evidence of progress in a few key areas:

1. **Eliminate weak and shared passwords:**
   Enforce minimum password standards and
   [reduce password reuse](https://specopssoft.com/blog/password-reuse-hidden-danger/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
   , particularly for administrative and service accounts. Strong password hygiene limits the impact of credential theft and reduces the risk of lateral movement following initial access.
2. **Apply MFA across all critical access paths:**
   [Ensure MFA is enforced](https://specopssoft.com/blog/keep-mfa-running-during-identity-service-disruptions/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
   on remote access, cloud applications, VPNs, and all privileged accounts. Insurers increasingly expect MFA coverage to be comprehensive rather than selectively applied.
3. **Reduce permanent privileged access:**
   [Limit permanent administrative rights](https://specopssoft.com/blog/six-ways-to-apply-the-principle-of-least-privilege-to-your-active-directory/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
   wherever practical and adopt just-in-time or time-bound access for elevated tasks. Fewer always-on privileged accounts directly reduce the impact of credential compromise.
4. **Regularly review and certify access:**
   Conduct routine reviews of user and privileged permissions to ensure they align with current roles.
   [Stale access](https://specopssoft.com/blog/stale-user-accounts-report-in-active-directory/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
   and orphaned accounts are common red flags in insurance assessments.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPoDaw7Z6Ha_RsUGENuvMiqsO9o58t3YfnTi-sZf8PRLfkH5_NY2PKSFhfdzDH_ai16nDvqSiblDnOys-h3VFO61Ak3Wvu18cQzrEEWuvqkSDRxUB6fkIOcINgznwcspn18htBvnoO6LF7dlIVkGC9XYsbW-GthL8q6lCQnUVmYnFk7128pyD51EBZpy-9/s1600/2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPoDaw7Z6Ha_RsUGENuvMiqsO9o58t3YfnTi-sZf8PRLfkH5_NY2PKSFhfdzDH_ai16nDvqSiblDnOys-h3VFO61Ak3Wvu18cQzrEEWuvqkSDRxUB6fkIOcINgznwcspn18htBvnoO6LF7dlIVkGC9XYsbW-GthL8q6lCQnUVmYnFk7128pyD51EBZpy-9/s1600/2.png)

Insurers increasingly expect organizations to demonstrate not only that identity controls exist, but that they are actively monitored and improved over time.

[Specops Password Auditor](https://specopssoft.com/product/specops-password-auditor/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
supports this by providing clear visibility into password exposure within Active Directory and enforcing controls that reduce credential-based risk.

To understand how these controls can be applied in your environment and aligned with insurer expectations,
[speak with a Specops expert](https://specopssoft.com/contact-us/?utm_source=thehackernews&utm_medium=referral&utm_campaign=thehackernews_referral_na&utm_content=article)
or request a live demo.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.