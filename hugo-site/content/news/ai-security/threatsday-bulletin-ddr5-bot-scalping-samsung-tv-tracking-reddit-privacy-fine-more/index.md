---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-06T00:15:15.152610+00:00'
exported_at: '2026-03-06T00:15:18.617503+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/threatsday-bulletin-redis-rce-ddr5-bot.html
structured_data:
  about: []
  author: ''
  description: Latest cybersecurity threats, malware campaigns, research findings,
    and key security developments from this week’s ThreatsDay Bulletin.
  headline: 'ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy
    Fine & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/threatsday-bulletin-redis-rce-ddr5-bot.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: DDR5 Bot Scalping, Samsung TV Tracking, Reddit Privacy
  Fine & More'
updated_at: '2026-03-06T00:15:15.152610+00:00'
url_hash: 981fdc37bede06fe19512310b44b5429aaecc4a5
---

**

Ravie Lakshmanan
**

Mar 05, 2026

Cybersecurity / Hacking News

Some weeks in cybersecurity feel routine. This one doesn’t.

Several new developments surfaced over the past few days, showing how quickly the threat landscape keeps shifting. Researchers uncovered fresh activity, security teams shared new findings, and a few unexpected moves from major tech companies also drew attention.

Together, these updates offer a useful snapshot of what is happening behind the scenes in the cyber world right now. From new tactics and campaigns to security and policy changes that could affect millions of users, there is a lot unfolding at once.

Below is a quick roundup of the most notable stories making headlines this week.

