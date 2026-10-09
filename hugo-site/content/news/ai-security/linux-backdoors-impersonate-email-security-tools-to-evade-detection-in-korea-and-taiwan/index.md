---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T21:15:15.113685+00:00'
exported_at: '2026-10-07T21:15:17.470402+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/linux-backdoors-impersonate-email.html
structured_data:
  about: []
  author: ''
  description: Linux backdoors targeting South Korea and Taiwan disguise processes
    and traffic as trusted email services to evade detection.
  headline: Linux Backdoors Impersonate Email Security Tools to Evade Detection in
    Korea and Taiwan
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/linux-backdoors-impersonate-email.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Linux Backdoors Impersonate Email Security Tools to Evade Detection in Korea
  and Taiwan
updated_at: '2026-10-07T21:15:15.113685+00:00'
url_hash: 007c3190cf2b720071dba531805f86e2c20b89e3
---

Linux backdoors targeting telecom and network appliances in South Korea and Taiwan have been disguising their traffic as email services and seemingly legitimate processes to blend in and evade detection.

Threat actors are known to name their malicious software after a legitimate operating system component or a process as a defense evasion measure. By borrowing the name of a real binary, it may make it appear less conspicuous among other Windows processes, lend it a false sense of trust, or be overlooked by an analyst during casual inspection.

