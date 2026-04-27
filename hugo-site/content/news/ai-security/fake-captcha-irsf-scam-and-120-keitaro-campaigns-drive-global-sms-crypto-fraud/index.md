---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-27T10:15:14.292308+00:00'
exported_at: '2026-04-27T10:15:16.497575+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html
structured_data:
  about: []
  author: ''
  description: Fake CAPTCHA IRSF scam sends up to 60 SMS messages since June 2020,
    exploiting 17 countries and costing victims $30 per attack.
  headline: Fake CAPTCHA IRSF Scam and 120 Keitaro Campaigns Drive Global SMS, Crypto
    Fraud
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake CAPTCHA IRSF Scam and 120 Keitaro Campaigns Drive Global SMS, Crypto Fraud
updated_at: '2026-04-27T10:15:14.292308+00:00'
url_hash: 86b430883ddc05b2ebb34414fd5dd1c7127c178e
---

Cybersecurity researchers have disclosed details of a telecommunications fraud campaign that uses fake CAPTCHA verification tricks to dupe unsuspecting users into sending international text messages that incur charges on their mobile bills, generating illicit revenue for the threat actors who lease the phone numbers.

According to a new report published by Infoblox, the operation is believed to have been active since at least June 2020, using methods like social engineering and
[back button hijacking](https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html#crackdown-on-navigation-abuse)
in web browsers. As many as 35 phone numbers spanning 17 countries have been observed as part of the international revenue share fraud (
[IRSF](https://www.ndss-symposium.org/ndss-paper/understanding-and-detecting-international-revenue-share-fraud/)
) campaign.

"The fake CAPTCHA has multiple steps, and each message crafted by the site is preconfigured with over a dozen phone numbers, meaning the victim isn't charged for just a single message – they're charged for sending SMSs to over 50 international destinations," researchers David Brunsdon and Darby Wise
[said](https://www.infoblox.com/blog/threat-intelligence/hold-the-phone-international-revenue-share-fraud-driven-by-fake-captchas/)
in an analysis.

"This type of scam also benefits from delayed billing, as the 'international SMS' charges often appear on the victim's bill weeks later and the experience with the fake CAPTCHA has been long forgotten."

What makes the threat notable is the coming together of revenue share fraud and malicious traffic distribution systems (
[TDSs](https://unit42.paloaltonetworks.com/detect-block-malicious-traffic-distribution-systems/)
), with the activity using the infrastructure -- traditionally responsible for routing traffic to malware or phishing pages though a redirection chain to evade detection – to conduct SMS scams at scale.

IRSF schemes involve fraudsters illegally acquiring international premium rate numbers (IPRN) or number ranges and artificially inflating the volume of international calls or messages to those numbers to receive a share of the revenue generated from these calls from termination charges obtained by the number range holder for inbound traffic to the number ranges.

In this context, a termination fee refers to the inter-carrier charges paid by an originating telecom operator to a terminating operator for completing a call on their network. It's the exploitation of these "revenue sharing" agreements that drives IRSF, as the originating carrier ends up paying termination fees to the destination network for the incoming calls to the high-cost destinations, a portion of which is split with the fraudsters.

Infoblox said the observed campaign specifically registers phone numbers in countries with high termination fees or lax regulations, such as Azerbaijan, Kazakhstan, or certain premium-rate number ranges in Europe, and colludes with local telecom providers to pull off the scam.

The entire campaign plays out like this: a user is redirected to a bogus web page using a commercial TDS, which serves a CAPTCHA that instructs them to send an SMS to "confirm you are human."This, in turn, triggers a multi-stage "verification" chain, with each step triggering a separate SMS message to the server-designated numbers by programmatically launching the SMS apps on both Android and iOS devices with the phone numbers and message content pre-filled.

In the process, as many as 60 SMS messages are sent to 15 unique numbers after four steps of CAPTCHA, which could end up costing a user $30. While it may be a relatively small amount, the DNS threat intelligence firm warned that they could quickly add up for the threat actor when carried out at scale. The list of phone numbers spans 17 countries, such as Azerbaijan, the Netherlands, Belgium, Poland, Spain, and Turkey.

The campaign heavily relies on cookies to track progression through the fake verification flow, using values stored in certain cookies (e.g., "successRate") to determine the next course of action.If a user is deemed not suitable for the campaign, the page is designed to redirect them to an entirely different CAPTCHA page that's likely part of a separate campaign or controlled by a different actor.

Another novel strategy adopted by the scam operators is the use of back button hijacking, which relies on JavaScript to alter the browsing history such that any attempt made by the site visitor to navigate away from the CAPTCHA page by hitting the browser's back button redirects the user back to the fake page, effectively trapping them in a navigation loop unless they opt to fully exit the browser.

|  |
| --- |
|  |
| Redirection chain leading to a fake CAPTCHA page |

"This operation defrauds both individuals and telecommunication carriers simultaneously. Individual victims face unexpected premium SMS charges on their bills and would have difficulty identifying and reporting the fraud when it originates from such an unexpected source," Infoblox concluded. "Telecom carriers pay revenue share to the perpetrators while likely absorbing the losses from customer disputes or chargebacks."

### How Threat Actors Abuse Keitaro TDS

The disclosure comes as the company, in collaboration with
[Confiant](https://blog.confiant.com/p/tracking-software-weaponized-by-criminals)
, published a three-part analysis detailing how the
[Keitaro TDS](https://thehackernews.com/2025/02/new-frigidstealer-malware-targets-macos.html)
(aka Keitaro Tracker) is being abused, in some instances by acquiring stolen or cracked licenses (as in the case of
[TA2726](https://thehackernews.com/2025/08/socgholish-malware-spread-via-ad-tools.html)
), by a wide range of threat actors for
[malicious activities](https://www.infoblox.com/blog/threat-intelligence/no-reach-no-risk-the-keitaro-abuse-in-modern-cybercrime-distribution/)
, including malware delivery, cryptocurrency theft, and investment scams that claim to employ artificial intelligence (AI) to automate trading and promise huge returns.

The scam makes use of
[Facebook Ads to lure victims](https://www.infoblox.com/blog/threat-intelligence/inside-keitaro-abuse-a-persistent-stream-of-ai-driven-investment-scams/)
to the fraudulent AI‑powered platforms, in some cases even resorting to fabricating celebrity endorsements pushed via fake news articles and deepfake videos to promote the investment scheme. The use of synthetic videos has been attributed to a threat actor dubbed FaiKast.

"Keitaro is first and foremost a self-hosted advertising performance tracker designed to conditionally route visitors using flows," the companies
[said](https://www.infoblox.com/blog/threat-intelligence/patterns-pirates-and-provider-action-what-we-learned-working-with-keitaro/)
. "Threat actors repurpose this mechanism, transforming a Keitaro server into an all-in-one tool that acts as a traffic distribution system, tracker, and cloaking layer."

|  |
| --- |
|  |
| Distribution of observed spam campaigns utilizing Keitaro |

In all, more than 120 distinct campaigns have abused Keitaro's TDS for link delivery over a four-month period between October 2025 and January 2026. Infoblox noted that its customers recorded about 226,000 DNS queries spanning 13,500 domains associated with Keitaro‑related activity during the timeframe. Following responsible disclosure, Keitaro has stepped in to cancel over a dozen accounts linked to these activities.

"By combining an older but still highly effective investment fraud theme with modern AI technologies, actors have been able to launch large‑scale, highly convincing cyber campaigns," Infoblox and Confiant said. "Approximately 96% of Keitaro‑linked spam traffic promoted cryptocurrency wallet‑drainer schemes, primarily via fake airdrop/giveaway lures centered on AURA, SOL (Solana token), Phantom (wallet), and Jupiter (DEX/aggregator)."