---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-24T04:44:16.689752+00:00'
exported_at: '2026-03-24T04:44:19.793497+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/fbi-warns-russian-hackers-target-signal.html
structured_data:
  about: []
  author: ''
  description: Russian-linked phishing hits thousands of messaging accounts via fake
    support tactics, enabling impersonation and data access.
  headline: FBI Warns Russian Hackers Target Signal, WhatsApp in Mass Phishing Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/fbi-warns-russian-hackers-target-signal.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FBI Warns Russian Hackers Target Signal, WhatsApp in Mass Phishing Attacks
updated_at: '2026-03-24T04:44:16.689752+00:00'
url_hash: 5bd06c058b2e52a73eecc68172c6849c94e4d697
---

**

Ravie Lakshmanan
**

Mar 21, 2026

Cyber Espionage / Threat Intelligence

Threat actors affiliated with Russian Intelligence Services are conducting phishing campaigns to compromise commercial messaging applications (CMAs) like WhatsApp and Signal to seize control of accounts belonging to individuals with high intelligence value, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and Federal Bureau of Investigation (FBI)
[said](https://www.cisa.gov/resources-tools/resources/russian-intelligence-services-target-commercial-messaging-application-accounts)
Friday.

"The campaign targets individuals of high intelligence value, including current and former U.S. government officials, military personnel, political figures, and journalists," FBI Director Kash Patel
[said](https://x.com/FBIDirectorKash/status/2035080615435878429)
in a post on X. "Globally, this effort has resulted in unauthorized access to thousands of individual accounts. After gaining access, the actors can view messages and contact lists, send messages as the victim, and conduct additional phishing from a trusted identity."

It's worth noting that the attacks are designed to break into the victims' CMA accounts through phishing and do not exploit any security vulnerability or weakness to crack the platforms' encryption protections. These entail sending messages engineered to create a false sense of urgency by claiming that suspicious account activity or login attempts from an unrecognized device or location have been detected.

While the agencies did not attribute the activity to a specific threat actor, prior reports from Microsoft and Google Threat Intelligence Group have linked such campaigns to multiple Russia-aligned threat clusters tracked as
[Star Blizzard](https://thehackernews.com/2025/01/russian-star-blizzard-shifts-tactics-to.html)
,
[UNC5792 (aka UAC-0195), and UNC4221 (aka UAC-0185)](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html)
.

In a similar alert, the Cyber Crisis Coordination Center (C4), part of the National Cybersecurity Agency of France (ANSSI), warned of a surge in attack campaigns targeting instant messaging accounts associated with government officials, journalists, and business leaders.

"These attacks – when successful – can allow malicious actors to access conversation histories, or even take control of their victims' messaging accounts and send messages while impersonating them," C4
[said](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-003/)
.

The end goal of the campaign is to enable the threat actors to gain unauthorized access to victims' accounts, enabling them to view messages and contact lists, send messages on their behalf, and even conduct secondary phishing against other targets by abusing trusted relationships.

As recently alerted by cybersecurity agencies from
[Germany](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html)
and
[the Netherlands](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html#messaging-account-takeover)
, the attack
[involves](https://www.ic3.gov/PSA/2026/PSA260320)
the adversary posing as "Signal Support" to approach targets and urge them to click on a link (or alternatively scan a QR code) or provide the PIN or verification code. In both cases, the social engineering scheme allows the threat actors to gain access to the victim's CMA account.

However, the campaign has two different outcomes for the victim depending on the method used -

* If the victim opts to provide the PIN or verification code to the threat actor, they lose access to their account, as the attacker has used it to recover the account on their end. While the threat actor cannot access past messages, the method can be used to monitor fresh messages and send messages to others by impersonating the victim.
* If the victim ends up clicking the link or scanning the QR code, a device under the control of the threat actor gets linked to the victim's account, allowing them to access all messages, including those sent in the past. In this scenario, the victim continues to have access to the CMA account unless they are explicitly removed from the app settings.

To better protect against the threat, users are advised to
[never share](https://faq.whatsapp.com/506595211487528)
their
[SMS code or verification PIN with anyone](https://support.signal.org/hc/en-us/articles/9932566320410-Staying-Safe-from-Phishing-Scams-and-Impersonation)
, exercise caution when receiving unexpected messages from unknown contacts, check links before clicking them, and periodically review linked devices and remove those that appear suspicious.

"These attacks, like all phishing, rely on social engineering. Attackers impersonate trusted contacts or services (such as the non-existent 'Signal Support Bot') to trick victims into handing over their login credentials or other information," Signal
[said](https://x.com/signalapp/status/2031038277604585785)
in a post on X earlier this month.

"To help prevent this, remember that your Signal SMS verification code is only ever needed when you are first signing up for the Signal app. We also want to emphasize that Signal Support will \*never\* initiate contact via in-app messages, SMS, or social media to ask for your verification code or PIN. If anyone asks for any Signal-related code, it is a scam."