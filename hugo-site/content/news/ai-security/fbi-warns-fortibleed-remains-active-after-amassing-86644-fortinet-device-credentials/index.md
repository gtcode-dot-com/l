---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T03:53:09.429203+00:00'
exported_at: '2026-10-08T03:53:10.957759+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/fbi-warns-fortibleed-remains-active.html
structured_data:
  about: []
  author: ''
  description: FBI and USSS warn FortiBleed remains active, using stolen credentials
    and traffic sniffing to harvest Fortinet authentication data.
  headline: FBI Warns FortiBleed Remains Active After Amassing 86,644 Fortinet Device
    Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/fbi-warns-fortibleed-remains-active.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FBI Warns FortiBleed Remains Active After Amassing 86,644 Fortinet Device Credentials
updated_at: '2026-10-08T03:53:09.429203+00:00'
url_hash: 9f1a8977892018e92868669c6ec02440bf608392
---

**

Ravie Lakshmanan
**

Oct 07, 2026

Cybercrime / Network Security

The U.S. Federal Bureau of Investigation (FBI) and Secret Service (USSS) on Tuesday warned that the FortiBleed credential harvesting campaign remains an active threat aimed at internet-facing Fortinet FortiGate firewalls and secure socket layer (SSL) virtual private network (VPN) gateways.

"The campaign exploits reused or leaked credentials and legacy SHA-256 password storage, enabling threat actors to harvest and crack authentication data at scale," the agencies
[said](https://www.ic3.gov/CSA/2026/261006.pdf)
. "Initial findings indicate attackers are continuing to scan internet-exposed Fortinet firewalls using previously obtained compromised credentials."

FortiBleed was
[first documented](https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html)
by SOCRadar in Hudson Rock in June 2026, with the activity targeting thousands of Fortinet firewalls as part of a global campaign. In all, the Russian-speaking operation is estimated to have netted more than 86,644 working device credentials spanning 194 countries as of June 19, 2026.

The campaign subsequently prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to
[urge](https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html)
Fortinet customers with FortiGate appliances to enable phishing-resistant authentication, terminate active SSL VPN and administrative sessions, reset Fortinet VPN and administrative passwords, use the Password-Based Key Derivation Function 2 (PBKDF2) algorithm to store administrator credentials, and review logs for signs of suspicious activity.

FortiBleed is a
[five-stage campaign](https://thehackernews.com/2026/06/fortibleed-targeted-fortigate-firewalls.html)
that conducts widespread reconnaissance to identify exposed portals, gain access to those devices using credential stuffing and password spraying based on data obtained from prior leak dumps and infostealer logs, and then deploy a Go-based tool called FortigateSniffer to passively intercept authentication traffic across 24 protocols and harvest credentials and password hashes.

The password hashes are then routed to a GPU-accelerated cracking cluster that uses Hashmat and Hashtopolis for offline cracking, after which they are used to facilitate lateral movement, Active Directory enumeration, Kerberos validation, and SMB authentication. In the final stage, sensitive data from network shares is exfiltrated while stolen session cookies are used to maintain persistent, authenticated access.

"Cracked credentials were enriched, sorted, and validated, with scripts filtering out honeypots, mapping organizations, and prioritizing high-value targets based on revenue and network structure," the agencies said. "New administrative accounts were created on the firewall to maintain persistence."

With the verified credentials in hand, the attackers have been found to move deeper into victim environments, conduct enumeration, and conduct password spraying to expand access and identify privileged accounts.

In addition, the initial access is used to add new accounts to the system as a way of maintaining persistence on the appliance. Some of the commonly identified compromised account names is listed below -

* adminin
* fortiAdmin
* forticloud-sync
* admin
* fgtsecure
* pakedge
* forticloud-tech
* districtadmin
* system\_config
* gttadmin
* roadmin
* itadmin
* Technical\_support
* adminsslvpn
* IT\_Manager
* my\_admin
* support\_fortinet
* fgtsec
* forti\_support2

The adversary is suspected to be an initial access broker that packages the stolen information and sells it to downstream threat actors. This is evidenced by the fact that operator overlaps tying FortiBleed to
[INC and Lynx ransomware operations](https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html)
, likely indicating that the access is being abused for ransomware deployment.

"Based on initial responses, some victims may get locked out of their Fortinet devices if the threat actor either deletes or changes the password for original accounts on the system," the FBI and USSS warned.

"During the initial intrusion, threat actors create new accounts not previously on the device. In certain cases, threat actors delete existing accounts to block organizations from accessing affected devices and to maintain persistence on the system while attempting lateral movement within the environment."

If potential compromise is detected, organizations are advised to isolate the affected devices, collect necessary artifacts and logs, report the incident to the FBI and USSS, and apply relevant countermeasures to mitigate the threat.