1. Phishing Campaign Deploys Multiple Malware Strains

   The Computer Emergency Response Team of Ukraine (CERT-UA) has
   [warned](https://cert.gov.ua/article/6287707)
   of a hacking campaign targeting Ukrainian government institutions using phishing emails containing a ZIP archive (or a link to a website vulnerable to cross-site scripting attacks) to distribute SHADOWSNIFF and SALATSTEALER information-stealing malware and a Go backdoor called DEAFTICKK. The agency attributed the activity to a threat actor tracked as UAC-0252. The development comes as a suspected Russian espionage campaign is targeting Ukraine with two previously undocumented malware strains,
   [BadPaw and MeowMeow](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html)
   , according to ClearSky. While the campaign is likely said to be the work of APT28, the cybersecurity company did not identify the targets of the campaign or say whether the attacks were successful.
2. Fake RMM Service Spreads RAT via Phishing

   A new malware-as-a-service (MaaS) dubbed TrustConnect ("trustconnectsoftware[.]com") masqueraded as a legitimate remote monitoring and management (RMM) tool for $300 per month. It's assessed that the threat actor behind TrustConnect was also a prominent user of
   [RedLine Stealer](https://thehackernews.com/2024/04/new-redline-stealer-variant-disguised.html)
   . According to email security firm
   [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/dont-trustconnect-its-a-rat)
   , multiple threat actors have been observed distributing the malware via phishing emails as of January 27, 2026. The emails claim to be event invites or bid proposals, tricking recipients into clicking on links that lead to the download of bogus executables that install TrustConnect RAT. The RAT backdoors users' machines and gives attackers full mouse and keyboard control, allowing them to record and stream the victim's screen. Some campaigns have also been observed delivering legitimate remote access software like ScreenConnect and LogMeIn Resolve alongside TrustConnect between January 31 and February 3, 2026. Customers who purchase the toolkit are granted access to a dashboard to remotely commandeer infected devices and generate branded installers containing the malware. After Proofpoint took steps to disrupt some of the malware's infrastructure on February 17, 2026, the threat actor resurfaced with a rebranded version of the malware platform called DocConnect. "Disruptions to MaaS operations like RedLine, Lumma Stealer, and Rhadamanthys have created new opportunities for malware creators to fill gaps in the cybercrime market," Proofpoint said. "Although TrustConnect only masqueraded as a legitimate RMM, the lures, attack chains, and follow-on payloads (which include RMMs) show overlap with techniques and delivery methods that are frequently observed in RMM campaigns and used by multiple threat actors." The development comes amid skyrocketing abuse of legitimate RMM software in cyber attacks.
3. Chrome Moves to Two-Week Release Cycle

   Google has announced that new Chrome iterations will be released every two weeks, moving away from the current four-week release cycle. Since 2021, Google has been shipping major Chrome versions every four weeks, and since 2023, it has been delivering security updates every week for a reduced patch gap and improved quality. "The web platform is constantly advancing, and our goal is to ensure developers and users have immediate access to the latest performance improvements, fixes, and new capabilities," Google
   [said](https://developer.chrome.com/blog/chrome-two-week-release)
   . The new release cycle will also apply to beta releases, starting with Chrome 153, which will arrive on September 8, 2026.
4. TPMS Signals Allow Covert Vehicle Tracking

   Researchers at IMDEA Networks Institute have found that Tire Pressure Monitoring System (TPMS) sensors inside each car wheel broadcast unencrypted wireless signals containing persistent identifiers. While the feature is designed for vehicle safety, each sensor transmits a unique ID that does not change, allowing the same car to be recognized again and tracked over time. This, in turn, opens the door to a low-cost monitoring network that uses software-defined radio receivers near roads (at a distance of up to 40m from the car) and parking areas to collect TPMS messages from thousands of vehicles and build profiles of their movements over time. "Malicious users could deploy passive receivers on large scales and track citizens without their knowledge. The advantage of such a system, over more traditional camera-based ones, is that no direct line-of-sight is needed with the TPMS sensors, and spectrum receivers could be placed in covert or hidden locations, making them harder to spot by victims," the researchers
   [warned](https://dspace.networks.imdea.org/handle/20.500.12761/2011)
   . "Our results show that TPMS transmissions can be used to systematically infer potentially sensitive information such as the presence, type, weight, or driving pattern of the driver." The disclosure adds to a growing body of research demonstrating how various components fitted into modern vehicles can become unintended conduits for surveillance and exploits.
5. Telegram Emerges as Cybercrime Command Hub

   A new analysis from CYFIRMA has pointed out how Telegram's structure offers threat actors a way to extend their reach globally without the need for specialized tooling, enable frictionless onboarding of buyers and affiliates, support payment options, and facilitate audience growth. The emergence of the platform has fundamentally changed the way cyber operations are coordinated, monetized, and publicized. "For financially motivated actors, Telegram functions as a scalable storefront and customer support hub," the company
   [said](https://www.cyfirma.com/research/telegram-as-the-new-operational-layer-of-cyber-threat-activity/)
   . "For hacktivists, it serves as a mobilization and propaganda amplifier. For state-aligned operations, it offers a rapid distribution channel for narratives and leaks. In many cases, telegram complements and increasingly replaces traditional Tor-based ecosystems by removing technical friction while maintaining operational flexibility."
6. AuraStealer Infrastructure Revealed

   A new analysis of
   [AuraStealer](https://thehackernews.com/2025/12/weekly-recap-firewall-exploits-ai-data.html#:~:text=AuraStealer%20Spotted%20in%20the%20Wild)
   from Intrinsec has
   [uncovered](https://www.intrinsec.com/analysis-of-aurastealer-an-emerging-infostealer/)
   48 command-and-control (C2) domain names linked to the stealer's operations. The threat actor behind the malware has been found to use .shop and .cfd top-level domains, in addition to routing all traffic through Cloudflare as a reverse proxy to conceal the real server. AuraStealer first appeared on underground hacker forums in July 2025, shortly after the disruption of the Lumma Stealer as part of a law enforcement operation. It was advertised by a user named AuraCorp on the XSS forum. It comes in two subscription packages: $295/month for Basic and $585/month for Advanced. One of the primary mechanisms through which the stealer is distributed is
   [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
   .
7. Malvertising Pushes New Atomic Stealer Variant

   A malvertising campaign is using bogus ads on Google Search results pages to redirect users looking for ways to free up macOS storage to fraudulent web pages hosted on Medium, Evernote, and Kimi AI to serve
   [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
   -style instructions that drop a new variant of the Atomic Stealer called malext to steal a wide range of data from compromised macOS systems. The campaign uses more than 50 compromised Google Ads accounts that push "over 485 malicious landing pages, ultimately leading to a ClickFix attack that deployed a potentially new version of AMOS Stealer onto infected systems," security researcher Gi7w0rm
   [said](https://gi7w0rm.medium.com/amos-stealer-malext-variant-spread-in-a-global-malvertising-campaign-using-free-text-sharing-4d240e11d7e2)
   .
8. Bots Hammer DRAM Pages for DDR5 Inventory

   A large-scale data gathering operation has submitted more than 10 million web scraping requests to hit DRAM product pages on e-commerce sites in an effort to find sellers carrying desirable DRAM stock. The bots have been found to check the stock of specific RAM kits every 6.5 seconds by using a technique called cache busting to ensure they get the most up-to-date information, DataDome said. "These bots aggressively target the entire supply chain, from consumer RAM to B2B industrial memory providers and raw hardware components like DIMM sockets," the company
   [said](https://datadome.co/threat-research/scarcity-ddr5-ram-fueled-by-ai-demand-scalping-surge/)
   . "Scrapers attempt to avoid detection by adding
   [cache-busting parameters](https://www.keycdn.com/support/what-is-cache-busting)
   to every request and calibrating their speed to stay just below volumetric alarm thresholds. By rapidly snapping up the limited DDR5 memory inventory for profitable resale, these bots further deplete the consumer supply, effectively boxing out legitimate customers and driving market prices even higher."
9. Reddit Fined Over Children's Data Handling

   The U.K. Information Commissioner's Office (ICO) has
   [fined](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/reddit-issued-with-1447m-fine-for-children-s-privacy-failures/)
   Reddit £14.47 million for unlawfully processing the personal information of children under the age of 13 and for failing to properly check the age of its users, thereby putting them at risk of being exposed to inappropriate and harmful content online. In July 2025, Reddit introduced age assurance measures that include age verification to access mature content and asking users to declare their age when opening an account. Reddit
   [said](https://arstechnica.com/tech-policy/2026/02/uk-fines-reddit-for-not-checking-user-ages-aggressively-enough/)
   it would appeal the decision, stating it doesn't require users to share information about their identities, regardless of age, to ensure users' online privacy and safety.
10. Samsung Restricts TV Data Collection in Texas

    Texas Attorney General Ken Paxton announced that Samsung will no longer collect Automated Content Recognition (
    [ACR](https://en.wikipedia.org/wiki/Automatic_content_recognition)
    ) data without consumers' express consent. The development comes in the wake of a lawsuit filed against the South Korean electronics giant for its data collection practices and over allegations that the collected ACR information could be used to serve targeted ads. "Additionally, it compels Samsung to promptly update its smart TVs and implement disclosures and consent screens that are clear and conspicuous to ensure that Texans can make an informed decision regarding whether their data is collected and how it's used," the Office of the Attorney General
    [said](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs)
    . Samsung has denied it spies on users.
11. NATO Clears Consumer iPhones and iPads

    Apple iPhones and iPads have been
    [approved](https://www.apple.com/newsroom/2026/02/iphone-and-ipad-approved-to-handle-classified-nato-information/)
    to handle classified information in NATO networks. They are the first consumer-grade devices to be approved for NATO use without additional special software or settings. iPhone and iPad previously received approval to handle classified German government data on devices using native iOS and iPadOS security measures following a security evaluation conducted by Germany's Federal Office for Information Security.
12. TikTok Rejects End-to-End Encryption for DMs

    ByteDance's TikTok said it has no plans to add end-to-end encryption (E2EE) to direct messages because it would prevent law enforcement and safety teams from reading messages if necessary. In a statement shared with the BBC, the company
    [said](https://www.bbc.com/news/articles/cly2m5e5ke4o)
    it wanted to protect users, especially young people, from harm.
13. Multi-Stage Phishing Attack Spreads Agent Tesla

    A new phishing campaign using purchase order lures has leveraged a multi-stage attack chain to deliver
    [Agent Tesla](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html)
    , allowing threat actors to harvest sensitive data, while taking steps to evade detection using techniques like obfuscation and in-memory execution. "From the initial obfuscated JSE loader to the reflective loading of .NET assemblies and process hollowing of legitimate Windows utilities, Agent Tesla is designed to stay invisible," Fortinet FortiGuard Labs
    [said](https://www.fortinet.com/blog/threat-research/unmasking-agent-tesla-deep-dive-into-multi-stage-campaign)
    . "Its extensive anti-analysis checks further ensure that it only reveals its true nature when it’s certain it isn't being watched."
14. Attackers Abuse Infrastructure-Only .arpa Domain

    With organizations taking steps to tighten their traditional email and web filters, new research from Infoblox has
    [found](https://www.infoblox.com/blog/threat-intelligence/abusing-arpa-the-tld-that-isnt-supposed-to-host-anything/)
    a novel campaign where actors are abusing the .arpa top-level domain, a space strictly reserved for network infrastructure, to host malicious content and bypass standard blocklists. The development shows cybercriminals are finding "impossible" hiding spots within the internet’s core infrastructure to bypass security, the DNS threat intelligence firm said. Elsewhere, threat actors are also abusing LNK shortcut files and WebDAV to download malicious files on targets' systems. "Because being able to remotely access things on the internet via File Explorer is a relatively unknown functionality to most people, WebDAV is an exploitable way to make people download files without going through a traditional web browser file download," Cofense
    [said](https://cofense.com/blog/abusing-windows-file-explorer-and-webdav-for-malware-delivery)
    .
15. Spoofed Email Chains Target LastPass Users

    A new phishing campaign that commenced on March 1, 2026, is using lures related to unauthorized access to individuals' accounts to trick recipients into visiting fake LastPass login pages to take control of their accounts. The attack takes advantage of the fact that many email clients, especially mobile, show only the display name, hiding the real sender address unless users expand it. "Attackers are forwarding fake email chains to make it appear as though another individual is trying to take unauthorized action on their LastPass account (i.e., export vault, full account recovery, new trusted device registered, etc.)," LastPass
    [said](https://blog.lastpass.com/posts/march-2026-phishing-campaign-targeting-lastpass-customers)
    . "Attackers use display name spoofing so that the name portion of the sender field is manipulated to impersonate LastPass, while the actual sending email address is unrelated."
16. Experts Warn Against Blind Trust in AI Coding Agents

    With the emergence of tools like
    [Claude Code Security](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html)
    , OX Security is urging users to resist the temptation to outsource judgment, architecture, and validation to a single artificial intelligence (AI) model. "AI doesn't invent fundamentally new code patterns," it
    [said](https://www.ox.security/blog/the-claude-code-security-promise-why-this-cant-be-our-safety-net/)
    . "It reproduces the most common ones it has seen before. That means it scales not only productivity, but also existing weaknesses in software engineering practice." The cybersecurity company also warned that AI systems may be prone to false positives and may not reliably inform a user if an issue flagged in a single repository is actually exploitable in a complex and unique environment. A pipeline that relies on the same AI system for both writing and reviewing code is not ideal, it added.
17. LLMs Enable Automated Internet Deanonymization

    A team of academics from Anthropic, ETH Zurich, and
    [MATS Research](https://www.matsprogram.org/research/large-scale-online-deanonymization-with-llms)
    has developed large language models (LLMs) that can deanonymize internet users based on past comments or other digital clues they leave behind. "Given two databases of pseudonymous individuals, each containing unstructured text written by or about that individual, we implement a scalable attack pipeline that uses LLMs to: (1) extract identity-relevant features, (2) search for candidate matches via semantic embeddings, and (3) reason over top candidates to verify matches and reduce false positives," the researchers
    [said](https://arxiv.org/abs/2602.16800)
    . The method works even if targets use different pseudonyms across multiple platforms. The researchers said using their LLMs outperforms classical research methods, where digital footprints are examined manually by a human operator. This, in turn, enables fully automated deanonymization attacks that can work on unstructured data at scale, while also reducing the cost and effort that goes into intelligence gathering. "Our results show that the practical obscurity protecting pseudonymous users online no longer holds and that threat models for online privacy need to be reconsidered," the researchers said. "The average online user has long operated under an implicit threat model where they have assumed pseudonymity provides adequate protection because targeted deanonymization would require extensive effort. LLMs invalidate this assumption."

That wraps up this week’s quick look at what has been happening across the cybersecurity landscape.

Each update on its own may seem small, but together they show how quickly things continue to change. New techniques appear, old tactics evolve, and security decisions from major companies can shift the wider ecosystem.

For security teams, researchers, and anyone who follows the threat landscape, keeping track of these signals helps make sense of the bigger picture.

Stay tuned for the next edition of the ThreatsDay Bulletin with more developments from the cyber world.