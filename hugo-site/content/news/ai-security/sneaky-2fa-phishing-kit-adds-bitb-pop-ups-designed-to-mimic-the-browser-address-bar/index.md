---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-19T01:01:25.073650+00:00'
exported_at: '2025-11-19T01:01:27.617558+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html
structured_data:
  about: []
  author: ''
  description: Sneaky 2FA adds BitB phishing and attackers exploit passkey flaws using
    rogue extensions and downgrade attacks.
  headline: Sneaky 2FA Phishing Kit Adds BitB Pop-ups Designed to Mimic the Browser
    Address Bar
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Sneaky 2FA Phishing Kit Adds BitB Pop-ups Designed to Mimic the Browser Address
  Bar
updated_at: '2025-11-19T01:01:25.073650+00:00'
url_hash: 3dbca5323c2d4a4636d7b8d3aa4e290531eb5af8
---

The malware authors associated with a Phishing-as-a-Service (PhaaS) kit known as
[Sneaky 2FA](https://thehackernews.com/2025/01/new-sneaky-2fa-phishing-kit-targets.html)
have incorporated Browser-in-the-Browser (BitB) functionality into their arsenal, underscoring the continued evolution of such offerings and further making it easier for less-skilled threat actors to mount attacks at scale.

Push Security, in a
[report](https://pushsecurity.com/blog/analyzing-the-latest-sneaky2fa-phishing-page)
shared with The Hacker News, said it observed the use of the technique in phishing attacks designed to steal victims' Microsoft account credentials.

BitB was
[first documented](https://thehackernews.com/2022/03/new-browser-in-browser-bitb-attack.html)
by security researcher mr.d0x in March 2022, detailing how it's possible to leverage a combination of HTML and CSS code to create fake browser windows that can masquerade as login pages for legitimate services in order to
[facilitate credential theft](https://thehackernews.com/2025/04/microsoft-warns-of-tax-themed-email.html)
.

"BitB is principally designed to mask suspicious phishing URLs by simulating a pretty normal function of in-browser authentication – a pop-up login form," Push Security said. "BitB phishing pages replicate the design of a pop-up window with an iframe pointing to a malicious server."

To complete the deception, the pop-up browser window shows a legitimate Microsoft login URL, giving the victim the impression that they are entering the credentials on a legitimate page, when, in reality, it's a phishing page.

In one attack chain observed by the company, users who land on a suspicious URL ("previewdoc[.]us") are served a Cloudflare Turnstile check. Only after the user passes the bot protection check does the attack progress to the next stage, which involves displaying a page with a "Sign in with Microsoft" button in order to view a PDF document.

Once the button is clicked, a phishing page masquerading as a Microsoft login form is loaded in an embedded browser using the BitB technique, ultimately exfiltrating the entered information and session details to the attacker, who can then use them to take over the victim's account.

Besides using bot protection technologies like CAPTCHA and Cloudflare Turnstile to prevent security tools from accessing the phishing pages, the attackers leverage
[conditional loading techniques](https://phishing-techniques.pushsecurity.com/techniques/conditional-loading/)
to ensure that only the intended targets can access them, while filtering out the rest or redirecting them to benign sites instead.

Sneaky 2FA, first highlighted by Sekoia earlier this year, is known to adopt various methods to resist analysis, including using obfuscation and disabling browser developer tools to prevent attempts to inspect the web pages. In addition, the phishing domains are
[quickly rotated](https://www.centripetal.ai/threat-research/typhoon-versus-sneaky)
to minimize detection.

"Attackers are continuously innovating their phishing techniques, particularly in the context of an increasingly professionalized PhaaS ecosystem," Push Security said. "With identity-based attacks continuing to be the leading cause of breaches, attackers are incentivized to refine and enhance their phishing infrastructure."

The disclosure comes against the backdrop of research that
[found](https://labs.sqrx.com/passkeys-pwned-0dbddb7ade1a)
that it's possible to employ a malicious browser extension to fake passkey registration and logins, thereby allowing threat actors to access enterprise apps without the user's device or biometrics.

The Passkey Pwned Attack, as it's called, takes advantage of the fact that there is no secure communication channel between a device and the service and that the browser, which serves as the intermediary, can be manipulated by means of a rogue script or extension, effectively hijacking the authentication process.

When registering or authenticating on websites using passkeys, the website communicates via the web browser by invoking WebAuthn APIs such as navigator.credentials.create() and navigator.credentials.get(). The attack manipulates these flows through JavaScript injection.

"The malicious extension intercepts the call before it reaches the authenticator and generates its own attacker-controlled key pair, which includes a private key and a public key," SquareX said. "The malicious extension stores the attacker-controlled private key locally so it can reuse it to sign future authentication challenges on the victim's device without generating a new key."

A copy of the private key is also transmitted to the attacker to permit them to access enterprise apps on their own device. Similarly, during the login phase, the call to "navigator.credentials.get()" is intercepted by the extension to sign the challenge with the attacker's private key created during registration.

That's not all. Threat actors have also found a way to sidestep phishing-resistant authentication methods like passkeys by means of what's known as a downgrade attack, where adversary-in-the-middle (AitM) phishing kits like
[Tycoon](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)
can ask the victim to choose between a less secure option that's phishable instead of allowing them to use a passkey.

"So, you have a situation where even if a phishing-resistant login method exists, the presence of a less secure backup method means the account is still vulnerable to phishing attacks," Push Security
[noted](https://pushsecurity.com/blog/mfa-downgrade-attacks/)
back in July 2025.

As attackers continue to hone their tactics, it's essential that users exercise vigilance before opening suspicious messages or installing extensions on the browser. Organizations can also adopt conditional access policies to prevent account takeover attacks by restricting logins that don't meet certain criteria.