---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-02T02:15:14.520359+00:00'
exported_at: '2026-05-02T02:15:17.766072+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html
structured_data:
  about: []
  author: ''
  description: 30,000 Facebook accounts hacked via AppSheet phishing emails, exploiting
    Meta lures, leading to large-scale account theft and resale.
  headline: 30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign
updated_at: '2026-05-02T02:15:14.520359+00:00'
url_hash: c964fa83825effcbd727aee06505b41cab0b7c7e
---

**

Ravie Lakshmanan
**

May 01, 2026

Malware / Threat Intelligence

A newly discovered Vietnamese-linked operation has been observed using a Google AppSheet as a "phishing relay" to distribute phishing emails with an aim to compromise Facebook accounts.

The activity has been codenamed
**AccountDumpling**
by Guardio, with the scheme selling the stolen accounts back through an illicit storefront run by the threat actors. In all, roughly 30,000 Facebook accounts are estimated to have been hacked as part of the campaign.

"What we found wasn't a single phishing kit," security researcher Shaked Chen
[wrote](https://guard.io/labs/accountdumpling---hunting-down-the-google-sent-phishing-wave-compromising-30-000-facebook-accounts)
in a report shared with The Hacker News. "It was a living operation with real-time operator panels, advanced evasion, continuous evolution and a criminal-commercial loop that quietly feeds on the same accounts it helps steal back."

The findings are just the latest example of how
[Vietnamese threat actors](https://thehackernews.com/2025/05/fake-kling-ai-facebook-ads-deliver-rat.html)
continue to
[embrace various tactics](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html)
to gain unauthorized access to victims' Facebook accounts, which are then sold on underground ecosystems for monetary gain.

The starting point of the latest attacks is a phishing email targeting Facebook Business account owners, claiming to be from Meta Support and urging them to submit an appeal, or risk getting their account permanently deleted. The emails are sent from a Google AppSheet address ("noreply@appsheet.com"), allowing them to bypass spam filters.

This false sense of urgency is used to direct users to a fake web page designed to harvest their credentials. It's worth noting that a
[similar campaign](https://thehackernews.com/2025/05/cybercriminals-clone-antivirus-site-to_4.html)
was reported by KnowBe4 in May 2025.

Over the past few weeks, these campaigns have adopted various kinds of lures designed to induce a "Meta-related panic." These range from account disablement and copyright complaints to verification review, executive recruitment, and Facebook login alerts. The four main clusters identified by Guardio are listed below -

* Netlify-hosted Facebook help center pages that enable account takeover attacks, in addition to collecting dates of birth, phone numbers, and government-issued ID photos. The data is ultimately forwarded to an attacker-controlled Telegram channel.
* Blue badge evaluation lures that guide victims to Vercel-hosted "Security Check" or "Meta | Privacy Center" pages that are gated by a bogus CAPTCHA check before directing users to the phishing landing page to collect contact details, business information, credentials (after a forced retry), and two-factor authentication (2FA) codes and exfiltrate them to a Telegram channel.
* Google Drive-hosted PDFs masquerading as instructions to complete account verification to direct users to collect passwords, 2FA codes, government ID photos, and browser screenshots through html2canvas. The PDF documents are generated using a free Canva account.
* Fake job offers that impersonate companies like WhatsApp, Meta, Adobe, Pinterest, Apple, and Coca-Cola to build rapport with the recipients and ask them to join a call or continue the discussion on attacker-controlled sites.

Cumulatively, the Telegram channels associated with the first three clusters have been found to hold about 30,000 victim records, most of whom are located in the U.S., Italy, Canada, the Philippines, India, Spain, Australia, the U.K., Brazil, and Mexico, and have been locked out of their own accounts.

As for who is behind the operation, the smoking gun evidence has come from the PDFs generated as part of the third cluster using the free Canva account, with metadata listing a Vietnamese name "PHẠM TÀI TÂN" as the files' author. Further open-source intelligence has led to the discovery of a website ("phamtaitan[.]vn"), where they offer digital marketing services.

In a post shared on X in February 2023, the website's handle
[said](https://x.com/phamtaitanvn/status/1623563864456720384)
it "specializes in providing digital marketing services, marketing resources, and consulting on effective digital marketing strategies."

"Taken together, they form a consistent picture of a large, Vietnamese-based, mega operation," Chen said. "This campaign is bigger than a single AppSheet abuse. It's a window into the dark market around stolen Facebook assets, where access, business identity, ad reputation, and even account recovery have all become tradable commodities. Another entry in the pattern we keep surfacing: trusted platforms repurposed as delivery, hosting, and monetization layers."