---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T12:15:14.428613+00:00'
exported_at: '2026-04-14T12:15:16.794261+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html
structured_data:
  about: []
  author: ''
  description: Mirax Android RAT spreads via Meta ads reaching 220,000 accounts, enabling
    proxy abuse and fraud operations.
  headline: Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000
    via Meta Ads
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta
  Ads
updated_at: '2026-04-14T12:15:14.428613+00:00'
url_hash: 256044fb8312cfd0a3e0a294b2fb212b9a388981
---

A nascent Android remote access trojan called
**Mirax**
has been observed actively targeting Spanish-speaking countries, with campaigns reaching more than 220,000 accounts on Facebook, Instagram, Messenger, and Threads through advertisements on Meta.

"Mirax integrates advanced Remote Access Trojan (RAT) capabilities, allowing threat actors to fully interact with compromised devices in real time," Italian online fraud prevention firm Cleafy
[said](https://www.cleafy.com/cleafy-labs/mirax-a-new-android-rat-turning-infected-devices-into-potential-residential-proxy-nodes)
.

"Beyond traditional RAT behavior, Mirax enhances its operational value by turning infected devices into
[residential proxy nodes](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/the-rise-of-residential-proxies-and-its-impact-on-cyber-risk-exposure-management)
. Leveraging SOCKS5 protocol support and Yamux multiplexing, it establishes persistent proxy channels that allow attackers to route their traffic through the victim's real IP address."

Details of Mirax
[first emerged](https://thehackernews.com/2026/03/six-android-malware-families-target-pix.html)
last month when Outpost24's KrakenLabs revealed that a threat actor going by the name "Mirax Bot" has been advertising a private malware-as-a-service (MaaS) offering on underground forums for $2,500 for a three-month subscription. Also available for $1,750 per month is a lightweight variant that removes certain features like the proxy and the ability to bypass Google Play Protect using a
[crypter](https://thehackernews.com/2023/05/acecryptor-cybercriminals-powerful.html)
.

Like other Android malware, Mirax supports the ability to capture keystrokes, steal photos, gather lock screen details, run commands, navigate the user interface, and monitor user activity on the compromised device. It can also dynamically fetch HTML overlay pages from a command-and-control (C2) server to be rendered over legitimate applications for credential theft.

The incorporation of a SOCKS proxy, on the other hand, is a relatively lesser-known feature that sets it apart from conventional RAT behavior. The proxy botnet offers several advantages in that it allows threat actors to get around geolocation-based restrictions, evade fraud detection systems, and conduct account takeovers or transaction fraud under the guise of increased anonymity and legitimacy.

"Unlike typical MaaS offerings, Mirax is distributed through a highly controlled and exclusive model, limited to a small number of affiliates," researchers Alberto Giust, Alessandro Strino, and Federico Valentini said. "Access appears to be prioritized for Russian-speaking actors with established reputations in underground communities, indicating a deliberate effort to maintain operational security and campaign effectiveness."

Attack chains distributing the malware use Meta ads to promote dropper app web pages, tricking unsuspecting users into downloading them. As many as six ads have been observed
[actively advertising](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&q=streamtv%20esp&search_type=keyword_unordered&sort_data[direction]=desc&sort_data[mode]=total_impressions)
a streaming service with free access to live sports and movies. Of these, five ads are directed against users in Spain. One of the ads, which started running on April 6, 2026, has a reach of 190,987 accounts.

The dropper app URLs implement a number of checks to ensure that they are accessed from mobile devices and to prevent automated scans from revealing their true color. The names of the malicious apps are listed below -

* StreamTV (org.lgvvfj.pluscqpuj or org.dawme.secure5ny) - Dropper app
* Reproductor de video (org.yjeiwd.plusdc71 or org.azgaw.managergst1d) - Mirax

A notable aspect of the campaign is the use of GitHub to host the malicious dropper APK files. In addition, the builder panel offers the ability to choose between two crypters – Virbox and
[Golden Crypt](https://thehackernews.com/2025/12/new-albiriox-maas-malware-targets-400.html)
(aka Golden Encryption) – for enhanced APK protection.

Once installed, the dropper instructs users to allow installation from unknown sources to deploy the malware. The process of extracting the final payload is a "sophisticated, multi-stage operation" that's designed to sidestep security analysis and automated sandboxing tools.

The malware, after getting installed on the device, masquerades as a video playback utility and prompts the victim to enable accessibility services, thereby allowing it to run in the background, display a fake error message stating the installation was unsuccessful, and serve bogus overlays to conceal malicious activities.

It also establishes multiple bidirectional C2 channels for tasking and data exfiltration -

* WebSocket on port 8443, to manage remote access and execute remote commands.
* WebSocket on port 8444, to manage remote streaming and data exfiltration.
* WebSocket on port 8445 (or a custom port), to set up the residential proxy using SOCKS5.

"This convergence of RAT and proxy capabilities reflects a broader shift in the threat landscape," Cleafy said. "While residential proxy abuse has historically been associated with compromised IoT devices and low-cost Android hardware such as smart TVs, Mirax marks a new phase by embedding this functionality within a full-featured banking trojan."

"This approach not only increases the monetization potential of each infection but also expands the operational scope of attackers, who can now leverage compromised devices for both direct financial fraud and as infrastructure for wider cybercriminal activities."

The disclosure comes as Breakglass Intelligence detailed an Arabic-language Android RAT called ASO RAT that's distributed via apps disguised as PDF readers and Syrian government applications.

"The platform provides full device compromise capabilities – SMS interception, camera access, GPS tracking, call logging, file exfiltration, and DDoS launching from victim devices," the company
[said](https://intel.breakglass.tech/post/aso-rat-arabic-android-surveillance-platform-syria)
. "A multi-user panel with role-based access control suggests this operates as a RAT-as-a-Service or supports a multi-operator team."

It's currently not known what the exact end goals of the campaign are, but Syria-themed lures for the apps (e.g., SyriaDefenseMap and GovLens) suggest that it may be targeting individuals with an interest in Syrian military or governance matters as part of what's suspected to be a surveillance operation.