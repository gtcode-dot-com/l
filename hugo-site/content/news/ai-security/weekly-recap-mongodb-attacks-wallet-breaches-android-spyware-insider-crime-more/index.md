---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-30T00:15:13.200994+00:00'
exported_at: '2025-12-30T00:15:16.633188+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html
structured_data:
  about: []
  author: ''
  description: 'Weekly 2025 cyber recap: MongoBleed targets 87,000, Trust Wallet $7M
    loss, LastPass $35M theft, DNS poisoning, npm WhatsApp trap.'
  headline: '⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider
    Crime & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: '⚡ Weekly Recap: MongoDB Attacks, Wallet Breaches, Android Spyware, Insider
  Crime & More'
updated_at: '2025-12-30T00:15:13.200994+00:00'
url_hash: fa9bf352bc7ef4024035ff756937dcb353394791
---

**

Dec 29, 2026
**

Ravie Lakshmanan

Hacking News / Cybersecurity

Last week's cyber news in 2025 was not about one big incident. It was about many small cracks opening at the same time. Tools people trust every day behave in unexpected ways. Old flaws resurfaced. New ones were used almost immediately.

A common theme ran through it all in 2025. Attackers moved faster than fixes. Access meant for work, updates, or support kept getting abused. And damage did not stop when an incident was "over" — it continued to surface months or even years later.

This weekly recap brings those stories together in one place. No overload, no noise. Read on to see what shaped the threat landscape in the final stretch of 2025 and what deserves your attention now.

## **⚡ Threat of the Week**

