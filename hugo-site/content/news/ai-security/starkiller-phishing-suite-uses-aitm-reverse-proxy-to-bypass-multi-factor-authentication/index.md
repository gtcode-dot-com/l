---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-04T00:15:15.753892+00:00'
exported_at: '2026-03-04T00:15:18.068501+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html
structured_data:
  about: []
  author: ''
  description: Starkiller phishing suite uses live reverse proxying to bypass MFA,
    while attackers abuse OAuth device codes to hijack Microsoft 365 accounts.
  headline: Starkiller Phishing Suite Uses AitM Reverse Proxy to Bypass Multi-Factor
    Authentication
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Starkiller Phishing Suite Uses AitM Reverse Proxy to Bypass Multi-Factor Authentication
updated_at: '2026-03-04T00:15:15.753892+00:00'
url_hash: a2a4288c7e9590630fb2ed370c45c1a45df1ed9a
---

Cybersecurity researchers have disclosed details of a new phishing suite called
**Starkiller**
that proxies legitimate login pages to bypass multi-factor authentication (MFA) protections.

It's advertised as a cybercrime platform by a threat group calling itself Jinkusu, granting customers access to a dashboard that lets them select a brand to impersonate or enter a brand's real URL. It also lets users choose custom keywords like "login," "verify," "security," or "account," and integrates URL shorteners such as TinyURL to obscure the destination URL.

"It launches a
[headless Chrome instance](https://developer.chrome.com/docs/chromium/headless)
– a browser that operates without a visible window – inside a
[Docker container](https://www.docker.com/resources/what-container/)
, loads the brand's real website, and acts as a reverse proxy between the target and the legitimate site," Abnormal researchers Callie Baron and Piotr Wojtyla
[said](https://abnormal.ai/blog/starkiller-phishing-kit)
.

"Recipients are served genuine page content directly through the attacker's infrastructure, ensuring the phishing page is never out of date. And because Starkiller proxies the real site live, there are no template files for security vendors to fingerprint or blocklist."

This login page proxying technique obviates the need for attackers to update their phishing page templates periodically as the real pages they're impersonating get updated.

Put differently, the container acts as an AitM reverse proxy, forwarding the end user's inputs entered on the spoofed live page to the legitimate site and returning the site's responses. Under the hood, every keystroke, form submission, and session token is routed through attacker-controlled infrastructure and is captured for account takeover.

"The platform streamlines phishing operations by centralizing infrastructure management, phishing page deployment, and session monitoring within a single control panel," Abnormal said. "Combined with URL masking, session hijacking, and MFA bypass, it gives low-skill cybercriminals access to attack capabilities that were previously out of reach."

The development comes as Datadog revealed that the 1Phish kit had evolved from a basic credential harvester in September 2025 into a multi-stage phishing kit targeting 1Password users.

The updated version of the kit incorporates a pre-phishing fingerprint and validation layer, support for capturing one-time passcodes (OTPs) and recovery codes, and browser fingerprinting logic to filter out bots.

"This progression reflects deliberate iteration rather than simple template reuse," security researcher Martin McCloskey
[said](https://securitylabs.datadoghq.com/articles/hook-line-vault-a-deep-dive-into-1phish/)
. "Each version builds upon the previous one, introducing controls designed to increase conversion rates, reduce automated analysis, and support secondary authentication harvesting."

The findings show that turkey solutions like Starkiller and 1Phish are increasingly turning phishing into SaaS-style workflows, further lowering the skill barrier necessary to pull off such attacks at scale.

They also coincide with a sophisticated phishing campaign targeting North American businesses and professionals by abusing the OAuth 2.0 device authorization grant flow to sidestep multi-factor authentication (MFA) and compromise Microsoft 365 accounts.

To achieve this, the attacker registers on the Microsoft OAuth application and generates a unique
[device code](https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html)
, which is then delivered to the victim via a targeted phishing email.

"The victim is directed to the legitimate Microsoft domain (microsoft.com/devicelogin) portal to enter an
[attacker-supplied device code](https://blog.knowbe4.com/what-is-device-code-phishing)
," researchers Jeewan Singh Jalal, Prabhakaran Ravichandhiran, and Anand Bodke
[said](https://blog.knowbe4.com/uncovering-the-sophisticated-phishing-campaign-bypassing-m365-mfa)
. "This action authenticates the victim and issues a valid OAuth access token to the attacker's application. The real-time theft of these tokens grants the attacker persistent access to the victim's Microsoft 365 accounts and corporate data."

In recent months, phishing campaigns have also targeted financial institutions, specifically U.S.-based banks and credit unions, to harvest credentials. The campaign is said to have taken place over two distinct phases, an initial wave beginning in late June 2025 and a more sophisticated set of attacks beginning in mid-November 2025.

"The actors began registering [.]co[.]com domains spoofing financial institution websites, presenting credible impersonations of real financial institutions," BlueVoyant researchers Shira Reuveny and Joshua Green
[said](https://www.bluevoyant.com/blog/multi-stage-phishing-campaign-targets-finance)
. "These [.]co[.]com domains serve as the initial entry point in a refined multi-stage chain."

The domain, when visited from a clickable link in a phishing email, is designed to load a fraudulent Cloudflare CAPTCHA page that mimics the targeted institution. The CAPTCHA is non-functional and creates a deliberate delay before a Base64-encoded script redirects users to the credential harvesting page.

In an effort to evade detection and prevent automated scanners from flagging the malicious content, directly accessing the [.]co[.]com domains trigger a redirect to a malformed "www[.]www" URL.

"The adversary's deployment of a more advanced multi-layered evasion chain – incorporating referrer validation, cookie-based access controls, intentional delays, and code obfuscation – effectively creates a more resilient infrastructure that presents barriers for automated security tools and manual analysis," BlueVoyant said.