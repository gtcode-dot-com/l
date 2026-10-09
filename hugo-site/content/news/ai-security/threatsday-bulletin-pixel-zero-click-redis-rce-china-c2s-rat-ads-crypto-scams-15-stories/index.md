---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T16:15:13.037976+00:00'
exported_at: '2026-01-22T16:15:15.290505+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/threatsday-bulletin-pixel-zero-click.html
structured_data:
  about: []
  author: ''
  description: Weekly cybersecurity bulletin tracking how routine systems are being
    quietly misused across platforms, infrastructure, and services.
  headline: 'ThreatsDay Bulletin: Pixel Zero-Click, Redis RCE, China C2s, RAT Ads,
    Crypto Scams & 15+ Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/threatsday-bulletin-pixel-zero-click.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: Pixel Zero-Click, Redis RCE, China C2s, RAT Ads, Crypto
  Scams & 15+ Stories'
updated_at: '2026-01-22T16:15:13.037976+00:00'
url_hash: c4e18e75a1a5495898e46d687758d082214ad008
---

**

Ravie Lakshmanan
**

Jan 22, 2026

Cybersecurity / Hacking News

Most of this week's threats didn't rely on new tricks. They relied on familiar systems behaving exactly as designed, just in the wrong hands. Ordinary files, routine services, and trusted workflows were enough to open doors without forcing them.

What stands out is how little friction attackers now need. Some activity focused on quiet reach and coverage, others on timing and reuse. The emphasis wasn't speed or spectacle, but control gained through scale, patience, and misplaced trust.

The stories below trace where that trust bent, not how it broke. Each item is a small signal of a larger shift, best seen when viewed together.

