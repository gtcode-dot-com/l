---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-17T06:19:00.665747+00:00'
exported_at: '2026-09-17T06:19:02.058721+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html
structured_data:
  about: []
  author: ''
  description: UAT-10147 targets Windows and Linux servers with known flaws and AI
    tools, deploying malware for SEO fraud and data theft.
  headline: UAT-10147 Uses AI to Scale Server Attacks, Deploys SPECTRE With EDR Bypass
    and Linux Rootkit
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UAT-10147 Uses AI to Scale Server Attacks, Deploys SPECTRE With EDR Bypass
  and Linux Rootkit
updated_at: '2026-09-17T06:19:00.665747+00:00'
url_hash: 55c3f66451ed5e0a0786ec27e94f49cc7f364569
---

Cybersecurity researchers have disclosed details of a Chinese-speaking cybercrime group dubbed
**UAT-10147**
that's targeting Windows and Linux web servers globally across the education, media, technology, and gaming sectors.

The vast majority of the targets are located in Brazil, Bolivia, China, Canada, and Vietnam. Details of the threat activity came to light following the discovery of an open directory hosted at "139.180.197[.]150," which was observed communicating with one of the compromised machines.

"The actor leveraged publicly disclosed vulnerabilities to gain initial access at scale," Cisco Talos
[said](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/)
in a two-part report published last week. The actor employed a mixture of open-source offensive frameworks, including
[Metasploit](https://docs.metasploit.com/)
,
[ysoserial](https://github.com/pwntester/ysoserial.net)
,
[PentestGPT](https://pentestgpt.com/)
, DeepAudit, and multiple privilege escalation exploits to automate intrusion operations and establish persistence."

UAT-10147 has been described as a threat actor that conducts search engine optimization (SEO) fraud and data theft, while integrating artificial intelligence (AI)-powered tools at various phases of the attack cycle to facilitate exploitation, reconnaissance, payload generation, validation, and persistence.

Specifically, this involves using AI to refine exploits, troubleshoot logic, automate post-exploitation workflows, validate exploits, and generate operational documentation, indicating an attempt to implement offensive tradecraft at scale.

An analysis of the exposed directory has identified a text file containing a target list with approximately 170,000 URLs, with the attacker splitting it into 17 smaller files containing about 10,000 URLs each to more efficiently parse the set. The top five destinations based on the target list consist of the U.S., India, the U.K., Germany, and the Netherlands.

Attack chains involve exploiting known flaws to achieve remote code execution (RCE) on a website or a vulnerable IIS server, and then run an automated script to install and deploy malware for SEO fraud or data stealing. Select instances entail the deployment of a web shell, which then paves the way for
[BadIIS](https://thehackernews.com/2026/01/china-linked-uat-8099-targets-iis.html)
and additional backdoors for persistent access.

Some of the other steps undertaken by UAT-10147 are as follows -

* Using a batch script that employs certutil to download a privilege escalation tool ("EfsPotato"), a secondary batch script, and Quasar RAT from a remote server ("adminapi.tippusoni[.]in")
* Using EfsPotato to gain elevated system privileges, configure Microsoft Defender exclusions
* Deleting initial payloads to cover its tracks and thwart forensic analysis
* Deploying follow-on implants like
  [Gh0stCringe](https://thehackernews.com/2025/06/silver-fox-apt-targets-taiwan-with.html)
  and a previously unreported cross-platform implant dubbed SPECTRE
* Using the secondary batch script to silently execute Quasar RAT and establish persistence using a deceptive scheduled task named "Google Chrome Start"
* Abusing the elevated privileges to download a third batch script, which then installs BadIIS

Interestingly, the core BadIIS malware is the same specific variant that's known to operate under a
[malware-as-a-service (MaaS) model](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)
and is used by multiple Chinese-speaking cybercrime groups.

The Linux attacks, like in the case, leverage various known vulnerabilities to obtain an initial foothold, followed by abusing various known Local Privilege Escalation (LPE) exploits to escalate to root, including
[CVE-2022-0995](https://nvd.nist.gov/vuln/detail/CVE-2022-0995)
,
[CVE-2021-3156](https://nvd.nist.gov/vuln/detail/CVE-2021-3156)
,
[CVE-2015-5287](https://nvd.nist.gov/vuln/detail/CVE-2015-5287)
,
[CVE-2015-3246](https://nvd.nist.gov/vuln/detail/CVE-2015-3246)
,
[CVE-2010-3904](https://nvd.nist.gov/vuln/detail/CVE-2010-3904)
, and
[CVE-2022-0847](https://nvd.nist.gov/vuln/detail/CVE-2022-0847)
.

Once root-level access is unlocked, the threat actor has been observed deploying multiple backdoors like
[Noodle RAT](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html)
(a variant of Gh0st RAT and Rekoobe), SPECTRE, and Meterpreter to enable outbound connections to remote command-and-control (C2) infrastructure. Some of the vulnerabilities weaponized by the threat actor over the course of the campaign include
[CVE-2022-27925](https://nvd.nist.gov/vuln/detail/CVE-2022-27925)
(Zimbra),
[CVE-2021-23758](https://nvd.nist.gov/vuln/detail/CVE-2021-23758)
(AjaxPro),
[CVE-2019-18935](https://nvd.nist.gov/vuln/detail/cve-2019-18935)
(Telerik UI for ASP.NET AJAX),
[CVE-2021-29441](https://nvd.nist.gov/vuln/detail/CVE-2021-29441)
, and
[CVE-2021-29442](https://nvd.nist.gov/vuln/detail/CVE-2021-29442)
(Alibaba Nacos).

"By routing exfiltrated data to a legitimate cloud-based configuration management service, the attackers effectively blend their traffic with normal administrative operations," Talos researcher Joey Chen said. "This infrastructure choice acts as an asynchronous exfiltration sink, allowing the adversaries to poll their own Nacos instance to verify successful exploitation across victims without the operational overhead or detection risk of establishing a persistent reverse shell or maintaining direct inbound connections."

A notable aspect of UAT-10147's tradecraft concerns an AI-driven framework called DeepAudit for vulnerability scanning. Talos said it found no evidence of the threat actor exploiting vulnerabilities discovered by the tool in victim environments, although it was left accessible on the management server.

This has raised the possibility that the attackers are planning on using DeepAudit to identify vulnerabilities within target environments. Conversely, it's also likely that it could be used to improve their own defensive posture by proactively auditing their own infrastructure and tooling to prevent potential exposure and compromise by other threat actors.

UAT-10147 has also been found to install PentestGPT, an open-source autonomous pentesting framework, on their C2 server to scan web servers and execute relevant proof-of-concept exploits. In one case, the threat actor is said to have successfully exploited a website and collected information about the victim host using Linux commands.

Another AI-oriented tool put to use by the threat actor is an ASP.NET ViewState deserialization remote code execution guide, which delves into the following aspects -

* Making use of the
  [badsecrets](https://github.com/blacklanternsecurity/badsecrets)
  library comprising publicly known or leaked
  [ASP.NET MachineKey configurations](https://thehackernews.com/2025/07/gold-melody-iab-exploits-exposed-aspnet.html)
  , checks the key's validity, employs ysoserial.net to build malicious deserialization payloads that bypass View State protection using the pre-exposed MachineKey, and achieves code execution
* Conducting systematic reconnaissance following code execution via PowerShell to collect system information, privilege tokens, web directory listings, IIS site configurations, network interface data, and running processes, and exfiltrate them to a remote webhook
* Establishing persistent interactive access using SPECTRE, or alternatively, writing an ASHX web shell to the IIS webroot and a PowerShell TCP reverse shell
* Elevating privileges from IIS AppPool identity to SYSTEM using the Potato family of tools or SPECTRE through a built-in routine named "spectre\_potato()"

Four other AI-generated tools used by UAT-10147 are Python scripts: One which acts as a post-exploitation diagnostic utility to troubleshoot, among other things, web shell write failures, while the second uses the ViewState deserialization primitive to download and launch the SPECTRE implant.

The third script deploys the ASHX web shell onto the compromised IIS server via the same deserialization mechanism. The final script is responsible for blending exfiltration traffic with legitimate software-as-a-service (SaaS) traffic over HTTPS and transmitting webfoot enumeration, IIS site inventory, and privilege assessment details to a webhook endpoint.

SPECTRE, per Talos, is a cross-platform backdoor written in C that features obfuscation and anti-analysis techniques to fly under the radar. It communicates with a C2 server using HTTPS and supports as many as 45 commands that grant the operator extensive control over the infected endpoint. The first use of the implant by the threat actor dates back to April 2026.

"The newly identified SPECTRE implant represents a significant evolution in commodity intrusion tooling, integrating cross-platform command-and-control (C2) operations, process injection, credential theft, anti-analysis protections, and kernel-level endpoint detection and response (EDR) bypass functionality," Talos
[said](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/)
.

The Windows version is equipped to perform file operations, record keystrokes, take screenshots, download/upload files, execute shell commands, get running processes, terminate a specific process, get system information, set beacon sleep interval, modify file timestamps, inject shellcode, use
[process hollowing](https://attack.mitre.org/techniques/T1055/012/)
and
[Early Bird APC](https://kpmg.co.il/technologyconsulting/blog/earlybird-technique-an-advanced-malware-evasion-strategy)
[injection](https://attack.mitre.org/techniques/T1055/004/)
, kill EDR processes using the bring your own vulnerable driver (
[BYOVD](https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html)
) technique, and delete itself from the host.

The BYOVD attack utilizes two well-known vulnerable drivers MSI's "RTCore64.sys" (
[CVE-2019-16098](https://nvd.nist.gov/vuln/detail/cve-2019-16098)
) and Dell's "DBUtil\_2\_3.sys" (
[CVE-2021-21551](https://nvd.nist.gov/vuln/detail/cve-2021-21551)
) to obtain elevated privileges and terminate security-related processes.

SPECTRE's Linux variant follows more or less the same pattern, running a series of anti-sandbox checks before setting up a C2 connection. Both versions employ a weighted scoring mechanism that causes the program to self-terminate if the score exceeds 50 points. The evaluation is based on process name blocklists, RAM capacity, CPU core count, disk space, sleep acceleration detection, and common sandbox host names and usernames.

The Linux version's instruction set, in contrast, only supports 29 commands that encompass file system manipulation, system and process reconnaissance, agent management, and unrestricted shell execution. Its most potent capability is an integrated kernel-level rootkit dubbed Specter that's deployed as a kernel module.

It's suspected that the rootkit was developed using a combination of AI-assisted development and human expertise, given the presence of descriptive source code comments, uniform decorative separators to explain each function, and the presence of multiple methods to achieve the same purpose – something that AI models are known to generate when prompted to be thorough, as opposed to just implementing the most effective method.

"This architecture grants the threat actor persistent, kernel-level control of the compromised host that survives both reboots and most user-level security controls," Talos said. "The SPECTRE backdoor loads the Linux Kernel rootkit, Specter, to prevent detection from security products."