---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:19:51.406139+00:00'
exported_at: '2026-11-15T07:19:53.286571+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/operation-endgame-takes-down-gootloader.html
structured_data:
  about: []
  author: ''
  description: Operation Endgame seized 235 servers, 257 domains, and 6.4 million
    stolen logins in a takedown targeting Gootloader, CastleRAT, and StealC.
  headline: Operation Endgame Takes Down Gootloader, CastleRAT and StealC Servers,
    Seizes 6.4M Stolen Logins
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/operation-endgame-takes-down-gootloader.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Operation Endgame Takes Down Gootloader, CastleRAT and StealC Servers, Seizes
  6.4M Stolen Logins
updated_at: '2026-11-15T07:19:51.406139+00:00'
url_hash: 5df4bf07aed5b496f0abefa15d48eb411855500b
---

An international police operation took down servers behind
**Gootloader**
,
**CastleRAT**
and
**StealC**
this week. Criminals used the three malware tools to gain access to computers, steal passwords, and launch ransomware attacks.

Police also seized about 6.4 million stolen logins belonging to more than 40,000 victims, according to Germany's Federal Criminal Police Office (BKA).

**Gootloader**
is a loader: once on a computer, it could download other malware, especially ransomware. It spread through fake legal documents placed on hacked websites, often WordPress sites. Criminals used SEO poisoning to push those sites high in search results.

Gootloader has infected at least 25,000 computers worldwide since 2018, the U.S. Justice Department said. Its operators used those computers to infect more computers, then sold access to the new ones to ransomware criminals. In the U.S., Gootloader was used in ransomware attacks against at least 44 victims, resulting in about $28.8 million in losses.

German police gave a much higher count in their
[statement in German](https://www.presseportal.de/blaulicht/pm/7/6389442)
. Based on what investigators know so far, Gootloader has infected millions of computers worldwide since it first appeared in 2020.

Across the three tools, police seized 235 servers and 257 domains, according to an
[operation summary](https://www.europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks)
from Europol, which supported the action. The takedown is part of Operation Endgame, an international police campaign against malware criminals use to access victims' computers.

For Gootloader, police took down 14 servers and 218 domains and removed malware from 681 hacked websites.

With court approval, U.S. agencies and their international partners removed Gootloader from more than 100 servers, including hacked WordPress sites. They also seized U.S. domains used to deliver and control the malware, according to the
[Justice Department announcement](https://www.justice.gov/opa/pr/gootloader-malware-disrupted-international-cyber-operation)
.

**CastleRAT**
, a remote access trojan (RAT) known since 2025, allows attackers to control an infected computer remotely. Police seized 120 of its servers and 39 domains.

**StealC**
is an infostealer that exfiltrates passwords and other login credentials from infected computers, allowing criminals to sell or misuse them. Police took down its servers again this week, after a
[June operation](https://thehackernews.com/2026/06/amadey-and-stealc-malware-network.html)
against it.

After that June action, its operators changed their infrastructure and brought it back online to stay out of investigators' reach, German police said. Some of StealC's key infrastructure ran on Virtualine/Omegatech, a bulletproof hosting service that advertised its services to criminals.

Police shut that hosting service down in a
[late-October takedown](https://thehackernews.com/2026/10/fbi-seizes-virtualine-domain-over.html)
.

No arrests were announced in this week's action. Dutch police also carried out further investigations targeting Gootloader's main suspect, according to their
[news release](https://www.politie.nl/en/news/2026/november/international-action-disables-cybercriminal-network.html)
.

### What Victims and Site Owners Can Do

Dutch police have loaded data stolen by CastleRAT into
[Check your hack](https://www.politie.nl/en/information/checkyourhack.html)
, a police service where people can enter an email address. If the address is in the data, the police send an email within a few minutes with steps to remove the malware. If it is not, no email arrives.

More data will be added in the coming weeks. The service checks single addresses, not whole domains, but organizations can join No More Leaks, a police project that shares data with private partners. The stolen data is also being shared with services including Have I Been Pwned and the Shadowserver Foundation.

Emails that claim to come from the police and ask people to check the data are fake. The police never send emails with links.

Even after police seize the data, criminals may still have the stolen logins, the police say in their
[frequently asked questions](https://www.politie.nl/en/information/frequently-asked-questions-about-check-your-hack.html)
. As long as the malware stays on a computer, criminals may also keep getting its passwords.

The Shadowserver Foundation is working with internet service providers and computer security incident response teams (CSIRTs) to find infected computers and notify their owners, the Justice Department said. In Germany, the Federal Office for Information Security (BSI) is helping notify victims, according to the BKA.

Denmark's National Special Crime Unit (NSK) helped clean the 681 websites. In a
[statement in Danish](https://politi.dk/national-enhed-for-saerlig-kriminalitet/nyhedsliste/skadelig-kode-fjernet-fra-over-600-hjemmesider/2026/11/12)
, the unit said it believes the attackers got into the sites with stolen passwords that came through criminal channels. They then installed a backdoor.

Officers removed the attackers' code and access, and left a message for the site owners with advice on securing their sites.

Police in Denmark and the Netherlands advise WordPress site owners to take these steps, several of which are set out in a
[Dutch advice sheet](https://www.politie.nl/binaries/content/assets/politie/nieuws/2026/november/67e23014-cf5f-4970-be59-aeff916c15f1.pdf)
:

* Change all administrator passwords to unique, at least 12-character passwords.
* Turn on multi-factor authentication (MFA).
* Remove accounts you do not recognize.
* Remove any backdoor code from the site.
* Update WordPress, its themes, and its plugins.
* Allow access to the /wp-admin login page only from the IP addresses of your own devices.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.