However, the backdoors
[examined](https://www.rapid7.com/blog/post/tr-smtp-is-the-key-bpfdoor-averat-hitting-the-network-edge/)
by Rapid7 have been found to go beyond imitating file names by assuming the identities of email security products like
[SpamSniper](https://global.jiran.com/spamsniper)
and
[ShareTech](https://www.sharetech.com.tw/en-us/)
that are widely used in enterprise environments in South Korea and Taiwan.

According to vendor Jiran Group, SpamSniper is advertised as "Korea's leading email security solution" that defends organizations against spam, malware, and server attacks.

The malicious artifacts include a new BPFDoor variant and a BPF Rekoobe build used against South Korean targets, and a previously unreported Linux implant dubbed AVERAT that's delivered via a dropper and deployed against Taiwanese appliances.

"The BPFDoor variants seen against South Korean systems impersonate the PID file of SpamSniper, a Korean anti-spam product, and rotate through ten Linux daemon names," Rapid7 said. "Across the samples, each component adopts names and conventions designed to look unremarkable in the environment it targets."

BPFdoor and its many iterations were the subject of an
[extensive analysis](https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html)
by Rapid7 earlier this year, with the activity linked to a threat group dubbed Red Menshen (aka Earth Bluecrow, DecisiveArchitect, and Red Dev 18), which has targeted telecom providers across the Middle East and Asia going all the way back to 2021.

At a high level, BPFDoor abuses the Berkeley Packet Filter (BPF) functionality to inspect incoming network traffic and activate its behavior only upon detecting a
[magic packet](https://en.wikipedia.org/wiki/Wake-on-LAN)
. The detection of a new BPFDoor version indicates that the threat actors behind the malware are actively refining and retooling their arsenal in response to public disclosures.

"Once security vendors wrote static network signatures (Suricata/Snort) to detect these Layer 4 anomalies, the operators began targeting the edge proxies," Rapid7 said. "By wrapping the magic packet in standard HTTPS POST requests and relying on SSL offloading common in telecom environments, the trigger can be delivered to the BPFDoor-infected node in a way that may evade conventional deep packet inspection."

While some BPFDoor samples spoof SpamSniper, another artifact sets its process name to "ora\_ppmond," mimicking the naming convention associated with Oracle-backed telecom subscriber and provisioning platforms. Specifically, the name appears to be a reference to "
[ora\_pmon\_\*](https://docs.oracle.com/communications/G13327_01/doc.151/ncc_sysadmin.pdf)
," which represents the Process Monitor (PMON) background process of an Oracle Database instance.

Once triggered, the BPFDoor sample launches a TinyShell session and supports commands to facilitate interactive shell, upload, and download capabilities. Interestingly, the use of
[TinyShell](https://en.wikipedia.org/wiki/TinyShell)
has been previously attributed to China-nexus clusters like
[Liminal Panda](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html)
,
[UNC3886](https://thehackernews.com/2025/03/chinese-hackers-breach-juniper-networks.html)
(aka
[Fire Ant](https://thehackernews.com/2026/08/weekly-recap-chinese-spy-proxy-ai.html#:~:text=Fire%20Ant%20Targets%20Trusted%20Infrastructure%20in%202026)
), and
[Velvet Ant](https://thehackernews.com/2024/08/chinese-hackers-exploit-zero-day-cisco.html)
, all of which have singled out
[telecom networks and edge devices](https://www.sygnia.co/blog/operation-highland-velvet-ant/)
.

"These samples show BPFDoor operating as a modular framework that adapts to the telecom layer it targets, integrating TinyShell and Rekoobe logic to support exfiltration," Rapid7 explained.

Also observed in conjunction with the activity is a
[Rekoobe](https://thehackernews.com/2022/06/new-syslogk-linux-rootkit-lets.html)
-based BPF
[backdoor](https://intezer.com/blog/linux-rekoobe-operating-with-new-undetected-malware-samples)
that intercepts TCP/UDP/SCTP IPv4 and UDP IPv6 traffic with source and destination ports equal 25. Furthermore, it names its processes after components of SpamSniper.

The dropper observed in an overlapping campaign is an ELF binary that acts as a local installer for AVERAT, a modular implant that uses the Simple Mail Transfer Protocol (SMTP) for command-and-control (C2) and to obscure its malicious activity.

Located within the ShareTech appliance's "/addpkg/sbin/" add-on package directory, the ELF dropper works by deriving its encryption key from the string "ShareTech" and then using it to decrypt a shell script that's responsible for staging and executing two binaries: "ntpdate," which is the dropper itself, and "udevds," which is the AVERAT payload. The two files are deleted 10 seconds later.

AVERAT periodically polls a C2 server ("mx.zxopfds[.]com") over TCP port 25 every 600 to 699 seconds. The server details and beacon interval are extracted from an encrypted configuration. The backdoor supports a long list of command codes that include -

* 20, to enumerate directory contents
* 21, to download a file from the host, with resume support
* 22, to upload a file to the host in chunks
* 25, to recursively delete a file or directory tree
* 30, to recursively walk a directory tree
* 629, to enumerate running processes with command lines
* 632, to terminate a process (SIGTERM)
* 842, to overwrite the C2 host and port tables at runtime
* 912, to open an interactive shell session and up to 10 concurrent sessions
* 914, to write a command into an open shell session
* 916, to reboot the appliance
* 1010, to load or unload a shared object (\*.so) module, extending the implant functionality
* 1576, to set the callback interval and persist it to database
* 1618, to open a proxy or port-forward channel through the appliance
* unknown, to close the socket and terminate the process immediately

AVERAT's C2 infrastructure, per Rapid7, matches the device-class profile typically associated with an
[Operational Relay Box](https://www.team-cymru.com/post/an-introduction-to-operational-relay-box-orb-networks-unpatched-forgotten-and-obscured)
(
[ORB](https://thehackernews.com/2026/04/firestarter-backdoor-hit-federal-cisco.html#chinese-hackers-shift-from-individually-procured-infrastructure-to-covert-networks)
) network, although there is no evidence it's part of any known ORBs such as
[LapDogs](https://thehackernews.com/2026/07/china-linked-uat-7810-expands-orb.html)
(aka UAT-7810),
[SPACEHOP, and FLORAHOX](https://thehackernews.com/2024/05/new-frontiers-old-tactics-chinese-cyber.html)
.

Organizations are recommended to review unexpected raw packet sockets and BPF filters on Linux systems that do not require packet capture, audit outbound TCP port 25 connections from processes that are not mail services, scan for processes posing as common daemons, and restrict management access to routers, DVRs and other edge appliances.

The findings demonstrate how threat actors are leveraging the privileged position occupied by secure email gateways (SEGs) for intelligence collection. In 2023, a China-nexus threat actor codenamed UNC4841 was observed exploiting two different vulnerabilities in Barracuda Email Security Gateway (ESG) appliances (
[CVE-2023-2868](https://thehackernews.com/2023/07/hackers-deploy-submarine-backdoor-in.html)
and
[CVE-2023-7102](https://thehackernews.com/2023/12/chinese-hackers-exploited-new-zero-day.html)
) to deliver persistent backdoors.

"The common thread is regionalized disguise: each sample is aware of the vendor's software running on the targeted systems and implements process spoofing accordingly," the cybersecurity company said. "Passive BPF implants avoid conventional port scans; while outbound beacons hide inside ordinary DNS, TCP, and traffic, the threat actor(s) are leveraging SMTP to stay under the radar."