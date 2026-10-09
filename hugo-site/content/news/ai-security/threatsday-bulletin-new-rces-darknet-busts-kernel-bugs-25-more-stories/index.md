---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T14:15:14.017188+00:00'
exported_at: '2026-01-29T14:15:17.278562+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html
structured_data:
  about: []
  author: ''
  description: Weekly ThreatsDay Bulletin with concise updates on cyber attacks, exploits,
    scams, arrests, and emerging security risks.
  headline: 'ThreatsDay Bulletin: New RCEs, Darknet Busts, Kernel Bugs & 25+ More
    Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: New RCEs, Darknet Busts, Kernel Bugs & 25+ More Stories'
updated_at: '2026-01-29T14:15:14.017188+00:00'
url_hash: 20b96e182e09f258fce4510a00f8b917a9fc9124
---

**

Ravie Lakshmanan
**

Jan 29, 2026

Cybersecurity / Hacking News

This week's updates show how small changes can create real problems. Not loud incidents, but quiet shifts that are easy to miss until they add up. The kind that affects systems people rely on every day.

Many of the stories point to the same trend: familiar tools being used in unexpected ways. Security controls are being worked on. Trusted platforms turning into weak spots. What looks routine on the surface often isn't.

There's no single theme driving everything — just steady pressure across many fronts. Access, data, money, and trust are all being tested at once, often without clear warning signs.

This edition pulls together those signals in short form, so you can see what's changing before it becomes harder to ignore.

