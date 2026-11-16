---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T18:53:47.651468+00:00'
exported_at: '2026-11-16T18:53:48.565844+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/hackers-probe-newly-disclosed-flaws-in-copeland-refrigeration-controllers
structured_data:
  about: []
  author: ''
  description: Vulncheck disclosed 14 vulnerabilities affecting Copeland XWEB EVO
    controllers, including two that threat actors quickly targeted.
  headline: Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/hackers-probe-newly-disclosed-flaws-in-copeland-refrigeration-controllers
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers
updated_at: '2026-11-16T18:53:47.651468+00:00'
url_hash: 2aba980e2462894f857dc0f487ddf270cab2ae4d
---

**Exploitation attempts against a vulnerability in Copeland’s XWEB EVO refrigeration controllers began less than two hours after the issue was made public last week, according to VulnCheck.**

The security firm disclosed 14 vulnerabilities in XWEB EVO, a Dixell supervisory system now sold under the Copeland name. VulnCheck’s Valentin Lobstein said each flaw was shown to yield root privileges on test systems.

The product drew the researcher’s attention after the
[October 11-12 attack](https://www.securityweek.com/refrigeration-controller-hack-spoils-food-across-european-supermarkets/)
that triggered defrost cycles at roughly 700 French supermarkets. CERT-FR named
[Copeland and Dixell XWEB controllers](https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/)
among the compromised products, and France has
[blamed Iran](https://www.securityweek.com/france-blames-iran-for-a-cyberattack-that-heated-supermarket-refrigerators/)
for the campaign.

Nine of the flaws disclosed by VulnCheck only affect firmware builds that predate a 2021 rewrite. They include unauthenticated command execution, a hardcoded administrator password, and command injection via the login page.

The other five vulnerabilities also impact the latest firmware. Four of them involve predictable credentials: the administrator’s daily password is generated from the device’s MAC address and the current date, and the MAC address is exposed to unauthenticated users.

An attacker can calculate the password offline, enable SSH, and log in as root, since the root password is built from the same daily code. The fifth flaw is a command injection issue that requires authentication.

Advertisement. Scroll to continue reading.

These five issues will not be fixed. Copeland
[ended software support](https://webapps.copeland.com/dixell/Content/Pages/SystemSoftwareUpdate/XWEB30005000-EVO/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf)
for the XWEB EVO family on March 16, 2026, and has advised customers to move to XWEB Pro models.

The CVE records were published on November 12, and VulnCheck’s sensors saw the first exploitation attempts within two hours. They targeted CVE-2026-124014, which allows unauthenticated attackers to write to the system configuration file.

A single IP address sent 125 requests overnight. On November 13, a second IP sent four probes aimed at CVE-2026-124010, the unauthenticated root command execution flaw. Both targeted flaws only affect the older firmware.

“Neither scanning source is evidence of the October refrigeration campaign that France attributed to Iran’s IRGC unit Shahid Kaveh: that was a targeted sabotage operation, while these are opportunistic hosts acting on fresh advisories,” Lobstein
[said](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root)
.

Onyphe data cited by VulnCheck shows nearly 2,000 internet-exposed XWEB EVO hosts, compared with 108 for XWEB Pro.

“Operators who still run one should treat it as a device that must never touch the public internet, segment it behind a VPN, and plan the move to a supported platform,” the researcher added.

**Related**
:
[Cyberattack Hits French Blood Bank Site but No Blood Products Are Compromised](https://www.securityweek.com/cyberattack-hits-french-blood-bank-site-but-no-blood-products-are-compromised/)

**Related**
:
[Over 100 European Stores Hit as Supermarket Fridge Attacks Return](https://www.securityweek.com/over-100-european-stores-hit-as-supermarket-fridge-attacks-resume/)

**Related**
:
[US Agencies Urge Organizations to Harden Refrigeration Controllers](https://www.securityweek.com/us-agencies-urge-organizations-to-harden-refrigeration-controllers/)