---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T05:59:04.366906+00:00'
exported_at: '2026-10-07T05:59:05.623817+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html
structured_data:
  about: []
  author: ''
  description: A human-operated phishing platform impersonates AI ad tools to capture
    credentials and MFA codes through browser-in-the-browser login windows.
  headline: Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA
    Codes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA Codes
updated_at: '2026-10-07T05:59:04.366906+00:00'
url_hash: ec14eeb066a7343525b2b91828c399941207c2cf
---

Cybersecurity researchers have disclosed details of a "human-operated phishing platform" that impersonates advertising products for artificial intelligence (AI) chatbots like Google Gemini, Anthropic Claude, OpenAI ChatGPT, Perplexity, Meta Muse, and Manus.

The products, which claim to offer campaign optimization, spend audits, and business-account connections, are designed with one goal in mind: to capture credentials and multi-factor authentication (MFA) codes via spoofed login windows using the browser-in-the-browser (
[BitB](https://thehackernews.com/2022/03/new-browser-in-browser-bitb-attack.html)
) trick.

"Each product was built around the same action: Connect," Island researchers Oleg Zaytsev and Ofek Ronen
[said](http://www.island.io/blog/behind-the-connect-button-the-fake-ai-ads-campaign)
in a report shared with The Hacker News. "Clicking it opened a browser drawn inside the real browser. The fake address bar displayed trusted origins such as accounts.google.com or an Okta tenant, while the real browser remained on the phishing domain."

"Behind the interface, the platform kept every password attempt, fingerprinted the device, and let an operator pick which MFA challenge the victim saw next."

One of the websites in question is "museads.ai," which emerged on September 16, 2026, a little over a week after Meta launched
[Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
, its AI agent designed for personal workflows. Described as "Your AI ads manager for paid media workflows," the platform claimed to help customers reach buyers, connect their ad accounts, and run sponsored placements.

Prominently placed in the spoofed web page is a Prompt Box with a "Connect" button, clicking which triggers a BitB attack to capture a visitor's account credentials for Google, Meta, TikTok, and Okta workflows. This is accomplished by drawing a fake window displaying a bogus account sign-in form with the address bar pointing to a legitimate domain (e.g., accounts.google[.]com).

In the background, the victim's device is fingerprinted, and the information is transmitted to the attacker at the endpoint "/api/send/ip" over Socket.IO, after which operator commands and victim data are exchanged based on the login workflow. Armed with the account credentials, the attacker attempts to sign in to the account in real-time.

"Every brand gets its own pitch," the researchers explained. "ChatGPT promises a Monday Google Ads brief. Gemini promises MCC (manager account) and linked-client support. Claude gets its own advertising portal, Perplexity offers campaign planning and spend audits, and Manus offers a private Meta integration."

Users are
[assessed](https://ironscales.com/threat-intelligence/gemini-ads-beta-invite-attacker-built-bulk-mail-compliance-kit)
to be
[directed](https://research.intezer.com/blog/2026/08/when-the-whole-company-adopts-ai/)
to these landing pages via fake invitation emails that impersonate these trusted brands to lend the attacks a veneer of legitimacy.

"Each one in this campaign poses as a believable product, with its own brand, pitch, and sign-in flow," the researchers pointed out. "They also move with the news."

Island said the AI ads pages are part of a broader phishing platform that supports a three-pronged operation, the two others being Google Ads-themed refund claims and payment confirmation, as well as recruitment-related sites for Tesla, Louis Vuitton, Nike, and Adecco.

All the identified websites have been found to share the same technology stack comprising Next.js and Socket.IO, and communicate with the same endpoints. What's more, the threat actors behind the operation have exposed source code for earlier versions of the platform through misconfigured public GitHub repositories.

The AI ads-focused campaign is designed to target agency staff, media buyers, and manager-account administrators, likely with the end goal of monetizing the ads accounts to run their own ad campaigns or sell them for profit, especially when they have a clean spend history.

According to a report
[published](https://www.mimecast.com/threat-intelligence-hub/ad-account-theft/)
by Mimecast in July 2026, malware families like VietCredCare, DuckTail, NodeStealer, and PXA Stealer have engendered ad account theft at scale, leading to a "widespread commodity crime in the advertising ecosystem" where bad actors drain business budgets and sell accounts with good reputation in underground markets.

"For the victim, the card is the easy part: they can remove it within hours. Getting the account back is not," Island said. "Attackers typically add their own administrators and downgrade the legitimate owner, and recovery can take weeks or months while the account keeps serving ads. For a manager account, the damage reaches the agency’s clients."

To mitigate the threat, organizations are recommended to enable phishing-resistant authentication, review advertising control changes, and scrutinize AI integrations before connecting accounts.

The disclosure comes as Island revealed that threat actors are abusing Google-sponsored results to route unsuspecting users to
[custom GPTs or shared-AI chat content](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html)
, which then redirect them to a fake Cloudflare verification page serving ClickFix-style lures to deliver NetSupport RAT.

"The campaign did not require a vulnerability in ChatGPT or Google," Island
[said](https://www.island.io/blog/how-attackers-use-sponsored-search-custom-gpts-in-malware-delivery)
. "It abused trusted platforms, attacker-authored content, paid search, and social engineering to move people toward malware delivery."

"Across a three-month observation period ending in August 2026, the broader delivery cluster included about 850 paid-ad landings, 26 lookalike ChatGPT destinations, and 71 Google Ads campaign IDs."