**[MongoDB Vulnerability Comes Under Attack](https://thehackernews.com/2025/12/mongodb-vulnerability-cve-2025-14847.html)**
— A newly disclosed security vulnerability in MongoDB has come under active exploitation in the wild, with over 87,000 potentially susceptible instances identified across the world. The vulnerability in question is CVE-2025-14847 (CVSS score: 8.7), which allows an unauthenticated attacker to remotely leak sensitive data from the MongoDB server memory. It has been codenamed MongoBleed. The exact details surrounding the nature of attacks exploiting the flaw are presently unknown. Users are advised to update to MongoDB versions 8.2.3, 8.0.17, 7.0.28, 6.0.27, 5.0.32, and 4.4.30. Data from attack surface management company Censys shows that there are more than 87,000 potentially vulnerable instances, with a majority of them located in the U.S., China, Germany, India, and France. Wiz noted that 42% of cloud environments have at least one instance of MongoDB in a version vulnerable to CVE-2025-14847. This includes both internet-exposed and internal resources.

## **🔔 Top News**

* **[Trust Wallet Chrome Extension Hack Leads to $7M Loss](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html)**
  — Trust Wallet urged users to update its Google Chrome extension to the latest version following what it described as a "security incident" that led to the loss of approximately $7 million. Users are advised to update to version 2.69 as soon as possible. "We've confirmed that approximately $7 million has been impacted, and we will ensure all affected users are refunded," Trust Wallet said. The Chrome extension has about 1 million users. Mobile-only users and all other browser extension versions are not affected. It's currently not known who is behind the attack, but Trust Wallet said the attacker likely published a malicious version (2.68) by using a leaked Chrome Web Store API key. Affected victims have been asked to fill out a form to process reimbursements.
* **[Evasive Panda Stages DNS Poisoning Attack to Push MgBot Malware](https://thehackernews.com/2025/12/china-linked-evasive-panda-ran-dns.html)**
  — A China-linked advanced persistent threat (APT) group known as Evasive Panda was attributed to a highly-targeted cyber espionage campaign in which the adversary poisoned Domain Name System (DNS) requests to deliver its signature MgBot backdoor in attacks targeting victims in Türkiye, China, and India. The activity took place between November 2022 and November 2024. According to Kaspersky, the hacking group conducted adversary-in-the-middle (AitM) attacks on specific victims to serve trojanized updates for popular tools like SohuVA, iQIYI Video, IObit Smart Defrag, and Tencent QQ that ultimately deployed MgBot, a modular implant with wide-ranging information gathering capabilities. It's currently not known how the threat actor is poisoning DNS responses. But two possible scenarios are suspected: either the ISPs used by the victims were selectively targeted and compromised to install some kind of network implant on edge devices, or a router or firewall used by the victims was hacked for this purpose.
* **[LastPass 2022 Breach Leads to Crypto Theft](https://thehackernews.com/2025/12/lastpass-2022-breach-led-to-years-long.html)**
  — The encrypted vault backups stolen from the 2022 LastPass data breach enabled bad actors to take advantage of weak master passwords to crack them open and drain cryptocurrency assets as recently as late 2025. New findings from TRM Labs show that threat actors with possible ties to the Russian cybercriminal ecosystem have stolen no less than $35 million as of September 2025. The Russian links to the stolen cryptocurrency stem from two primary factors: The use of exchanges commonly associated with the Russian cybercriminal ecosystem in the laundering pipeline and operational connections gleaned from wallets interacting with mixers both before and after the mixing and laundering process.
* **[Fortinet Warns of Renewed Activity Exploiting CVE-2020-12812](https://thehackernews.com/2025/12/fortinet-warns-of-active-exploitation.html)**
  — Fortinet said it observed "recent abuse" of CVE-2020-12812, a five-year-old security flaw in FortiOS SSL VPN, in the wild under certain configurations. The vulnerability could allow a user to log in successfully without being prompted for the second factor of authentication if the case of the username was changed. The newly issued guidance does not give any specifics on the nature of the attacks exploiting the flaw, nor whether any of those incidents were successful. Fortinet has also advised impacted customers to contact its support team and reset all credentials if they find evidence of admin or VPN users being authenticated without two-factor authentication (2FA).
* **[Fake WhatsApp API npm Package Steals Messages](https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html)**
  — A new malicious package on the npm repository named lotusbail was found to work as a fully functional WhatsApp API, but contained the ability to intercept every message and link the attacker's device to a victim's WhatsApp account. It has been downloaded over 56,000 times since it was first uploaded to the registry by a user named "seiren\_primrose" in May 2025. The package has since been removed by npm. Once the npm package is installed, the threat actor can read all WhatsApp messages, send messages to others, download media files, and access contact lists. "And here's the critical part, uninstalling the npm package removes the malicious code, but the threat actor's device stays linked to your WhatsApp account," Koi said. "The pairing persists in WhatsApp's systems until you manually unlink all devices from your WhatsApp settings. Even after the package is gone, they still have access."

## **‎️‍🔥 Trending CVEs**

Hackers act fast. They can use new bugs within hours. One missed update can cause a big breach. Here are this week's most serious security flaws. Check them, fix what matters first, and stay protected.

This week's list includes —
[CVE-2025-14847](https://thehackernews.com/2025/12/mongodb-vulnerability-cve-2025-14847.html)
(MongoDB),
[CVE-2025-68664](https://thehackernews.com/2025/12/critical-langchain-core-vulnerability.html)
(LangChain Core),
[CVE-2023-52163](https://thehackernews.com/2025/12/cisa-flags-actively-exploited-digiever.html)
(Digiever DS-2105 Pro),
[CVE-2025-68613](https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html)
(n8n),
[CVE-2025-13836](https://fatihhcelik.github.io/posts/Crashing-Python-http.client-CVE-2025-13836/)
(Python http.client),
[CVE-2025-26794](https://nvd.nist.gov/vuln/detail/cve-2025-26794)
(Exim),
[CVE-2025-68615](https://github.com/net-snmp/net-snmp/security/advisories/GHSA-4389-rwqf-q9gq)
(Net-SNMP),
[CVE-2025-44016](https://www.teamviewer.com/en-us/resources/trust-center/security-bulletins/tv-2025-1005/)
(TeamViewer DEX Client), and
[CVE-2025-13008](https://product.m-files.com/security-advisories/cve-2025-13008/)
(M-Files Server).

## **📰 Around the Cyber World**

* **Former Coinbase Customer Service Agent Arrested in India**
  — Coinbase Chief Executive Officer Brian Armstrong said that a former customer service agent for the largest U.S. crypto exchange was arrested in India, months after
  [hackers bribed customer service representatives](https://thehackernews.com/2025/05/coinbase-agents-bribed-data-of-1-users.html)
  to gain access to customer information. In May, the company said hackers bribed contractors working out of India to steal sensitive customer data and demanded a $20 million ransom. "We have zero tolerance for bad behavior and will continue to work with law enforcement to bring bad actors to justice," Armstrong
  [said](https://x.com/brian_armstrong/status/2004583231165780024)
  . "Thanks to the Hyderabad Police in India, an ex-Coinbase customer service agent was just arrested. Another one down and more still to come." The incident impacted 69,461 individuals. A
  [September 2025 class action lawsuit](https://storage.courtlistener.com/recap/gov.uscourts.nysd.643269/gov.uscourts.nysd.643269.36.0.pdf)
  has revealed that Coinbase hired TaskUs to handle customer support from India. The court document also mentioned that Coinbase "cut ties with the TaskUs personnel involved and other overseas agents, and tightened controls." One TaskUs employee based out of Indore, Ashita Mishra, is accused of "joining the conspiracy by agreeing to sell highly sensitive Coinbase user data to those criminals" as early as September 2024. Mishra was arrested in January 2025 for allegedly selling the stolen data to hackers for $200 per record. TaskUs claimed that "it identified two individuals who illegally accessed information from one of our clients [who] were recruited by a much broader, coordinated criminal campaign against this client that also impacted a number of other providers servicing this client." It also
  [alleged](https://storage.courtlistener.com/recap/gov.uscourts.nysd.643269/gov.uscourts.nysd.643269.29.0.pdf)
  that Coinbase "had vendors other than TaskUs, and that Coinbase employees were involved in the data breach." But the company provided no further details.
* **Cloud Atlas Targets Russia and Belarus**
  — The threat actor known as
  [Cloud Atlas](https://thehackernews.com/2024/12/cloud-atlas-deploys-vbcloud-malware.html)
  has
  [leveraged](https://securelist.com/cloud-atlas-h1-2025-campaign/118517/)
  phishing lures with a malicious Microsoft Word document attachment that, when opened, downloads a malicious template from a remote server that, in turn, fetches and executes an HTML Application (HTA) file. The malicious HTA file extracts and creates several Visual Basic Script (VBS) files on disk that are parts of the VBShower backdoor. VBShower then downloads and installs other backdoors, including PowerShower, VBCloud, and CloudAtlas. VBCloud can download and execute additional malicious scripts, including a file grabber to exfiltrate files of interest. Similar to VBCloud, PowerShower is capable of retrieving an additional payload from a remote server. CloudAtlas establishes communication with a command-and-control (C2) server via WebDAV and fetches executable plugins in the form of a DLL, allowing it to gather files, run commands, steal passwords from Chromium-based browsers, and capture system information. Attacks mounted by the threat actor have primarily targeted organizations in the telecommunications sector, construction, government entities, and plants in Russia and Belarus.
* **BlackHawk Loader Spotted in the Wild**
  — A new MSIL loader named BlackHawk has been detected in the wild, incorporating three layers of obfuscation that show signs of being generated using artificial intelligence (AI) tools. Per
  [ESET](https://infosec.exchange/@ESETresearch/115746705461960105)
  , it features a Visual Basic Script and two PowerShell scripts, the second of which contains the Base64-encoded BlackHawk loader and the final payload. The loader is being actively used in campaigns distributing Agent Tesla in attacks targeting hundreds of endpoints in Romanian small and medium-sized companies. The loader has also been
  [used](https://labs.k7computing.com/index.php/phantom-3-5-initial-vector-analysis-forensics/)
  to deliver an information stealer known as Phantom.
* **Surge in Cobalt Strike Servers**
  — Censys has noted a sudden spike in Cobalt Strike servers hosted online between early December and December 18, 2025, specifically on the networks of AS138415 (YANCY) and AS133199 (SonderCloud LTD). "Viewing the timeline above, AS138415 first exhibits limited 'seed' activity beginning on December 4, followed by a substantial expansion of 119 new Cobalt Strike servers on December 6," Censys
  [said](https://censys.com/blog/recap-of-a-suspicious-surge-in-cobalt-strike)
  . "Within just two days, however, nearly all of this newly added infrastructure disappears. On December 8, AS133199 experienced a near mirror-image increase and decrease in newly observed Cobalt Strike servers." More than 150 distinct IPs associated with AS138415 have been flagged as hosting Cobalt Strike listeners during this window. This netblock, 23.235.160[.]0/19, was allocated to RedLuff, LLC in September 2025.
* **Meet Fly, the Russian Market Administrator**
  — Intrinsec has revealed that a threat actor known as Fly is likely the administrator of Russian Market, an underground portal for selling credentials stolen via infostealers. "This threat actor promoted the marketplace on multiple occasions and throughout the years," the French cybersecurity company
  [said](https://www.intrinsec.com/mapping-fly-a-threat-actor-with-links-to-russian-markets-infrastructure/)
  . "His username is reminiscent of the old name of the marketplace, 'Flyded.' We found two e-mail addresses used to register the first Russian Market domains, which enabled us to find potential links to a Gmail account named 'AlexAske1,' but we could not find additional information surrounding this potential identity."
* **New Scam Campaign Targets MENA with Fake Job Offers**
  — A new scam campaign is targeting Middle East and North Africa (MENA) countries with fake online jobs across social media and private messaging platforms like Telegram and WhatsApp that promise easy work and fast money, but are designed to collect personal data and steal money. The scams exploit trust in recognized institutions and the low cost of social media advertising. The targeting is intentionally broad to cast a wide phishing net. "The fake job ads often impersonate well-known companies, banks, and authorities to gain trust of victims," Group-IB
  [said](https://www.group-ib.com/blog/online-job-scams-mena/)
  . "Once victims engage, the conversation moves to private messaging channels where the actual financial fraud and data theft take place." The ads typically redirect victims to a WhatsApp group, where a recruiter directs them to a scam website for registration. Once the victim has completed the step, they are added to various Telegram channels where they are instructed to pay a fee to secure tasks and earn commissions from it. "The scammers will actually send a small payout for the initial task to build trust," Group-IB said. "They will then push victims to deposit larger amounts to take on bigger tasks that promise even greater returns. When victims do make a big deposit, the payout stops, the channels and accounts disappear and the victim finds themselves blocked, making communication and tracking almost impossible." The ads are directed against MENA countries such as Egypt, Gulf States' members, Algeria, Tunisia, Morocco, Iraq, and Jordan.
* **EmEditor Breached to Distribute Infostealer**
  — Windows-based text editing program EmEditor has disclosed a security breach. Emurasoft
  [said](https://www.emeditor.com/general/important-security-incident-notice-regarding-the-emeditor-installer-download-link/)
  a "third-party" performed an unauthorized modification of the download link for its Windows installer to point to a malicious MSI file hosted in a different location on the EmEditor website between December 19 and 22, 2022. Emurasoft said it's investigating the incident to determine the full scope of impact. According to Chinese security firm QiAnXin, the malicious installer is
  [used](https://mp.weixin.qq.com/s/M1-UdMaGflhkuqet0K1gqg)
  to launch a PowerShell script that's capable of harvesting system information, including system metadata, files, VPN configuration, Windows login credentials, browser data, and information associated with apps like Zoho Mail, Evernote, Notion, discord, Slack, Mattermost, Skype, LiveChat, Microsoft Teams, Zoom, WinSCP, PuTTY, Steam, and Telegram. It also installs an Edge browser extension (ID: "ngahobakhbdpmokneiohlfofdmglpakd") named Google Drive Caching that₹₹₹ can fingerprint browsers, replace cryptocurrency wallet addresses in the clipboard, log keystrokes from specific websites such as x[.]com, and steal Facebook advertising account details.
* **Docker Hardened Images Now Available for Free**
  — Docker has made
  [Hardened Images](https://www.docker.com/products/hardened-images/)
  free for every developer to bolster software supply chain security. Introduced in May 2025, these are a set of secure, minimal, production-ready images that are managed by Docker. The company said it has hardened over 1,000 images and helm charts in its catalog. "Unlike other opaque or proprietary hardened images, DHI is compatible with Alpine and Debian, trusted and familiar open source foundations teams already know and can adopt with minimal change," Docker
  [noted](https://www.docker.com/blog/docker-hardened-images-for-every-developer/)
  .
* **Flaw in Livewire Disclosed**
  — Details have emerged about a now-patched critical security flaw in Livewire (
  [CVE-2025-54068](https://nvd.nist.gov/vuln/detail/cve-2025-54068)
  , CVSS score: 9.8), a full-stack framework for Laravel, that could allow unauthenticated attackers to achieve remote command execution in specific scenarios. The issue was addressed in
  [Livewire version 3.6.4](https://github.com/livewire/livewire/releases/tag/v3.6.4)
  released in July 2025. According to Synacktiv, the vulnerability is rooted in the platform's hydration mechanism, which is used to manage component states and ensure that they have not been tampered with during transit by means of a checksum. "However, this mechanism comes with a critical vulnerability: a dangerous unmarshalling process can be exploited as long as an attacker is in possession of the APP\_KEY of the application," the cybersecurity company
  [said](https://www.synacktiv.com/en/publications/livewire-remote-command-execution-through-unmarshaling)
  . "By crafting malicious payloads, attackers can manipulate Livewire's hydration process to execute arbitrary code, from simple function calls to stealthy remote command execution." To make matters worse, the research also identified a pre-authenticated remote code execution vulnerability that's exploitable even without knowledge of the application's APP\_KEY. "Attackers could inject malicious synthesizers through the updates field in Livewire requests, leveraging PHP's loose typing and nested array handling," Synacktiv added. "This technique bypasses checksum validation, allowing arbitrary object instantiation and leading to full system compromise."
* **ChimeraWire Malware Boosts Website SERP Rankings**
  — A new malware dubbed ChimeraWire has been found to artificially boost the ranking of certain websites in search engine results pages (SERPs) by performing hidden internet searches and mimicking user clicks on infected Windows devices. ChimeraWire is typically deployed as a second-stage payload on systems previously infected with other malware downloaders, Doctor Web said. The malware is designed to download a Windows version of the Google Chrome browser and install add-ons like NopeCHA and Buster into it for automated CAPTCHA solving. ChimeraWire then launches the browser in debugging mode with a hidden window to perform the malicious clicking activity based on certain pre-configured criteria. "For this, the malicious app searches target internet resources in the Google and Bing search engines and then loads them," the Russian company
  [said](https://news.drweb.com/show/?i=15090&lng=en&c=5)
  . "It also imitates user actions by clicking links on the loaded sites. The Trojan performs all malicious actions in the Google Chrome web browser, which it downloads from a certain domain and then launches it in debug mode over the WebSocket protocol."
* **More Details About LANDFALL Campaign Emerge**
  — The LANDFALL Android spyware campaign was
  [disclosed](https://thehackernews.com/2025/11/samsung-zero-click-flaw-exploited-to.html)
  by Palo Alto Networks Unit 42 last month as having exploited a now-patched zero-day flaw in Samsung Galaxy Android devices (CVE-2025-21042) in targeted attacks in the Middle East. Google Project Zero said it identified six suspicious image files that were uploaded to VirusTotal between July 2024 and February 2025. It's suspected that these images were received over WhatsApp, with Google noting that the files were DNG files targeting the
  [Quram library](https://projectzero.google/2020/07/mms-exploit-part-1-introduction-to-qmage.html)
  , an image parsing library specific to Samsung devices. Further investigation has determined that the images are engineered to trigger an exploit that runs within the com.samsung.ipservice process. "The com.samsung.ipservice process is a Samsung-specific system service responsible for providing 'intelligent' or AI-powered features to other Samsung applications," Project Zero's Benoît Sevens
  [said](https://projectzero.google/2025/12/android-itw-dng.html)
  . "It will periodically scan and parse images and videos in Android's MediaStore. When WhatsApp receives and downloads an image, it will insert it in the MediaStore. This means that downloaded WhatsApp images (and videos) can hit the image parsing attack surface within the com.samsung.ipservice application." Given that WhatsApp does not automatically download images from untrusted contacts, it's assessed that a 1-click exploit is used to trigger the download and have it added to the MediaStore. This, in turn, fires an exploit for the flaw, resulting in an out-of-bounds write primitive. "This case illustrates how certain image formats provide strong primitives out of the box for turning a single memory corruption bug into interactionless ASLR bypasses and remote code execution," Sevens noted. "By corrupting the bounds of the pixel buffer using the bug, the rest of the exploit could be performed by using the 'weird machine' that the DNG specification and its implementation provide."
* **New Android Spyware Discovered on Belarusian Journalist's Phone**
  — Belarusian authorities are
  [deploying](https://rsf.org/en/exclusive-rsf-uncovers-new-spyware-belarus)
  a new spyware called ResidentBat on the smartphones of local journalists after their phones are confiscated during police interrogations by the Belarusian secret service. The spyware can collect call logs, record audio through the microphone, take screenshots, collect SMS messages and chats from encrypted messaging apps, and exfiltrate local files. It can also factory reset the device and remove itself. According to a report from
  [RESIDENT.NGO](https://resident.ngo/lab/writeups/residentbat-android-kgb-spyware-in-belarus-2025/)
  , ResidentBat's server infrastructure has been operational since March 2021. In December 2024, similar cases of implanting spyware on individuals' phones while they were being questioned by police or security services were reported in
  [Serbia](https://thehackernews.com/2024/12/novispy-spyware-installed-on.html)
  and
  [Russia](https://thehackernews.com/2024/12/fsb-uses-trojan-app-to-monitor-russian.html)
  . "The infection relied on physical access to the device," RESIDENT.NGO said. "We hypothesize that the KGB officers observed the device password or PIN as the journalist typed it in their presence during the conversation. Once the officers had the PIN and physical possession of the phone while it was in the locker, they enabled 'Developer Mode' and 'USB Debugging.' The spyware was then sideloaded onto the device, likely via ADB commands from a Windows PC."
* **Former Incident Responders Plead Guilty to Ransomware Attacks**
  — Former cybersecurity professionals Ryan Clifford Goldberg and Kevin Tyler Martin
  [pleaded guilty](https://cyberscoop.com/incident-responders-plead-guilty-ransomware-digitalmint/)
  to participating in a
  [series of BlackCat ransomware attacks](https://thehackernews.com/2025/11/us-prosecutors-indict-cybersecurity.html)
  between May and November 2023 while they were employed at cybersecurity companies tasked with helping organizations fend off ransomware attacks. Goldberg and Martin were indicted last month. While Martin worked as a ransomware threat negotiator for DigitalMint, Goldberg was an incident response manager for cybersecurity company Sygnia. A third unnamed co-conspirator, who was also employed at DigitalMint, allegedly obtained an affiliate account for BlackCat, which the trio used to commit ransomware attacks.
* **Congressional Report Says China Exploits U.S.-funded Research on Nuclear Technology**
  — A new report
  [released](https://chinaselectcommittee.house.gov/media/press-releases/investigation-reveals-energy-department-collaborated-with-china-s-military-on-research)
  by the House Select Committee on China and the House Permanent Select Committee on Intelligence (HPSCI) has revealed that China exploits the U.S. Department of Energy (DOE) to gain access and divert American taxpayer-funded research and fuel its military and technological rise. The investigation identified about 4,350 research papers between June 2023 and June 2025, where DOE funding or research support involved research relationships with Chinese entities, including over 730 DOE awards and contracts. Of these, approximately 2,200 publications were conducted in partnership with entities within China's defense research and industrial base. "This case study and many more like it in the report underscore a deeply troubling reality: U.S. government scientists – employed by the DOE and working at federally funded national laboratories – have coauthored research with Chinese entities at the very heart of the PRC's military-industrial complex," the House Select Committee on the Chinese Communist Party (CCP) said. "They involve the joint development of technologies relevant to next-generation military aircraft, electronic warfare systems, radar deception techniques, and critical energy and aerospace infrastructure – alongside entities already restricted by multiple U.S. agencies for posing a threat to national security." In a statement shared with Associated Press, the Chinese Embassy in Washington
  [said](https://apnews.com/article/china-nuclear-energy-department-research-congressional-report-470549567520c89c04be1b30b218fe33)
  the select committee "has long smeared and attacked China for political purposes and has no credibility to speak of."
* **Moscow Court Sentences Russian Scientist to 21 Years for Treason**
  — A Moscow court
  [handed](https://tass.ru/proisshestviya/25814693)
  a 21-year prison sentence to
  [Artyom Khoroshilov](https://meduza.io/en/feature/2025/11/26/russian-prosecutors-seeking-25-year-prison-sentence-for-physicist-who-donated-to-ukrainian-charities)
  , 34, a researcher at the Moscow Institute of General Physics, who has been accused of treason, attacking critical infrastructure, and plotting sabotage. He was also fined 700,000 rubles (~$9,100). Khoroshilov is said to have colluded with the Ukrainian IT army to conduct distributed denial-of-service (DDoS) attacks on the Russian Post in August 2022. He also planned to commit sabotage by blowing up the railway tracks used by the military unit of the Ministry of Defense of the Russian Federation to transport military goods. The IT Army of Ukraine, a hacktivist group known for coordinating DDoS attacks on Russian infrastructure,
  [said](https://t.me/itarmyofukraine2022/3465)
  it does not know if Khoroshilov was part of their community, but noted "the enemy hunts down any sign of resistance."
* **New DIG AI Tool Used by Malicious Actors**
  — Resecurity said it has observed a "notable increase" in malicious actors' utilization of DIG AI, the latest addition to a long list of dark Large Language Models (LLMs) that can be used for illegal, unethical, malicious or harmful activities, such as generating phishing emails or instructions for bombs and prohibited substances. It can be accessed by users via the Tor browser without requiring an account. According to its developer, Pitch, the service is based on OpenAI's ChatGPT Turbo. "DIG AI enables malicious actors to leverage the power of AI to generate tips ranging from explosive device manufacturing to illegal content creation, including CSAM," the company
  [said](https://www.resecurity.com/blog/article/dig-ai-uncensored-darknet-ai-assistant-at-the-service-of-criminals-and-terrorists)
  . "Because DIG AI is hosted on the TOR network, such tools are not easily discoverable and accessible to law enforcement. They create a significant underground market – from piracy and derivatives to other illicit activities."
* **China Says U.S. Seized Cryptocurrency from Chinese Firm**
  — The Chinese government said the U.S. unduly seized cryptocurrency assets that actually belonged to LuBian. In October 2025, the U.S. Justice Department
  [seized](https://thehackernews.com/2025/10/threatsday-bulletin-15b-crypto-bust.html#crypto-empire-built-on-slavery)
  $15 billion worth of Bitcoin from the operator of scam compounds last month. The agency claimed the funds were owned by the Prince Group and its CEO, Chen Zhi. China's National Computer Virus Emergency Response Center (CVERC) alleged that the funds could be traced back to the 2020 hack of Chinese bitcoin mining pool operator LuBian, echoing a report from Elliptic. What's evident is that the digital assets were stolen from Zhi before they ended up with the U.S. "The U.S. government may have stolen Chen Zhi's 127,000 Bitcoin through hacking techniques as early as 2020, making this a classic case of 'black-on-black' crime orchestrated by a state-sponsored hacking organization," CVERC
  [said](https://mp.weixin.qq.com/s/vIg9N2xRy6o6EufAAv9uVA)
  . However, it bears noting that the report makes no mention of the stolen assets being linked to scam campaigns.

## **🎥 Cybersecurity Webinars**

* [How Zero Trust and AI Catch Attacks With No Files, No Binaries, and No Indicators](https://thehacker.news/proactive-cloud-security?source=recap)
  — Cyber threats are evolving faster than ever, exploiting trusted tools and fileless techniques that evade traditional defenses. This webinar reveals how Zero Trust and AI-driven protection can uncover unseen attacks, secure developer environments, and redefine proactive cloud security—so you can stay ahead of attackers, not just react to them.
* [Master Agentic AI Security: Learn to Detect, Audit, and Contain Rogue MCP Servers](https://thehacker.news/securing-agentic-ai?source=recap)
  — AI tools like Copilot and Claude Code help developers move fast, but they can also create big security risks if not managed carefully. Many teams don't know which AI servers (MCPs) are running, who built them, or what access they have. Some have already been hacked, turning trusted tools into backdoors. This webinar shows how to find hidden AI risks, stop shadow API key problems, and take control before your AI systems create a breach.

## **🔧 Cybersecurity Tools**

* [GhidraGPT](https://github.com/weirdmachine64/GhidraGPT)
  — It is a plugin for Ghidra that adds AI-powered assistance to reverse engineering work. It uses large language models to help explain decompiled code, improve readability, and highlight potential security issues, making it easier for analysts to understand and analyze complex binaries.
* [Chameleon](https://github.com/qeeqbox/chameleon/)
  — It is an open-source honeypot tool used to monitor attacks, bot activity, and stolen credentials across a wide range of network services. It simulates open and vulnerable ports to attract attackers, logs their activity, and shows the results through simple dashboards, helping teams understand how their systems are being scanned and attacked in real environments.

*Disclaimer: These tools are for learning and research only. They haven't been fully tested for security. If used the wrong way, they could cause harm. Check the code first, test only in safe places, and follow all rules and laws.*

## **Conclusion**

This weekly recap brings those stories together in one place to close out 2025. It cuts through the noise and focuses on what actually mattered in the final days of the year. Read on for the events that shaped the threat landscape, the patterns that kept repeating, and the risks that are likely to carry forward into 2026.