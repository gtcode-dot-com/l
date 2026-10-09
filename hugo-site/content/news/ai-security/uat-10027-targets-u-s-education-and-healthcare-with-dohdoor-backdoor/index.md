---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-03T03:24:57.561391+00:00'
exported_at: '2026-03-03T03:24:59.303910+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/uat-10027-targets-us-education-and.html
structured_data:
  about: []
  author: ''
  description: Cisco Talos tracks UAT-10027 targeting U.S. education and healthcare
    with Dohdoor DoH-based backdoor and Cobalt Strike payload.
  headline: UAT-10027 Targets U.S. Education and Healthcare with Dohdoor Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/uat-10027-targets-us-education-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UAT-10027 Targets U.S. Education and Healthcare with Dohdoor Backdoor
updated_at: '2026-03-03T03:24:57.561391+00:00'
url_hash: f1d7c8934a68011067d289d11abce74547c4c085
---

**

Ravie Lakshmanan
**

Feb 26, 2026

Malware / Threat Intelligence

A previously undocumented threat activity cluster has been attributed to an ongoing malicious campaign targeting education and healthcare sectors in the U.S. since at least December 2025.

The campaign is being tracked by Cisco Talos under the moniker
**UAT-10027**
. The end goal of the attacks is to deliver a never-before-seen backdoor codenamed Dohdoor.

"Dohdoor utilizes the DNS-over-HTTPS (DoH) technique for command-and-control (C2) communications and has the ability to download and execute other payload binaries reflectively," security researchers Alex Karkins and Chetan Raghuprasad
[said](https://blog.talosintelligence.com/new-dohdoor-malware-campaign/)
in a technical report shared with The Hacker News.

Although the initial access vector used in the campaign is currently not known, it's suspected to involve the use of social engineering phishing techniques, leading to the execution of a PowerShell script.

The script then proceeds to download and run a Windows batch script from a remote staging server, which, for its part, facilitates the download of a malicious Windows dynamic-link library (DLL) that's named "propsys.dll" or "batmeter.dll."

The DLL payload – i.e., Dohdoor – is launched by means of a legitimate Windows executable (e.g., "Fondue.exe," "mblctr.exe," and "ScreenClippingHost.exe") using a technique referred to as
[DLL side-loading](https://attack.mitre.org/techniques/T1574/001/)
. The backdoored access created by the implant is used to retrieve a next-stage payload directly into the victim's memory and execute it. The payload is assessed to be a Cobalt Strike Beacon.

"The threat actor hides the C2 servers behind the Cloudflare infrastructure, ensuring that all outbound communication from the victim machine appears as legitimate HTTPS traffic to a trusted global IP address," Talos said.

"This technique bypasses DNS-based detection systems, DNS sinkholes, and network traffic analysis tools that monitor suspicious domain lookups, ensuring that the malware's C2 communications remain stealth by traditional network security infrastructure."

Dohdoor has also been found to unhook system calls to bypass endpoint detection and response (EDR) solutions that monitor Windows API calls through
[user-mode hooks in NTDLL.dll](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)
.

Raghuprasad told The Hacker News that, "the attacker had infected several educational institutions, including a university that is connected to several other institutions, indicating a potential wider attack surface. Additionally, one of the affected entities was a healthcare facility, specifically for elderly care."

Analysis of the campaign has revealed no evidence of data exfiltration to date. Although no final payloads have been observed other than what appears to be the Cobalt Strike Beacon to backdoor into the victim's environment, it's believed that UAT-10027's actions are likely driven by financial gain based on the victimology pattern, the researcher added.

There is currently no clarity on who is behind UAT-10027, but Cisco Talos said it found some tactical similarities between Dohdoor and
[LazarLoader](https://thehackernews.com/2025/03/thn-weekly-recap-router-hacks-pypi.html#:~:text=Lazarus%20Group%20Drops%20LazarLoader%20Malware)
, a
[downloader](https://s2w.inc/en/resource/detail/941)
previously identified as used by the North Korean hacking group Lazarus in attacks aimed at South Korea.

"While UAT-10027's malware shares technical overlaps with the Lazarus Group, the campaign’s focus on the education and health care sectors deviates from Lazarus' typical profile of cryptocurrency and defense targeting," Talos concluded.

"However, [...] North Korean APT actors have targeted the healthcare sector using
[Maui ransomware](https://thehackernews.com/2022/07/north-korean-maui-ransomware-actively.html)
, and another North Korean APT group,
[Kimsuky](https://thehackernews.com/2021/11/north-korean-hackers-found-behind-range.html)
, has targeted the
[education sector](https://globalcyberalliance.org/aide-data-kimsuky/)
, highlighting the overlaps in the victimology of UAT-10027 with that of other North Korean APTs."