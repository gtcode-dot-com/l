---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-09T16:15:14.450203+00:00'
exported_at: '2026-01-09T16:15:16.734490+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/russian-apt28-runs-credential-stealing.html
structured_data:
  about: []
  author: ''
  description: Russian-linked APT28 ran credential-harvesting attacks in 2025 using
    fake Microsoft, Google, and VPN login pages, PDF lures, and legitimate web servic
  headline: Russian APT28 Runs Credential-Stealing Campaign Targeting Energy and Policy
    Organizations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/russian-apt28-runs-credential-stealing.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Russian APT28 Runs Credential-Stealing Campaign Targeting Energy and Policy
  Organizations
updated_at: '2026-01-09T16:15:14.450203+00:00'
url_hash: ae26dd60f68e7a3e0c6ed9851a353662c69da843
---

**

Jan 09, 2026
**

Ravie Lakshmanan

Email Security / Threat Intelligence

Russian state-sponsored threat actors have been linked to a fresh set of credential harvesting attacks targeting individuals associated with a Turkish energy and nuclear research agency, as well as staff affiliated with a European think tank and organizations in North Macedonia and Uzbekistan.

The activity has been attributed to APT28 (aka BlueDelta), which was attributed to a "sustained"
[credential-harvesting campaign](https://thehackernews.com/2025/12/apt28-targets-ukrainian-ukr-net-users.html)
targeting users of UKR[.]net last month. APT28 is associated with the Main Directorate of the General Staff of the Armed Forces of the Russian Federation (GRU).

"The use of Turkish-language and regionally targeted lure material suggests that BlueDelta tailored its content to increase credibility among specific professional and geographic audiences," Recorded Future's Insikt Group
[said](https://www.recordedfuture.com/research/gru-linked-bluedelta-evolves-credential-harvesting)
. "These selections reflect a continued interest in organizations connected to energy research, defense cooperation, and government communication networks relevant to Russian intelligence priorities."

The cybersecurity company described the attacks as targeting a small but distinct set of victims in February and September 2025, with the campaign leveraging fake login pages that were styled to resemble popular services like Microsoft Outlook Web Access (OWA), Google, and Sophos VPN portals.

The efforts are noteworthy for the fact that unsuspecting users are redirected to the legitimate sites after the credentials are entered on the bogus landing pages, thereby avoiding raising any red flags. The campaigns have also been found to lean heavily on services like Webhook[.]site, InfinityFree, Byet Internet Services, and ngrok to host the phishing pages, exfiltrate stolen data, and enable redirections.

In a further attempt to lend them a veneer of legitimacy, the threat actors are said to have used legitimate PDF lure documents, including a publication from the Gulf Research Center related to the
[June 2025 Iran-Israel war](https://www.grc.net/documents/68527c604ba00StrategicandPoliticalImplicationsforIsraelandIran2.pdf)
and a July 2025 policy briefing calling for a
[new pact for the Mediterranean](https://eccoclimate.org/climate-action-as-a-strategic-priority-for-the-new-pact-for-the-mediterranean/)
released by climate change think tank ECCO.

The attack chain starts with a phishing email containing a shortened link that, when clicked, redirects victims to another link hosted on webhook[.]site, which briefly displays the decoy document for about two seconds before redirecting to a second webhook[.]site that hosts a spoofed Microsoft OWA login page.

Present within this page is a hidden HTML form element that stores the webhook[.]site URL and uses JavaScript to send a

"page opened" beacon, transmit the submitted credentials to the webhook endpoint, and ultimately redirect back to the PDF hosted on the actual website.

APT28 has also been observed conducting three other campaigns -

* A June 2025 campaign that deployed a credential-harvesting page mimicking a Sophos VPN password reset page hosted on infrastructure provided by InfinityFree to harvest credentials entered into the form and redirect victims to a legitimate Sophos VPN portal belonging to an unnamed E.U. think tank
* A September 2025 campaign that used credential-harvesting pages hosted on InfinityFree domains to falsely warn users of expired passwords to trick them into entering their credentials and redirect to a legitimate login page associated with a military organization in the Republic of North Macedonia and an IT integrator based in Uzbekistan
* An April 2025 campaign that used a fake Google password reset page hosted on Byet Internet Services to gather victims' credentials and exfiltrate them to an ngrok URL

"BlueDelta's consistent abuse of legitimate internet service infrastructure demonstrates the group's continued reliance on disposable services to host and relay credential data," the Mastercard-owned company said. "These campaigns underscore the GRU's sustained commitment to credential harvesting as a low-cost, high-yield method of collecting information that supports Russian intelligence objectives."