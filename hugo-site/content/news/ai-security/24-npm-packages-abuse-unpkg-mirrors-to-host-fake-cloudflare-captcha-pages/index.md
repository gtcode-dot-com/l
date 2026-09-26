---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T16:53:32.360148+00:00'
exported_at: '2026-09-26T16:53:33.549515+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html
structured_data:
  about: []
  author: ''
  description: A campaign uses 24 npm packages and unpkg mirrors to host fake Cloudflare
    CAPTCHA pages that can redirect users to attacker-chosen sites.
  headline: 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages
updated_at: '2026-09-26T16:53:32.360148+00:00'
url_hash: e7c2149d23bc69134683a0fd2625b646e1241e48
---

**

Ravie Lakshmanan
**

Aug 25, 2026

Phishing / Threat Intelligence

Cybersecurity researchers have disclosed details of a new campaign that uses a cluster of 24 npm packages as free phishing infrastructure for redirecting to ClickFix-style fake CAPTCHA pages.

"While the malware is simply a single HTML page inside the npm package, and while downloading it wouldn't do harm, the threat actor’s use of npm isn't to infect developers who install it, but to use the registry and its mirrors as a safe, validated storage for the malware," OX Security researchers Moshe Siman Tov Bustan and Vitalii Chepurko
[said](https://www.ox.security/blog/research-clickfix-phishing-npm-packages/)
.

The list of npm packages, some of which are still available for download, is below -

* bgzxcuite2
* prezdentkxheiw
* egair0810
* mnteckets
* airdzticket
* egypt0811
* passport811
* vxhjkseuiaqkb
* ndmushdkeqe
* ndmxchdjxn2
* ndmfguyhoxc3
* mjsdqwocvn
* m2fcsfyjkuxb
* m3fdfocdoewn
* @worrisome/reutil
* testdgdbcsd
* tesgfvbncsdbcv
* mndsxcusiwlk1
* mn2adskhweox
* mn3sadkoiewu
* mn4xcouzvhus
* mbxcnsuwgs1
* skxcmwuncbg2
* mobiwaefhxc3

The campaign specifically targets mirrors like unpkg. Once mirrored on these services, the HTML file (e.g., "unpkg[.]com/ndmxchdjxn2@1.0.0/index.html") becomes a live, fully-rendered fake Cloudflare CAPTCHA page that's hosted on a trusted domain but redirects to attacker-controlled phishing infrastructure that could enable ClickFix attacks or credential harvesting.

As a result, anyone who opens a link that's hosted on the npm mirror will be tricked into carrying out unintended actions that can lead to the deployment of malware. This involves displaying a fake Cloudflare verification page, which then sends the target to an external website controlled by the attacker.

The HTML page embeds the logic to serve the bogus CAPTCHA verification prompt, as well as JavaScript necessary to send a request to a remote server. Initial iterations of the malware were found to send the request to a typosquat domain that impersonates the Microsoft login page ("login[.]microsofte[.]live").

But after the domain was added to Google Chrome's Safe Browsing blocklist, the threat actor behind the campaign is said to have responded by switching to
[KeyVal](https://keyval.org/#)
("api.keyval[.]org"), a free, public key-value store that allows developers to set a key-value pair or retrieve a value given a key using a REST API.

In doing so, it turns the legitimate service into a dead drop resolver (
[DDR](https://www.cc.gatech.edu/news/hiding-plain-sight-disrupting-malwares-secret-web-dead-drops)
) and uses it to extract and decode the URL to which the victim is redirected to.

"Currently the remote logic transfers the user to the legitimate ChatGPT website, but it could be weaponized to deliver ClickFix or any other phishing domains when configured to by the attacker," the researchers said.

This is not the first time this approach has been abused by bad actors. In October 2025, Socket
[detailed](https://thehackernews.com/2025/10/175-malicious-npm-packages-with-26000.html)
a set of 175 npm packages that used unpkg.com's content delivery network (CDN) to host redirect scripts that routed victims to credential harvesting pages as part of a campaign codenamed Beamglea.

"Threat actors keep finding and using new and novel techniques not just to deliver malware, but to use legitimate infrastructure to store their payloads and data," OX Security said.

"When we think of malware as families of code that steal data directly from the machine they are running on, we can miss other ideas such as infrastructure abuse, using npm and its mirrors as free storage, and persistence – since npm packages can live forever in mirrors even after they are removed from the official stores."