---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T08:15:13.504489+00:00'
exported_at: '2026-01-29T08:15:15.719732+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/google-disrupts-ipidea-one-of-worlds.html
structured_data:
  about: []
  author: ''
  description: Google dismantled IPIDEA, a residential proxy network used by 550+
    threat groups to hijack millions of consumer devices for cybercrime and espionage.
  headline: Google Disrupts IPIDEA — One of the World’s Largest Residential Proxy
    Networks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/google-disrupts-ipidea-one-of-worlds.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Disrupts IPIDEA — One of the World’s Largest Residential Proxy Networks
updated_at: '2026-01-29T08:15:13.504489+00:00'
url_hash: 6bdb5bad7bb773e03f44c292a8fbfd3832616d53
---

Google on Wednesday
[announced](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network)
that it worked together with other partners to disrupt IPIDEA, which it described as one of the largest residential proxy networks in the world.

To that end, the company said it took legal action to take down dozens of domains used to control devices and proxy traffic through them. As of writing, IPIDEA's website ("www.ipidea.io") is no longer accessible. It advertised itself as the "world's leading provider of IP proxy" with more than 6.1 million daily updated IP addresses and 69,000 daily new IP addresses.

"Residential proxy networks have become a pervasive tool for everything from high-end espionage to massive criminal schemes," John Hultquist, Google Threat Intelligence Group's (GTIG) chief analyst, said in a statement shared with The Hacker News.

"By routing traffic through a person's home internet connection, attackers can hide in plain sight while infiltrating corporate environments. By taking down the infrastructure used to run the IPIDEA network, we have effectively pulled the rug out from under a global marketplace that was selling access to millions of hijacked consumer devices."

Google said that, as recently as this month, IPIDEA's proxy infrastructure has been leveraged by more than 550 individual threat groups with varying motivations, such as cybercrime, espionage, advanced persistent threat (APTs), information operations, from across the world, including China, North Korea, Iran, and Russia. These activities ranged from access to victim SaaS environments, on-premises infrastructure, and password spray attacks.

In an analysis published earlier this month, Synthient
[revealed](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)
that the threat actors behind the
[AISURU/Kimwolf botnet](https://thehackernews.com/2026/01/kimwolf-botnet-infected-over-2-million.html)
were abusing security flaws in residential proxy services like IPIDEA to relay malicious commands to susceptible Internet of Things (IoT) devices behind a firewall within local networks to propagate the malware.

The malware that turns consumer devices into proxy endpoints is stealthily bundled within apps and games pre-installed on off-brand Android TV streaming boxes. This forces the infected device to relay malicious traffic and participate in distributed denial-of-service (DDoS) attacks.

IPIDEA is also said to have released standalone apps, marketed directly to people looking to make "easy cash" by blatantly advertising they'll pay consumers to install the app and allow it to use their "unused bandwidth."

While residential proxy networks offer the ability to route traffic through IP addresses owned by internet service providers (ISPs), this can also provide the perfect cover for bad actors looking to mask the origin of their malicious activity.

"To do this, residential proxy network operators need code running on consumer devices to enroll them into the network as exit nodes," GTIG explained. "These devices are either pre-loaded with proxy software or are joined to the proxy network when users unknowingly download trojanized applications with embedded proxy code. Some users may knowingly install this software on their devices, lured by the promise of 'monetizing' their spare bandwidth."

The tech giant's threat intelligence team said IPIDEA has become notorious for its role in facilitating a number of botnets, including the
[China](https://krebsonsecurity.com/2026/01/who-operates-the-badbox-2-0-botnet/)
-based
[BADBOX 2.0](https://thehackernews.com/2025/07/google-sues-25-chinese-entities-over.html)
. In July 2025, Google filed a lawsuit against 25 unnamed individuals or entities in China for allegedly operating the botnet and its associated residential proxy infrastructure.

It also pointed out that the proxy applications from IPIDEA not only routed traffic through the exit node device, but also sent traffic to the device with the goal of compromising it, posing severe risks to consumers whose devices may have knowingly or unknowingly joined the proxy network.

The proxy network that powers IPIDEA is not a monolithic entity. Rather, it's a collection of multiple well-known residential proxy brands under its control -

* Ipidea (ipidea[.]io)
* 360 Proxy (360proxy[.]com)
* 922 Proxy (922proxy[.]com)
* ABC Proxy (abcproxy[.]com)
* Cherry Proxy (cherryproxy[.]com)
* Door VPN (doorvpn[.]com)
* Galleon VPN (galleonvpn[.]com)
* IP 2 World (ip2world[.]com)
* Luna Proxy (lunaproxy[.]com)
* PIA S5 Proxy (piaproxy[.]com)
* PY Proxy (pyproxy[.]com)
* Radish VPN (radishvpn[.]com)
* Tab Proxy (tabproxy[.]com)

"The same actors that control these brands also control several domains related to Software Development Kits (SDKs) for residential proxies," Google said. "These SDKs are not meant to be installed or executed as standalone applications, rather they are meant to be embedded into existing applications."

These SDKs are marketed to third-party developers as a way to monetize their Android, Windows, iOS, and WebOS applications. Developers who integrate the SDKs into their apps are paid by IPIDEA on a per-download basis. This, in turn, transforms a device that installs these apps into a node for the proxy network, while simultaneously providing the advertised functionality. The names of the SDKs controlled by the IPIDEA actors are listed below -

* Castar SDK (castarsdk[.]com)
* Earn SDK (earnsdk[.]io)
* Hex SDK (hexsdk[.]com)
* Packet SDK (packetsdk[.]com)

The SDKs have significant overlaps in their command-and-control (C2) infrastructure and code structure. They follow a two-tier C2 system where the infected devices contact a Tier One server to retrieve a set of Tier Two nodes to connect to. The application then initiates communication with the Tier Two server to periodically poll for payloads to proxy through the device. Google's analysis found that there are about 7,400 Tier Two servers.

Besides proxy services, the IPIDEA actors have been found to control domains that offer free Virtual Private Network (VPN) tools, which are also engineered to join the proxy network as an exit node incorporating either the Hex or Packet SDK. The names of the VPN services are as follows -

* Galleon VPN (galleonvpn[.]com)
* Radish VPN (radishvpn[.]com
* Aman VPN (defunct)

In addition, GTIG said it identified 3,075 unique Windows binaries that have sent a request to at least one Tier One domain, some of which masqueraded as OneDriveSync and Windows Update. These trojanized Windows applications were not distributed by the IPIDEA actors directly. As many as 600 Android applications (spanning utilities, games, and content) from multiple download sources have been flagged for containing code connecting to Tier One C2 domains by using the monetization SDKs to enable the proxy behavior.

In a
[statement](https://www.wsj.com/tech/google-aims-knockout-blow-at-chinese-company-linked-to-massive-cyber-weapon-3c3fdc40)
shared with The Wall Street Journal, a spokesperson for the Chinese company said it had engaged in "relatively aggressive market expansion strategies" and "conducted promotional activities in inappropriate venues (e.g., hacker forums)," and it has "explicitly opposed any form of illegal or abusive conduct."

To counter the threat, Google said it has updated Google Play Protect to automatically warn users about apps containing IPIDEA code. For certified Android devices, the system will automatically remove these malicious applications and block any future attempts to install them.

"While proxy providers may claim ignorance or close these security gaps when notified, enforcement and verification are challenging given intentionally murky ownership structures, reseller agreements, and diversity of applications," Google said.