---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-21T12:14:07.482896+00:00'
exported_at: '2025-11-21T12:14:09.701112+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/apt24-deploys-badaudio-in-years-long.html
structured_data:
  about: []
  author: ''
  description: APT24 and Autumn Dragon launch multi-year espionage campaigns using
    BADAUDIO, supply chain attacks, and new CVE-2025-8088 exploits.
  headline: APT24 Deploys BADAUDIO in Years-Long Espionage Hitting Taiwan and 1,000+
    Domains
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/apt24-deploys-badaudio-in-years-long.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: APT24 Deploys BADAUDIO in Years-Long Espionage Hitting Taiwan and 1,000+ Domains
updated_at: '2025-11-21T12:14:07.482896+00:00'
url_hash: 5cdb680a1b31fbf663499ec22d78832b195e3f4c
---

A China-nexus threat actor known as
**APT24**
has been observed using a previously undocumented malware dubbed BADAUDIO to establish persistent remote access to compromised networks as part of a nearly three-year campaign.

"While earlier operations relied on broad strategic web compromises to compromise legitimate websites, APT24 has recently pivoted to using more sophisticated vectors targeting organizations in Taiwan," Google Threat Intelligence Group (GTIG) researchers Harsh Parashar, Tierra Duncan, and Dan Perez
[said](https://cloud.google.com/blog/topics/threat-intelligence/apt24-pivot-to-multi-vector-attacks/)
[said](https://cloud.google.com/security/resources/insights/apt-groups)
.

"This includes the repeated compromise of a regional digital marketing firm to execute supply chain attacks and the use of targeted phishing campaigns."

APT24, also called Pitty Tiger, is the moniker
[assigned](https://web.archive.org/web/20240921024940/https://cyber.airbus.com/the-eye-of-the-tiger/)
to a suspected Chinese hacking group that has targeted government, healthcare, construction and engineering, mining, nonprofit, and telecommunications sectors in the U.S. and Taiwan.

According to a July 2014 report from FireEye, the adversary is
[believed](https://web.archive.org/web/20220517174055/https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html)
to be active as early as 2008, with the attacks leveraging pushing emails to trick recipients into opening Microsoft Office documents that, in turn, exploit known security flaws in the software (e.g.,
[CVE-2012-0158](https://nvd.nist.gov/vuln/detail/cve-2012-0158)
and
[CVE-2014-1761](https://nvd.nist.gov/vuln/detail/cve-2014-1761)
) to infect systems with malware.

Some of the malware families associated with APT24 include CT RAT, a variant of
[Enfal/Lurid Downloader](https://unit42.paloaltonetworks.com/cmstar-downloader-lurid-and-enfals-new-cousin/)
called MM RAT (aka Goldsun-B), and variants of Gh0st RAT known as Paladin RAT and Leo RAT. Another notable malware put to use by the threat actor is a backdoor named
[Taidoor](https://thehackernews.com/2020/08/chinese-hacking-malware.html)
(aka Roudan).

APT24 is assessed to be closely related to another advanced persistent threat (APT) group called Earth Aughisky, which has also deployed Taidoor in its campaigns and has leveraged infrastructure previously attributed to APT24 as part of attacks distributing another backdoor referred to as Specas.

Both the malware strains, per an
[October 2022 report](https://thehackernews.com/2022/10/researchers-detail-malicious-tools-used.html)
from Trend Micro, are designed to read proxy settings from a specific file "%systemroot%\\system32\\sprxx.dll."

The latest findings from GTIG show that the BADAUDIO campaign has been underway since November 2022, with the attackers using watering holes, supply chain compromises, and spear-phishing as initial access vectors.

A highly obfuscated malware written in C++, BADAUDIO uses
[control flow flattening](https://news.sophos.com/en-us/2022/05/04/attacking-emotets-control-flow-flattening/)
to resist reverse engineering and acts as a first-stage downloader that's capable of downloading, decrypting, and executing an AES-encrypted payload from a hard-coded command and control (C2) server. It works by gathering and exfiltrating basic system information to the server, which responds with the payload to be run on the host. In one case, it was a Cobalt Strike Beacon.

|  |
| --- |
|  |
| BADAUDIO campaign overview |

"BADAUDIO typically manifests as a malicious Dynamic Link Library (DLL) leveraging DLL Search Order Hijacking (MITRE ATT&CK T1574.001) for execution via legitimate applications," GTIG said. "Recent variants observed indicate a refined execution chain: encrypted archives containing BADAUDIO DLLs along with VBS, BAT, and LNK files."

From November 2022 to at least early September 2025, APT24 is estimated to have compromised more than 20 legitimate websites to inject malicious JavaScript code to specifically exclude visitors coming from macOS, iOS, and Android, generate a unique browser fingerprint using the FingerprintJS library, and serve them a fake pop-up urging them to download BADAUDIO under the guise of a Google Chrome update.

Then, starting in July 2024, the hacking group breached a regional digital marketing firm in Taiwan to orchestrate a supply chain attack by injecting the malicious JavaScript into a widely used JavaScript library that the company distributed, effectively allowing it to hijack more than 1,000 domains.

The modified third-party script is configured to reach out to a typosquatted domain impersonating a legitimate Content Delivery Network (CDN) and fetch the attacker-controlled JavaScript to fingerprint the machine and then serve the pop-up to download BADAUDIO after validation.

"The compromise in June 2025 initially employed conditional script loading based on a unique web ID (the specific domain name) related to the website using the compromised third-party scripts," Google said. "This suggests tailored targeting, limiting the strategic web compromise (MITRE ATT&CK T1189) to a single domain."

|  |
| --- |
|  |
| Compromised JS supply chain attack to deliver BADAUDIO malware |

"However, for a ten-day period in August, the conditions were temporarily lifted, allowing all 1,000 domains using the scripts to be compromised before the original restriction was reimposed."

APT24 has also been observed conducting targeted phishing attacks since August 2024, using lures related to an animal rescue organization to trick recipients into responding and ultimately deliver BADAUDIO via encrypted archives hosted on Google Drive and Microsoft OneDrive. These messages come fitted with tracking pixels to confirm whether the emails were opened by the targets and tailor their efforts accordingly.

"The use of advanced techniques like supply chain compromise, multi-layered social engineering, and the abuse of legitimate cloud services demonstrates the actor's capacity for persistent and adaptive espionage," Google said.

### China-nexus APT Group Targets Southeast Asia

The disclosure comes as CyberArmor
[detailed](https://cyberarmor.tech/blog/autumn-dragon-china-nexus-apt-group-targets-south-east-asia)
a sustained espionage campaign orchestrated by a suspected China-nexus threat actor against government, media, and news sectors in Laos, Cambodia, Singapore, the Philippines, and Indonesia. The activity has been codenamed
**Autumn Dragon**
.

The attack chain commences with a RAR archive likely sent as an attachment in spear-phishing messages that, when extracted, exploits a WinRAR security flaw (
[CVE-2025-8088](https://thehackernews.com/2025/08/winrar-zero-day-under-active.html)
, CVSS score: 8.8) to launch a batch script ("Windows Defender Definition Update.cmd") that sets up persistence to ensure that the malware is launched automatically when the user logs in to the system the next time.

It also downloads a second RAR archive hosted on Dropbox via PowerShell. The RAR archive contains two files, a legitimate executable ("obs-browser-page.exe") and a malicious DLL ("libcef.dll"). The batch script then runs the binary to sideload the DLL, which then communicates with the threat actor over Telegram to fetch commands ("shell"), capture screenshots ("screenshot"), and drop additional payloads ("upload").

"The bot controller (threat actor) uses these three commands to gather information and perform reconnaissance of the victim's computer and deploy third-stage malware," security researchers Nguyen Nguyen and BartBlaze said. "This design enables the controller to remain stealthy and evade detection."

The third stage once again involves the use of DLL side-loading to launch a rogue DLL ("CRClient.dll") by using a real binary ("Creative Cloud Helper.exe"), which then decrypts and runs shellcode responsible for loading and executing the final payload, a lightweight implant written in C++ that can communicate with a remote server ("public.megadatacloud[.]com") and supports eight different commands -

* 65, to run a specified command using "cmd.exe," gather the result, and exfiltrate it back to the C2 server
* 66, to load and execute a DLL
* 67, to execute shellcode
* 68, to update configuration
* 70, to read a file supplied by the operator
* 71, to open a file and write the content supplied by the operator
* 72, to get/set the current directory
* 73, to sleep for a random interval and terminate itself

While the activity has not been tied to a specific threat actor or group, it's possibly the work of a China-nexus group possessing intermediate operational capabilities. This assessment is based on the adversary's continued targeting of countries surrounding
[the South China Sea](https://thehackernews.com/2025/09/chinese-apt-deploys-eggstreme-fileless.html)
.

"The attack campaign is targeted," the researchers said. "Throughout our analysis, we frequently observed the next stages being hosted behind Cloudflare, with geo-restrictions enabled, as well as other restrictions such as only allowing specific HTTP User Agents."