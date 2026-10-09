---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-14T06:49:14.113931+00:00'
exported_at: '2025-11-14T06:49:16.339701+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/threatsday-bulletin-cisco-0-days-ai-bug.html
structured_data:
  about: []
  author: ''
  description: 'Global cyber roundup: new AI bug bounties, malware threats, GDPR backlash,
    Cisco zero-days, data leaks, and rising attacks on key infrastructure.'
  headline: 'ThreatsDay Bulletin: Cisco 0-Days, AI Bug Bounties, Crypto Heists, State-Linked
    Leaks and 20 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/threatsday-bulletin-cisco-0-days-ai-bug.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: Cisco 0-Days, AI Bug Bounties, Crypto Heists, State-Linked
  Leaks and 20 More Stories'
updated_at: '2025-11-14T06:49:14.113931+00:00'
url_hash: a9e6f099a886e6b326a7aa64c0ed3d7d3198e884
---

**

Nov 13, 2025
**

Ravie Lakshmanan

Cybersecurity / Hacking News

Behind every click, there's a risk waiting to be tested. A simple ad, email, or link can now hide something dangerous. Hackers are getting smarter, using new tools to sneak past filters and turn trusted systems against us.

But security teams are fighting back. They're building faster defenses, better ways to spot attacks, and stronger systems to keep people safe. It's a constant race — every move by attackers sparks a new response from defenders.

In this week's ThreatsDay Bulletin, we look at the latest moves in that race — from new malware and data leaks to AI tools, government actions, and major security updates shaping the digital world right now.

