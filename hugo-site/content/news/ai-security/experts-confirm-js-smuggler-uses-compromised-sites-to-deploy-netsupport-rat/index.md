---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-09T00:03:07.236582+00:00'
exported_at: '2025-12-09T00:03:10.206316+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/experts-confirm-jssmuggler-uses.html
structured_data:
  about: []
  author: ''
  description: Researchers detail JS#SMUGGLER, a multi-stage web attack using JavaScript,
    HTA, and PowerShell to deploy NetSupport RAT on targeted systems.
  headline: Experts Confirm JS#SMUGGLER Uses Compromised Sites to Deploy NetSupport
    RAT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/experts-confirm-jssmuggler-uses.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Experts Confirm JS#SMUGGLER Uses Compromised Sites to Deploy NetSupport RAT
updated_at: '2025-12-09T00:03:07.236582+00:00'
url_hash: a7799dde22b7e86330cdaf48474f5bb1fae1acd4
---

Cybersecurity researchers are calling attention to a new campaign dubbed
**JS#SMUGGLER**
that has been observed leveraging compromised websites as a distribution vector for a remote access trojan named
[NetSupport RAT](https://thehackernews.com/2025/02/threat-actors-exploit-clickfix-to.html)
.

The attack chain, analyzed by Securonix, involves three main moving parts: An obfuscated JavaScript loader injected into a website, an HTML Application (HTA) that runs encrypted PowerShell stagers using "mshta.exe," and a PowerShell payload that's designed to download and execute the main malware.

"NetSupport RAT enables full attacker control over the victim host, including remote desktop access, file operations, command execution, data theft, and proxy capabilities," researchers Akshay Gaikwad, Shikha Sangwan, and Aaron Beardslee
[said](https://www.securonix.com/blog/jssmuggler-multi-stage-hidden-iframes-obfuscated-javascript-silent-redirectors-netsupport-rat-delivery/)
.

There is little evidence at this stage to tie the campaign to any known threat group or country. The activity has been found to target enterprise users through compromised websites, indicative of a broad-strokes effort.

The cybersecurity company described it as a multi-stage web-based malware operation that employs hidden iframes, obfuscated loaders, and layered script execution for malware deployment and remote control.

In these attacks, silent redirects embedded into the infected websites act as a conduit for a heavily scrambled JavaScript loader ("phone.js") retrieved from an external domain, which then profiles the device to determine whether to serve a full-screen iframe (when visiting from a mobile phone) or load another remote second-stage script (when visiting from a desktop).

The invisible iframe is designed to direct the victim to a malicious URL. The JavaScript loader incorporates a tracking mechanism to ensure that the malicious logic is fired only once and during the first visit, thereby minimizing the chances of detection.

"This device-aware branching enables attackers to tailor the infection path, hide malicious activity from certain environments, and maximize their success rate by delivering platform-appropriate payloads while avoiding unnecessary exposure," the researchers said.

The remote script downloaded in the first stage of the attack lays the foundation by constructing at runtime a URL from which an HTA payload is downloaded and executed using "mshta.exe." The HTA payload is another loader for a temporary PowerShell stager, which is written to disk, decrypted, and executed directly in memory to evade detection.

Furthermore, the HTA file is run stealthily by disabling all visible window elements and minimizing the application at startup. Once the decrypted payload is executed, it also takes steps to remove the PowerShell stager from disk and terminates itself to avoid leaving as much forensic trail as possible.

The primary goal of the decrypted PowerShell payload is to retrieve and deploy NetSupport RAT, granting the attacker complete control over the compromised host.

"The sophistication and layered evasion techniques strongly indicate an actively maintained, professional-grade malware framework," Securonix said. "Defenders should deploy strong CSP enforcement, script monitoring, PowerShell logging, mshta.exe restrictions, and behavioral analytics to detect such attacks effectively."

### CHAMELEON#NET Delivers Formbook Malware

The disclosure comes weeks after the company also detailed another multi-stage malspam campaign dubbed CHAMELEON#NET that uses phishing emails to deliver
[Formbook](https://thehackernews.com/2023/02/formbook-malware-spreads-via.html)
, a keylogger and information stealer. The email messages are aimed at luring victims in the National Social Security Sector into downloading a seemingly harmless archive after their credentials on a bogus webmail portal designed for this purpose.

"This campaign begins with a phishing email that tricks users into downloading a .BZ2 archive, initiating a multi-stage infection chain," Sangwan
[said](https://www.securonix.com/blog/chameleonnet-a-deep-dive-into-multi-stage-net-malware-leveraging-reflective-loading-and-custom-decryption-for-stealthy-operations/)
. "The initial payload is a heavily obfuscated JavaScript file that acts as a dropper, leading to the execution of a complex VB.NET loader. This loader uses advanced reflection and a custom conditional XOR cipher to decrypt and execute its final payload, the Formbook RAT, entirely in memory."

Specifically, the JavaScript dropper decodes and writes to disk in the %TEMP% directory two additional JavaScript files -

* svchost.js, which drops a .NET loader executable dubbed
  [DarkTortilla](https://thehackernews.com/2022/08/researchers-detail-evasive-darktortilla.html)
  ("QNaZg.exe"), a crypter that's often used to distribute next-stage payloads
* adobe.js, which drops a file named "PHat.jar," an MSI installer package that exhibits similar behavior as "svchost.js"

In this campaign, the loader is configured to decrypt and execute an embedded DLL, the Formbook malware. Persistence is achieved by adding it to the Windows startup folder to ensure that it's automatically launched upon a system reboot. Alternatively, it also manages persistence through the Windows Registry.

"The threat actors combine social engineering, heavy script obfuscation, and advanced .NET evasion techniques to successfully compromise targets," Securonix said. "The use of a custom decryption routine followed by reflective loading allows the final payload to be executed in a fileless manner, significantly complicating detection and forensic analysis."