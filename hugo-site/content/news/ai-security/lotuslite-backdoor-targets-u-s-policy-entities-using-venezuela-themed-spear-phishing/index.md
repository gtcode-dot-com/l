---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-16T12:15:13.788135+00:00'
exported_at: '2026-01-16T12:15:16.014938+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html
structured_data:
  about: []
  author: ''
  description: China-linked attackers used Venezuela-themed phishing and DLL side-loading
    to deploy the LOTUSLITE backdoor against U.S. government and policy targets
  headline: LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed
    Spear Phishing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: LOTUSLITE Backdoor Targets U.S. Policy Entities Using Venezuela-Themed Spear
  Phishing
updated_at: '2026-01-16T12:15:13.788135+00:00'
url_hash: 1b425e2d3bc9b6ced1f115e8c3ceab143a31b8a6
---

**

Jan 16, 2026
**

Ravie Lakshmanan

Malware / Cyber Espionage

Security experts have disclosed details of a new campaign that has targeted U.S. government and policy entities using politically themed lures to deliver a backdoor known as
**LOTUSLITE**
.

The targeted malware campaign leverages decoys related to the
[recent geopolitical developments](https://en.wikipedia.org/wiki/2026_United_States_intervention_in_Venezuela)
between the U.S. and Venezuela to distribute a ZIP archive ("US now deciding what's next for Venezuela.zip") containing a malicious DLL that's launched using DLL side-loading techniques. It's not known if the campaign managed to successfully compromise any of the targets.

The activity has been attributed with moderate confidence to a Chinese state-sponsored group known as
[Mustang Panda](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html)
(aka Earth Pret, HoneyMyte, and Twill Typhoon), citing tactical and infrastructure patterns. It's worth noting that the threat actor is known for extensively relying on DLL side-loading to launch its backdoors, including TONESHELL.

"This campaign reflects a continued trend of targeted spear phishing using geopolitical lures, favoring reliable execution techniques such as DLL side-loading over exploit-based initial access," Acronis researchers Ilia Dafchev and Subhajeet Singha
[said](https://www.acronis.com/en/tru/posts/lotuslite-targeted-espionage-leveraging-geopolitical-themes/)
in an analysis.

The backdoor ("kugou.dll") employed in the attack, LOTUSLITE, is a bespoke C++ implant that's designed to communicate with a hard-coded command-and-control (C2) server using Windows WinHTTP APIs to enable beaconing activity, remote tasking using "cmd.exe," and data exfiltration. The complete list of supported commands is as follows -

* 0x0A, to initiate a remote CMD shell
* 0x0B, to terminate the remote shell
* 0x01, to send commands via the remote shell
* 0x06, to reset beacon state
* 0x03, to enumerate files in a folder
* 0x0D, to create an empty file
* 0x0E, to append data to a file
* 0x0F, to get beacon status

LOTUSLITE is also capable of establishing persistence by making Windows Registry modifications to ensure that it's automatically executed each time the user logs in to the system.

Acronis said the backdoor "mimics the behavioral shenanigans of Claimloader by embedding provocative messages." Claimloader is the name assigned to a DLL that's launched using DLL side-loading and is used to deploy PUBLOAD, another Mustang Panda tool. The malware was
[first documented](https://thehackernews.com/2025/06/pubload-and-pubshell-malware-used-in.html)
by IBM X-Force in June 2025 in connection with a cyber espionage campaign aimed at the Tibetan community.

"This campaign demonstrates how simple and well-tested techniques can still be effective when paired with targeted delivery and relevant geopolitical lures," the Singaporean cybersecurity company concluded. "Although the LOTUSLITE backdoor lacks advanced evasion features, its use of DLL sideloading, reliable execution flow, and basic command-and-control functionality reflects a focus on operational dependability rather than sophistication."

The disclosure comes as The New York Times
[published](https://www.nytimes.com/2026/01/15/us/politics/cyberattack-venezuela-military.html)
details about a purported cyber attack undertaken by the U.S. to disrupt electricity for most residents in the capital city of Caracas for a few minutes, before the January 3, 2026, military operation that captured Venezuelan President Nicolás Maduro. The mission

"Turning off the power in Caracas and interfering with radar allowed US military helicopters to move into the country undetected on their mission to capture Nicolás Maduro, the Venezuelan president who has now been brought to the United States to face drug charges," the Times reported.

"The attack caused most of Caracas's residents to lose their power for a few minutes, though some neighborhoods near the military base where Mr. Maduro was captured were left without electricity for up to 36 hours."