---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-30T14:15:15.114937+00:00'
exported_at: '2026-04-30T14:15:19.499368+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/threatsday-bulletin-sms-blaster-busts.html
structured_data:
  about: []
  author: ''
  description: 'Latest ThreatsDay: SMS blasters, npm supply chain hits, and unpatched
    Windows flaws. Stay ahead of new phishing kits and exposed servers.'
  headline: 'ThreatsDay Bulletin: SMS Blaster Busts, OpenEMR Flaws, 600K Roblox Hacks
    and 25 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/threatsday-bulletin-sms-blaster-busts.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: SMS Blaster Busts, OpenEMR Flaws, 600K Roblox Hacks and
  25 More Stories'
updated_at: '2026-04-30T14:15:15.114937+00:00'
url_hash: 2cb115c84d548b2e0bd08028528e9fa8a9fcf320
---

**

Ravie Lakshmanan
**

Apr 30, 2026

Hacking News / Cybersecurity News

The internet is noisy this week. We are seeing some wild new tactics, like people using fake cell towers to send scam texts, while some developers are accidentally downloading tools that peek into their private files during a simple install. It is definitely a busy time to be online.

Security is always a moving target. Millions of servers are currently sitting online without any passwords, and old software bugs are showing up in the most unexpected places. Even with the right fixes available, staying one step ahead is a full-time job for all of us.

Data is shifting in strange ways, too. Some browser tools are now legally selling user history for profit, and new kits are making it simpler for almost anyone to launch a campaign. You have to see these latest updates to believe them. Let’s look at the full list...

