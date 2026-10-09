---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-08T12:03:08.355791+00:00'
exported_at: '2025-12-08T12:03:10.573350+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html
structured_data:
  about: []
  author: ''
  description: MuddyWater’s UDPGangster malware uses macro phishing & UDP channels
    for remote control, data theft, payload delivery in Turkey, Israel & Azerbaijan.
  headline: MuddyWater Deploys UDPGangster Backdoor in Targeted Turkey-Israel-Azerbaijan
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MuddyWater Deploys UDPGangster Backdoor in Targeted Turkey-Israel-Azerbaijan
  Campaign
updated_at: '2025-12-08T12:03:08.355791+00:00'
url_hash: 53df54948f245f2b5780d458661c45b6178544f1
---

**

Dec 08, 2025
**

Ravie Lakshmanan

Network Security / Vulnerability

The Iranian hacking group known as
[MuddyWater](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html)
has been observed leveraging a new backdoor dubbed
**UDPGangster**
that uses the User Datagram Protocol (UDP) for command-and-control (C2) purposes.

The cyber espionage activity targeted users in Turkey, Israel, and Azerbaijan, according to a report from Fortinet FortiGuard Labs.

"This malware enables remote control of compromised systems by allowing attackers to execute commands, exfiltrate files, and deploy additional payloads – all communicated through UDP channels designed to evade traditional network defenses," security researcher Cara Lin
[said](https://www.fortinet.com/blog/threat-research/udpgangster-campaigns-target-multiple-countries)
.

The attack chain involves using spear-phishing tactics to distribute booby-trapped Microsoft Word documents that trigger the execution of a malicious payload once macros are enabled. Some of the phishing messages impersonate the Turkish Republic of Northern Cyprus Ministry of Foreign Affairs and purport to invite recipients to an online seminar titled "Presidential Elections and Results."

Attached along with the emails are a ZIP file ("seminer.zip") and a Word document ("seminer.doc"). The ZIP file also contains the same Word file, opening which users are asked to enable macros to stealthily execute embedded VBA code.

For its part, the VBA script in the dropper file is equipped to conceal any sign of malicious activity by displaying a Hebrew-language decoy image from Israeli telecommunications provider Bezeq about supposed disconnection periods in the first week of November 2025 across various cities in the country.

"The macro uses the Document\_Open() event to automatically execute, decoding Base64-encoded data from a hidden form field (UserForm1.bodf90.Text) and writing the decoded content to C:\Users\Public\ui.txt," Lin explained. "It then executes this file using the Windows API CreateProcessA, launching the UDPGangster payload."

UDPGangster establishes persistence through Windows Registry modifications and boasts of various anti-analysis checks to resist efforts made by security researchers to take it apart. This includes -

* Verifying if the process is being debugged
* Analyzing CPU configurations for sandboxes or virtual machines
* Determining if the system has less than 2048 MB of RAM
* Retrieving network adapter information to validate if the MAC address prefix matches a list of known virtual machine vendors
* Validating if the computer is part of the default Windows workgroup rather than a joined domain
* Examining running processes for tools like VBoxService.exe, VBoxTray.exe, vmware.exe, and vmtoolsd.exe
* Running Registry scans to searches for matches to known virtualization vendor identifiers, such as VBox, VMBox, QEMU, VIRTUAL, VIRTUALBOX, VMWARE, and Xen
* Searching for known sandboxing or debugging tools, and
* Ascertaining whether the file is running in an analysis environment

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/zscaler-ai-event-d)

It's only after these checks are satisfied does UDPGangster proceed to gather system information and connects to an external server ("157.20.182[.]75") over UDP port 1269 to exfiltrate collected data, run commands using "cmd.exe," transmit files, update C2 server, and drop and execute additional payloads.

"UDPGangster uses macro-based droppers for initial access and incorporates extensive anti-analysis routines to evade detection," Lin said. "Users and organizations should remain cautious of unsolicited documents, particularly those requesting macro activation."

The development comes days after ESET attributed the threat actor to attacks spanning academia, engineering, local government, manufacturing, technology, transportation, and utilities sectors in Israel that delivered another backdoor referred to as
[MuddyViper](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html)
.