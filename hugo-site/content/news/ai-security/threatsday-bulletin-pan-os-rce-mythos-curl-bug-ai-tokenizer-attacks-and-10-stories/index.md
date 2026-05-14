---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T22:13:50.956625+00:00'
exported_at: '2026-05-14T22:13:53.271005+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html
structured_data:
  about: []
  author: ''
  description: 'Weekly ThreatsDay Bulletin: supply chain attacks, fake support lures,
    AI tampering, data leaks, ransomware, and exploited flaws.'
  headline: 'ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks,
    and 10+ Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/threatsday-bulletin-pan-os-rce-mythos.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and
  10+ Stories'
updated_at: '2026-05-14T22:13:50.956625+00:00'
url_hash: 54d0faf9d6c15eb6135cbcb940ef7af322c28350
---

**

Ravie Lakshmanan
**

May 14, 2026

Hacking News / Cybersecurity News

Everything is still on fire.

This week feels dumb in the worst way — bad links, weak checks, fake help desks, shady forum posts, and people turning supply chain attacks into some cursed little game for clout and cash. Half of it feels new. Half of it feels like crap we should have fixed years ago.

The mess keeps getting louder: users get tricked, boxes get popped, tools meant for normal work get used for bad stuff, and nobody seems shocked anymore. Great. Love that for us.

Anyway. Let’s get into it.

1. Exploited PAN-OS RCE

   Palo Alto Networks has
   [released](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html)
   the first round of fixes to address
   [CVE-2026-0300](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html)
   , a critical buffer overflow vulnerability in the User-ID Authentication Portal service of PAN-OS software that could allow an unauthenticated attacker to execute arbitrary code with root privileges by sending specially crafted packets. The company said it has observed the flaw being exploited in limited attacks since at least last month, with unknown threat actors leveraging it to drop payloads like EarthWorm and ReverseSocks5.
