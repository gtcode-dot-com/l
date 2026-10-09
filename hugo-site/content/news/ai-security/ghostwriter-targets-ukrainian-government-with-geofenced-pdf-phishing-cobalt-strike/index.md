---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T22:13:51.295397+00:00'
exported_at: '2026-05-14T22:13:53.266413+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html
structured_data:
  about: []
  author: ''
  description: Ghostwriter’s March 2026 Ukraine attacks use PDF lures and geofencing
    to deploy Cobalt Strike on government targets.
  headline: Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing,
    Cobalt Strike
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Ghostwriter Targets Ukrainian Government With Geofenced PDF Phishing, Cobalt
  Strike
updated_at: '2026-05-14T22:13:51.295397+00:00'
url_hash: cb45df31e3e4e1f4819c3a1dce6d71ce507e0673
---

The Belarus-aligned threat group known as
**[Ghostwriter](https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html)**
has been attributed to a fresh set of attacks targeting governmental organizations in Ukraine.

Active since at least 2016, Ghostwriter has been linked to both cyber espionage and influence operations targeting neighboring countries, particularly Ukraine. It's also tracked under the monikers FrostyNeighbor, PUSHCHA, Storm-0257, TA445, UAC‑0057, Umbral Bison (formerly RepeatingUmbra), UNC1151, and White Lynx.

"FrostyNeighbor has been running continual cyber operations, changing and updating its toolset regularly, updating its compromise chain and methods to evade detection – targeting victims located in Eastern Europe," ESET
[said](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)
in a report shared with The Hacker News.

