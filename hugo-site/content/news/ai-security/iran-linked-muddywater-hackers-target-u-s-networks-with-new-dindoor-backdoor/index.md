---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-06T22:52:43.745183+00:00'
exported_at: '2026-03-06T22:52:46.120279+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html
structured_data:
  about: []
  author: ''
  description: Iran-linked MuddyWater hackers breached U.S. networks with new Dindoor
    malware as regional cyber attacks escalate amid Middle East conflict.
  headline: Iran-Linked MuddyWater Hackers Target U.S. Networks With New Dindoor Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Iran-Linked MuddyWater Hackers Target U.S. Networks With New Dindoor Backdoor
updated_at: '2026-03-06T22:52:43.745183+00:00'
url_hash: d3ac49878da41b13cfbe7dbf99db14e25041dac5
---

New research from Broadcom's Symantec and Carbon Black Threat Hunter Team has
[discovered](https://www.security.com/threat-intelligence/iran-cyber-threat-activity-us)
evidence of an Iranian hacking group embedding itself in several U.S. companies' networks, including banks, airports, non-profit, and the Israeli arm of a software company.

The activity has been attributed to a state-sponsored hacking group called
**[MuddyWater](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)**
(aka Seedworm). It's affiliated with the Iranian Ministry of Intelligence and Security (MOIS). The campaign is assessed to have begun in early February, with recent activity detected following
[U.S. and Israeli military strikes on Iran](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html)
.

"The software company is a supplier to the defense and aerospace industries, among others, and has a presence in Israel, with the company's Israel operation seeming to be the target in this activity," the security vendor said in a report shared with The Hacker News.

The attacks targeting the software company, as well as a U.S. bank and a Canadian non-profit, have been found to pave the way for a previously unknown backdoor dubbed Dindoor, which leverages the
[Deno](https://deno.com/)
JavaScript runtime for execution. Broadcom said it also identified an attempt to exfiltrate data from the software company using the Rclone utility to a Wasabi cloud storage bucket. However, it's currently not known if the effort paid off.

Also found in the networks of a U.S. airport and a non-profit was a separate Python backdoor called Fakeset, which was downloaded from servers belonging to Backblaze, an American cloud storage and data backup company. The digital certificate used to sign Fakeset has also been used to sign Stagecomp and Darkcomp malware, both previously linked to MuddyWater.

"While this malware wasn't seen on the targeted networks, the use of the same certificates suggests the same actor -- namely Seedworm -- was behind the activity on the networks of the U.S. companies," Symantec and Carbon Black said.

"Iranian threat actors have become increasingly proficient in recent years. Not only has their tooling and malware improved, but they've also demonstrated strong social engineering capabilities, including spear-phishing campaigns and 'honeytrap' operations used to build relationships with targets of interest to gain access to accounts or sensitive information."

The findings come against the backdrop of an escalating military conflict in Iran, triggering a barrage of cyber attacks in the digital sphere. Recent research from Check Point has uncovered the pro-Palestinian hacktivist group known as Handala Hack (aka Void Manticore) routing its operations through Starlink IP ranges to probe externally facing applications for misconfigurations and weak credentials.

In recent months, multiple
[Iran-nexus adversaries](https://www.tenable.com/blog/operation-epic-fury-potential-iranian-cyber-counteroffensive-operations)
, such as
[Agrius](https://thehackernews.com/2023/11/iranian-hackers-launches-destructive.html)
(aka Agonizing Serpens, Marshtreader, and Pink Sandstorm), have also
[observed](https://blog.checkpoint.com/research/what-defenders-need-to-know-about-irans-cyber-capabilities/)
scanning for vulnerable Hikvision cameras and video intercom solutions using known security flaws such as
[CVE-2017-7921](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html)
and
[CVE-2023-6895](https://nvd.nist.gov/vuln/detail/CVE-2023-6895)
.

The targeting, per Check Point, has intensified in the wake of the current Middle East conflict. The exploitation attempts against IP cameras have witnessed a surge in Israel and Gulf countries, including the U.A.E., Qatar, Bahrain, and Kuwait, along with Lebanon and Cyprus. The activity has singled out cameras from Dahua and Hikvision, weaponizing the two aforementioned vulnerabilities, as well as
[CVE-2021-36260](https://nvd.nist.gov/vuln/detail/CVE-2021-36260)
,
[CVE-2025-34067](https://nvd.nist.gov/vuln/detail/CVE-2025-34067)
, and
[CVE-2021-33044](https://nvd.nist.gov/vuln/detail/cve-2021-33044)
.

"Taken together, these findings are consistent with the assessment that Iran, as part of its doctrine, leverages camera compromise for operational support and ongoing battle damage assessment (BDA) for missile operations, potentially in some cases prior to missile launches," the company
[said](https://research.checkpoint.com/2026/interplay-between-iranian-targeting-of-ip-cameras-and-physical-warfare-in-the-middle-east/)
.

"As a result, tracking camera-targeting activity from specific, attributed infrastructures may serve as an early indicator of potential follow-on kinetic activity."

The U.S. and Israel's war with Iran has also prompted an advisory from the Canadian Centre for Cyber Security (CCCS), which
[cautioned](https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-iranian-cyber-threat-response-usisrael-strikes-february-2026)
that Iran will likely use its cyber apparatus to stage retaliatory attacks against critical infrastructure and information operations to further the regime's interests.

Some other key developments that have unfolded in recent days are listed below -

* Israeli intelligence agencies
  [hacked](https://www.calcalistech.com/ctechnews/article/syimwdmfzl)
  into Tehran's extensive traffic camera network for years to monitor the movements of bodyguards of Ayatollah Ali Khamenei and other top Iranian officials in the lead up to the assassination of the supreme leader last week, the Financial Times
  [reported](https://www.ft.com/content/bf998c69-ab46-4fa3-aae4-8f18f7387836)
  .
* Iran's Islamic Revolutionary Guard Corps (IRGC) targeted Amazon's data center in Bahrain for the company's support of the "enemy's military and intelligence activities," state media Fars News Agency
  [said](https://t.me/farsna/415292)
  on Telegram.
* Active wiper campaigns are said to be underway against Israeli energy, financial, government, and utilities sectors. "Iran's wiper arsenal includes 15+ families (ZeroCleare, Meteor, Dustman, DEADWOOD, Apostle, BFG Agonizer, MultiLayer, PartialWasher, and others)," Anomali
  [said](https://www.anomali.com/blog/cyber-threat-briefing-iran-retaliatory-posture)
  .
* Iranian state-sponsored APT groups like MuddyWater, Charming Kitten, OilRig, Elfin, and Fox Kitten "demonstrated clear signs of activation and rapid retooling, positioning themselves for retaliatory operations amid the escalating conflict," LevelBlue
  [said](https://www.levelblue.com/blogs/spiderlabs-blog/levelblue-spiderlabs-breaks-down-the-role-of-cyber-operations-taken-in-the-iran-crisis)
  , adding "cyber represents one of Iran's most accessible asymmetric tools for retaliation against Gulf states that condemned its attacks and support U.S. operations."
* According to Flashpoint, a massive #OpIsrael cyber campaign involving pro-Russian and pro-Iranian actors has targeted Israeli industrial control systems (ICS) and government portals across Kuwait, Jordan, and Bahrain. The campaign is driven by NoName057(16), Handala Hack, Fatemiyoun Electronic Team, and Cyber Islamic Resistance (aka 313 Team).
* Between 28 February 2026 and 2 March 2026, pro-Russia hacktivist group Z-Pentest claimed responsibility for compromising several U.S.-based entities, including ICS and SCADA systems and multiple CCTV networks. "The timing of these unverified claims, coinciding with Operation Epic Fury, suggests Z-Pentest likely began prioritizing U.S. entities as targets," Adam Meyers, head of Counter Adversary Operations at CrowdStrike, told The Hacker News.

"Iran's offensive cyber capability has matured into a durable instrument of state power used to support intelligence collection, regional influence, and strategic signaling during periods of geopolitical tension," UltraViolet Cyber
[said](https://www.uvcyber.com/resources/reports/threat-advisory-special-report-iranian-threat-actor-group-update)
. "A defining feature of Iran's current cyber doctrine is its emphasis on identity and cloud control planes as the primary attack surface."

"Rather than prioritizing zero-day exploitation or highly novel malware at scale, Iranian operators tend to focus on repeatable access techniques such as credential theft, password spraying, and social engineering, followed by persistence through widely deployed enterprise services."

Organizations are advised to bolster their cybersecurity posture, strengthen monitoring capabilities, limit exposure to the internet, disable remote access to operational technology (OT) systems, enforce phishing-resistant multi-factor authentication (MFA), implement network segmentation, take offline backups, and ensure that all internet-facing applications, VPN gateways, and edge devices are up-to-date

"Western organizations should continue to remain on high-alert for potential cyber response as the conflict continues and activity may move beyond hacktivism and into destructive operations," Meyers said.