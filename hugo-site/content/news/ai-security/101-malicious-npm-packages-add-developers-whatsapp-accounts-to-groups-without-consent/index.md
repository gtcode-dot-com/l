---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:16:09.514781+00:00'
exported_at: '2026-10-07T01:16:12.024394+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html
structured_data:
  about: []
  author: ''
  description: 101 npm packages in PhantomSub abuse Baileys to add WhatsApp users
    to groups without consent, with 490,000 downloads in total.
  headline: 101 Malicious npm Packages Add Developers' WhatsApp Accounts to Groups
    Without Consent
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 101 Malicious npm Packages Add Developers' WhatsApp Accounts to Groups Without
  Consent
updated_at: '2026-10-07T01:16:09.514781+00:00'
url_hash: c27b3357c720aeab9696a0df7ae5490f057276ac
---

**

Ravie Lakshmanan
**

Sep 29, 2026

Supply Chain / Malware

Cybersecurity researchers have identified a cluster of 101 npm packages that are used to trap developers into a WhatsApp group subscriber campaign dubbed
**PhantomSub**
.

"The malicious packages abuse the 'Baileys' WhatsApp open source project to add the victims to groups without their consent," OX Security researchers Nir Zadok, Moshe Siman Tov Bustan, and Vitalii Chepurko
[said](https://www.ox.security/blog/phantomsub-malicious-npm-campaign-secretly-adds-users-to-whatsapp-spam-channels/)
in a technical write-up published Monday.

These packages have been collectively downloaded 490,000 times, out of which 116,000 occurred in the last 30 days. The names of some of the packages are below -

* ourin-baileys
* @nexustechpro/baileys
* @badzz88/baileys
* @ostyado/baileys
* levvleys
* @vanzxy/baileys
* @yudzxml/baileys
* @chatunity/baileys
* @kelvdra/baileys
* neuralwhatsapp
* lilys-baileys
* @fyxzpediaa/baileys
* noxleyss
* @xrelly-stack/bails
* alipclutch-baileys
* kurobails
* eliteprotech-baileys
* @xayz/baileys
* chromestaff-baileys
* @sanzoffc/baileys
* @sairidev/baileys-new
* cloud-baileys
* @nyzzpediaa/baileys-new
* ishumdz-bail
* nishiki-bail
* diezyclutch-baileys
* oktz-baileys
* my-auto-follow

Details of the activity first emerged in August 2026, when SafeDep
[said](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)
it identified a set of Baileys npm forks that were found to engage in malicious behaviors, such as stealthily making the installer's WhatsApp account follow channels the package author controls and injecting the author's advertising URL into every image and video the bot sends.

Then, earlier this month, the Xygeni Security Research Team disclosed details of another Baileys mod named "
[@dappaoffc/baileys-mod](https://xygeni.io/blog/malicious-npm-package-in-baileys-fork-skyzopedia-case/)
" that was also found to subscribe the developer's authenticated WhatsApp bot session to attacker-controlled newsletter channels.

OX Security's analysis has uncovered three different variants of the malware, each implementing different ways of handling the subscription routine -

* Variant 1 (19 packages), which fetches channel IDs from GitHub at runtime
* Variant 2 (60 packages), which embeds channel IDs in its source code in cleartext
* Variant 3 (14 packages), which embeds channel IDs in its source code in encoded and obfuscated form

One of the WhatsApp groups is assessed to be based in Indonesia and advertises accounts for mobile games and applications, such as Mobile Legends: Bang Bang and TikTok. These posts also specify a phone number that's linked to an Indonesian business WhatsApp account named "Dan."

Some of the other identified groups and channels are listed below -

* Neural (798 followers), which markets Resource Supplies (RSS) sales using JualanRSS, an online marketplace that sells in-game resources such as food, ore, stone, timber, and gold.
* MONTE – BMG (1,000 followers)
* CORTANA TECH (1,300 followers)
* Fyxzpedia.ID – Utama (4,800 followers)

"The channels we could identify are mostly small bot-seller and 'market' channels, largely Indonesian, where follower counts serve as social proof for selling bot scripts, bot-building services, 'premium' APKs and social-media boosting," OX Security said.

"Many packages in this campaign are not independent. The same channel IDs, the same remote channel lists, and the same GitHub accounts appear across packages with different names and publishers. A shared channel means a shared beneficiary: whoever owns the channel collects followers from every package that targets it, whoever published the package."

Developers are advised to check if they have been added to the WhatsApp groups, block them, configure detection rules for blocking the malicious npm Baileys packages, and refrain from using packages that require the personal WhatsApp account to be connected.