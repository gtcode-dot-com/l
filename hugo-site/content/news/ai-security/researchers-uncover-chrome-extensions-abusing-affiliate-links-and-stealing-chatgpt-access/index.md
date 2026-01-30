---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-30T16:15:13.701495+00:00'
exported_at: '2026-01-30T16:15:16.118510+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html
structured_data:
  about: []
  author: ''
  description: Experts uncovered malicious Chrome extensions that replace affiliate
    links, exfiltrate data, and steal ChatGPT authentication tokens from users.
  headline: Researchers Uncover Chrome Extensions Abusing Affiliate Links and Stealing
    ChatGPT Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Uncover Chrome Extensions Abusing Affiliate Links and Stealing
  ChatGPT Access
updated_at: '2026-01-30T16:15:13.701495+00:00'
url_hash: 938654f797a73133c40a93000114e3ede4c51a4e
---

Cybersecurity researchers have discovered malicious Google Chrome extensions that come with capabilities to hijack affiliate links, steal data, and collect OpenAI ChatGPT authentication tokens.

One of the extensions in question is Amazon Ads Blocker (ID: pnpchphmplpdimbllknjoiopmfphellj), which claims to be a tool to browse Amazon without any sponsored content. It was uploaded to the Chrome Web Store by a publisher named "10Xprofit" on January 19, 2026.

