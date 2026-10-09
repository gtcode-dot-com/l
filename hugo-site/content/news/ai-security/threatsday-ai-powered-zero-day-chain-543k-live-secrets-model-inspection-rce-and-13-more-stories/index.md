---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:31:19.783791+00:00'
exported_at: '2026-10-07T01:31:21.102497+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html
structured_data:
  about: []
  author: ''
  description: 'This week in cybersecurity: AI-driven attacks, exposed secrets, old
    flaws, new exploit tricks, malware techniques, and security research worth knowing'
  headline: 'ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection
    RCE and 13 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection
  RCE and 13 More Stories'
updated_at: '2026-10-07T01:31:19.783791+00:00'
url_hash: f1d14dce844e54b225ce8b410b574db361e690cb
---

**

Ravie Lakshmanan
**

Oct 01, 2026

Hacking News / Cybersecurity News

This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years.

That is the lesson running through the list. Attackers do not always need a brilliant new trick. They can hide commands in public infrastructure, reuse old flaws, abuse weak defaults, or let automation stitch together a rough path that still works. Faster tools are changing the pace, but basic mistakes are still doing plenty of the work.

So the interesting question this week is not “what broke?” It is “what did we assume was safe because it looked ordinary?” The full list has answers.

The threats change every week.
Subscribe, and we’ll alert you
when each new ThreatsDay Bulletin is out.