Previous attacks mounted by the hacking crew have leveraged a malware family known as
[PicassoLoader](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html)
, which then acts as a conduit for Cobalt Strike Beacon and njRAT. In late 2023, the threat actor was also
[observed](https://thehackernews.com/2023/11/experts-uncover-darkcasino-new-emerging.html)
weaponizing a vulnerability in WinRAR (
[CVE-2023-38831](https://thehackernews.com/2023/09/ukraines-cert-thwarts-apt28s.html)
, CVSS score: 7.8) to deploy PicassoLoader and Cobalt Strike.

As recently as last year, Polish entities were at the receiving end of a phishing campaign orchestrated by Ghostwriter that
[exploited](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q2-2025-q3-2025/)
a cross-site flaw in Roundcube (
[CVE-2024-42009](https://thehackernews.com/2025/06/cisa-adds-erlang-ssh-and-roundcube.html)
, CVSS score: 9.3) to run malicious JavaScript responsible for capturing email login credentials.

In at least some cases, the threat actors are said to have leveraged the harvested credentials to analyze mailbox contents, download the contact list, and abuse the compromised account to propagate more phishing messages, per a
[report](https://cert.pl/en/posts/2025/06/unc1151-campaign-roundcube/)
from CERT Polska in June 2025. Towards the end of 2025, the group also
[began to incorporate](https://strikeready.com/blog/captch-ya-if-you-can/)
an anti-analysis technique where lure documents relied on dynamic CAPTCHA checks to trigger the attack chain.

"FrostyNeighbor remains a persistent and adaptive threat actor, demonstrating a high level of operational maturity with the use of diverse lure documents, evolving lure and downloader variants, and new delivery mechanisms," ESET researcher Damien Schaeffer said. "This newest compromise chain that we detected is a continuation of the group's willingness to update and renew its arsenal, trying to evade detection to compromise its targets."

The latest set of activities, observed since March 2026, involves using links in malicious PDFs sent via spear-phishing attachments to target government entities in Ukraine, ultimately resulting in the deployment of a JavaScript version of PicassoLoader to drop Cobalt Strike. The PDF decoy documents have been found to impersonate the Ukrainian telecommunications company Ukrtelecom.

The infection sequence incorporates a geofencing check, serving a benign PDF file to victims whose IP address does not correspond to Ukraine. The embedded link in the PDF document is used to deliver a RAR archive containing a JavaScript payload that displays a lure document to keep up the ruse, while simultaneously launching PicassoLoader in the background.

The downloader is also designed to profile and fingerprint the compromised host, based on which the operators may manually decide to send a third-stage JavaScript dropper for Cobalt Strike Beacon. The system fingerprint is transmitted to attacker-controlled infrastructure every 10 minutes, allowing the threat actor to assess whether the victim is of interest.

The activity primarily appears to center around military, defense sector, and governmental organizations in Ukraine, whereas the victimology in Poland and Lithuania is much broader, targeting industrial and manufacturing, healthcare and pharmaceuticals, logistics, and government sectors.

"FrostyNeighbor remains a persistent and adaptive threat actor, demonstrating a high level of operational maturity with the use of diverse lure documents, evolving lure and downloader variants, and new delivery mechanisms," ESET said. "The payload is only delivered after server-side victim validation, combining automated checks of the requesting user agent and IP address with the manual validation by the operators."

### Gamaredon Delivers GammaDrop and GammaLoad in Ukraine Attacks

The disclosure comes as the Russia-affiliated
[Gamaredon](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html)
hacking group has been tied to a spear-phishing campaign targeting Ukrainian state institutions since September 2025, with an aim to deliver
[GammaDrop](https://thehackernews.com/2025/12/warning-winrar-vulnerability-cve-2025.html)
and
[GammaLoad](https://blog.synapticsystems.de/gamaredon-now-downloading-via-windows-updates-best-friend/)
downloader
[malware](https://thehackernews.com/2024/12/hackers-leveraging-cloudflare-tunnels.html)
through RAR archives that exploit
[CVE-2025-8088](https://nvd.nist.gov/vuln/detail/CVE-2025-8088)
.

"These emails – spoofed or sent from compromised government accounts – deliver persistent, multi-stage VBScript downloaders that profile the infected system," HarfangLab
[said](https://harfanglab.io/insidethelab/gamaredon-gammadrop-gammaload/)
. "There is little technical novelty here, but Gamaredon has never relied on sophistication. The group's strength lies in its relentless operational tempo and scale."

### Russia Targeted by BO Team and Hive0117

The findings also follow a report from Kaspersky that the pro-Ukraine hacktivist group known as
[BO Team](https://thehackernews.com/2025/09/new-coldriver-malware-campaign-joins-bo.html)
(aka Black Owl) may be working with
[Head Mare](https://thehackernews.com/2026/04/phantomcore-exploits-trueconf.html)
(aka PhantomCore) in attacks aimed at Russian organizations, citing overlapping infrastructure and tools. Attacks orchestrated by the BO Team in 2026 have employed spear-phishing to serve BrockenDoor and ZeronetKit, the latter of which is capable of also compromising Linux systems.

Also observed in these attacks is a previously undocumented Go-based backdoor referred to as ZeroSSH that can execute arbitrary commands using "cmd.exe" and establish a reverse SSH channel. As many as 20 organizations have been targeted by the BO Team in the first quarter of 2026.

"The nature of the interaction between the groups remains unclear, but the recorded intersections of tools and infrastructure indicate at least the potential coordination of actions against Russian organizations," Kaspersky
[said](https://securelist.ru/tr/boteam-campaign-zeronetkit-headmare/115429/)
.

In recent months, Russian enterprises have also been targeted by a financially motivated group called
[Hive0117](https://thehackernews.com/2025/05/darkwatchman-sheriff-malware-hit-russia.html)
to steal over 14 million rubles by breaking into accountants' computers via phishing campaigns and disguising transfers as salary payments. The phishing emails were sent to more than 3,000 Russian organizations between February and March 2026, per F6.

Besides Russia, the activity has also targeted users from Lithuania, Estonia, Belarus, and Kazakhstan. The attacks employ invoice-themed lures to distribute RAR archives that contain malicious files to drop DarkWatchman, a remote access trojan attributed to the group.

"Using remote access to online banking systems via compromised accountants' computers, they initiated payments to be credited to bank accounts listed in the registry," F6
[said](https://www.f6.ru/media-center/press-releases/hive0117-attacks-accountants/)
. "Formerly, this looked like a payroll transfer, but the registry listed the bank accounts of mules. If such payment transactions did not go through anti-fraud systems, the attackers were able to withdraw significant amounts from the companies' accounts."