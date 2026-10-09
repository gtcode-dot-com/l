---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-14T06:49:15.045624+00:00'
exported_at: '2025-11-14T06:49:16.331599+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/russian-hackers-create-4300-fake-travel.html
structured_data:
  about: []
  author: ''
  description: Hackers built 4,300 fake travel sites in 2025 to steal hotel guests’
    card data using real brand logos.
  headline: Russian Hackers Create 4,300 Fake Travel Sites to Steal Hotel Guests'
    Payment Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/russian-hackers-create-4300-fake-travel.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Russian Hackers Create 4,300 Fake Travel Sites to Steal Hotel Guests' Payment
  Data
updated_at: '2025-11-14T06:49:15.045624+00:00'
url_hash: 9eb3ade2d207476f4f482bc108a075d2b01163a1
---

A Russian-speaking threat behind an ongoing, mass phishing campaign has registered
[more than 4,300 domain names](https://github.com/netcraftcom/public-iocs/blob/main/2025-11%20hotel%20phishing%20IOCs.csv)
since the start of the year.

The
[activity](https://www.netcraft.com/blog/thousands-of-domains-target-hotel-guests-in-massive-phishing-campaign)
, per Netcraft security researcher Andrew Brandt, is designed to target customers of the hospitality industry, specifically hotel guests who may have travel reservations with spam emails. The campaign is said to have begun in earnest around February 2025.

Of the 4,344 domains tied to the attack, 685 domains contain the name "Booking", followed by 18 with "Expedia," 13 with "Agoda," and 12 with "Airbnb," indicating an attempt to target all popular booking and rental platforms.

"The ongoing campaign employs a sophisticated phishing kit that customizes the page presented to the site visitor depending on a unique string in the URL path when the target first visits the website," Brandt said. "The customizations use the logos from major online travel industry brands, including Airbnb and Booking.com."

The attack begins with a phishing email urging recipients to click on a link to confirm their booking within the next 24 hours using a credit card. Should they take the bait, the victims are taken to a fake site instead after initiating a chain of redirects. These bogus sites follow consistent naming patterns for their domains, featuring phrases like confirmation, booking, guestcheck, cardverify, or reservation to give them an illusion of legitimacy.

The pages support 43 different languages, allowing the threat actors to cast a wide net. The page then instructs the victim to pay a deposit for their hotel reservation by entering their card information. In the event that any user directly attempts to access the page without a unique identifier called AD\_CODE, they are greeted with a blank page. The bogus sites also feature a fake CAPTCHA check that mimics Cloudflare to deceive the target.

"After the initial visit, the AD\_CODE value is written to a cookie, which ensures that subsequent pages present the same impersonated branding appearance to the site visitor as they click through pages," Netcraft said. This also means that changing the "AD\_CODE" value in the URL produces a page targeting a different hotel on the same booking platform.

As soon as the card details, along with the expiration data and CVV number, are entered, the page attempts to process a transaction in the background, while an "support chat" window appears on the screen with steps to complete a supposed "3D Secure verification for your credit card" to secure against fake bookings.

The identity of the threat group behind the campaign remains unknown, but the use of Russian for source code comments and debugger output either alludes to their provenance or is an attempt to cater to prospective customers of the phishing kit who may be looking to customize it to suit their needs.

The disclosure comes days after Sekoia
[warned](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)
of a large-scale phishing campaign targeting the hospitality industry that lures hotel managers to ClickFix-style pages and harvest their credentials by deploying malware like PureRAT and then approach hotel customers via WhatsApp or emails with their reservation details and confirm their booking by clicking on a link.

Interestingly, one of the indicators shared by the French cybersecurity company – guestverifiy5313-booking[.]com/67122859 – matches the domain pattern registered by the threat actor (e.g., verifyguets71561-booking[.]com), raising the possibility that these two clusters of activity could be related. The Hacker News has reached out to Netcraft for comment, and we will update the story if we hear back.

In recent weeks, large-scale phishing campaigns have also
[impersonated](https://cyble.com/blog/multi-brand-phishing-campaign-harvests-credentials/)
multiple brands like Microsoft, Adobe, WeTransfer, FedEx, and DHL to steal credentials by distributing HTML attachments through email. The embedded HTML files, once launched, display a fake login page while JavaScript code captures credentials entered by the victim and sends them directly to attacker-controlled Telegram bots, Cyble said.

The campaign has mainly targeted a wide range of organizations across Central and Eastern Europe, particularly in the Czech Republic, Slovakia, Hungary, and Germany.

"The attackers distribute phishing emails posing as legitimate customers or business partners, requesting quotations or invoice confirmations," the company pointed out. "This regional focus is evident through targeted recipient domains belonging to local enterprises, distributors, government-linked entities, and hospitality firms that routinely process RFQs and supplier communications."

Furthermore, phishing kits have been put to use in a large-scale campaign targeting customers of Aruba S.p.A, one of Italy's largest web hosting and IT service providers, in a similar attempt to steal sensitive data and payment information.

The phishing kit is a "fully automated, multi-stage platform designed for efficiency and stealth," Group-IB researchers Ivan Salipur and Federico Marazzi
[said](https://www.group-ib.com/blog/uncover-phishing-italy/)
. "It employs CAPTCHA filtering to evade security scans, pre-fills victim data to increase credibility, and uses Telegram bots to exfiltrate stolen credentials and payment information. Every function serves a single goal: industrial-scale credential theft."

These findings exemplify the growing demand for phishing-as-a-service (PhaaS) offerings in the underground economy, enabling threat actors with little to no technical expertise to pull off attacks at scale.

"The automation observed in this particular kit exemplifies how phishing has become systematized – faster to deploy, harder to detect, and easier to replicate," the Singaporean company added. "What once required technical expertise can now be executed at scale through pre-built, automated frameworks."