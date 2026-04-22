---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-22T10:15:13.969208+00:00'
exported_at: '2026-04-22T10:15:16.409939+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/mustang-pandas-new-lotuslite-variant.html
structured_data:
  about: []
  author: ''
  description: Updated LOTUSLITE targets India banking sector via CHM and DLL side-loading,
    expanding espionage campaign to South Korea and U.S. policy circles.
  headline: Mustang Panda’s New LOTUSLITE Variant Targets India Banks, South Korea
    Policy Circles
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/mustang-pandas-new-lotuslite-variant.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Mustang Panda’s New LOTUSLITE Variant Targets India Banks, South Korea Policy
  Circles
updated_at: '2026-04-22T10:15:13.969208+00:00'
url_hash: 77ebf2e764d9f10abd71977e4f1fadae480c10b6
---

**

Ravie Lakshmanan
**

Apr 22, 2026

Cyber Espionage / Malware

Cybersecurity researchers have discovered a new variant of a known malware called
**LOTUSLITE**
that's distributed via a theme related to India's banking sector.

"The backdoor communicates with a dynamic DNS-based command-and-control server over HTTPS and supports remote shell access, file operations, and session management, indicating a continued espionage-focused capability set rather than financially motivated objectives," Acronis researchers Subhajeet Singha and Santiago Pontiroli
[said](https://www.acronis.com/en/tru/posts/same-packet-different-magic-mustang-panda-hits-indias-banking-sector-and-korea-geopolitics/)
in an analysis.

The use of LOTUSLITE was
[previously observed](https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html)
in spear-phishing attacks targeting U.S. government and policy entities using decoys associated with the geopolitical developments between the U.S. and Venezuela. The activity was attributed with medium confidence to a Chinese nation-state group tracked as Mustang Panda.

The latest activity flagged by Acronis involves deploying an evolved version of LOTUSLITE that demonstrates "incremental improvements" over its predecessor, indicating that the malware is being actively maintained and refined by its operators.

The deviation from the prior attack wave relates to a geographic pivot that focuses mainly on the banking sector of India, while keeping the rest of the operational playbook mostly intact. The starting point of the attack is a Compiled HTML (CHM) file embedding the malicious payloads – a legitimate executable and a rogue DLL – along with an HTML page that contains a pop-up which prompts the user to click "Yes."

This step is designed to silently retrieve and execute a JavaScript malware from a remote server ("cosmosmusic[.]com"), whose primary responsibility is to extract and run the malware contained inside the CHM file using
[DLL side-loading](https://techzone.bitdefender.com/en/tech-explainers/what-is-dll-sideloading.html)
. The DLL ("dnx.onecore.dll") is an updated version of LOTUSLITE that communicates with the domain "editor.gleeze[.]com" to receive commands and exfiltrate data of interest.

Further analysis of the campaign has uncovered similar artifacts designed to target South Korean entities, specifically individuals within the policy and diplomatic community.

"We believe that the group had been targeting certain entities belonging to the South Korean and U.S. diplomatic and policy communities, specifically those involved in Korean peninsula affairs, North Korea policy discussions and Indo-Pacific security dialogues," Acronis said.

"What stands out is the broadening of the group's targeting, from U.S. government entities with geopolitical lures, to India's banking sector through implants embedded with HDFC Bank references and pop-ups masquerading as legitimate banking software, and now to South Korean and U.S. policy circles through the impersonation of a prominent figure in Korean peninsula diplomacy, delivered via spoofed Gmail accounts and Google Drive staging."