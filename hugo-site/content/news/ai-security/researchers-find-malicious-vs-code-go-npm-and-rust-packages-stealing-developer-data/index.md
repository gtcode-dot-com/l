---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-09T12:03:07.905782+00:00'
exported_at: '2025-12-09T12:03:10.139897+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/researchers-find-malicious-vs-code-go.html
structured_data:
  about: []
  author: ''
  description: Researchers found malicious VS Code extensions and Go, npm, and Rust
    packages stealing developer data via hidden payloads and exfiltration.
  headline: Researchers Find Malicious VS Code, Go, npm, and Rust Packages Stealing
    Developer Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/researchers-find-malicious-vs-code-go.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Find Malicious VS Code, Go, npm, and Rust Packages Stealing Developer
  Data
updated_at: '2025-12-09T12:03:07.905782+00:00'
url_hash: aa1a8e1cef8c32fb7e81e51ff71d62f0f4c0991e
---

**

Dec 09, 2025
**

Ravie Lakshmanan

Malware / Threat Analysis

Cybersecurity researchers have discovered two new extensions on Microsoft Visual Studio Code (VS Code) Marketplace that are designed to infect developer machines with stealer malware.

The VS Code extensions masquerade as a premium dark theme and an artificial intelligence (AI)-powered coding assistant, but, in actuality, harbor covert functionality to download additional payloads, take screenshots, and siphon data. The captured information is then sent to an attacker-controlled server.

"Your code. Your emails. Your Slack DMs. Whatever's on your screen, they're seeing it too," Koi Security's Idan Dardikman
[said](https://www.koi.ai/blog/the-vs-code-malware-that-captures-your-screen)
. "And that's just the start. It also steals your WiFi passwords, reads your clipboard, and hijacks your browser sessions."

The names of the extensions are below -

* BigBlack.bitcoin-black (16 installs) - Removed by Microsoft on December 5, 2025
* BigBlack.codo-ai (25 installs) - Removed by Microsoft on December 8, 2025

Microsoft's list of removed extensions from the Marketplace
[shows](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md)
that the company also removed a third package named "BigBlack.mrbigblacktheme" from the same publisher for containing malware.

While "BigBlack.bitcoin-black" activates on every VS Code action, Codo AI embeds its malicious functionality within a working tool, thereby allowing it to bypass detection.

Earlier versions of the extensions came with the ability to execute a PowerShell script to download a password-protected ZIP archive from an external server ("syn1112223334445556667778889990[.]org") and extract from it the main payload using four different methods: Windows native Expand-Archive, .NET System.IO.Compression, DotNetZip, and 7-Zip (if installed).

That said, the attacker is said to have inadvertently shipped a version that created a visible PowerShell window and could have alerted the user. Subsequent iterations, however, have been found to hide the window and streamline the entire process by switching to a batch script that uses a curl command to download the executable and DLL.

The executable is the legitimate Lightshot binary that's used to load the rogue DLL ("Lightshot.dll") via DLL hijacking, which proceeds to gather clipboard contents, a list of installed apps, running processes, desktop screenshots, stored Wi-Fi credentials, and detailed system information. It also launches Google Chrome and Microsoft Edge in headless mode to grab stored cookies and hijack user sessions.

"A developer could install what looks like a harmless theme or a useful AI tool, and within seconds their WiFi passwords, clipboard contents, and browser sessions are being exfiltrated to a remote server," Dardikman said.

The disclosure comes as Socket said it identified malicious packages across the Go, npm, and Rust ecosystems that are capable of harvesting sensitive data -

* Go packages named "github[.]com/bpoorman/uuid" and "github[.]com/bpoorman/uid" that have been available since 2021 and typosquat trusted UUID libraries ("github[.]com/google/uuid" and "github[.]com/pborman/uuid") to
  [exfiltrate data](https://socket.dev/blog/malicious-go-packages-impersonate-googles-uuid-library-and-exfiltrate-data)
  to a paste site called dpaste when an application explicitly invokes a supposed helper function named "valid" along with the information to be validated.
* A set of
  [420 unique npm packages](https://socket.dev/blog/elves-on-npm)
  published by a likely French-speaking threat actor that follows a consistent naming pattern including "elf-stats-\*," some of which contain code to execute a reverse shell and exfiltrate files to a Pipedream endpoint.
* A Rust crate named finch-rust published by faceless, that
  [impersonates](https://socket.dev/blog/malicious-crate-mimicking-finch-exfiltrates-credentials)
  the legitimate bioinformatics tool "finch" and serves as a loader for a malicious payload through a credential-stealing package known as "sha-rust" when a developer uses the library's sketch serialization functionality.

"Finch-rust acts as a malware loader; it contains mostly legitimate code copied from the legitimate finch package but includes a single malicious line that loads and executes the sha-rust payload," Socket researcher Kush Pandya said. "This separation of concerns makes detection harder: finch-rust looks benign in isolation, while sha-rust contains the actual malware."