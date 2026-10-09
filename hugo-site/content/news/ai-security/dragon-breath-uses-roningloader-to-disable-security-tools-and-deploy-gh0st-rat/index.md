---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-17T16:57:41.691868+00:00'
exported_at: '2025-11-17T16:57:44.850104+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html
structured_data:
  about: []
  author: ''
  description: Gh0st RAT spreads through Dragon Breath and large-scale impersonation
    campaigns using multi-stage loaders and evasive NSIS installers targeting Chines
  headline: Dragon Breath Uses RONINGLOADER to Disable Security Tools and Deploy Gh0st
    RAT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Dragon Breath Uses RONINGLOADER to Disable Security Tools and Deploy Gh0st
  RAT
updated_at: '2025-11-17T16:57:41.691868+00:00'
url_hash: 48b57cec3a5900f4169a34e3ea5a497dc6944f29
---

The threat actor known as
**Dragon Breath**
has been observed making use of a multi-stage loader codenamed RONINGLOADER to deliver a modified variant of a remote access trojan called Gh0st RAT.

The campaign, which is primarily aimed at Chinese-speaking users, employs trojanized NSIS installers masquerading as legitimate like Google Chrome and Microsoft Teams, according to Elastic Security Labs.

"The infection chain employs a multi-stage delivery mechanism that leverages various evasion techniques, with many redundancies aimed at neutralising endpoint security products popular in the Chinese market," security researchers Jia Yu Chan and Salim Bitam
[said](https://www.elastic.co/security-labs/roningloader)
. "These include bringing a legitimately signed driver, deploying custom WDAC policies, and tampering with the Microsoft Defender binary through
[PPL](https://thehackernews.com/2025/08/researchers-detail-windows-epm.html)
[Protected Process Light] abuse."

Dragon Breath, also known as APT-Q-27 and Golden Eye, was
[previously highlighted](https://thehackernews.com/2023/05/dragon-breath-apt-group-using-double.html)
by Sophos in May 2023 in connection with a campaign that leveraged a technique called double-dip DLL side-loading in attacks targeting users in the Philippines, Japan, Taiwan, Singapore, Hong Kong, and China.

The hacking group, assessed to be active since at least 2020, is linked to a larger Chinese-speaking entity tracked as Miuuti Group that's known for attacking the online gaming and gambling industries.

In the latest campaign documented by Elastic Security Labs, the malicious NSIS installers for trusted applications act as a launchpad for two more embedded NSIS installers, one of which ("letsvpnlatest.exe") is benign and installs the legitimate software. The second NSIS binary ("Snieoatwtregoable.exe") is responsible for stealthily triggering the attack chain.

This involves delivering a DLL and an encrypted file ("tp.png"), with the former used to read the contents of the supposed PNG image and extract shellcode designed to launch another binary in memory.

RONINGLOADER, besides attempting to remove any userland hooks by loading a fresh new "
[ntdll.dll](https://thehackernews.com/2022/12/guloader-malware-utilizing-new.html)
," tries to elevate its privileges by using the
[runas](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v%3Dws.11))
command and scans a list of running processes for hard-coded antivirus-related solutions, such as Microsoft Defender Antivirus, Kingsoft Internet Security, Tencent PC Manager, and Qihoo 360 Total Security.

The malware then proceeds to terminate those identified processes. In the event the identified process is associated with Qihoo 360 Total Security (e.g., "360tray.exe," "360Safe.exe," or "ZhuDongFangYu.exe"), it takes a different approach. This step involves the following sequence of actions -

* Block all network communication by changing the firewall
* Inject shellcode into the process (vssvc.exe) associated with the Volume Shadow Copy (VSS) service, but not before granting itself the
  [SeDebugPrivilege](https://thehackernews.com/2025/04/pipemagic-trojan-exploits-windows-clfs.html)
  token
* Start the VSS service and get its process ID
* Inject shellcode into the VSS service process using the technique called
  [PoolParty](https://thehackernews.com/2023/12/new-poolparty-process-injection.html)
* Load and make use of a signed driver named "ollama.sys" to terminate the three processes by means of a temporary service called "xererre1"
* Restore the firewall settings

For other security processes, the loader directly writes the driver to disk and creates a temporary service called "ollama" to load the driver, perform process termination, and stop and delete the service.

|  |
| --- |
|  |
| RONINGLOADER Execution flow |

Once all security processes have been killed on the infected host, RONINGLOADER runs batch scripts to bypass User Account Control (UAC) and create firewall rules to block inbound and outbound connections associated with Qihoo 360 security software.

The malware has also been observed using two techniques documented earlier this year by security researcher Zero Salarium that abuse
[PPL](https://www.zerosalarium.com/2025/08/countering-edrs-with-backing-of-ppl-protection.html)
and the Windows Error Reporting ("WerFaultSecure.exe") system (aka
[EDR-Freeze](https://www.zerosalarium.com/2025/09/EDR-Freeze-Puts-EDRs-Antivirus-Into-Coma.html)
) to disable Microsoft Defender Antivirus. Furthermore, it targets Windows Defender Application Control (WDAC) by writing a malicious policy that explicitly blocks Chinese security vendors Qihoo 360 Total Security and Huorong Security.

The end goal of the loader is to inject a rogue DLL into "regsvr32.exe," a legitimate Windows binary, to conceal its activity and launch a next-stage payload into another legitimate, high-privilege system process like "TrustedInstaller.exe" or "elevation\_service.exe." The final malware deployed is a modified version of Gh0st RAT.

The trojan is designed to communicate with a remote server to fetch additional instructions that allow it to configure Windows Registry keys, clear Windows Event logs, download and execute files from provided URLs, alter clipboard data, run commands via "cmd.exe," inject shellcode into "svchost.exe," and execute payloads dropped to disk. The variant also implements a module that captures keystrokes, clipboard contents, and foreground window titles.

### Brand Impersonation Campaigns Target Chinese Speakers with Gh0st RAT

The disclosure comes as Palo Alto Networks Unit 42
[said](https://unit42.paloaltonetworks.com/impersonation-campaigns-deliver-gh0st-rat/)
it identified two interconnected malware campaigns that have employed "large-scale brand impersonation" to deliver Gh0st RAT to Chinese-speaking users. The activity has not been attributed to any known threat actor or group.

While the first campaign – named Campaign Trio – took place between February and March 2025 by mimicking i4tools, Youdao, and DeepSeek across over 2,000 domains, the second campaign, detected in May 2025, is said to have been more sophisticated, impersonating more than 40 applications, including QQ Music and Sogou browser. The second wave has been codenamed Campaign Chorus.

"From the first campaign to the second, the adversary advanced from simple droppers to complex, multi-stage infection chains that misuse legitimate, signed software to bypass modern defenses," security researchers Keerthiraj Nagaraj, Vishwa Thothathri, Nabeel Mohamed, and Reethika Ramesh said.

The domains have been found to host ZIP archives containing the trojanized installers, ultimately paving the way for the deployment of Gh0st RAT. The second campaign, however, not only leverages more software programs as lures to reach a wider demographic of Chinese speakers, but also employs an "intricate and elusive" infection chain using intermediary redirection domains to fetch the ZIP archives from public cloud service buckets.

|  |
| --- |
|  |
| Campaign Chorus Attack Chain |

In doing so, the approach can bypass network filters that are capable of blocking traffic from unknown domains, not to mention the threat actor's operational resilience. The MSI installer, in this case, also runs an embedded Visual Basic Script that's responsible for decrypting and launching the final payload by means of
[DLL side-loading](https://attack.mitre.org/techniques/T1574/001/)
.

"The parallel operation of both old and new infrastructure through sustained activity suggests an operation that is not merely evolving but consists of multiple infrastructures and distinct tool sets simultaneously," the researchers said. "This could indicate A/B testing of TTPs, targeting different victim sets with different levels of complexity, or simply a cost-effective strategy of continuing to leverage older assets as long as they remain effective."