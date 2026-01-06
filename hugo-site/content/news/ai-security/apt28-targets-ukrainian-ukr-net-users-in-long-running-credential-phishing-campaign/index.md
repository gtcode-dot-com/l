---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-19T04:44:04.148314+00:00'
exported_at: '2025-12-19T04:44:07.575385+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/apt28-targets-ukrainian-ukr-net-users.html
structured_data:
  about: []
  author: ''
  description: APT28 ran a sustained phishing campaign from June 2024 to April 2025,
    using fake UKR.net login pages to steal credentials and 2FA codes.
  headline: APT28 Targets Ukrainian UKR-net Users in Long-Running Credential Phishing
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/apt28-targets-ukrainian-ukr-net-users.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: APT28 Targets Ukrainian UKR-net Users in Long-Running Credential Phishing Campaign
updated_at: '2025-12-19T04:44:04.148314+00:00'
url_hash: b49bb03b0ec487a2c49a8baf7d6fd976bf91ab88
---

**

Dec 17, 2025
**

Ravie Lakshmanan

Email Security / Threat Intelligence

The Russian state-sponsored threat actor known as
**[APT28](https://thehackernews.com/2025/09/russian-apt28-deploys-notdoor-outlook.html)**
has been attributed to what has been described as a "sustained" credential-harvesting campaign targeting users of UKR[.]net, a webmail and news service popular in Ukraine.

The activity, observed by Recorded Future's Insikt Group between June 2024 and April 2025, builds upon
[prior findings](https://thehackernews.com/2024/05/russian-hackers-target-europe-with.html)
from the cybersecurity company in May 2024 that detailed the hacking group's attacks targeting European networks with the HeadLace malware and credential-harvesting web pages.

APT28 is also tracked as BlueDelta, Fancy Bear, Forest Blizzard, FROZENLAKE, Iron Twilight, ITG05, Pawn Storm, Sednit, Sofacy, and TA422. It's assessed to be affiliated with Russia's Main Directorate of the General Staff of the Russian Federation's Armed Forces (GRU).

The latest attacks are characterized by the deployment of UKR[.]net-themed login pages on legitimate services like Mocky to entice recipients into entering their credentials and two-factor authentication (2FA) codes. Links to these pages are embedded within PDF documents that are distributed via phishing emails.

The links are shortened using services like tiny[.]cc or tinyurl[.]com. In some cases, the threat actor has also been observed using subdomains created on platforms like Blogger (\*.blogspot[.]com) to launch a two-tier redirection chain that leads to the credential harvesting page.

The efforts are part of a broader set of phishing and credential theft operations orchestrated by the adversary since mid-2000s targeting government institutions, defense contractors, weapons suppliers, logistics firms, and policy think tanks in pursuit of Russia's strategic objectives.

"While this campaign does not reveal specific targets, BlueDelta's historical focus on credential theft to enable intelligence collection provides strong indicators of likely intent to collect sensitive information from Ukrainian users in support of broader GRU intelligence requirements," the Mastercard-owned company said in a report shared with The Hacker News.

What has changed is the transition from using compromised routers to proxy tunneling services such as ngrok and Serveo to capture and relay the stolen credentials and 2FA codes.

"BlueDelta's continued abuse of free hosting and anonymized tunneling infrastructure likely reflects an adaptive response to
[Western-led infrastructure takedowns](https://thehackernews.com/2024/02/cybersecurity-agencies-warn-ubiquiti.html)
in early 2024," Recorded Future said. "The campaign highlights the GRU's persistent interest in compromising Ukrainian user credentials to support intelligence-gathering operations amid Russia's ongoing war in Ukraine."