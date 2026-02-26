---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T16:15:16.325443+00:00'
exported_at: '2026-02-26T16:15:18.714634+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/threatsday-bulletin-kali-linux-claude.html
structured_data:
  about: []
  author: ''
  description: This week’s ThreatsDay Bulletin highlights emerging cyber threats,
    evolving attack tactics, and key security developments.
  headline: 'ThreatsDay Bulletin: Kali Linux + Claude, Chrome Crash Traps, WinRAR
    Flaws, LockBit & 15+ Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/threatsday-bulletin-kali-linux-claude.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: Kali Linux + Claude, Chrome Crash Traps, WinRAR Flaws,
  LockBit & 15+ Stories'
updated_at: '2026-02-26T16:15:16.325443+00:00'
url_hash: 8ca736b39419d1f85864eed18d458c733195814c
---

**

Ravie Lakshmanan
**

Feb 26, 2026

Cybersecurity / Hacking News

Nothing here looks dramatic at first glance. That’s the point. Many of this week’s threats begin with something ordinary, like an ad, a meeting invite, or a software update.

Behind the scenes, the tactics are sharper. Access happens faster. Control is established sooner. Cleanup becomes harder.

Here is a quick look at the signals worth paying attention to.

1. AI-powered command execution

   Kali Linux, an advanced penetration testing Linux distribution used for ethical hacking and network security assessments, has
   [added](https://www.kali.org/blog/kali-llm-claude-desktop/)
   an integration with Anthropic's Claude large language model through the Model Context Protocol (MCP) to issue commands in natural language and translate them into technical commands.
2. Belarus-linked Android spyware

   ResidentBat is an Android spyware implant used by Belarusian authorities for surveillance operations against journalists and civil society. Once installed, it provides operators with access to call logs, microphone recordings, SMS, encrypted messenger traffic, screen captures, and locally stored files. The malware, although
   [first documented](https://thehackernews.com/2025/12/weekly-recap-mongodb-attacks-wallet.html#:~:text=New%20Android%20Spyware%20Discovered%20on%20Belarusian%20Journalist%27s%20Phone)
   in December 2025, is assessed to date back to 2021. According to Censys, ResidentBat-associated infrastructure is
   [concentrated](https://censys.com/blog/residentbat-belarusian-kgb-android-spyware/)
   in Europe and Russia: the Netherlands (5 hosts), Germany (2 hosts), Switzerland (2 hosts), and Russia (1 host) in a recent Platform view, using a narrow port range (7000-7257) for control traffic.
3. Crypto phishing wave

   Phishing campaigns are impersonating cryptocurrency brokerage services like Bitpanda to harvest sensitive data under the pretext of reconfirming their information or risk having their accounts blocked. "Attempting to get multiple forms of information and identification, the attackers used tactics that would seem legitimate to the everyday user," Cofense
   [said](https://cofense.com/blog/pii-pillage-how-attackers-use-bitpanda-to-plunder-credentials)
   . "User information such as name verification, email, and password credentials, and location were all used in this attempt to harvest information under the guise of a multi-factor authentication process."
4. Breakout times shrink

   In its 2026 Global Threat Report, CrowdStrike said adversaries became faster than ever before in 2025. "The average e-crime breakout time — the period between initial access and lateral movement onto another system — dropped to 29 minutes, a 65% increase in speed from 2024," the company
   [said](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-global-threat-report-findings/)
   . One such intrusion undertaken by
   [Luna Moth](https://thehackernews.com/2025/05/hackers-are-calling-your-office-fbi.html)
   (aka Chatty Spider) targeting a law firm moved from initial access to data exfiltration in four minutes. Chief among the factors fueling this dramatic acceleration was the widespread abuse of legitimate credentials, which allowed attackers to blend into normal network traffic and bypass many traditional security controls. This was coupled with threat actors of varied motivations utilizing AI technology to accelerate and optimize their existing techniques. Some of the threat actors that have leveraged AI in their operations include
   [Fancy Bear](https://thehackernews.com/2025/07/cert-ua-discovers-lamehug-malware.html)
   , Punk Spider (aka Akira), Blind Spider (aka Blind Eagle), Odyssey Spider (aka TA558), and an India-nexus hacking group called Frantic Tiger that has used Netlify and Cloudflare pages for credential-harvesting operations. The cybersecurity company said it observed an 89% increase in the number of attacks by AI-enabled adversaries compared to 2024 and a 42% year-over-year increase in zero-days exploited prior to public disclosure. In tandem, 67% of vulnerabilities exploited by China-nexus adversaries provided immediate system access, and 40% targeted edge devices that typically lack comprehensive monitoring. The vast majority of attacks, 82%, were free of malware — highlighting attackers' enduring shift toward hands-on-keyboard operations and the abuse of legitimate tools and credentials.
5. 4-minute lateral movement

   In a similar report, ReliaQuest said the fastest intrusions reached lateral movement in just 4 minutes, an 85% acceleration from last year, with data exfiltration taking place in 6 minutes. The statistic is fueled by attackers increasingly weaving AI and automation into their tradecraft. "As attackers increasingly secure valid credentials with elevated privileges, the time to react has drastically dropped," ReliaQuest
   [said](https://reliaquest.com/blog/2026-annual-cyber-threat-report/)
   . "In 2025, the average breakout time (initial access to lateral movement) dropped to 34 minutes. In 47% of incidents, they secured high privileges before ever touching the network. This allows them to skip escalation, blend into traffic, and repurpose legitimate tools."
6. ClickFix fuels Mac stealers

   Mac users searching for popular software like Homebrew, 7-Zip, Notepad++, LibreOffice, and Final Cut Pro are the target of an
   [active malvertising campaign](https://www.bitdefender.com/en-us/blog/hotforsecurity/hijacked-google-ads-push-fake-7-zip-notepad-and-office-downloads-to-mac-users-via-evernote-pages)
   powered by at least 35 hijacked Google advertiser accounts originating from countries including the U.S., Canada, Italy, Poland, Brazil, India, Saudi Arabia, Japan, China, Romania, Malta, Slovenia, Germany, the U.K., and the U.A.E. More than 200 malicious advertisements impersonating legitimate macOS software have been found. The end goal of these efforts is to direct users to fake pages that contain
   [ClickFix](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html)
   -like instructions to deliver MacSync stealer. Another ClickFix campaign has been
   [observed](https://www.cyberproof.com/blog/fake-captcha-attack-uncovered-clickfix-infostealer-campaign/)
   using fake CAPTCHA verification lures on bogus phishing pages to distribute stealer malware that can harvest data from web browsers, gaming apps like Steam, cryptocurrency wallets, and VPN apps. According to ReliaQuest data, a quarter of attacks used social engineering for initial access last year, with ClickFix
   [responsible](https://reliaquest.com/campaigns/annual-threat-report-2026/executive-summary-2025-vs-2024-at-a-glance)
   for delivering 59% of the top malware families.
7. Encryption debate resurfaces

   Meta went ahead with a plan to encrypt the messaging services connected to its Facebook and Instagram apps despite internal warnings that it would hinder the social media giant's ability to flag child-exploitation cases to law enforcement, Reuters
   [reported](https://www.reuters.com/legal/government/meta-executive-warned-facebook-messenger-encryption-plan-was-so-irresponsible-2026-02-24/)
   . The internal chat exchange dated March 2019 was filed
   [in connection with a lawsuit](https://www.reuters.com/legal/government/meta-faces-new-mexico-trial-over-child-exploitation-claims-2026-01-30/)
   brought by the U.S. state of New Mexico, accusing it of exposing children and teens to sexual exploitation on its platforms and profiting from it. In response to the concerns raised, Meta said it worked on additional safety features before it launched encrypted messaging on Facebook and Instagram in 2023.
8. ActiveMQ flaw aids LockBit

   Threat actors are exploiting a now-patched security flaw in internet-facing Apache ActiveMQ servers (
   [CVE-2023-46604](https://thehackernews.com/2023/11/new-poc-exploit-for-apache-activemq.html)
   ) to deploy LockBit ransomware. "Despite being evicted after the initial intrusion, they successfully breached the same server on a second occasion 18 days later," The DFIR Report
   [said](https://thedfirreport.com/2026/02/23/apache-activemq-exploit-leads-to-lockbit-ransomware/)
   . "After compromising the server, the threat actor used Metasploit, possibly along with Meterpreter, to perform post-exploitation activities. These activities included escalating privileges, accessing LSASS process memory, and moving laterally across the network. After regaining access following their eviction, the threat actor swiftly transitioned to deploying ransomware. They leveraged credentials extracted during their previous breach to deploy LockBit ransomware via RDP." The ransomware is suspected to be crafted using the
   [leaked LockBit builder](https://thehackernews.com/2023/08/lockbit-30-ransomware-builder-leak.html)
   .
9. Chrome crash-to-command trick

   Two newly flagged Google Chrome extensions, Pixel Shield - Block Ads (ID: nlogodaofdghipmbdclajkkpheneldjd) and PageGuard - Phishing Protection (ID: mlaonedihngoginmmlaacpihnojcoocl), have been found to adopt the same playbook as
   [CrashFix](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html)
   , where the browser is deliberately crashed, and the user is tricked into running a malicious command à la ClickFix. The most concerning aspect of this campaign is that the extensions actually work and offer the advertised functionality. "The original NexShield DoS created a billion chrome.runtime.connect() calls," Annex Security's John Tuckner
   [said](https://annex.security/blog/promise-bomb/)
   . "These variants use a different technique I'm calling the Promise Bomb because it crashes the browser by flooding Chrome's message passing system with millions of unresolvable promises." While the original NexShield used timer-based activation, the new variants have evolved to push notification-based command-and-control (C2), causing the denial-of-service to be triggered only when the C2 server sends a push notification containing a "newVersion" value ending in "2." This, in turn, gives the attacker selective remote control over when the crashes happen.
10. WinRAR patch lag persists

    Cybersecurity firm Stairwell said more than 80% of the IT networks it monitors run versions of WinRAR vulnerable to
    [CVE-2025-8088](https://thehackernews.com/2026/01/google-warns-of-active-exploitation-of.html)
    , a vulnerability that has been widely exploited by cybercrime and cyber espionage groups. "This finding underscores a persistent challenge in enterprise security when widely deployed, trusted software that quietly falls out of date and becomes a high-value target for attackers," Alex Hegyi
    [said](https://stairwell.com/resources/stairwell-detects-widespread-exposure-to-critical-winrar-vulnerability-across-customer-environments/)
    .
11. Crypto IV reuse risk

    A new analysis from Trail of Bits has revealed that more than 723,000 open-source projects use cryptographic libraries with insecure defaults. The aes-js and pyaes libraries have been found to provide a default initialization vector (IV) in their AES-CTR API, leading to a large number of key/IV reuse bugs. "Reusing a key/IV pair leads to serious security issues: if you encrypt two messages in CTR mode or GCM with the same key and IV, then anybody with access to the ciphertexts can recover the XOR of the plaintexts, and that’s a very bad thing," Trail of Bits
    [said](https://blog.trailofbits.com/2026/02/18/carelessness-versus-craftsmanship-in-cryptography/)
    . While neither library has been updated in years, strongSwan has released an update to address the problem in strongMan (
    [CVE-2026-25998](https://github.com/strongswan/strongMan/security/advisories/GHSA-88w4-jv97-c8xr)
    ).
12. AI audits smart contracts

    OpenAI and Paradigm have jointly announced EVMbench, a benchmark that measures how well AI agents can detect, exploit, and patch high-severity smart contract vulnerabilities. "EVMbench draws on 120 curated vulnerabilities from 40 audits, with most sourced from open code audit competitions," OpenAI
    [said](https://openai.com/index/introducing-evmbench/)
    . "EVMbench is intended both as a measurement tool and as a call to action. As agents improve, it becomes increasingly important for developers and security researchers to incorporate AI-assisted auditing into their workflows."
13. Fake FSB extortion plot

    A Russian national has been accused of trying to extort money from the notorious Conti ransomware group by posing as an officer of Russia’s Federal Security Service (FSB), according to local media reports. RBC
    [reported](https://www.rbc.ru/society/25/02/2026/699d8a1b9a794762555ca146?)
    that the suspect, Ruslan Satuchin, posed as an FSB officer and demanded a large payment from Conti. Although an investigation was formally launched in September 2025, the incident allegedly began in September 2022 when Satuchin contacted one of the members of the hacker group and extorted them to avoid criminal liability. Once a prolific ransomware gang, Conti
    [shut down its operations](https://thehackernews.com/2022/05/conti-ransomware-gang-shut-down-after.html)
    in mid-2022 after splintering into small groups.
14. Ad cloaking service exposed

    Varonis has disclosed details of a newly identified cybercrime service known as 1Campaign that enables threat actors to run malicious Google Ads for extended periods of time while evading scrutiny. The cloaking platform "passes Google's screening, filters out security researchers, and keeps phishing and crypto drainer pages online for as long as possible, funneling real users to attacker-controlled sites," Varonis security researcher Daniel Kelley
    [said](https://www.varonis.com/blog/1campaign)
    . "It combines real-time visitor filtering, fraud scoring, geographic targeting, and a bot guard script generator into a single dashboard." It's developed and maintained by a threat actor named DuppyMeister for over three years, along with offering Telegram channels for support. Traffic linked to 1Campaign has been distributed across the U.S., Canada, the Netherlands, China, Germany, France, Japan, Hungary, and Albania.
15. Teams call drops macOS malware

    A social engineering campaign has been observed using Microsoft Teams meetings to trick attendants into installing macOS malware. Daylight Security has assessed that the activity is consistent with an ongoing attack campaign orchestrated by North Korean threat actors under the name
    [GhostCall](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html)
    . "During the call, the attacker claimed audio issues and coached the victim into running terminal commands that downloaded and executed malicious binaries," Daylight researchers Kyle Henson and Oren Biderman
    [said](https://daylight.ai/blog/prospect-call-microsoft-teams-meetings)
    . "Analysts observed staged downloads and execution from macOS cache and temporary paths, Keychain credential access, and outbound connections to newly created attacker-controlled domains."
16. RAMP fallout reshapes underground

    Last month, law enforcement authorities from the U.S. seized the
    [notorious RAMP cybercrime forum](https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html#major-cybercrime-forum-takedown)
    . The event has had a cascading impact, destabilising trust and accelerating fragmentation across the underground cybercrime ecosystem. There are also speculations that RAMP may have functioned as a honeypot or had been compromised long before its seizure. "Rather than consolidating around a single successor, ransomware actors are redistributing across both gated platforms like T1erOne and accessible forums such as Rehub," Rapid7
    [said](https://www.rapid7.com/blog/post/tr-post-ramp-allegations-fragmentation-ransomware-underground-rebuild/)
    . "This shift reflects adaptation, not decline. Disruption fractures trust and redistributes coordination across multiple platforms."
17. Anonymous Fénix members detained

    Spanish authorities have
    [announced](https://web.guardiacivil.es/es/destacados/noticias/Detenidos-los-cuatro-principales-integrantes-del-grupo-hacktivista-Anonymous-Fenix-por-ciberataques-contra-organismos-publicos/)
    the arrest of four members of the Anonymous Fénix group for their involvement in distributed denial-of-service (DDoS) attacks. The suspects, whose names were not disclosed, targeted the websites of government ministries, political parties, and public institutions. Two of the group leaders were arrested in May 2025. The first attacks occurred in April 2023. The group is said to have intensified its activities beginning in September 2024, recruiting volunteers to mount DDoS attacks against targets of interest.
18. Judicial spear-phish drops RAT

    A spear-phishing campaign has been observed targeting Argentina's judicial sector that delivers a ZIP archive containing a Windows shortcut that, when launched, displays a decoy PDF to the victims, while stealthily dropping a Rust-based remote access trojan (RAT). "The campaign leverages highly authentic judicial decoy documents to exploit trust in court communications, enabling successful delivery of a covert remote access trojan and facilitating long-term access to sensitive legal and institutional data," Seqrite Labs
    [said](https://www.seqrite.com/blog/operation-covert-access-weaponized-lnk-based-spear-phishing-targeting-argentinas-judicial-sector-to-deploy-a-covert-rat/)
    .
19. Typosquat spreads ValleyRAT

    A persuasive lookalike website of Huorong Security antivirus ("huoronga[.]com") has been used to deliver a RAT malware known as
    [ValleyRAT](https://thehackernews.com/2026/02/weekly-recap-double-tap-skimmers.html#:~:text=Phishing%20Campaigns%20in%20Taiwan%20Deliver%20Winos%204%2E0)
    . The campaign is the work of a Chinese cybercrime group called Silver Fox, which has a history of distributing trojanized versions of popular Chinese software and other popular programs through typosquatted domains to distribute trojanized installers responsible for deploying ValleyRAT. "Once it's installed, attackers can monitor the victim, steal sensitive information, and remotely control the system," Malwarebytes
    [said](https://www.malwarebytes.com/blog/scams/2026/02/huorong)
    .
20. Repo-squatting via Google Ads

    Users searching for developer tools have become the target of an ongoing campaign dubbed
    [GPUGate](https://thehackernews.com/2025/09/gpugate-malware-uses-google-ads-and.html)
    that uses a malicious installer to deliver
    [Hijack Loader](https://thehackernews.com/2025/04/new-malware-loaders-use-call-stack.html)
    and
    [Atomic Stealer](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html)
    . "The attacker creates a throwaway GitHub account and forks the official GitHub Desktop repository," GMO Cybersecurity by Ierae
    [said](https://gmo-cybersecurity.com/blog/revisiting-gpugate-repo-squatting-and-opencl-deception-to-deliver-hijackloader/)
    . "The attacker edits the download link in the README to point to their malicious installer and commits the change. Lastly, the attacker used sponsored ads for 'GitHub Desktop' to promote their commit, using an anchor in README.md to skip past GitHub's cautions." Victims who downloaded the malicious Windows installer would execute a multi-stage loader, while Mac victims received Atomic Stealer.

These stories may seem separate, but they point in the same direction. Speed is increasing. Deception is improving. And attackers are finding new ways to blend into everyday activity.

The warning signs are there for those who look closely. Small gaps, delayed patches, misplaced trust, and rushed clicks still make the biggest difference.

Staying aware of these shifts is no longer optional. The details change each week. The pressure does not.