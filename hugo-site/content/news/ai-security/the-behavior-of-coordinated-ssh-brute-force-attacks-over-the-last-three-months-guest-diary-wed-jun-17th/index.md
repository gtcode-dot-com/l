---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T04:30:35.401511+00:00'
exported_at: '2026-06-23T04:30:36.770512+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33086
structured_data:
  about: []
  author: ''
  description: 'The Behavior of Coordinated SSH Brute Force Attacks over the last
    three months [Guest Diary], Author: Guy Bruneau'
  headline: The Behavior of Coordinated SSH Brute Force Attacks over the last three
    months &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33086
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Behavior of Coordinated SSH Brute Force Attacks over the last three months
  &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)
updated_at: '2026-06-23T04:30:35.401511+00:00'
url_hash: cca40b7d9a3ec6d7fdcea6adc0e26c0fbcb118d0
---

[This is a Guest Diary by Adam Nason, an ISC intern as part of the
[SANS.edu](https://www.sans.edu/cyber-security-programs/bachelors-degree/)
BACS program]

Brute force SSH attacks are an ever-present threat on the internet today. We examine probing behavior over the last three months to identify coordinated and opportunistic attacks by threat actors. A DShield Honeypot has quietly collected and logged the behavior of these threat actors to develop a clearer picture of their malicious intentions. During the log collection period, several significant cyber and geopolitical events occurred. We will take a closer look at these behaviors by analyzing their timing and cross-referencing them with external factors that align with their attack patterns. Can an increase or change in SSH brute force botnet activity be observed during these volatile times?

**Infrastructure Setup and Data Collection Framework – Home Lab**

**Infrastructure**

• Raspberry Pi 4 Model B

• Network Equipment – Isolated from personal home network

o UniFi Security Gateway Pro

o UniFi 24 Port Switch

**Data Ingestion**

• RaspberryOS running on Raspberry Pi

• DShield Honeypot Software

o Logs Collected: 17 Feb 2026 through 26 May 2026

**Software Tools**

• Elasticsearch, Logstash, Kabana (ELK)

• Microsoft VS Code (JSON and Python)

• Microsoft Excel

**Data Analysis of Honeypot Logs**

**Scanning Volume and Timeline Overview**

The cowrie honeypot logs recorded over 20 million SSH brute-force attempts over the past 100 days. Investigation into the scanning trends appears to be closely correlated with Chinese botnets, major law enforcement actions, geopolitical events, and critical cybersecurity advisories released in the first half of 2026. As shown in Figure 1: Daily Brute Force Probing Totals, the timeline shows extended periods of high-volume traffic, with abrupt spikes and drops that seem to align with external events.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic1.png)

Table 1:
*Overview of SSH data collected*

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic2.png)

Figure 1:
*Daily Brute Force Probing Totals*

**Notable events within the brute force scan timeline**

**February 17 – 24 (Initial Baseline)**

The first week of running the honeypot produced what can be considered a quiet baseline of standard background scanning activity. During this period, between 200 and 400 attempts were captured each day.

**February 25 – 28 (Sudden Surge)**

Following a quiet start, a spike of over 2100% attempts was observed by the honeypot. It was during this period that CISA published Emergency Directive 26-03 (CISA, 2026), related to Cisco’s software-defined wide-area network, which led to opportunistic attacks against unpatched systems. Additional probing was observed during this period, which can also be attributed to the rising conflict between Iran, Israel, and the United States (Al Jazeera, 2026).

**March 1 – 8 (Activity Peaks)**

Scanning observations peaked this week, with over 300,000 events collected on March 8th (Radauskas, 2026). This is as tensions continue to rise between Iran, Israel, and the United States, and both advanced persistent threats and opportunistic botnets are becoming more active (Reuters, 2026).

**March 9 – April 14 (Sustained Attacks)**

The honeypot continues to collect and log a high volume of activity during this period, with daily probes remaining above 50,000, often exceeding 100,000 (Le Poidevin, 2026). The periodic spikes and dips tend to lean towards automated attack campaigns.

**April 15 (Rapid Decline)**

Attack observations plummet to just over 23,000 attempts logged by the honeypot.

**April 16 – May 14 (Attack Rebounds)**

