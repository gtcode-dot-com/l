---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T03:42:17.551321+00:00'
exported_at: '2026-06-10T03:42:20.335239+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/unc3753-used-vishing-and-physical.html
structured_data:
  about: []
  author: ''
  description: UNC3753 hit dozens of U.S. firms in Jan-May 2026 using vishing and
    RMM tools, driving rapid data theft extortion.
  headline: UNC3753 Used Vishing and Physical Intrusions in U.S. Data Theft Extortion
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/unc3753-used-vishing-and-physical.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UNC3753 Used Vishing and Physical Intrusions in U.S. Data Theft Extortion Campaign
updated_at: '2026-06-10T03:42:17.551321+00:00'
url_hash: b79b6d6856efbe3648ad9f989e7f03a4a3041832
---

Cybersecurity researchers have disclosed details of a financially motivated data theft extortion campaign that has targeted dozens of organizations across professional, legal, and financial services in the U.S. between January and May 2026.

The activity has been attributed by Google Mandiant and Google Threat Intelligence Group (GTIG) to a threat actor dubbed
**UNC3753**
, which is also known as Chatty Spider, Luna Moth, and Silent Ransom Group (SRG).

"UNC3753 leverages voice phishing (vishing) and social engineering deception techniques to achieve remote access into corporate environments," researchers Chad Reams, Tufail Ahmed, Keith Knapp, Ashley Frazer, and Tyler McLellan
[said](https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms)
.

"Using pretexts such as data migration or invoice-related emails, the threat actors initiate phone conversations posing as IT support and convince targets to host screen-sharing sessions and download remote monitoring and management (RMM) utilities."

Upon gaining access, the threat actors have been found to either carry out direct searches to locate and exfiltrate files of interest or deceive the victim into carrying out the actions on their behalf. Stolen information includes proprietary legal agreements, personally identifiable information (PII), and financial records.

In some instances, the attackers have accessed victims' systems in person, echoing an
[advisory](https://thehackernews.com/2026/05/threatsday-bulletin-claude-security.html#law-firms-targeted-by-srg)
issued by the U.S. Federal Bureau of Investigation (FBI) last month. These physical intrusions involve the threat actors posing as IT technicians to enter corporate offices and attempt to steal data using removable USB media.

"By sending someone in-person to the victim's location to facilitate the intrusion, SRG actors exfiltrate data to an external hard drive or USB drive inserted by the threat actor into the victim's computer," the FBI said of the new escalation in UNC3753's capabilities.

Google said UNC3753 shares tactical overlaps with UNC2686, a threat cluster previously known for carrying out
[BazarCall-style](https://thehackernews.com/2022/10/bazarcall-callback-phishing-attacks.html)
[campaigns](https://thehackernews.com/2023/12/bazacall-phishing-scammers-now.html)
in 2021. Although the group has been observed deploying LockBit Black ransomware in the past, it has mainly focused on extortion-only operations since 2022, pressuring victims to pay up or risk getting their data published on the LEAKEDDATA data leak site.

Both UNC3753 and UNC2686 are assessed to be offshoots of the
[now-defunct Conti ransomware gang](https://thehackernews.com/2022/08/conti-cybercrime-cartel-using-bazarcall.html)
, with early iterations of the campaigns using
[subscription cancellation lures](https://thehackernews.com/2022/11/luna-moth-gang-invests-in-call-centers.html)
as part of callback phishing attacks that aim to install remote access software on victims' machines.

Beginning around March 2025, the hacking crew has impersonated internal corporate IT help desk staff to trick victims into joining a screen-sharing session on enterprise communication platforms like Zoom, Microsoft Teams, or Quick Assist under the guise of addressing a security issue helping with a corporate data migration project, effectively bypassing traditional security controls.

"The threat group frequently initializes campaigns using benign, invoice-themed email lures sent from actor-controlled consumer email accounts," Google said. "These messages contain no active links or malicious attachments. Instead, they typically contain a brief, generic message. The primary purpose of these emails is to establish a pretext, raising the target's internal security concerns so they are more susceptible to follow-up voice calls."

Once a session is established, the attackers attempt to establish a persistent foothold by guiding the victims to install legitimate remote desktop software like AnyDesk, Bomgar, SuperOps RMM, or Zoho Assist. Instructions to install these programs are shared via a legitimate service called "
[privnote[.]com](https://privnote.com/)
," which allows users to send notes that self-destruct after being read by the recipient.

UNC3753 has also been observed establishing Zoom sessions directly on targets' personal laptops to access corporate virtual desktop infrastructure (VDI) and burrow deeper into corporate file systems with the goal of enumerating local and cloud directories, crawling mapped network drives, and harvesting data from highly sensitive folders, including those related to tax filings, audits, corporate client agreements, and Social Security numbers (SSNs).

In the final stage, the captured data is sent to the threat actors via WinSCP or Rclone, or to email addresses controlled by the threat actor from the target's mailbox. This is followed by the attackers sending an extortion demand in the form of an email message, typically within 30 minutes of exiting the target environment.

The email messages give victims a three-day deadline to initiate ransom negotiations. They also threaten to call and email target employees and external clients directly to notify them of the data breach should they remain unresponsive, not to mention publish the entire stolen information on the data leak site.

In many incidents investigated by Google's threat intelligence and incident response teams, the end-to-end operation from initial contact to data extortion is said to have occurred within a single business day. The fast-tempo operational model is exemplified by the fact that the attackers initiate data searches, staging, and theft in under an hour.

"Legal services firms represent high-value targets for extortion actors. They maintain concentrated repositories of extremely sensitive client transaction files, merger and acquisition plans, client trade secrets, and corporate regulatory reports," Google said.

"Threat groups recognize that legal entities are subject to heavy reputational and regulatory exposure and may be highly motivated to resolve extortion situations quietly to protect their professional standing. Threat actors recognize that targeting the human element - specifically using voice-guided social engineering-enables them to easily bypass robust technical perimeters, web security gateways, and MFA configurations."

The findings coincide with a new report from Resecurity about the threat actor's use of
[DNS Fast Flux network infrastructure](https://www.cloudflare.com/learning/dns/dns-fast-flux/)
across various countries in Latin America, Eastern Europe, Central Asia, Middle East/Africa, East Asia, and the Caribbean to make its domains harder to block -

* business-data-leaks[.]com, the data leak site that lists close to 100 victim organizations as of June 2026
* ep6pheij[.]com, which stages the stolen data per victim

"By changing the DNS records and using short Time-To-Live (TTL) values, attackers make their malicious infrastructure resilient against takedowns," the cybersecurity company
[said](https://www.resecurity.com/blog/article/silent-ransom-group-srg-uncovering-dns-fast-flux-infrastructure)
.

"Both domains operate on a fast-flux network backed by a botnet spread across 18 countries and 22 ISPs. The two domains share 50-60% of their bot pool, confirming a single threat actor operates both. The infrastructure contains zero datacenter or hosting IPs - every node traces back to a consumer ISP (e.g., Telecentro, Mega Cable, Vodafone) and is flagged as residential or mobile IP address."