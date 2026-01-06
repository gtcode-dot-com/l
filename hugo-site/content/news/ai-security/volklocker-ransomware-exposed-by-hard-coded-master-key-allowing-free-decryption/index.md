---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-16T00:03:28.161133+00:00'
exported_at: '2025-12-16T00:03:30.894113+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/volklocker-ransomware-exposed-by-hard.html
structured_data:
  about: []
  author: ''
  description: Cybersecurity, Ransomware, Malware, Encryption, Cybercrime, Linux,
    Windows, Telegram, Data Recovery
  headline: VolkLocker Ransomware Exposed by Hard-Coded Master Key Allowing Free Decryption
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/volklocker-ransomware-exposed-by-hard.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: VolkLocker Ransomware Exposed by Hard-Coded Master Key Allowing Free Decryption
updated_at: '2025-12-16T00:03:28.161133+00:00'
url_hash: da5f1a8e42b1342347a86c6c4002a66e23981029
---

**

Dec 15, 2025
**

Ravie Lakshmanan

Ransomware / Cybercrime

The pro-Russian hacktivist group known as
**[CyberVolk](https://thehackernews.com/2024/12/thn-recap-top-cybersecurity-threats.html#:~:text=CyberVolk%2C%20a%20Pro%2DRussian%20Hacktivist%20Collective%20Originating%20from%20India)**
(aka GLORIAMIST) has resurfaced with a new ransomware-as-a-service (RaaS) offering called VolkLocker that suffers from implementation lapses in test artifacts, allowing users to decrypt files without paying an extortion fee.

According to SentinelOne, VolkLocker (aka CyberVolk 2.x) emerged in August 2025 and is capable of targeting both Windows and Linux systems. It's written in Golang.

"Operators building new VolkLocker payloads must provide a bitcoin address, Telegram bot token ID, Telegram chat ID, encryption deadline, desired file extension, and self-destruct options," security researcher Jim Walter
[said](https://www.sentinelone.com/labs/cybervolk-a-deep-dive-into-the-hacktivists-tools-and-ransomware-fueling-pro-russian-cyber-attacks/)
in a report published last week.

Once launched, the ransomware attempts to escalate privileges, performs reconnaissance and system enumeration, including checking local MAC address prefixes against known virtualization vendors like Oracle and VMware. In the next stage, it lists all available drives and determines the files to be encrypted based on the embedded configuration.

VolkLocker uses AES-256 in Galois/Counter Mode (
[GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode)
) for encryption through Golang's "crypto/rand" package. Every encrypted file is assigned a custom extension such as .locked or .cvolk.

However, an analysis of the test samples has uncovered a fatal flaw where the locker's master keys are not only hard-coded in the binaries, but are also used to encrypt all files on a victim system. More importantly, the master key is also written to a plaintext file in the %TEMP% folder ("C:\Users\AppData\Local\Temp\system\_backup.key").

Since this backup key file is never deleted, the design blunder enables self-recovery. That said, VolkLocker has all the hallmarks typically associated with a ransomware strain. It makes Windows Registry modifications to thwart recovery and analysis, deletes volume shadow copies, and terminates processes associated with Microsoft Defender Antivirus and other common analysis tools.

However, where it stands out is in the use of an enforcement timer, which wipes the content of user folders, viz. Documents, Desktop, Downloads, and Pictures, if victims fail to pay within 48 hours or enter the wrong decryption key three times.

CyberVolk's RaaS operations are managed through Telegram, costing prospective customers between $800 and $1,100 for either a Windows or Linux version, or between $1,600 and $2,200 for both operating systems. VolkLocker payloads come with built-in Telegram automation for command-and-control, allowing users to message victims, initiate file decryption, list active victims, and get system information.

As of November 2025, the threat actors have advertised a remote access trojan and keylogger, both priced at $500 each, indicating a broadening of their monetization strategy.

CyberVolk launched its own RaaS in June 2024. Known for conducting distributed denial-of-service (DDoS) and ransomware attacks on public and government entities to support Russian government interests, it's
[believed to be of Indian origin](https://threatmon.io/cybervolk-ransomware-technical-malware-analysis/)
.

"Despite repeated Telegram account bans and channel removals throughout 2025, CyberVolk has reestablished its operations and expanded its service offerings," Walter said. "Defenders should see CyberVolk's adoption of Telegram-based automation as a reflection of broader trends among politically-motivated threat actors. These groups continue to lower barriers for ransomware deployment while operating on platforms that provide convenient infrastructure for criminal services."