With news of new vulnerabilities (CISA, 2026), and tensions growing with the Iran-United States ceasefire, logged scans start to rise again. A second spike is observed on May 2nd with 244,344 probes in a single day. This comes just after 24 hours following a major Linux vulnerability that was published by CISA (CISA, 2026)

**May 15 – 23 (Extended Decline)**

Daily log observations drop nearly 95%, as the ceasefire extends (Madhani et al., 2026), and opportunistic threat actors lose interest as the Iran, Israel, and United States war continues to drag on with minimal active military engagements.

**Top 10 Identified Probing IPs (Patterns, Clusters, and Campaign Data)**

From February 2026 through May 2026, the top ten observed IP addresses (Table 2) appeared to have strong geographic and Autonomous System Number (ASN) clustering. Both DigitalOcean (ASN – AS14061) and M247 (ASN – AS9009) show activity from multiple countries (Table 3). Furthermore, synchronized scanning bursts can be observed using identical SSH client fingerprints and version strings, occurring within minutes of each other across different countries.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic3.png)

Table 2:
*Top Ten Probing IPs, with Country and ASN*

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic4.png)

Table 3:
*Country Clustering of IPs and ASN*

A closer review of the data shows an example of what appears to be synchronized scanning. Over the course of 53 seconds, two attacks are observed from both the United States and Ukraine. Of note, both attacks exhibit the same HASSH fingerprint. HASSH is a fingerprinting standard developed by the Detection Cloud team at Salesforce and is used to detect attacks with higher granularity than a simple IP address can (Reardon, 2022). Seeing the same HASSH, SSH Version, from two different ASNs and countries does point to a high likelihood of a coordinated attack.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic5.png)

Table 4:
*Clustered attack within 53-seconds*

Further review of the collected honeypot logs shows that 702,706 events use the exact same HASSH fingerprint (03a80b21afa810682a776a7d42e5e6fb) and SSH version, indicating the use of a single managed attack toolkit that has been deployed globally (SSHwatch, 2025).

Finally, a detailed review of the logs shows evidence of a botnet quota assignment (Table 5). These are throttled scan rates, which are tell-tale indicators of a botnet-driven SSH campaign. Reviewing the logs over such extended periods shows a low variation and high uniform attack rates, which point to a controller assigning quotas or workloads to the botnet zombies under its control. Automating a scan in this type of organization has been shown to be a characteristic of these types of programmed botnet operations (Sing et al., 2024 p. 1731-1750).

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic6.png)

Table 5:
*Attack Rate Analysis of IPs showing Automated Campaigns*

**Reduce your Attack Surface**

As we have seen above, networks are under constant attack, which seems to follow the ebb and flow of external events on digital cyberspace. However, there are several steps you can take to reduce your attack surface, most of which require little effort. Strategies like IP blocks, geo-blocking, and changing default values can go a long way in preventing a potential compromise.

**Prevention**

• While not specifically noted in this paper, a majority of SSH brute force login attempts observed targeted the user ‘root’. Disabling ‘root’ user login would effectively make all those attack attempts obsolete.

• Enforce Multi-Factor Authentication (MFA).

• Use private keys for SSH, provided they are properly protected, rotated, and audited.

• Properly hardened jump boxes to reduce exposure and enable session monitoring with Security Information and Event Management (SIEM) systems.

(Hartman, 2026)

**Detection**

• Centralized SIEM Log Collection

• Deploy rules to alert to brute force patterns in platforms like Snort or Suricata. This can include ‘SYN Flood Attacks’ against port 22 (or your SSH port if you change the default value).

(Hartman, 2026)

**Conclusion**

Over 20 million SSH brute force attempts were collected by my DShield honeypot over nearly 100 days. This data was compared with several major cybersecurity advisories, changing geopolitical tensions, and law enforcement activities, which uncovered a close alignment. The top probing IPs showed clear signs of SSH botnet attack campaigns when evaluating the log data for attack timing, rates, HASSH fingerprints, and SSH client identification. These findings help to illustrate the adaptability and persistence of threat actors as they respond to capitalize on external events, highlighting the underlying need of all connected devices to be aware not only of cybersecurity-related advisories but also of the activities taking place across the globe. Some of the simplest security measures would have stopped many of these attacks in their tracks, raising the persistent need to continue to remind users to change default settings (usernames and ports) and increase the use of MFA.