1. SMS blaster phishing crackdown

   Canadian authorities have arrested three men for operating an SMS blaster device that masquerades as a cellular tower to send phishing texts to nearby phones. These tools trick devices into connecting to them by emitting signals that mimic a legitimate tower. "An SMS blaster works by mimicking a legitimate cellular tower. When nearby phones connect to it, users receive fraudulent text messages that appear to come from trusted organizations," authorities
   [said](https://www.tps.ca/media-centre/stories/unprecedented-sms-blaster-arrests/)
   . "These messages often prompt recipients to click on links that lead to fake websites designed to capture personal information, including banking credentials and passwords." The three men are facing 44 charges in connection with the crime. About tens of thousands of devices were connected to the blaster over several months, the official said. This is the first time that an SMS blaster has been spotted in the country.
2. npm brandsquat data theft

   A new supply chain attack has leveraged an npm package impersonating TanStack to ship malicious versions that exfiltrate environment variables from developers’ machines during install. The package, named tanstack, is designed to "silently steal environment variable files, including .env, .env.local, and .env.production, from developers' machines at install time, exfiltrating them to an attacker-controlled endpoint," Socket
   [said](https://socket.dev/blog/tanstack-brandsquat-compromise)
   . The malicious package is maintained by a user named "sh20raj." Versions 2.0.4 through 2.0.7 are confirmed malicious.
3. Extensions legally sell user data

   In a new analysis, LayerX found that multiple networks of browser extensions collect user data and resell it for profit. Unlike malicious extensions that conceal their behavior by offering some harmless functionality, the identified 80 extensions explicitly inform users in their privacy policy that they collect and sell data of users who install their extensions. "A network of 24 media extensions that are installed on 800,000 users and collect viewing data and demographic information on major streaming platforms such as Netflix, Hulu, Disney+, Amazon Prime Video, HBO, Apple TV, and others," LayerX
   [said](https://layerxsecurity.com/blog/your-extensions-sell-your-data-and-its-perfectly-legal/)
   . "12 separate ad blockers with a combined install base of over 5.5 million users openly selling user data. Nearly 50 other extensions, with over 100,000 users in aggregate, that collected and resold users’ browsing data."
4. Komari tool weaponized in attacks

   Huntress has revealed that unknown threat actors used stolen VPN credentials to pivot into a Windows workstation belonging to an unspecified organization via Impacket's smbexec.py, and dropped a SYSTEM-level backdoor using the
   [Komari](https://github.com/komari-monitor/komari)
   agent, a Go-based remote-control, monitoring, and management tool. The development marks the first publicly documented case of the tool being abused in a real-world intrusion. It also illustrates how bad actors are increasingly switching to publicly available and legitimate tools to conduct attacks. "Komari is not a telemetry tool that happens to be abusable - it is a bidirectional control channel by design. The agent opens a persistent WebSocket to its server and accepts three server-to-agent event types out of the box: exec (arbitrary command execution via PowerShell / sh), terminal (interactive PTY reverse shell in the operator's browser), and ping (ICMP / TCP / HTTP probing)," Huntress
   [said](https://www.huntress.com/blog/komari-c2-agent-abuse?hnt=y0ni9ucare7o)
   . "All three are enabled by default." Whereas other tools like Velociraptor and SimpleHelp that have been abused by threat actors typically act as means to an end, Komari gives an operator arbitrary command execution, an interactive PTY reverse shell, and network probing by default, over a TLS-fronted WebSocket.
5. Next-gen phishing kits escalate

   Threat actors have detailed two new phishing kits named Saiga 2FA and Phoenix System that have been linked to emails and SMS phishing attacks. According to Barracuda, Saiga 2FA goes beyond traditional adversary-in-the-middle (
   [AitM](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html)
   ) features by integrating tools like FM Scanner for extracting and analyzing mailbox content. "Saiga 2FA is an example of how phishing kits are evolving into application-level platforms," the company
   [said](https://blog.barracuda.com/2026/04/28/threat-spotlight--boutique-phishing-kit-saiga-2fa)
   . "Unlike traditional phishing kits, Saiga integrates infrastructure, automation, and post-compromise capabilities into a unified system, supporting advanced and highly targeted campaigns." Phoenix System, on the other hand, has been tied to over 2,500 phishing domains since January 2025, while relying on IP-based filtering and geofencing for precision targeting. It's assessed to be the successor to the now-defunct Mouse System. "The campaigns are delivered via SMS, potentially leveraging fake Base Transceiver Stations (BTS) to bypass carrier-level filtering and allow threat actors to send messages that appear under the brand names of trusted organizations directly to victims," Group-IB
   [said](https://www.group-ib.com/blog/phoenix-phaas-kit-smishing/)
   . "The campaign has so far targeted more than 70 organizations across the financial services, telecommunications, and logistics sectors globally."
6. Mass exposure of remote access servers

   A new analysis from Forescout has found 1.8 million RDP and 1.6 million VNC servers are exposed on the internet. "China accounts for 22% of exposed RDP and 70% of exposed VNC servers; the U.S. accounts for 20% and 7%; Germany accounts for 8% and 2%," the company
   [said](https://www.forescout.com/blog/rdp-security-cps-threats-spark-need-for-secure-remote-access/)
   . "Of 91,000 RDP and 29,000 VNC servers mapped to specific industries, retail, services, and education lead RDP exposure; education, services, and healthcare lead VNC." What's more, 18% of exposed RDP servers run end-of-life Windows versions, more than 19,000 RDP servers remain vulnerable to BlueKeep (CVE-2019-0708), and nearly 60,000 VNC servers have authentication disabled. To make matters worse, more than 670 exposed VNC servers have authentication disabled and provide direct access to OT/ICS control panels.
7. China-linked influence op falters

   A China-linked online influence campaign attempted to undermine April 26 elections for the Tibetan parliament-in-exile with little impact. The operation, part of
   [Spamouflage](https://thehackernews.com/2023/09/meta-takes-down-thousands-of-accounts.html)
   , a long-running influence network linked to Beijing, has used a cluster of 90 Facebook profiles and 13 Instagram profiles to push criticism of the Tibetan government-in-exile and its leadership. "The network tries to drive wedges within the community," DFRLab
   [said](https://dfrlab.org/2026/04/24/china-linked-spamouflage-targets-tibetan-parliament-in-exile-elections/)
   . "The goal is to erode trust in the exile government, weaken its international voice, and raise doubts about whether it can credibly represent Tibetans without the Dalai Lama. However, virtually none of these posts seem to have attracted any organic engagement, possibly because all the identified assets are regular Facebook profiles with limited reach and not established pages."
8. Unpatched RPC privilege escalation

   An unpatched vulnerability can allow for local privilege escalation in Windows systems through the abuse of the Remote Procedure Call (RPC) architecture in the operating system. Called
   [PhantomRPC](https://securelist.com/phantomrpc-rpc-vulnerability/119428/)
   , the flaw stems from an architectural weakness in how RPC handles connections to unavailable services. To
   [exploit the flaw](https://github.com/klsecservices/PhantomRPC)
   , an attacker with limited local access needs to first compromise a privileged service that runs under the Network Service identity, deploy a fake RPC server with the same RPC interface UUID and exposed endpoint name (i.e., TermService), listen to specific requests, and then impersonate the targeted service to escalate their privileges to SYSTEM. Kaspersky, which identified the weakness, said it discovered four PhantomRPC exploitation paths that could lead to privilege escalation. Following responsible disclosure in September 2025, Microsoft opted to not address the issue as it requires an attacker to first compromise the machine through some other means.
9. Vidar dominates infostealer market

   The information stealer known as Vidar (now in its second iteration called
   [Vidar Stealer 2.0](https://www.trendmicro.com/en_us/research/25/j/how-vidar-stealer-2-upgrades-infostealer-capabilities.html)
   ) has vaulted to the top of the infostealer market since November 2025 in the aftermath of law enforcement takedowns of Lumma and Rhadamanthys. "Vidar profited from the generated chaos to rise to the top of the stealer ecosystem," Intrinsec
   [said](https://www.intrinsec.com/wp-content/uploads/2026/04/TLP_CLEAR-20260424-New_Vidar.pdf)
   . "We assess that this rise was made available due to the release of version 2.0 of the malware, and to the collaboration with 'Cloud' Telegram channels." It's advertised by a user named "Loadbaks" on underground forums. Recent campaigns have been observed distributing malware that has used bogus links shared via YouTube videos promoting fake software to direct users to Mediafire pages, which are used to deliver executables responsible for downloading and running the broad-spectrum credential harvester. The stolen credentials are then quickly monetized on underground marketplaces like Russian Market.
10. Critical flaws hit healthcare platform

    Thirty-eight critical security vulnerabilities have been disclosed in OpenEMR, the world's most widely used open-source electronic medical records platform. The vulnerabilities, now patched, range in severity from medium to critical and include missing or incorrect authorization checks, cross-site scripting (XSS), SQL injection, path traversal, and insufficient session expiration. These issues, which include two designated critical (CVE-2026-24908 and CVE-2026-23627), could have been exploited to access and tamper with patient and provider data, posing a serious health and regulatory risk to individuals and institutions. "In the most severe cases, SQL injection vulnerabilities combined with modest database privileges could have led to full database compromise, PHI exfiltration at scale, and remote code execution on the server," AISLE
    [said](https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers)
    . OpenEMR is used by more than 100,000 medical providers, serving more than 200 million patients in 34 languages.
11. Swiss crackdown on Black Axe

    A coordinated police operation in Switzerland has led to the arrest of 10 suspected members of the
    [Black Axe](https://thehackernews.com/2026/01/europol-arrests-34-black-axe-members-in.html)
    criminal network, including the Black Axe "Regional Head" for the Southern European region. Most of those arrested are reported to be of Nigerian origin. The suspects are accused of numerous crimes, including romance scams, cyber fraud offences causing millions of Swiss francs in damages, and money laundering. "The criminal network is known for its involvement in a wide range of criminal activities, including cyber-enabled fraud, drug trafficking, human trafficking and prostitution, kidnapping, armed robbery, and fraudulent spiritual practices," Europol
    [said](https://www.europol.europa.eu/media-press/newsroom/news/europol-supports-hit-against-black-axe-criminal-organisation-in-switzerland-10-arrests)
    .
12. PyPI package hijacked via CI exploit

    In yet another software supply chain attack, unknown threat actors pushed a malicious version of the popular "elementary-data" package on the Python Package Index (PyPI) to steal sensitive developer data and cryptocurrency wallets. According to StepSecurity, elementary-data version 0.23.3 was uploaded to PyPI on April 24, 2026, at 10:20 p.m. UTC. The attacker opened a pull request with malicious code and exploited a script-injection vulnerability in one of its GitHub Actions workflows to publish it as release 0.23.3. Specifically, it came embedded with a "elementary.pth" file that enabled the theft of developer credentials and secrets. "The attacker exploited a script injection vulnerability in one of the project's own GitHub Actions workflows, then used the workflow's GITHUB\_TOKEN to forge a signed release commit and dispatch the legitimate publishing pipeline against it – without ever touching the master branch or opening a pull request," the company
    [said](https://www.stepsecurity.io/blog/elementary-data-compromised-on-pypi-and-ghcr-forged-release-pushed-via-github-actions-script-injection)
    . The developers urged users who installed 0.23.3, or pulled and ran its Docker image, to
    [assume compromise and rotate any credentials](https://www.elementary-data.com/post/security-incident-report-malicious-release-of-elementary-oss-python-cli-v0-23-3)
    .
13. $230M crypto laundering sentence

    22-year-old Evan Tangeman of Newport Beach, California, was sentenced to 70 months in prison for laundering funds stolen in a massive
    [$230 million cryptocurrency heist](https://www.justice.gov/usao-dc/pr/indictment-charges-two-230-million-cryptocurrency-scam)
    as part of an elaborate social engineering scheme. "This criminal enterprise was built on greed so brazen it borders on the cartoonish. They stole millions, spent it on half-million-dollar nightclub tabs, Lamborghinis, and Rolexes,"
    [said](https://www.justice.gov/usao-dc/pr/california-money-launderer-sentenced-dc-70-months-role-scheme-stole-263-million)
    U.S. Attorney Jeanine Ferris Pirro. "But Evan Tangeman didn't just launder the money that fueled that lifestyle. When his co-conspirators were arrested, he moved to destroy the evidence. That is consciousness of guilt, and this office and the court have treated that accordingly." Tangeman pleaded guilty in December 2025. The criminal enterprise began no later than October 2023 and continued through at least May 2025.
14. Legacy TLS finally deprecated

    Microsoft has announced plans to start blocking legacy TLS connections for POP and IMAP email clients in Exchange Online starting in July 2026. "We're planning to fully deprecate support for legacy TLS versions (TLS 1.0 and TLS 1.1) for POP3 and IMAP4 connections to Exchange Online. These older TLS versions have been industry-deprecated for some time and are no longer considered secure," the company
    [said](https://techcommunity.microsoft.com/blog/exchange/deprecating-legacy-tls-and-endpoints-for-pop-and-imap-in-exchange-online/4515201)
    . "Several years ago, we started the move to block these older versions, but we did allow you to use them by opting in; we're now removing support for them entirely. Our expectation is that only customers who have explicitly opted into using those legacy endpoints are impacted by the deprecation."
15. Phishing via account flow abuse

    Threat actors are
    [abusing](https://www.reddit.com/r/phishing/comments/1swovb5/phishing_email_from_verified_robinhood_sender/)
    online trading platform Robinhood's account creation process to send phishing emails that bypass spam filters. The emails, which originate from "noreply@robinhood[.]com," warn of suspicious activity tied to their accounts and urge them to click to complete a security check by clicking on a link that directs to a phishing site. "This phishing attempt was made possible by an abuse of the account creation flow," Robinhood
    [said](https://x.com/AskRobinhood/status/2048649252352487683)
    in an X post. "It was not a breach of our systems or customer accounts, and personal information and funds were not impacted. If you received this email, please delete it and do not click any suspicious links. If you have clicked a suspicious link or have any questions about your account, please contact us directly within the Robinhood app or website." Reports on Reddit
    [indicate](https://www.reddit.com/r/phishing/comments/1swozms/comment/oijfv4c/)
    that the attackers created new Robinhood accounts using modified versions of existing Gmail addresses via the so-called "dot trick." The technique takes advantage of the fact that Gmail ignores periods inserted into or removed from a username, whereas Robinhood treats each variation as a distinct user, allowing the attackers to create a new account that points to an existing account.
16. Social media scams surge

    The U.S. Federal Trade Commission (FTC) warned of a massive increase in losses from social media scams since 2020, exceeding $2.1 billion in 2025, including $794 million to scams that started on Facebook, more than on any other platform. "In 2025, nearly 30% of people who reported losing money to a scam said that it started on social media, with reported losses reaching a staggering $2.1 billion. Social media scams produced far more in losses – an eightfold increase since 2020 – than any other contact method used by scammers to reach consumers," the FTC
    [said](https://www.ftc.gov/news-events/news/press-releases/2026/04/new-ftc-data-show-people-have-lost-billions-social-media-scams)
    . "Social media creates easy access to billions of people from anywhere in the world, making a scammer's job easier at very little cost. Scammers may hack a user's account, exploit what a user posts to figure out how to target them, or buy ads and use the same tools used by real businesses to target people by age, interests, or shopping habits."
17. Billions of credentials exposed

    KELA
    [said](https://www.kelacyber.com/blog/the-state-of-cybercrime-2026/)
    it tracked 2.86 billion compromised credentials in 2025 globally. These included usernames, passwords, session tokens, cookies found in URL, login and password (ULP) lists, breached email repositories, and cybercrime marketplaces. At least 347 million were originally obtained by infostealers found on around 3.9 million infected machines.
18. arXiv papers leak sensitive data

    An analysis of 2.7 million submissions to the arXiv preprint service -- which also makes available the LaTeX sources and other files used to create them -- has found that they include unnecessary files, expose metadata embedded in files (usernames, email addresses, hardware details, GPS information, software versions), and leak irrelevant content in files such as source code comments. This includes backups, hidden .nfs files, Git repositories (including editing histories), andconfiguration files containing API keys. "Apart from unused template files that put unnecessary storage burden on arXiv, we further discovered scripts, research data, and even entire Git repositories. Additionally, comments in LaTeX sources reveal, e.g., author conversations or todo items – for some of those comments, we are certain that the authors did not intend to disclose them publicly. Alarmingly, our findings also include URLs without any access restrictions to other resources (e.g., Google Docs), security tokens, and private keys," the study
    [said](https://arxiv.org/abs/2604.20927)
    . While arXiv recommends Google's
    [arxiv\_latex\_cleaner](https://github.com/google-research/arxiv-latex-cleaner)
    to clean the LaTeX code, the researchers have released a tool called ALC-NG to comprehensively remove files, metadata, and comments that are not needed to compile a LaTeX paper.
19. Roblox account hacking ring busted

    The Ukrainian police have
    [arrested](http://gp.gov.ua/en/posts/na-lvivshhini-zatrimano-xakersku-grupu-yaka-zlamuvala-igrovi-akaunti-i-otrimala-maize-10-mln-grn-pributku-vid-yix-prodazu-v-rosiyu)
    three individuals who hacked more than 610,000 Roblox gaming accounts and sold them for a profit of $225,000 on Russian websites. The suspects face up to 15 years in prison if convicted and have been placed in pretrial detention while the investigation is in progress. The scheme was allegedly
    [masterminded](https://npu.gov.ua/news/prodaly-vykradeni-ihrovi-akaunty-na-10-mln-hrn-politseiski-lvivshchyny-zatrymaly-khakerske-uhrupovannia)
    by a 19-year-old resident of Drohobych, Lviv Oblast, who met his accomplices, aged 21 and 22, on gaming forums last year. From October 2025 to January 2026, the suspects are believed to have accessed more than 600,000 Roblox user accounts.
20. Iran-linked group targets troops

    The
    [Iran-linked](https://socradar.io/blog/handala-hack-us-doxxing-troop-bahrain/)
    threat actor
    [Handala Hack](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)
    has targeted U.S. troops in Bahrain in an influence campaign carried out via WhatsApp, according to
    [Stars and Stripes](https://www.stripes.com/theaters/middle_east/2026-04-28/handala-hack-iran-bahrain-navy-21510827.html)
    . The messages, signed Handala and containing a link to the group’s website, claimed the service members were under surveillance and soon to be targeted with drones and missiles. "Your identities are fully known to our missile units, and every move you make is under our surveillance. Very soon, you will be targeted by our Shahed drones and Kheibar and Ghadeer missiles," the message sent on April 28, 2026, read.
21. Record surge in privacy fines

    U.S. states issued $3.45 billion in privacy-related fines to companies in 2025, a total larger than the last five years combined, per Gartner. "Regulators are also shifting their efforts away from spreading awareness to full-scale enforcement," the company
    [said](https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-estimates-us-states-privacy-fines-totaled-3-point-425-billion-dollars-in-2025-trend-expected-to-accelerate-through-2028)
    . "This is increasingly becoming the standard in 2026 and beyond."
22. WordPress plugin backdoor uncovered

    Anchor Hosting has
    [revealed](https://anchor.host/wordpress-plugin-hijacked-in-2020-hid-a-dormant-backdoor-for-years/)
    that a WordPress plugin named
    [Quick Page/Post Redirect](https://wordpress.org/plugins/quick-pagepost-redirect-plugin/)
    plugin, which has over 70,000 installs, was compromised with a backdoor that enables injecting arbitrary code into users' sites. Plugin versions 5.2.1 and 5.2.2, released between 2020 and 2021, have been found to include a covert self-update mechanism that reaches out to a third-party domain, anadnet[.]com, to facilitate the execution of arbitrary code. It's worth noting that the passive backdoor triggers only for logged-out users to hide its activity from site administrators. As of April 16, the plugin has been closed temporarily pending a full review.
23. Qinglong flaws abused for mining

    Hackers are exploiting two authentication bypass vulnerabilities in
    [Qinglong](https://github.com/whyour/qinglong)
    , an open-source timed task management platform with over 19,500 GitHub stars, to deploy cryptocurrency miners. The two flaws –
    [CVE-2026-3965](https://nvd.nist.gov/vuln/detail/CVE-2026-3965)
    and
    [CVE-2026-4047](https://nvd.nist.gov/vuln/detail/CVE-2026-4047)
    – enable authentication bypass that results in remote code execution. "While these vulnerabilities were formally reported on February 27, exploitation had already been underway for weeks," Snyk
    [said](https://snyk.io/blog/qinglong-task-scheduler-rce-vulnerabilities/)
    . "Starting around February 7-8, 2026, Qinglong users began
    [opening issues](https://github.com/whyour/qinglong/issues/2923)
    about a hidden process called .fullgc consuming 85-100% of their CPU. The .fullgc filename may have been chosen to blend in with legitimate processes. In Java/JVM environments, 'Full GC' (Full Garbage Collection) is a known source of CPU spikes, which could delay an administrator's investigation." The issues have since been addressed in
    [#PR 2941](https://github.com/whyour/qinglong/pull/2941)
    .
24. Trivy hack enabled repo breach

    In a new update shared this week, Checkmarx
    [said](https://checkmarx.com/blog/supply-chain-security-incident-update/)
    its investigation into the cybersecurity incident has revealed the TeamPCP attack affecting the Trivy scanner is the "likely vector that enabled the attackers to obtain credentials and to gain unauthorized access to our GitHub repositories." This, in turn, allowed the attackers to interact with Checkmarx's GitHub environment and publish malicious code to certain artifacts. The development comes as the company
    [acknowledged](https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html)
    that data stolen from the GitHub repository was published on the dark web by a cybercrime group known as LAPSUS$.
25. npm stealer tied to DPRK group

    The North Korean threat actor known as
    [Famous Chollima](https://thehackernews.com/2026/04/new-wave-of-dprk-attacks-uses-ai.html)
    has been attributed to the npm package named js-logger-pack that comes embedded with a WebSocket stealer that's triggered via a postinstall hook. "The payload is a long-running WebSocket agent that: installs the attacker's RSA key into ~/.ssh/authorized\_keys on Linux; exfiltrates Telegram Desktop tdata sessions; drains credentials from 27 crypto wallets and Chromium-family browsers; steals .npmrc, cloud provider tokens, and shell history; and runs a native keylogger on Windows, macOS, and Linux with autostart persistence on all three," SafeDep
    [said](https://safedep.io/malicious-js-logger-pack-npm-stealer/)
    .

Security is a team sport. We keep seeing the same gaps because we focus on the new shiny toys while the basics, like simple passwords and old software versions, fall through the cracks. It is clear that just having a patch isn't enough if nobody actually installs it.

The best lesson here is to stay curious and cautious. Whether it is a weird text from a "trusted" source or a new tool that seems too good to be true, taking a second to verify can save a lot of trouble later. Let's keep learning and stay sharp until the next update!