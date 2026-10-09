---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-19T04:44:04.284445+00:00'
exported_at: '2025-12-19T04:44:07.573620+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/new-forumtroll-phishing-attacks-target.html
structured_data:
  about: []
  author: ''
  description: Kaspersky reports ForumTroll phishing attacks targeting Russian academics,
    using fake eLibrary emails, personalized files & Windows malware delivery.
  headline: New ForumTroll Phishing Attacks Target Russian Scholars Using Fake eLibrary
    Emails
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/new-forumtroll-phishing-attacks-target.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New ForumTroll Phishing Attacks Target Russian Scholars Using Fake eLibrary
  Emails
updated_at: '2025-12-19T04:44:04.284445+00:00'
url_hash: c33236963603183c90e13b8a83d84bebd1aa70f2
---

**

Dec 17, 2025
**

Ravie Lakshmanan

Vulnerability / Malware

The threat actor linked to
**Operation ForumTroll**
has been attributed to a fresh set of phishing attacks targeting individuals within Russia, according to Kaspersky.

The Russian cybersecurity vendor said it detected the new activity in October 2025. The origins of the threat actor are presently unknown.

"While the spring cyberattacks focused on organizations, the fall campaign honed in on specific individuals: scholars in the field of political science, international relations, and global economics, working at major Russian universities and research institutions," security researcher Georgy Kucherin
[said](https://securelist.com/operation-forumtroll-new-targeted-campaign/118492/)
.

Operation ForumTroll
[refers](https://thehackernews.com/2025/10/chrome-zero-day-exploited-to-deliver.html)
to a series of sophisticated phishing attacks exploiting a then-zero-day vulnerability in Google Chrome (CVE-2025-2783) to deliver the LeetAgent backdoor and a spyware implant known as Dante.

The latest attack wave also commences with emails that claimed to be from eLibrary, a Russian scientific electronic library, with the messages sent from the address "support@e-library[.]wiki." The domain was registered in March 2025, six months before the start of the campaign, suggesting that preparations for the attack had been underway for some time.

Kaspersky said the
[strategic domain aging](https://thehackernews.com/2023/05/new-decoy-dog-malware-toolkit-uncovered.html)
was done to avoid raising any red flags typically associated with sending emails from a freshly registered domain. In addition, the attackers also hosted a copy of the legitimate eLibrary homepage ("elibrary[.]ru") on the bogus domain to maintain the ruse.

The emails instruct prospective targets to click on an embedded link pointing to the malicious site to download a plagiarism report. Should a victim follow through, a ZIP archive with the naming pattern "<LastName>\_<FirstName>\_<Patronymic>.zip" is downloaded to their machine.

What's more, these links are designed for one-time use, meaning any subsequent attempts to navigate to the URL cause it to display a Russian language message stating "Download failed, please try again later." In the event, the download is attempted from a platform other than Windows, the user is prompted to "try again later on a Windows computer."

"The attackers also carefully personalized the phishing emails for their targets, specific professionals in the field," the company said. "The downloaded archive was named with the victim's last name, first name, and patronymic."

The archive contains a Windows shortcut (LNK) with the same name, which, when executed, runs a PowerShell script to download and launch a PowerShell-based payload from a remote server. The payload then contacts a URL to fetch a final-stage DLL and persist it using COM hijacking. It also downloads and displays a decoy PDF to the victim.

The final payload is a command-and-control (C2) and red teaming framework known as
[Tuoni](https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html)
, enabling the threat actors to gain remote access to the victim's Windows device.

"ForumTroll has been targeting organizations and individuals in Russia and Belarus since at least 2022," Kaspersky said. "Given this lengthy timeline, it is likely this APT group will continue to target entities and individuals of interest within these two countries."

The disclosure comes as Positive Technologies
[detailed](https://global.ptsecurity.com/en/research/pt-esc-threat-intelligence/dragons-in-thunder/#id1)
the activities of two threat clusters,
[QuietCrabs](https://thehackernews.com/2025/04/critical-ivanti-flaw-actively-exploited.html)
– a suspected Chinese hacking group also tracked as UTA0178 and UNC5221 – and
[Thor](https://www.angarasecurity.ru/news/3384/)
, which appears to be involved in ransomware attacks since May 2025.

These intrusion sets have been found to leverage security flaws in Microsoft SharePoint (
[CVE-2025-53770](https://thehackernews.com/2025/07/critical-microsoft-sharepoint-flaw.html)
), Ivanti Endpoint Manager Mobile (
[CVE-2025-4427 and CVE-2025-4428](https://thehackernews.com/2025/09/cisa-warns-of-two-malware-strains.html)
), Ivanti Connect Secure (
[CVE-2024-21887](https://thehackernews.com/2024/01/chinese-hackers-exploit-zero-day-flaws.html)
), and Ivanti Sentry (
[CVE-2023-38035](https://thehackernews.com/2023/08/ivanti-warns-of-critical-zero-day-flaw.html)
).

Attacks carried out by QuietCrabs take advantage of the initial access to deploy an ASPX web shell and use it to deliver a JSP loader that's capable of downloading and executing
[KrustyLoader](https://thehackernews.com/2024/01/chinese-hackers-exploiting-critical-vpn.html)
, which then drops the
[Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html)
implant.

"Thor is a threat group first observed in attacks against Russian companies in 2025," researchers Alexander Badayev, Klimentiy Galkin, and Vladislav Lunin said. "As final payloads, the attackers use LockBit and Babuk ransomware, as well as Tactical RMM and MeshAgent to maintain persistence."