1. ATM jackpotting crackdown

   The U.S. Treasury's Office of Foreign Assets Control (OFAC)
   [sanctioned](https://home.treasury.gov/news/press-releases/sb0640/)
   10 targets involved in a Tren de Aragua
   [ATM jackpotting scheme](https://thehackernews.com/2026/02/fbi-reports-1900-atm-jackpotting.html)
   that stole at least $40.73 million from U.S. financial institutions. The network
   [used cryptocurrency](https://www.chainalysis.com/blog/ofac-sanctions-tren-de-aragua-crypto-laundering-september-2026/)
   to launder the proceeds. Tren de Aragua is a designated Foreign Terrorist Organization. Jackpotting uses Ploutus malware to force ATMs to dispense cash. Treasury estimates show reported losses totaling $40.73 million from more than 1,500 alleged TdA jackpotting attacks in the U.S. as of August 2025. TRM Lab
   [said](https://www.trmlabs.com/resources/blog/treasury-sanctions-tren-de-aragua-atm-jackpotting-network-including-seven-tron-addresses)
   the seven designated crypto wallet addresses have received approximately $6.1 million in total inflows since March 2022. "Tren de Aragua is using ATM malware as a terrorist financing tool, then moving the cash onto TRON so it looks like ordinary exchange deposits,"  said Ari Redbord, Global Head of Policy at TRM Labs. "That is the same playbook we keep seeing from FTOs with on-chain infrastructure. These sanctions target that playbook. We are seeing the Treasury go after both the bad actors and their financial facilitators."
2. Blockchain-based malware concealment

   Cyber threat actors are using public blockchains to conceal malware instructions, making it challenging to seize or take down. This technique, referred to as
   [EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)
   , is part of a broader approach called Blockchain Dead Drops (BDD). Chainalysis
   [said](https://www.chainalysis.com/blog/etherhiding-blockchain-dead-drops/)
   "North Korean and Iranian-state operators are among those developing distinct blockchain dead drop techniques," adding "BDDs have surged 440% since the launch of Chinese high-capacity open-source AI models that place no restrictions on generating malicious code."
3. AI safety review underway

   BBC News has
   [reported](https://www.bbc.com/news/articles/cmrergq3j7lgo)
   that Chinese AI company Moonshot is conducting an internal review after a
   [July 2026 report from Mindgard](https://mindgard.ai/blog/easy-to-use-ai-to-develop-bioweapons)
   found that its AI models, Kimi K2.6 and K3 Swarm, could bypass safety guardrails and generate dangerous information, including providing plans for cyberattacks, terrorism plots, and assassinations.
4. Prompt injection as defense

   In July 2026, Tracebit detailed a technique called
   [Context Bombs](https://thehackernews.com/2026/08/threatsday-ghostjacking-ai-attacks.html#prompt-injection-as-defense)
   that uses prompt injections as a way to trip an AI model provider's runtime safety checks and prevent it from taking malicious actions. In a new report, the AI security company said indirect prompt injections can be used to stop attacks from open-weight models, abliterated or otherwise. "We turned to indirect prompt injection: instructions placed in material an agent reads while carrying out its task," Tracebit
   [said](https://tracebit.com/blog/context-bombs-against-abliterated-ai-models)
   . "The new payload was designed to make the agent believe its operator had ended the assessment. We placed it inside a canary secret in AWS Secrets Manager, where an agent exploring the account could discover it. The string used conversation delimiters to make the secret’s contents resemble an exchange between the assistant and its user. The forged user message then told the agent to stop all activity and acknowledge the instruction."
5. New EDR evasion technique

   Security researcher Zero Salarium has outlined a new process injection technique that, instead of WriteProcessMemory(), uses a console process's stdin pipe and WriteFile() to write arbitrary bytes into memory and execute them. "Unlike traditional approaches, console named-pipe injection does not use VirtualAllocEx and WriteProcessMemory," the researcher
   [said](https://www.zerosalarium.com/2026/09/edr-evasion-process-injection-without-WriteProcessMemory.html)
   . "Instead, it takes advantage of read and write operations through a named pipe, along with the way console programs store interactive commands in memory. As a result, traditional monitoring methods cannot be used to reliably detect and prevent this technique."
6. Cache collisions enable poisoning

   YesWeHack has detailed a web cache poisoning technique called cache key injection that turns the cache key into an attack surface. At a high level, if a cache builds its key by simply combining attacker-influenced strings together without separators, an attacker can make two distinct HTTP requests produce the same cache key. This collision can then be used for cache deception, leaking cached restricted responses, denial-of-service, or, under more specific conditions, stored XSS when executable content is injected. "Cache key injection vulnerabilities arise when a cache concatenates unsafe fragments without clearly defined boundaries," YesWeHack
   [said](https://www.yeswehack.com/lab/research-cache-key-injection)
   . "Different combinations of fragment values can then produce the same final key. Severity depends on the affected endpoint, cache lifetime, number of users sharing the cache, and whether the poisoned response propagates through edge or origin caching layers."
7. 22TB breach claim questioned

   A cyber
   [threat intelligence report](https://www.hack-elite.com/blog/exposed-pakistani-threat-actor-behind-%E2%80%93-indian-embassy-mofa-data-leak-claim)
   from HackElite has questioned claims that a threat actor stole 22 TB of data from Indian embassies and foreign-affairs entities after researchers found that samples shared as proof overlapped with information already available from public sources. The data was advertised on X Forums on September 23 for $200,000 and was said to include embassy directories, Foreign Service records, organizational charts, officer lists, and other government documents. The report said the actor used the handle “RAYLEAS” and shared the Telegram account @Rayhucker for sample access and sales inquiries, while an OSINT investigation linked the account to a Pakistan-based individual through historical display names and public profiles. However, the researchers stressed that the 22 TB breach claim and the identity attribution remain unverified, adding that the findings should be treated as an intelligence assessment rather than a legal conclusion.
8. Miner compiled on victim host

   In a novel attack documented by Huntress, a threat actor compiled a cryptocurrency miner on the victim endpoint instead of dropping one directly. "The incident started with exploitation of a known Samsung MagicINFO flaw [
   [CVE-2025-4632](https://nvd.nist.gov/vuln/detail/cve-2025-4632)
   ]," Huntress
   [said](https://www.huntress.com/blog/threat-actor-compiles-cryptominer)
   . "Attackers then deployed a rogue AnyDesk instance (after three tries), created a new local admin account, and disabled Defender protections. While the miner compilation aspect of this attack is interesting, the incident shows why defenders should look beyond known miner binaries: repeated RMM downloads and unexpected compiler activity can reveal a compromise before the final payload runs."
9. AI lowers cyberattack barriers

   Chen Yixin, head of China's Ministry of State Security, said AI has implications for political security, institutional security, and ideological security, with "hostile forces" using synthetic content to spread fabricated political rumors, spread harmful information, and incite confrontational sentiments at low cost and in large quantities. Calling the emergence of frontier AI models from Anthropic and OpenAI a "disruptive transformation," Chen
   [said](https://mp.weixin.qq.com/s/jsc97cKVYOcHuI_WisvOxw)
   the technology boosts the "efficiency and weaponization capabilities associated with discovering cyber vulnerabilities and developing malware. Cyber ​​warfare has entered a new phase characterized by the industrialization of vulnerability discovery, fully automated offensive and defensive operations, and AI-versus-AI confrontations. Certain nations and organizations now possess the ability to rapidly discover vulnerabilities at scale, automatically chain attack paths, and execute complex hacking missions; this drastically lowers the technical barriers and costs associated with launching cyberattacks, thereby posing serious risks to China's critical information infrastructure."
10. Quantum-safe certificates coming

    Cloudflare has
    [announced](https://blog.cloudflare.com/cloudflare-certificate-authority/)
    plans to become a public Certificate Authority (CA) that can issue quantum-safe digital certificates that websites need to encrypt traffic and prove their identity to visitors. "The new CA will support both traditional encryption and next-generation
    [post-quantum Merkle Tree Certificates](https://blog.cloudflare.com/pq-ca-with-mtcs/)
    (MTCs), giving every website a path to stay protected as computing power advances—with no new tools or rebuilds required," the company said. In addition, Cloudflare has agreed to acquire established, publicly trusted Root CA key material from GlobalSign to ensure certificates work on older smartphones, operating systems, and devices that no longer receive software updates. Earlier this February, Google
    [said](https://thehackernews.com/2026/03/google-develops-merkle-tree.html)
    it's developing an evolution of HTTPS certificates based on Merkle Tree Certificates (MTCs) for use in its Chrome web browser. Production MTC issuance is scheduled for the first quarter of 2027.
11. Over half a million secrets exposed

    A new study from Truffle Security has found 543,699 unique credentials exposed in public GitHub repositories that were still valid as of July 2026 despite the platform's security measures to prevent leakage of such data. "The median one had been sitting in a public default branch for 784 days. The oldest was committed in 2009 and still works," Truffle Security
    [said](https://trufflesecurity.com/blog/github-repos-exposed-543699-credentials-nobody-revoked-them)
    . "Just under 200,000 of them were pushed after GitHub turned push protection on by default."
12. Encrypted backups reach iOS

    Signal has
    [introduced](https://aboutsignal.com/news/signal-introduces-on-device-backups-for-iphone-and-ipad/)
    on-device encrypted backups for iPhones and iPads with version 8.30, a feature that was already supported on Android, Linux, macOS, and Windows. The messaging app is also
    [testing](https://aboutsignal.com/news/signal-registration-without-a-phone-number-now-available/)
    the ability for users to register for an account without providing their phone number. The feature, in its current form, does not allow an existing user to remove a phone number. The feature, called
    [Signal Login](https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android)
    , is currently limited to Signal Android Beta 8.28.1.
13. Model inspection triggers code execution

    Unsloth, an open-source library for fine-tuning and quantizing LLMs, has been found to contain a vulnerability in the model picker component in Unsloth Studio that could automatically execute Python code from its repository. "Selecting a model in the UI caused the backend to download and run Python code shipped inside that model's HuggingFace repository," Pillar Security
    [said](https://www.pillar.security/blog/look-dont-load-model-inspection-in-unsloth-studio-leads-to-critical-arbitrary-code-execution)
    . "The code ran from nothing more than a metadata check. Reading the model's config.json was enough to trigger the exploit; the backend never loaded the weights or ran inference – the act of inspecting a model was enough to run its code." An attacker could exploit this flaw to expose proprietary training data, model artifacts, and any Hugging Face tokens, SSH keys, or cloud credentials accessible to that process. "An attacker could run code as the user, which could translate to stealing accessible data, altering models and training outputs, or using available credentials to access other systems," Pillar added. The issue has been addressed in version 2026.6.9 released on June 18, 2026.
14. $16 million crypto fraud case

    Trung Nguyen Van, 37, a Vietnamese national, has been charged for his role in defrauding a victim out of millions of dollars' worth of cryptocurrency in a wire fraud
    [pig butchering scam](https://thehackernews.com/2026/01/researchers-uncover-service-providers.html)
    . "Between June and August of 2024, Victim #1 transferred approximately $16,000,000 worth of cryptocurrency, believing they were making an investment in a cryptocurrency investment platform called 'Triangle,'" the U.S. Justice Department
    [said](https://www.justice.gov/usao-wdmo/pr/vietnamese-national-charged-role-massive-pig-butchering-cryptocurrency-scam)
    . "One such transfer, taking place on Aug. 7, 2024, directly traceable to Van’s cryptocurrency wallet, was for over $569,000 in cryptocurrency. On Aug. 9, 2024, Van’s cryptocurrency wallet received six transfers totaling approximately $569,569 in cryptocurrency, traceable to Victim #1. Immediately following the receipt of the funds, Van proceeded to transfer approximately $567,999 worth of cryptocurrency in four transactions to a private, un-hosted cryptocurrency wallet off the centralized blockchain network." Between February 9, 2018, and December 17, 2024, Van's cryptocurrency wallets received approximately $53,275,939 in cryptocurrency assets from wire fraud schemes targeting U.S. citizens.
15. Zero-days chained to root access

    Two zero-day vulnerabilities in the open-source Zammad ticketing system,
    [CVE-2026-102489 and CVE-2026-102490](https://csirt.divd.nl/cases/DIVD-2026-00014/)
    , have been chained by threat actors to
    [break into](https://www.divd.nl/newsroom/articles/when-no-if/)
    the Dutch Institute for Vulnerability Disclosure (DIVD). The incident
    [took place on September 21, 2026](https://csirt.divd.nl/cases/DIVD-2026-00014/)
    . "Used together, they allowed the attackers to hijack sessions, run code remotely and escalate privileges from the Zammad user to root, in seconds, due to the agentic part of this hack," DIVD
    [said](https://www.linkedin.com/posts/zammad-share-7511092586393010176-RkCb/)
    . "From there they were able to access other services and read and exfiltrate data." This
    [includes](https://www.linkedin.com/posts/divd-nl_this-is-probably-the-most-painful-and-awkward-activity-7511448012582387714-W3cT)
    user data of its volunteers, such as DIVD email addresses and possibly contact details. Evidence indicates that the "loud and very, very messy" attack was powered by AI. "We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic or pattern," DIVD
    [added](https://www.linkedin.com/posts/in-every-crisis-you-work-with-whatever-you-share-7510363577375993856--zPB/)
    . "It also looks like the agent skipped a few steps on its learning curve, because it has done some pretty dumb things, like polluting its own MitM attack with password spraying."
16. AI reshapes vulnerability discovery

    AI Vulnerability Discovery and Exploitation Trends

    Google Threat Intelligence Group (GTIG) has revealed that the number of vulnerabilities disclosed per month has doubled, rising from 5,045 in January 2026 to 10,477 in July and 10,740 in August 2026. "The number of vulnerabilities exploited increased from an average of 10.5 per month in 2025 to an average of 18 per month from January 2026 to August 2026," GTIG said. "Zero-day vulnerability exploitation grew from an average of 8 per month in 2025 to an average of 11 per month from January 2026 to August 2026." The tech giant said AI is not only changing the pace of vulnerability discovery and exploitation, but also the types of vulnerabilities being discovered. "AI-assisted discovery found proportionally fewer Low-Risk vulnerabilities, more Moderate-Risk vulnerabilities, and more vulnerabilities leading to remote code execution (RCE)," it said. The number of High-Risk vulnerabilities has surged from 131 disclosures in January 2026 to 350 in August 2026, a 167% growth. From January 2026 to August 2026, a total of 141 distinct vulnerabilities have been disclosed and exploited, up from 127 for the entirety of 2025. Most of the flaws discovered by AI-assisted approaches include RCE, denial-of-service, security bypass, information disclosure, and data manipulation.
17. 189-month prison sentences

    Two Delaware men, Chijioke Timothy Odimegwu, 25, and Harafat Mogaji, 26, have been sentenced to 189 months in federal prison for their roles in an international cyber intrusion scheme. While serving the U.S. Air Force, the defendants "attacked business victims across the United States with email 'spamming' and phishing campaigns to steal usernames and passwords for victims' employee email accounts," the Justice Department
    [said](https://www.justice.gov/usao-sdia/pr/delaware-men-sentenced-cyber-intrusion-scheme-targeting-victims-southern-district-iowa)
    . "They and their co-conspirators then used these stolen credentials, along with 'spoofed' email addresses mimicking emails associated with the victim or its business partners, to communicate with their victims and redirect payments to and from the victims' trusted business partners to accounts controlled by the defendants’ co-conspirators. As part of their spamming and phishing campaigns, Odimegwu and Mogaji also harvested financial information from victims, such as financial account numbers and information, personal identification numbers, and credit and debit card numbers." Odimegwu and Mogaji are said to have fraudulently diverted around $2.4 million wire sent by two victims in Iowa and Ohio to a bank account under their control.

The useful part is not remembering every story. It is noticing the small choices behind them: what gets trusted, what stays exposed, what runs without much checking, and what nobody looks at because it seems routine. Those are the places attackers keep finding room.

The tools are getting faster, and some attacks are getting stranger, but the basic lesson is still pretty simple. Know what your systems can reach, what they are allowed to do, and which old assumptions are still hanging around. That will matter next week too.