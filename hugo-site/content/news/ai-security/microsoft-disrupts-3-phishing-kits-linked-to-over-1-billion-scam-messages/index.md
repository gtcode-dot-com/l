---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T04:02:37.612325+00:00'
exported_at: '2026-10-15T04:02:39.862484+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/microsoft-disrupts-3-phishing-kits.html
structured_data:
  about: []
  author: ''
  description: Microsoft and partners disrupted CoGUI, Haozi, and Iron Man, phishing
    kits linked to more than 1 billion messages since January 2026.
  headline: Microsoft Disrupts 3 Phishing Kits Linked to Over 1 Billion Scam Messages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/microsoft-disrupts-3-phishing-kits.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Disrupts 3 Phishing Kits Linked to Over 1 Billion Scam Messages
updated_at: '2026-10-15T04:02:37.612325+00:00'
url_hash: 78b0d9b2dfa117c3a73cc06145b37d273d7ebbc4
---

Microsoft and Health-ISAC, along with the Japan Cybercrime Control Center (JC3) and a coalition of private sector companies, such as Resecurity, Cloudflare, Oracle, Proofpoint, and TRM Labs, announced the disruption of three phishing kits,
**CoGUI**
(aka NX or FA),
**Haozi**
(aka Phoenix), and
**Iron Man System**
.

"Since January 2026, the threat actors behind these kits have been responsible for facilitating the sending of over one billion phishing emails and SMS messages to over 75 thousand organizations worldwide," the Microsoft Threat Intelligence and Microsoft Digital Crimes Unit
[said](https://www.microsoft.com/en-us/security/blog/2026/10/14/the-hidden-network-inside-the-phishing-infrastructure-ecosystem-powering-global-cybercrime/)
.

The court-authorized operation is the result of an investigation that Microsoft launched in late 2025 after it was notified of malicious messaging campaigns targeting people in Japan. The

The Chinese-language cybercriminal ecosystem has been described as an interconnected network of phishing kit operators, developers, and an illicit marketplace and initial access broker (IAB) codenamed YAM Store that peddles tools and infrastructure using compromised or fraudulently obtained Microsoft or Google environments for large-scale phishing attacks.

Microsoft is tracking the underground marketplace as Storm-3119 and the developers behind all three phishing kits as Storm-2990. Evidence indicates that the three kits overlap in capabilities and infrastructure, suggesting shared development origins, code reuse, or close collaboration among their Chinese-speaking developers.

As is the case with any phishing-as-a-service (PhaaS or PaaS) platform, the end goal is to provide phishing templates impersonating legitimate brands and organizations spanning government, financial, and logistics sectors worldwide, and enable high-volume phishing and credential stealing operations.

"These messages have been used to target consumers, healthcare organizations, financial institutions, and other businesses in more than 150 countries, generating tens of millions of dollars for their operators," Health-ISAC
[said](https://health-isac.org/disrupting-the-service-economy-behind-transnational-cybercrime-operations/)
.

Threat actors are said to have purchased these phishing kits, along with access to compromised or fraudulent Microsoft or Google cloud environments, to target organizations across the healthcare, financial services, wholesale distribution, and information technology (IT) sectors in Japan, the U.S., Australia, and India.

"These phishing kits have been advertised through YAM Store, first CoGUI and Haozi, followed by Iron Man System starting in June 2026," Microsoft said. "YAM Store and affiliated phishing kit companies accepted payments through cryptocurrency, including USDT and Ethereum, adding another layer to conceal illicit activity."

YAM Store also occupies a central place in the operations, as it advertises legitimate infrastructure associated with legitimate, expired, or previously used organizations that other cybercriminals can purchase to attack their targets.

Some of the notable aspects of Storm-3119's tradecraft are listed below -

* Use of automation to identify expired environment or organization names, profile cloud-enabled organizations, and discover Microsoft 365 tenants. The reconnaissance phase occurs anonymously through Tor infrastructure.
* Take over viable environments and manage them using app-only administrative panels implemented in PHP, Java/Spring, and Cloudflare Workers.
* Establish presence within the compromised tenant, grant itself broad Microsoft Graph permissions and full control over the SharePoint API, and abuse the tenant's SharePoint and OneDrive as bulk hosting and turn the hijacked storage into a sellable product.
* Maintain dedicated infrastructure to support and oversee phishing operations on behalf of their customers.
* Resell hijacked accounts, licenses, and storage through an automated storefront.
* Sell phishing kits tracked as Storm-2990 to facilitate theft of sign-in credentials and financial data.

CoGUI, as
[detailed](https://thehackernews.com/2025/05/employees-searching-payroll-portals-on.html)
by Proofpoint in May 2025, has been observed
[targeting Japanese organizations](https://www.jc3.or.jp/news/2026/20261014-718.html)
by impersonating well-known consumer and finance brands such as Amazon, PayPay, MyJCB, Apple, Orico, and Rakuten. The kit is said to have been used in real-world campaigns since at least October 2024.

The phishing kit, per the enterprise security company, has also
[spawned](https://www.proofpoint.com/us/blog/threat-insight/disruption-targets-major-chinese-language-phishing-kits-japanese-focus)
two closely related variants named CoAceV and CoFish\_Ws. In total, around 17,000 unique domains have been used by the three kits. By mid-2026, CoGUI was being increasingly replaced by Iron Man System, according to
[TRM Labs](https://www.trmlabs.com/resources/blog/trm-supports-takedown-of-chinese-language-cybercrime-ecosystem-with-microsoft-health-isac-and-others)
.

The Iron Man System features more than 2,335 phishing templates that are tailored to impersonate trusted brands and organizations across 139 countries, including Australia, Japan, India, and the U.S., while taking steps to restrict access to phishing content to only users from specific countries.

Resecurity, which purchased a license and deployed the kit in an isolated lab,
[said](https://www.resecurity.com/blog/article/iron-man-yamstore-powering-a-global-phishing-as-a-service-ecosystem)
it supports 2,360 distinct phishing lure packages impersonating postal, tax, banking, telecom and loyalty-programme brands across 130 countries and regions. It also said it located a self-hosted Git and container-registry server containing 911 builds for the admin panel from October 2025 through June 2026.

The cybersecurity company also found that the kit requires regular contact with the vendor's licensing server to function, "a dependency that favors defenders, since disabling or sinkholing the authorization host would degrade every active deployment, not just the one under investigation."

Other advanced evasion techniques employed by the kits include fake CAPTCHA gates to filter out automated browsing sessions, IP-based block list and allow list, and Telegram-based alerts that notify the kit operator when a victim acts on a phishing lure.

The sensitive information entered on the phishing site is captured using a WebSocket, allowing the operators to monitor their progress in real-time and decide what their targets see next. The stolen financial information is used by downstream actors to make fraudulent purchases of high-end goods or fraudulent transactions on legitimate financial platforms.

"What began with scam activity targeting people and organizations in Japan led investigators to an underground service economy supplying criminals around the world," Steven Masada, associate general counsel and general manager of Microsoft's Digital Crimes Unit,
[said](https://blogs.microsoft.com/on-the-issues/2026/10/14/disrupting-the-service-economy-behind-transnational-cybercrime-operations/)
.

"YAM Store, CoGUI and Iron Man are only part of that larger criminal network, but disrupting them makes it harder for criminals to obtain the accounts, tools and infrastructure they rely on. The scam message is often the only part victims see. The businesses behind it are what make it possible."

The development comes less than a month after it
[announced](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html)
the takedown of the EvilTokens device code phishing service that it said used artificial intelligence (AI) "at every step of the attack chain."