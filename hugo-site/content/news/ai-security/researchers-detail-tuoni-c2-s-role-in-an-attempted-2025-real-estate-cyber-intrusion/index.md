---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-18T16:25:44.430977+00:00'
exported_at: '2025-11-18T16:25:46.478445+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html
structured_data:
  about: []
  author: ''
  description: Researchers reveal a failed 2025 attack using Tuoni C2, steganographic
    payloads, and Teams impersonation.
  headline: Researchers Detail Tuoni C2's Role in an Attempted 2025 Real-Estate Cyber
    Intrusion
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Detail Tuoni C2's Role in an Attempted 2025 Real-Estate Cyber Intrusion
updated_at: '2025-11-18T16:25:44.430977+00:00'
url_hash: 7fb2fb606c841df740e1b34afe8a39cdb69bdf17
---

**

Nov 18, 2025
**

Ravie Lakshmanan

Malware / Social Engineering

Cybersecurity researchers have disclosed details of a cyber attack targeting a major U.S.-based real-estate company that involved the use of a nascent command-and-control (C2) and red teaming framework known as
**Tuoni**
.

"The campaign leveraged the emerging Tuoni C2 framework, a relatively new, command-and-control (C2) tool (with a free license) that delivers stealthy, in-memory payloads," Morphisec researcher Shmuel Uzan
[said](https://www.morphisec.com/blog/morphisec-thwarts-sophisticated-tuoni-c2-attack-on-us-real-estate-firm/)
in a report shared with The Hacker News.

Tuoni is advertised as an advanced C2 framework designed for security professionals, facilitating penetration testing operations, red team engagements, and security assessments. A "Community Edition" of the software is
[freely available](https://github.com/shell-dot/tuoni)
for download from GitHub. It was first released in early 2024.

The attack, per Morphisec, unfolded in mid-October 2025, with the unknown threat actor likely leveraging social engineering via
[Microsoft Teams impersonation](https://thehackernews.com/2025/06/former-black-basta-members-use.html)
for initial access. It's suspected that the attackers likely posed as trusted vendors or colleagues to deceive an employee at the company into running a PowerShell command.

The command, for its part, downloads a second PowerShell script from an external server ("kupaoquan[.]com"), which, in turn, employs steganographic tricks to conceal the next-stage payload within a bitmap image (BMP). The primary goal of the embedded payload is to extract shellcode and execute it directly in memory.

This results in the execution of "TuoniAgent.dll," which corresponds to an
[agent](https://docs.shelldot.com/HowToUse/Terminology.html)
that operates within the targeted machine and connects to a C2 server (in this case, "kupaoquan[.]com"), allowing for remote control.

"While Tuoni itself is a sophisticated but traditional C2 framework, the delivery mechanism showed signs of AI assistance in code generation, evident from the scripted comments and modular structure of the initial loader," Morphisec added.

The attack, although ultimately unsuccessful, demonstrates continued abuse of red teaming tools for malicious purposes. In September 2025, Check Point
[detailed](https://thehackernews.com/2025/09/threat-actors-weaponize-hexstrike-ai-to.html)
the use of an artificial intelligence (AI)-powered tool called HexStrike AI to rapidly accelerate and simplify vulnerability exploitation.