---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-24T18:15:15.332044+00:00'
exported_at: '2026-04-24T18:15:17.516614+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/firestarter-backdoor-hit-federal-cisco.html
structured_data:
  about: []
  author: ''
  description: FIRESTARTER backdoor hit Cisco ASA in Sept 2025, persists after patching
    CVE-2025-20333, risking continued federal network access.
  headline: FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security
    Patches
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/firestarter-backdoor-hit-federal-cisco.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security
  Patches
updated_at: '2026-04-24T18:15:15.332044+00:00'
url_hash: fac946ad110cbc4aa57d45f34bef9359c55485bb
---

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has revealed that an unnamed federal civilian agency's Cisco Firepower device running Adaptive Security Appliance (ASA) software was compromised in September 2025 with malware called
**FIRESTARTER**
.

FIRESTARTER, per CISA and the U.K.'s National Cyber Security Centre (NCSC), is
[assessed](https://www.cisa.gov/news-events/analysis-reports/ar26-113a)
to be a backdoor designed for remote access and control. It's believed to be deployed as part of a "widespread" campaign orchestrated by an advanced persistent threat (APT) actor to obtain access to Cisco Adaptive Security Appliance (ASA) firmware by exploiting
[now-patched security flaws](https://thehackernews.com/2025/11/cisco-warns-of-new-firewall-attack.html)
such as -

* **CVE-2025-20333**
  (CVSS score: 9.9) - An improper validation of user-supplied input vulnerability that could allow an authenticated, remote attacker with valid VPN user credentials to execute arbitrary code as root on an affected device by sending crafted HTTP requests.
* **CVE-2025-20362**
  (CVSS score: 6.5) - An improper validation of user-supplied input vulnerability that could allow an unauthenticated, remote attacker to access restricted URL endpoints without authentication by sending crafted HTTP requests.

"FIRESTARTER can persist as an active threat on Cisco devices running ASA or Firepower Threat Defense (FTD) software, maintaining post-patching persistence and enabling threat actors to re-access compromised devices without re-exploiting vulnerabilities," the agencies said.

In the investigated incident, the threat actors have been found to deploy a post-exploitation toolkit called
[LINE VIPER](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.html)
that can execute CLI commands, perform packet captures, bypass VPN Authentication, Authorization, and Accounting (AAA) for actor devices, suppress syslog messages, harvest user CLI commands, and force a delayed reboot.

The elevated access afforded by LINE VIPER served as a conduit for FIRESTARTER, which was deployed on the Firepower device before September 25, 2025, allowing the threat actors to maintain continued access and return to the compromised appliance as recently as last month.

A Linux ELF binary, FIRESTARTER can set up persistence on the device, and survive firmware updates and device reboots unless a hard power cycle occurs. The malware lodges itself into the device's boot sequence by manipulating a startup mount list, ensuring it automatically reactivates every time the device reboots normally. The resilience aside, it also shares some level of overlap with a previously documented bootkit referred to as RayInitiator.

"FIRESTARTER attempts to install a hook – a way to intercept and modify normal operations – within LINA, the device’s core engine for network processing and security functions," according to the advisory. "This hook enables the execution of arbitrary shell code provided by the APT actors, including the deployment of LINE VIPER."

"Although Cisco's patches addressed CVE-2025-20333 and CVE-2025-20362, devices compromised prior to patching may remain vulnerable because FIRESTARTER is not removed by firmware updates."

Cisco, which is tracking the exploitation activity associated with the two vulnerabilities under the moniker
[UAT4356](https://thehackernews.com/2024/04/state-sponsored-hackers-exploit-two.html)
(aka Storm-1849),
[described](https://blog.talosintelligence.com/uat-4356-firestarter/)
FIRESTARTER as a backdoor that facilitates the execution of arbitrary shellcode received by the LINA process by parsing specially crafted WebVPN authentication requests containing a "magic packet."

The exact origins of the threat activity are not known, although an
[analysis](https://thehackernews.com/2024/05/china-linked-hackers-suspected-in.html)
from attack surface management platform Censys in May 2024 suggested links to China. UAT4356 was first attributed to a campaign called ArcaneDoor that exploited two zero-day flaws in Cisco networking gear to deliver bespoke malware capable of capturing network traffic and reconnaissance.

"To fully remove the persistence mechanism, Cisco strongly recommends reimaging and upgrading the device," Cisco
[said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-persist-CISAED25-03)
. "In cases of confirmed compromise on any Cisco Secure ASA or FTD platforms, all configuration elements of the device should be considered untrusted."

As mitigations until reimaging can be performed, the company is recommending that customers perform a cold restart to remove the FIRESTARTER implant. "The shutdown, reboot, and reload CLI commands will not clear the malicious persistent implant, the power cord must be pulled out and plugged back in the device," it added.

### Chinese Hackers Shift From Individually Procured Infrastructure to Covert Networks

The disclosure comes as the U.S., the U.K., and various international partners
[released](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-113a)
a joint advisory about large-scale networks of compromised SOHO routers and IoT devices commandeered by China-nexus threat actors to disguise their espionage attacks and complicate attribution efforts.

State-sponsored groups like
[Volt Typhoon](https://thehackernews.com/2024/02/after-fbi-takedown-kv-botnet-operators.html)
and
[Flax Typhoon](https://thehackernews.com/2024/09/new-raptor-train-iot-botnet-compromises.html)
have been using these botnets, consisting of home routers, security cameras, video recorders, and other IoT devices, to target critical infrastructure sectors and conduct cyber espionage in a "low-cost, low-risk, deniable way," per the alert.

Complicating matters further is the fact that the networks are constantly updated, not to mention multiple China-affiliated threat groups might use the same botnet at the same time, making it challenging for defenders to identify and block them using static IP blocklists.

"Covert networks mostly consist of compromised SOHO routers, but they also pull in any vulnerable device they can exploit at scale," the agencies said. "Their traffic will be forwarded through multiple compromised devices, used as traversal nodes, before exiting the network from an exit node, usually in the same geographic region as the target."

The findings underscore a common pattern seen in state-sponsored attacks: the targeting of network perimeter devices belonging to residential, enterprise, and government networks with an aim to either turn them into a proxy node or intercept sensitive data and communications.