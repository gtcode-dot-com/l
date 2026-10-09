---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T02:14:53.405219+00:00'
exported_at: '2026-06-09T02:14:55.108870+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/google-doubleclick-abused-in-new.html
structured_data:
  about: []
  author: ''
  description: DoubleClick redirects hide DesckVB RAT malspam, using dynamic lures
    and .NET loaders to evade detection and control hosts.
  headline: Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/google-doubleclick-abused-in-new.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google DoubleClick Abused in New Malspam Campaign to Deliver DesckVB RAT
updated_at: '2026-06-09T02:14:53.405219+00:00'
url_hash: 75183210d26fb99f4bec0b6669914427bd5b1658
---

**

Ravie Lakshmanan
**

Jun 03, 2026

Malware / Microsoft Defender

Cybersecurity researchers have flagged a new malspam campaign that makes use of Google's DoubleClick domain as a way to evade detection and ultimately deliver a remote access trojan (RAT) named
**[DesckVB RAT](https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html)**
.

"Before the victim ever reaches attacker-controlled infrastructure, the lure routes through DoubleClick, a legitimate Google-owned domain that many security tools are less likely to treat as suspicious," Huntress researchers Anna Pham and Adam Mooney
[said](https://www.huntress.com/blog/malspam-to-deskcvb-rat-delivery-chain-analysis)
in a report shared with The Hacker News.

"From there, the victim is passed into a malspam kit that personalizes itself on the fly using the victim's email address, dynamically pulling in company branding and location details to make the page feel convincing without requiring the operators to handcraft a lure for each target."

What makes this attack noteworthy is that it eliminates the need for having a bespoke kit for each targeted organization, thereby making these operations more scalable and cost-effective. The end goal of the campaign is to drop DesckVB RAT, a .NET-based trojan that has been active in the wild since February 2026.

The attack begins when an unsuspecting user opens an HTML file that's attached to a phishing email. The file triggers a meta-refresh browser redirect to a Google DoubleClick Campaign Manager click-tracking URL, from where the user is steered to another redirector, which decodes the Base64-encoded email address and leads the victim to a landing page containing a "Download PDF" button.

Clicking the button causes the server to respond with a ZIP archive that initiates the rest of the infection chain. This is achieved by means of a JavaScript loader, whose main responsibility is to retrieve and execute a .NET RAT while flying under the radar. The script extracts and runs a PowerShell script, which then fetches a .NET loader from an external server.

The loader acts as a stager that verifies it's not being analyzed, neutralizes the machine's security controls, sets up persistence, and then ultimately downloads and runs the RAT payload by using a technique called process hollowing that involves injecting the malware into Microsoft-signed processes.

Once launched, the trojan communicates with a command-and-control (C2) server over raw TCP sockets, carries out system reconnaissance, and configures Microsoft Defender exclusions. The trojan also patches Antimalware Scan Interface (
[AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)
) and Event Tracing for Windows (
[ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows)
) at the native API level at the outset in an effort to blind Windows telemetry before persistence is established on the host by setting up Run and RunOnce Registry entries, along with placing a loader responsible for launching the RAT in the user's Startup folder.

The malware comes with capabilities to extract data, run commands, and deploy additional payloads, granting the attackers full control over the infected machines, while simultaneously taking steps to fly under the radar by terminating and rebooting the machine if it detects an analysis tool or determines that it's running in a sandboxed environment.

"This is a strong reminder of why defence in depth matters," Huntress said. "Configuring a Group Policy Object (GPO) in Active Directory to force script files such as .vbs, .hta, and .js to open in Notepad by default can stop a threat actor at the very first stage, preventing additional payloads from ever being dropped."

"On the email security front, organizations should consider deploying DMARC, DKIM, and SPF records to reduce the likelihood of spoofed or malicious emails reaching end users. Beyond that, an email gateway solution capable of sandboxing attachments and links before delivery adds another meaningful layer of protection."