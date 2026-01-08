---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:28:28.663849+00:00'
exported_at: '2026-01-08T21:28:30.907383+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/whatsapp-worm-spreads-astaroth-banking.html
structured_data:
  about: []
  author: ''
  description: Astaroth banking malware is spreading in Brazil through WhatsApp messages,
    using ZIP files to steal contacts and banking credentials on Windows system
  headline: WhatsApp Worm Spreads Astaroth Banking Trojan Across Brazil via Contact
    Auto-Messaging
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/whatsapp-worm-spreads-astaroth-banking.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: WhatsApp Worm Spreads Astaroth Banking Trojan Across Brazil via Contact Auto-Messaging
updated_at: '2026-01-08T21:28:28.663849+00:00'
url_hash: 1ff4f952bb4683885dc99543568bc39619436c97
---

**

Jan 08, 2026
**

Ravie Lakshmanan

Malware / Financial Crime

Cybersecurity researchers have disclosed details of a new campaign that uses WhatsApp as a distribution vector for a Windows banking trojan called
[Astaroth](https://thehackernews.com/2025/10/astaroth-banking-trojan-abuses-github.html)
in attacks targeting Brazil.

The campaign has been codenamed
**Boto Cor-de-Rosa**
by Acronis Threat Research Unit.

"The malware retrieves the victim's WhatsApp contact list and automatically sends malicious messages to each contact to further spread the infection," the cybersecurity company
[said](https://www.acronis.com/en/tru/posts/boto-cor-de-rosa-campaign-reveals-astaroth-whatsapp-based-worm-activity-in-brazil/)
in a report shared with The Hacker News.

"While the core Astaroth payload remains written in Delphi and its installer relies on Visual Basic script, the newly added WhatsApp-based worm module is implemented entirely in Python, highlighting the threat actors' growing use of multi-language modular components."

Astaroth, also called Guildma, is a
[banking malware](https://thehackernews.com/2020/07/brazilian-banking-trojan.html)
that has been detected in the wild since 2015, primarily targeting users in Latin America, particularly Brazil, to facilitate data theft. In 2024, multiple threat clusters tracked as
[PINEAPPLE](https://thehackernews.com/2024/07/pineapple-and-fluxroot-hacker-groups.html)
and
[Water Makara](https://thehackernews.com/2024/10/astaroth-banking-malware-resurfaces-in.html)
were observed leveraging phishing emails to propagate the malware.

The use of WhatsApp as a delivery vehicle for banking trojans is a new tactic that has gained traction among threat actors targeting Brazilian users, a move fueled by the widespread use of the messaging platform in the country. Last month, Trend Micro
[detailed](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html)
Water Saci's reliance on WhatsApp to spread Maverick and a variant of Casbaneiro.

Sophos, in a report
[published](https://thehackernews.com/2025/12/weekly-recap-usb-malware-react2shell.html#:~:text=Brazil%20Hit%20by%20Banking%20Trojan%20Spread%20via%20WhatsApp%20Worm)
in November 2025, said it's tracking a multi-stage malware distribution campaign codenamed STAC3150 targeting WhatsApp users in Brazil with Astaroth. More than 95% of the impacted devices were located in Brazil, and, to a lesser extent, in the U.S. and Austria.

The activity, active since at least September 24, 2025, delivers ZIP archives containing a downloader script that retrieves a PowerShell or Python script to collect WhatsApp user data for further propagation, along with an MSI installer that deploys the trojan. The latest findings from Acronis is a continuation of this trend, where ZIP files distributed through WhatsApp messages act as a jumping-off point for the malware infection.

"When the victim extracts and opens the archive, they encounter a Visual Basic Script disguised as a benign file," the cybersecurity company said. "Executing this script triggers the download of the next-stage components and marks the beginning of the compromise."

This includes two modules -

* A Python-based propagation module that gathers the victim's WhatsApp contacts and automatically forwards a malicious ZIP file to each of them, effectively leading to the spread of the malware in a worm-like manner
* A banking module that operates in the background and continuously monitors a victim's web browsing activity, and activates when banking-related URLs are visited to harvest credentials and enable financial gain

"The malware author also implemented a built-in mechanism to track and report propagation metrics in real time," Acronis said. "The code periodically logs statistics such as the number of messages successfully delivered, the number of failed attempts, and the sending rate measured in messages per minute."