"The extension does block ads as advertised, but its primary function is hidden: it automatically injects the developer's affiliate tag (10xprofit-20) into every Amazon product link and replaces existing affiliate codes from content creators," Socket security researcher Kush Pandya
[said](https://socket.dev/blog/malicious-chrome-extension-performs-hidden-affiliate-hijacking)
.

Further analysis has determined that Amazon Ads Blocker is part of a larger cluster of 29 browser add-ons that target several e-commerce platforms like AliExpress, Amazon, Best Buy, Shein, Shopify, and Walmart. The complete list is as follows -

* AliExpress Invoice Generator (FREE) - AliInvoice™️ (10+ Templates) (ID: mabbblhhnmlckjbfppkopnccllieeocp)
* AliExpress Price Tracker - Price History & Alerts (ID: loiofaagnefbonjdjklhacdhfkolcfgi)
* AliExpress Quick Currency & Price Converter (ID: mcaglpclodnaiimhicpjemhcinjfnjce)
* AliExpress Deals Countdown - Flash Sale Timer (ID: jmlgkeaofknfmnbpmlmadnfnfajdlehn)
* 10Xprofit - Amazon Seller Tools (FBA & FBM) (ID: ahlnchhkedmjbdocaamkbmhppnligmoh)
* Amazon Ads Blocker (ID: pnpchphmplpdimbllknjoiopmfphellj)
* Amazon ASIN Lookup 10xprofit (ID: ljcgnobemekghgobhlplpehijemdgcgo)
* Amazon Search Suggestion (ID: dnmfcojgjchpjcmjgpgonmhccibjopnb)
* Amazon Product Scraper 10xprofit (ID: mnacfoefejolpobogooghoclppjcgfcm)
* Amazon Quick Brand Search (ID: nigamacoibifjohkmepefofohfedblgg)
* Amazon Stock Checker 999 (ID: johobikccpnmifjjpephegmfpipfbfme)
* Amazon Price History Saver (ID: kppfbknppimnoociaomjcdgkebdmenkh)
* Amazon ASIN Copy (ID: aohfjaadlbiifnnajpobdhokecjokhab)
* Amazon Keyword Cloud Generator (ID: gfdbbmngalhmegpkejhidhgdpmehlmnd)
* Amazon Image Downloader (ID: cpcojeeblggnjjgnpiicndnahfhjdobd)
* Amazon Negative Review Hider (ID: hkkkipfcdagiocekjdhobgmlkhejjfoj)
* Amazon Listing Score Checker (ID: jaojpdijbaolkhkifpgbjnhfbmckoojh)
* Amazon Keyword Density Searcher (ID: ekomkpgkmieaaekmaldmaljljahehkoi)
* Amazon Sticky Notes (ID: hkhmodcdjhcidbcncgmnknjppphcpgmh)
* Amazon Result Numbering (ID: nipfdfkjnidadibpbflijepbllfkokac)
* Amazon Profit Calculator Lite (ID: behckapcoohededfbgjgkgefgkpodeho)
* Amazon Weight Converter (ID: dfnannaibdndmkienngjahldiofjbkmj)
* Amazon BSR Fast View (ID: nhilffccdbcjcnoopblecppbhalagpaf)
* Amazon Character Count & Seller Tools (ID: goikoilmhcgfidolicnbgggdpckdcoam)
* Amazon Global Price Checker (ID: mjcgfimemamogfmekphcfdehfkkbmldn)
* BestBuy Search By Image (ID: nppjmiadmakeigiagilkfffplihgjlec)
* SHEIN Search By Image (ID: mpgaodghdhmeljgogbeagpbhgdbfofgb)
* Shopify Search By Image (ID: gjlbbcimkbncedhofeknicfkhgaocohl)
* Walmart Search By Image (ID: mcaihdkeijgfhnlfcdehniplmaapadgb)

While "Amazon Ads Blocker" offers the advertised functionality, it also embeds malicious code that scans all Amazon product URL patterns for any affiliate tag without requiring any user interaction, and replaces it with "10xprofit-20" (or "\_c3pFXV63" for AliExpress). In cases where there are no tags, the attacker's tag is appended to each URL.

Socket also noted that the extension listing page on the Chrome Web Store makes misleading disclosures, claiming that the developers earn a "small commission" every time a user makes use of a coupon code to make a purchase.

Affiliate links are widely used across social media and websites. They refer to URLs containing a specific ID that enables tracking of traffic and sales to a particular marketer. When a user clicks this link to buy the product, the affiliate earns a cut of the sale.

Due to the extensions searching for existing tags and replacing them, social media content creators who share Amazon product links with their own affiliate tags lose commissions when users who have installed the add-on click those links.

This amounts to a violation of
[Chrome Web Store policies](https://developer.chrome.com/docs/webstore/program-policies/affiliate-ads)
, as they require extensions using affiliate links to accurately divulge how the program works, require user action before each injection, and never replace existing affiliate codes.

"The disclosure describes a coupon/deal extension with user-triggered reveals. The actual product is an ad blocker with automatic link modification," Pandya explained. "This mismatch between disclosure and implementation creates false consent."

"The extension also violates the
[Single Purpose policy](https://developer.chrome.com/docs/webstore/program-policies/policies)
by combining two unrelated functions (ad blocking and affiliate injection) that should be separate extensions."

The identified extensions have also been found to scrape product data and exfiltrate it to "app.10xprofit[.]io," with those focusing on AliExpress serving bogus "LIMITED TIME DEAL" countdown timers on product pages to create a false sense of urgency and rush them into making purchases so as to earn commissions on affiliate links.

"Extensions that combine unrelated functionality (ad blocking, price comparison, coupon finding) with affiliate injection should be treated as high-risk, particularly those with disclosures that don't match the actual code behavior," Socket said.

The disclosure comes as Broadcom-owned Symantec flagged four different extensions that have a combined user base exceeding 100,000 users and are designed to steal data -

* Good Tab (ID: glckmpfajbjppappjlnhhlofhdhlcgaj), which grants full clipboard permissions to an external domain ("api.office123456[.]com") to enable remote clipboard-read and clipboard-write permissions
* Children Protection (ID: giecgobdmgdamgffeoankaipjkdjbfep), which implements functionality to harvest cookies, inject ads, and execute arbitrary JavaScript by contacting a remote server
* DPS Websafe (ID: bjoddpbfndnpeohkmpbjfhcppkhgobcg), which changes the default search to one under their control to capture search terms entered by users and potentially route them to malicious websites
* Stock Informer (ID: beifiidafjobphnbhbbgmgnndjolfcho), which is susceptible to a years-old cross-site (XSS) vulnerability in the
  [Stockdio Historical Chart](https://jondow.eu/cve-2020-28707-xss-in-stockdio-historical-chart-plugin-for-wordpress-before-version-281/)
  WordPress plugin (
  [CVE-2020-28707](https://nvd.nist.gov/vuln/detail/CVE-2020-28707)
  , CVSS score: 6.1) that could allow a remote attacker to execute JavaScript code

"While browser extensions can provide a wide range of handy tools to help us achieve more online, much care needs to be taken when choosing to install them, even when installing from trusted sources," researchers Yuanjing Guo and Tommy Dong
[said](https://www.security.com/threat-intelligence/chrome-extensions-are-you-getting-more-you-bargained)
.

Rounding off the list of malicious extensions is another network of 16 add-ons (15 on the Chrome Web Store and one on the Microsoft Edge Add-ons marketplace) that are designed to intercept and steal ChatGPT authentication tokens by injecting a content script into chatgpt[.]com. Cumulatively, the extensions were downloaded about 900 times, according to LayerX.

The extensions are assessed to be part of a coordinated campaign due to overlaps in source code, icons, branding, and descriptions -

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjX4b6e5cbN8TDKtCLqwOWVSKj7_PGrGII9WAu3MagJ5rbxfIoEoAtMvtenYYL2FG0P7dZbR3RkMgILL145kmXSN_gmUaGHSJ84swq-nNVs4NMIZ4rpKpSDlxoC8kjKihWopaXmHVHhqZon3HTg3ksUMAYk44h-j0rjD0_5jtkvNxpZS9X-OSPiVfvuw_2h/s1700-e365/layerx.jpg)

* ChatGPT folder, voice download, prompt manager, free tools – ChatGPT Mods (ID: lmiigijnefpkjcenfbinhdpafehaddag)
* ChatGPT voice download, TTS download – ChatGPT Mods (ID: obdobankihdfckkbfnoglefmdgmblcld)
* ChatGPT pin chat, bookmark – ChatGPT Mods (ID: kefnabicobeigajdngijnnjmljehknjl)
* ChatGPT message navigator, history scroller – ChatGPT Mods (ID: ifjimhnbnbniiiaihphlclkpfikcdkab)
* ChatGPT model switch, save advanced model uses – ChatGPT Mods (ID: pfgbcfaiglkcoclichlojeaklcfboieh)
* ChatGPT export, Markdown, JSON, images – ChatGPT Mods (ID: hljdedgemmmkdalbnmnpoimdedckdkhm)
* ChatGPT Timestamp Display – ChatGPT Mods (ID: afjenpabhpfodjpncbiiahbknnghabdc)
* ChatGPT bulk delete, Chat manager – ChatGPT Mods (ID: gbcgjnbccjojicobfimcnfjddhpphaod)
* ChatGPT search history, locate specific messages – ChatGPT Mods (ID: ipjgfhcjeckaibnohigmbcaonfcjepmb)
* ChatGPT prompt optimization – ChatGPT Mods (ID: mmjmcfaejolfbenlplfoihnobnggljij)
* Collapsed message – ChatGPT Mods (ID: lechagcebaneoafonkbfkljmbmaaoaec)
* Multi-Profile Management & Switching – ChatGPT Mods (ID: nhnfaiiobkpbenbbiblmgncgokeknnno)
* Search with ChatGPT – ChatGPT Mods (ID: hpcejjllhbalkcmdikecfngkepppoknd)
* ChatGPT Token counter – ChatGPT Mods (ID: hfdpdgblphooommgcjdnnmhpglleaafj)
* ChatGPT Prompt Manager, Folder, Library, Auto Send – ChatGPT Mods (ID: ioaeacncbhpmlkediaagefiegegknglc)
* ChatGPT Mods – Folder Voice Download & More Free Tools (ID: jhohjhmbiakpgedidneeloaoloadlbdj)

With artificial intelligence (AI)-related extensions becoming increasingly common in enterprise workflows, the development highlights an emerging attack surface where threat actors weaponize the trust associated with popular AI brands to deceive users into installing them.

Because such tools often require elevated execution context within the browser and have access to sensitive data, seemingly harmless extensions can become a lucrative attack vector, permitting adversaries to obtain persistent access without the need for exploiting security flaws or resorting to other methods that may trigger security alarms.

"Possession of such tokens provides account-level access equivalent to that of the user, including access to conversation history and metadata," security researcher Natalie Zargarov
[said](https://layerxsecurity.com/blog/how-we-discovered-a-campaign-of-16-malicious-extensions-chatgpt/)
. "As a result, attackers can replicate the users' access credentials to ChatGPT and impersonate them, allowing them to access all of the user's ChatGPT conversations, data, or code."

### Browsers Become a Lucrative Attack Vector

The findings also coincide with the emergence of a new malware-as-a-service toolkit called
[Stanley](https://thehackernews.com/2026/01/weekly-recap-firewall-flaws-ai-built.html#:~:text=New%20Stanley%20Kit%20Guarantees%20Chrome%20Web%20Store%20Approval)
that's being peddled on a Russian cybercrime forum for between $2,000 and $6,000, and allows crooks to generate malicious Chrome browser extensions that can be used to serve phishing pages within an
[HTML iframe element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
while still showing the legitimate URL in the address bar.

Customers of the tool gain access to a C2 panel for managing victims, configuring spoofed redirects, and sending fake browser notifications. Those who are willing to spend $6,000 get a guarantee that any extension they create using the kit will pass Google's vetting process for the Chrome Web Store.

These extensions take the form of innocuous note-taking utilities to fly under the radar. But their malicious behavior is activated when the user navigates to a website of interest to the attacker, such as a bank, at which point a full-screen iframe containing the phishing page is overlaid, while leaving the browser's URL bar intact. This visual deception creates a defensive blind spot that can dupe even vigilant users into entering their credentials or sensitive information on the page.

As of January 27, 2025, the service appears to have vanished – likely prompted by the public disclosure – but it's very much possible that it can resurface under a different name in the future.

"Stanley provides a turnkey website-spoofing operation disguised as a Chrome extension, with its premium tier promising guaranteed publication on the Chrome Web Store," Varonis researcher Daniel Kelley noted earlier this week. "BYOD policies, SaaS-first environments, and remote work have made the browser the new endpoint. Attackers have noticed. Malicious browser extensions are now a primary attack vector."