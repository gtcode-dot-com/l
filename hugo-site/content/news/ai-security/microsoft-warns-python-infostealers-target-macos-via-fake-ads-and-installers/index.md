---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-04T10:15:14.402199+00:00'
exported_at: '2026-02-04T10:15:17.092963+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/microsoft-warns-python-infostealers.html
structured_data:
  about: []
  author: ''
  description: Python infostealers are spreading from Windows to macOS via Google
    Ads, ClickFix lures, and fake installers to steal credentials and financial data.
  headline: Microsoft Warns Python Infostealers Target macOS via Fake Ads and Installers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/microsoft-warns-python-infostealers.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Warns Python Infostealers Target macOS via Fake Ads and Installers
updated_at: '2026-02-04T10:15:14.402199+00:00'
url_hash: 354cd85681a0c7311334b7561df74c2eb13a4cad
---

**

Ravie Lakshmanan
**

Feb 04, 2026

Malvertising / Infostealer

Microsoft has warned that information-stealing attacks are "rapidly expanding" beyond Windows to target Apple macOS environments by leveraging cross-platform languages like Python and abusing trusted platforms for distribution at scale.

The tech giant's Defender Security Research Team said it observed macOS-targeted infostealer campaigns using social engineering techniques such as
[ClickFix](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)
since late 2025 to distribute disk image (DMG) installers that deploy stealer malware families like Atomic macOS Stealer (
[AMOS](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html)
),
[MacSync](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html)
, and
[DigitStealer](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploited-chinas.html#:~:text=New%20DigitStealer%20macOS%20Malware%20Spotted)
.

The campaigns have been found to use techniques like fileless execution, native macOS utilities, and AppleScript automation to facilitate data theft. This includes details like web browser credentials and session data, iCloud Keychain, and developer secrets.

The starting point of these attacks is often a malicious ad, often served through Google Ads, that redirects users searching for tools like DynamicLake and artificial intelligence (AI) tools to fake sites that employ ClickFix lures, tricking them into infecting their own machines with malware.

"Python-based stealers are being leveraged by attackers to rapidly adapt, reuse code, and target heterogeneous environments with minimal overhead," Microsoft
[said](https://www.microsoft.com/en-us/security/blog/2026/02/02/infostealers-without-borders-macos-python-stealers-and-platform-abuse/)
. "They are typically distributed via phishing emails and collect login credentials, session cookies, authentication tokens, credit card numbers, and crypto wallet data."

One such stealer is
[PXA Stealer](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html)
, which is linked to Vietnamese-speaking threat actors and is capable of harvesting login credentials, financial information, and browser data. The Windows maker said it identified two PXA Stealer campaigns in October 2025 and December 2025 that used phishing emails for initial access.

Attack chains involved the use of registry Run keys or scheduled tasks for persistence and Telegram for command-and-control communications and data exfiltration.

In addition, bad actors have been observed weaponizing popular messaging apps like WhatsApp to distribute malware like
[Eternidade Stealer](https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html)
and gain access to financial and cryptocurrency accounts. Details of the campaign were publicly documented by LevelBlue/Trustwave in November 2025.

Other stealer-related attacks have revolved around fake PDF editors like Crystal PDF that are distributed via malvertising and search engine optimization (SEO) poisoning through Google Ads to deploy a Windows-based stealer that can stealthily collect cookies, session data, and credential caches from Mozilla Firefox and Chrome browsers.

To counter the threat posed by infostealer threats, organizations are advised to educate users on social engineering attacks like malvertising redirect chains, fake installers, and ClickFix‑style copy‑paste prompts. It's also advised to monitor for suspicious Terminal activity and access to the iCloud Keychain, as well as inspect network egress for POST requests to newly registered or suspicious domains.

"Being compromised by infostealers can lead to data breaches, unauthorized access to internal systems, business email compromise (BEC), supply chain attacks, and ransomware attacks," Microsoft said.