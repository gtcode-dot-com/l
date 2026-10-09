---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-14T20:15:13.233596+00:00'
exported_at: '2026-01-14T20:15:21.245461+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/kimwolf-botnet-infected-over-2-million.html
structured_data:
  about: []
  author: ''
  description: The Kimwolf botnet compromised more than 2 million Android devices,
    turning them into residential proxies for DDoS attacks and traffic abuse.
  headline: Researchers Null-Route Over 550 Kimwolf and Aisuru Botnet Command Servers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/kimwolf-botnet-infected-over-2-million.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Null-Route Over 550 Kimwolf and Aisuru Botnet Command Servers
updated_at: '2026-01-14T20:15:13.233596+00:00'
url_hash: e6462446c5b11d1068b16ca75ced2bddc5787e8b
---

The Black Lotus Labs team at Lumen Technologies
[said](https://www.linkedin.com/pulse/keeping-kimwolf-bay-putting-leash-massive-ddos-botnet-t1pyc/)
it null-routed traffic to more than 550 command-and-control (C2) nodes associated with the AISURU/Kimwolf botnet since early October 2025.

AISURU and its Android counterpart, Kimwolf, have emerged as some of the biggest botnets in recent times, capable of directing enslaved devices to participate in distributed denial-of-service (DDoS) attacks and relay malicious traffic for
[residential proxy services](https://spur.us/what-is-a-residential-proxy/)
.

Details about Kimwolf
[emerged last month](https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html)
when QiAnXin XLab published an exhaustive analysis of the malware, which turns compromised devices – mostly unsanctioned Android TV streaming devices – into a residential proxy by delivering a software development kit (SDK) called ByteConnect either directly or through sketchy apps that come pre-installed on them.

The net result is that the botnet has expanded to
[infect more than 2 million Android devices](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)
with an exposed Android Debug Bridge (ADB) service by tunneling through residential proxy networks, thereby allowing the threat actors to compromise a wide swath of TV boxes.

A subsequent report from Synthient has revealed Kimwolf actors attempting to offload proxy bandwidth in exchange for upfront cash.

Black Lotus Labs said it identified in September 2025 a group of residential SSH connections originating from multiple Canadian IP addresses based on its analysis of backend C2 for Aisuru at 65.108.5[.]46, with the IP addresses using SSH to access 194.46.59[.]169, which proxy-sdk.14emeliaterracewestroxburyma02132[.]su.

It's worth noting that the second-level domain
[surpassed Google](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploit-chrome-0.html#:~:text=environments.-,Microsoft%20Mitigates%20Record%2015.72%20Tbps%20DDoS%20Attack)
in Cloudflare's list of top 100 domains in November 2025, prompting the web infrastructure company to
[scrub it from the list](https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/)
.

Then, in early October 2025, the cybersecurity company said it identified another C2 domain – greatfirewallisacensorshiptool.14emeliaterracewestroxburyma02132[.]su – that resolved to 104.171.170[.]21, an IP address belonging to Utah-based hosting provider Resi Rack LLC. The company advertises itself as a "Premium Game Server Hosting Provider."

This link is crucial, as a recent report from independent security journalist Brian Krebs
[revealed](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/)
how people behind various proxy services based on the botnets were peddling their warez on a Discord server called resi[.]to. This also includes Resi Rack's co-founders, who are said to have been actively engaged in selling proxy services via Discord for nearly two years.

The server, which has since disappeared, was owned by someone named "d" (assessed to be short for the handle "Dort"), with Snow believed to be the botmaster.

"In early October, we observed a 300% surge in the number of new bots added to Kimwolf over a 7-day period, which was the start of an increase that reached 800,000 total bots by mid-month," Black Lotus Labs said. "Nearly all of the bots in this surge were found listed for sale on a single residential proxy service."

Subsequently, the Kimwolf C2 architecture was found to scan PYPROXY and other services for vulnerable devices between October 20, 2025, and November 6, 2025 -- a behavior explained by the botnet's exploitation of a security flaw in many proxy services that made it possible to interact with devices on the internal networks of residential proxy endpoints and drop the malware.

This, in turn, turns the device into a residential proxy node, causing its public IP address (assigned by the Internet Service Provider) to be listed for rent on a residential proxy provider site. Threat actors, such as those behind these botnets, then lease access to the infected node and weaponize it to scan the local network for devices with ADB mode enabled for further propagation.

"After one successful null route [in October 2025], we observed the greatfirewallisacensorshiptool domain move to 104.171.170[.]201, another Resi Rack LLC IP," Black Lotus Labs noted. "As this server stood up, we saw a large spike of traffic with 176.65.149[.]19:25565, a server used to host their malware. This was on a common ASN that was used by the Aisuru botnet at the same time."

The disclosure comes against the backdrop of a report from Chawkr that detailed a sophisticated proxy network containing 832 compromised KeeneticOS routers operating across Russian ISPs, such as Net By Net Holding LLC, VladLink, and GorodSamara.

"The consistent SSH fingerprints and identical configurations across all 832 devices point toward automated mass exploitation, whether leveraging stolen credentials, embedded backdoors, or known security flaws in the router firmware," it
[said](https://chawkr.com/threat-intel/keenetic-proxy-botnet-analysis)
. "Each compromised router maintains both HTTP (port 80) and SSH (port 22) access."

Given that these compromised SOHO routers function as residential proxy nodes, they provide threat actors with the ability to conduct malicious activities by blending into normal internet traffic. This illustrates how adversaries are increasingly leveraging consumer devices as conduits for multi-stage attacks.

"Unlike datacenter IPs or addresses from known hosting providers, these residential endpoints operate below the radar of most security vendor reputation lists and threat intelligence feeds," Chawkr noted.

"Their legitimate residential classification and clean IP reputation allow malicious traffic to masquerade as ordinary consumer activity, evading detection mechanisms that would immediately flag requests originating from suspicious hosting infrastructure or known proxy services."