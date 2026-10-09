---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-12T22:51:24.880393+00:00'
exported_at: '2025-11-12T22:54:39.976324+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/from-log4j-to-iis-chinas-hackers-turn.html
structured_data:
  about: []
  author: ''
  description: China-linked hackers exploited multiple CVEs in April 2025 to target
    global entities with advanced persistence.
  headline: From Log4j to IIS, China’s Hackers Turn Legacy Bugs into Global Espionage
    Tools
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/from-log4j-to-iis-chinas-hackers-turn.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: From Log4j to IIS, China’s Hackers Turn Legacy Bugs into Global Espionage Tools
updated_at: '2025-11-12T22:51:24.880393+00:00'
url_hash: af5e5ae81498edf5c83f0dd1e569ba622bea81cb
---

A China-linked threat actor has been attributed to a cyber attack targeting an U.S. non-profit organization with an aim to establish long-term persistence, as part of broader activity aimed at U.S. entities that are linked to or involved in policy issues.

The organization, according to a
[report](https://www.security.com/threat-intelligence/china-apt-us-policy)
from Broadcom's Symantec and Carbon Black teams, is "active in attempting to influence U.S. government policy on international issues." The attackers managed to gain access to the network for several weeks in April 2025.

The first sign of activity occurred on April 5, 2025, when mass scanning efforts were detected against a server by leveraging various well-known exploits, including
[CVE-2022-26134](https://nvd.nist.gov/vuln/detail/cve-2022-26134)
(Atlassian),
[CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228)
(Apache Log4j),
[CVE-2017-9805](https://nvd.nist.gov/vuln/detail/cve-2017-9805)
(Apache Struts), and
[CVE-2017-17562](https://nvd.nist.gov/vuln/detail/cve-2017-17562)
(GoAhead Web Server).

Symantec and Carbon Black told The Hacker News that there is no indication that these exploitation efforts were successful. It's suspected that the attackers ultimately gained initial access with a brute-force or credential stuffing attack.

No further actions were recorded until April 16, when the attacks executed several curl commands to test internet connectivity, after which the Windows command-line tool netstat was executed to collect network configuration information. This was followed by setting up persistence on the host by means of a scheduled task.

The task was designed to execute a legitimate Microsoft binary "msbuild.exe" to run an unknown payload, as well as create another scheduled task that's configured to run every 60 minutes as a high-privileged SYSTEM user.

This new task, Symantec and Carbon Black said, was capable of loading and injecting unknown code into "csc.exe" that ultimately established communications with a command-and-control (C2) server ("38.180.83[.]166"). Subsequently, the attackers were observed executing a custom loader to unpack and run an unspecified payload, likely a remote access trojan (RAT) in memory.

Also observed was the execution of the legitimate Vipre AV component ("vetysafe.exe") to sideload a DLL loader ("sbamres.dll"). This component is also said to have been used for DLL side-loading in connection with
[Deed RAT](https://thehackernews.com/2025/10/hackers-used-snappybee-malware-and.html)
(aka
[Snappybee](https://thehackernews.com/2024/11/chinese-hackers-use-ghostspider-malware.html)
) in prior activity attributed to Salt Typhoon (aka Earth Estries), and in attacks attributed to
[Earth Longzhi](https://thehackernews.com/2024/06/chinese-state-backed-cyber-espionage.html)
, a sub-cluster of
[APT41](https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html)
.

"A copy of this malicious DLL was previously used in attacks linked to the China-based threat actors known as
[Space Pirates](https://thehackernews.com/2023/08/researchers-expose-space-pirate-cyber.html)
," Broadcom said. "A variant of this component, with a different filename, was also used by that Chinese APT group Kelp (aka Salt Typhoon) in a separate incident."

Some of the other tools observed in the targeted network included Dcsync and Imjpuexc. It's not clear how successful the attackers were in their efforts. No additional activity was registered after April 16, 2025.

"It is clear from the activity on this victim that the attackers were aiming to establish a persistent and stealthy presence on the network, and they were also very interested in targeting domain controllers, which could potentially allow them to spread to many machines on the network," Symantec and Carbon Black said.

"The sharing of tools among groups has been a long-standing trend among Chinese threat actors, making it difficult to say which specific group is behind a set of activities."

The disclosure comes as a security researcher who goes by the online moniker BartBlaze
[disclosed](https://bartblaze.blogspot.com/2025/10/earth-estries-alive-and-kicking.html)
Salt Typhoon's exploitation of a security flaw in WinRAR (
[CVE-2025-8088](https://thehackernews.com/2025/08/winrar-zero-day-under-active.html)
) to initiate an attack chain that
[sideloads a DLL](https://www.virustotal.com/gui/file/5e062fee5b8ff41b7dd0824f0b93467359ad849ecf47312e62c9501b4096ccda/community)
responsible for running shellcode on the compromised host. The final payload is designed to establish contact with a remote server ("mimosa.gleeze[.]com").

### Activity from Other Chinese Hacking Groups

According to a report from ESET, China-aligned groups have
[continued](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html)
to remain active, striking entities across Asia, Europe, Latin America, and the U.S. to serve Beijing's geopolitical priorities. Some of the notable campaigns include -

* The targeting of the energy sector in Central Asia by a threat actor codenamed
  [Speccom](https://thehackernews.com/2021/07/indigozebra-apt-hacking-campaign.html)
  (aka IndigoZebra or SMAC) in July 2025 via phishing emails to deliver a variant of
  [BLOODALCHEMY](https://thehackernews.com/2024/05/japanese-experts-warn-of-bloodalchemy.html)
  and custom backdoors such as kidsRAT and RustVoralix.
* The targeting of European organizations by a threat actor codenamed
  [DigitalRecyclers](https://thehackernews.com/2025/05/chinese-hackers-deploy-marssnake.html)
  in July 2025, using an unusual persistence technique that involved the use of the
  [Magnifier accessibility tool](https://oddvar.moe/2018/07/23/another-way-to-get-to-a-system-shell/)
  to gain SYSTEM privileges.
* The targeting of governmental entities in Latin America (Argentina, Ecuador, Guatemala, Honduras, and Panama) between June and September 2025 by a threat actor codenamed
  [FamousSparrow](https://thehackernews.com/2025/03/new-sparrowdoor-backdoor-variants-found.html)
  that likely exploited
  [ProxyLogon](https://thehackernews.com/2021/03/microsoft-exchange-cyber-attack-what-do.html)
  flaws in Microsoft Exchange Server to deploy SparrowDoor.
* The targeting of a Taiwanese company in the defense aviation sector, a U.S. trade organization based in China, and the China-based offices of a Greek governmental entity, and an Ecuadorian government body between May and September 2025 by a threat actor codenamed
  [SinisterEye](https://thehackernews.com/2022/06/chinese-luoyu-hackers-using-man-on-side.html)
  (aka LuoYu and Cascade Panda) to deliver malware like WinDealer (for Windows) and SpyDealer (for Android) using adversary-in-the-middle (AitM) attacks to hijack legitimate software update mechanisms.
* The targeting of a Japanese company and a multinational enterprise, both in Cambodia, in June 2025 by a threat actor codenamed
  [PlushDaemon](https://thehackernews.com/2025/01/plushdaemon-apt-targets-south-korean.html)
  by means of AitM poisoning to deliver SlowStepper.

"PlushDaemon achieves AitM positioning by compromising network devices such as routers, and deploying a tool that we have named EdgeStepper, which redirects DNS traffic from the targeted network to a remote, attacker-controlled DNS server," ESET said.

"This server responds to queries for domains associated with software update infrastructure with the IP address of the web server that performs the update hijacking and ultimately serves PlushDaemon's flagship backdoor, SlowStepper."

### Chinese Hacking Groups Target Misconfigured IIS Servers

In recent months, threat hunters have also spotted a Chinese-speaking threat actor targeting misconfigured IIS servers using
[publicly exposed machine keys](https://thehackernews.com/2025/02/microsoft-identifies-3000-publicly.html)
to install a backdoor called TOLLBOOTH (aka HijackServer) that comes with SEO cloaking and web shell capabilities.

"REF3927 abuses publicly disclosed ASP.NET machine keys to compromise IIS servers and deploy TOLLBOOTH SEO cloaking modules globally," Elastic Security Labs researchers
[said](https://www.elastic.co/security-labs/tollbooth)
in a report published late last month. Per HarfangLab, the operation has infected hundreds of servers around the world, with infections concentrated in India and the U.S.

The attacks are also characterized by attempts to weaponize the initial access to drop the Godzilla web shell, execute GotoHTTP remote access tool, use Mimikatz to harvest credentials, and deploy HIDDENDRIVER, a modified version of the open source rootkit
[Hidden](https://github.com/JKornev/hidden)
, to conceal the presence of malicious payloads on the infected machine.

|  |
| --- |
|  |
| REF3927 attack pattern and TOLLBOOTH SEO cloaking workflow |

It's worth pointing out that the cluster is the latest addition to a long list of Chinese threat actors, such as
[GhostRedirector](https://thehackernews.com/2025/09/ghostredirector-hacks-65-windows.html)
,
[Operation Rewrite](https://thehackernews.com/2025/09/badiis-malware-spreads-via-seo.html)
, and
[UAT-8099](https://thehackernews.com/2025/10/chinese-cybercrime-group-runs-global.html)
, that have targeted IIS servers, indicating a surge in such activity.

"While the malicious operators appear to be using Chinese as their main language and leveraging the compromises to support search engine optimization (SEO), we notice that the deployed module offers a persistent and unauthenticated channel which allows any party to remotely execute commands on affected servers," the French cybersecurity company
[said](https://harfanglab.io/insidethelab/rudepanda-owns-iis-servers-like-2003/)
.

*(The story was updated after publication to include a response from Symantec and Carbon Black.)*