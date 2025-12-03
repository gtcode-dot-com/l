---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-03T00:03:08.496505+00:00'
exported_at: '2025-12-03T00:03:10.830450+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html
structured_data:
  about: []
  author: ''
  description: MuddyWater is targeting multiple Israeli sectors using its new MuddyViper
    backdoor, advanced loaders, and credential-stealing tools.
  headline: Iran-Linked Hackers Hits Israeli Sectors with New MuddyViper Backdoor
    in Targeted Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Iran-Linked Hackers Hits Israeli Sectors with New MuddyViper Backdoor in Targeted
  Attacks
updated_at: '2025-12-03T00:03:08.496505+00:00'
url_hash: afe74fc571818bd5be8b5859aac628189ebf0192
---

Israeli entities spanning academia, engineering, local government, manufacturing, technology, transportation, and utilities sectors have emerged as the target of a new set of attacks undertaken by Iranian nation-state actors that have delivered a previously undocumented backdoor called MuddyViper.

The activity has been
[attributed](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
by ESET to a hacking group known as
**[MuddyWater](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html)**
(aka Mango Sandstorm or TA450), a cluster assessed to be affiliated with Iran's Ministry of Intelligence and Security (MOIS). The attacks also singled out one technology company based in Egypt.

The
[hacking group](https://thehackernews.com/2023/06/from-muddyc3-to-phonyc2-irans.html)
first came to light in November 2017, when Palo Alto Networks Unit 42
[detailed](https://unit42.paloaltonetworks.com/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/)
targeted attacks against the Middle East between February and October of that year using a custom backdoor dubbed POWERSTATS. It's also known for its destructive attacks on Israeli organizations using a Thanos ransomware variant called PowGoop as part of a campaign referred to as
[Operation Quicksand](https://www.clearskysec.com/operation-quicksand/)
.

According to
[data](https://www.gov.il/BlobFolder/reports/maddy_water_2024/en/ALERT_CERT_IL_W_1858.pdf)
from the Israel National Cyber Directorate (INCD), MuddyWater's attacks have aimed at the country's local authorities, civil aviation, tourism, healthcare, telecommunications, information technology, and small and medium-sized enterprises (SMEs).

Typical attack chains involve techniques like spear-phishing and the exploitation of known vulnerabilities in VPN infrastructure to infiltrate networks and deploy legitimate remote management tools – a long-favored approach of MuddyWater. However, at least since May 2024, the phishing campaigns have delivered a backdoor known as
[BugSleep](https://thehackernews.com/2024/07/iranian-hackers-deploy-new-bugsleep.html)
(aka MuddyRot).

Some of the other notable tools in its arsenal include a Blackout, a remote administration tool (RAT); AnchorRat, a RAT that offers file upload and command execution features; CannonRat, a RAT that can receive commands and transmit information;
[Neshta](https://thehackernews.com/2024/07/new-hardbit-ransomware-40-uses.html)
, a known file infector virus; and Sad C2, a command-and-control (C2) framework that delivers a loader called TreasureBox, which deploys the BlackPearl RAT for remote control, and a binary known as Pheonix to download payloads from the C2 server.

The cyber espionage group has a track record of striking a wide range of industries, specifically governments and critical infrastructure, using a mix of custom malware and publicly available tools. The latest attack sequence begins, as in previous campaigns, with phishing emails containing PDF attachments that link to legitimate remote desktop tools like Atera, Level, PDQ, and SimpleHelp.

The campaign is marked by the use of a loader named Fooder that's designed to decrypt and execute the C/C++-based MuddyViper backdoor. Alternatively, the C/C++ loader has also been found to deploy go-socks5 reverse tunneling proxies and an open-source utility called
**HackBrowserData**
to collect browser data from several browsers, with the exception of Safari in Apple macOS.

"MuddyViper enables the attackers to collect system information, execute files and shell commands, transfer files, and exfiltrate Windows login credentials and browser data," the Slovak cybersecurity company said in a report shared with The Hacker News.

In all, the backdoor supports 20 commands that facilitate covert access and control of infected systems. A number of Fooder variants impersonate the classic Snake game, while incorporating delayed execution to evade detection. MuddyWater's use of Fooder was
[first highlighted](https://thehackernews.com/2025/09/unc1549-hacks-34-devices-in-11-telecom.html)
by Group-IB in September 2025.

Also used in the attacks are the following tools -

* VAXOne, a backdoor that impersonates Veeam, AnyDesk, Xerox, and the OneDrive updater service
* CE-Notes, a browser-data stealer that attempts to bypass Google Chrome's
  [app-bound encryption](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
  by stealing the encryption key stored in the Local State file of Chromium-based browsers (shares similarities with the open-source
  **ChromElevator**
  project)
* Blub, a C/C++ browser-data stealer that gathers user login data from Google Chrome, Microsoft Edge, Mozilla Firefox, and Opera
* LP-Notes, a credential stealer written in C/C++ that tricks users into entering their system username and password by displaying a fake Windows Security dialog

"This campaign indicates an evolu/on in the opera/onal maturity of MuddyWater," ESET said. "The deployment of previously undocumented components – such as the Fooder loader and MuddyViper backdoor – signals an effort to enhance stealth, persistence, and credential harvesting capabilities."

### Charming Kitten Leaks

The disclosure comes weeks after the Israel National Digital Agency (INDA) attributed Iranian threat actors known as APT42 to attacks targeting individuals and organizations of interest in an espionage-focused campaign named
[SpearSpecter](https://thehackernews.com/2025/11/iranian-hackers-launch-spearspecter-spy.html)
. APT42 is believed to share overlaps with another hacking group tracked as APT35 (aka Charming Kitten and Fresh Feline).

It also follows a
[massive](https://blog.narimangharib.com/posts/2025%2F09%2F1759266283738?lang=en)
[leak](https://blog.narimangharib.com/posts/2025%2F10%2F1760604853962?lang=en)
of
[internal](https://blog.narimangharib.com/posts/2025%2F10%2F1761609810950?lang=en)
[documents](https://blog.narimangharib.com/posts/2025%2F11%2F1763938840948?lang=en)
that has exposed the hacking group's cyber operations, which, according to British-Iranian activist Nariman Gharib,
[feeds into a system](https://content.iranintl.com/unit40/index.html)
designed to locate and kill individuals deemed a threat to Iran. It's linked to the Islamic Revolutionary Guard Corps (IRGC), specifically its counterintelligence division known as Unit 1500.

"The story reads like a horror script written in PowerShell and Persian," FalconFeeds
[said](https://falconfeeds.io/blogs/kittenbusters-expose-charming-kitten-leaks)
, adding the leak reveals "a complete map of Iran's IRGC Unit 1500 cyber division."

The data dump was posted to GitHub in September and October 2025 by an anonymous collective named
**KittenBusters**
, whose motivations remain unknown. Notably, the trove identifies Abbas Rahrovi, also known as Abbas Hosseini, as the operation's leader, and alleges that the hacking unit is managed through a network of front companies.

Perhaps one of the other most consequential revelations is the release of the entire source code associated with the
[BellaCiao](https://thehackernews.com/2023/04/charming-kittens-new-bellaciao-malware.html)
malware, which was flagged by Bitdefender in April 2023 as used in attacks targeting companies in the U.S., Europe, the Middle East, and India. Per Gharib, the backdoor is the work of a team operating from the Shuhada base in Tehran.

"The leaked materials reveal a structured command architecture rather than a decentralized hacking collective, an organization with distinct hierarchies, performance oversight, and bureaucratic discipline," DomainTools
[said](https://dti.domaintools.com/threat-intelligence-report-apt35-internal-leak-of-hacking-campaigns-against-lebanon-kuwait-turkey-saudi-arabia-korea-and-domestic-iranian-targets/)
.

"The APT35 leak exposes a bureaucratized cyber-intelligence apparatus, an institutional arm of the Iranian state with defined hierarchies, workflows, and performance metrics. The documents reveal a self-sustaining ecosystem where clerks log daily activity, quantify phishing success rates, and track reconnaissance hours. Meanwhile, technical staff test and weaponize exploits against current vulnerabilities."