1. Spear-phishing delivers custom backdoor

   Government entities in Afghanistan have been at the receiving end of a spear-phishing campaign dubbed Operation Nomad Leopard that employs bogus administrative documents as decoys to distribute a backdoor named FALSECUB by means of a GitHub-hosted ISO image file. The campaign was first detected in late December 2025. "The ISO file contains three files," Seqrite Lab
   [said](https://www.seqrite.com/blog/operation-nomad-leopard-targeted-spear-phishing-campaign-against-government-entities-in-afghanistan/)
   . "The LNK file, Doc.pdf.lnk, is responsible for displaying the PDF to the victim and executing the payload. The PDF file, doc.pdf, contains the government-themed lure." The final payload is a C++ executable that's capable of receiving commands from an external server. The activity has not been attributed to any specific country or known hacker group. "The campaign appears to be conducted by a regionally focused threat actor with a low-to-moderate sophistication level," the Indian cybersecurity company added.
2. DoS attacks hit UK services

   The U.K. government is warning of continued malicious activity from Russian-aligned hacktivist groups like
   [NoName057(16)](https://www.ncsc.gov.uk/news/pro-russia-hacktivist-activity-continues-to-target-uk-organisations)
   targeting critical infrastructure and local government organizations in the country with denial-of-service (DoS) attacks. The end goal of these attacks is to take websites offline and disable access to essential services. "Although DoS attacks are typically low in sophistication, a successful attack can disrupt entire systems, costing organisations significant time, money, and operational resilience by having to analyse, defend against, and recover from them," the U.K. National Cyber Security Centre (NCSC)
   [said](https://www.ncsc.gov.uk/news/ncsc-issues-warning-over-hacktivist-groups-disrupting-uk-organisations-online-services)
   .
3. Trusted apps load malicious DLLs

   Google-owned VirusTotal has
   [disclosed](https://blog.virustotal.com/2026/01/malicious-infostealer-january-26.html)
   details of an information stealer campaign that relies on a trusted executable to trick the operating system into loading a malicious DLL ("CoreMessaging.dll") payload – a technique called
   [DLL side-loading](https://thehackernews.com/2026/01/hackers-use-linkedin-messages-to-spread.html)
   – leading to the execution of secondary-stage infostealers designed to exfiltrate sensitive data. Both the executable and the DLL are distributed via ZIP archives that mimic installers for legitimate applications like Malwarebytes (e.g., "malwarebytes-windows-github-io-6.98.5.zip") and other programs.
4. WSL abused without process spawn

   SpecterOps researcher Daniel Mayer has
   [released](https://github.com/MayerDaniel/the-one-wsl-bof)
   a beacon object file (
   [BOF](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm)
   ) – a compiled C program designed to run within the memory of a post-exploitation agent like Cobalt Strike Beacon – that
   [interacts](https://specterops.io/blog/2026/01/16/one-wsl-bof-to-rule-them-all/)
   with the Windows Subsystem for Linux (WSL) by directly invoking the WSL COM service, avoiding process creation for "wsl.exe" entirely and allowing operators to list all installed WSL distributions and execute arbitrary commands on any WSL distribution that the BOF finds.
5. Ads push covert RAT installers

   Cybersecurity researchers have disclosed an active malicious campaign that uses advertisements placed on legitimate websites to lure users into downloading "converter" tools for converting images or documents. These services share a similar website template and go by names like Easy2Convert, ConvertyFile, Infinite Docs, and PowerDoc. Should a user end up attempt to download the program, they are redirected to another domain that actually hosts the C# dropper files. "In the foreground, these tools usually work as promised, so users do not become suspicious," Nextron Systems
   [said](https://www.nextron-systems.com/2026/01/14/free-converter-software-convert-any-system-from-clean-to-infected-in-seconds/)
   . "In the background, however, they behave almost identically: they install persistent remote access trojans (RATs) that give the threat actor continuous access to the victim system." Specifically, the executable is designed to establish persistence using a scheduled task, which points to the main payload, a .NET application that initiates communication with a remote server, executes .NET assemblies received from the server, and sends the results back via an HTTP POST request.
6. Short-lived TLS certs roll out

   Let's Encrypt said its short-lived TLS certificates with a 6-day lifetime are now generally available. Each certificate is valid for a period of 160 hours from the time it is issued. "Short-lived certificates are opt-in and we have no plan to make them the default at this time. Subscribers that have fully automated their renewal process should be able to switch to short-lived certificates easily if they wish, but we understand that not everyone is in that position and generally comfortable with this significantly shorter lifetime," Let's Encrypt
   [said](https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability)
   . To request one, operators must select the "shortlived" profile in their ACME client. Short-lived certificates are opt-in and there are no plans to make them the default at this time, the non-profit certificate authority added.
7. Support tickets abused for spam

   Zendesk has revealed that unsecured support systems are being used to
   [send spam emails](https://www.reddit.com/r/Zendesk/comments/1qhiz79/how_do_i_stop_receiving_spam_ticket_emails/)
   . The attacks take advantage of Zendesk's ability to allow unverified users to submit support tickets, which then automatically generate confirmation emails that are sent to the email address entered by the attacker. This automated response system is being weaponized to turn the support platform into a delivery vehicle for spam by creating fake tickets. "These emails look like legitimate contacts from companies that use Zendesk to communicate with their customers, and are a spam tactic known as relay spam," the customer relationship management (CRM) vendor
   [said](https://support.zendesk.com/hc/en-us/articles/9833274501786-Important-notice-about-recent-spam-emails-via-Zendesk)
   in an advisory. The company described it as a "potential side effect" that arises when Zendesk is set to allow unverified users to submit requests, adding that it's actively working to reduce spam and prevent new spam campaigns. It has also urged customers to remove specific placeholders from first-reply triggers and permit only added users to submit tickets.
8. EU targets high-risk suppliers

   The European Commission has
   [proposed](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-eu-cybersecurity-act)
   new cybersecurity legislation mandating the removal of high-risk suppliers to secure telecommunications networks and strengthen defenses against state-backed and cybercrime groups targeting critical infrastructure. "The new Cybersecurity Act aims to reduce risks in the EU's ICT supply chain from third-country suppliers with cybersecurity concerns," the Commission
   [said](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_105)
   . "It sets out a trusted ICT supply chain security framework based on a harmonised, proportionate and risk-based approach. This will enable the E.U. and Member States to jointly identify and mitigate risks across the EU's 18 critical sectors, considering also economic impacts and market supply." The revised Cybersecurity Act is also expected to ensure that products and services reaching E.S. consumers are tested for security in a more efficient way through a renewed European Cybersecurity Certification Framework (ECCF). The amended act will take effect immediately upon approval by the European Parliament and the Council of the E.U. Once adopted, member states have one year to implement the directive into national law.
9. Mass scans probe plugin exposure

   Threat intelligence firm GreyNoise has
   [uncovered](https://www.labs.greynoise.io/grimoire/2026-01-19-creepy-crawlers-hunting-those-who-hunt-for-wordpress-plugins/index.html)
   a large-scale WordPress plugin reconnaissance activity aimed at enumerating potentially vulnerable sites. The mass scanning, observed between October 20, 2025, and January 19, 2026, involved 994 unique IP addresses across 145 ASNs targeting 706 distinct WordPress plugins in over 40,000 unique enumeration events. The most targeted plugins are Post SMTP, Loginizer, LiteSpeed Cache, SEO by Rank Math, Elementor, and Duplicator. The activity touched a new high on December 7, 2025, when 6,550 unique sessions were recorded. More than 95% of the spike was driven by a single IP address: 112.134.208[.]214. Users of the aforementioned plugins are advised to keep them up-to-date.
10. Crate vulnerabilities surface early

    The Rust project has updated Crates.io to include a "Security" tab on individual crate pages. The tab displays security advisories drawn from the RustSec database and lists which versions of a crate may have known vulnerabilities. This change gives developers an easy way to view relevant security information before adding the crate as a dependency. "The tab shows known vulnerabilities for the crate along with the affected version ranges," the maintainers
    [said](https://blog.rust-lang.org/2026/01/21/crates-io-development-update/)
    . Other improvements include expanded Trusted Publishing support, which now works with GitLab CI/CD in addition to GitHub Actions, and a new Trusted Publishing mode that, when enabled, turns off traditional API token-based publishing so as to reduce the risk of unauthorized publishes from leaked API tokens. Trusted Publishing has also been updated to block pull\_request\_target and workflow\_run GitHub Actions triggers. "These triggers have been responsible for multiple security incidents in the GitHub Actions ecosystem and are not worth the risk," the Crates.io team said.
11. China hosts vast C2 footprint

    A
    [new analysis](https://hunt.io/blog/china-hosting-malware-c2-infrastructure)
    from Hunt.io has revealed that the Chinese internet space is hosting more than 18,000 active command-and-control (C2 or C&C) servers across 48 different providers in the last three months. China Unicom hosts nearly half of all observed servers, with Alibaba Cloud and Tencent following suit. More than half of the C2 servers (about 9,427 unique C2 IPs) are used to control an IoT botnet known as
    [Mozi](https://thehackernews.com/2024/11/androxgh0st-malware-integrates-mozi.html)
    . A chunk of the remaining C2 servers is used for activity related to Cobalt Strike (1,204), Vshell (830), and Mirai (703). "Across Chinese hosting environments, a small number of large telecom and cloud providers account for the majority of observed command-and-control activity, supporting everything from commodity malware and IoT botnets to phishing operations and state-linked tooling," Hunt.io said.
12. Military-linked espionage probe

    A 33-year-old former IT consultant for Sweden's Armed Forces has been
    [detained](https://www.aklagare.se/for-media/pressmeddelanden/2026/januari/uppdatering-i-arende-om-misstankt-spioneri/)
    on suspicion of passing information to Russia's intelligence service, according to the Swedish Prosecution Authority. The suspected criminal activity took place throughout 2025 and until January 4, 2026, but Swedish authorities suspect the espionage may have been ongoing since 2022, when Russia launched its full-scale invasion of Ukraine. The suspect, who has denied any wrongdoing, worked as an IT consultant for the Swedish military from 2018 to 2022,
    [per the AFP](https://www.barrons.com/news/swede-suspected-of-spying-for-russia-prosecutor-b9defd53)
    . The investigation is said to be still in early stages. In February 2021, a 47-year-old Swedish tech consultant was
    [charged](https://www.euronews.com/2021/02/22/sweden-charges-man-for-selling-high-tech-industry-information-to-russian-diplomat)
    with espionage for allegedly selling information about truckmaker Scania and Volvo Cars to a Russian diplomat for several years. He was sentenced to
    [three years in prison](https://www.reuters.com/world/europe/swedish-court-finds-man-guilty-spying-russia-truckmaker-scania-2021-09-15/)
    later that September.
13. Supply-chain platform fully exposed

    Critical vulnerabilities (from CVE-2026-22236 through CVE-2026-22240) have been disclosed in the
    [Bluvoyix](https://blusparkglobal.com/bluvoyix/)
    platform of Bluspark Global, a cloud-based solution that's used to help shippers manage their supply chain data, which could have allowed a bad actor to gain full control of the platform and access customer and shipment data. They could have enabled access to customer accounts and track freight and component shipments, as well as enabled complete access to the platform's API without the need for authentication. This loophole could have been weaponized to create administrator accounts for follow-on exploitation. The vulnerabilities have since been patched, but not before a
    [protracted disclosure process](https://techcrunch.com/2026/01/14/us-cargo-tech-company-publicly-exposed-its-shipping-systems-and-customer-data-to-the-web/)
    . Security researcher Eaton Zveare, who has
    [previously](https://thehackernews.com/2023/06/password-reset-hack-exposed-in-hondas-e.html)
    [uncovered](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=Flaws%20in%20Carmaker%20Dealership%20Portal)
    [security holes](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html#:~:text=Security%20Weaknesses%20in%20Tata%20Motors%20Sites)
    in platforms used by automotive firms,
    [said](https://eaton-works.com/2026/01/14/bluspark-bluvoyix-hack/)
    the "admin access made it possible to view, modify, and even cancel customer shipments going back to 2007."
14. Crypto scams hit record scale

    Cryptocurrency scams
    [received](https://www.chainalysis.com/blog/crypto-scams-2026/)
    at least $14 billion worth of cryptocurrency in 2025, a jump from $12 billion reported in the year prior. The average scam payment extracted from victims also increased from $782 to $2,764. High-yield investment and pig butchering remained the most dominant categories by volume, even as impersonation scams – which involve fraudsters posing as legitimate organizations such as
    [E-ZPass](https://thehackernews.com/2025/11/google-sues-china-based-hackers-behind.html)
    to manipulate victims into transferring funds – surged 1,400%. Based on historical trends, the 2025 figure is projected to exceed $17 billion as more illicit wallet addresses are identified in the coming months, Chainalysis said. Scammers have been found increasingly leveraging deepfake technology and AI-generated content to create convincing impersonations in romance and investment scams. "Major scam operations became increasingly industrialized, with sophisticated infrastructure, including phishing-as-a-service tools, AI-generated deepfakes, and professional money laundering networks," the company said. "Pig-butchering networks across Southeast Asia, drawing heavily on CMLNs [Chinese money laundering networks], generate billions of dollars annually and rely on layered wallet structures, exchanges, shell companies, and informal banking channels to launder funds and convert crypto into real-world assets, including real estate and luxury goods."
15. ATM malware ring dismantled

    A group of five Venezuelan nationals has
    [pleaded guilty](https://www.justice.gov/usao-mdga/pr/multi-state-atm-jackpotting-ring-busted-middle-district-georgia)
    or been sentenced for their involvement in a multi-state
    [ATM jackpotting thefts](https://thehackernews.com/2025/12/us-doj-charges-54-in-atm-jackpotting.html)
    between September 14 and 16, 2024, that used sophisticated malware to steal thousands of dollars across Georgia, Florida, and Kentucky. The group, Hector Alejandro Alvarado Alvarez (20), Cesar Augusto Gil Sanchez (22), Javier Alejandro Suarez-Godoy (20), David Josfrangel Suarez-Sanchez (24), and Giobriel Alexander Valera-Astudillo (26), targeted various financial institutions by deploying malware or accessing the ATM's supervisor mode to trigger cash withdrawals. Members of the group were caught on camera carrying out the attacks and were identified based on fingerprints left behind on the ATM machines. They face up to 30 years in prison, followed by immediate deportation.
16. Zero-click chain hits Pixel

    Google Project Zero has released a zero-click exploit (
    [Part 1](https://projectzero.google/2026/01/pixel-0-click-part-1.html)
    ,
    [Part 2](https://projectzero.google/2026/01/pixel-0-click-part-2.html)
    , and
    [Part 3](https://projectzero.google/2026/01/pixel-0-click-part-3.html)
    ) that can compromise Android smartphones via the Dolby audio decoder. The exploit is made possible because the Google Messages application automatically processes incoming audio attachments in the background for transcription purposes and decodes them without requiring user interaction. The exploit leverages
    [CVE-2025-54957](https://project-zero.issues.chromium.org/issues/428075495)
    to gain arbitrary code execution in the mediacodec context of a Google Pixel 9, and then makes use of
    [CVE-2025-36934](https://project-zero.issues.chromium.org/issues/426567975)
    , a use-after-free in the BigWave driver, to escalate privileges from mediacodec to kernel on the device. "The time investment required to find the necessary vulnerabilities was small compared to the impact of this exploit, especially for the privilege escalation stage," researcher Natalie Silvanovich said. "The time needed to find the bugs for a 0-click exploit chain on Android can almost certainly be measured in person-weeks for a well-resourced attacker." While Dolby
    [patched](https://professional.dolby.com/siteassets/pdfs/dolby-security-advisory-CVE-2025-54957-Oct-14-25.pdf)
    the flaw in October 2025, Samsung was the first mobile vendor to patch the vulnerability the next month. Pixel devices did not get the patch until January 5, 2026. A patch for the BigWave driver flaw was shipped to Pixel devices on January 6, 2026.
17. Malicious ads seed infostealer

    A malvertising campaign
    [detected](https://www.sophos.com/pt-br/blog/tamperedchef-serves-bad-ads-with-infostealers-as-the-main-course)
    by Sophos in September 2025 used Google Ads to redirect victims to deceptive sites that promoted a trojanized PDF editing application called AppSuite PDF Editor. The application, once installed, appeared legitimate to users, but stealthily delivered an information stealer dubbed
    [TamperedChef](https://thehackernews.com/2025/11/tamperedchef-malware-spreads-via-fake.html)
    targeting Windows devices. The actively evolving threat cluster is known to employ tactics like delayed execution, staying dormant for about 56 days before activating the infostealer behavior to ensure persistence. The time period aligns with the typical 30-60-day cycle of paid advertising campaigns. TamperedChef is assessed to be a part of a wider campaign known as EvilAI. According to telemetry data gathered by the cybersecurity company, over 100 systems were affected by the campaign, with the majority of the victims located in Germany (~15%), the U.K. (~14%), and France (~9%). "Victims of this campaign span a variety of industries, particularly those where operations rely heavily on specialized technical equipment – possibly because users in those industries frequently search online for product manuals, a behavior that the TamperedChef campaign exploits to distribute malicious software," the company said.

    [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5JfFL1Qfc_gchFg1tnzMLQ7awTYglqaHvC5uB0-4Ep8BhVGzVhPwWnH7nWV9MNkhrNrTbUuGjWGV36XrvnfKEvAA_cGUPQAEw5-SKLq0eyYWJFCVTyOrRJvVCrNwU7AgKvddnfRp8HYsKUPIOgzT711GT-6feWSXUxU4LX_GBFtsK5FdyGgp2RR9tgi0N/s1600-e365/xops.png)
18. PNG files hide JS stealer

    A new phishing campaign has been observed using phony pharmaceutical invoices to trick recipients into opening ZIP archives containing JavaScript that, upon execution, uses PowerShell to download a malicious PNG image hosted on the Internet Archive. "But this isn't actually a standard PNG. Well, it is, but with extras," Swiss Post Cybersecurity
    [said](https://www.swisspost-cybersecurity.ch/news/purelogs-infostealer-analysis-dont-judge-a-png-by-its-header)
    . "The attackers embedded a Base64-encoded payload after the IEND chunk of the PNG, which marks the official end of the image data. The file still renders as a valid image in any viewer. The actual malware sits between two custom markers, BaseStart- and -BaseEnd." The extracted payload between these markers is used to launch a malware loader known as VMDetectLoader, which is responsible for persistence, environment checks, and launching
    [PureLogs Stealer](https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html)
    , a commodity stealer developed by a threat actor known as PureCoder. It's worth noting that VMDetectLoader has been
    [previously used](https://thehackernews.com/2025/06/weekly-recap-airline-hacks-citrix-0-day.html#:~:text=Hive0131%20Campaign%20Delivers%20DCRat%20in%20Colombia)
    to deliver DCRat in attacks targeting Colombia.
19. Loan lures harvest bank data

    A large-scale loan phishing operation in Peru has been
    [discovered](https://www.group-ib.com/blog/peru-digital-loan-scam/)
    abusing fake loan offers to harvest sensitive personal and banking information (bank card details, online banking password, and a 6-digit PIN code) from unsuspecting users. The campaign is propagated via social media advertisements. The threat actors behind the operation have created approximately 370 unique domains impersonating banks in Peru, Colombia, El Salvador, Chile, and Ecuador since 2024. "This particular phishing targets individuals through a seemingly legitimate loan application process, designed to harvest valid card credentials and corresponding PIN codes," Group-IB said. "These credentials are then either sold on the black market or used in further phishing activities." As soon as the details are entered on the fake sites, a script running in the background on the web page validates the information using the
    [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)
    to ensure that the entered credit card details and government identification number are genuine.
20. Fake installer sells bandwidth

    A threat actor tracked as Larva-25012 is making use of a fake Notepad++ installer as a lure to distribute
    [proxyware](https://thehackernews.com/2025/07/threat-actor-mimo-targets-magento-and.html)
    in attacks targeting South Korea. The installers, written in C++ and hosted on GitHub, are promoted through advertisement pages on websites posing as download portals for cracked or otherwise illegal software. "These installers drop the downloader malware DPLoader. Once registered in the Windows Task Scheduler, DPLoader executes persistently and retrieves commands from its C&C server. All PowerShell scripts observed to date have included logic to install various Proxyware tools," AhnLab
    [said](https://asec.ahnlab.com/en/92183/)
    . "In addition, the attacker is actively changing techniques to evade detection -- such as injecting Proxyware into the Windows Explorer process or leveraging Python-based loaders." The objective of these attacks is to install proxyware on the victim's machine without their knowledge, and monetize their unused internet bandwidth by selling it to third parties. Larva-25012 is assessed to be active since at least 2024, distributing multiple types of proxyware, including DigitalPulse, Honeygain, and Infatica.

Taken together, these incidents show how quickly the "background layer" of technology has become the front line. The weakest points weren't exotic exploits, but the spaces people stop watching once systems feel stable.

The takeaway isn't a single threat or fix. It's the pattern: exposure accumulates quietly, then surfaces all at once. The full list makes that pattern hard to ignore.