2. Private AI chats

   Meta has
   [announced](https://about.fb.com/news/2026/05/incognito-chat-whatsapp-meta-ai/)
   Incognito Chat with Meta AI in its namesake app and WhatsApp. Incognito Chat is "a completely private way to interact with AI, similar to how end-to-end encryption means no one can read your conversations, even Meta or WhatsApp," CEO Mark Zuckerberg said. "Incognito Chat handles all AI inference in a Trusted Execution Environment that ensures your messages are not accessible to us. The conversations on your phone also disappear when you exit the session." The feature is powered by
   [Private Processing](https://thehackernews.com/2025/04/whatsapp-launches-private-processing-to.html)
   , which already underlies its message summarization and composition tools.
3. Zero-auth data leak

   A defense technology company with Department of Defense contracts exposed user records and military training materials through API endpoints that lacked meaningful authorization checks. The issue affected Schemata, an AI-powered virtual training platform used in military and defense settings. According to
   [Strix](https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup)
   , an ordinary low-privilege account was able to access data across multiple tenants, including user listings, organization records, course information, training metadata, and direct links to documents hosted on Schemata’s Amazon Web Services instances. In a statement posted on the company’s website, Schemata
   [said](https://schemata.com/blog/security-disclosure-notice-and-response)
   it did not have "evidence that any third party exploited the vulnerability to access customer data."
4. Router update reprieve

   The U.S. Federal Communications Commission (FCC) has
   [extended](https://thehackernews.com/2026/03/fcc-bans-new-foreign-made-routers-over.html)
   the deadline for owners of banned internet routers to provide security updates to U.S.-based users by two years. In March 2026, the FCC banned the import and sale of all "consumer-grade" internet routers produced in a foreign country, citing unacceptable national security risks. In a new public notice published last week, the Commission's Office of Engineering and Technology (OET) said it is extending this deadline until "at least" January 1, 2029. That said, the extension only applies to software and firmware updates so as to ensure the continued safety of already deployed routers in the U.S. and mitigate potential harm. "These include all software and firmware updates to ensure the continued functionality of the devices, such as those that patch vulnerabilities and facilitate compatibility with different operating systems," per the
   [FCC](https://www.fcc.gov/document/oet-announces-extension-and-expansion-waivers)
   .
5. APT phishing campaign

   A new state-sponsored threat cluster dubbed Operation GriefLure has been
   [observed](https://www.seqrite.com/blog/operation-grieflure-dissecting-an-apt-campaign-targeting-vietnams-military-telecom-philippine-healthcare/)
   targeting Vietnam's telecom and the Philippines' healthcare sectors with a RAR archive distributed via spear-phishing emails to deploy a remote access trojan on compromised hosts, while leveraging credible decoy documents to give them a veneer of legitimacy and trust. The malware is capable of process enumeration, screenshot capture, file and directory listing, credential harvesting, and file execution capabilities.
6. JPEG PowerShell lure

   A multi-stage intrusion campaign has been observed leveraging a weaponized PowerShell payload disguised as a legitimate JPEG image file to deliver a trojanized instance of ConnectWise ScreenConnect to stealthy remote access. "The intrusion likely originated through social engineering techniques such as phishing emails, malicious attachments, deceptive file-sharing interactions, or fake update lures involving a malicious file named sysupdate.jpeg," CYFIRMA
   [said](https://www.cyfirma.com/research/operation-silentcanvas-jpeg-based-multistage-powershell-intrusion/)
   . "The payload was specifically crafted to exploit user trust and bypass conventional file-extension validation mechanisms while blending malicious activity with legitimate enterprise software."
7. Aid-themed infostealer

   A targeted cyber espionage campaign is leveraging social engineering and trusted infrastructure to establish persistent access to victim systems. The activity, which employs lure themes centred around humanitarian aid, is assessed to target Russian-speaking individuals or entities. "The attack is delivered via phishing emails containing a malicious LNK file disguised within a RAR archive, using a Russian humanitarian aid request form to exploit contextual trust," Cyble
   [said](https://cyble.com/blog/operation-humanitarianbait-infostealer-campaign/)
   . "Execution triggers a stealthy, multi-stage infection chain in which a decoy document is presented to the user while a heavily obfuscated, fileless (PE-less) Python-based implant is silently deployed." The payload is retrieved from GitHub Releases, allowing the operator to blend in with legitimate enterprise activity. The implant operates as a "full-spectrum surveillance platform," facilitating credential harvesting, keystroke logging, clipboard and screenshot capture, sensitive data exfiltration, and covert remote access.
8. Ransomware-like file lock

   A new proof-of-concept (PoC) tool dubbed GhostLock, created by Kim Dvash of Israel Aerospace Industries, has revealed that it's possible for a domain user with read access to a file share to deny access to files without the need for deploying any ransomware or requiring elevated privileges. "By calling CreateFileW with dwShareMode = 0x00000000 across a target share, a low-privileged user holds files in an exclusively locked state indefinitely," Dvash
   [said](https://ghostlock.io/)
   . "Other clients receive STATUS\_SHARING\_VIOLATION (0xC0000043) on every access attempt. ERP systems fail. Workflow queues stall. The impact is indistinguishable from encrypted ransomware. The attack produces none of the signals that encrypted ransomware produces." The disruptive technique is not a vulnerability, but rather documented behavior required for data integrity.
   [GhostLock](https://github.com/kimd155/ghostlock)
   affects "any organization running SMB-backed shared file infrastructure where users have standard domain credentials and network access to file shares."
9. AI scan false positives

   cURL developer Daniel Stenberg said that Anthropic Mythos model's scan of the utility five "confirmed security vulnerabilities," out of which one was a low-severity bug, while the rest were false positives. "The single confirmed vulnerability is going to end up a severity low CVE planned to get published in sync with our pending next curl release 8.21.0 in late June," Stenberg
   [said](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/)
   . "The flaw is not going to make anyone grasp for breath. All details of that vulnerability will ofcourse not get public before then, so you need to hold out for details on that." Stenberg, however, acknowledged that artificial intelligence powered code analyzers are significantly better at finding security flaws and mistakes in source code than any traditional code analyzers.
10. Fraud intel pact

    The Indian Cyber Crime Coordination Centre (I4C), along with the Ministry of Home Affairs, and Reserve Bank Innovation Hub (RBIH), have
    [signed](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2260277&reg=3&lang=2)
    a Memorandum of Understanding (MoU) to "facilitate cooperation in the areas of fraud-risk intelligence sharing, analytical support, and operational coordination for strengthening proactive fraud detection and prevention mechanisms." The goal is to combat cyber-enabled financial fraud and curtail mule accounts across the banking and digital payments ecosystem.
11. OnlyFans ransomware lure

    Attackers are enticing users seeking "free OnlyFans accounts" to download a seemingly harmless ZIP file that contains the crpx0 ransomware. The activity targets both Windows and macOS systems. "Inside that ZIP file is a small trick, a malicious shortcut disguised as something legitimate. When the user clicks it, it quietly executes hidden commands," Aryaka
    [said](https://www.aryaka.com/blog/crpx0-ransomware-multi-stage-attack/)
    . "A VBScript loader prepares the system and silently installs the components needed to run Python-based code. This is where the attack becomes more flexible. Rather than relying on a single static payload, the attackers now have a programmable environment. Once the Python script is running, it connects to a remote server." The Python-based malware allows the attackers to send commands, update the malware, or deploy new payloads. This enables system profiling, clipboard hijacking to conduct cryptocurrency theft, seed phrase harvesting, andransomware deployment.
12. ClickFix proxy access

    A new
    [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
    campaign carried out via a compromised website has been observed using scheduled tasks for persistence and
    [PySoxy](https://github.com/MisterDaneel/pysoxy/)
    , an open-source Python SOCKS5 proxy, to establish encrypted proxy access. "In the observed chain, one user-executed command led to persistence, domain reconnaissance, an initial PowerShell-based command-and-control (C2) channel, and a second C2 path through PySoxy, giving the attacker encrypted proxy access without relying on well-known malware or remote monitoring and management (RMM) tools," ReliaQuest
    [said](https://reliaquest.com/blog/threat-spotlight-clickfix-evolves-with-pysoxy-proxying/)
    . "This development shows ClickFix moving beyond one-time user execution into modular post-exploitation, where older open-source tools can create redundant access paths that are harder to classify and contain."
13. Tokenizer output hijack

    HiddenLayer has demonstrated a technique called tokenizer tampering that details how modifying the "tokenizer.json" file in Hugging Face AI models can give an attacker direct control over model output, enabling an attacker to exfiltrate sensitive data via, say, stealthy tool call injections. The attack works across Safetensors, ONNX, and GGUF formats. "Tokenizer.json ships with the model in a HuggingFace repository, as shown above, and is loaded automatically when the model is initialized for inference, making it a direct attack surface," HiddenLayer
    [said](https://www.hiddenlayer.com/research/tokenizer-tampering)
    . "This can affect conversational responses, tool-call arguments, and any other generated text, without weight modifications, adversarial input, or knowledge of the model’s architecture."
14. Teams helpdesk lure

    Threat actors are sending Microsoft Teams messages from a
    [fake IT Support account](https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html)
    to trigger an attack chain that enables remote access, malware deployment, privilege escalation, credential theft, lateral movement, and exfiltration. "By abusing Teams external access, the threat actor delivered a Dropbox-hosted Python payload [called
    [ModeloRAT](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
    ] that established command-and-control, deployed multiple backdoors, and began mapping the internal environment," Rapid7
    [said](https://www.rapid7.com/blog/post/tr-it-support-dissecting-modelorat-campaign-microsoft-teams-compromise/)
    . "The attacker then escalated privileges to SYSTEM using
    [CVE-2023-36036](https://thehackernews.com/2023/11/alert-microsoft-releases-patch-updates.html)
    before deploying a fake Windows lock screen designed to harvest the user's domain password." The attackers then moved laterally to a second host, used legitimate tooling such as DumpIt to gather system memory, and likely exfiltrated the data via an anonymous file-sharing service. ReliaQuest has
    [attributed](https://reliaquest.com/blog/threat-spotlight-help-desk-lures-drop-kongtukes-evolved-modelorat/)
    the activity to a financially motivated initial access broker (IAB) tracked as
    [KongTuke](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html)
    .
15. Supply chain contest

    The notorious threat actor known as
    [TeamPCP](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
    , which was recently linked to the compromise of
    [TanStack's npm packages](https://tanstack.com/blog/incident-followup)
    , has teamed up with Breached forum to announce a supply chain attack competition with a $1,000 prize in Monero. As part of the announcement, the Shai-Hulud worm has been open-sourced and hosted on the forum's content delivery network. While it was also
    [made available on GitHub](https://www.ox.security/blog/shai-hulud-open-source-malware-github/)
    , it has since been removed. According to
    [screenshots shared](https://x.com/DarkWebInformer/status/2054590267252940870)
    by Dark Web Informer on X, the competition rules require participants to use the worm in their attacks and submit proof that they have obtained access to a target's environment. "The biggest supply chain based on the amount of weekly/monthly downloads will win," the threat actor said. "If you compromise many small packages, it will be added up." The development marks a newfound escalation of TeamPCP's tradecraft. "The contest essentially functions as a public recruitment stunt, turning supply chain compromise into a leaderboard for lower-tier actors willing to trade risk for recognition," Socket
    [said](https://socket.dev/blog/teampcp-supply-chain-attack-contest)
    . "TeamPCP has already been positioning supply chain compromise as a way to harvest credentials, expose enterprise environments, and hand access to groups that know how to monetize it. Now it is giving forum users an open source worm, a scoring system, and a reason to rack up compromises."
16. NATS-powered C2

    An unknown threat actor has been spotted using a
    [NATS](https://github.com/nats-io/nats-server)
    server as a command-and-control (C2) channel rather than relying on traditional HTTP-based panels or chat platforms. The novel technique has been codenamed NATS-as-C2 by cloud security company Sysdig. The activity relates to the exploitation of
    [CVE-2026-33017](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html)
    , an unauthenticated remote code execution (RCE) vulnerability in Langflow. "Over roughly 30 minutes of hands-on activity, the operator at 159.89.205.184 (DigitalOcean) downloaded a Python worker and a Go binary," the company
    [said](https://www.sysdig.com/blog/nats-as-c2-inside-a-new-technique-attackers-are-using-to-harvest-cloud-credentials-and-ai-api-keys)
    . While threat actors have adopted legitimate platforms and services as covert communication channels, this is the first time NATS, a high-performance communications system, has been leveraged for this purpose.

That’s it. Attackers keep winning with simple crap: fake prompts, trusted tools, weak checks, and old systems nobody wants to fix.

Do the boring work. Patch. Change keys. Check users. Test backups. Block the obvious junk. We’ll be back when the fire moves.