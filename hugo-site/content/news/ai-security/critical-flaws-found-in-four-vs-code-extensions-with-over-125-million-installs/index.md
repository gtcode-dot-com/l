---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-27T06:25:15.931587+00:00'
exported_at: '2026-02-27T06:25:18.598748+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/critical-flaws-found-in-four-vs-code.html
structured_data:
  about: []
  author: ''
  description: Critical vulnerabilities in four widely used VS Code extensions could
    enable file theft and remote code execution across 125M installs.
  headline: Critical Flaws Found in Four VS Code Extensions with Over 125 Million
    Installs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/critical-flaws-found-in-four-vs-code.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Critical Flaws Found in Four VS Code Extensions with Over 125 Million Installs
updated_at: '2026-02-27T06:25:15.931587+00:00'
url_hash: 52e8332101260ed08172b97be3eab6abfaee5b32
---

**

Ravie Lakshmanan
**

Feb 18, 2026

Vulnerability / Software Security

Cybersecurity researchers have disclosed multiple security vulnerabilities in four popular Microsoft Visual Studio Code (VS Code) extensions that, if successfully exploited, could allow threat actors to steal local files and execute code remotely.

The extensions, which have been collectively installed more than 125 million times, are Live Server, Code Runner, Markdown Preview Enhanced, and Microsoft Live Preview.

"Our research demonstrates that a hacker needs only one malicious extension, or a single vulnerability within one extension, to perform lateral movement and compromise entire organizations," OX Security researchers Moshe Siman Tov Bustan and Nir Zadok
[said](https://www.ox.security/blog/four-vulnerabilities-expose-a-massive-security-blind-spot-in-ide-extensions/)
in a report shared with The Hacker News.

Details of the vulnerabilities are as follows -

* **[CVE-2025-65717](https://www.ox.security/blog/cve-2025-65717-live-server-vscode-vulnerability/)**
  (CVSS score: 9.1) - A vulnerability in Live Server that allows attackers to exfiltrate local files, tricking a developer into visiting a malicious website when the extension is running, causing JavaScript embedded in the page to crawl and extract files from the local development HTTP server that runs at localhost:5500, and transmit them to a domain under their control. (Remains unpatched)
* **[CVE-2025-65716](https://www.ox.security/blog/cve-2025-65716-markdown-preview-enhanced-vscode-vulnerability/)**
  (CVSS score: 8.8) - A vulnerability in Markdown Preview Enhanced that allows attackers to execute arbitrary JavaScript code by uploading a crafted markdown (.md) file, allowing local port enumeration and exfiltration to a domain under their control. (Remains unpatched)
* **[CVE-2025-65715](https://www.ox.security/blog/cve-2025-65715-code-runner-vscode-rce/)**
  (CVSS score: 7.8) - A vulnerability in Code Runner that allows attackers to execute arbitrary code by convincing a user to alter the "settings.json" file through phishing or social engineering. (Remains unpatched)
* A
  [vulnerability in Microsoft Live Preview](https://www.ox.security/blog/xssinlivepreview/)
  allows attackers to access sensitive files on a developer's machine by tricking a victim into visiting a malicious website when the extension is running, which then enables specially crafted JavaScript requests targeting the localhost to enumerate and exfiltrate sensitive files. (No CVE, Fixed silently by Microsoft in
  [version 0.4.16](https://github.com/microsoft/vscode-livepreview/blob/main/CHANGELOG.md)
  released in September 2025)

VIDEO

To secure the development environment, it's essential to avoid applying untrusted configurations, disable or uninstall non-essential extensions, harden the local network behind a firewall to restrict inbound and outbound connections, periodically update extensions, and turn off localhost-based services when not in use.

"Poorly written extensions, overly permissive extensions, or malicious ones can execute code, modify files, and allow attackers to take over a machine and exfiltrate information," OX Security said. "Keeping vulnerable extensions installed on a machine is an immediate threat to an organization's security posture: it may take only one click, or a downloaded repository, to compromise everything."