1. U.K. moves to tighten cyber rules for key sectors

   The U.K. government has proposed a new Cyber Security and Resilience Bill that aims to strengthen national security and secure public services like healthcare, drinking water providers, transport, and energy from cybercriminals and state-backed actors. Under the proposal, medium and large companies providing services like IT management, IT help desk support, and cybersecurity to private and public sector organisations like the National Health Service (NHS) will be regulated. Organizations covered by the new law would have to report more harmful cyber incidents to both their regulator and the National Cyber Security Centre (NCSC) within 24 hours, followed by a full report sent within 72 hours. Penalties for serious violations under the new rules will reach daily fines equivalent to £100,000 ($131,000), or 10% of the organization's daily turnover – whichever is higher. "Because they hold trusted access across government, critical national infrastructure and business networks, they will need to meet clear security duties," the government
   [said](https://www.gov.uk/government/news/tough-new-laws-to-strengthen-the-uks-defences-against-cyber-attacks-on-nhs-transport-and-energy)
   .
   "This includes reporting significant or potentially significant cyber incidents promptly to the government and their customers as well as having robust plans in place to deal with the consequences."
2. Intel's data breach drama unfolds

   A former Intel employee has been accused of downloading thousands of documents shortly after the company fired him in July, many of them classified as "Top Secret." The Oregonian, which
   [reported](https://www.oregonlive.com/silicon-forest/2025/11/intel-says-software-engineer-took-top-secret-documents-after-getting-fired.html)
   on the lawsuit, said Jinfeng Luo downloaded 18,000 files to a storage device. After failing to get in touch with Luo at his home in Seattle and at two other addresses associated with him, the chipmaker filed suit seeking at least $250,000 in damages.
3. New OWASP list exposes evolving web threats

   The Open Web Application Security Project (OWASP) has
   [released](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
   a revised version of its Top 10 list of critical risks to web applications, adding two new categories, including software supply chain failures and mishandling of exceptional conditions to the list. While the former relates to compromises occurring within or across the entire ecosystem of software dependencies, build systems, and distribution infrastructure, the latter focuses on "improper error handling, logical errors, failing open, and other related scenarios stemming from abnormal conditions that systems may encounter." Broken Access Control, Security Misconfiguration, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Software and Data Integrity Failures, and Logging & Alerting Failures take up the remaining eight spots.
4. Sensitive data spills from top AI firms

   A study of 50 leading AI companies has found that 65% had leaked verified secrets on GitHub, including API keys, tokens, and sensitive credentials. "Some of these leaks could have exposed organizational structures, training data, or even private models," Wiz researchers Shay Berkovich and Rami McCarthy
   [said](https://www.wiz.io/blog/forbes-ai-50-leaking-secrets)
   .
   "If you use a public Version Control System (VCS), deploy secret scanning now. This is your immediate, non-negotiable defense against easy exposure. Even companies with the smallest footprints can be exposed to secret leaks as we have just proved."
5. Fake Meta invites trick businesses worldwide

   A new large-scale phishing campaign is abusing Facebook's Business Suite and facebookmail.com features to send convincing fake notifications ("Meta Agency Partner Invitation" or "Account Verification Required") that appear to come directly from Meta. "This method makes their campaigns extremely convincing, bypasses many traditional security filters, and demonstrates how attackers are exploiting trust in well-known platforms," Check Point
   [said](https://blog.checkpoint.com/email-security/new-phishing-campaign-exploits-meta-business-suite-to-target-smbs-across-the-u-s-and-beyond/)
   .
   "While the volume of emails may suggest a spray-and-pray approach, the credibility of the sender domain makes these phishing attempts far more dangerous than ordinary spam." More than 40,000 phishing emails have been recorded to date, primarily targeting entities in the U.S., Europe, Canada, and Australia that rely heavily on Facebook for advertising. To pull off the scheme, the attackers create fake Facebook Business pages and use the Business invitation feature to send phishing emails that mimic official Facebook alerts. The fact that these messages are sent from the "facebookmail[.]com" domain means they are perceived as trustworthy by email security filters. Present within the emails are links that, when clicked, direct users to bogus websites that are designed to steal credentials and other sensitive information.
6. Firefox tightens shield against online tracking

   Mozilla has
   [added](https://blog.mozilla.org/en/firefox/fingerprinting-protections/)
   more fingerprint protections to its Firefox browser to prevent websites from identifying users without their consent, even when cookies are blocked or private browsing is enabled. The safeguards, starting with Firefox 145, aim to block access to certain pieces of information used by online fingerprinters. "This ranges from strengthening the font protections to preventing websites from getting to know your hardware details like the number of cores your processor has, the number of simultaneous fingers your touchscreen supports, and the dimensions of your dock or taskbar," Mozilla said. Specifically, the new protections
   [include](https://support.mozilla.org/en-US/kb/firefox-protection-against-fingerprinting)
   introducing random data to images generated in canvas elements, preventing locally installed fonts from being used to render text on a page, reporting the number of simultaneous touches supported by device hardware as 0, 1, or 5, reporting Available Screen Resolution as the screen height minus 48 pixels, and reporting the number of processor cores as either 4 or 8.
7. Phishing kit simplifies global Microsoft 365 theft

   A new phishing kit called Quantum Route Redirect is being wielded by threat actors to steal Microsoft 365 credentials. "Quantum Route Redirect comes with a pre-configured setup and phishing domains that significantly simplifies a once technically complex campaign flow, further 'democratizing' phishing for less skilled cybercriminals," KnowBe4 Threat Labs
   [said](https://blog.knowbe4.com/quantum-route-redirect-anonymous-tool-streamlining-global-phishing-attack)
   .
   The phishing campaigns impersonate legitimate services like DocuSign, or masquerade as payment notifications or missed voicemails to trick users into clicking on URLs that consistently follow the pattern "/([\w\d-]+\.){2}[\w]{,3}\/quantum.php/" and are hosted on parked or compromised domains. Nearly 1,000 such domains have been detected. The phishing kit also enables browser fingerprinting and VPN/proxy detection to redirect security tools to legitimate websites. Campaigns leveraging the kit have successfully claimed victims across 90 countries, with the U.S. accounting for 76% of affected users.
8. AI platform boosts defenses with Guardio tech

   AI coding platform Lovable has
   [partnered](https://guard.io/blog/lovable-integrates-guardio-to-ensure-safe-responsible-ai-development)
   with Guardio to embed its Safe Browsing detection engine into the platform's generative AI workflows, with an aim to scan every site created on the platform to detect phishing, scams, impersonation, and other forms of abuse. The development comes against the backdrop of reports that found AI-powered coding assistants like Lovable to be susceptible to techniques like
   [VibeScamming](https://thehackernews.com/2025/04/lovable-ai-found-most-vulnerable-to.html)
   ,
   allowing bad actors to set up lookalike credential harvesting pages and carry out scams.
9. Windows boosts passkey freedom for users

   Microsoft has officially launched native support for third-party passkey managers in Windows 11. The feature is available with the Windows November 2025 security update. "This new capability empowers users to choose their favorite passkey manager – whether it's Microsoft Password Manager or trusted third-party providers," Microsoft
   [said](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-11-expands-passkey-manager-support/4467572)
   .
   The company also noted it has integrated Microsoft Password Manager from Microsoft Edge into Windows as a plugin, thereby making it possible to use it in Microsoft Edge, other browsers, or any app that supports passkeys.
10. Hackers lay siege to construction industry

    Threat actors ranging from ransomware operators and organized cybercriminal networks to state-sponsored APT groups are increasingly targeting the construction industry by exploiting the sector's growing dependence on vulnerable IoT-enabled heavy machinery, Building Information Modeling (BIM) systems, and cloud-based project management platforms. "Cybercriminals increasingly target construction companies for initial access and data leaks, exploiting weak security practices, outdated legacy systems, and widespread use of cloud-based project management tools," Rapid7
    [said](https://www.rapid7.com/blog/post/tr-building-construction-sector-threat-landscape-initial-access-supply-chain-iot/)
    .
    "Attackers commonly employ phishing email messages, compromised credentials, and supply chain attacks, taking advantage of insufficient employee training and lax vendor risk management." Attackers are also shifting to procuring initial access to construction company networks through underground forums rather than conducting resource-intensive initial compromise operations themselves. These listings facilitate support for escrow services to provide buyers with assurances about the validity of purchased data. Once breached, the threat actors move swiftly across the network to exfiltrate valuable data and even extort it through ransomware.
11. Google backs down, keeps sideloading alive

    Back in August, Google
    [announced](https://thehackernews.com/2025/08/google-to-verify-all-android-developers.html)
    plans to verify the identity of all developers who distribute apps on Android, even for those who distribute their software outside the Play Store. The move was
    [met with backlash](https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html)
    ,
    raising concerns that it could be the end of sideloading in Android. While Google has claimed the intention behind the change was to tackle online scams and malware campaigns, particularly those that occur when users download APK files distributed via third-party marketplaces, F-Droid painted the framing as disingenuous, given that there already exists Google Play Protect as a remediation mechanism. "Any perceived risks associated with direct app installation can be mitigated through user education, open-source transparency, and existing security measures without imposing exclusionary registration requirements," F-Droid
    [said](https://f-droid.org/en/2025/10/28/sideloading.html)
    .
    In response to feedback from "developers and power users," Google
    [said](https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html)
    it's "building a new advanced flow that allows experienced users to accept the risks of installing software that isn't verified." More details are expected to be shared in the coming months.
12. CISA warns of false Cisco patch security

    The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has
    [issued](https://www.cisa.gov/news-events/alerts/2025/11/12/update-implementation-guidance-emergency-directive-cisco-asa-and-firepower-device-vulnerabilities)
    a
    [new alert](https://www.cisa.gov/ed-25-03-guidance-device-updates-and-patching)
    ,
    stating it has identified devices marked as "patched" as part of Emergency Directive 25-03, but which were "updated to a version of the software that is still vulnerable to the threat activity" that involves the exploitation of
    [CVE-2025-20333 and CVE-2025-20362](https://thehackernews.com/2025/09/urgent-cisco-asa-zero-day-duo-under.html)
    .
    "CISA is aware of multiple organizations that believed they had applied the necessary updates but had not in fact updated to the minimum software version," the agency said. "CISA recommends all organizations verify the correct updates are applied." Both vulnerabilities have come under active exploitation by a suspected China-linked hacking group known as
    [UAT4356](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.html)
    (aka Storm-1849).
13. Russia tests new SIM-based drone defense

    Russia's Digital Development Ministry has
    [disclosed](https://t.me/mintsifry/2676)
    that telecom operators in the country have launched a new mechanism to combat drones at the request of regulators. "If a SIM card is brought into Russia from abroad, it must be confirmed that it is used by a person and not embedded in a drone," the ministry said in a post on Telegram. "Until then, mobile internet and SMS services on this SIM card will be temporarily blocked." The mechanism is being tested as of November 10, 2025. The ministry also noted that subscribers with Russian SIM cards are eligible for a 24-hour cooling-off period if the SIM has been inactive for 72 hours or upon returning from international travel. Subscribers can restore access by solving a CAPTCHA provided by the carrier or calling their service provider and verifying their identity over the phone. The development comes a month after Moscow imposed a similar 24-hour blackout for people entering Russia with foreign SIM cards, citing similar reasons.
14. Citrix patches exploitable XSS bug in NetScaler

    Cybersecurity company watchTowr Labs has published details about a newly patched
    [reflected cross-site scripting](https://www.imperva.com/learn/application-security/reflected-xss-attacks/)
    (XSS) flaw (CVE-2025-12101, CVSS score: 6.1) in NetScaler ADC and NetScaler Gateway when the appliance is configured as a Gateway (VPN virtual server, ICA Proxy, CVPN, RDP Proxy) or Authentication, Authorization, and Auditing (AAA) virtual server. The
    [vulnerability](https://docs.netscaler.com/en-us/netscaler-console-service/instance-advisory/remediate-vulnerabilities-cve-2025-12101.html)
    was patched by Citrix
    [earlier this week](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695486)
    .
    Sina Kheirkhah of watchTowr said the vulnerability stems from the application's handling of the RelayState parameter, allowing an attacker to execute an arbitrary XSS payload by means of a specially crafted HTTPS request containing a RelayState parameter with a Base64-encoded value. "While this may not look realistic as a usable vulnerability (and we'd agree given the low hanging fruit elsewhere), it is broadly still usable via CSRF - as the NetScaler's /cgi/logout endpoint accepts an HTTP POST request containing a valid SAMLResponse and a modified RelayState," Kheirkhah
    [said](https://labs.watchtowr.com/is-it-citrixbleed4-well-no-is-it-good-also-no-citrix-netscalers-memory-leak-rxss-cve-2025-12101/)
    .

    [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf4MxQE8nv0ruWgtlWDBqNIGWeF4shoNwhWtpG7UC8dC_FnVDaJLbOH0oaBSol2QnizZH_P8L-ztoOW9H4xjhaMQa26Qi1J9NNHurTTT0DEbUx5RG3cSFHw56odfuXQfgp3NQgxGZe11d1nVnpROGxB7LWC07EtzkqHFBIdMEMiOgvdH4hnNOuDPr7H1ce/s2600/net.png)
15. Cloud apps emerge as top malware carriers

    A new report from Netskope has found that approximately 22 out of every 10,000 users in the manufacturing sector encounter malicious content every month. "Microsoft OneDrive is now the most commonly exploited platform, with 18% of organizations reporting malware downloads from the service each month," the cybersecurity company
    [said](https://www.netskope.com/resources/threat-labs-reports/threat-labs-report-manufacturing-2025#recommendations)
    .
    GitHub came in second at 14%, followed by Google Drive (11%) and SharePoint (5.3%). To counter the risk, organizations are advised to inspect all HTTP and HTTPS downloads, including all web and cloud traffic, to prevent malware from infiltrating the enterprise network.
16. Malvertising crew reroutes paychecks nationwide

    A financially motivated threat actor known as
    [Payroll Pirates](https://thehackernews.com/2025/10/microsoft-warns-of-payroll-pirates.html)
    (aka Storm-2657) has been observed hijacking payroll systems, credit unions, and trading platforms across the U.S. by orchestrating malvertising campaigns. The malicious activity, described as persistent and adaptive, dates back to May 2023, when the threat actors set up phishing sites that impersonated payroll platforms. These sites were promoted via Google Ads, tricking employees into logging into fake HR portals with the goal of stealing their credentials. Once the login details were captured, the attackers rerouted salaries to their own accounts. Subsequent iterations came equipped with capabilities to bypass two-factor authentication (2FA). Check Point, which has been tracking a recent surge in these campaigns, said it found a single Telegram bot that's used to capture the 2FA codes in real-time across credit unions, payroll, health care benefits, and trading platforms, suggesting a "unified network." While one set of attacks has been found to rely on cloaking techniques to ensure that only intended victims are redirected to the phishing sites, a second cluster targets financial institutions using Microsoft Ads. "Domains are aged for months and host dozens of phishing pages with randomized URLs," Check Point
    [said](https://blog.checkpoint.com/email-security/payroll-pirates-one-network-hundreds-of-targets)
    .
    "A cloaking service from adspect.ai determines which page to show based on browser fingerprinting. Both clusters use the same phishing kits. Pages adapt dynamically based on operator feedback, making it easy to bypass most authentication methods."

    [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm75bNNXLJkou4Qlvp9Z6YepNL5CeGyliXnsCuK9ZXtGt-fHenTbzLmup3YFPECNOx_JRDGM_J5u3225E0bSGv7IzxZkyTpajtNZN_DocTSRcNKCD8sPiw_PmWigo30YfrCTOwrMVb3X7gKnYM3c3gPMVeb6Uk_loTarqzRsCU4FDe9sub4OLN4vQzGG1H/s2800/check.png)
17. Infamous banking trojan resurfaces stronger

    The
    [DanaBot](https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html)
    malware has returned with a new version 669, nearly six months after law enforcement's Operation Endgame disrupted its activity in May. The new variant has a command-and-control (C2) infrastructure that comprises Tor domains and BackConnect nodes, per
    [Zscaler](https://x.com/Threatlabz/status/1987965385036230779)
    .
    It's also using four different wallet addresses to steal cryptocurrency: 12eTGpL8EqYowAfw7DdqmeiZ87R922wt5L (BTC), 0xb49a8bad358c0adb639f43c035b8c06777487dd7 (ETH), LedxKBWF4MiM3x9F7zmCdaxnnu8A8SUohZ (LTC), and TY4iNhGut31cMbE3M6TU5CoCXvFJ5nP59i (TRX).
18. New Android RAT enters black market for $500

    A new Android remote access trojan (RAT) called KomeX RAT is being
    [advertised](https://x.com/KrakenLabs_Team/status/1988162776473170216)
    for sale on cybercrime forums for a monthly price of $500 or $1,200 for a lifetime license. Potential buyers can also obtain access to the entire codebase for $3,000. According to claims made by the seller, the Trojan is based on
    [BTMOB](https://cyble.com/blog/btmob-rat-newly-discovered-android-malware/)
    ,
    another Android remote control tool that emerged earlier this year as an evolution of SpySolr. Other features include the ability to acquire all necessary permissions, bypass Google Play Protect, log keystrokes, harvest SMS messages, and more. The threat actor also claims the RAT works worldwide without any geographic restrictions. Interestingly, a
    [Facebook page for SpySolr](https://www.facebook.com/spysolr/)
    states that the malware is developed by
    [EVLF](https://thehackernews.com/2023/08/syrian-threat-actor-evlf-unmasked-as.html)
    ,
    which was unmasked in 2023 as a Syrian threat actor behind CypherRAT and CraxsRAT.
19. Amazon opens its AI models to ethical hackers

    Amazon has become the latest company to open its large language models to outside security researchers by instituting a bug bounty program to identify security issues in
    [NOVA](https://nova.amazon.com)
    ,
    the company's suite of foundational AI models. "Through this program, researchers will test the Nova models across critical areas, including cybersecurity issues and Chemical, Biological, Radiological, and Nuclear (CBRN) threat detection," the tech giant
    [said](https://www.amazon.science/news/amazon-launches-private-ai-bug-bounty-to-strengthen-nova-models)
    .
    "Qualified participants can earn monetary rewards, ranging from $200 to $25,000."
20. Privacy groups slam EU's proposed GDPR rewrite

    Austrian privacy non-profit None of Your Business (noyb) has condemned the European Commission's
    [leaked plans](https://www.mlex.com/mlex/articles/2407305/eu-commission-eyes-codifying-legitimate-interest-as-legal-basis-for-ai-training)
    to overhaul the bloc's landmark privacy regulation, referred to as the General Data Protection Regulation (GDPR), including likely allowing AI companies to use personal data of citizens in the region for model training. "In addition, the special protection of sensitive data like health data, political views or sexual orientation would be significantly reduced," noyb
    [said](https://noyb.eu/en/eu-commission-about-wreck-core-principles-gdpr)
    .
    "Also, remote access to personal data on PCs or smartphones without the consent of the user would be enabled." Max Schrems, founder of noyb, said the draft represents a massive downgrade of user privacy, while mainly benefiting Big Tech. The Commission is planning to introduce the amendments on November 19.
21. Bitcoin Queen jailed in record $5.6B fraud case

    A U.K. court has
    [sentenced](https://news.met.police.uk/news/man-and-woman-jailed-for-their-roles-in-multibillion-pound-fraudulent-bitcoin-scheme-503184)
    a 47-year-old Chinese woman,
    [Zhimin Qian](https://www.bbc.com/news/articles/cvg4w1g9ezko)
    (aka Yadi Zhang), to 11 years and 8 months in prison for laundering bitcoin linked to a $5.6 billion investment scheme. Until her arrest in April 2024, the defendant had been on the run since 2017 after carrying out a large-scale scam in China between 2014 and 2017, which defrauded more than 128,000 people. Qian, nicknamed Bitcoin Queen, entered Europe using fake passports and settled in Britain under a fake name — Yadi Zhang. She
    [pleaded guilty](https://thehackernews.com/2025/09/uk-police-just-seized-55-billion-in.html)
    to offenses related to acquiring and possessing criminal property (i.e., cryptocurrency) back in September. The investigation also led to the seizure of 61,000 bitcoin, now valued at over $6 billion, making it the largest cryptocurrency seizure in history.
22. New malware duo drains crypto and spies on browsers

    Cybersecurity researchers have discovered two new second-stage malware families called LeakyInjector and LeakyStealer that are designed to target cryptocurrency wallets and browser history. "LeakyInjector uses low-level APIs for injection to avoid detection and injects LeakyStealer in 'explorer.exe,'" Hybrid Analysis
    [said](https://hybrid-analysis.blogspot.com/2025/11/leakyinjector-and-leakystealer-duo.html)
    .
    "The duo performs reconnaissance on an infected machine and targets multiple crypto wallets, including browser extensions corresponding to crypto wallets. The malware also looks for browser history files from Google Chrome, Microsoft Edge, Brave, Opera, and Vivaldi." LeakyStealer implements a polymorphic engine that modifies memory bytes using specific hard-coded values at runtime. It also beacons to an external server at regular intervals to execute Windows commands and download and run additional payloads.
23. Experts warn against self-policing AI safety tools

    Last month, OpenAI released a set of safety tools called
    [Guardrails safety framework](https://github.com/openai/openai-guardrails-python)
    to detect and block potentially harmful model behavior, such as jailbreaks and prompt injections. This includes detectors that rely on large language models (LLMs) to determine whether an input or output poses a security risk. AI security company HiddenLayer said this approach is fundamentally flawed, as it can be exploited by an attacker to the Guardrails framework. "If the same type of model used to generate responses is also used to evaluate safety, both can be compromised in the same way," it
    [said](https://hiddenlayer.com/innovation-hub/same-model-different-hat/)
    .
    "This experiment highlights a critical challenge in AI security: self-regulation by LLMs cannot fully defend against adversarial manipulation. Effective safeguards require independent validation layers, red teaming, and adversarial testing to identify vulnerabilities before they can be exploited."
24. Massive leak exposes Chinese cyber arsenal

    A
    [data breach](https://mrxn.net/news/Knownsec-data-leak.html)
    at a Chinese security vendor called Knownsec has led to the leak of over 12,000 classified documents, per Chinese security blog MXRN, "including information on Chinese state-owned cyber weapons, internal tools, and global target lists." The trove is also said to have apparently included evidence of RATs that can break into Linux, Windows, macOS, iOS, and Android devices, as well as details about the company's contracts with the Chinese government. The Android code can reportedly extract information from popular Chinese messaging apps and from Telegram. Also present in the leak data was a spreadsheet listing 80 overseas targets Knownsec has successfully attacked, plus 95GB of immigration data obtained from India, 3TB of call records stolen from South Korean telecom operator LG U-Plus, 459GB of road planning data obtained from Taiwan, passwords for Taiwanese Yahoo accounts, and data on Brazilian LinkedIn accounts. It's currently not known who is behind the leaks. There are indications that the leak is from an old data breach of Knownsec from 2023, per
    [NetAskari](https://netaskari.substack.com/p/knownsec-breach-what-we-know-so-far)
    .

The cyber world never slows down. Every fix, every patch, every new idea brings a new risk waiting to be found. Staying alert isn't just a choice anymore — it's a habit we all need to build.

The good news is that defenders are learning faster than ever. Researchers, companies, and governments are sharing more knowledge, closing more gaps, and helping each other face threats head-on. Progress may be slow, but it's steady.

As we wrap up this week's ThreatsDay Bulletin, remember — awareness is the first line of defense. Stay curious, stay updated, and stay safe until next time.