---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-12T10:15:13.935522+00:00'
exported_at: '2026-01-12T10:15:16.205674+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/researchers-uncover-service-providers.html
structured_data:
  about: []
  author: ''
  description: Researchers show how pig butchering-as-a-service providers equip scam
    networks with turnkey tools and infrastructure for large-scale online fraud.
  headline: Researchers Uncover Service Providers Fueling Industrial-Scale Pig Butchering
    Fraud
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/researchers-uncover-service-providers.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Uncover Service Providers Fueling Industrial-Scale Pig Butchering
  Fraud
updated_at: '2026-01-12T10:15:13.935522+00:00'
url_hash: d8bcc32501c5d463b94a0e4c9dddf54657425b18
---

Cybersecurity researchers have shed light on two service providers that supply online criminal networks with the necessary tools and infrastructure to fuel the pig butchering-as-a-service (PBaaS) economy.

At least since 2016, Chinese-speaking criminal groups have
[erected](https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html#scam-empire-kingpin-caught)
industrial-scale scam centers across Southeast Asia, creating special economic zones that are
[devoted](https://thehackernews.com/2024/04/indian-government-rescues-250-citizens.html)
to fraudulent investment and impersonation operations.

These compounds are host to thousands of people who are
[lured](https://thehackernews.com/2024/05/chinese-nationals-arrested-for.html)
with the promise of high-paying jobs, only to have their passports and be forced to conduct scams under the threat of violence. INTERPOL has
[characterized](https://thehackernews.com/2024/12/interpol-pushes-for-romance-baiting-to.html)
these networks as human trafficking-fuelled fraud on an industrial scale.

One of the crucial drivers of the pig butchering (aka romance baiting) scams is service providers who supply the networks with all the tools to run and manage social engineering operations, as well as swiftly launder stolen funds and cryptocurrencies and move ill-gotten proceeds to accounts that cannot be reached by law enforcement.

"Large scam compounds such as the Golden Triangle Economic Zone (GTSEZ) are now using ready-made applications and templates from PBaaS providers," Infoblox
[said](https://www.infoblox.com/blog/threat-intelligence/scaling-the-fraud-economy-pig-butchering-as-a-service/)
in a report published last week.

"Compounding the situation further, what once required technical expertise, or an outlay for physical infrastructure, can now be purchased as an off-the-shelf service offering everything from stolen identities and front companies to turnkey scam platforms and mobile apps, dramatically lowering the barrier to entry."

These services have been found to offer full packages and fraud kits that set the groundwork for launching scalable online scam operations without much effort. One such threat actor is Penguin Account Store, which also goes by the names Heavenly Alliance and Overseas Alliance.

Penguin operates under a crimeware-as-a-service (CaaS) model, advertising fraud kits, scam templates, and "shè gōng kù" datasets comprising stolen personal information belonging to Chinese citizens. The group also peddles account data from various popular so-called media platforms like Twitter, Tinder, YouTube, Snapchat, Facebook, Instagram, Apple Music, OpenAI ChatGPT, Spotify, and Netflix, among others.

It's believed that these credentials are likely obtained through information-stealing logs sold on the dark web. But it's presently not known if they operate the stealers themselves or whether they are merely acting as a broker of stolen data for other threat actors. Prices for pre-registered social media accounts start from just $0.10 and go up in value depending on the date of registration and authenticity.

Also provided by Penguin are bulk pre-registered SIM cards, stolen social media accounts, 4G or 5G routers, IMSI catchers, and packages of stolen pictures (aka character sets) that are used to entrap victims. Besides these, the threat actor has developed a Social Customer Relationship Management (SCRM) platform dubbed SCRM AI to allow scam operators to facilitate automated victim engagement on social media.

"The threat actor also advertises BCD Pay, a payment processing platform. BCD Pay, which links directly to the Bochuang Guarantee (博创担保自), is an anonymous peer-to-peer (P2P) solution à la
[HuiOne](https://thehackernews.com/2025/01/illicit-huione-telegram-market.html)
, with deep roots in the illegal online gambling space."

A second service category that's central to the PBaaS economy is customer relationship management (CRM) platforms, which provide centralized control over several individual agents. UWORK, a seller of content and agent management tools, provides pre-made templates for creating investment scam websites. Many a scam offering also claims to have integration with legitimate trading platforms like MetaTrader to lend the sites a veneer of trust by displaying real-time financial information.

These websites also come fitted with a Know Your Customer (KYC) panel that requires victims to upload proof of their identity. The websites' settings are configured by an administrator through a dedicated panel, granting them a high-level view of the entire operation, along with the ability to create profiles for agents, who likely interface with the victims.

|  |
| --- |
|  |
| Panel to add a new victim account and assign them a direct agent |

"The admin panel offers everything needed to run a pig butchering operation. Multiple email templates, user management, agent management, profitability metrics, as well as chat and email records," Infoblox said. "The management of agents is very complex, and agents can even be affiliates of one another."

PBaaS suppliers have also been found to provide mobile applications for Android and iOS by distributing them in the form of APK files and enrolling a limited number of Apple devices into a
[testing program](https://thehackernews.com/2022/03/cryptorom-crypto-scam-abusing-iphone.html)
in order to bypass app store controls.

Some threat actors have taken it a step further, opting to release such apps directly on app marketplaces while concealing their functionality by masquerading as seemingly harmless news apps. The trading panel is displayed only when a user enters a specific password in the search bar.

Website templates that include hosting can cost as little as $50. A complete pack, including a website with admin access, VPS hosting, mobile app, access to a trading platform, front company incorporation in a tax haven to mask their activities, and registration with the relevant local financial regulator, can start at around $2,500.

"Sophisticated Asian crime syndicates have created a global shadow economy from their safe havens in Southeast Asia," researchers Maël Le Touz and John Wòjcik said. "PBaaS provides the mechanisms to scale an operation with relatively little effort and cost."

### Parked Domains as a Conduit for Scams and Malware

The disclosure comes against the backdrop of a new study from the DNS threat intelligence firm, finding that the vast majority of parked domains – domain names that are mostly expired or dormant, or common misspellings of popular websites (aka typosquatting) – are being used to redirect visitors to sites that serve scams and malware.

Infoblox revealed that visitors to a typosquat of the legitimate domain belonging to a financial institution from a virtual private network (VPN) are shown a normal parking page, but are redirected to scam or malware sites if they are visiting from a residential IP address. The parked pages, for their part, send visitors through a redirect chain, while simultaneously profiling their system using IP geolocation, device fingerprinting, and cookies to determine where to redirect them.

"In large scale experiments, we found that over 90% of the time, visitors to a parked domain would be directed to illegal content, scams, scareware and anti-virus software subscriptions, or malware, as the 'click' was sold from the parking company to advertisers, who often resold that traffic to yet another party," the company
[said](https://www.infoblox.com/blog/threat-intelligence/parked-domains-become-weapons-with-direct-search-advertising/)
. "None of this displayed content was related to the domain name we visited."

### Malicious Evilginx AitM Infrastructure Drives Credential Harvesting

In recent months, it has also emerged that threat actors are leveraging an adversary-in-the-middle (AitM) phishing toolkit named Evilginx in attacks targeting at least 18 universities and educational institutions across the U.S. since April 12, 2025, with an aim to steal login credentials and session cookies. As many as 67 domains have been identified as linked to the activity.

"The low detection rates across the cybersecurity community highlight how effective Evilginx's evasion techniques have become," Infoblox
[said](https://www.infoblox.com/blog/threat-intelligence/dns-uncovers-infrastructure-used-in-sso-attacks/)
. "Recent versions, such as Evilginx Pro, add features that make detection even harder."

"These include default use of wildcard TLS certificates, bot filtering through advanced fingerprinting like JA4, decoy web pages, improved integration with DNS providers (e.g., Cloudflare, DigitalOcean), multi-domain support for phishlets, and JavaScript obfuscation. As Evilginx continues to mature, identifying its phishing URLs will only become more challenging."

### Fraudulent Gambling Network Shows Signs of APT Operation

Last month, researchers from security firm Malanta disclosed details of a sprawling infrastructure spanning more than 328,000 domains and subdomains, including over 236,000 gambling-related domains, that has been active since at least 2011 and is likely a dual operation run by a nation-state-sponsored group targeting victims in the U.S., Europe, and Southeast Asia.

The network, primarily used to target Indonesian-speaking visitors, is assessed to be part of a larger operation that includes thousands of gambling domains, malicious Android applications, hijacking of domains and subdomains hosted on cloud services, and stealth infrastructure embedded inside enterprise and government websites worldwide, researchers Yinon Azar, Noam Yitzhack, Tzur Leibovitz, and Assaf Morag said.

"Blending illegal gambling, SEO manipulation, malware distribution, and highly persistent takeover techniques, this campaign represents one of the largest and most complex Indonesian-speaking, well-funded, state-sponsored-level ecosystems observed to date," Malanta
[said](https://www.malanta.ai/blog-posts/what-if-indonesias-gambling-network-is-actually-a-state-aligned-cyber-operation)
.

The activity involves systematic exploitation of WordPress, PHP components, dangling DNS, and expired cloud assets to hijack and weaponize trusted domains. The infrastructure has also been found to power a massive Android malware ecosystem hosted on Amazon Web Services (AWS) S3 buckets to distribute APK droppers with command-and-control (C2) and data-theft capabilities.

The threat actors behind the scheme rely on social media and instant messaging platforms to advertise the gambling sites and direct users to install the Android apps. As many as 7,700 domains have been flagged containing links to at least 20 AWS S3 buckets staging the APK files (e.g., "jayaplay168.apk" or "1poker-32bit.apk").

Some aspects of the 14-year-old operation were previously highlighted by
[Imperva](https://thehackernews.com/2025/01/python-based-bots-exploiting-php.html)
and
[Sucuri](https://blog.sucuri.net/2025/11/slot-gacor-the-rise-of-online-casino-spam.html)
, with the latter tracking it as an online casino spam campaign dubbed Slot Gacor that was found hijacking existing pages on compromised WordPress websites by replacing them with casino spam pages.

The longevity of the infrastructure, combined with the scale and sophistication, has raised the possibility that it's maintained by an Advanced Persistent Threat (APT) that is deeply embedded in the Indonesian cybercrime ecosystem while actively exploiting governmental virtual assets worldwide.