1. Major cybercrime forum takedown

   The U.S. Federal Bureau of Investigation (FBI) has seized the notorious RAMP cybercrime forum. Visitors to the forum's Tor site and its clearnet domain, ramp4u[.]io, are now greeted by a seizure banner that states the "action has been taken in coordination with the United States Attorney's Office for the Southern District of Florida and the Computer Crime and Intellectual Property Section of the Department of Justice." On the XSS forum, RAMP's current administrator Stallman confirmed the takedown,
   [stating](https://x.com/DarkWebInformer/status/2016545523608539381)
   , "This event has destroyed years of my work to create the most free forum in the world, and although I hoped that this day would never come, in my heart I always knew it was possible." RAMP was
   [launched](https://www.rapid7.com/blog/post/2024/08/20/selling-ransomware-breaches-4-trends-spotted-on-the-ramp-forum/)
   in July 2021 after both Exploit and XSS banned the promotion of ransomware operations. It was established by a user named
   [Orange](https://thehackernews.com/2023/05/us-offers-10-million-bounty-for-capture.html)
   , who has since been outed as
   [Mikhail Pavlovich Matveev](https://therecord.media/an-interview-with-initial-access-broker-wazawaka-there-is-no-such-money-anywhere-as-there-is-in-ransomware)
   (aka Wazawaka, m1x, Boriselcin, and Uhodiransomwar). "Groups such as Nova and DragonForce are reportedly shifting activity toward Rehub, illustrating the underground's ability to reconstitute quickly in alternative spaces," Tammy Harper, senior threat intelligence researcher at Flare.io, said. "These transitions are often chaotic, opening new risks for threat actors: loss of reputation, escrow instability, operational exposure, and infiltration during the scramble to rebuild trust."
2. WhatsApp privacy claims challenged

   A new lawsuit filed against Meta in the U.S. has alleged the social media giant has made false claims about the privacy and security of WhatsApp. The lawsuit claims Meta and WhatsApp "store, analyze, and can access virtually all of WhatsApp users' purportedly 'private' communications" and accuse the company of defrauding WhatsApp's users. In a statement shared with Bloomberg, Meta
   [called](https://www.bloomberg.com/news/articles/2026-01-25/lawsuit-claims-meta-can-see-whatsapp-chats-in-breach-of-privacy)
   the lawsuit frivolous and said that the company "will pursue sanctions against plaintiffs' counsel." Will Cathcart, head of WhatsApp at Meta,
   [said](https://x.com/wcathcart/status/2016003768694014092)
   , "WhatsApp can't read messages because the encryption keys are stored on your phone, and we don't have access to them. This is a no-merit, headline-seeking lawsuit brought by the very same firm defending NSO after their spyware attacked journalists and government officials." Complainants claim that WhatsApp has an internal team with unlimited access to encrypted communications, which can grant access to data requests. These requests are sent to the Meta engineering team, which then grants access to a user's messages, often without scrutiny, as the lawsuit laid out. These allegations go beyond scenarios where up to five recent messages are sent to WhatsApp for review when a user reports another user in an individual or group chat. The crux of the debate is whether WhatsApp's security is a technical lock that can't be picked, or a policy lock that employees can open. WhatsApp has
   [stressed](https://x.com/WhatsApp/status/2016227173749739875)
   that the messages are private and that "any claims to the contrary are false."
3. Post-quantum shift accelerates

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has
   [published](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards)
   an initial list of hardware and software product categories that support or are expected to support post-quantum cryptography (PQC) standards. The guidance covers cloud services, collaboration and web software, endpoint security, and networking hardware and software. The list aims to guide organizations in shaping their PQC migration strategies and evaluating future technological investments. "The advent of quantum computing poses a real and urgent threat to the confidentiality, integrity, and accessibility of sensitive data — especially systems that rely on public-key cryptography,"
   [said](https://www.cisa.gov/news-events/news/cisa-releases-product-categories-list-propel-post-quantum-cryptography-adoption-pursuant-president)
   Madhu Gottumukkala, Acting Director of CISA. "To stay ahead of these emerging risks, organizations must prioritize the procurement of PQC-capable technologies. This product categories list will support organizations making that critical transition." Government agencies and private sector firms are preparing for the threat posed by the advent of a cryptographically relevant quantum computer (CRQC), which the security community believes will be able to break open some forms of classical encryption. There are also concerns that threat actors could be harvesting encrypted data now in the hopes of accessing it once a quantum codebreaking machine is developed, a surveillance strategy known as harvest now, decrypt later (
   [HNDL](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later)
   ).
4. Physical access systems exposed

   More than 20 security vulnerabilities (from CVE-2025-59090 through CVE-2025-59109) discovered in Dormakaba physical access control systems could have allowed hackers to remotely open doors at major organizations. The flaws included hard-coded credentials and encryption keys, weak passwords, a lack of authentication, insecure password generation, local privilege escalation, data exposure, path traversal, and command injection. "These flaws let an attacker open arbitrary doors in numerous ways, reconfigure connected controllers and peripherals without prior authentication, and much more," SEC Consult
   [said](https://sec-consult.com/blog/detail/hands-free-lockpicking-critical-vulnerabilities-in-dormakabas-physical-access-control-system/)
   . There is no
   [evidence](https://assets.ctfassets.net/y0dk4vkszqeh/78reZeK1fTECnB4a6bL1fn/d37a5bdd5755c0b8cc3297fb82da9387/DKSA-26-26-012_Kaba_exos9300.pdf)
   that the
   [vulnerabilities](https://assets.ctfassets.net/y0dk4vkszqeh/24oRToEzmOXVHtJx3RRVFd/69c7ce3b927cfe352057f960d8ae10a8/DKSA-26-26-011_AM_92xxK5_92xxK7_exos_Client.pdf)
   were
   [exploited](https://assets.ctfassets.net/y0dk4vkszqeh/78reZeK1fTECnB4a6bL1fn/d37a5bdd5755c0b8cc3297fb82da9387/DKSA-26-26-012_Kaba_exos9300.pdf)
   in the wild.
5. Fake hiring lures steal logins

   A new phishing campaign is leveraging fake recruitment-themed emails that impersonate well-known employers and staffing companies, claiming to offer easy jobs, fast interviews, and flexible work. "The messages appear in multiple languages, including English, Spanish, Italian, and French, often tailored to the recipient's location," Bitdefender
   [said](https://www.bitdefender.com/en-us/blog/hotforsecurity/hiring-season-is-scam-season-how-fake-recruiters-exploit-job-seekers-with-trusted-brand-names)
   . "Top targets include people in the U.S., the U.K., France, Italy, and Spain." Clicking on a confirmation link in the message takes recipients to a fake page that harvests credentials, collects sensitive data, or redirects to malicious content.
6. Trusted cloud domains abused

   A novel campaign has exploited the trust associated with \*.vercel.app domains to bypass email filters and deceive users with financially themed lures, such as overdue invoices and shipping documents, as part of a phishing campaign observed from November 2025 to January 2026. The activity, which also employs a Telegram-gated delivery mechanism designed to filter out security researchers and automated sandboxes, is designed to deliver a legitimate remote access tool called GoTo Resolve, per
   [Cloudflare](https://www.cloudflare.com/cloudforce-one/research/report/vercel-hosted-rmm-abuse-campaign-evolves-with-telegram-c2-for-victim-filtering/)
   . Details of the campaign were
   [first documented](https://cyberarmor.tech/blog/threat-insight-cybercriminals-abusing-vercel-to-deliver-remote-access-malware)
   by CyberArmor in June 2025.
7. Cellular location precision reduced

   With iOS 26.3, Apple is adding a new "limit precise location" setting that reduces the location data available to cellular networks to increase user privacy. "The limit precise location setting enhances your location privacy by reducing the precision of location data available to cellular networks," Apple
   [said](https://support.apple.com/en-us/126101)
   . "With this setting turned on, some information made available to cellular networks is limited. As a result, they might be able to determine only a less precise location — for example, the neighborhood where your device is located, rather than a more precise location (such as a street address)." According to a new support document, iPhone models from supported network providers will offer the feature. The feature is expected to be available in Germany (Telekom), the U.K. (EE, BT), the U.S. (Boost Mobile), and Thailand (AIS, True). It also requires iPhone Air, iPhone 16e, or iPad Pro (M5) Wi-Fi + Cellular.
8. Legacy iOS support extended

   In more Apple-related news, the iPhone maker has released security updates for iOS 12 and iOS 15 to extend the digital certificate required by features such as iMessage, FaceTime, and device activation to continue working after January 2027. The update is available in
   [iOS 12.5.8](https://support.apple.com/en-us/118387)
   and
   [iOS 15.8.6](https://support.apple.com/en-us/108051)
   .
9. SEO poisoning-for-hire exposed

   A backlink marketplace has been discovered as a way to help customers get their malicious web pages ranked higher in search results. The group refers to themselves as Haxor, a slang word for hackers, and their marketplace as HxSEO, or HaxorSEO. The threat actors have established their operations and marketplace on Telegram and WhatsApp. The marketplace allows fraudsters to purchase a
   [backlink](https://www.semrush.com/blog/what-are-backlinks/)
   to a website of their choice, from a selection of legitimate domains already compromised by the group. These compromised domains are typically 15-20 years old and have a "trust" score associated with them to show how effective the purchased backlink would be for increasing search engine rankings. Each legitimate website is compromised with a web shell that enables Haxor to upload a malicious backlink to the site. By buying and then inserting these links into their sites, threat actors can boost search rankings, drawing unsuspecting visitors to phishing pages designed to harvest their credentials or install malware. WordPress sites with plugin flaws and vulnerable php components are the target of these efforts. The operation offers backlinks for just $6 per listing. The idea is that when users search for keywords like "financial logins" for specific banks, the HxSEO team's manipulation ensures the compromised sites appear ahead of the legitimate page in the search results. "HxSEO stands out for its emphasis on unethical search engine optimization (SEO) techniques, selling a service that supports phishing campaigns by improving the perceived legitimacy of malicious pages," Fortra
   [said](https://www.fortra.com/blog/seo-poisoning-marketplace-topping-search-results-impersonating-top-financial-institutions)
   . HxSEO leverages a range of malicious tools along with unethical Search Engine Optimization (SEO) tactics to ensure malicious sites appear at the top of your search results, making compromised sites harder to spot and to lure more potential victims. They also specialize in illicit backlink sales for SEO poisoning." The threat actors have been active since 2020.
10. Phishing hijacks ad accounts

    Meta business accounts belonging to advertising agencies and social media managers have been targeted by a new campaign that's designed to seize control of their accounts for follow-on malicious activities. The phishing attack begins with a message crafted to create urgency and concern, mimicking Meta's branding to warn recipients of policy violations, intellectual property issues, or unusual activity, and instructing them to click on a fake link that's engineered to harvest their credentials. "Once an account is compromised, the attacker: changes billing information, adding stolen or virtual cards, launches scam ads promoting fake crypto or investment platforms, [and] removes legitimate administrators, taking full control," CyberArmor
    [said](https://cyberarmor.tech/blog/global-phishing-targeting-meta-business-accounts)
    .
11. Kernel bug flagged as exploited

    The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has
    [added](https://www.cisa.gov/news-events/alerts/2026/01/26/cisa-adds-five-known-exploited-vulnerabilities-catalog)
    a security flaw impacting the Linux kernel to its Known Exploited Vulnerabilities (
    [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
    ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by February 16, 2026. "Linux Kernel contains an integer overflow vulnerability in the create\_elf\_tables() function, which could allow an unprivileged local user with access to SUID (or otherwise privileged) binary to escalate their privileges on the system," CISA said. The
    [vulnerability](https://dl.acm.org/doi/full/10.1145/3715001)
    ,
    [tracked](https://www.qualys.com/2018/09/25/cve-2018-14634/mutagen-astronomy-integer-overflow-linux-create_elf_tables-cve-2018-14634.txt)
    as
    [CVE-2018-14634](https://thehackernews.com/2018/09/linux-kernel-vulnerability.html)
    , has a CVSS score of 7.8. There are currently no reports of the flaws' in-the-wild exploitation.
12. France pushes video sovereignty

    The French government has announced plans to replace U.S. videoconferencing apps like Zoom, Microsoft Teams, Google Meet, Webex in favor of a homegrown alternative named Visio as part of efforts to improve security and strengthen its digital resilience. David Amiel, minister delegate for Civil Service and State Reform, said the country cannot risk having its scientific exchanges, sensitive data, and strategic innovations exposed to non-European actors. "Many government agencies currently use a wide variety of tools (Teams, Zoom, GoTo Meeting, or Webex), a situation that compromises data security, creates strategic dependencies on external infrastructure, leads to increased costs, and complicates cooperation between ministries," the government
    [said](https://presse.economie.gouv.fr/souverainete-numerique-letat-generalise-visio-sa-solution-de-visioconference-securisee-et-souveraine-a-destination-des-agents-publics/)
    . "The gradual implementation over the coming months of a unified solution, controlled by the state and based on French technologies, marks an important step in strengthening our digital resilience."
13. Student data tracking blocked

    Microsoft has been
    [ordered](https://noyb.eu/en/noyb-win-microsoft-ordered-stop-tracking-school-children)
    to cease the use of tracking cookies in Microsoft 365 Education after the Austrian data protection authority (DSB)
    [found](https://thehackernews.com/2025/10/weekly-recap-whatsapp-worm-critical.html#:~:text=Austria%20Says%20Microsoft%20Violated%20E%2EU%2E%20Laws)
    that the company illegally installed cookies on the devices of a minor without consent. These cookies can be used to analyze user behavior, collect browser data, and serve targeted ads. It's worth noting that German data protection authorities have already considered Microsoft 365 to fall short of GDPR requirements, Austrian non-profit none of your business (NOYB) said. Microsoft has four weeks to cease tracking the complainant.
14. Cross-border swatting ring busted

    Hungarian and Romanian police have arrested four young suspects in connection with bomb threats, false emergency calls, and the misuse of personal data. The suspects include a 17-year-old Romanian national and three Hungarians aged 16, 18, and 20. As part of the operation, officials confiscated all their data storage devices, mobile phones, and computer equipment. The development comes in the aftermath of a probe that began in mid-July 2025 following a series of phone calls to law enforcement. The suspects approached victims on Discord, obtained their phone numbers and personal details, and then used that information to place false emergency calls in their names. "The reports included threats to blow up educational and religious institutions and residential buildings, to kill various people, and to attack police units," authorities
    [said](https://www.police.hu/hu/hirek-es-informaciok/legfrissebb-hireink/bunugyek/swatting-es-doxing-miatt-indult-nyomozas)
    . "The reports required the intervention of a significant police force."
15. Latin America hit hardest

    According to data from Check Point, organizations experienced an average of 2,027 cyber attacks per organization per week in December 2025. "This represents a 1% month-over-month increase and a 9% year-over-year increase," the company
    [said](https://blog.checkpoint.com/research/latin-america-sees-sharpest-rise-in-cyber-attacks-in-december-2025-as-ransomware-activity-accelerates/)
    . "While overall growth remained moderate, Latin America recorded the sharpest regional increase, with organizations experiencing an average of 3,065 attacks per week, a 26% increase year over year." APAC followed with 3,017 weekly attacks per organization (+2% year-over-year), while Africa averaged 2,752 attacks, representing a 10% decrease year-over-year. The education sector remained the most targeted industry in December, averaging 4,349 attacks per organization per week. The other prominent targeted sectors include governments, associations, telecommunications, and energy. Within Latin America, healthcare and medical organizations were the top targets.
16. Crypto laundering ring punished

    The U.S. Department of Justice (DoJ) announced that Chinese national Jingliang Su was sentenced today to 46 months in prison for his role in laundering more than $36.9 million from victims in a digital asset investment scam that was carried out from
    [scam centers](https://www.wired.com/story/the-red-bull-leaks/)
    in Cambodia. Su has also been ordered to pay $26,867,242.44 in restitution. Su was part of an international criminal network that tricked U.S. victims into transferring funds to accounts controlled by co-conspirators, who then laundered victim money through U.S. shell companies, international bank accounts, and digital asset wallets. Su
    [pleaded guilty](https://thehackernews.com/2025/06/weekly-recap-iphone-spyware-microsoft-0.html#:~:text=2%20ViLE%20Members%20Sentenced%20to%20Prison)
    to the charges, along with four others, in June 2025. "This defendant and his co-conspirators scammed 174 Americans out of their hard-earned money,"
    [said](https://www.justice.gov/opa/pr/chinese-national-sentenced-prison-role-crypto-scam-targeting-americans)
    Assistant Attorney General A. Tysen Duva of the Justice Department's Criminal Division. "In the digital age, criminals have found new ways to weaponize the internet for fraud." In all, eight co-conspirators have
    [pleaded guilty](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=U%2ES%2E%20Treasury%20Sanctions%2019%20People%20and%20Entities%20in%20Connection%20with%20Scam%20Operations)
    so far, including Jose Somarriba and ShengSheng He.
17. Major dark web operator convicted

    Raheim Hamilton (aka Sydney and Sydney), 30, of Suffolk, Virginia, has pleaded guilty in the U.S. to a federal drug conspiracy charge in connection with operating a dark web marketplace called
    [Empire Market](https://thehackernews.com/2024/06/singapore-police-extradites-malaysians.html)
    between 2018 and 2020, alongside Thomas Pavey (aka Dopenugget). "During that time, the online market facilitated more than four million transactions between vendors and buyers valued at more than $430 million, making it one of the largest dark web marketplaces of its kind at the time," the DoJ
    [said](https://www.justice.gov/usao-ndil/pr/co-creator-dark-web-marketplace-pleads-guilty-chicago-drug-conspiracy-charge)
    . "The illegal products and services available on the site included controlled substances, compromised or stolen account credentials, stolen personally identifying information, counterfeit currency, and computer-hacking tools. Sales of controlled substances were the most prevalent activity, with net drug sales totaling nearly $375 million over the life of the site." Hamilton agreed to forfeit certain ill-gotten proceeds, including about 1,230 bitcoin and 24.4 Ether, as well as three properties in Virginia. Pavey, 40, pleaded guilty last year to a federal drug conspiracy charge and admitted his role in creating and operating Empire Market. He is currently awaiting sentencing.
18. Darknet operator admits role

    [Alan Bill](https://www.justice.gov/usao-edmo/pr/slovakian-man-accused-running-darknet-market-selling-drugs-and-personal-information)
    , 33, of Bratislava, has pleaded guilty to his involvement in a darknet market called
    [Kingdom Market](https://thehackernews.com/2023/12/german-authorities-dismantle-dark-web.html)
    that sold drugs and stolen personal information between March 2021 and December 2023. Bill has also admitted to receiving cryptocurrency from a wallet associated with Kingdom, in addition to assisting with the creation of Kingdom's forum pages on Reddit and Dread and having access to Kingdom usernames that made postings on behalf of Kingdom on social media accounts. As part of his plea agreement, Bill has agreed to forfeit five different types of coins in a cryptocurrency wallet, as well as the Kingdommarket[.]live and Kingdommarket[.]so domains, which have been shut down by authorities. Bill is scheduled to be sentenced on May 5, 2026. "Bill was arrested December 15, 2023, at Newark Liberty International Airport after a customs inspection found two cellular telephones, a laptop, a thumb drive, and a hardware wallet used to store cryptocurrency private keys," the DoJ
    [said](https://www.justice.gov/usao-edmo/pr/slovakian-man-admits-aiding-darknet-market-sold-drugs-and-stolen-personal-information)
    . "The electronics contained evidence of his involvement with Kingdom."
19. Android theft defenses expanded

    Google has
    [announced](https://security.googleblog.com/2026/01/android-theft-protection-feature-updates.html)
    an expanded set of Android theft-protection features that build upon existing protections like
    [Theft Detection Lock and Offline Device Lock](https://thehackernews.com/2024/05/google-adds-ai-powered-theft-protection.html)
    introduced in
    [2024](https://security.googleblog.com/2024/10/android-theft-protection.html)
    . The features are available for Android devices running Android 16+. Chief among them are granular controls to enable or disable Failed Authentication Lock, which automatically locks the device's screen after excessive failed authentication attempts. Other notable updates include extending
    [Identity Check](https://thehackernews.com/2025/01/androids-new-identity-check-feature.html)
    to cover all features and apps that use the Android Biometric Prompt, stronger protections against attempts to guess PIN, pattern, or password by increasing the lockout time after failed attempts, and adding an optional security question to initiate a Remote Lock so as to ensure that it's being done by the real device owner. "These protections are designed to make Android devices harder targets for criminals before, during, and after a theft attempt," Google said.
20. AI-linked malware tooling spotted

    A
    [PureRAT](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html)
    campaign has
    [targeted job seekers](https://thehackernews.com/2025/12/silver-fox-uses-fake-microsoft-teams.html#job-seekers-targeted-by-purerat)
    using malicious ZIP archives either attached in emails or shared as links pointing to Dropbox that, when opened, leverage DLL side-loading to launch a batch script that's responsible for executing the malware. In a new analysis, Broadcom's Symantec and Carbon Black Threat Hunter Team said there are signs these tools, including the batch script, have been authored using artificial intelligence (AI). "Multiple tools used by the attacker bear hallmarks of having been developed using AI, such as detailed comments and numbered steps in scripts, and instructions to the attacker in debug messages," it
    [said](https://www.security.com/threat-intelligence/ai-purerat-phishing)
    . "Virtually every step in the batch file has a detailed comment in Vietnamese." It's suspected that the threat actor behind the actor is based in Vietnam and is likely selling access to compromised organizations to other actors.
21. UK–China cyber talks launched

    The U.K. and China have established a forum called Cyber Dialogue to discuss cyber attacks for security officials from the two nations to manage threats to each other's national security. The deal, according to
    [Bloomberg](https://www.bloomberg.com/news/articles/2026-01-20/uk-and-china-set-up-forum-on-cyberattacks-to-lower-tensions)
    , is a way to "improve communication, allow private discussion of deterrence measures and help prevent escalation." The U.K. has previously called out Chinese threat actors for targeting its national infrastructure and government systems. As recently as this week, The Telegraph
    [reported](https://www.telegraph.co.uk/news/2026/01/26/china-hacked-downing-street-phones-for-years/)
    that Chinese nation-state threat actors have hacked the mobile phones of senior U.K. government members since 2021.
22. Poor OPSEC unmasks broker

    Earlier this month, Jordanian national Feras Khalil Ahmad Albashiti
    [pleaded guilty](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html#:~:text=Jordan%20National%20Pleads%20Guilty%20to%20Selling%20Access)
    to charges of selling access to the networks of at least 50 companies through a cybercriminal forum. Albashiti, who also went by the online aliases r1z, secr1z, and j0rd4n14n, is said to have made 1,600 posts across multiple forums, including XSS, Nulled, Altenen, RaidForums, BlackHatWorld, and Exploit. On LinkedIn, Albashiti described himself as an information technology architect and consultant, claiming experience in cyber threats, cloud, network, web, and penetration testing. The kicker? His LinkedIn profile URL was "linkedin[.]com/in/r1z." "The actor's website, sec-r1z.com, was created in 2009, and based on WHOIS information, also reveals personal details of Firas, including the same Gmail address, alongside additional details like address and phone number," KELA
    [said](https://www.kelacyber.com/blog/the-high-price-of-poor-opsec-inside-the-r1z-initial-access-broker-case-/)
    . "The r1z case shows how initial access brokers monetize firewall exploits and enterprise access at scale, while the actor's OPSEC failures leave long-term attribution trails that expose the ransomware supply chain."
23. Encryption flaw traps victims

    Cybersecurity company Halcyon said it identified a critical flaw in the encryption process of
    [Sicarii](https://thehackernews.com/2026/01/new-osiris-ransomware-emerges-as-new.html)
    , a newly discovered ransomware strain, that makes data recovery impossible even if an impacted organization pays a ransom. "During execution, the malware regenerates a new RSA key pair locally, uses the newly generated key material for encryption, and then discards the private key," the company
    [said](https://www.halcyon.ai/ransomware-alerts/alert-sicarii-ransomware-encryption-key-handling-defect)
    . "This per-execution key generation means encryption is not tied to a recoverable master key, leaving victims without a viable decryption path and making attacker-provided decryptors ineffective for affected systems." It's assessed with moderate confidence that the threat actors used AI-assisted tooling that may have led to the implementation error.
24. Human-in-the-loop MFA bypass

    Google-owned Mandiant said it's
    [tracking](https://cyberscoop.com/shinyhunters-voice-phishing-sso-okta-mfa-bypass-data-theft/)
    a fresh wave of
    [voice-phishing attacks](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html)
    targeting single sign-on tools that are resulting in data theft and extortion attempts. Multiple threat actors are said to be combining voice calls and custom phishing kits, including a group identifying itself as ShinyHunters, to obtain unauthorized access and enroll threat actor-controlled devices into victim multi-factor authentication (MFA) for persistent access. Upon gaining access, the threat actors have been found to pivot to SaaS environments to exfiltrate sensitive data. It's unclear how many organizations have been impacted by the campaign. In a similar alert, Silent Push said SSO providers are being targeted by a massive identity-theft campaign across more than 100 high-value enterprises. The activity leverages a new Live Phishing Panel that allows a human attacker to sit in the middle of a login session, intercept credentials, and gain persistent access. The hackers have set up fake domains targeting these companies, but it's not known whether they have actually been targeted or whether their attempts to gain access to systems were successful. Some of the companies impacted include
    [Crunchbase, SoundCloud, and Betterment](https://www.linkedin.com/posts/alon-gal-utb_big-shinyhunters-confirmed-to-me-that-they-activity-7420398716076908544-Ch8-/)
    , per Hudson Rock's co-founder and CTO Alon Gal. "This isn't a standard automated spray-and-pray attack; it is a human-led, high-interaction voice phishing ('vishing') operation designed to bypass even hardened Multi-Factor Authentication (MFA) setups," it
    [noted](https://www.silentpush.com/blog/slsh-alert/)
    .
25. React flaw fuels crypto-mining attacks

    Threat actors have
    [exploited](https://bi.zone/eng/expertise/blog/zloumyshlenniki-ekspluatiruyut-uyazvimost-cve-2025-55182-v-atakakh-na-rossiyskie-kompanii/)
    the recently disclosed security flaw in React Server Components (CVE-2025-55182 aka
    [React2Shell](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html)
    ) to infect Russian companies with XMRig-based cryptominers, per BI.ZONE. Other payloads deployed as part of the attacks include botnets such as
    [Kaiji](https://thehackernews.com/2025/12/react2shell-exploitation-delivers.html)
    and
    [Rustobot](https://thehackernews.com/2025/04/docker-malware-exploits-teneo-web3-node.html)
    , as well as the
    [Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html)
    implant. Russian companies in the housing, finance, urban infrastructure and municipal services, aerospace, consumer digital services, chemical industry, construction, and production sectors have also been
    [targeted](https://habr.com/ru/companies/F6/articles/987734/)
    by a suspected pro-Ukrainian threat group called PhantomCore that employs phishing containing ZIP attachments to deliver a PowerShell malware that's similar to
    [PhantomRemote](https://thehackernews.com/2025/07/weekly-recap-sharepoint-0-day-chrome.html#:~:text=Rainbow%20Hyena%20Goes%20After%20Russian%20Firms)
    .
26. Malware flood hits open source

    Supply chain security company Sonatype said it logged 454,600 open-source malware packages in 2025, taking the total number of known and blocked malware to over 1.233 million packages across npm, PyPI, Maven Central, NuGet, and Hugging Face. The threat is compounded by AI agents confidently recommending nonexistent versions or malware-infected packages, exposing developers to new risks like slop squatting. "The evolution of open source malware crystallized, evolving from spam and stunts into sustained, industrialized campaigns against the people and tooling that build software," it
    [said](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction)
    . "The next frontier of software supply chain attacks is not limited to package managers. AI model hubs and autonomous agents are converging with open source into a single, fluid software supply chain — a mesh of interdependent ecosystems without uniform security standards."
27. Ransomware ecosystem doubles

    A new analysis from Emsisoft revealed that ransomware groups had a massive year in 2025, claiming between 8,100 and 8,800 victims, significantly up from about 5,300 in 2023. "As the number of victims has grown, so has the number of ransomware groups," the company
    [said](https://www.emsisoft.com/en/blog/47215/the-state-of-ransomware-in-the-u-s-report-and-statistics-2025/)
    . The number of active groups has surged from about 70 in 2023 to nearly 140 in 2025. Qilin, Akira, Cl0p, and Play emerged as some of the most active players in the landscape. "Law enforcement efforts are working—they are fragmenting major groups, forcing shutdowns, and creating instability at the top. Yet this disruption has not translated into fewer victims," Emsisoft said. "Instead, ransomware has become more decentralized, more competitive, and more resilient. As long as affiliates remain plentiful and social engineering remains effective, victim counts are likely to continue rising."
28. ATM malware ring charged

    The DoJ has announced charges against an additional 31 individuals accused of being involved in a massive ATM jackpotting scheme that resulted in the theft of millions of dollars. The attacks involve the use of malware called
    [Ploutus](https://thehackernews.com/2025/12/us-doj-charges-54-in-atm-jackpotting.html)
    to hack into ATMs and force them to dispense cash. Between February 2024 and December 2025, the gang stole at least $5.4 million from at least 63 ATMs, most of which belonged to credit unions, the DoJ alleged. Many of the defendants charged in this Homeland Security Task Force operation are Venezuelan and Colombian nationals, including illegal alien Tren de Aragua (TdA) members, the DoJ said, adding 56 others have already been charged. "A large ring of criminal aliens allegedly engaged in a nationwide conspiracy to enrich themselves and the TdA terrorist organization by ripping off American citizens,"
    [said](https://www.justice.gov/opa/pr/investigation-international-atm-jackpotting-scheme-and-tren-de-aragua-results-additional)
    Deputy Attorney General Todd Blanche. "The Justice Department's Joint Task Force Vulcan will not stop until it completely dismantles and destroys TdA and other foreign terrorists that import chaos to America."
29. Blockchain-based C2 evasion

    A ransomware strain called
    [DeadLock](https://threatscene.com/blog-update/deadlock-ransomware-current-assessment-and-defender-guidance/)
    , which was first detected in the wild in July 2025, has been observed using Polygon smart contracts for proxy server address rotation or distribution. While the exact
    [initial access vectors](https://www.broadcom.com/support/security-center/protection-bulletin/deadlock-ransomware)
    used by the ransomware are not known, it drops an HTML file which acts as a wrapper for Session, an end-to-end encrypted and decentralized instant messenger. The HTML is used to facilitate direct communication between the DeadLock operator and the victim by sending and receiving messages from a server that acts as a middleware or proxy. "The most interesting part of this is how server addresses are retrieved and managed by DeadLock," Group-IB
    [noted](https://www.group-ib.com/blog/deadlock-ransomware-polygon-smart-contracts/)
    , stating it "uncovered JS code within the HTML file that interacts with a smart contract over the Polygon network." This list contains the available endpoints for interacting with the Polygon network or blockchain and obtaining the current proxy URL via the smart contract. DeadLock also stands apart from traditional ransomware operations in that it lacks a data leak site to publicize the attacks. However, it uses AnyDesk as a remote management tool and leverages a previously unknown loader to exploit the Baidu Antivirus driver ("BdApiUtil.sys") vulnerability (CVE-2024-51324) to conduct a bring your own vulnerable driver (BYOVD) attack and disable endpoint security solutions. According to
    [Cisco Talos](https://blog.talosintelligence.com/byovd-loader-deadlock-ransomware/)
    , it's believed that the threat actor leverages the compromised valid accounts to gain access to the victim's machine.
30. Crypto laundering networks scale up

    In a report published this week, Chainalysis said Chinese-language money laundering networks (CMLNs) are dominating known crypto money laundering activity, processing an estimated 20% of illicit cryptocurrency funds over the past five years. "CMLNs processed $16.1 billion in 2025 – approximately $44 million per day across 1,799+ active wallets," the blockchain intelligence firm
    [said](https://www.chainalysis.com/blog/2026-crypto-money-laundering/)
    . "The illicit on-chain money laundering ecosystem has grown dramatically in recent years, increasing from $10 billion in 2020 to over $82 billion in 2025." These networks launder funds using a variety of mechanisms, including gambling platforms, money movement, and peer-to-peer (P2P) services that process fund transfers without know your customer (KYC) checks. CLMNs have also processed an estimated 10% of funds stolen in pig butchering scams, an increase coinciding with the decline in the use of centralized exchanges. This is complemented by the emergence of
    [guarantee marketplaces](https://thehackernews.com/2026/01/tudou-guarantee-marketplace-halts.html)
    like HuiOne and Xinbi that function primarily as marketing venues and escrow infrastructure for CMLNs. "CMLNs' advertising on these guarantee services offer a range of money laundering techniques with the primary goal of integrating illicit funds into the legitimate financial system," Chainalysis said.
31. SMS fraud hits Canadians

    Threat actors are impersonating government services and trusted national brands in Canada, often using lures related to traffic fines, tax refunds, airline bookings, and parcel delivery alerts in SMS messages and malicious ads to enable account takeovers and direct financial fraud by directing them to phishing landing pages. "A significant portion of the activity is aligned with the 'PayTool' phishing ecosystem, a known fraud framework that specializes in traffic violation and fine payment scams targeting Canadians through SMS-based social engineering," CloudSEK
    [said](https://www.cloudsek.com/blog/pivoting-from-paytool-tracking-various-frauds-and-e-crime-targeting-canada)
    .

Seen together, these stories show problems building slowly, not all at once. The same gaps are being used again and again until they work.

Most of this didn't start this week. It's growing, spreading, and getting easier for attackers to repeat. The full list helps show where things are heading before they become normal.