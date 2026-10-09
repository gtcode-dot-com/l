---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-02T02:15:14.729829+00:00'
exported_at: '2026-05-02T02:15:17.763920+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/cybercrime-groups-using-vishing-and-sso.html
structured_data:
  about: []
  author: ''
  description: Two groups exploit SaaS via vishing since Oct 2025, stealing credentials
    to access multiple apps, enabling rapid data theft and extortion
  headline: Cybercrime Groups Using Vishing and SSO Abuse in Rapid SaaS Extortion
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/cybercrime-groups-using-vishing-and-sso.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cybercrime Groups Using Vishing and SSO Abuse in Rapid SaaS Extortion Attacks
updated_at: '2026-05-02T02:15:14.729829+00:00'
url_hash: 40a5d9dea62a5d9983cc8856c7eea269f5ac8f00
---

**

Ravie Lakshmanan
**

May 01, 2026

Malware / Social Engineering

Cybersecurity researchers are warning of two cybercrime groups that are carrying out "rapid, high-impact attacks" operating almost within the confines of SaaS environments, while leaving minimal traces of their actions.

The clusters,
**[Cordial Spider](https://www.crowdstrike.com/en-us/adversaries/cordial-spider/)**
(aka BlackFile, CL-CRI-1116, O-UNC-045, and UNC6671) and
**[Snarky Spider](https://www.crowdstrike.com/en-us/adversaries/snarky-spider/)**
(aka O-UNC-025 and UNC6661), have been attributed to high-speed data theft and extortion campaigns that share a remarkable degree of operational similarities. Both hacking groups are assessed to be active since at least October 2025, with the latter a native English-speaking crew sharing ties to the e-crime ecosystem known as
[The Com](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)
.

"In most cases, these adversaries use voice phishing (vishing) to direct targeted users to malicious, SSO-themed adversary-in-the-middle (AiTM) pages, where they capture authentication data and pivot directly into SSO-integrated SaaS applications," CrowdStrike's Counter Adversary Operations
[said](https://www.crowdstrike.com/en-us/blog/defending-against-cordial-spider-and-snarky-spider-with-falcon-shield/)
in a report.

"By operating almost exclusively within trusted SaaS environments, they minimize their footprint while accelerating time to impact. The combination of speed, precision, and SaaS-only activity creates significant detection and visibility challenges for defenders."

In a report published back in January 2026, Google-owned Mandiant
[revealed](https://thehackernews.com/2026/01/mandiant-finds-shinyhunters-using.html)
that the two clusters represent an expansion in threat activity that employs tactics consistent with extortion-themed attacks carried out by the ShinyHunters group. This involves impersonating IT staff in calls to deceive victims and obtain their credentials and multi-factor authentication (MFA) codes by directing them to phishing pages.

|  |
| --- |
|  |
| Snarky Spider begins exfiltration in under an hour |

As recently as last week, Palo Alto Networks Unit 42 and Retail & Hospitality Information Sharing and Analysis Center (RH-ISAC)
[assessed](https://rhisac.org/threat-intelligence/extortion-in-the-enterprise-defending-against-blackfile-attacks/)
with moderate confidence that the attackers behind CL-CRI-1116 are also most likely associated with The Com, adding that the intrusions primarily rely on living-off-the-land (LotL) techniques, as well as utilize residential proxies to conceal their geographic location and bypass basic IP-based reputation filters.

"CL-CRI-1116 activity has been actively targeting the retail and hospitality space since February 2026, specifically leveraging vishing attacks
[impersonating IT help desk personnel](https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html)
in combination with phishing login sites to steal credentials," researchers Lee Clark, Matt Brady, and Cuong Dinh said.

Attacks mounted by the two groups are known to register a new device in order to bypass MFA and maintain access to compromised access -- but not before removing existing devices -- following which the threat actors move to suppress automated email notifications related to unauthorized device registration by configuring inbox rules that automatically delete such messages.

The next stage entails pivoting to targeting high-privileged accounts via further social engineering by scraping internal employee directories. Upon again elevated access, the adversaries break into target SaaS environments to look for high-value files and business-critical reports in Google Workspace, HubSpot, Microsoft SharePoint, and Salesforce, and then exfiltrate data of interest to infrastructure under its control.

"In most observed cases, these credentials grant access to the organization's identity provider (IdP), providing a single point of entry into multiple SaaS applications," CrowdStrike said. "By abusing the trust relationship between the IdP and connected services, the adversaries bypass the need to compromise individual SaaS apps and instead move laterally across the victim's entire SaaS ecosystem with a single authenticated session."