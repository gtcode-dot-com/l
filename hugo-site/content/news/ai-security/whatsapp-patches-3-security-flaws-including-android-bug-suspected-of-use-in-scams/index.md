---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-21T00:36:18.524900+00:00'
exported_at: '2026-11-21T00:36:19.871018+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html
structured_data:
  about: []
  author: ''
  description: WhatsApp fixed three security flaws, including an Android IP exposure
    bug suspected of abuse in scam messages.
  headline: WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of
    Use in Scams
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in
  Scams
updated_at: '2026-11-21T00:36:18.524900+00:00'
url_hash: 6cc616c5c6e76f971a0e2bcbe54a9b1f6084cddf
---

**

Ravie Lakshmanan
**

Nov 20, 2026

Vulnerability / Mobile Security

Meta-owned WhatsApp has
[addressed](https://www.whatsapp.com/security/advisories/2026/)
security vulnerabilities, including one impacting its Android app that it suspects may have been exploited in connection with scam messages.

The vulnerability, tracked as
**CVE-2026-23871**
, has been described as a case of incomplete validation of external ad-reply URLs in WhatsApp for Android and WhatsApp Business for Android before 2.26.17.4.

The issue could have "caused a target's device to reveal its IP information to an attacker if an attacker sent media from an attacker-controlled URL when a crafted
[Click to WhatsApp](https://whatsappbusiness.com/products/ads-that-click-to-whatsapp/)
ad-reply message was rendered and displayed in a message thread," WhatsApp said.

The messaging platform said it may have been "abused in conjunction with specific spam messages." Internal researchers on the WhatsApp Security Team have been credited with discovering and reporting the issue.

When reached for comment, a WhatsApp spokesperson told The Hacker News that the vulnerability was discovered while disrupting a scam campaign. "We believe a scammer was using it to make their scam message seem more credible," the spokesperson added.

WhatsApp did not disclose the scale of the activity, and if those efforts were successful.

Also addressed by the company are two other flaws -

* **CVE-2026-102769**
  - An SQL injection vulnerability in WhatsApp for Android prior to version 2.26.35.74 that occurred when a recipient tapped on a specially crafted "order details" message sent from an unofficial client, causing locally-stored WhatsApp files to be deleted.
* **CVE-2026-44908**
  - A trust-validation vulnerability in WhatsApp's certificate verification mechanism for Meta AI's confidential computing infrastructure that affects WhatsApp for iOS before 2.26.24.72, WhatsApp Business for iOS and WhatsApp for Mac Desktop before v2.26.23.72, WhatsApp for Android before v2.26.23.74, and WhatsApp Business for Android before v2.26.23.70.

Interestingly, CVE-2026-102769 is also capable of leaking one bit of information through a timing-based side channel if the user is online at the time of receipt of the malicious message.

It "leaked one bit of information asked by the attacker about the user's chat database via an induced-crash delivery receipt timing side channel," WhatsApp added. There is no evidence the vulnerability has been exploited in the wild.

Successful exploitation of CVE-2026-44908, on the other hand, could have allowed a bad actor positioned within Meta infrastructure to bypass the hardware root of trust using a Versioned Chip Endorsement Key (
[VCEK](https://docs.amd.com/api/khub/documents/U5H~LHvkigTowyppBkpyrA/content)
) certificate not signed by the hardware manufacturer's key.

"Any such VCEK Cert would first have to be published to the third-party binary transparency ledger used by WhatsApp Private Processing," WhatsApp noted. "The ledger shows that every published VCEK certificate chains to the hardware root of trust, confirming no exploitation."

WhatsApp is advising users to keep their apps and devices up to date to ensure optimal protection. The company also said that it continuously works to strengthen its systems and acknowledged the bug bounty community's contributions towards keeping the platform secure.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.