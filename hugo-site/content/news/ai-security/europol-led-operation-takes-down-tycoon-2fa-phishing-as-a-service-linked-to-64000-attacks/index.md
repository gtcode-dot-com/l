---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-06T20:36:05.353865+00:00'
exported_at: '2026-03-06T20:36:08.157549+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html
structured_data:
  about: []
  author: ''
  description: Authorities dismantle Tycoon 2FA phishing service linked to 64,000
    attacks, millions of emails, and breaches at nearly 100,000 organizations worldwide
  headline: Europol-Led Operation Takes Down Tycoon 2FA Phishing-as-a-Service Linked
    to 64,000 Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Europol-Led Operation Takes Down Tycoon 2FA Phishing-as-a-Service Linked to
  64,000 Attacks
updated_at: '2026-03-06T20:36:05.353865+00:00'
url_hash: df600d6a1c75ebab9408a41d5cf8629ba3f50073
---

**Tycoon 2FA**
, one of the prominent
[phishing-as-a-service (PhaaS) toolkits](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)
that allowed cybercriminals to stage adversary-in-the-middle (AitM) credential harvesting attacks at scale, was dismantled by a coalition of law enforcement agencies and security companies.

The
[subscription-based phishing kit](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/tycoon2fa-new-evasion-technique-for-2025/)
, which
[first emerged in August 2023](https://www.pointwild.com/threat-intelligence/how-tycoon-2fa-is-rewriting-the-rules-of-identity-theft-not-just-a-phishing-kit-a-business-model/)
, was described by Europol as one of the largest phishing operations worldwide. The kit was sold via Telegram and Signal for a starting price of $120 for 10 days or $350 for access to a web-based administration panel for a month. Tycoon 2FA's primary developer is alleged to be
[Saad Fridi](https://noticeofpleadings.com/tycoon2FA/)
, who is said to be based in Pakistan.

The panel serves as a hub for configuring, tracking, and refining campaigns. It features pre‑built templates, attachment files for common lure formats, domain and hosting configuration, redirect logic, and victim tracking. Operators can also configure how the malicious content is delivered through attachments, as well as keep tabs on valid and invalid sign-in attempts.

The captured information, such as credentials, multi-factor authentication (MFA) codes, and session cookies, can be downloaded directly within the panel or forwarded to Telegram for near‑real‑time monitoring.

"It enabled thousands of cybercriminals to covertly access email and cloud-based service accounts," Europol
[said](https://www.europol.europa.eu/media-press/newsroom/news/global-phishing-service-platform-taken-down-in-coordinated-public-private-action)
. "At scale, the platform generated tens of millions of phishing emails each month and facilitated unauthorized access to nearly 100,000 organizations globally, including schools, hospitals, and public institutions."

As part of the coordinated effort, 330 domains that formed the backbone of the criminal service, including phishing pages and control panels, have been taken down.

Characterizing Tycoon 2FA as "dangerous," Intel 471
[said](https://www.intel471.com/blog/born-to-bypass-mfa-taking-down-tycoon-2fa)
the kit was linked to over 64,000 phishing incidents and
[tens of thousands of domains](https://www.cloudflare.com/threat-intelligence/research/report/tycoon-2fa-takedown/)
, generating tens of millions of phishing emails each month. According to Microsoft, which is tracking the operators of the service under the name Storm-1747, Tycoon 2FA
[became](https://thehackernews.com/2025/11/threatsday-bulletin-ai-malware-voice.html#microsoft-links-13m-phishing-emails-to-top-phaas-operation)
the most prolific platform observed by the company in 2025, prompting it to block more than 13 million malicious emails linked to the crimeware service in October 2025.

In total, Tycoon 2FA accounted for approximately 62% of all
[phishing attempts](https://www.coinbase.com/en-in/blog/coinbase-and-microsoft-disrupt-tycoon-2fa)
blocked by Microsoft as of mid-2025, including more than 30 million emails in a single month. The service has been linked to an estimated 96,000 distinct phishing victims worldwide since 2023, including more than 55,000 Microsoft customers, the tech giant
[added](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/)
.

|  |
| --- |
|  |
| Tycoon 2FA Evolution Timeline (Source: Point Wild) |

Geographic analysis of victim log data by SpyCloud indicates that the U.S. had the largest concentration of identified victims (179,264), followed by the U.K. (16,901), Canada (15,272), India (7,832), and France (6,823).

"The overwhelming majority of targeted accounts were enterprise-managed or otherwise associated with paid domains, reinforcing the conclusion that Tycoon 2FA is primarily directed at business environments rather than individual consumer accounts," the cybersecurity company
[said](https://spycloud.com/blog/tycoon-2fa-takedown-inside-the-global-phishing-infrastructure-disruption/)
.

Data from Proofpoint
[shows](https://www.proofpoint.com/us/blog/threat-insight/disruption-targets-tycoon-2fa-popular-aitm-phaas)
that Tycoon 2FA accounted for the highest volume AiTM phishing threats. The email security company said it observed over three million messages associated with the phishing kit in February 2026 alone. Trend Micro, which was one of the private sector partners in the operation,
[noted that](https://www.trendmicro.com/en_us/research/26/c/tycoon2fa-takedown.html)
the PhaaS platform had approximately 2,000 users.

Campaigns leveraging Tycoon 2FA have indiscriminately targeted almost all sectors, including education, healthcare, finance, non-profit, and government. Phishing emails sent from the kit reached over 500,000 organizations each month worldwide.

"Tycoon 2FA's platform enabled threat actors to impersonate trusted brands by mimicking sign-in pages for services like Microsoft 365, OneDrive, Outlook, SharePoint, and Gmail," Microsoft
[said](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/)
.

"It also allowed threat actors using its service to establish persistence and to access sensitive information even after passwords are reset, unless active sessions and tokens were explicitly revoked. This worked by intercepting session cookies generated during the authentication process, simultaneously capturing user credentials. The MFA codes were subsequently relayed through Tycoon 2FA's proxy servers to the authenticating service."

The kit also employed techniques like keystroke monitoring, anti-bot screening, browser fingerprinting, heavy code obfuscation, self-hosted CAPTCHAs, custom JavaScript, and dynamic decoy pages to sidestep detection efforts. Another key aspect is the use of a broader mix of top-level domains (TLDs) and short-lived fully qualified domain names (FQDNs) to host the phishing infrastructure on Cloudflare.

The FQDNs often only last for 24 to 72 hours, with the rapid turnover a deliberate effort to complicate detection and prevent building reliable blocklists. Microsoft also attributed Tycoon 2FA's success to closely mimicking legitimate authentication processes to stealthily intercept user credentials and session tokens.

To make matters worse, Tycoon 2FA customers leveraged a technique called ATO Jumping, whereby a compromised email account is used to distribute Tycoon 2FA URLs and attempt further account takeover activities. "Using this technique enables emails to look like they are authentically coming from a victim’s trusted contact, increasing the likelihood of a successful compromise," Proofpoint noted.

[Phishing kits](https://securelist.com/phishing-kit-market-whats-inside-off-the-shelf-phishing-packages/106149/)
like Tycoon are designed to be flexible so that it's accessible to less technically savvy actors while still offering advanced capabilities for more experienced operators.

"In 2025, 99% of organizations experienced account takeover attempts in 2025, and 67% experienced a successful account takeover," Selena Larson, staff threat researcher at Proofpoint, said in a statement shared with The Hacker News. "Of these, 59% of the taken-over accounts had MFA enabled. While not all of these attacks were related to Tycoon MFA, this shows the impact of AiTM phishing on enterprises."

"These cyberattacks that enable full account takeovers can lead to disastrous impacts, including ransomware or the loss of sensitive data. As threat actors continue to prioritize identity, gaining access to enterprise email accounts is often the first step in an attack chain that can have destructive consequences."