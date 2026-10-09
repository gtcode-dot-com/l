---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-25T12:32:07.968472+00:00'
exported_at: '2025-11-25T12:32:10.160120+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html
structured_data:
  about: []
  author: ''
  description: ToddyCat upgrades tools like TCSectorCopy and TomBerBil to steal corporate
    email and browser data, targeting Outlook and Microsoft 365 defenses.
  headline: ToddyCat’s New Hacking Tools Steal Outlook Emails and Microsoft 365 Access
    Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: ToddyCat’s New Hacking Tools Steal Outlook Emails and Microsoft 365 Access
  Tokens
updated_at: '2025-11-25T12:32:07.968472+00:00'
url_hash: 3676b325575dc68c1068a3bbe076b17a97c9581f
---

**

Nov 25, 2025
**

Ravie Lakshmanan

Malware / Vulnerability

The threat actor known as
**ToddyCat**
has been observed adopting new methods to obtain access to corporate email data belonging to target companies, including using a custom tool dubbed TCSectorCopy.

"This attack allows them to obtain tokens for the OAuth 2.0 authorization protocol using the user's browser, which can be used outside the perimeter of the compromised infrastructure to access corporate mail," Kaspersky
[said](https://securelist.ru/toddycat-apt-steals-email-data-from-outlook/114045/)
in a technical breakdown.

ToddyCat, assessed to be active since 2020, has a
[track record](https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html)
of targeting various organizations in Europe and Asia with various tools, Samurai and TomBerBil to retain access and steal cookies and credentials from web browsers like Google Chrome and Microsoft Edge.

Earlier this April, the hacking group was
[attributed](https://thehackernews.com/2025/04/new-tcesb-malware-found-in-active.html)
to the exploitation of a security flaw in ESET Command Line Scanner (CVE-2024-11859, CVSS score: 6.8) to deliver a previously undocumented malware codenamed TCESB.

Kaspersky said it detected a PowerShell variant of TomBerBil (as opposed to C++ and C# versions flagged before) in attacks that took place between May and June 2024, which comes with capabilities to extract data from Mozilla Firefox. A notable feature of this version is that it runs on domain controllers from a privileged user and can access browser files via shared network resources using the SMB protocol.

The malware, the company added, was launched by means of a scheduled task that executed a PowerShell command. Specifically, it searches for browser history, cookies, and saved credentials in the remote host over SMB. While the copied files containing the information are encrypted using the Windows Data Protection API (
[DPAPI](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
), TomBerBil is equipped to capture the encryption key necessary to decrypt the data.

"The previous version of TomBerBil ran on the host and copied the user token. As a result, DPAPI was used to decrypt the master key in the user's current session, and subsequently the files themselves," researchers said. "In the newer server version, TomBerBil copies files containing user encryption keys that are used by DPAPI. Using these keys, as well as the user's SID and password, attackers can decrypt all copied files locally."

The threat actors have also been found to access corporate emails stored in local Microsoft Outlook storage in the form of OST (short for Offline Storage Table) files using TCSectorCopy ("xCopy.exe"), bypassing restrictions that limit access to such files when the application is running.

Written in C++, TCSectorCopy accepts as input a file to be copied (in this case, OST files) and then proceeds to open the disk as a read-only device and sequentially copy the file contents sector by sector. Once the OST files are written to a path of the attacker's choosing, the contents of the electronic correspondence are extracted using
[XstReader](https://github.com/Dijji/XstReader)
, an open-source viewer for Outlook OST and PST files.

Another tactic adopted by ToddyCat involves efforts to obtain access tokens directly from memory in cases where victim organizations used the Microsoft 365 cloud service. The JSON web tokens (JWTs) are obtained through an open-source C# tool named
[SharpTokenFinder](https://github.com/HuskyHacks/SharpTokenFinder)
, which enumerates Microsoft 365 applications for plain text authentication tokens.

But the threat actor is said to have faced a setback in at least one investigated incident after security software installed on the system blocked SharpTokenFinder's attempt to dump the Outlook.exe process. To get around this restriction, the operator used the
[ProcDump](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)
tool from the Sysinternals package with specific arguments to take a memory dump of the Outlook process.

"The ToddyCat APT group is constantly developing its techniques and looking for those that would hide activity to gain access to corporate correspondence within the compromised infrastructure," Kaspersky said.