Have you observed similar activities in your honeypot or within your organization? Feel free to share your findings and experiences in the comments below or consider joining the SANS Internet Storm Center and contributing data to their global network of sensors and honeypots.

[1] Al Jazeera. (2026, February 28). US, Israel bomb Iran: A timeline of talks and threats leading up to attacks. https://www.aljazeera.com/news/2026/2/28/us-israel-bomb-iran-a-timeline-of-talks-and-threats-leading-up-to-attacks#:~:text=US%2C%20Israel%20bomb%20Iran%3A,since%20the%20June%202025

[2] CISA. (2026, February 25). ED 26-03: Mitigate vulnerabilities in Cisco SD-WAN systems. Cybersecurity and Infrastructure Security Agency CISA. https://www.cisa.gov/news-events/directives/ed-26-03-mitigate-vulnerabilities-cisco-sd-wan-systems

[3] CISA. (2026, May 1). CISA adds one known exploited vulnerability to catalog. Cybersecurity and Infrastructure Security Agency CISA. https://www.cisa.gov/news-events/alerts/2026/05/01/cisa-adds-one-known-exploited-vulnerability-catalog

[4] CISA. (2026, April 20). CISA adds eight known exploited vulnerabilities to catalog. Cybersecurity and Infrastructure Security Agency CISA. https://cisa.gov/news-events/alerts/2026/04/20/cisa-adds-eight-known-exploited-vulnerabilities-catalog

[5] Hartman, K. G. (2026, February 13). Securing SSH keys in cloud environments: Practical guidance for security, forensics, and legal accountability. SANS Institute. https://www.sans.org/blog/securing-ssh-keys-cloud-environments-practical-guidance-security-forensics-legal-accountability

[6] Le Poidevin, O. (2026, March 9). UAE envoy to UN urges de-escalation of US-Israeli war with Iran. reuters.com. https://www.reuters.com/world/middle-east/uae-envoy-un-urges-de-escalation-us-israeli-war-with-iran-2026-03-09/#:~:text=UAE%20envoy%20to%20UN,and%20a%20return%20to

[7] Madhani, A., Gambrell, J., Price, M., &amp; Metz, S. (2026, May 29). US and Iranian negotiators reach tentative deal to extend ceasefire and start new nuclear talks. AP News. https://apnews.com/article/iran-us-war-oil-may-28-2026-8f5ed2813ba63df7ae9ccbe991688d29

[8] Radauskas, G. (2026, March 3). Wild pack without a leader: pro-Iranian hackers already active in wake of US-Israeli strikes. Cybernews. https://cybernews.com/security/iran-war-cyberattacks-hacking/

[9] Reardon, B. (2022, April 14). Open sourcing HASSH. Salesforce Engineering Blog. https://engineering.salesforce.com/open-sourcing-hassh-abed3ae5044c/

[10] Reuters. (2026, February 28). Global reaction to US, Israeli attacks on Iran. reuters.com. https://www.reuters.com/business/aerospace-defense/global-reaction-israeli-us-attacks-iran-2026-02-28/#:~:text=Global%20reaction%20to%20US%2C,into%20a%20renewed%20military

[11] Singh, S. K., Gautam, S., Cartier, C., Patil, S., &amp; Ricci, R. (2024). Where The Wild Things Are: Brute-Force SSH Attacks In The Wild And How To Stop Them. USENIX Association, 1731-1750. https://www.usenix.org/conference/nsdi24/presentation/singh-sachin

[12] SSHwatch. (2025, April 28). SSH honeypots: Detecting and understanding attack patterns. https://www.sshwatch.com/ssh-honeypots-detecting-and-understanding-attack-patterns/#:~:text=Distributed%20credential%20partitioning%2C%20wordlist,logs%20with%20tools%20like

[13] https://www.sans.edu/cyber-security-programs/bachelors-degree/

Note: To ensure full transparency and academic integrity, generative A.I. software (Grammarly) was used for grammar and spelling checks. No further use of generative A.I. was used in the creation of this writing.

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu