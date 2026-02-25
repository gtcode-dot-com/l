---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-25T05:16:38.447847+00:00'
exported_at: '2026-02-25T05:16:40.571072+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/study-uncovers-25-password-recovery.html
structured_data:
  about: []
  author: ''
  description: Academic study finds 25 attack methods in major cloud password managers
    exposing vault, recovery, and encryption design risks.
  headline: Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/study-uncovers-25-password-recovery.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers
updated_at: '2026-02-25T05:16:38.447847+00:00'
url_hash: 9cf9977f6088522c087b3b53dd2f77610c874101
---

A new study has
[found](https://ethz.ch/en/news-and-events/eth-news/news/2026/02/password-managers-less-secure-than-promised.html)
that multiple cloud-based password managers, including Bitwarden, Dashlane, and LastPass, are susceptible to password recovery attacks under certain conditions.

"The attacks range in severity from integrity violations to the complete compromise of all vaults in an organization," researchers Matteo Scarlata, Giovanni Torrisi, Matilda Backendal, and Kenneth G. Paterson
[said](https://zkae.io)
. "The majority of the attacks allow the recovery of passwords."

It's worth noting that the threat model, per the study from ETH Zurich and Università della Svizzera italiana, supposes a malicious server and aims to examine the password manager's zero-knowledge encryption (ZKE) promises made by the three solutions. ZKE is a cryptographic technique that allows one party to prove knowledge of a secret to another party without actually revealing the secret itself.

ZKE is also a little different from end-to-end encryption (E2EE). While E2EE refers to a method of securing data in transit, ZKE is mainly about storing data in an encrypted format such that only the person with the key can access that information. Password manager vendors are known to implement ZKE to "enhance" user privacy and security by ensuring that the vault data cannot be tampered with.

However, the latest research has uncovered 12 distinct attacks against Bitwarden, seven against LastPass, and six against Dashlane, ranging from integrity violations of targeted user vaults to a total compromise of all the vaults associated with an organization. Collectively, these password management solutions serve over 60 million users and nearly 125,000 businesses.

"Despite vendors' attempts to achieve security in this setting, we uncover several common design anti-patterns and cryptographic misconceptions that resulted in vulnerabilities," the researchers said in an accompanying paper.

The attacks fall under four broad categories -

* Attacks that exploit the "Key Escrow" account recovery mechanism to compromise the confidentiality guarantees of Bitwarden and LastPass, resulting from vulnerabilities in their key escrow designs.
* Attacks that exploit flawed item-level encryption -- i.e., encrypting data items and sensitive user settings as separate objects and often combine with unencrypted or unauthenticated metadata, to result in integrity violations, metadata leakage, field swapping, and key derivation function (
  [KDF](https://en.wikipedia.org/wiki/Key_derivation_function)
  ) downgrade.
* Attacks that exploit sharing features to compromise vault integrity and confidentiality.
* Attacks that exploit backwards compatibility with legacy code that result in downgrade attacks in Bitwarden and Dashlane.

The study also found that 1Password, another popular password manager, is vulnerable to both item-level vault encryption and sharing attacks. However, 1Password has opted to treat them as arising from already known architectural limitations.

|  |
| --- |
|  |
| Summary of attacks (BW stands for Bitwarden, LP for LastPass, and DL for Dashlane) |

When reached for comment, Jacob DePriest, Chief Information Security Officer and Chief Information Officer at 1Password, told The Hacker News that the company's security reviewed the paper in detail and found no new attack vectors beyond those already documented in its publicly available
[Security Design White Paper](https://agilebits.github.io/security-design/)
.

"We are committed to continually strengthening our
[security architecture](https://support.1password.com/1password-security/)
and evaluating it against advanced threat models, including malicious-server scenarios like those described in the research, and evolving it over time to maintain the protections our users rely on," DePriest added.

"For example, 1Password uses
[Secure Remote Password](https://support.1password.com/secure-remote-password/)
(SRP) to authenticate users without transmitting encryption keys to our servers, helping mitigate entire classes of server-side attacks. More recently, we introduced a
[new capability](https://support.1password.com/cs/dns-record/)
for enterprise-managed credentials, which from the start are created and secured to withstand sophisticated threats."

As for the rest, Bitwarden, Dashlane, and LastPass have all implemented countermeasures to mitigate the risks highlighted in the research, with LastPass also planning to harden its admin password reset and sharing workflows to counter the threat posed by a malicious intermediary. There is no evidence that any of these issues has been exploited in the wild.

Specifically, Dashlane has patched an issue where a successful compromise of its servers could have allowed a downgrade of the encryption model used to generate encryption keys and protect user vaults. The issue was fixed by removing support for legacy cryptography methods with Dashlane Extension
[version 6.2544.1](https://support.dashlane.com/hc/en-us/articles/33346483084050-Security-advisory-Cryptography-downgrade-issue)
released in November 2025.

"This downgrade could result in the compromise of a weak or easily guessable Master Password, and the compromise of individual 'downgraded' vault items," Dashlane
[said](https://www.dashlane.com/blog/zero-knowledge-malicious-server)
. "This issue was the result of the allowed use of legacy cryptography. This legacy cryptography was supported by Dashlane in certain cases for backwards compatibility and migration flexibility."

Bitwarden said all identified issues are being addressed. "Seven of which have been resolved or are in active remediation by the Bitwarden team," it
[said](https://bitwarden.com/blog/security-through-transparency-eth-zurich-audits-bitwarden-cryptography/)
. "The remaining three issues have been accepted as intentional design decisions necessary for product functionality."

In a similar advisory, LastPass
[said](https://blog.lastpass.com/posts/details-on-hardening-in-response-to-eth-zurich-reported-security-issues)
it's "actively working to add stronger integrity guarantees to better cryptographically bind items, fields, and metadata, thereby helping to maintain integrity assurance."